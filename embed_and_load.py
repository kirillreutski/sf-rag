"""
Embed chunks with Gemini Embedding 2 and load them into PostgreSQL (pgvector).

Usage:
    python embed_and_load.py --chunks chunks/lwc_chunks.jsonl --table lwc_chunks

Environment variables (set in .env):
    PG_CONNECTION_STRING        postgresql://user:pass@host:5432/dbname
    GEMINI_EMBEDDING_API_TOKEN  your Gemini API key
"""

import argparse
import collections
import json
import os
import time
import psycopg2
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

GEMINI_MODEL  = os.getenv("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-2")
EMBEDDING_DIM = 768      # must match setup_db.sql vector(N)
BATCH_SIZE    = 50       # DB insert batch size
MAX_RPM       = 80       # Gemini API rate limit (requests per minute)
MAX_RETRIES   = 5

# ── Rate limiter ──────────────────────────────────────────────────────────────

class RateLimiter:
    """Sliding-window rate limiter. Blocks until a request slot is free."""

    def __init__(self, max_per_minute: int) -> None:
        self.max_rpm = max_per_minute
        self._timestamps: collections.deque[float] = collections.deque()

    def acquire(self) -> None:
        while True:
            now = time.monotonic()
            # Drop timestamps older than 60 s
            while self._timestamps and now - self._timestamps[0] >= 60.0:
                self._timestamps.popleft()

            if len(self._timestamps) < self.max_rpm:
                self._timestamps.append(now)
                return

            # Sleep until the oldest slot expires
            sleep_for = 60.0 - (now - self._timestamps[0]) + 0.01
            time.sleep(sleep_for)


_limiter = RateLimiter(MAX_RPM)

# ── Gemini key rotator ────────────────────────────────────────────────────────

class KeyRotator:
    """
    Cycles through API keys on 429. Raises only when every key
    returns 429 in a row without a successful request between them.
    """

    def __init__(self, keys: list[str]) -> None:
        if not keys:
            raise ValueError("GEMINI_EMBEDDING_API_TOKEN is empty")
        self.keys = keys
        self._idx = 0
        self._consecutive_failures = 0

    @property
    def client(self) -> genai.Client:
        return genai.Client(api_key=self.keys[self._idx])

    def on_success(self) -> None:
        self._consecutive_failures = 0

    def rotate(self) -> bool:
        """Switch to next key. Returns False when all keys have failed in a row."""
        self._consecutive_failures += 1
        if self._consecutive_failures >= len(self.keys):
            return False
        self._idx = (self._idx + 1) % len(self.keys)
        return True

    @property
    def label(self) -> str:
        return f"key {self._idx + 1}/{len(self.keys)}"


_keys = [k.strip() for k in os.environ["GEMINI_EMBEDDING_API_TOKEN"].split(",") if k.strip()]
_rotator = KeyRotator(_keys)


def get_embedding(text: str, retries: int = 0) -> list[float]:
    _limiter.acquire()
    try:
        result = _rotator.client.models.embed_content(
            model=GEMINI_MODEL,
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT",
                output_dimensionality=EMBEDDING_DIM,
            ),
        )
        _rotator.on_success()
        return result.embeddings[0].values
    except Exception as exc:
        if "429" in str(exc):
            if not _rotator.rotate():
                raise RuntimeError(f"All {len(_rotator.keys)} API keys exhausted with 429") from exc
            print(f"\n  [429 → {_rotator.label}]")
            return get_embedding(text, retries)   # retry same chunk with new key, no backoff

        if retries >= MAX_RETRIES:
            raise
        wait = 2 ** retries
        print(f"\n  [retry {retries + 1}/{MAX_RETRIES}] {exc!r} — waiting {wait}s")
        time.sleep(wait)
        return get_embedding(text, retries + 1)


# ── PostgreSQL ────────────────────────────────────────────────────────────────

def vec_literal(v: list[float]) -> str:
    return "[" + ",".join(f"{x:.8f}" for x in v) + "]"


def connect() -> psycopg2.extensions.connection:
    return psycopg2.connect(os.environ["PG_CONNECTION_STRING"])


def get_existing_ids(conn, table: str) -> set[str]:
    with conn.cursor() as cur:
        cur.execute(f"SELECT id FROM {table};")
        return {str(row[0]) for row in cur.fetchall()}


def insert_batch(conn, rows: list[dict], table: str) -> int:
    sql = f"""
        INSERT INTO {table} (id, source, breadcrumb, heading, text, token_count, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s::vector)
        ON CONFLICT (id) DO NOTHING;
    """
    with conn.cursor() as cur:
        cur.executemany(
            sql,
            [
                (
                    r["id"], r["source"], r["breadcrumb"], r["heading"],
                    r["text"], r["token_count"], vec_literal(r["embedding"]),
                )
                for r in rows
            ],
        )
    conn.commit()
    return len(rows)


# ── Progress display ──────────────────────────────────────────────────────────

def fmt_duration(seconds: float) -> str:
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    m, s = divmod(seconds, 60)
    return f"{m}m {s:02d}s"


class ProgressLogger:
    BAR_WIDTH = 30

    def __init__(self, total: int) -> None:
        self.total     = total
        self.done      = 0
        self.inserted  = 0
        self.start     = time.monotonic()
        self._api_ts: collections.deque[float] = collections.deque(maxlen=60)

    def tick(self, inserted: int) -> None:
        self.done     += 1
        self.inserted += inserted
        self._api_ts.append(time.monotonic())
        self._render()

    def _render(self) -> None:
        elapsed   = time.monotonic() - self.start
        pct       = self.done / self.total
        filled    = int(self.BAR_WIDTH * pct)
        bar       = "█" * filled + "░" * (self.BAR_WIDTH - filled)
        rpm       = self._current_rpm()
        eta       = self._eta(elapsed)
        rate_warn = f" ⚠ rpm={rpm:.0f}>{MAX_RPM}" if rpm > MAX_RPM else f" rpm={rpm:.0f}"

        line = (
            f"\r[{bar}] {self.done}/{self.total} ({pct*100:.1f}%)"
            f"  elapsed={fmt_duration(elapsed)}"
            f"  eta={eta}"
            f"{rate_warn}"
            f"  saved={self.inserted}"
        )
        # Pad to overwrite previous longer line
        print(line.ljust(110), end="", flush=True)

    def _current_rpm(self) -> float:
        now = time.monotonic()
        recent = [t for t in self._api_ts if now - t <= 60.0]
        return len(recent)

    def _eta(self, elapsed: float) -> str:
        if self.done == 0:
            return "?"
        rate = self.done / elapsed          # chunks per second
        remaining = (self.total - self.done) / rate
        return fmt_duration(remaining)

    def finish(self, elapsed: float) -> None:
        pct = self.done / self.total * 100 if self.total else 100
        bar = "█" * self.BAR_WIDTH
        print(
            f"\r[{bar}] {self.done}/{self.total} ({pct:.1f}%)"
            f"  elapsed={fmt_duration(elapsed)}"
            f"  done".ljust(110)
        )


# ── Main ──────────────────────────────────────────────────────────────────────

def main(chunks_path: Path, table: str) -> None:
    chunks = [
        json.loads(line)
        for line in chunks_path.read_text().splitlines()
        if line.strip()
    ]

    print(f"Chunks file : {chunks_path}  ({len(chunks)} total)")
    print(f"Table       : {table}")

    conn     = connect()
    existing = get_existing_ids(conn, table)
    todo     = [c for c in chunks if c["id"] not in existing]

    print(f"In DB       : {len(existing)}")
    print(f"To embed    : {len(todo)}")
    print(f"Rate limit  : {MAX_RPM} rpm  |  batch size: {BATCH_SIZE}")

    if not todo:
        print("Nothing to do — all chunks already embedded.")
        conn.close()
        return

    print()

    progress = ProgressLogger(len(todo))
    batch: list[dict] = []
    t_start = time.monotonic()

    for chunk in todo:
        chunk["embedding"] = get_embedding(chunk["text"])
        batch.append(chunk)

        inserted = 0
        if len(batch) >= BATCH_SIZE:
            inserted = insert_batch(conn, batch, table)
            batch.clear()

        progress.tick(inserted)

    # Flush remainder
    if batch:
        inserted = insert_batch(conn, batch, table)
        progress.inserted += inserted

    elapsed = time.monotonic() - t_start
    progress.finish(elapsed)

    conn.close()
    print(f"\nSaved {progress.inserted} chunks in {fmt_duration(elapsed)}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks", required=True,              type=Path, help="Input .jsonl file")
    parser.add_argument("--table",  required=True,              type=str,  help="Target PostgreSQL table (e.g. lwc_chunks)")
    args = parser.parse_args()
    main(args.chunks, args.table)
