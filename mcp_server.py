"""
MCP server: Salesforce documentation semantic search.

Transports
----------
stdio            (default) — local subprocess, no auth needed.
streamable-http  — network server with Bearer token auth (recommended for remote).
sse              — legacy SSE transport, use streamable-http instead.

Environment variables (set in .env):
    PG_CONNECTION_STRING        postgresql://user:pass@host:5432/dbname
    GEMINI_EMBEDDING_API_TOKEN  your Gemini API key
    MCP_TRANSPORT               "stdio" (default) | "streamable-http" | "sse"
    MCP_HOST                    bind host (default: 0.0.0.0)
    MCP_PORT                    bind port (default: 8000)
    MCP_API_TOKEN               bearer token required for remote transports
"""

import os
import sys
import psycopg2
import uvicorn
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.responses import Response

from gemini_embed import EMBEDDING_DIM, get_embedding

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

TRANSPORT = os.getenv("MCP_TRANSPORT", "stdio")
HOST      = os.getenv("MCP_HOST", "0.0.0.0")
PORT      = int(os.getenv("MCP_PORT", "8000"))
API_TOKEN = os.getenv("MCP_API_TOKEN", "")


def embed_query(text: str) -> list[float]:
    return get_embedding(text, "RETRIEVAL_QUERY")


# ── PostgreSQL ────────────────────────────────────────────────────────────────

def vec_literal(v: list[float]) -> str:
    return "[" + ",".join(f"{x:.8f}" for x in v) + "]"


def semantic_search(embedding: list[float], table: str, k: int, min_sim: float):
    guide = table.replace("_chunks", "")
    conn = psycopg2.connect(os.environ["PG_CONNECTION_STRING"])
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT breadcrumb, heading, text, similarity "
                f"FROM search_{guide}(%s::vector, %s, %s);",
                (vec_literal(embedding), k, min_sim),
            )
            return cur.fetchall()
    finally:
        conn.close()


# ── MCP definition ────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="sf-docs",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
    instructions=(
        "Use the appropriate search tool based on what the user is asking about:\n"
        "- search_apex_docs  → Apex (server-side code, triggers, classes, SOQL, governors)\n"
        "- search_lwc_docs   → Lightning Web Components (client-side UI, HTML templates, JS)\n"
        "- search_aura_docs  → Aura Components (legacy Lightning framework)"
    ),
)


def _search(table: str, query: str, k: int) -> str:
    k = min(k, 10)
    rows = semantic_search(embed_query(query), table, k, min_sim=0.3)
    if not rows:
        return "No relevant documentation found. Try rephrasing the query."
    parts = [
        f"## Result {i} — {breadcrumb}\n**Similarity:** {sim:.2f}\n\n{text}"
        for i, (breadcrumb, _, text, sim) in enumerate(rows, 1)
    ]
    return "\n\n---\n\n".join(parts)


@mcp.tool()
def search_apex_docs(query: str, k: int = 5) -> str:
    """
    Search the Salesforce Apex Developer Guide.
    Use for: Apex syntax, classes, triggers, SOQL/SOSL, governor limits,
    async Apex, batch jobs, platform events, testing.

    Args:
        query: Question or keyword phrase about Apex.
        k:     Number of results (default 5, max 10).
    """
    return _search("apex_chunks", query, k)


@mcp.tool()
def search_lwc_docs(query: str, k: int = 5) -> str:
    """
    Search the Lightning Web Components (LWC) Developer Guide.
    Use for: LWC component lifecycle, HTML templates, JS controllers,
    wire service, events, navigation, testing with Jest.

    Args:
        query: Question or keyword phrase about LWC.
        k:     Number of results (default 5, max 10).
    """
    return _search("lwc_chunks", query, k)


@mcp.tool()
def search_aura_docs(query: str, k: int = 5) -> str:
    """
    Search the Aura Components Developer Guide.
    Use for: Aura component bundle structure, controllers, helpers,
    renderers, events, force: and lightning: namespaces.

    Args:
        query: Question or keyword phrase about Aura.
        k:     Number of results (default 5, max 10).
    """
    return _search("aura_chunks", query, k)


# ── Auth middleware ───────────────────────────────────────────────────────────

class BearerTokenMiddleware:
    """Pure ASGI middleware — compatible with streaming responses."""

    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] == "http":
            path = scope.get("path", "")
            # Allow OAuth discovery endpoints without auth
            if not path.startswith("/.well-known"):
                headers = dict(scope.get("headers", []))
                auth = headers.get(b"authorization", b"").decode()
                token = auth.removeprefix("Bearer ").strip()
                if token != API_TOKEN:
                    response = Response("Unauthorized", status_code=401, media_type="text/plain")
                    await response(scope, receive, send)
                    return
        await self.app(scope, receive, send)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if TRANSPORT in ("sse", "streamable-http"):
        if not API_TOKEN:
            print(f"ERROR: MCP_API_TOKEN must be set for {TRANSPORT} transport.", file=sys.stderr)
            sys.exit(1)

        if TRANSPORT == "streamable-http":
            app = mcp.streamable_http_app()
            print(f"Starting MCP streamable-http server on {HOST}:{PORT}/mcp")
        else:
            app = mcp.sse_app()
            print(f"Starting MCP SSE server on {HOST}:{PORT}/sse")

        app.add_middleware(BearerTokenMiddleware)
        uvicorn.run(app, host=HOST, port=PORT, proxy_headers=True, forwarded_allow_ips="*")

    else:
        mcp.run()  # stdio — no auth, local only
