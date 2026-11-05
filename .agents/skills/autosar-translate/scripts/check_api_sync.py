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
# The name class includes "." so templated names survive intact
# ("BndM_Block&lt;BlockId.Shortname&gt;Type" — R23-11 SWS_BulkNvDataManager 8.2.3).
SRC_RE = re.compile(r"(?:^|[^0-9.])8\.([23])\.(\d+)\s+\**\s*([A-Za-z][A-Za-z0-9_.\\&;<>]*)")
# Grouped layout: leaf functions one level deeper ("## 8.3.1.1  GetVersionInfo"
# under "## 8.3.1  General"). When such 4-level headings exist they are the
# real function entries; the 3-level headings are group captions.
# NvM (R23-11) nests one level deeper still: "## 8.3.3.6  Callback notifications"
# is a 4-level group caption whose leaves are 5-level ("## 8.3.3.6.1 NVRAM
# Manager job end notification without error"). The leaf pattern therefore
# matches 4- OR 5-level numbers; parent filtering below drops any entry whose
# number is extended by a deeper entry (a group caption), whatever its depth.
# Some extracted leaf headings split an escaped underscore from the next
# identifier token (for example, ``Dcm\_ SetActiveDiagnostic``). Capture that
# token as part of the name; norm() removes the separator and extraction slash.
SRC_LEAF_RE = re.compile(
    r"(?:^|[^0-9.])8\.(?P<chap>[23])\.(?P<num>\d+(?:\.\d+){1,2})\s+\**\s*"
    # name: one identifier token plus any number of continuation tokens — the
    # prose leaf headings of NvM's callbacks span seven words; the historical
    # single-continuation `?` (added for "Dcm\_ SetActiveDiagnostic") is not
    # enough
    r"(?P<name>[A-Za-z][A-Za-z0-9_.\\&;<>]*(?:\s+[A-Za-z][A-Za-z0-9_.\\&;<>]*)*)"
)
ART_RE = re.compile(r"^####\s+7\.([23])\.(\d+)\.\s+(.+?)\s*$")
# Article heading level = numeric depth + 2, so 4-level entries are ##### and
# 5-level entries (NvM callbacks) are ######.
ART_LEAF_RE = re.compile(
    r"^#{5,6}\s+7\.(?P<chap>[23])\.(?P<num>\d+(?:\.\d+){1,2})\.\s+(?P<name>.+?)\s*$"
)

# Structural (non-API) heading names whose Chinese rendering is fixed by the
# site's API-chapter convention. SRC_RE only captures the first English word,
# so "Optional Interfaces" compares as "Optional"; the article renders it as
# 可选接口. The tripwire still enforces counts and order around the alias.
# Likewise the source heading "Extension to Std_ReturnType" is captured as
# "Extension", while the site renders that type heading as
# 「Std_ReturnType 的扩展」 (crypto_driver / crypto_interface / key_manager /
# stbm precedent) — the alias keeps the tripwire from reporting a false
# mismatch on all four articles.
ALIASES = {
    "可选接口": "Optional",
    "Std_ReturnType的扩展": "Extension",
    # NvM (R23-11) names its two callback entries with prose headings ("NVRAM
    # Manager job end notification without/with error"); the article keeps the
    # pre-existing function-name headings (old-article 8.4.1/8.4.2 continuity,
    # site API function listing) — map the source prose names onto them.
    "NVRAMManagerjobendnotificationwithouterror": "NvM_JobEndNotification",
    "NVRAMManagerjobendnotificationwitherror": "NvM_JobErrorNotification",
}


def norm(name: str) -> str:
    r"""Normalize a heading name: drop extraction backslashes and spaces,
    decode PDF-conversion HTML entities so source names like
    ``IoHwAb&lt;Init\_Id&gt;\_ConfigType`` compare equal to the article's
    ``IoHwAb<Init_Id>_ConfigType``."""
    name = name.replace("\\", "").replace(" ", "")
    for ent, ch in (("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&")):
        name = name.replace(ent, ch)
    return ALIASES.get(name, name)


def _drop_parents(entries: list[tuple[str, str]]) -> list[str]:
    """Names of entries that are not a parent of a deeper entry.

    Group captions can sit at any depth (NvM: "8.3.3.6 Callback notifications"
    is a 4-level caption over 5-level leaves); an entry whose number is
    extended by another entry's number is a caption, not an API leaf."""
    nums = [num for num, _ in entries]
    return [
        name
        for num, name in entries
        if not any(other != num and other.startswith(num + ".") for other in nums)
    ]


def source_entries(text: str, chap: str) -> list[str]:
    flat: list[str] = []
    leaf: list[tuple[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("#"):
            continue
        hits = [m for m in SRC_RE.finditer(line) if m.group(1) == chap]
        if hits:
            name = norm(hits[-1].group(3))
            if not flat or flat[-1] != name:  # dedupe merged-heading repeats
                flat.append(name)
        leaf_hits = [m for m in SRC_LEAF_RE.finditer(line) if m.group("chap") == chap]
        if leaf_hits:
            m = leaf_hits[-1]
            if not leaf or leaf[-1][0] != m.group("num"):
                leaf.append((m.group("num"), norm(m.group("name"))))
    leaves = _drop_parents(leaf)
    return leaves if leaves else flat


def article_entries(text: str, chap: str) -> list[str]:
    flat: list[str] = []
    leaf: list[tuple[str, str]] = []
    for line in text.splitlines():
        m = ART_RE.match(line)
        if m and m.group(1) == chap:
            flat.append(norm(m.group(3)))
        m = ART_LEAF_RE.match(line)
        if m and m.group("chap") == chap:
            if not leaf or leaf[-1][0] != m.group("num"):
                leaf.append((m.group("num"), norm(m.group("name"))))
    leaves = _drop_parents(leaf)
    return leaves if leaves else flat


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


def _reconcile_module_prefix(src: list[str], art: list[str]) -> tuple[list[str], list[str]]:
    """Some SWS documents head their API entries with bare names ("8.3.1 Init",
    "8.2.1 ConfigType") while the article headings carry the full identifier
    ("Fw_Init", "Fw_ConfigType") — the Firewall R23-11 precedent. When every
    article entry is positionally the source entry with one shared prefix
    (e.g. "Fw_"), lift the source names by that prefix so the comparison is
    name-preserving instead of failing on the missing module qualifier."""
    if not src or len(src) != len(art):
        return src, art
    prefix = None
    for a, s in zip(art, src):
        if not a.endswith(s):
            return src, art
        p = a[: len(a) - len(s)]
        if prefix is None:
            prefix = p
        elif p != prefix:
            return src, art
    if not prefix:
        return src, art
    return [prefix + s for s in src], art


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

    for chap, art_chap, label in (("2", "2", "types"), ("3", "3", "functions")):
        src = source_entries(src_text, chap)
        art = article_entries(art_text, art_chap)
        print(
            f"{label:9s}: source 8.{chap}.x = {len(src):2d} | article 7.{art_chap}.x = {len(art):2d}"
        )
        if not src and art:
            problems.append(
                f"  {label}: source chapter 8.{chap} parsed as empty while the "
                "article has entries — check for an unparseable source structure "
                "(see gen_api_list.py's known `!` documents) before overriding"
            )
        src, art = _reconcile_module_prefix(src, art)
        problems.extend(diff_names(src, art, label))
        if chap == "3":
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
