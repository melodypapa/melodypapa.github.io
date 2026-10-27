#!/usr/bin/env python3
"""Check API-chapter sync between an SWS source and its Type A article.

Compares, for one document pair:
  - source chapter 8.2.x type headings   <-> article section 7.2.x headings
  - source chapter 8.3.x function headings <-> article section 7.3.x headings
    (count, names and order; source names may carry PDF-extraction
     backslash-escaped underscores and HTML entities, which are normalized away)
  - the number of `**说明**` blocks in the article's 7.3 chapter against the
    number of functions

This is the mechanical tripwire for SKILL.md Phase A check 7. It cannot see
prose fidelity inside an entry — the cell-by-cell type-table and
requirement-by-requirement reads stay Phase B work.

Usage:
  check_api_sync.py <source.markdown> <article-index.md>

Exit codes: 0 = in sync, 1 = mismatch (report printed), 2 = usage/IO error.
"""

import re
import sys
from pathlib import Path

# "## 8.2.3  Pwm\_OutputStateType" — but PDF extraction merges some headings
# with fence junk ("## ⌋ () 8.2.5  Pwm\_ChannelClassType"), so match anywhere
# in the line; only lines starting with '#' are scanned (keeps ToC tables out).
# The lookbehind avoids matching the "8" of "18.3.2" style chapter numbers.
# The optional third group covers grouped function chapters where the source
# numbers functions as four-deep headings (8.3.1.x Synchronous / 8.3.2.x
# Asynchronous, e.g. MemAcc) and the article mirrors that grouping as
# #### 7.3.1. 同步函数 / ##### 7.3.1.x entries (EcuM precedent). In grouped
# mode only the four-segment headings are entries; the three-segment
# Synchronous/Asynchronous group headings are excluded.
SRC_RE = re.compile(
    r"(?:^|[^0-9.])8\.([23])\.(\d+)(?:\.(\d+))?\s+\**\s*([A-Za-z][A-Za-z0-9_\\&;<>]*)"
)
ART_RE = re.compile(r"^#{4,6}\s+7\.([23])\.(\d+)(?:\.(\d+))?\.\s+(.+?)\s*$")


def norm(name: str) -> str:
    r"""Normalize a heading name: drop extraction backslashes and spaces,
    decode PDF-conversion HTML entities so source names like
    ``IoHwAb&lt;Init\_Id&gt;\_ConfigType`` compare equal to the article's
    ``IoHwAb<Init_Id>_ConfigType``."""
    name = name.replace("\\", "").replace(" ", "")
    for ent, ch in (("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&")):
        name = name.replace(ent, ch)
    return name


def collect(lines, key_re, immut_key):
    """Scan heading lines for API entries and return them as ordered names.

    Grouped mode is entered per chapter when ANY matching heading carries a
    third (x.y.z) numeric segment; then only three-deep headings (7.3.1.x)
    are entries and two-deep headings (7.3.1 同步函数) are group chrome.
    Flat mode collects the two-deep headings as today.
    """
    hits_by_chap: dict[str, list] = {k: [] for k in ("2", "3")}
    for line in lines:
        if not line.startswith("#"):
            continue
        for m in key_re.finditer(line):
            chap, sub = m.group(1), m.group(3)
            hits_by_chap[chap].append((sub, m.group(immut_key)))
    found_by_chap: dict[str, list[str]] = {}
    for chap, hits in hits_by_chap.items():
        grouped = any(sub is not None for sub, _ in hits)
        found: list[str] = []
        for sub, name in hits:
            if grouped and sub is None:
                continue  # group chrome (Synchronous/Asynchronous ...)
            if (not grouped) and sub is not None:
                continue  # grouped entry under a flat-mode chapter
            if not found or found[-1] != norm(name):  # dedupe merged-heading repeats
                found.append(norm(name))
        found_by_chap[chap] = found
    return found_by_chap


def source_entries(text: str) -> dict:
    return collect(text.splitlines(), SRC_RE, 4)


def article_entries(text: str) -> dict:
    return collect(text.splitlines(), ART_RE, 4)


def slice_section(text: str, start_re: str, end_re: str) -> str:
    lines = text.splitlines()
    start = end = None
    for i, line in enumerate(lines):
        if start is None and re.match(start_re, line):
            start = i
        elif start is not None and re.match(end_re, line):
            end = i
            break
    if start is None:
        return ""
    return "\n".join(lines[start : end if end is not None else len(lines)])


def diff_names(src: list[str], art: list[str], label: str) -> list[str]:
    problems: list[str] = []
    missing = [n for n in src if n not in art]
    extra = [n for n in art if n not in src]
    if missing:
        problems.append(f"  {label}: in source, missing from article: {missing}")
    if extra:
        problems.append(f"  {label}: in article, not in source: {extra}")
    common_src = [n for n in src if n in art]
    common_art = [n for n in art if n in src]
    if common_src != common_art:
        problems.append(
            f"  {label}: order differs\n    source : {common_src}\n    article: {common_art}"
        )
    return problems


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src_path, art_path = Path(sys.argv[1]), Path(sys.argv[2])
    try:
        src_text = src_path.read_text(encoding="utf-8")
        art_text = art_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"! cannot read input: {exc}")
        return 2

    problems: list[str] = []

    for srcchap, artchap, label in (("2", "2", "types"), ("3", "3", "functions")):
        src = source_entries(src_text)[srcchap]
        art = article_entries(art_text)[artchap]
        print(
            f"{label:9s}: source 8.{srcchap}.x = {len(src):2d} | article 7.{artchap}.x = {len(art):2d}"
        )
        if not src and art:
            problems.append(
                f"  {label}: source chapter 8.{srcchap} parsed as empty while the "
                "article has entries — check for an unparseable source structure "
                "(see gen_api_list.py's known `!` documents) before overriding"
            )
        problems.extend(diff_names(src, art, label))
        if srcchap == "3":
            body = slice_section(art_text, r"^### 7\.3\.", r"^### 7\.[4-9]\.")
            shuoming = len(re.findall(r"^\*\*说明\*\*", body, re.M))
            print(f"**说明** blocks in §7.3 = {shuoming} (functions = {len(art)})")
            if shuoming != len(art):
                problems.append(
                    f"  functions: {len(art)} headings but {shuoming} **说明** blocks in §7.3"
                )

    if problems:
        print("== API sync: MISMATCH ==")
        for p in problems:
            print(p)
        return 1
    print("== API sync: OK (count, names and order match; **说明** blocks match functions) ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
