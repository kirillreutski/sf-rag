"""
Embed chunks with Gemini Embedding 2 and load them into PostgreSQL (pgvector).

Usage:
    python embed_and_load.py [--chunks chunks/chunks.jsonl] [--workers 1]

Environment variables (set in .env):
    PG_CONNECTION_STRING        postgresql://user:pass@host:5432/dbname
    GEMINI_EMBEDDING_API_TOKEN  your Gemini API key
"""

import argparse
import json
import os
import time
import psycopg2
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

GEMINI_MODEL   = "models/gemini-embedding-exp-03-07"
EMBEDDING_DIM  = 768      # must match setup_db.sql vector(N)
BATCH_SIZE     = 50       # DB insert batch size
REQUEST_DELAY  = 0.05     # seconds between Gemini API calls (free tier: ~15 RPM)
MAX_RETRIES    = 5

# ── Gemini ────────────────────────────────────────────────────────────────────

genai.configure(api_key=os.environ["GEMINI_EMBEDDING_API_TOKEN"])


def get_embedding(text: str, retries: int = 0) -> list[float]:
    """Embed a single text using Gemini Embedding 2 (RETRIEVAL_DOCUMENT task)."""
    try:
        result = genai.embed_content(
            model=GEMINI_MODEL,
            content=text,
            task_type="retrieval_document",
            output_dimensionality=EMBEDDING_DIM,
        )
        return result["embedding"]
    except Exception as exc:
        if retries >= MAX_RETRIES:
            raise
        wait = 2 ** retries
        print(f"  [retry {retries+1}/{MAX_RETRIES}] {exc} — waiting {wait}s")
        time.sleep(wait)
        return get_embedding(text, retries + 1)


# ── PostgreSQL ────────────────────────────────────────────────────────────────

def vec_literal(v: list[float]) -> str:
    """Format a Python list as a pgvector literal '[0.1,0.2,...]'."""
    return "[" + ",".join(f"{x:.8f}" for x in v) + "]"


def connect() -> psycopg2.extensions.connection:
    return psycopg2.connect(os.environ["PG_CONNECTION_STRING"])


def get_existing_ids(conn) -> set[str]:
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM apex_chunks;")
        return {str(row[0]) for row in cur.fetchall()}


def insert_batch(conn, rows: list[dict]) -> None:
    sql = """
        INSERT INTO apex_chunks (id, source, breadcrumb, heading, text, token_count, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s::vector)
        ON CONFLICT (id) DO NOTHING;
    """
    with conn.cursor() as cur:
        cur.executemany(
            sql,
            [
                (
                    r["id"],
                    r["source"],
                    r["breadcrumb"],
                    r["heading"],
                    r["text"],
                    r["token_count"],
                    vec_literal(r["embedding"]),
                )
                for r in rows
            ],
        )
    conn.commit()


# ── Main ──────────────────────────────────────────────────────────────────────

def main(chunks_path: Path) -> None:
    chunks = [json.loads(line) for line in chunks_path.read_text().splitlines() if line.strip()]
    print(f"Loaded {len(chunks)} chunks from {chunks_path}")

    conn = connect()
    existing = get_existing_ids(conn)
    todo = [c for c in chunks if c["id"] not in existing]
    print(f"Already in DB: {len(existing)}  |  To embed: {len(todo)}")

    if not todo:
        print("Nothing to do.")
        conn.close()
        return

    batch: list[dict] = []
    for i, chunk in enumerate(todo, 1):
        embedding = get_embedding(chunk["text"])
        chunk["embedding"] = embedding
        batch.append(chunk)
        time.sleep(REQUEST_DELAY)

        if len(batch) >= BATCH_SIZE:
            insert_batch(conn, batch)
            batch.clear()

        if i % 50 == 0 or i == len(todo):
            pct = i / len(todo) * 100
            print(f"  {i}/{len(todo)} ({pct:.1f}%)")

    if batch:
        insert_batch(conn, batch)

    conn.close()
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks", default="chunks/chunks.jsonl", type=Path)
    args = parser.parse_args()
    main(args.chunks)
