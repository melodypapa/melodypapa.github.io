#!/usr/bin/env python3
"""Rewrite docs/autosar/glossary.md into the canonical entry format.

Before (2026-10-30):

    **Term**
    > definition
    > 来源：[Doc A](a.md)（SWS_A · R23-11）
    > 来源：[Doc B](b.md)（SWS_B · R23-11）

After:

    **Term**
    > definition
    >
    > 来源：[Doc A](a.md)（SWS_A）、[Doc B](b.md)（SWS_B）
    {: .glossary-source}

The rewrite also repairs the defects that made the generated HTML wrong:

  * a ``**Term**`` line glued to the previous ``> 来源：`` line was swallowed
    into the previous entry's blockquote (75 entries);
  * the definition and its 来源 shared one ``<p>``, so the attribution was
    typographically identical to the definition;
  * the constant ``· R23-11`` tail repeated on 553 of 554 source lines;
  * one 来源 line had lost its spec id, two source link labels had drifted
    from their article's front-matter title;
  * the page claimed to be alphabetically sorted, but 15 terms sat in the
    wrong letter section and 57 adjacent pairs were out of order;
  * 10 terms appeared twice.

The release is stated once in the page intro instead of on every line.
Terms are re-bucketed into letter sections by their own first letter, so a
term's section no longer depends on where the entry happened to be pasted.

Usage:  python3 .agents/skills/autosar-translate/scripts/rewrite_glossary.py [--check]
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
GLOSSARY = ROOT / "docs" / "autosar" / "glossary.md"

TERM_LINE_RE = re.compile(r"^\*\*(.+?)\*\*")
SOURCE_RE = re.compile(r"^> 来源：(.+)$")
ITEM_RE = re.compile(r"^\[([^\]]+)\]\(([^)]+)\)(（([A-Za-z_0-9]+)）)?$")
# （SWS_ADCDriver · R23-11）  ->  （SWS_ADCDriver）
TAIL_RE = re.compile(r"（([A-Za-z_0-9]+) · R23-11）$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")

# Link labels that drifted from the target article's front-matter title
# (the article title is the canonical link text).
LABEL_FIXES = {
    "AUTOSAR 诊断事件管理器（Dem）": "AUTOSAR Diagnostic Event Manager（诊断事件管理器）",
    "AUTOSAR SoAd（Socket Adaptor）": "AUTOSAR SoAd (Socket Adaptor)",
}

# Terms whose abbreviation denotes two different concepts in two different
# AUTOSAR documents (verified against the R23-11 sources). They stay
# separate and carry their expansion in the heading, in the site's existing
# alias style (``**ADC Result Buffer**（**ADC Streaming Buffer**）``).
#
# Every other duplicated term is one concept: the entries are merged into
# one, keeping the longer definition and unioning the sources.
HOMONYMS = {
    "MSTP": {
        "SWS_DiagnosticLogAndTrace": "Message Type",
        "AUTOSAR_CP_EXP_FunctionalSafetyMeasures": "Microcontroller Specific Test Package",
    },
    "SRS": {
        "SWS_XCP": "Software Requirements Specification",
        "AUTOSAR_CP_EXP_AIOccupantAndPedestrianSafety": "Safety Restraint System",
    },
}

INTRO = (
    "本页汇总各 AUTOSAR 模块文章以及 AUTOSAR TR 术语表（Foundation）的术语，"
    "按字母排序。所有词条均出自 AUTOSAR **R23-11** 版规范文档；"
    "「来源」行注明该词条所引用的规范文档及其 spec 编号。"
)


def split_item(raw: str) -> tuple[str, str, str | None]:
    """Split a 来源 payload into (label, path, spec).

    The constant ``· R23-11`` tail is dropped first: the release is stated
    once in the page intro, not on every source line.
    """
    raw = TAIL_RE.sub(r"（\1）", raw.strip())
    m = ITEM_RE.match(raw)
    if not m:
        raise SystemExit(f"unparsable 来源 payload: {raw!r}")
    return m.group(1), m.group(2), m.group(4)


def split_items(raw: str) -> list[tuple[str, str, str | None]]:
    """Split a 来源 payload into its items.

    A payload holds one item per contributing document, separated by ``、``
    (an already-merged line), or a single item (a line as written by hand).
    """
    items: list[tuple[str, str, str | None]] = []
    for part in raw.split("、"):
        part = part.strip()
        if part:
            items.append(split_item(part))
    return items


def plain(text: str) -> str:
    """The heading text without markdown emphasis."""
    return BOLD_RE.sub(r"\1", text).strip()


def effective_name(term: str) -> str:
    """The name used for section assignment and sorting.

    HTML entities are decoded and a leading bracket (``<Ie>``) is unwrapped,
    so the term sorts under the letter it actually names.
    """
    text = html.unescape(plain(term)).strip()
    m = re.match(r"^<(.+)>$", text)
    if m:
        text = m.group(1)
    return text


def section_of(term: str) -> str:
    """The letter section a term belongs to (``#`` when it names no letter)."""
    for ch in effective_name(term):
        if ch.isalpha():
            return ch.upper()
    return "#"


def sort_key(entry: dict) -> tuple:
    """Case-insensitive sort key on the whole heading, stable on spelling."""
    return (effective_name(entry["name"]).lower(), entry["name"])


def parse(lines: list[str]) -> tuple[list[str], list[dict], list[str]]:
    """Parse the body into (front_matter, entries, original_sections).

    Every ``**Term**`` line starts a new entry, whether or not it is glued to
    the previous entry's blockquote.
    """
    fm_end = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i + 1
                break
    front_matter = lines[:fm_end]

    entries: list[dict] = []
    original_sections: list[str] = []
    current: dict | None = None
    for line in lines[fm_end:]:
        if line.startswith("## "):
            original_sections.append(line[3:].strip())
            current = None
            continue
        m = TERM_LINE_RE.match(line)
        if m and not line.startswith("> "):
            current = {
                "line": line,
                "name": plain(line),
                "def": [],
                "src": [],
            }
            entries.append(current)
            continue
        if line.startswith("> "):
            if current is None:
                continue
            text = line[2:]
            s = SOURCE_RE.match(line)
            if s:
                current["src"].append(s.group(1))
            else:
                current["def"].append(text)
    return front_matter, entries, original_sections


def spec_ids(entry: dict) -> set[str]:
    ids: set[str] = set()
    for raw in entry["src"]:
        for _label, _path, spec in split_items(raw):
            if spec:
                ids.add(spec)
    return ids


def source_key(entry: dict) -> frozenset:
    """The set of source documents an entry cites."""
    return frozenset(
        item for raw in entry["src"] for item in split_items(raw)
    )


def resolve_duplicates(entries: list[dict]) -> tuple[list[dict], int]:
    """Collapse duplicate entries of the same term.

    Entries are first partitioned by the set of documents they cite:

    * **one partition** — the same document lists the term twice (an
      abbreviation table and a prose sentence). One entry is the right
      result; the longer definition wins.
    * **several partitions** — different documents define the same term. The
      "one term is translated once" rule (SKILL.md Step 6.1) keeps one
      definition and appends the other documents as sources — unless the
      term is a registered homonym (HOMONYMS), whose entries stay separate
      and carry their expansion in the heading.
    """
    groups: dict[str, list[dict]] = {}
    for entry in entries:
        groups.setdefault(entry["name"], []).append(entry)

    out: list[dict] = []
    collapsed = 0
    for name, group in groups.items():
        if len(group) == 1:
            out.append(group[0])
            continue

        partitions: dict[frozenset, list[dict]] = {}
        for entry in group:
            partitions.setdefault(source_key(entry), []).append(entry)

        if name in HOMONYMS and len(partitions) > 1:
            # different concepts sharing an abbreviation: keep them apart
            for part in partitions.values():
                out.extend(merge_group(part))
                collapsed += len(part) - 1
            continue

        # one concept: merge every partition into a single entry
        flat = [e for part in partitions.values() for e in part]
        merged = merge_group(flat)
        out.extend(merged)
        collapsed += len(flat) - 1
    return out, collapsed


def merge_group(group: list[dict]) -> list[dict]:
    """Merge a group of same-term entries into one.

    The longer definition wins (it is the more informative one) and the
    sources are unioned in first-seen order.
    """
    if len(group) == 1:
        return group
    keeper = group[0]
    for entry in group[1:]:
        if len("".join(entry["def"])) > len("".join(keeper["def"])):
            keeper["def"] = entry["def"]
        known = {item for raw in keeper["src"] for item in split_items(raw)}
        for raw in entry["src"]:
            for item in split_items(raw):
                if item not in known:
                    keeper["src"].append(raw)
                    known.add(item)
                    break
    return [keeper]


def disambiguate_homonyms(entries: list[dict]) -> int:
    """Give each homonym its expansion in the heading."""
    changed = 0
    for entry in entries:
        # the base name, so an already-disambiguated heading is not suffixed twice
        base = re.sub(r"（[^（）]*）$", "", entry["name"])
        table = HOMONYMS.get(base)
        if not table:
            continue
        ids = spec_ids(entry)
        alias = next((v for k, v in table.items() if k in ids), None)
        if alias is None:
            continue
        entry["name"] = f"{base}（{alias}）"
        entry["line"] = f"**{entry['name']}**"
        changed += 1
    return changed


def build_spec_map(entries: list[dict]) -> dict[str, str]:
    """Map a source path to its spec id, harvested from the page itself.

    The glossary's spec ids are not always the article's front-matter
    ``spec:`` (e.g. ``SWS_DiagnosticEventManager`` vs
    ``AUTOSAR_CP_SWS_DiagnosticEventManager``), so the page is its own
    source of truth. Only unambiguous paths are mapped.
    """
    seen: dict[str, set[str]] = {}
    for entry in entries:
        for raw in entry["src"]:
            for _label, path, spec in split_items(raw):
                if spec:
                    seen.setdefault(path, set()).add(spec)
    return {path: next(iter(specs)) for path, specs in seen.items() if len(specs) == 1}


def normalize_items(entry: dict, spec_map: dict[str, str]) -> list[str]:
    """Normalize one entry's 来源 payloads: repair, de-duplicate, drop release."""
    items: list[str] = []
    for raw in entry["src"]:
        for label, path, spec in split_items(raw):
            if spec is None:
                # the one line that lost its spec id
                spec = spec_map.get(path)
            label = LABEL_FIXES.get(label, label)
            item = f"[{label}]({path})" + (f"（{spec}）" if spec else "")
            if item not in items:
                items.append(item)
    return items


def render(front_matter: list[str], entries: list[dict]) -> str:
    spec_map = build_spec_map(entries)

    buckets: dict[str, list[dict]] = {}
    for entry in entries:
        buckets.setdefault(section_of(entry["name"]), []).append(entry)

    out: list[str] = list(front_matter)
    out.append("")
    out.append(INTRO)
    out.append("")

    for letter in sorted(buckets):
        out.append(f"## {letter}")
        out.append("")
        for entry in sorted(buckets[letter], key=sort_key):
            out.append(entry["line"])
            out.extend(f"> {d}" for d in entry["def"])
            out.append(">")
            items = normalize_items(entry, spec_map)
            out.append("> 来源：" + "、".join(items))
            out.append("{: .glossary-source}")
            out.append("")

    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report what would change without writing the file",
    )
    args = parser.parse_args()

    text = GLOSSARY.read_text(encoding="utf-8")
    front_matter, entries, original_sections = parse(text.split("\n"))
    merged, merged_count = resolve_duplicates(entries)
    disambiguated = disambiguate_homonyms(merged)
    out = render(front_matter, merged)

    new_sections = re.findall(r"^## (.+)$", out, re.M)
    print(f"glossary: {len(entries)} entries -> {len(merged)} "
          f"(merged {merged_count} duplicate entries, "
          f"disambiguated {disambiguated} homonyms)")
    print(f"glossary: sections {original_sections} -> {new_sections}")
    print(f"glossary: {out.count('{: .glossary-source}')} source attributions classed")

    if args.check:
        print("glossary: --check, file not written")
        return 0

    GLOSSARY.write_text(out, encoding="utf-8")
    print("glossary: written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
