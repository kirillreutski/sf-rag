# Apex RAG — Setup Guide

## Prerequisites

- PostgreSQL ≥ 15 with [pgvector](https://github.com/pgvector/pgvector) installed
- Python 3.11+
- Gemini API key with access to `gemini-embedding-exp-03-07`

---

## Step 1 — Environment

Create `.env` in the project root:

```
PG_CONNECTION_STRING=postgresql://user:password@localhost:5432/yourdb
GEMINI_EMBEDDING_API_TOKEN=your_gemini_api_key

# SSE transport only (see Step 4b)
MCP_TRANSPORT=sse
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_API_TOKEN=your_generated_token
```

Generate a secure token:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

---

## Step 2 — Database setup

```bash
psql "$PG_CONNECTION_STRING" -f setup_db.sql
```

Creates table `apex_chunks`, HNSW index, and `search_apex_docs()` function.

---

## Step 3 — Embed and load

```bash
pip install google-genai psycopg2-binary python-dotenv mcp uvicorn
python embed_and_load.py
```

- Embeds 890 chunks with Gemini Embedding 2 (dimension 768)
- Rate-limited to 80 RPM with a sliding-window limiter
- Skips chunks already in DB — safe to re-run after interruption

---

## Step 4a — Local use (stdio, no auth)

For running directly on the same machine as Claude Code. No network, no auth.

Add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "apex-docs": {
      "command": "python3",
      "args": ["mcp_server.py"],
      "cwd": "/absolute/path/to/sf-rag"
    }
  }
}
```

Restart Claude Code. `apex-docs` will appear in the MCP servers list.

---

## Step 4b — Remote server (SSE, bearer token auth)

For running the MCP server on a remote host (e.g. alongside the PostgreSQL DB).

**On the server**, set `MCP_TRANSPORT=sse` in `.env` and start:

```bash
python3 mcp_server.py
# → Starting MCP SSE server on 0.0.0.0:8000
```

Or with systemd / Docker — the process just needs the `.env` variables.

**On the client**, add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "apex-docs": {
      "url": "http://your-server:8000/sse",
      "headers": {
        "Authorization": "Bearer your_generated_token"
      }
    }
  }
}
```

The server returns `401 Unauthorized` for any request with a missing or
wrong token. `MCP_API_TOKEN` must be set or the server will refuse to start.

---

## Step 5 — Verify

Ask Claude:

```
What are the governor limits for SOQL queries in Apex?
```

Claude calls `search_apex_docs` automatically and cites the relevant chunks.

---

## Connecting from other agents / tools

### Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json`)

SSE (remote):
```json
{
  "mcpServers": {
    "apex-docs": {
      "url": "http://your-server:8000/sse",
      "headers": { "Authorization": "Bearer your_token" }
    }
  }
}
```

### Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "apex-docs": {
      "url": "http://your-server:8000/sse",
      "headers": { "Authorization": "Bearer your_token" }
    }
  }
}
```

### Custom agent (Python)

```python
from mcp.client.sse import sse_client
from mcp import ClientSession

async with sse_client(
    "http://your-server:8000/sse",
    headers={"Authorization": "Bearer your_token"},
) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool(
            "search_apex_docs",
            {"query": "how to write a trigger", "k": 5},
        )
        print(result.content[0].text)
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `extension "vector" does not exist` | `apt install postgresql-16-pgvector` or build from source |
| `EMBEDDING_DIM mismatch` | Must be `768` in `setup_db.sql` and both Python files |
| Gemini 429 errors | Rate limiter handles retries, but check your API quota |
| `401 Unauthorized` | Check `MCP_API_TOKEN` matches the `Authorization: Bearer …` header |
| `MCP_API_TOKEN must be set` | SSE transport requires the token env var to be non-empty |
| Low relevance results | Lower `min_sim` in `mcp_server.py` `semantic_search()` call (default 0.3) |
