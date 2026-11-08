#!/usr/bin/env python3
"""Dump one chapter of the NXP S32G3 Reference Manual PDF for translation.

The NXP corpus has no parsed Markdown mirror, so the PDF is the sole source.
This helper makes reading it deterministic: chapter boundaries and the section
tree come from the PDF outline, page text is stripped of the repeated header and
footer, tables are emitted as row grids, and figure/table captions are indexed
by page.

Read-only: opens the PDF for reading only, never writes to the repo.

Usage:
  extract_chapter.py <pdf> <chapter> [--out FILE] [--sections-only] [--json]

Exit codes: 0 ok, 2 bad input / missing source, 3 missing PyMuPDF.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import sys

try:
    import pymupdf
except ImportError:  # pragma: no cover - environment dependent
    print("error: PyMuPDF is not installed (pip install pymupdf)", file=sys.stderr)
    sys.exit(3)

SOURCE_DOC = "S32G3RM Rev. 5, 2025-09-17"
APPENDIX_PAGE = 5083  # appendix A ("A General Changes") begins here
LAST_CHAPTER_END = 5082
TOTAL_PAGES = 5101

CHAPTER_RE = re.compile(r"^(\d+)\s+(.+)$")
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)+)\s")
CAPTION_RE = re.compile(r"^(Figure|Table)\s+(\d+)\.\s*(.*)$", re.IGNORECASE)
CONTINUATION_RE = re.compile(r"^Table\s+(?:continued|continues)\b", re.IGNORECASE)
CHROME_RES = [
    re.compile(r"^NXP Semiconductors$"),
    re.compile(r"^S32G3 Reference Manual,\s*Rev\.\s*5,\s*2025-09-17$"),
    re.compile(r"^S32G3 Reference Manual.*$"),
    re.compile(r"^Reference Manual$"),
    re.compile(r"^General Business Information$"),
    re.compile(r"^\d+\s*/\s*5101$"),
]

TOP_BAND = 62.0     # blocks above this y0 are the running header
BOTTOM_BAND = 740.0  # blocks below this y0 are the page footer
MAX_CHAPTER = 81


def slugify(title: str) -> str:
    """lower_snake_case of a chapter title, keeping identifier underscores."""
    s = re.sub(r"[^A-Za-z0-9]+", "_", title.lower()).strip("_")
    return re.sub(r"_+", "_", s)


def chapter_dir(number: int, title: str) -> str:
    """Target article directory, zero-padded so lexical order == chapter order."""
    return f"ch{number:02d}_{slugify(title)}"


def heading_label(section_number: str):
    """Map a source section number to the article's heading.

    Drop the chapter number, keep the rest; heading level = number of remaining
    numeric components + 1, clamped at h6. Deeper levels become a bold paragraph
    carrying the full number instead of an invalid ####### heading.

    Returns (level, label, clamped).
    """
    parts = section_number.split(".")
    if len(parts) < 2:
        raise ValueError(f"not a section number: {section_number!r}")
    remaining = parts[1:]
    label = ".".join(remaining) + "."
    level = min(len(remaining) + 1, 6)
    return level, label, len(remaining) + 1 > 6


def is_chrome_line(line: str) -> bool:
    return any(rx.match(line) for rx in CHROME_RES)


def is_continuation_marker(line: str) -> bool:
    return bool(CONTINUATION_RE.match(line))


def parse_chapters(toc):
    """Numbered chapters from the PDF outline.

    Chapters 1-4 are level-1 entries; chapters 5-81 are level-2 entries nested
    under unnumbered level-1 group headers (including "Debug", which lacks a
    "Chapter NN-NN:" prefix). Both are caught by level <= 2 + numeric title.
    """
    chapters = []
    for level, title, page in toc:
        if level <= 2 and (m := CHAPTER_RE.match(title)):
            chapters.append({"number": int(m.group(1)), "title": m.group(2).strip(),
                             "start": page})
    numbers = [c["number"] for c in chapters]
    expected = list(range(1, MAX_CHAPTER + 1))
    if numbers != expected:
        raise ValueError(f"expected 81 contiguous chapters, got {numbers[:5]}…{numbers[-5:]}")
    return chapters


def chapter_range(chapters, number: int):
    """Inclusive PDF page range for a chapter."""
    ch = next(c for c in chapters if c["number"] == number)
    if number < MAX_CHAPTER:
        end = next(c["start"] for c in chapters if c["number"] == number + 1) - 1
    else:
        end = LAST_CHAPTER_END
    return ch["start"], end


def section_tree(toc, number: int, start: int, end: int):
    """All outline entries belonging to one chapter, in source order."""
    prefix = re.compile(rf"^{number}\.")
    out = []
    for level, title, page in toc:
        if not (start <= page <= end):
            continue
        if prefix.match(title) or title.startswith(f"{number} "):
            out.append({"level": level, "title": title, "page": page})
    return out


def clean_page(page):
    """Text lines with the repeated header/footer removed.

    Header/footer blocks live outside the TOP_BAND/BOTTOM_BAND content area.
    Continuation markers ("Table continued...", "Table continues...") sit near
    those bands but carry table state, so they are always preserved.
    """
    lines = []
    for block in page.get_text("blocks"):
        x0, y0, x1, y1, text = block[:5]
        in_band = y0 < TOP_BAND or y0 > BOTTOM_BAND
        for raw in text.splitlines():
            line = raw.strip()
            if not line:
                continue
            if is_continuation_marker(line):
                lines.append(line)
                continue
            if in_band or is_chrome_line(line):
                continue
            lines.append(line)
    return lines


def stitch_table_rows(grids):
    """Concatenate per-page table grids, dropping repeated header rows."""
    rows = []
    for grid in grids:
        if not grid:
            continue
        if rows and grid[0] == rows[0]:
            grid = grid[1:]
        rows.extend(grid)
    return rows


def page_tables(page):
    """Row grids detected on a page (stdout noise from PyMuPDF suppressed)."""
    grids = []
    with contextlib.redirect_stdout(io.StringIO()):
        found = page.find_tables()
    for table in found.tables:
        grid = [[re.sub(r"\s+", " ", cell or "").strip()
                 for cell in row] for row in table.extract()]
        if grid:
            grids.append(grid)
    return grids


def check_source(path: str):
    if not os.path.isfile(path):
        print(f"error: source PDF not found: {path}", file=sys.stderr)
        sys.exit(2)
    with open(path, "rb") as fh:
        head = fh.read(200)
    if b"git-lfs.github.com/spec/v1" in head:
        print("error: source is an unresolved Git LFS pointer; run 'git lfs pull'", file=sys.stderr)
        sys.exit(2)


def build_report(pdf_path, number, sections_only=False):
    doc = pymupdf.open(pdf_path)
    chapters = parse_chapters(doc.get_toc())
    start, end = chapter_range(chapters, number)
    ch = next(c for c in chapters if c["number"] == number)
    report = {
        "source": pdf_path,
        "document": SOURCE_DOC,
        "chapter": number,
        "title": ch["title"],
        "pages": [start, end],
        "target": f"docs/nxp/s32g3/{chapter_dir(number, ch['title'])}/index.md",
        "sections": section_tree(doc.get_toc(), number, start, end),
        "captions": [],
        "tables": [],
        "page_text": [],
    }
    if sections_only:
        doc.close()
        return report

    for pno in range(start, end + 1):
        page = doc[pno - 1]
        lines = clean_page(page)
        report["page_text"].append({"page": pno, "lines": lines})
        for line in lines:
            if m := CAPTION_RE.match(line):
                report["captions"].append({"page": pno, "kind": m.group(1).title(),
                                          "number": int(m.group(2)), "text": line})
            elif is_continuation_marker(line):
                report["captions"].append({"page": pno, "kind": "Continuation",
                                          "number": None, "text": line})
        for grid in page_tables(page):
            report["tables"].append({"page": pno, "rows": grid})
    doc.close()
    return report


def render_text(report):
    out = [
        f"# Chapter {report['chapter']} — {report['title']}",
        "",
        f"Source: {report['source']} ({report['document']})",
        f"PDF pages: {report['pages'][0]}-{report['pages'][1]}",
        f"Target: {report['target']}",
        "",
        f"## Outline sections ({len(report['sections'])})",
    ]
    for s in report["sections"]:
        out.append(f"  L{s['level']:<2} p{s['page']:<5} {s['title']}")
    if not report["page_text"]:
        return "\n".join(out) + "\n"

    out += ["", f"## Captions ({len(report['captions'])})"]
    for c in report["captions"]:
        out.append(f"  p{c['page']:<5} {c['text']}")

    out += ["", "## Page text"]
    for p in report["page_text"]:
        out += ["", f"### PDF page {p['page']}"] + p["lines"]

    out += ["", f"## Table grids ({len(report['tables'])})"]
    for i, t in enumerate(report["tables"], 1):
        out += ["", f"### Table grid {i} (PDF page {t['page']})"]
        for row in t["rows"]:
            out.append("| " + " | ".join(row) + " |")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", help="path to RMS32G3.pdf")
    ap.add_argument("chapter", type=int, help="chapter number 1-81")
    ap.add_argument("--out", help="write the dump to this file instead of stdout")
    ap.add_argument("--sections-only", action="store_true",
                    help="emit only the outline section tree (fast, no page text)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = ap.parse_args(argv)

    if not 1 <= args.chapter <= MAX_CHAPTER:
        print(f"error: chapter must be 1-{MAX_CHAPTER}", file=sys.stderr)
        sys.exit(2)
    check_source(args.pdf)
    report = build_report(args.pdf, args.chapter, args.sections_only)
    if args.json:
        payload = json.dumps(report, ensure_ascii=False, indent=2)
    else:
        payload = render_text(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(payload)
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
