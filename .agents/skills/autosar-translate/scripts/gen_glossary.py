#!/usr/bin/env python3
"""Generate docs/autosar/glossary.md — an A–Z index of every term defined in
the 缩略语 chapter (## 2. 缩略语) of every article under docs/autosar/.

The glossary is a pure derivation of the articles: never hand-edit it. Run
this script after any change to a ch.2 chapter (autosar-translate SKILL.md
Step 5b) and verify with --check in Phase A.

Usage:
  python .agents/skills/autosar-translate/scripts/gen_glossary.py           # (re)write
  python .agents/skills/autosar-translate/scripts/gen_glossary.py --check   # exit 1 if stale

Parsed shapes (STANDARD.md §1 ch.2 form first; legacy GFM table as fallback):
  **Term**                          -> term line (trailing text/aliases kept for display)
  > definition (one or more lines)  -> definition
  | Term | definition |             -> legacy table row (reported as 待改排)
"""
from __future__ import annotations

import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DOCS = ROOT / "docs" / "autosar"
OUT = DOCS / "glossary.md"
SKIP_DIRS = {"sync-todo", "r21_11", "autosar_pdf"}
SKIP_FILES = {"STANDARD.md", "TODO.md", "glossary.md"}

CH2_RE = re.compile(r"^## 2\. 缩略语\s*$(.*?)(?=^## |\Z)", re.M | re.S)
TERM_RE = re.compile(r"^\*\*(.+?)\*\*(.*)$")
TABLE_ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def front_field(text, field):
    m = re.search(rf"^{field}:\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else None


def iter_articles():
    """Yield (path, spec, release) for mapped articles only — provenance is a
    hard requirement: every glossary entry must name its document and release."""
    for p in sorted(DOCS.rglob("*.md")):
        if p.name in SKIP_FILES or SKIP_DIRS & set(p.parts):
            continue
        text = p.read_text(encoding="utf-8")
        spec = front_field(text, "spec")
        if not spec:
            continue
        yield p, spec, front_field(text, "release") or "R23-11"


def article_label(p: Path) -> str:
    return p.parent.name if p.name == "index.md" else p.stem


def rel_link(p: Path) -> str:
    return p.relative_to(DOCS).as_posix()


def _next_nonblank(lines, i):
    while i < len(lines) and not lines[i].strip():
        i += 1
    return i


def parse_blockquote(lines):
    """Term line = `**Term**…` immediately followed (blank lines allowed) by
    one or more `>` lines. A bold-led sentence with no `>` after it is prose,
    not a term."""
    entries, i = [], 0
    while i < len(lines):
        m = TERM_RE.match(lines[i].rstrip())
        j = _next_nonblank(lines, i + 1) if m else -1
        if m and j < len(lines) and lines[j].startswith(">"):
            display, key, defs = lines[i].strip(), m.group(1).strip(), []
            i = j
            while i < len(lines):
                if lines[i].startswith(">"):
                    defs.append(lines[i].lstrip(">").strip())
                    i += 1
                elif not lines[i].strip():
                    k = _next_nonblank(lines, i)
                    if k < len(lines) and lines[k].startswith(">"):
                        i = k
                    else:
                        break
                else:
                    break
            entries.append((key, display, " ".join(d for d in defs if d)))
        else:
            i += 1
    return entries


def parse_table(lines):
    entries, seen_header = [], False
    for ln in lines:
        m = TABLE_ROW_RE.match(ln)
        if not m:
            continue
        if not seen_header:
            seen_header = True  # header row
            continue
        if re.match(r"^\|?\s*-{2,}", ln):
            continue
        term, desc = m.group(1), m.group(2)
        if set(term) <= set("-: ") or term.endswith("definition:") or term in ("术语",):
            continue
        entries.append((term, f"**{term}**", desc))
    return entries


def norm_def(s: str) -> str:
    s = s.replace("**", "")
    s = re.sub(r"\s+", "", s)
    return s.rstrip("。.；;，,")


def letter_of(key: str) -> str:
    c = key[0].upper()
    return c if "A" <= c <= "Z" else "#"


def build() -> tuple[str, list[str]]:
    terms: "OrderedDict[str, dict]" = OrderedDict()
    report = []
    n_articles = 0
    for p, spec, release in iter_articles():
        text = p.read_text(encoding="utf-8")
        m = CH2_RE.search(text)
        if not m:
            continue
        lines = m.group(1).splitlines()
        bq, tbl = parse_blockquote(lines), parse_table(lines)
        entries, fmt = (bq, "blockquote") if len(bq) >= len(tbl) else (tbl, "table")
        if not entries:
            report.append(f"  ! {rel_link(p)}: ch.2 present but no entries parsed")
            continue
        n_articles += 1
        flag = "  (table — 待改排)" if fmt == "table" else ""
        report.append(f"  {len(entries):3d} {rel_link(p)}{flag}")
        spec_disp = spec.removeprefix("AUTOSAR_CP_")
        for key, display, definition in entries:
            k = key.lower()
            t = terms.setdefault(k, {"display": display, "defs": OrderedDict()})
            if display.count("**") > t["display"].count("**"):
                t["display"] = display
            d = t["defs"].setdefault(norm_def(definition), {"text": definition, "src": []})
            if definition.count("**") > d["text"].count("**"):
                d["text"] = definition
            src = (article_label(p), rel_link(p), spec_disp, release)
            if src not in d["src"]:
                d["src"].append(src)

    out = [
        "---",
        'title: "AUTOSAR 术语表（缩略语与缩写）"',
        "---",
        "",
        "本页汇总各 AUTOSAR 模块文章第 2 章「缩略语」中的全部术语，按字母排序，便于查找。"
        "**由脚本自动生成，请勿手工编辑**——修改应在对应文章的第 2 章进行，然后重新生成"
        "（`python .agents/skills/autosar-translate/scripts/gen_glossary.py`）。"
        "同一术语在不同模块中的释义若有差异，分条列出并标注来源。",
        "",
        f"共 **{len(terms)}** 个术语，来自 **{n_articles}** 篇文章。",
        "",
    ]
    current = None
    for k in sorted(terms, key=lambda s: (letter_of(s) == "#", s)):
        t = terms[k]
        letter = letter_of(k)
        if letter != current:
            current = letter
            out += [f"## {letter if letter != '#' else '其他'}", ""]
        out.append(t["display"])
        for d in t["defs"].values():
            srcs = "、".join(f"[{lbl}]({lnk})（{sp} · {rl}）" for lbl, lnk, sp, rl in d["src"])
            out.append(f"> {d['text']} — 来源：{srcs}")
        out.append("")
    return "\n".join(out).rstrip() + "\n", report


def main(argv):
    content, report = build()
    if "--check" in argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != content:
            print(f"STALE: {OUT.relative_to(ROOT)} differs from regenerated content — run gen_glossary.py", file=sys.stderr)
            return 1
        print("glossary up to date")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
