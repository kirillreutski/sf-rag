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
pip install google-generativeai psycopg2-binary python-dotenv mcp
python embed_and_load.py
```

- Embeds 890 chunks with Gemini Embedding 2 (dimension 768)
- Skips chunks already in DB — safe to re-run after interruption
- ~890 Gemini API calls, ~3 minutes on paid tier

---

## Step 4 — Connect the MCP server to Claude Code

Add to `.claude/settings.json` in the project root (create the file if it doesn't exist):

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

> **Note:** Use the absolute path in `cwd`. Claude Code starts the MCP server
> as a subprocess and communicates over stdio.

Restart Claude Code (`/restart` or reopen the project). You should see
`apex-docs` appear in the MCP servers list.

---

## Step 5 — Verify

Ask Claude in the project:

```
What are the governor limits for SOQL queries in Apex?
```

Claude will call `search_apex_docs` automatically and cite the relevant chunks.

---

## Connecting from other agents / tools

Any host that supports MCP stdio servers works the same way.

### Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "apex-docs": {
      "command": "python3",
      "args": ["/absolute/path/to/sf-rag/mcp_server.py"]
    }
  }
}
```

### Cursor (`.cursor/mcp.json` in project root)

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

### Custom agent (Python, using MCP SDK)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server = StdioServerParameters(
    command="python3",
    args=["/path/to/sf-rag/mcp_server.py"],
)

async with stdio_client(server) as (read, write):
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
| `extension "vector" does not exist` | Install pgvector: `apt install postgresql-16-pgvector` or build from source |
| `EMBEDDING_DIM mismatch` | Must be 768 in both `setup_db.sql` and both Python files |
| Gemini 429 error | Increase `REQUEST_DELAY` in `embed_and_load.py` |
| MCP server not found | Check that `cwd` is an absolute path and `mcp_server.py` is present |
| Low relevance results | Lower `min_similarity` in `mcp_server.py` (default 0.3) |
