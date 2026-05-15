"""
Extract Salesforce Apex Developer Guide PDF to Markdown files.
Splits by level-2 TOC sections, preserves code blocks and heading hierarchy.
"""

import fitz
import re
import os
from pathlib import Path

PDF_PATH = "/home/user/sf-rag/salesforce_apex_developer_guide.pdf"
OUTPUT_DIR = "/home/user/sf-rag/docs"

HEADING_FONT = "VAGRoundedStd"
BODY_FONTS = {"MyriadPro-LightSemiCn", "MyriadPro-LightSemiCnIt", "MyriadPro-SemiboldSemiCn"}

KNOWN_SECTION_FOOTERS = {
    "Apex Developer Guide", "Introducing Apex", "Getting Started with Apex",
    "Apex Development Process", "Apex Quick Start",
    "Writing Apex", "Running Apex", "Debugging, Testing, and Deploying Apex",
    "Apex Reference", "Appendices",
    "Data Types and Variables", "Classes, Objects, and Interfaces",
    "Apex Triggers", "Apex Security and Sharing", "Testing Apex",
    "Apex Integration Services", "Apex Transactions and Governor Limits",
    "Batch Apex", "Queueable Apex", "Scheduled Apex", "Future Methods",
    "Platform Events and Apex",
}


def is_code_font(font_name: str) -> bool:
    return "Courier" in font_name or "CourierNew" in font_name


def size_to_heading(size: int) -> int | None:
    """Map VAGRoundedStd font size to markdown heading level. None = footer."""
    if size >= 38:
        return 1
    if size >= 20:
        return 2
    if size >= 16:
        return 2
    if size >= 14:
        return 3
    if size >= 12:
        return 4
    return None  # sz=10 → footer


def is_footer_block(block: dict, page_height: float) -> bool:
    """Heuristic: footer lives in the bottom 10% of the page."""
    if block["bbox"][1] < page_height * 0.88:
        return False
    text = " ".join(
        span["text"]
        for line in block["lines"]
        for span in line["spans"]
    ).strip()
    if re.fullmatch(r"\d{1,4}", text):
        return True
    if text in KNOWN_SECTION_FOOTERS:
        return True
    return False


# ── per-span classification ─────────────────────────────────────────────────

def classify_span(span: dict) -> str:
    """Return 'code', 'heading_N', 'bold', 'bullet', or 'body'."""
    font = span["font"]
    size = round(span["size"])
    text = span["text"]

    if is_code_font(font):
        return "code"

    if HEADING_FONT in font:
        level = size_to_heading(size)
        if level is None:
            return "footer"
        return f"heading_{level}"

    if "SemiboldSemiCn" in font or "Bold" in font:
        stripped = text.strip()
        if stripped in ("•", "–", "-"):
            return "bullet_marker"
        return "bold"

    if text.strip() in ("•", "–"):
        return "bullet_marker"

    return "body"


# ── block → structured items ─────────────────────────────────────────────────

def block_to_items(block: dict) -> list[tuple[str, str]]:
    """
    Convert one PDF block to a list of (type, text) items.

    Types: code_block, heading_N, bold, bullet, body, inline_code
    """
    # Count code vs. non-code spans to decide whether the block is a code block
    code_chars = 0
    total_chars = 0
    for line in block["lines"]:
        for span in line["spans"]:
            t = span["text"].strip()
            if not t:
                continue
            total_chars += len(t)
            if is_code_font(span["font"]):
                code_chars += len(t)

    pure_code = total_chars > 0 and code_chars / total_chars >= 0.90

    if pure_code:
        # Emit as a single code_block
        code_lines = []
        for line in block["lines"]:
            line_text = "".join(s["text"] for s in line["spans"])
            stripped = line_text.rstrip()
            if stripped:
                code_lines.append(stripped)
        if code_lines:
            return [("code_block", "\n".join(code_lines))]
        return []

    # Mixed or non-code block: process span by span
    items: list[tuple[str, str]] = []
    bullet_pending = False

    for line in block["lines"]:
        line_parts: list[tuple[str, str]] = []  # (span_type, text)
        has_bullet_marker = False

        for span in line["spans"]:
            text = span["text"].strip()
            if not text:
                continue
            stype = classify_span(span)
            if stype == "footer":
                continue
            if stype == "bullet_marker":
                has_bullet_marker = True
                continue
            line_parts.append((stype, text))

        if not line_parts:
            continue

        # Determine dominant line type
        types_in_line = [t for t, _ in line_parts]
        is_heading = any(t.startswith("heading_") for t in types_in_line)

        if is_heading:
            # Headings: take the heading span type and join all text
            htype = next(t for t in types_in_line if t.startswith("heading_"))
            text = " ".join(v for _, v in line_parts)
            items.append((htype, text))
        else:
            # Regular text line: inline code gets backtick-wrapped
            parts_text = []
            prev_type = None
            for stype, text in line_parts:
                if stype == "code":
                    parts_text.append(f"`{text}`")
                elif stype == "bold":
                    parts_text.append(f"**{text}**")
                else:
                    parts_text.append(text)
                prev_type = stype

            joined = " ".join(parts_text)
            if has_bullet_marker or bullet_pending:
                items.append(("bullet", joined))
                bullet_pending = False
            else:
                items.append(("body", joined))

    return items


# ── page extraction ───────────────────────────────────────────────────────────

def extract_page_content(page: fitz.Page) -> list[tuple[str, str]]:
    page_height = page.rect.height
    data = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
    items: list[tuple[str, str]] = []

    for block in data["blocks"]:
        if block["type"] != 0:
            continue
        if is_footer_block(block, page_height):
            continue
        items.extend(block_to_items(block))

    return items


# ── items → markdown ──────────────────────────────────────────────────────────

def items_to_markdown(items: list[tuple[str, str]]) -> str:
    out: list[str] = []
    i = 0

    while i < len(items):
        itype, itext = items[i]

        if itype == "code_block":
            out.append("```apex")
            out.append(itext)
            out.append("```")
            out.append("")

        elif itype.startswith("heading_"):
            level = int(itype.split("_")[1])
            out.append("")
            out.append("#" * level + " " + itext)
            out.append("")

        elif itype == "bullet":
            out.append(f"- {itext}")

        elif itype == "bold":
            # Bold label (term definition, etc.)
            out.append("")
            out.append(f"**{itext}**")
            out.append("")

        elif itype == "body":
            # Merge consecutive body lines into one paragraph
            para = [itext]
            while i + 1 < len(items) and items[i + 1][0] == "body":
                i += 1
                para.append(items[i][1])
            out.append(" ".join(para))
            out.append("")

        else:
            out.append(itext)
            out.append("")

        i += 1

    return "\n".join(out)


# ── main ──────────────────────────────────────────────────────────────────────

def slugify(title: str) -> str:
    t = title.lower()
    t = re.sub(r"[^a-z0-9]+", "_", t)
    return t.strip("_")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    doc = fitz.open(PDF_PATH)
    toc = doc.get_toc()
    total_pages = len(doc)

    # Level-2 sections with 0-indexed start pages
    level2 = [(title, page - 1) for level, title, page in toc if level == 2]

    # Build chapters: merge sections that start on the same page
    chapters: list[tuple[str, int, int]] = []
    for idx, (title, start) in enumerate(level2):
        end = level2[idx + 1][1] if idx + 1 < len(level2) else total_pages
        if start >= end:
            # Zero-length section (same page as next) – skip or merge forward
            print(f"  [skip] '{title}' has no dedicated pages (p{start} == p{end})")
            continue
        chapters.append((title, start, end))

    print(f"Extracting {len(chapters)} chapters from {total_pages} pages...\n")

    for ch_idx, (title, start, end) in enumerate(chapters):
        filename = f"{ch_idx:02d}_{slugify(title)}.md"
        filepath = Path(OUTPUT_DIR) / filename
        print(f"  [{ch_idx+1}/{len(chapters)}] {title} (pp {start+1}–{end}) → {filename}")

        all_items: list[tuple[str, str]] = [("heading_1", title)]

        for page_num in range(start, end):
            page = doc[page_num]
            all_items.extend(extract_page_content(page))

        md = items_to_markdown(all_items)
        md = re.sub(r"\n{3,}", "\n\n", md)

        filepath.write_text(md, encoding="utf-8")
        print(f"     → {filepath.stat().st_size // 1024} KB")

    doc.close()
    print("\nDone!")


if __name__ == "__main__":
    main()
