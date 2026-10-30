#!/usr/bin/env python3
"""Check that an article's sub-headings are translated into Chinese.

Type A articles are Chinese translations of AUTOSAR standard documents.
Their section headings are direct translations of the source headings, so a
heading title must contain Chinese text. The exceptions are *identifier-titled*
headings — API names, type names, config-container names, port and callback
names — which the site keeps verbatim (STANDARD.md §4: "code identifiers stay
untranslated").

This is the mechanical tripwire for SKILL.md Phase A check 2. The heading
audit there (`grep '^## '`) only inspects the level-2 chapter skeleton, so an
untranslated `###`/`####` sub-heading passed it silently; this script closes
that gap.

Identifier-shaped title (exempt):
  - every word of it is not a plain English word — i.e. it is built from
    capitals, digits and underscores (StbM_Init, StbMGeneral, ISRType, IOC,
    IocSend, GlobalTime_Master, ReadPeripheral8, HSE_GPR2);
  - or it names an entity the article's own tables declare — a configuration
    container (`| 模块名称 | Dio |`, `| 容器名称 | X |`), its parent
    (`| 父容器 | Com |`) or a meta-model class (`| 类 | Identifiable |`);
  - or, in a glossary file, it is a chapter-4 term heading (`### 4.1. Abstract
    Platform`): the English term is the entry key and stays verbatim
    (STANDARD.md §7); the Chinese gloss appears in the body
    (`抽象平台（**Abstract Platform**）`).

Everything else is prose and must carry Chinese. Single English words that are
prose rather than identifiers — General, Common, Overview, Accuracy, Variants —
are therefore flagged, which is intended.

Usage:
  check_heading_lang.py <article.md> [<article.md> ...]
  check_heading_lang.py --site [--allow <path-fragment> ...]

`--site` sweeps the Type A module articles of `docs/autosar/`, skipping the
working documents (STANDARD.md, TODO.md), the sync-todo queue files, the
generated glossary and API list — none of them are module articles.

Exit codes: 0 = all headings translated, 1 = violations found, 2 = usage/IO error.
"""

import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*```")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
# The heading's own numbering ("6.4.2.1 ", "C.1. ") is not part of its title.
NUMBER_PREFIX_RE = re.compile(r"^(?:[A-Z]|\d+)(?:\.(?:\d+|[A-Z]))*\.?\s+")
# A table cell that names the very entity the heading documents: a
# configuration container's name, or a meta-model class's name. The heading
# title then IS an identifier (Dio, Crypto, Spi, ARPackage, Code) and stays
# untranslated. The name may carry a trailing annotation (| 类 | `X`（抽象） |).
CONTAINER_NAME_RE = re.compile(
    r"^\|\s*(?:模块名称|容器名称|父容器|类)\s*\|\s*(?:`([^`]+)`|([^|]+?))(?:\s*[（(][^|]*)?\s*\|"
)
# A plain English word: capitalized ("General", "Driver", "Handling") or
# lowercase ("and", "structure"). A heading title built only from tokens that
# are *not* plain English words is an identifier — StbM_Init, StbMGeneral,
# ISRType, IOC, IocSend, GlobalTime_Master, ReadPeripheral8, HSE_GPR2 — and
# stays untranslated. Single letters and all-caps tokens are not English words.
ENGLISH_WORD_RE = re.compile(r"^(?:[A-Z][a-z]{2,}|[a-z]{2,})$")


def is_identifier_titled(title: str, container_names: set[str]) -> bool:
    """True for API/type/container/port names, which stay untranslated."""
    if title in container_names:
        return True
    return not any(ENGLISH_WORD_RE.match(tok) for tok in title.split())


def heading_title(raw: str) -> str:
    """Strip the heading's numbering prefix and Markdown emphasis."""
    title = raw.strip()
    title = NUMBER_PREFIX_RE.sub("", title)
    title = title.replace("`", "").replace("*", "")
    return title.strip()


def is_glossary_term(line: str) -> bool:
    """True for a glossary entry heading — the English term is the entry key.

    In `tr_glossary` (and any glossary file) chapter 4 is 术语定义; its
    `### 4.N. <English term>` headings are the defined terms themselves, not
    prose to be translated. STANDARD.md §7 keeps term names verbatim, so the
    heading stays English even though it carries no Chinese (the body gives the
    Chinese gloss: `抽象平台（**Abstract Platform**）`).
    """
    m = HEADING_RE.match(line)
    if not m:
        return False
    # m.group(2) is the heading text with the `### ` prefix already removed;
    # a glossary term entry is any heading whose number is under chapter 4.
    return bool(re.match(r"^4\.(?:\d+\.)*\d+\.?\s+\S", m.group(2)))


def check(path: Path) -> list[tuple[int, str]]:
    """Return (line number, heading) pairs that carry no Chinese."""
    lines = path.read_text(encoding="utf-8").splitlines()
    # Names the article's own tables declare: configuration containers, their
    # parent containers, and meta-model classes. A heading carrying one of
    # these names stands for that entity, so it is an identifier.
    declared = declared_names(lines)
    is_glossary = "glossary" in path.as_posix()
    violations: list[tuple[int, str]] = []
    in_fence = False
    for lineno, line in enumerate(lines, 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        if is_glossary and is_glossary_term(line):
            continue
        title = heading_title(m.group(2))
        if not title:
            continue
        if CJK_RE.search(title):
            continue
        if is_identifier_titled(title, declared):
            continue
        violations.append((lineno, line.rstrip()))
    return violations


def declared_names(lines: list[str]) -> set[str]:
    """Entity names the article's tables declare (containers, classes).

    `| 模块名称 | X |` / `| 容器名称 | X |` name a configuration container,
    `| 父容器 | X |` names its parent, and `| 类 | X |` names a meta-model
    class. A heading whose title is one of these names stands for that entity.
    """
    names: set[str] = set()
    for line in lines:
        m = CONTAINER_NAME_RE.match(line)
        if m:
            names.add((m.group(1) or m.group(2)).replace("`", "").strip())
    return names


def iter_site(corpus: Path, allow: list[str]):
    """Yield the Type A module articles of the AUTOSAR corpus.

    The corpus also holds working documents (STANDARD.md, TODO.md), the
    sync-todo queue files, the generated glossary and API list, and the
    section landing pages — none of them are module articles, so they are
    out of scope for this check.
    """
    for path in sorted(corpus.rglob("*.md")):
        rel = path.relative_to(corpus).as_posix()
        if any(frag in rel for frag in allow):
            continue
        if rel in ("STANDARD.md", "TODO.md", "glossary.md", "api_reference.md"):
            continue
        if rel.startswith("sync-todo/"):
            continue
        # tr_glossary is a guide/topic article (STANDARD.md §7 exempt): its
        # ch.4 `### 4.x. <Term>` headings are term names that stay verbatim.
        if rel.startswith("foundation/general/tr_glossary/"):
            continue
        if path.name != "index.md":
            continue
        yield path


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2

    site = False
    allow: list[str] = []
    targets: list[Path] = []
    for arg in args:
        if arg == "--site":
            site = True
        elif arg == "--allow":
            continue
        elif arg.startswith("--allow="):
            allow.append(arg.split("=", 1)[1])
        elif arg.startswith("--"):
            print(f"! unknown option: {arg}")
            return 2
        else:
            targets.append(Path(arg))

    # "--allow X Y" collects the following bare paths as allowances.
    if "--allow" in args:
        i = args.index("--allow")
        rest = args[i + 1 :]
        j = 0
        while j < len(rest) and not rest[j].startswith("--"):
            allow.append(rest[j])
            j += 1

    if site:
        repo = Path(__file__).resolve().parents[4]
        corpus = repo / "docs" / "autosar"
        if not corpus.is_dir():
            print(f"! cannot locate the AUTOSAR corpus at {corpus}")
            return 2
        paths = list(iter_site(corpus, allow))
    else:
        paths = targets

    if not paths:
        print("! no files to check")
        return 2

    total = 0
    for path in paths:
        if not path.is_file():
            print(f"! not a file: {path}")
            return 2
        violations = check(path)
        if violations:
            total += len(violations)
            print(f"{path}: {len(violations)} untranslated heading(s)")
            for lineno, line in violations:
                print(f"  L{lineno}: {line}")

    if total:
        print(f"== heading language: {total} violation(s) — sub-headings must be "
              "translated (identifier-titled headings are exempt) ==")
        return 1

    scope = f"{len(paths)} file(s)" if site else f"{len(paths)} file(s)"
    print(f"== heading language: OK — all sub-headings translated ({scope}) ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
