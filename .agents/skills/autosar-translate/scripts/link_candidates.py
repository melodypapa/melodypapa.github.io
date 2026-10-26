#!/usr/bin/env python3
"""link_candidates.py — potential-links census and intra-article link applier.

Phase A check 9 (census) + Step 5 helper (apply) of the autosar-translate
skill. See SKILL.md Step 5 "Potential links" and Phase A check 9.

Usage:
  link_candidates.py --list <article.md>    # census only (no modification)
  link_candidates.py --apply <article.md>   # apply intra-article links

Applied class (restoration of the source PDF's own hyperlinks):
  - type mentions      (identifier-titled ch.7 headings) -> that heading's
    anchor
  - constant mentions  (bold bullets inside a 7.2.x section) -> its anchor
  - error-code mentions (X_E_Y-style codes in the 错误-titled §6 subsections'
    tables — DIO/PWM 6.6.x 开发错误, EcuM 6.12/6.13) -> that section's anchor
  - function mentions  (identifier-titled ch.7 headings — functions,
    callbacks, callouts, scheduled functions, port interfaces) -> that
    heading's anchor
  - prose citation markers [n] -> the §3.1 registry entry's own anchor
    (`<a id="ref-n"></a>` + `[\\[n\\]](#ref-n)`, user decision 2026-10-27 —
    brackets stay visible: the plain `[n](#ref-n)` form rendered as bare n):
    restores the source PDF's citation hyperlink. Only numbers the registry
    defines convert; the WHOLE article is scanned (a citation is a citation
    everywhere — no 配置规范 stop), but headings, code fences, inline code,
    registry lines and **译者注：** lines never convert. --ref-skip n,n
    exempts user-approved mismatch numbers (census context names a different
    document than the entry title, e.g. "ECU Configuration [5]" vs entry [5]
    Glossary in SWS_EcuM).

Function/type entries are headings whose title is a plain ASCII identifier.
This handles BOTH API-chapter layouts: one-function-per-####-heading (PWM,
DIO, ...) and grouped #### groups with the functions at ###### level (EcuM
7.3.1 通用 -> 7.3.1.1 EcuM_GetVersionInfo). A Chinese group title (通用,
状态管理, ...) is not an identifier and is never a link target — a previous
version matched those and tried to link every occurrence of the word.
Scan region for --apply: front matter .. the chapter BEFORE 配置规范 — the
config-spec tables are definitional context (parameter cells define, not
mention). 时序图 prose is ordinary prose and is scanned since the chapter's
2026-10-24 unban (old behaviour stopped at `## 8` and missed it). Applying is
idempotent — existing markdown links are masked, never re-wrapped.
Report-only classes (user decisions, never auto-added): §7.2 constant bullets
(STD_HIGH, ICU_MODE_* — no corpus article links enum/mode values, audited
2026-10-25), 参见/参考/详见 lines, the citation two-hop resolution (entry ->
document -> SITE/EXTERNAL class), cross-article module mentions. The census
also reports UNRESOLVED citation numbers (not in the §3.1 registry — source
typos like EcuM's [23], never linked, 译者注 is a user decision) and UNLINKED
resolved ones (context shown so a document-name mismatch is caught).
"""
import os
import re
import sys

CONFIG_TITLE = "配置规范"  # --apply stops before this chapter (definitional tables)

# Registry entry line: optional invisible #ref-n anchor prefix + "[n] Title"
# (the prefix is what --apply adds; census/parse must tolerate both states)
REF_ANCHOR = r'(?:<a id="ref-\d+"></a>)?'

MD_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")

# A heading title that is a plain ASCII code identifier (types, functions,
# callbacks, callouts) — as opposed to a Chinese group/section title.
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_]*")


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

    defs = {}  # NAME -> anchor (types, functions, error codes — the applied class)
    consts = {}  # NAME -> anchor — §7.2 constant bullets (STD_HIGH, ICU_MODE_*):
    # report-only. No corpus article links enum/mode values (audited
    # 2026-10-25); auto-linking them produced 20+ noise links on DIO.
    section_range = {}  # name -> (start_line, end_line) of its own defining section
    heading_at = {h[0]: h for h in headings}
    heading_by_slug = {h[4]: h for h in headings}
    ends = {h[0]: (headings[idx + 1][0] if idx + 1 < len(headings) else len(lines))
            for idx, h in enumerate(headings)}
    enc72 = None  # enclosing 7.2.x section (constant bullets)
    enc_err = None  # enclosing 错误-titled §6 section (error-classification tables)

    # types, functions, callbacks, callouts, scheduled functions and port
    # interfaces from identifier-titled headings ANYWHERE in ch.7 (the API
    # chapter — its layout varies: MCAL/I-O articles 7.2–7.5 classic, the
    # EcuM house shape adds 7.6 调度函数 (EcuM_MainFunction) and 7.7/7.8
    # interfaces, BswM puts port interfaces at 7.7.2.x. The IDENT.fullmatch
    # guard — NOT a section range — is the filter: Chinese-titled groups
    # (通用, 期望接口) and suffixed titles (EcuM_ShutdownTarget端口接口)
    # never become targets). Any heading level (grouped layout:
    # #### group -> ###### entry, EcuM-style; flat layout: #### entry,
    # PWM-style — the IDENT filter accepts both)
    for (i, lvl, num, title, slug) in headings:
        if lvl == 4:
            section_range[title] = (i, ends[i])
        if re.match(r"7\.", num) and IDENT.fullmatch(title):
            defs[title] = slug
            section_range[title] = (i, ends[i])

    for i, ln in enumerate(lines):
        if i in heading_at:
            h = heading_at[i]
            if h[1] == 4 and h[2].startswith("7.2."):
                enc72 = h[4]
            elif h[1] <= 3:
                enc72 = None
            if h[1] <= 4:
                if h[2].startswith("6.") and "错误" in h[3]:
                    enc_err = h[4]
                else:
                    enc_err = None
            continue
        m = re.match(r"^\s*\*\s+\*\*([A-Za-z][A-Za-z0-9_]+)\*\*", ln)
        if m and enc72:
            name = m.group(1)
            j = heading_by_slug[enc72][0]
            if re.fullmatch(r"[A-Z][A-Z0-9_]+", name):
                consts.setdefault(name, enc72)  # uppercase = enum/mode value
            # lowercase bullets are parameter names, not constants — ignored
        if enc_err and ln.lstrip().startswith("|"):
            for tok in re.findall(r"\b[A-Z][A-Z0-9]*_E_[A-Z0-9_]+\b", ln):
                if tok not in defs:
                    defs[tok] = enc_err
                    hl = heading_by_slug[enc_err][0]
                    section_range.setdefault(tok, (hl, ends[hl]))
    return lines, headings, defs, section_range, consts


# --- semantic pattern catalog (2026-10-24, corpus survey) -------------------
# [n] in prose == "Related documentation, entry n" — a two-hop reference:
#   citation -> §3.1 entry n -> external document OR a site article/page.
# Classification is by the entry's AUTOSAR_CP_* document id (NEVER by title
# substring: "Requirements on Port Driver" (SRS_PortDriver) is NOT the site's
# Port article). SITE targets exist on this site; EXTERNAL needs a curated
# official URL before it can become a link (check 8 then applies).
DOC_TARGETS = {
    "swsbswmodemanager": ("SITE", "BswM article", "../basic_software_mode_manager/"),
    "swsdiagnosticcommunicationmanager": ("SITE", "Dcm article", "../../diagnostics/diagnostic_communication_manager/"),
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
    "tpssoftwarecomponenttemplate": ("EXTERNAL", "TPS_SWCT", None),
    "tpmbswmoduledescriptiontemplate": ("EXTERNAL", "TPS_BSWModuleDescriptionTemplate", None),
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
    "trbswmodulelist": ("EXTERNAL", "TR_BSWModuleList", None),
    "trgbswmodulelist": ("EXTERNAL", "TR_BSWModuleList", None),
}

# Cross-article module mentions (report-only class). Status reflects the site
# as of 2026-10-25 — re-verify before applying any of these as links. Names are
# matched case-insensitively with word boundaries (articles render "Port
# Driver" as **PORT**/**Port**驱动程序, "Det" as **DET**); standalone bold-term
# lines (the §2 acronym entries) are skipped — a term line defines, not mentions.
MODULE_LINKS = {
    "Port Driver": ("SITE", "../port_driver/"),
    "PORT": ("SITE", "../port_driver/"),
    "EcuM": ("SITE", "../ecu_state_manager/"),
    "BswM": ("SITE", "../basic_software_mode_manager/"),
    "Det": ("NO-ARTICLE", None),
    "DEM": ("SITE", "../../diagnostics/diagnostic_event_manager/"),
    "CanIf": ("NO-ARTICLE", None),
    "Mcu": ("NO-ARTICLE", None),
    "NvM": ("SITE", "../../memory/nvram_manager/"),
    "Dcm": ("SITE", "../../diagnostics/diagnostic_communication_manager/"),
    "SoAd": ("SITE", "../../communication/SoAd/SoAd/"),
    "ComM": ("NO-ARTICLE", None),
    "CanSM": ("NO-ARTICLE", None),
    "LinSM": ("NO-ARTICLE", None),
    "FrSM": ("NO-ARTICLE", None),
    "EthSM": ("NO-ARTICLE", None),
    "Sd": ("NO-ARTICLE", None),
    "Nm": ("NO-ARTICLE", None),
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


def _registry_sec(article: str):
    # §3.1 registry (SWS articles) or an unnumbered 参考文献 section (EXP
    # guides) — both carry the [n] Title / > DOCID registry format. A §3.1
    # only qualifies if it actually holds [n] entries (guide chapters number
    # their sections 3.1 too, e.g. EXP_ModeManagementGuide's process steps).
    # Entry lines may carry the invisible #ref-n anchor prefix --apply adds.
    sec = re.search(r"### 3\.1\..*?(?=### 3\.2)", article, re.S)
    if not (sec and re.search(rf"^{REF_ANCHOR}\[\d+\]\s", sec.group(0), re.M)):
        sec = re.search(r"## 参考文献\n.*?(?=\n## )", article, re.S)
    return sec


def parse_entries31(article: str):
    sec = _registry_sec(article)
    entries = {}
    if sec:
        blocks = re.split(rf"(?=^{REF_ANCHOR}\[\d+\])", sec.group(0), flags=re.M)
        for b in blocks:
            m = re.match(rf"^{REF_ANCHOR}\[(\d+)\]\s+(.+)$", b, re.M)
            if not m:
                continue
            n, title = m.group(1), m.group(2).strip()
            d = re.search(r"(AUTOSAR_[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+)", b)
            entries[n] = (title, d.group(1) if d else "")
    return entries


def entries31_span(article: str):
    sec = _registry_sec(article)
    if not sec:
        return None
    start = len(article[:article.index(sec.group(0))].splitlines())
    end = start + len(sec.group(0).splitlines())
    return start, end


def front_matter_end(lines):
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


def config_start(lines, headings):
    """Line of the first 配置规范 chapter heading (scan-stop), or None."""
    for (i, lvl, num, title, slug) in headings:
        if lvl == 2 and title.strip().endswith(CONFIG_TITLE):
            return i
    return None


def add_registry_anchors(lines, entries31):
    """Prefix every §3.1 registry entry line with its invisible #ref-n anchor
    (idempotent — a line already carrying id="ref-n" is left alone)."""
    if not entries31:
        return 0
    span = entries31_span("\n".join(lines))
    if not span:
        return 0
    added = 0
    for i in range(span[0], span[1]):
        m = re.match(rf"^{REF_ANCHOR}\[(\d+)\]\s", lines[i])
        if m and f'id="ref-{m.group(1)}"' not in lines[i]:
            lines[i] = f'<a id="ref-{m.group(1)}"></a>' + lines[i]
            added += 1
    return added


def convert_citation_links(lines, entries31, ref_skip=frozenset()):
    """[n] -> [\\[n\\]](#ref-n) (brackets kept visible) for every number the
    registry defines. Whole
    article (unlike identifiers, a citation is a citation everywhere), but
    never in headings (a link would change the Material slug), code fences,
    inline code, the registry itself, or **译者注：** lines; --ref-skip
    exempts user-approved document-name mismatches."""
    if not entries31:
        return 0
    span = entries31_span("\n".join(lines))
    fm_end = front_matter_end(lines)
    fence = False
    changed = 0

    def sub(m):
        nonlocal changed
        n = m.group(1)
        if n in ref_skip or n not in entries31:
            return m.group(0)
        changed += 1
        # escaped brackets in the link text keep the source's visible [n]
        return f"[\\[{n}\\]](#ref-{n})"

    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if (fence or ln.startswith("#") or i < fm_end
                or (span and span[0] <= i < span[1])
                or ln.lstrip().startswith("**译者注：**")):
            continue
        segs = re.split(r"(`[^`]*`)", ln)  # odd indices = inline code
        lines[i] = "".join(
            seg if si % 2 else re.sub(r"\[(\d+)\](?!\()", sub, seg)
            for si, seg in enumerate(segs))
    return changed


def census(article: str, self_dir: str = ""):
    entries31 = parse_entries31(article)
    lines, headings, defs, _, consts = collect(article)
    fm_end = front_matter_end(lines)
    sec31_span = entries31_span(article)
    fence = False
    chapter = 0
    id_by_chapter = {}
    id_by_name = {}
    can_lines = 0
    n_lines = 0
    n_linked = 0
    tn_lines = 0
    unresolved = []
    unlinked_resolved = []
    resolutions = {}
    modules = {}
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        m = re.match(r"^## (\d+)\.", ln)
        if m:
            chapter = int(m.group(1))
            continue
        if fence or ln.startswith(("#", "---")) or i < fm_end:
            continue
        hits = [n for n in defs if re.search(rf"(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])", ln)]
        if hits:
            id_by_chapter[chapter] = id_by_chapter.get(chapter, 0) + 1
            for n in hits:
                id_by_name[n] = id_by_name.get(n, 0) + 1
        if re.search(r"参见|参考|详见", ln):
            can_lines += 1
        in31 = sec31_span and sec31_span[0] <= i < sec31_span[1]
        if not in31:
            # linked markers are those --apply already converted (idempotency
            # view); the whole article counts (no 配置规范 stop — a citation
            # is a citation everywhere)
            # tolerate both link forms: legacy bare [7](#ref-7) and the
            # bracket-preserving [\[7\]](#ref-7) (2026-10-27 migration) — the
            # trailing \]? is the markdown link's own outer closing bracket,
            # present only in the new form
            n_linked += len(re.findall(r"\\?\[(\d+)\\?\]\]?\(#ref-\d+\)", ln))
            if ln.lstrip().startswith("**译者注：**"):
                tn_lines += 1
            else:
                # no (?<!]) lookbehind: adjacent citation pairs ([19][4], the
                # RTE article) must BOTH convert; reference-style links
                # [text][1] do not exist in the corpus (audited 2026-10-26)
                for m2 in re.finditer(r"\[(\d+)(?:,\s*[^\]]+)?\](?!\()", ln):
                    n_lines += 1
                    n = m2.group(1)
                    ctx = ln[max(0, m2.start() - 24):m2.end()].strip()
                    ent = entries31.get(n)
                    if ent:
                        title, docid = ent
                        cls, label, target = classify_doc(title, docid)
                        resolutions.setdefault((n, title[:40], cls, label or "?"), 0)
                        resolutions[(n, title[:40], cls, label or "?")] += 1
                        unlinked_resolved.append((i + 1, n, ctx))
                    else:
                        unresolved.append((i + 1, n, ctx))
        if re.match(r"^\*\*[^*]+\*\*\s*$", ln):
            continue  # §2 acronym term line — a definition, not a mention
        for mod, (status, target) in MODULE_LINKS.items():
            # an article never links to itself: drop the module whose target
            # directory IS the article's own directory (EcuM x87 in the EcuM
            # article was census noise, fixed 2026-10-25)
            if (self_dir and target
                    and os.path.normpath(os.path.join(self_dir, target)) == os.path.normpath(self_dir)):
                continue
            if re.search(rf"(?<![A-Za-z0-9_]){re.escape(mod)}(?![A-Za-z0-9_])", ln, re.IGNORECASE):
                modules.setdefault((mod, status, target), 0)
                modules[(mod, status, target)] += 1

    total = sum(id_by_chapter.values())
    print("== identifier mentions (applied class) ==")
    print(f"  total lines: {total}")
    print("  by chapter: " + ", ".join(f"§{c}: {v}" for c, v in sorted(id_by_chapter.items()) if v))
    print("  per name: " + ", ".join(f"{n} x{c}" for n, c in sorted(id_by_name.items(), key=lambda x: -x[1])))
    const_hits = sum(1 for i, ln in enumerate(lines)
                     if not ln.startswith(("#", "```"))
                     and any(re.search(rf"(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])", ln) for n in consts))
    print(f"== §7.2 constant-bullet mentions (report-only): {const_hits}"
          + ("; per name: " + ", ".join(f"{n} x{sum(1 for ln in lines if re.search(rf'(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])', ln))}" for n in sorted(consts)) if consts else ""))
    print(f"== 参见/参考/详见 lines (report-only): {can_lines}")
    print("== prose [n] citations (registry/fences/译者注 excluded, whole article) ==")
    print(f"  linked to #ref-n: {n_linked}; unlinked: {n_lines}"
          f" ({len(unresolved)} unresolved); 译者注 lines skipped: {tn_lines}")
    if unresolved:
        print("  UNRESOLVED numbers — not in the §3.1 registry: source-typo")
        print("  candidates, NEVER link; a 译者注 is a user decision:")
        for ln_no, n, ctx in unresolved:
            print(f"    L{ln_no} [{n}] …{ctx}")
    if unlinked_resolved:
        print("  UNLINKED resolved — --apply converts these; verify the context")
        print("  names the entry's own document (mismatch => --ref-skip):")
        for ln_no, n, ctx in unlinked_resolved:
            print(f"    L{ln_no} [{n}] …{ctx}")
    if resolutions:
        print("  [n] resolutions (entry -> document -> class):")
        for (n, title, cls, label), cnt in sorted(resolutions.items(), key=lambda x: int(x[0][0])):
            print(f"    [{n}] {title} -> {cls}:{label} x{cnt}")
    print("== cross-article module mentions (report-only) ==")
    if modules:
        for (mod, status, target), cnt in sorted(modules.items(), key=lambda x: -x[1]):
            print(f"    {mod} -> {status}{':' + target if target else ' (no article yet)'} x{cnt}")
    else:
        print("    0 candidates")


def apply_links(article: str, ref_skip=frozenset()):
    lines, headings, defs, section_range, _ = collect(article)
    entries31 = parse_entries31(article)
    fm_end = front_matter_end(lines)
    stop = config_start(lines, headings)
    names = sorted(defs, key=len, reverse=True)
    changed = 0
    fence = False
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith("#") or i < fm_end or (stop is not None and i >= stop):
            continue
        orig = ln
        # split into existing-link and free segments; substitute only in free
        # segments so re-running never double-wraps a link (idempotency)
        segs = []
        pos = 0
        for m in MD_LINK.finditer(ln):
            if m.start() > pos:
                segs.append((ln[pos:m.start()], False))
            segs.append((m.group(0), True))
            pos = m.end()
        if pos < len(ln):
            segs.append((ln[pos:], False))
        out = []
        for seg, is_link in segs:
            if is_link or not seg:
                out.append(seg)
                continue
            for n in names:
                if n not in seg:
                    continue
                sr = section_range.get(n)
                if sr and sr[0] <= i < sr[1]:
                    continue  # own defining section
                pat = re.compile(rf"\*\*{re.escape(n)}\*\*|(?<![A-Za-z0-9_]){re.escape(n)}(?![A-Za-z0-9_])")
                seg = pat.sub(lambda t: f"[{t.group(0)}](#{defs[n]})", seg)
            out.append(seg)
        ln = "".join(out)
        if ln != orig:
            lines[i] = ln
            changed += 1
    anchors_added = add_registry_anchors(lines, entries31)
    cites = convert_citation_links(lines, entries31, ref_skip)
    out_text = "\n".join(lines) + "\n"
    # verify anchors — heading slugs AND raw HTML ids (the #ref-n targets)
    anchors = set(h[4] for h in headings)
    anchors |= set(re.findall(r'id="([^"]+)"', out_text))
    bad = [a for a in re.findall(r"\]\(#([^)]+)\)", out_text) if a not in anchors]
    if bad:
        print(f"UNRESOLVED ANCHORS: {sorted(set(bad))}")
        sys.exit(1)
    print(f"lines changed: {changed}; citation links added: {cites}; "
          f"registry anchors added: {anchors_added}; all link anchors resolve"
          + (f"; ref-skip: {','.join(sorted(ref_skip))}" if ref_skip else "")
          + (f"; stopped before line {stop + 1} (配置规范)" if stop is not None else ""))
    return out_text


if __name__ == "__main__":
    args = sys.argv[1:]
    mode = path = None
    ref_skip = set()
    i = 0
    while i < len(args):
        if args[i] == "--ref-skip":
            i += 1
            ref_skip |= {s.strip() for s in args[i].split(",") if s.strip()}
        elif args[i] in ("--list", "--apply"):
            mode = args[i]
        else:
            path = args[i]
        i += 1
    if not mode or not path:
        print(__doc__)
        sys.exit(2)
    article = open(path).read()
    if mode == "--list":
        census(article, self_dir=os.path.dirname(os.path.abspath(path)))
    elif mode == "--apply":
        out = apply_links(article, ref_skip=ref_skip)
        open(path, "w").write(out)
    else:
        print(__doc__)
        sys.exit(2)
