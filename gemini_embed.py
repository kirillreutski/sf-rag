"""Shared Gemini embedding client with API key rotation and retry logic."""

import os
import time
from google import genai
from google.genai import types

GEMINI_MODEL  = os.getenv("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-2")
EMBEDDING_DIM = 768
MAX_RETRIES   = 5


class KeyRotator:
    """
    Cycles through API keys on 429. Raises only when every key
    returns 429 in a row without a successful request between them.
    """

    def __init__(self, keys: list[str]) -> None:
        if not keys:
            raise ValueError("GEMINI_EMBEDDING_API_TOKEN is empty")
        self.keys = keys
        self._clients = [genai.Client(api_key=k) for k in keys]
        self._idx = 0
        self._consecutive_failures = 0

    @property
    def client(self) -> genai.Client:
        return self._clients[self._idx]

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


def get_embedding(text: str, task_type: str, rate_limiter=None, retries: int = 0) -> list[float]:
    if rate_limiter:
        rate_limiter.acquire()
    try:
        result = _rotator.client.models.embed_content(
            model=GEMINI_MODEL,
            contents=text,
            config=types.EmbedContentConfig(
                task_type=task_type,
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
            return get_embedding(text, task_type, rate_limiter, retries)

        if retries >= MAX_RETRIES:
            raise
        wait = 2 ** retries
        print(f"\n  [retry {retries + 1}/{MAX_RETRIES}] {exc!r} — waiting {wait}s")
        time.sleep(wait)
        return get_embedding(text, task_type, rate_limiter, retries + 1)
