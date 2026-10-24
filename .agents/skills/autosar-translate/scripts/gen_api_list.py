#!/usr/bin/env python3
"""Generate docs/autosar/api_reference.md — an A–Z index of every API function
and type defined in chapter 8 (API specification) of every AUTOSAR CP SWS
document in the R23-11 markdown corpus, each entry naming its document and
release, and linking to the site article when one exists.

Pure derivation of the source corpus + the articles' front-matter `spec:` —
never hand-edit the output. Run after any article/front-matter change
(autosar-translate SKILL.md Step 6) and verify with --check in Phase A.

Usage:
  python .agents/skills/autosar-translate/scripts/gen_api_list.py           # (re)write
  python .agents/skills/autosar-translate/scripts/gen_api_list.py --check   # exit 1 if stale

Extraction (per source document):
  ch.8 region   = from `## 8 API specification` to `## 9 …`
  types         = `## 8.2.N[.M] <Identifier>`   (8.2 Type definitions)
  functions     = `## 8.3.N[.M] <Identifier>`   (8.3 Function definitions)
Group headings ("General Interface"), empty `## 8.3.1.1` stubs and prose
headings are excluded by requiring an identifier-shaped name.
"""
from __future__ import annotations

import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DOCS = ROOT / "docs" / "autosar"
OUT = DOCS / "api_reference.md"
RELEASE = "R23-11"
SRC = Path.home() / "Workspace/autosar_standard/markdown/Classic_Platform/Releases" / RELEASE

CH8_START = re.compile(r"^##\s+8\s+API\s+specification", re.I | re.M)
CH9_START = re.compile(r"^##\s+9\s", re.M)
HEAD_RE = re.compile(r"^##\s+(8(?:\.\d+)*)\s+(.+?)\s*$", re.M)
IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def section_items(region, title_re):
    """Every `## ` heading strictly inside the `8.x <title matching title_re>`
    section — the next numbered `## 8…` heading of same-or-shallower level
    ends it. Found by TITLE, never by fixed number: the numbering differs per
    document (Det: types in 8.1.2/functions in 8.1.3; TcpIp: functions in
    8.4), inner headings may carry no numeric prefix at all (CoreTest — the
    PDF conversion dropped them), and the section title itself varies
    (BFX: "Bit functions definitions")."""
    heads = [(m.group(1).split("."), m.group(2), m.start()) for m in HEAD_RE.finditer(region)]
    allh = [(m.start(), m.group(1)) for m in re.finditer(r"^##\s+(.+?)\s*$", region, re.M)]
    for i, (lvl, title, start) in enumerate(heads):
        if not title_re.search(title):
            continue
        end = len(region)
        for lvl2, _t2, start2 in heads[i + 1:]:
            if len(lvl2) <= len(lvl):
                end = start2
                break
        items = []
        for pos, txt in allh:
            if pos <= start or pos >= end:
                continue
            txt = re.sub(r"^8(?:\.\d+)*\s+", "", txt)
            items.append(txt)
        return items
    return None


def clean(name: str) -> str:
    name = re.sub(r"\s*glyph\[.*$", "", name)
    return name.replace("\\_", "_").strip()


def article_index():
    """spec stem -> (label, link) from articles' front-matter."""
    idx = {}
    for p in sorted(DOCS.rglob("*.md")):
        if "sync-todo" in p.parts or "r21_11" in p.parts or p.name in {"STANDARD.md", "TODO.md", "glossary.md", "api_reference.md"}:
            continue
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^spec:\s*(\S+)", text, re.M)
        if m:
            label = p.parent.name if p.name == "index.md" else p.stem
            idx[m.group(1)] = (label, p.relative_to(DOCS).as_posix())
    return idx


def extract(doc: Path):
    text = doc.read_text(encoding="utf-8", errors="replace")
    m = CH8_START.search(text)
    if not m:
        return None
    end = CH9_START.search(text, m.end())
    region = text[m.start(): end.start() if end else len(text)]
    t_titles = section_items(region, re.compile(r"types?\s+definitions", re.I))
    f_titles = section_items(region, re.compile(r"functions?\s+definitions", re.I))
    types = [clean(n) for n in (t_titles or []) if IDENT_RE.match(clean(n))]
    funcs = [clean(n) for n in (f_titles or []) if IDENT_RE.match(clean(n))]
    return types, funcs


def letter_of(name: str) -> str:
    c = name[0].upper()
    return c if "A" <= c <= "Z" else "#"


def build():
    idx = article_index()
    entries: "OrderedDict[str, list]" = OrderedDict()  # name.lower() -> [(name, kind, stem, label, link)]
    report, n_docs, n_types, n_funcs = [], 0, 0, 0
    for doc in sorted(SRC.rglob("AUTOSAR_CP_SWS_*.md")):
        if "_artifacts" in doc.parts:
            continue
        res = extract(doc)
        stem = doc.stem
        if res is None:
            report.append(f"  - {stem}: no ch.8 API specification heading")
            continue
        types, funcs = res
        if not types and not funcs:
            report.append(f"  ! {stem}: ch.8 present but no 8.2/8.3 identifiers parsed")
            continue
        n_docs += 1
        n_types += len(types)
        n_funcs += len(funcs)
        label_link = idx.get(stem)
        report.append(f"  {len(types):3d} types {len(funcs):3d} funcs  {stem}{'' if label_link else '  (未翻译)'}")
        for name, kind in [(t, "类型") for t in types] + [(f, "函数") for f in funcs]:
            entries.setdefault(name.lower(), []).append((name, kind, stem, label_link))

    translated = sum(1 for d in {e[2] for v in entries.values() for e in v} if d in idx)
    out = [
        "---",
        'title: "AUTOSAR API 清单（函数与类型）"',
        "---",
        "",
        f"本页汇总 AUTOSAR CP **{RELEASE}** 全部 SWS 文档第 8 章「API specification」中定义的**类型**（8.2）"
        "与**函数**（8.3），按字母排序，便于查找；每条标注所属文档与发布版本，已翻译的模块链接到站内文章。"
        "**由脚本自动生成，请勿手工编辑**（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；"
        f"源：`~/Workspace/autosar_standard/markdown/.../{RELEASE}/`）。",
        "",
        f"共 **{n_types}** 个类型、**{n_funcs}** 个函数，来自 **{n_docs}** 份文档（其中 **{translated}** 份已有站内文章）。",
        "",
    ]
    current = None
    for k in sorted(entries, key=lambda s: (letter_of(s) == "#", s)):
        occ = entries[k]
        letter = letter_of(k)
        if letter != current:
            current = letter
            out += [f"## {letter if letter != '#' else '其他'}", ""]
        out.append(f"**{occ[0][0]}**")
        for name, kind, stem, label_link in occ:
            spec_disp = stem.removeprefix("AUTOSAR_CP_")
            where = f"[{label_link[0]}]({label_link[1]})" if label_link else "未翻译"
            out.append(f"> {kind} · {where} · {spec_disp} · {RELEASE}")
        out.append("")
    return "\n".join(out).rstrip() + "\n", report


def main(argv):
    if not SRC.exists():
        print(f"source corpus not found: {SRC}", file=sys.stderr)
        return 2
    content, report = build()
    if "--check" in argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != content:
            print(f"STALE: {OUT.relative_to(ROOT)} differs from regenerated content — run gen_api_list.py", file=sys.stderr)
            return 1
        print("api_reference up to date")
        return 0
    OUT.write_text(content, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
