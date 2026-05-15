"""
MCP server: Salesforce Apex Developer Guide semantic search.

Exposes one tool:
    search_apex_docs(query, k=5) → top-K relevant documentation chunks

Transports
----------
stdio  (default) — local subprocess, no auth needed.
sse              — network server with Bearer token auth.

Environment variables (set in .env):
    PG_CONNECTION_STRING        postgresql://user:pass@host:5432/dbname
    GEMINI_EMBEDDING_API_TOKEN  your Gemini API key
    MCP_TRANSPORT               "stdio" (default) | "sse"
    MCP_HOST                    bind host for SSE (default: 0.0.0.0)
    MCP_PORT                    bind port for SSE (default: 8000)
    MCP_API_TOKEN               bearer token required for SSE transport
"""

import os
import sys
import psycopg2
import uvicorn
from google import genai
from google.genai import types
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

GEMINI_MODEL  = "gemini-embedding-2"
EMBEDDING_DIM = 768

TRANSPORT = os.getenv("MCP_TRANSPORT", "stdio")
HOST      = os.getenv("MCP_HOST", "0.0.0.0")
PORT      = int(os.getenv("MCP_PORT", "8000"))
API_TOKEN = os.getenv("MCP_API_TOKEN", "")

# ── Gemini ────────────────────────────────────────────────────────────────────

_gemini = genai.Client(api_key=os.environ["GEMINI_EMBEDDING_API_TOKEN"])


def embed_query(text: str) -> list[float]:
    result = _gemini.models.embed_content(
        model=GEMINI_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=EMBEDDING_DIM,
        ),
    )
    return result.embeddings[0].values


# ── PostgreSQL ────────────────────────────────────────────────────────────────

def vec_literal(v: list[float]) -> str:
    return "[" + ",".join(f"{x:.8f}" for x in v) + "]"


def semantic_search(embedding: list[float], table: str, k: int, min_sim: float):
    # Derive function name from table: apex_chunks → search_apex
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


# ── Auth middleware (SSE only) ─────────────────────────────────────────────────

class BearerTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth = request.headers.get("Authorization", "")
        token = auth.removeprefix("Bearer ").strip()
        if token != API_TOKEN:
            return Response("Unauthorized", status_code=401,
                            media_type="text/plain")
        return await call_next(request)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if TRANSPORT == "sse":
        if not API_TOKEN:
            print("ERROR: MCP_API_TOKEN must be set for SSE transport.", file=sys.stderr)
            sys.exit(1)

        app = mcp.sse_app()
        app.add_middleware(BearerTokenMiddleware)

        print(f"Starting MCP SSE server on {HOST}:{PORT}")
        uvicorn.run(app, host=HOST, port=PORT, proxy_headers=True, forwarded_allow_ips="*")

    else:
        mcp.run()  # stdio — no auth, local only
