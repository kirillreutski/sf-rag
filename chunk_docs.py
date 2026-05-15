"""
Chunk Markdown files into JSONL for RAG ingestion.

Strategy:
  1. Split each .md file at heading boundaries (H1–H4).
  2. Sections that exceed MAX_TOKENS are further split at paragraph/code-block
     boundaries with OVERLAP_TOKENS of carry-over context.
  3. Each chunk keeps a breadcrumb of parent headings.

Usage:
    python chunk_docs.py --docs docs/lwc/ --output chunks/lwc_chunks.jsonl
"""

import argparse
import json
import re
import uuid
from pathlib import Path
MAX_TOKENS = 1000
OVERLAP_TOKENS = 100

# ~4 chars per token for English technical text (cl100k_base approximation)
def count_tokens(text: str) -> int:
    return max(1, len(text) // 4)


# ── Markdown parser ──────────────────────────────────────────────────────────

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)


def parse_sections(md_text: str) -> list[dict]:
    """
    Split markdown into sections, each with:
      level, title, body (text between this heading and the next)
    """
    matches = list(HEADING_RE.finditer(md_text))
    sections = []
    for i, m in enumerate(matches):
        level = len(m.group(1))
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[body_start:body_end].strip()
        sections.append({"level": level, "title": title, "body": body})
    return sections


def build_breadcrumb(stack: list[str]) -> str:
    return " > ".join(stack)


# ── Text splitter ────────────────────────────────────────────────────────────

def split_paragraphs(text: str) -> list[str]:
    """
    Split text at blank lines. Code fences (```...```) are kept intact.
    """
    paragraphs: list[str] = []
    buf: list[str] = []
    in_code = False
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
        if not in_code and stripped == "":
            if buf:
                paragraphs.append("".join(buf).strip())
                buf = []
        else:
            buf.append(line)
    if buf:
        paragraphs.append("".join(buf).strip())
    return [p for p in paragraphs if p]


def chunk_text(title: str, body: str, breadcrumb: str) -> list[dict]:
    """
    Split one section's body into ≤MAX_TOKENS chunks with OVERLAP_TOKENS overlap.
    Each chunk carries the section title and breadcrumb.
    """
    # Prefix added to every chunk so context is always present
    prefix = f"# {breadcrumb}\n\n"
    prefix_tokens = count_tokens(prefix)
    budget = MAX_TOKENS - prefix_tokens

    paragraphs = split_paragraphs(body)
    if not paragraphs:
        return []

    chunks: list[dict] = []
    current_parts: list[str] = []
    current_tokens = 0
    overlap_buf: list[str] = []  # paragraphs carried over for overlap

    def flush(parts: list[str]) -> dict | None:
        if not parts:
            return None
        text = prefix + "\n\n".join(parts)
        return {
            "id": str(uuid.uuid4()),
            "source": "",          # filled by caller
            "breadcrumb": breadcrumb,
            "heading": title,
            "text": text,
            "token_count": count_tokens(text),
        }

    for para in paragraphs:
        para_tokens = count_tokens(para)

        # Single paragraph exceeds budget — hard-split by sentences
        if para_tokens > budget:
            if current_parts:
                chunks.append(flush(current_parts))
                overlap_buf = current_parts[-2:]  # keep last 2 paragraphs
                current_parts = list(overlap_buf)
                current_tokens = sum(count_tokens(p) for p in current_parts)

            # Split paragraph into sentences
            sentences = re.split(r"(?<=[.!?])\s+", para)
            for sent in sentences:
                st = count_tokens(sent)
                if current_tokens + st > budget and current_parts:
                    chunks.append(flush(current_parts))
                    current_parts = current_parts[-1:]  # overlap: last sentence-group
                    current_tokens = sum(count_tokens(p) for p in current_parts)
                current_parts.append(sent)
                current_tokens += st
            continue

        if current_tokens + para_tokens > budget and current_parts:
            chunks.append(flush(current_parts))
            # Carry over last few paragraphs as overlap
            overlap_tokens = 0
            overlap_buf = []
            for p in reversed(current_parts):
                t = count_tokens(p)
                if overlap_tokens + t > OVERLAP_TOKENS:
                    break
                overlap_buf.insert(0, p)
                overlap_tokens += t
            current_parts = list(overlap_buf)
            current_tokens = overlap_tokens

        current_parts.append(para)
        current_tokens += para_tokens

    if current_parts:
        chunks.append(flush(current_parts))

    return [c for c in chunks if c]


# ── Main ─────────────────────────────────────────────────────────────────────

def process_file(md_path: Path) -> list[dict]:
    text = md_path.read_text(encoding="utf-8")
    sections = parse_sections(text)

    chunks: list[dict] = []
    # heading stack: index = level-1, value = title
    stack: list[str] = []

    for sec in sections:
        level = sec["level"]
        title = sec["title"]
        body = sec["body"]

        # Update heading stack
        stack = stack[: level - 1]
        stack.append(title)
        breadcrumb = build_breadcrumb(stack)

        sec_chunks = chunk_text(title, body, breadcrumb)
        for c in sec_chunks:
            c["source"] = md_path.name
        chunks.extend(sec_chunks)

    return chunks


def main(docs_dir: Path, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    md_files = sorted(docs_dir.glob("*.md"))

    total = 0
    with output_file.open("w", encoding="utf-8") as out:
        for md_path in md_files:
            print(f"Processing {md_path.name} ...", end=" ", flush=True)
            file_chunks = process_file(md_path)
            for chunk in file_chunks:
                out.write(json.dumps(chunk, ensure_ascii=False) + "\n")
            print(f"{len(file_chunks)} chunks")
            total += len(file_chunks)

    print(f"\nTotal chunks: {total}")
    print(f"Output: {output_file}")

    # Quick stats
    token_counts = []
    with output_file.open() as f:
        for line in f:
            token_counts.append(json.loads(line)["token_count"])

    n = len(token_counts)
    mean = sum(token_counts) / n
    median = sorted(token_counts)[n // 2]
    print(f"Token stats — min: {min(token_counts)}, max: {max(token_counts)}, "
          f"mean: {mean:.0f}, median: {median}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs",   required=True, type=Path, help="Directory with .md files")
    parser.add_argument("--output", required=True, type=Path, help="Output .jsonl file")
    args = parser.parse_args()
    main(args.docs, args.output)
