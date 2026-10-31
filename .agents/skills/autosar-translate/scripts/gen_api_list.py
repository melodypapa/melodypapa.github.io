#!/usr/bin/env python3
"""Generate the AUTOSAR API listing under docs/autosar/api/ — an A–Z index of
the API functions and types covered by the site's TRANSLATED articles.

Basis is the translated articles (front-matter `spec:`), not the raw corpus:
for every article, the identifiers defined in the matching SWS document's
ch.8 (8.2 types / 8.3 functions, per the R23-11 markdown corpus) are listed
ONLY when the article itself carries a heading for the identifier, and the
identifier deep-links to that heading's anchor (Material slug rules,
including `_1`-style dedup) inside the article. Identifiers without a
matching article heading are dropped and reported — the listing never
promises more than the articles deliver.

Output (three pages, regenerate as a set — never hand-edit):
  api/index.md      landing page (intro + 文章 links to the two lists)
  api/types.md      type list  (ch.8 8.2 Type definitions)
  api/functions.md  function list (ch.8 8.3 Function definitions)

Pure derivation of the articles + the source corpus — never hand-edit the
output. Run after any article/front-matter change (autosar-translate
SKILL.md Step 6) and verify with --check in Phase A.

Usage:
  python .agents/skills/autosar-translate/scripts/gen_api_list.py           # (re)write
  python .agents/skills/autosar-translate/scripts/gen_api_list.py --check   # exit 1 if stale

Corpus extraction (per source document, classification only):
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
API_DIR = DOCS / "api"
OUT_INDEX = API_DIR / "index.md"
OUT_TYPES = API_DIR / "types.md"
OUT_FUNCS = API_DIR / "functions.md"
RELEASE = "R23-11"
SRC = Path.home() / "Workspace/autosar_standard/markdown/Classic_Platform/Releases" / RELEASE

CH8_START = re.compile(r"^##\s+8\s+API\s+specification", re.I | re.M)
CH9_START = re.compile(r"^##\s+9\s", re.M)
HEAD_RE = re.compile(r"^##\s+(8(?:\.\d+)*)\s+(.+?)\s*$", re.M)
IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def section_items(region, title_re):
    """Every `## ` heading belonging to the `8.x <title matching title_re>`
    section.

    Membership is decided by the heading's OWN numeric prefix when it has
    one: a heading numbered `8.3.1` belongs to the `8.3` section even when
    the PDF conversion placed it *before* that section's own heading (WdgM:
    `## 8.3.1 WdgM_Init` precedes `## 8.3 Function definitions`, so the
    positional scan filed it under 8.2 and dropped it from 8.3). Headings
    without a numeric prefix keep the positional rule — the conversion
    dropped the numbers in some documents (CoreTest).

    Found by TITLE, never by fixed number: the numbering differs per
    document (Det: types in 8.1.2/functions in 8.1.3; TcpIp: functions in
    8.4), inner headings may carry no numeric prefix at all (CoreTest — the
    PDF conversion dropped them), and the section title itself varies
    (BFX: "Bit functions definitions")."""
    heads = [(m.group(1).split("."), m.group(2), m.start()) for m in HEAD_RE.finditer(region)]
    allh = [(m.start(), m.group(1)) for m in re.finditer(r"^##\s+(.+?)\s*$", region, re.M)]
    numbered = {start: ".".join(lvl) for lvl, _title, start in heads}
    # the two API sections' own numbers, so a heading can be attributed to
    # the section it is numbered under rather than to the one it sits in
    secnum = {}
    for lvl, title, _start in heads:
        if re.search(r"types?\s+definitions", title, re.I):
            secnum.setdefault("types", ".".join(lvl))
        if re.search(r"functions?\s+definitions", title, re.I):
            secnum.setdefault("funcs", ".".join(lvl))
    for i, (lvl, title, start) in enumerate(heads):
        if not title_re.search(title):
            continue
        end = len(region)
        for lvl2, _t2, start2 in heads[i + 1:]:
            if len(lvl2) <= len(lvl):
                end = start2
                break
        prefix = ".".join(lvl)
        kind = "types" if re.search(r"types?\s+definitions", title, re.I) else "funcs"
        other = secnum.get("funcs" if kind == "types" else "types")
        items = []
        for pos, txt in allh:
            if pos <= start or pos >= end:
                continue
            num = numbered.get(pos)
            if num and other and num.startswith(other + "."):
                continue  # owned by the sibling section
            items.append((pos, txt))
        # headings this section owns that the conversion placed before it
        for pos, txt in allh:
            num = numbered.get(pos)
            if not num or not num.startswith(prefix + "."):
                continue
            if start <= pos < end:
                continue  # already collected
            items.append((pos, txt))
        items.sort(key=lambda it: it[0])
        return [re.sub(r"^8(?:\.\d+)*\s+", "", txt) for _pos, txt in items]
    return None


def clean(name: str) -> str:
    name = re.sub(r"\s*glyph\[.*$", "", name)
    return name.replace("\\_", "_").strip()


def article_index():
    """spec stem -> (label, link) from articles' front-matter."""
    idx = {}
    for p in sorted(DOCS.rglob("*.md")):
        if "sync-todo" in p.parts or "r21_11" in p.parts or p.name in {"STANDARD.md", "TODO.md", "glossary.md"}:
            continue
        if p.relative_to(DOCS).parts[0] == "api":
            continue
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^spec:\s*(\S+)", text, re.M)
        if m:
            tm = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
            label = tm.group(1) if tm else (p.parent.name if p.name == "index.md" else p.stem)
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


NUM_PREFIX = re.compile(r"^\d+(?:\.\d+)*\.?\s+")
ART_HEAD = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.M)


def material_slug(text: str) -> str:
    """pymdownx.slugs.slugify(case='lower'): lowercase, drop punctuation,
    whitespace -> '-'. Unicode word chars (CJK, _) survive — matches the
    site's Material config."""
    s = re.sub(r"[^\w\s-]", "", text.strip().lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def article_anchors(article: Path) -> dict[str, str]:
    """identifier (lower) -> anchor slug of its FIRST heading occurrence.

    Walks every heading in document order, computing Material slugs with
    the same-seen `_N` dedup mkdocs applies, so the recorded anchor is the
    one the rendered page actually assigns. First occurrence wins: the API
    definition chapter precedes the 配置规范 chapter, whose same-named
    container headings would otherwise shadow the definition."""
    seen: dict[str, int] = {}
    anchors: dict[str, str] = {}
    for m in ART_HEAD.finditer(article.read_text(encoding="utf-8")):
        text = m.group(2).strip()
        ident = NUM_PREFIX.sub("", text).strip()
        if not IDENT_RE.match(ident):
            continue
        base = material_slug(text)
        n = seen.get(base, 0)
        seen[base] = n + 1
        slug = base if n == 0 else f"{base}_{n}"
        anchors.setdefault(ident.lower(), slug)
    return anchors


def render_list(title: str, chapter_note: str, entries, n_items: int) -> list[str]:
    """One A–Z list page: intro + `## <letter>` sections of entries."""
    out = [
        "---",
        f'title: "{title}"',
        "---",
        "",
        f"本页汇总站内已翻译 AUTOSAR 文章所覆盖 SWS 文档第 8 章「API specification」中定义的{chapter_note}，"
        "按字母排序，便于查找；点击标识符直达站内文章中该条目的定义小节，"
        "每条另标注所属文档与发布版本。"
        "**由脚本自动生成，请勿手工编辑**（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；"
        f"源：`~/Workspace/autosar_standard/markdown/.../{RELEASE}/`）。",
        "",
        f"共 **{n_items}** 个条目。",
        "",
    ]
    current = None
    for k in sorted(entries, key=lambda s: (letter_of(s) == "#", s)):
        occ = entries[k]
        letter = letter_of(k)
        if letter != current:
            current = letter
            out += [f"## {letter if letter != '#' else '其他'}", ""]
        for name, kind, stem, label_link, anchor in occ:
            spec_disp = stem.removeprefix("AUTOSAR_CP_")
            # article paths are stored relative to docs/autosar/; the list
            # pages live one level deeper (autosar/api/), so prefix ../
            target = f"../{label_link[1]}"
            out.append(f"**[{name}]({target}#{anchor})**")
            out.append(f"> {kind} · [{label_link[0]}]({target}) · {spec_disp} · {RELEASE}")
            out.append("")
    return out


def build():
    idx = article_index()
    entries_t: "OrderedDict[str, list]" = OrderedDict()  # name.lower() -> [(name, kind, stem, label_link, anchor)]
    entries_f: "OrderedDict[str, list]" = OrderedDict()
    report, n_types, n_funcs = [], 0, 0
    n_articles = len(idx)
    for doc in sorted(SRC.rglob("AUTOSAR_CP_SWS_*.md")):
        if "_artifacts" in doc.parts:
            continue
        stem = doc.stem
        label_link = idx.get(stem)
        if not label_link:
            continue  # not translated — the listing is article-based
        res = extract(doc)
        if res is None:
            report.append(f"  - {stem}: no ch.8 in corpus, article anchors not enumerated")
            continue
        types, funcs = res
        article = DOCS / label_link[1]
        anchors = article_anchors(article)
        listed, dropped = 0, []
        for bucket, names in ((entries_t, types), (entries_f, funcs)):
            kind = "类型" if bucket is entries_t else "函数"
            for name in names:
                anchor = anchors.get(name.lower())
                if anchor is None:
                    dropped.append(name)
                    continue
                bucket.setdefault(name.lower(), []).append((name, kind, stem, label_link, anchor))
                listed += 1
        if dropped:
            report.append(f"  {stem}: {listed} listed, {len(dropped)} dropped (no heading in article): {', '.join(dropped[:8])}{' …' if len(dropped) > 8 else ''}")
        else:
            report.append(f"  {stem}: {listed} listed")
        n_types += sum(1 for t in types if t.lower() in anchors)
        n_funcs += sum(1 for f in funcs if f.lower() in anchors)

    index_page = [
        "---",
        'title: "AUTOSAR API 清单"',
        "---",
        "",
        f"本页汇总站内已翻译 AUTOSAR 文章所覆盖 SWS 文档第 8 章「API specification」中定义的 API，"
        "分为**类型**与**函数**两个清单，各自按字母排序，便于查找；点击标识符直达站内文章中该条目的定义小节。"
        "**由脚本自动生成，请勿手工编辑**"
        "（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；"
        f"源：`~/Workspace/autosar_standard/markdown/.../{RELEASE}/`）。",
        "",
        f"共 **{n_types}** 个类型、**{n_funcs}** 个函数，来自 **{n_articles}** 篇已翻译文章。",
        "",
        "## 文章",
        "",
        "- [AUTOSAR API 类型清单](types.md) —— 已翻译文章中的全部类型定义（源文档 8.2 Type definitions）",
        "- [AUTOSAR API 函数清单](functions.md) —— 已翻译文章中的全部函数定义（源文档 8.3 Function definitions）",
        "",
        "## 相关内容",
        "",
        "- [术语表](../glossary.md)",
        "- [CP AUTOSAR](../index.md)",
        "",
    ]

    types_page = render_list(
        "AUTOSAR API 类型清单",
        "**类型**（源文档 8.2 Type definitions）",
        entries_t,
        n_types,
    )
    funcs_page = render_list(
        "AUTOSAR API 函数清单",
        "**函数**（源文档 8.3 Function definitions）",
        entries_f,
        n_funcs,
    )
    return (
        (OUT_INDEX, "\n".join(index_page)),
        (OUT_TYPES, "\n".join(types_page).rstrip() + "\n"),
        (OUT_FUNCS, "\n".join(funcs_page).rstrip() + "\n"),
    ), report


def main(argv):
    if not SRC.exists():
        print(f"source corpus not found: {SRC}", file=sys.stderr)
        return 2
    pages, report = build()
    if "--check" in argv:
        for out, content in pages:
            current = out.read_text(encoding="utf-8") if out.exists() else ""
            if current != content:
                print(f"STALE: {out.relative_to(ROOT)} differs from regenerated content — run gen_api_list.py", file=sys.stderr)
                return 1
        print("api listing up to date")
        return 0
    API_DIR.mkdir(exist_ok=True)
    for out, content in pages:
        out.write_text(content, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
