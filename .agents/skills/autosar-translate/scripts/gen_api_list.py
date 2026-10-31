#!/usr/bin/env python3
"""Generate the AUTOSAR API listing under docs/autosar/api/ from the site's
TRANSLATED articles — the repository itself is the only input (no external
corpus dependency).

Per article (front-matter `spec:`), identifier-shaped headings are collected
and classified by the article's own section titles:

  类型   — under a 「类型定义」-style section (title containing 类型)
  函数   — under a 「函数定义」/「服务接口」-style section, or default when
           no deciding title is found (prose group headings)
  skipped — under 「导入的类型」 (defined in another article) or 「期望接口」
            (expected interfaces, not module API)
  the scan stops at the 「配置规范」 chapter — configuration containers are
  not API definitions

Each identifier deep-links to its heading anchor (Material slug rules,
including `_1`-style same-seen dedup) inside the article. Dedup across
articles is first-occurrence-wins by identifier.

Output (three pages, regenerate as a set — never hand-edit):
  api/index.md      landing page (intro + 文章 links to the two lists)
  api/types.md      type list, A–Z
  api/functions.md  function list, A–Z

Pure derivation of the articles — never hand-edit the output. Run after any
article/front-matter change (autosar-translate SKILL.md Step 6) and verify
with --check in Phase A.

Usage:
  python .agents/skills/autosar-translate/scripts/gen_api_list.py           # (re)write
  python .agents/skills/autosar-translate/scripts/gen_api_list.py --check   # exit 1 if stale
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

ART_HEAD = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.M)
NUM_PREFIX = re.compile(r"^\d+(?:\.\d+)*\.?\s+")
IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def material_slug(text: str) -> str:
    """pymdownx.slugs.slugify(case='lower'): lowercase, drop punctuation,
    whitespace -> '-'. Unicode word chars (CJK, _) survive — matches the
    site's Material config."""
    s = re.sub(r"[^\w\s-]", "", text.strip().lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def article_index():
    """spec stem -> (label, link, release) from articles' front-matter."""
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
            rm = re.search(r'^release:\s*"?([^"\s]+)"?\s*$', text, re.M)
            idx[m.group(1)] = (label, p.relative_to(DOCS).as_posix(), rm.group(1) if rm else "R23-11")
    return idx


def collect(article: Path):
    """(kind, identifier, slug) triples from the article's own headings.

    Non-identifier headings form a stack; classification walks it from the
    nearest title outward, so identifiers under prose group headings fall
    back to the enclosing 「类型定义」/「函数定义」 section or the chapter.
    First occurrence of an identifier wins (the API definition chapter
    precedes same-named container headings later in the page)."""
    items = []
    seen_ident: set[str] = set()
    seen_slug: dict[str, int] = {}
    stack: list[str] = []
    for m in ART_HEAD.finditer(article.read_text(encoding="utf-8")):
        level, text = len(m.group(1)), m.group(2).strip()
        if level == 2 and "配置规范" in text:
            break  # configuration containers are not API definitions
        ident = NUM_PREFIX.sub("", text).strip()
        if IDENT_RE.match(ident):
            if ident.lower() in seen_ident:
                continue
            kind = "函数"  # default: identifier headings under API-chapter
            # prose group headings count as functions
            for title in reversed(stack):
                if "导入的类型" in title or "期望接口" in title:
                    kind = None
                    break
                if "类型" in title:
                    kind = "类型"
                    break
                if "函数" in title or "服务接口" in title:
                    kind = "函数"
                    break
            if kind is None:
                continue  # under 导入的类型 / 期望接口
            seen_ident.add(ident.lower())
            base = material_slug(text)
            n = seen_slug.get(base, 0)
            seen_slug[base] = n + 1
            items.append((kind, ident, base if n == 0 else f"{base}_{n}"))
        else:
            del stack[level - 2:]
            stack.append(NUM_PREFIX.sub("", text).strip())
    return items


def letter_of(name: str) -> str:
    c = name[0].upper()
    return c if "A" <= c <= "Z" else "#"


def render_list(title: str, chapter_note: str, entries, n_items: int) -> list[str]:
    """One A–Z list page: intro + `## <letter>` sections of entries."""
    out = [
        "---",
        f'title: "{title}"',
        "---",
        "",
        f"本页汇总站内已翻译 AUTOSAR 文章中定义的{chapter_note}，"
        "按字母排序，便于查找；点击标识符直达站内文章中该条目的定义小节，"
        "每条另标注所属文档与发布版本。"
        "**由脚本自动生成，请勿手工编辑**（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；"
        "源：站内已翻译文章的章节标题）。",
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
        for name, kind, spec_disp, release, label_link, anchor in occ:
            # article paths are stored relative to docs/autosar/; the list
            # pages live one level deeper (autosar/api/), so prefix ../
            target = f"../{label_link[1]}"
            out.append(f"**[{name}]({target}#{anchor})**")
            out.append(f"> {kind} · [{label_link[0]}]({target}) · {spec_disp} · {release}")
            out.append("")
    return out


def build():
    idx = article_index()
    entries_t: "OrderedDict[str, list]" = OrderedDict()  # name.lower() -> [(name, kind, spec, release, label_link, anchor)]
    entries_f: "OrderedDict[str, list]" = OrderedDict()
    report, n_types, n_funcs = [], 0, 0
    contributing = set()
    for stem, (label, relpath, release) in sorted(idx.items(), key=lambda kv: kv[1][1]):
        spec_disp = stem.removeprefix("AUTOSAR_CP_")
        t = f = 0
        for kind, ident, anchor in collect(DOCS / relpath):
            if kind == "类型":
                entries_t.setdefault(ident.lower(), []).append((ident, kind, spec_disp, release, (label, relpath), anchor))
                t += 1
            else:
                entries_f.setdefault(ident.lower(), []).append((ident, kind, spec_disp, release, (label, relpath), anchor))
                f += 1
        n_types += t
        n_funcs += f
        if t or f:
            contributing.add(relpath)
        report.append(f"  {relpath}: {t} types {f} funcs")
    n_articles = len(contributing)

    index_page = [
        "---",
        'title: "AUTOSAR API 清单"',
        "---",
        "",
        "本页汇总站内已翻译 AUTOSAR 文章中定义的 API，分为**类型**与**函数**两个清单，"
        "各自按字母排序，便于查找；点击标识符直达站内文章中该条目的定义小节。"
        "**由脚本自动生成，请勿手工编辑**"
        "（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；"
        "源：站内已翻译文章的章节标题）。",
        "",
        f"共 **{n_types}** 个类型、**{n_funcs}** 个函数，来自 **{n_articles}** 篇已翻译文章。",
        "",
        "## 文章",
        "",
        "- [AUTOSAR API 类型清单](types.md) —— 已翻译文章「类型定义」章节中的全部类型",
        "- [AUTOSAR API 函数清单](functions.md) —— 已翻译文章「函数定义」「服务接口」等章节中的全部函数",
        "",
        "## 相关内容",
        "",
        "- [术语表](../glossary.md)",
        "- [CP AUTOSAR](../index.md)",
        "",
    ]

    types_page = render_list(
        "AUTOSAR API 类型清单",
        "**类型**",
        entries_t,
        n_types,
    )
    funcs_page = render_list(
        "AUTOSAR API 函数清单",
        "**函数**",
        entries_f,
        n_funcs,
    )
    return (
        (OUT_INDEX, "\n".join(index_page)),
        (OUT_TYPES, "\n".join(types_page).rstrip() + "\n"),
        (OUT_FUNCS, "\n".join(funcs_page).rstrip() + "\n"),
    ), report


def main(argv):
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
