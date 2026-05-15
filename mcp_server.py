"""
MCP server: Salesforce Apex Developer Guide semantic search.

Exposes one tool to Claude:
    search_apex_docs(query, k=5) → top-K relevant documentation chunks

Transport: stdio (Claude Code default).

Environment variables (set in .env):
    PG_CONNECTION_STRING        postgresql://user:pass@host:5432/dbname
    GEMINI_EMBEDDING_API_TOKEN  your Gemini API key
"""

import os
import psycopg2
from google import genai
from google.genai import types
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

GEMINI_MODEL  = "models/gemini-embedding-exp-03-07"
EMBEDDING_DIM = 768   # must match the value used during embed_and_load.py

# ── Gemini ────────────────────────────────────────────────────────────────────

_client = genai.Client(api_key=os.environ["GEMINI_EMBEDDING_API_TOKEN"])


def embed_query(text: str) -> list[float]:
    result = _client.models.embed_content(
        model=GEMINI_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=EMBEDDING_DIM,
        ),
    )
    return result.embeddings[0].values


# ── PostgreSQL ────────────────────────────────────────────────────────────────

def get_conn() -> psycopg2.extensions.connection:
    return psycopg2.connect(os.environ["PG_CONNECTION_STRING"])


def vec_literal(v: list[float]) -> str:
    return "[" + ",".join(f"{x:.8f}" for x in v) + "]"


def semantic_search(embedding: list[float], k: int, min_sim: float):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT breadcrumb, heading, text, similarity "
                "FROM search_apex_docs(%s::vector, %s, %s);",
                (vec_literal(embedding), k, min_sim),
            )
            return cur.fetchall()
    finally:
        conn.close()


# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="apex-docs",
    instructions=(
        "Use search_apex_docs whenever the user asks about Salesforce Apex: "
        "syntax, classes, triggers, governors, SOQL, async patterns, etc."
    ),
)


@mcp.tool()
def search_apex_docs(query: str, k: int = 5) -> str:
    """
    Semantic search over the Salesforce Apex Developer Guide.

    Args:
        query: Natural-language question or keyword phrase about Apex.
        k:     Number of results to return (default 5, max 10).

    Returns:
        Formatted documentation excerpts ranked by relevance.
    """
    k = min(k, 10)
    embedding = embed_query(query)
    rows = semantic_search(embedding, k, min_sim=0.3)

    if not rows:
        return "No relevant documentation found. Try rephrasing the query."

    parts = []
    for i, (breadcrumb, heading, text, sim) in enumerate(rows, 1):
        parts.append(
            f"## Result {i} — {breadcrumb}\n"
            f"**Similarity:** {sim:.2f}\n\n"
            f"{text}"
        )

    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    mcp.run()   # stdio transport
