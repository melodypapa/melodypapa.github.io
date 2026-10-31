#!/usr/bin/env python3
"""Check the nav and the three derived index levels of this site.

The `nav` block in `mkdocs.yml` is the source of truth for the site
structure. Three hand-maintained index pages are derived from it:

  docs/index.md                      site home: one bullet per top-level tab
  docs/autosar/index.md              CP AUTOSAR overview: full page tree
  docs/autosar/<section>/index.md    section landing page: its whole branch

This is the mechanical tripwire for SKILL.md Step 6.3 / Phase A check 4.
It verifies what the strict build cannot:

  1. every nav target exists on disk;
  2. the CP AUTOSAR overview links every page of that nav branch;
  3. every CP AUTOSAR section landing page links every page of its branch;
  4. the site home links every top-level nav tab;
  5. every internal link on those index pages resolves.

`--titles` additionally audits the `English（中文）` structure of CP AUTOSAR
article titles, including empty Chinese halves and nested parentheses, and
lists violations (report-only). Semantic equivalence still requires checking
the title against its `spec:` source; this script does not judge translations.

Exit codes: 0 = all checks pass, 1 = at least one check failed,
2 = usage/IO/config error.

Usage:
  check_indexes.py [--root <repo-root>] [--titles]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    sys.exit("check_indexes: PyYAML is required (use the mkdocs venv)")

CP_LABEL = "CP AUTOSAR"
HOME = "首页"
LINK_RE = re.compile(r"\]\(([^)]+)\)")


class _Loader(yaml.SafeLoader):
    """SafeLoader that tolerates mkdocs' python/name: tags."""


_Loader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:", lambda loader, suffix, node: suffix
)


def load_nav(root: Path):
    with open(root / "mkdocs.yml", encoding="utf-8") as fh:
        cfg = yaml.load(fh, Loader=_Loader)
    nav = cfg.get("nav")
    if not isinstance(nav, list):
        raise ValueError("mkdocs.yml has no explicit nav list")
    return nav


def pages_of(items) -> list[str]:
    """Flatten a nav subtree into page paths, in nav order."""
    out: list[str] = []
    for item in items:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    out.append(value)
                elif isinstance(value, list):
                    out.extend(pages_of(value))
    return out


def is_page(value) -> bool:
    return isinstance(value, str) and value.endswith(".md")


def landing_page(value):
    """Return the unlabeled first child when it is a section landing page."""
    if isinstance(value, list) and value and is_page(value[0]):
        return value[0]
    return None


def resolve(page: Path, target: str) -> Path:
    """Resolve one markdown link target against the file that contains it."""
    target = unquote(target.strip())
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    path = (page.parent / target).resolve()
    if target.endswith("/") or path.is_dir():
        path = path / "index.md"
    return path


def links_in(page: Path) -> set[Path]:
    text = page.read_text(encoding="utf-8")
    out: set[Path] = set()
    for raw in LINK_RE.findall(text):
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        out.add(resolve(page, raw))
    return out


def rel(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[4],
        help="repository root (default: inferred from this script's path)",
    )
    parser.add_argument(
        "--titles",
        action="store_true",
        help="also audit article-title structure (report-only)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    docs = root / "docs"

    try:
        nav = load_nav(root)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"check_indexes: cannot read mkdocs.yml: {exc}")
        return 2

    failures: list[str] = []

    # 1. Every nav target exists -------------------------------------------
    all_nav_pages = pages_of(nav)
    for page in all_nav_pages:
        if not (docs / page).is_file():
            failures.append(f"nav target missing on disk: {page}")

    # Locate the CP AUTOSAR branch ----------------------------------------
    cp_branch = None
    top_sections: list[tuple[str, object]] = []
    for item in nav:
        if not isinstance(item, dict):
            continue
        for label, value in item.items():
            top_sections.append((str(label), value))
            if str(label) == CP_LABEL:
                cp_branch = value
    if cp_branch is None:
        failures.append(f"nav has no '{CP_LABEL}' top-level tab")

    # Section landing pages inside the CP AUTOSAR branch -----------------
    cp_landings: list[str] = []
    if isinstance(cp_branch, list):
        for child in cp_branch:
            if not isinstance(child, dict):
                continue
            for branch in child.values():
                landing = landing_page(branch)
                if landing is not None:
                    cp_landings.append(landing)

    # 2. CP AUTOSAR overview links every page of the branch ----------------
    index_pages = [docs / "index.md"]
    landing_count = len(cp_landings)
    if cp_branch is not None:
        overview = docs / "autosar" / "index.md"
        index_pages.append(overview)
        expected = [p for p in pages_of(cp_branch) if p != "autosar/index.md"]
        linked = {rel(docs, p) for p in links_in(overview)}
        missing = [p for p in expected if p not in linked]
        if missing:
            failures.append(
                "CP AUTOSAR overview misses {} page(s): {}".format(
                    len(missing), ", ".join(missing[:8])
                )
            )

        # 3. Section landing pages link their whole branch ------------------
        for label, value in top_sections:
            if label != CP_LABEL or not isinstance(value, list):
                continue
            for child in value:
                if not isinstance(child, dict):
                    continue
                for branch in child.values():
                    landing = landing_page(branch)
                    if landing is None or not isinstance(branch, list):
                        continue
                    page = docs / landing
                    index_pages.append(page)
                    expected = [p for p in pages_of(branch) if p != landing]
                    linked = {rel(docs, p) for p in links_in(page)}
                    missing = [p for p in expected if p not in linked]
                    if missing:
                        failures.append(
                            "landing page {} misses {} page(s): {}".format(
                                landing, len(missing), ", ".join(missing[:8])
                            )
                        )

    # 4. Homepage links every top-level tab --------------------------------
    home = docs / "index.md"
    home_links = {rel(docs, p) for p in links_in(home)}
    for label, value in top_sections:
        pages = pages_of(value) if isinstance(value, list) else [value]
        if label == HOME or pages[:1] == ["index.md"]:
            continue
        if not pages:
            failures.append(f"nav tab {label!r} has no page to link")
            continue
        target = pages[0]
        if target not in home_links:
            failures.append(
                f"home misses top-level tab {label!r} (expected link to {target})"
            )

    # 5. Every internal link on those index pages resolves -----------------
    for page in index_pages:
        if not page.is_file():
            continue
        for target in sorted(links_in(page)):
            if not target.is_file():
                try:
                    shown = rel(docs, target)
                except ValueError:
                    shown = str(target)
                failures.append(f"broken link in {rel(docs, page)}: {shown}")

    # 6. Title structure audit (report-only) -------------------------------
    title_issues: list[tuple[str, str, str]] = []
    if args.titles and cp_branch is not None:
        skip = set(cp_landings) | {
            "autosar/index.md",
            "autosar/glossary.md",
            "autosar/api/index.md",
            "autosar/api/types.md",
            "autosar/api/functions.md",
        }
        for page in pages_of(cp_branch):
            if page in skip or not page.startswith("autosar/"):
                continue
            path = docs / page
            if not path.is_file():
                continue
            match = re.search(
                r"^title:\s*(.+)$", path.read_text(encoding="utf-8")[:1500], re.M
            )
            if not match:
                continue
            title = match.group(1).strip().strip('"').strip("'")
            opening = title.find("（")
            if opening < 0 or not title.endswith("）"):
                continue
            outside = title[:opening].strip()
            inside = title[opening + 1 : -1].strip()
            inside_has_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in inside)
            outside_has_cjk = any("\u4e00" <= ch <= "\u9fff" for ch in outside)
            if not outside or not inside:
                title_issues.append((page, title, "missing Chinese title half"))
            elif (
                outside_has_cjk
                and re.search(r"[A-Za-z]", inside)
                and not inside_has_cjk
            ):
                title_issues.append((page, title, "Chinese-first bilingual title"))
            elif not inside_has_cjk:
                title_issues.append((page, title, "missing Chinese title half"))

    if args.titles:
        print(f"title structure: {len(title_issues)} violation(s) of English（中文）")
        for page, title, reason in title_issues:
            print(f"  TITLE {page}: {title} ({reason})")

    if failures:
        print(f"index checks: {len(failures)} failure(s)")
        for line in failures:
            print("  FAIL", line)
        return 1

    print(
        "index checks: OK - nav {} targets, CP AUTOSAR overview {} pages, "
        "{} section landing pages, {} top-level tabs, 0 broken links".format(
            len(all_nav_pages),
            len([p for p in pages_of(cp_branch) if p != "autosar/index.md"])
            if cp_branch is not None
            else 0,
            landing_count,
            len([l for l, _ in top_sections if l != HOME]),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
