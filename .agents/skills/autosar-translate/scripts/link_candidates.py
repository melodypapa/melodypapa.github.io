#!/usr/bin/env python3
"""link_candidates.py — potential-links census and intra-article link applier.

Phase A check 9 (census) + Step 2 helper (apply) of the autosar-translate
skill. See SKILL.md Step 5 "Potential links" and Phase A check 9.

Usage:
  link_candidates.py --list <article.md>    # census only (no modification)
  link_candidates.py --apply <article.md>   # apply intra-article links

Applied class (restoration of the source PDF's own hyperlinks):
  - type mentions   (#### 7.2.x headings)  -> that heading's anchor
  - constant mentions (bold bullets inside §7.2 sections) -> the type's anchor
  - function mentions (#### 7.3.x headings) -> that heading's anchor
Excluded: headings, code fences, front-matter, each name's own defining
section, everything from the first `## 8` heading on (ch.8/9 Range tables
are definitional context). Report-only classes: 参见/参考/详见 lines and
prose `[n]` markers — candidates for a user decision, never auto-added.
"""
import re
import sys


def slug_of(num: str, title: str) -> str:
    # Material/uslugify behaviour observed on this site: dots stripped from the
    # number ("3.1." -> "31"), title lowercased with spaces -> '-', '_' kept.
    num = num.rstrip(".")
    num = num.replace(".", "")
    title = title.strip().lower()
    title = re.sub(r"\s+", "-", title)
    return f"{num}-{title}"


def collect(article: str):
    lines = article.splitlines()
    headings = []  # (lineno, level, num, title, slug)
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,6}) (\d[\d.]*)\.?\s+(.+?)\s*$", ln)
        if m:
            headings.append((i, len(m.group(1)), m.group(2), m.group(3), slug_of(m.group(2), m.group(3))))

    defs = {}  # NAME -> anchor
    const_map = {}  # CONST -> enclosing 7.2.x anchor
    cur72 = None
    section_range = {}  # name -> (start_line, end_line) of its own section
    for idx, (i, lvl, num, title, slug) in enumerate(headings):
        end = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines)
        if lvl == 4 and num.startswith("7.2."):
            m = re.match(r"(\d+\.\d+\.\d+)\.?\s+(.+)", num + " " + title) if False else None
        # names from #### headings
        if lvl == 4:
            m = re.match(rf"{re.escape(num)}\.?\s+(.+)$", title) or (None, title)
            name = title
            section_range[name] = (i, end)
            if num.startswith("7.2."):
                defs[name] = slug
                cur72 = (name, slug)
            elif num.startswith("7.3."):
                defs[name] = slug
        # constants: bold bullets inside a 7.2 section body
    for i, ln in enumerate(lines):
        if cur72:
            m = re.match(r"^\*\s+\*\*([A-Za-z][A-Za-z0-9_]+)\*\*", ln)
            # bullets look like '* **NAME**（...' possibly with leading spaces
            m = re.match(r"^\s*\*\s+\*\*([A-Za-z][A-Za-z0-9_]+)\*\*", ln)
            if m and headings:
                # find enclosing 7.2.x section
                enc = None
                for (j, lvl, num, title, slug) in headings:
                    if j > i:
                        break
                    if lvl == 4 and num.startswith("7.2."):
                        enc = slug
                if enc:
                    const_map.setdefault(m.group(1), enc)
    # constants must be scanned per line with enclosing-section tracking; redo properly
    const_map = {}
    enc72 = None
    heading_at = {i: h for h in headings for i in [h[0]]}
    for i, ln in enumerate(lines):
        if i in heading_at:
            h = heading_at[i]
            enc72 = h[4] if (h[1] == 4 and h[3].startswith("7.2.")) else (None if h[1] <= 3 else enc72)
            continue
        m = re.match(r"^\s*\*\s+\*\*([A-Za-z][A-Za-z0-9_]+)\*\*", ln)
        if m and enc72:
            const_map.setdefault(m.group(1), enc72)
    defs.update(const_map)
    return lines, headings, defs, section_range



# --- semantic pattern catalog (2026-10-24, corpus survey) -------------------
# [n] in prose == "Related documentation, entry n" — a two-hop reference:
#   citation -> §3.1 entry n -> external document OR a site article/page.
# Classification is by the entry's AUTOSAR_CP_* document id (NEVER by title
# substring: "Requirements on Port Driver" (SRS_PortDriver) is NOT the site's
# Port article). SITE targets exist on this site; EXTERNAL needs a curated
# official URL before it can become a link (check 8 then applies).
DOC_TARGETS = {
    "swsbswmodemanager": ("SITE", "BswM article", "../basic_software_mode_manager/"),
    "swsecustatemanager": ("SITE", "EcuM article", "../ecu_state_manager/"),
    "expmodemanagementguide": ("SITE", "Mode-management guide", "../guide_to_mode_management/"),
    "swsdiodriver": ("SITE", "DIO article", "../dio_driver/"),
    "swsportdriver": ("SITE", "PORT article", "../port_driver/"),
    "swspwmdriver": ("SITE", "PWM article", "../pwm_driver/"),
    "swsocudriver": ("SITE", "OCU article", "../ocu_driver/"),
    "swsicudriver": ("SITE", "ICU article", "../icu_driver/"),
    "swsadcdriver": ("SITE", "ADC article", "../adc_driver/"),
    "swsbswgeneral": ("EXTERNAL", "SWS_BSWGeneral", None),
    "tpsecuconfiguration": ("EXTERNAL", "TPS_ECUConfiguration", None),
    "explayeredsoftwarearchitecture": ("EXTERNAL", "EXP_LayeredSoftwareArchitecture", None),
    "swsrte": ("EXTERNAL", "SWS_RTE", None),
    "expvfb": ("EXTERNAL", "EXP_VFB", None),
    "srsbswgeneral": ("EXTERNAL", "SRS_BSWGeneral", None),
    "swsmcudriver": ("EXTERNAL", "SWS_MCUDriver", None),
    "swscantransceiverdriver": ("EXTERNAL", "SWS_CANTransceiverDriver", None),
    "swssoftwarecomponenttemplate": ("EXTERNAL", "SWCT", None),
    "trgbswmoduledocumentlist": ("EXTERNAL", "TR_BSWModuleList", None),
    "trbswmoduledocumentlist": ("EXTERNAL", "TR_BSWModuleList", None),
    "swsbswmodulelist": ("EXTERNAL", "TR_BSWModuleList", None),
}


def classify_doc(title: str, docid: str = ""):
    if title and re.sub(r"[^a-z]", "", title.lower()) == "glossary":
        return ("SITE", "site glossary", "/autosar/glossary/")
    key = re.sub(r"[^a-z]", "", docid.lower())
    key = key.replace("autosar", "", 1)
    if key.startswith("cp"):
        key = key[2:]
    if key in DOC_TARGETS:
        return DOC_TARGETS[key]
    return ("EXTERNAL", None, None)


def parse_entries31(article: str):
    t = article
    sec = re.search(r"### 3\.1\..*?(?=### 3\.2)", t, re.S)
    entries = {}
    if sec:
        blocks = re.split(r"(?=^\[\d+\])", sec.group(0), flags=re.M)
        for b in blocks:
            m = re.match(r"^\[(\d+)\]\s+(.+)$", b, re.M)
            if not m:
                continue
            n, title = m.group(1), m.group(2).strip()
            d = re.search(r"(AUTOSAR_[A-Z]+_[A-Za-z]+)", b)
            entries[n] = (title, d.group(1) if d else "")
    return entries


def census(article: str):
    entries31 = parse_entries31(article)
    lines, headings, defs, _ = collect(article)
    fence = False
    stop = None
    for i, ln in enumerate(lines):
        if re.match(r"^## 8\.|^## 9\.", ln):
            stop = i
            break
    id_lines = can_lines = n_lines = 0
    resolutions = {}
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith(("#", "---")) or (stop and i >= stop):
            continue
        if i < 8 and ln.startswith(("title:", "---")):
            continue
        hits = [n for n in defs if re.search(rf"(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])", ln)]
        if hits:
            id_lines += 1
        if re.search(r"参见|参考|详见", ln):
            can_lines += 1
        for m in re.finditer(r"(?<!\])\[(\d+)(?:,\s*[^\]]+)?\](?!\()", ln):
            n_lines += 1
            n = m.group(1)
            ent = entries31.get(n)
            if ent:
                title, docid = ent
                cls, label, target = classify_doc(title, docid)
                resolutions.setdefault((n, title[:40], cls, label or "?"), 0)
                resolutions[(n, title[:40], cls, label or "?")] += 1
    print(f"identifier-mention lines: {id_lines}")
    print(f"参见/参考/详见 lines (candidates): {can_lines}")
    print(f"prose [n] citation lines: {n_lines}")
    if resolutions:
        print("  [n] resolutions (entry -> document -> class):")
        for (n, title, cls, label), cnt in sorted(resolutions.items(), key=lambda x: int(x[0][0])):
            print(f"    [{n}] {title} -> {cls}:{label} x{cnt}")


def apply_links(article: str):
    lines, headings, defs, section_range = collect(article)
    fence = False
    stop = None
    for i, ln in enumerate(lines):
        if re.match(r"^## 8\.|^## 9\.", ln):
            stop = i
            break
    names = sorted(defs, key=len, reverse=True)
    changed = 0
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith("#") or (stop and i >= stop):
            continue
        orig = ln
        for n in names:
            if n not in ln:
                continue
            sr = section_range.get(n)
            if sr and sr[0] <= i < sr[1]:
                continue  # own defining section
            pat = re.compile(rf"\*\*{re.escape(n)}\*\*|(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])")
            def sub(m):
                tok = m.group(0)
                if tok.startswith("["):
                    return tok  # already linked
                inner = tok.strip("*")
                return f"[{tok}](#{defs[n]})"
            ln2 = pat.sub(sub, ln)
            if ln2 != ln:
                ln = ln2
        if ln != orig:
            lines[i] = ln
            changed += 1
    out = "\n".join(lines) + "\n"
    # verify anchors
    anchors = set(h[4] for h in headings)
    bad = [a for a in re.findall(r"\]\(#([^)]+)\)", out) if a not in anchors]
    if bad:
        print(f"UNRESOLVED ANCHORS: {sorted(set(bad))}")
        sys.exit(1)
    print(f"lines changed: {changed}; all link anchors resolve")
    return out


if __name__ == "__main__":
    mode, path = sys.argv[1], sys.argv[2]
    article = open(path).read()
    if mode == "--list":
        census(article)
    elif mode == "--apply":
        out = apply_links(article)
        open(path, "w").write(out)
    else:
        print(__doc__)
        sys.exit(2)
