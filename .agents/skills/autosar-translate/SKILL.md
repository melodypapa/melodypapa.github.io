---
name: autosar-translate
description: >
  Use when working on the AUTOSAR articles of the melodypapa.github.io MkDocs
  site: translating, completing, updating, verifying, or inventorying any
  article under docs/autosar/; syncing a specification document (AUTOSAR
  SWS/EXP/SRS/TPS, releases R22-11/R23-11/R25-11, docs/autosar_pdf PDFs, or
  the ~/Workspace/autosar_standard markdown tree) into a Type A article;
  checking which specs still lack articles; or answering coverage and
  progress questions about docs/autosar/ (TODO.md, STANDARD.md). Also use
  for any AUTOSAR module name (CanSM, SoAd, Dem, NvM, EthSwt, Com, Det…)
  appearing in the context of this site.
---

# AUTOSAR Spec → Site Article Sync

Translate or complete the Chinese articles under `docs/autosar/` of this
MkDocs site from authoritative AUTOSAR standard documents. The workflow below
distills six completed syncs (BswM, EcuM, Mode-Management guide, ICU, DIO,
Port, PWM, OCU); follow it in order.

## Step 0 — Read the law of the land

Read `docs/autosar/STANDARD.md` in the target repo before anything else. It
defines the mandatory Type A chapter skeleton, canonical chapter wording,
formatting rules, translation principles, landing-page format, and the
exemption list (guide/EXP articles). This skill does not restate those rules —
it tells you how to execute a sync under them. If `STANDARD.md` is missing,
stop and ask the user how to proceed rather than guessing conventions.

## Step 1 — Resolve the source document

Read `references/source-resolution.md` for the full recipe. Summary:

1. **Primary source**: markdown conversion of the standard,
   `~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11/<Category>/AUTOSAR_CP_<Type>_<Name>.md`
   (confirm the path on this machine first; it is outside the repo).
   Use the **SWS** document for module articles, **EXP** for guides. The SRS
   is only for requirement-coverage checks — never as the structural source.
2. **Fallback by release**: no R22-11 markdown exists. If the requested
   release is missing, use the nearest available release and **state which
   release you used** in the issue and PR text.
3. **Last resort**: bundled PDFs in `docs/autosar_pdf/AUTOSAR_CP/<Release>/`
   (pypdf extraction recipe and fidelity warnings in the reference).

## Step 2 — Map spec → target article

Read `references/mapping.md`. It holds the curated table of known
spec ↔ article mappings, the naming convention for new articles, and the
category → site-section correspondence. For a new article, propose the
directory name to the user when the module name is acronym-ambiguous
(e.g. SoAd).

## Step 3 — Gap analysis before any writing

Compare the article's `## ` headings against the source chapter list:

- **Missing article** → plan a full Type A translation.
- **Partial / stub** → plan in-place completion (insert translations at the
  positions where the source has them).
- **Complete** → report alignment status; do not rewrite content that already
  exists. The droppable set is exactly two things (user decision 2026-10-25,
  EcuM completion): the requirement-tracing chapter and appendix A (*Not
  applicable requirements*). Their absence is compliance, not a gap; the
  absence of ANY other source section is a gap — including *Known
  Limitations* (translates as unnumbered `## 已知限制` before §1), appendix B
  (translates as `## B. …`, Step 5 rule), expected/port-interface chapters
  (EcuM's source 8.7/8.8 were missing from a ✅-rated article — found by the
  2026-10-25 diff), and content diagrams inside translated chapters. The
  配置规范 chapter translates as `## 8. 配置规范` (or `## 9.` when a 时序图
  chapter is also present) and the 时序图 chapter as `## 8. 时序图` when the
  source has them (Step 5 rules).

For sources longer than ~2000 lines, present the sync plan and get user
confirmation before translating — a full SWS can be an entire session of work.

Gap analysis and syncing are **text-only**: compare Markdown headings and
content, never open figure files (`Figure*.png` etc.) — figures are omitted by
site convention and reading them can break the API pipeline.

## Step 4 — Generate the work todo list

Before writing anything, turn the gap analysis into a **concrete checkbox todo
list**. Three sources feed it:

- **The rule**: expand `docs/autosar/STANDARD.md` into a per-article checklist
  — 7-chapter skeleton, canonical chapter wording, no forbidden chapters, no
  requirement IDs, front-matter title only, footer pattern, nav registration.
- **The progress**: the article's current row in `docs/autosar/TODO.md` plus
  the gap-analysis results.
- **The decisions**: anything the user decides mid-run (a wording choice, a
  scope cut, a source-release fallback) is appended to the file the moment it
  is given.

**Output contract:** the program's todo is the **persistent batch queue** in
`docs/autosar/sync-todo/` — `Group-<section>.md` files, one row per document,
each row carrying a 6-step sub-checklist; `index.md` orders the batches
(`todo.md` alongside the outputs for a workspace/eval run). A run consumes
**one row**: take the first `[ ]` row of the named (or next unfinished) batch,
append run findings to its `- Note:` bullets, tick each step the moment it
passes, flip the row `[x]` with the commit hash (Step 8). If the user names an
article with no queue row, add the row to the right batch file first. Format,
row template and rules: read `references/todo-format.md`. In short:

- The parenthetical is the short fixed fields only; findings, evidence and
  decisions go on `- Note:` bullets under the row — a long markup-heavy
  checkbox line breaks the exact-line toggle, and a failed toggle then gets
  "recorded" out-of-band instead of in the row.
- Tick a step **in the file the moment it passes verification** — never
  batch-check at the end, never tick because a later step re-verifies it.
- A queue row exists for the article ⇒ **resume**: take the first `[ ]` row;
  do not re-derive scope from TODO.md or re-ask decisions already in Notes.
- The row `[x]` + its 6 step boxes `[x]` + the `docs/autosar/TODO.md` row
  updated (Step 8) = the run is finished. Never declare it finished with any
  `[ ]` left in the row.

Observed failures when this contract is skipped: the iteration-1 baseline run
translated end-to-end and only surfaced its plan afterwards, as prose —
coverage decisions were never reviewable before the work was done; the DIO run
(2026-10-24) posted its todo to chat and never saved a file. The full-program
queue (`docs/autosar/sync-todo/`, generated 2026-10-24 from the R23-11
inventory) is the "translate one by one" backbone; `TODO.md`'s Backlog keeps
program-level fixes outside single-article runs (wording sweeps, hygiene).

## Step 5 — Translate in place

- Existing translated content is never rewritten; fill gaps only, inserting
  at the position where the source has them.
- Faithful translation of the standard's own wording — not a summary in your
  own words. Verify doubtful passages against the SWS, not the SRS (they
  genuinely differ; the ADC driver "works on channel groups" is SWS-faithful).
- Pseudo-code listings stay verbatim in code fences (reconstruct the
  PDF-extraction garbling into readable formatting); prose is translated;
  figures are omitted.
- **Acronym chapter (ch.2) format**: the source's acronym table is reflowed
  into 「粗体术语行 + `>` 引用块释义」 (bold term line + `>` blockquote
  definition) — **never keep a GFM table**, even when the source is a table
  and every definition is one line (the site was once split 20 blockquote
  articles vs 6 tables; tables are unreadable with long definitions).
  Sub-rules:
  - Term line = the source Abbreviation/Acronym cell **bolded verbatim**,
    including bracketed aliases (the
    `**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）`
    pattern);
  - A pure acronym's definition reads `中文全称（**English Full Name**）` —
    the Chinese full name with the English full name bolded; term entries
    translate the description sentence, English terms bolded; `[n]`
    reference markers are dropped; an in-row source Note becomes a
    `**注意：**` paragraph inside the definition;
  - **Row set and row order strictly match the source table**: not one entry
    more or fewer, no splitting (if the source covers two modes in one
    *Conversion Mode* row, it stays one entry), no reordering, no dropping
    rows that "look too generic" (adc_driver once lost API/HW/SW, swapped
    DET/DEM, split one row in two — undetected under a ✅ status);
  - If the source has a prose intro sentence, translate and keep it;
    "the following table" wording becomes "以下" with the new format; if the
    source has only a table caption (Table 2.1), invent no intro sentence;
  - **Structure mirrors the source ch.2**: when the source has a *Definitions*
    section (EcuM 2.1), the chapter translates as `## 2. 定义和缩略语` with
    `### 2.1. 定义` (source 2.1 rows) + `### 2.2. 缩略语` (source 2.2 rows) —
    the same bold-term + blockquote format inside both; the row-set audit
    counts each subsection against its own source table.
- **API chapter (article §7 ↔ source ch.8) sync sub-rules** — types,
  functions and expected interfaces are all checked against the source item
  by item; counting chapters is not enough:
  - **Coverage 1:1**: every source `## 8.2.x` type ↔ `#### 7.2.x`, every
    source `## 8.3.x` function ↔ `#### 7.3.x`, names and order identical
    (the Phase A check 7 script gates count/name/order; PWM run baseline:
    8 types and 13 functions all aligned);
  - **Function entries**: the C signature is copied verbatim from the
    source's Syntax line into the code fence; the service-table fields are
    folded into `**说明**` per site convention (sync/async, re-entrancy,
    in/out parameters, return value, available via `<X>.h`);
    **every source requirement block under a function becomes one paragraph,
    in order** — look-alike duplicate sentences may be two distinct
    requirements (PWM's *pre compile time configurable* `10xx` vs
    *configurable … {MACRO}* `20xx` are two; never deduplicate or merge);
  - **Type tables checked cell by cell**: Kind / Derived from / Range
    (value + hex + description) / Description / Available via matched
    against the source cell by cell. Two pits already stepped in: ranges
    shifted by one row (PWM 7.2.1 carried the neighbor Pwm_PeriodType's
    "8..32 bit" on Pwm_ChannelType; the source Range was actually `- -`);
    and **rows that exist only in a newer release** (PWM 7.2.8's
    `PWM_FULL_POWER (0x00)` is absent from the R23-11 source table and only
    enters in R25-11) — such content mismatches always go to the queue row's
    Notes as user decisions, never silently kept or deleted;
  - 8.1 ↔ §7.1 (imported-type table row set identical) and
    8.4/8.5/8.6.1–8.6.3/8.7 ↔ §7.4–§7.7 (callbacks/scheduled/expected
    interfaces incl. configurable callbacks/API parameter checks) fall under
    the same rule.
- **时序图 chapter (source ch.9 → article `## 8. 时序图`, optional)** —
  present iff the source document has a *Sequence diagrams* chapter; source
  9.x renumbers to 8.x; the chapter sits between §7 and the 配置规范
  chapter (renumbering 配置规范 to `## 9.` when both are present — grep for
  inbound anchor links first). Rules:
  - translate the source's prose sentences faithfully; the PDF→markdown
    conversion spills UML diagram chrome into the text (lifeline/message
    labels like `Ocu_Notification_<Channel>()`, `«module»` box labels,
    `Ocu\_Delnit()` typos) — drop that chrome, keep the prose;
  - render each diagram per the site figure convention: the extracted local
    PNG (`![Figure9-1.png](Figure9-1.png)`) when the article directory has
    one — matching the rest of the article — or a mermaid `sequenceDiagram`
    redraw per icu_driver's chapter when no PNG exists (icu's intro
    blockquote naming the source chapter and release is the precedent);
  - source figure captions ("Figure 9.1: …") are not repeated as text — the
    site references figures without captions;
  - a subsection whose only content is a cross-reference (e.g. ocu 9.6 →
    source 8.3.8/8.3.9) translates the reference renumbered to the article's
    own chapters (→ §7.3.8/§7.3.9); a potential intra-article link is a
    Phase B candidate, not a silent addition;
  - **Figures are complete, not a selection**: every content diagram of the
    chapter embeds. Deduplicate by content hash — the converter repeats the
    same PNG under many image numbers, and 3 known decoration images
    (cover/section chrome) recur throughout a document (EcuM's "40 image
    refs" were really 21 diagrams + deco); copy each content artifact into
    the article directory (`Figure<N>-<k>.png` by source chapter) and
    reference it wherever the source has it.
- **Source tables translate as markdown tables, never as images** (user
  decision 2026-10-25, EcuM StartPreOS table request): the old
  tables-as-images convention (`Table7-1.png`) is retired — every content
  table of the source (sequence tables, init-block listings, error tables,
  state tables) renders as a GFM table in the article. Format:
  - caption line above the table, source numbering kept: 表7.1：StartPreOS
    序列（**StartPreOS Sequence**） — bilingual when the source name is a
    proper-noun table name; footnote markers (<sup>N</sup>) carry over and
    the footnote text follows the table as `> N …` blockquotes;
  - header row = the source's second header line (the spanning first header
    like "StartPreOS Sequence | StartPreOS Sequence | StartPreOS Sequence"
    is PDF chrome, dropped): e.g. 初始化活动 | 说明 | 可选;
  - **row set, row order and cell values strictly match the source** (same
    standard as the acronym rule); empty cells stay empty;
  - cross-references inside cells link to the article's own anchors
    (renumbered: source 7.3.5 → §6.3.5) and callout/function names link to
    their API headings; SWS-ID-only refs (See [SWS_EcuM_02181]) stay prose
    with the section named;
  - Phase A check: no `![Table*.png]` image refs remain in the article; the
    old `Table*.png` files become unreferenced (delete or leave — their
    removal is not part of the translation step).
- **Appendix B (*Change history of AUTOSAR traceable items*) translates as
  `## B. AUTOSAR 可追溯项变更历史`** after the last content chapter: one `###`
  per release, `####` added/changed/deleted sub-sections, the item-ID lists
  kept **verbatim in code fences** — the IDs are data, the one sanctioned
  exception to the no-requirement-IDs rule (un-escape `SWS\_EcuM\_…`
  artifacts); "none" → 无.
- **配置规范 chapter (source ch.10 → article `## 8. 配置规范`, or `## 9. 配置规范` when a 时序图 chapter precedes it, optional)** —
  present iff the source document has a configuration specification; source
  10.x renumbers to 8.x (no 时序图 chapter) or 9.x (with 时序图). Terminology (site majority, baseline-tested
  2026-10-24): *Configuration specification* → 配置规范; *Containers and
  configuration parameters* → 容器与配置参数; *container* → 容器
  (*configuration container* → 配置容器); *Container Name* → 容器名称;
  *Parent Container* → 父容器; *Included Containers* → 包含的容器;
  *Multiplicity* → 多重性; *configuration parameter* → 配置参数;
  *Parameter Name* → 参数名称; *Scope / Dependency* → 作用域/依赖;
  *published information* → 发布信息. Structure rules:
  - translate the source tables faithfully as GFM tables; normalize the
    PDF merged-cell artifacts (a value repeated across collapsed columns —
    IDs, headers — collapses to one column);
  - bracketed `[SWS_*]` and `[ECUC_*]` IDs are dropped per the hygiene rule;
    parameter/container NAMES (`AdcDeInitApi`, `AdcGeneral`) are code
    identifiers — never translated, kept verbatim in cells and headings;
  - boolean descriptions keep true/false and render per the site pattern
    `* **true**：…` / `* **false**：…` when the source lists them separately;
  - the chapter's internal cross-references are renumbered to the article's
    own chapters (source ch.7 → §6, ch.8 → §7);
  - flash_driver/time_service carry legacy flattened per-parameter headings
    from the pre-Type A era — do not copy that layout into new translations;
    their chapters get aligned when their rows run.
- **Potential links are applied during translation, not merely detected** — the
  intra-article class is restoration of the source PDF's own hyperlinks:
  identifier mentions (types/functions link to their defining ch.7 heading —
  an identifier-titled heading at ANY level ANYWHERE in ch.7, the API
  chapter: dio/adc `#### 7.2.x. Adc_ConfigType` flat, EcuM
  `###### 7.3.1.1 EcuM_GetVersionInfo` grouped, EcuM's scheduled function
  `#### 7.6.1. EcuM_MainFunction`, BswM's `###### 7.7.2.1
  BswM_modeNotificationPort` port interfaces. The identifier-title guard —
  NOT a section range — is the filter: Chinese group titles like 通用 and
  suffixed titles like `EcuM_ShutdownTarget端口接口` are never link targets),
  development-error codes (link to their
  错误-titled §6 section's anchor — DIO/PWM 6.6.x 开发错误, EcuM 6.12/6.13,
  ADC 6.5), and prose citation markers `[n]` (link to the §3.1 entry's own
  anchor — next bullet, user decision 2026-10-26); §7.2 constant bullets
  (STD_HIGH, ICU_MODE_* enum/mode values) and
  参见/详见 references stay candidates for a user decision — no corpus article
  links constants (audited 2026-10-25). The census excludes the article's own
  module from cross-article mentions (a self-link is never a candidate). Use
  `.agents/skills/autosar-translate/scripts/link_candidates.py --apply
  <article>` (idempotent — re-running changes 0 lines; identifier/error-code
  links scan through 时序图 prose and stop before 配置规范 whose tables are
  definitional; citation-marker links scan the whole article).
- **Citation markers `[n]` mean "Related documentation, entry n"** — a
  two-hop reference: citation → §3.1 entry → an external document or a page
  on this site. **Hop 1 is an applied class (user decision 2026-10-26)**: the
  marker itself links to the §3.1 entry, restoring the source PDF's own
  citation hyperlink — `--apply` prefixes every registry entry line with an
  invisible anchor (`<a id="ref-n"></a>`) and converts prose `[n]` to
  `[n](#ref-n)`, but ONLY for numbers the registry defines. Three things
  never convert: a number the registry does not define (UNRESOLVED — source
  typo, e.g. EcuM's `[23]`; leave as prose, a 译者注 is a user decision), a
  number whose surrounding prose names a DIFFERENT document than the entry
  (SWS_EcuM cites "ECU Configuration [5]" while §3.1 [5] is Glossary —
  re-apply with `--ref-skip 5` and record the decision in the queue row),
  and `**译者注：**` lines (translator prose, never source citations). The
  census reports UNRESOLVED and UNLINKED numbers with their inline context so
  both cases are caught before apply is trusted. Hop 2 stays a report-only
  user decision: `link_candidates.py --list` resolves every citation to its
  document and classifies by the entry's `AUTOSAR_*` doc id — **never by
  title substring** ("Requirements on Port Driver" is SRS_PortDriver, not
  the site's Port article). SITE class = the document's article/page exists
  here, linkable now (e.g. EcuM citing the BswM spec → the site's BswM
  article; `[n] AUTOSAR 术语表` → the site glossary page); EXTERNAL class =
  needs a curated official URL before it can become a link (check 8 then
  applies). Both are user decisions recorded with the census.
- **Link text is the document title, never a directory/file identifier**
  (user preference 2026-10-24): gen_api_list reads the article's
  front-matter `title:` for 来源/article links (stem only as fallback);
  hand-written links follow the same rule — `[ADC 驱动](io/adc_driver/)`,
  not `[adc_driver](…)`.

  Everything cross-article or anchor-less stays a reported candidate (user
  decision, queue in TODO.md's Backlog) — never silently added, and never
  silently *not counted*: the census is a Phase A output (check 9).
- Chapter numbering stays stable; when insertion forces a renumber, grep for
  inbound anchor links first and fix them in the same commit.

## Step 6 — Regenerate the derived indexes (glossary + API list)

`api_reference.md` is a **pure derivation** (regenerate via
`gen_api_list.py` when its source data changed); `glossary.md` is
**manually extended during translation runs** (see below — user decision
2026-10-24).

1. **Glossary `glossary.md`** — **manually extended during translation
   runs** (user decisions 2026-10-24/25, superseding the script scan): when
   an article or TR batch is translated, the run adds that article's/batch's
   terms to the page by hand with 来源 attribution (document title as link
   text, spec + release). **Page format (2026-10-25): flat alphabetical** —
   `## <letter>` sections, all entries A–Z across documents (no
   per-document sections, no methodology prose on the page); each entry =
   `**Term**` + one definition line + one 「来源：」 line per contributing
   document. Terms are extracted from the SOURCE
   during translation — never machine-extracted from the translated article
   afterwards; `gen_glossary.py` is retired. **One term is translated once**
   (user rule 2026-10-24): the same term appearing in another document is NOT
   re-translated — keep the one definition and append that document on its
   own 「来源：」 line; a substantively different definition is a user
   decision, never a silent second line. The
   Foundation TR glossary's translation state is tracked in
   `scripts/tr_glossary.json` (source-extraction workfile, not a build
   input).
2. **API reference `api_reference.md`** — every type (8.2) and function (8.3)
   defined in chapter 8 of every R23-11 SWS document, A–Z, each entry naming
   its document and release and linking to the site article when one exists.
   Regenerate after any front-matter `spec:` change or article addition:
   `python .agents/skills/autosar-translate/scripts/gen_api_list.py`. Its
   `!` lines (ch.8 present but nothing parsed — 7 known docs, all untranslated,
   e.g. the interpolation libraries' "routines definitions" structure) are
   recorded limitations, not errors to silence.

Every mapped article carries front-matter `spec:` (source document) and
`release:` (AUTOSAR release actually translated from) — set at article
creation/alignment (seeded from `references/mapping.md`; icu_driver is
`R22-11` until its Group-io realignment). An article without `spec:` is
invisible to both indexes.

## Step 7 — Verify (two-phase gate), then repo workflow

The strict build is necessary, not sufficient: it is blind to wording,
coverage and fidelity. The gate therefore has two phases — the first is run
before every commit, the second is evidence for the Step 8 confirmation.

**Phase A — mechanical checks** (scriptable; stop on any failure):

1. `mkdocs build --strict` via the venv recipe in the repo `AGENTS.md`: exit 0,
   **zero WARNINGs** (pre-existing INFO anchor notices are fine).
2. Heading audit: `grep '^## '` on the article equals the STANDARD.md §1
   skeleton with §2 wording, numbered `1.`–`7.` only — plus an unnumbered
   `## 已知限制` before `## 1.` when the source has a Known Limitations
   chapter; `###`/`####` numbering
   is continuous (no numbering gaps); no appendix A (`## A.`), and no forbidden
   chapter title (需求可追溯性 / 需求追踪) anywhere; `## B.` is allowed only
   as the 可追溯项变更历史 appendix; `## 8.` is
   allowed only as `## 8. 时序图` and `## 9.` only as `## 9. 配置规范`
   (both optional — only when the source has ch.9 / ch.10; when only one
   optional chapter is present it takes the lower number); a **numbered
   continuation** `## 10.`+ is allowed when the source has a chapter 11+ or a
   content annex that is not the droppable NA-requirements appendix
   (STANDARD.md §1) — its heading is a direct translation of the source title.
   **Before renaming
   a heading to a STANDARD.md term, grep that heading across `docs/autosar`** —
   if the standard and the site majority disagree, it is a user decision
   (record it; update STANDARD.md in the same PR), not a silent rename.
   Then sweep §2's `不用` variants mechanically: for every variant STANDARD.md
   §2 forbids (`可配置的接口`, `周期函数`, `适用于汽车领域`, `输入文件`, …),
   `grep -nE '^#+.*VARIANT'` on the article must return 0 hits (canonical:
   `可配置接口`, `调度函数`, `汽车域的适用性`, `输入文件和相关标准与规范`). §2 governs chapter heading
   wording (章节标题用词), so
   scope the grep to heading lines — faithful prose is not in scope. A stale
   §2 line is exactly how a rejected wording re-enters a new article — the
   grep, not judgment, is what catches it.
3. Hygiene greps: no `^# ` in the body; no requirement IDs
   (`\[[A-Z][A-Za-z]*_[A-Za-z0-9]*_[0-9]+\]`) and no `{DRAFT}`; a WeChat
   footer, if present, is `<section id="wechat">` + `<h4>`, never a markdown
   heading.
4. Nav and anchors: new pages registered in `mkdocs.yml` (paths `docs/`
   -relative), removed pages cleaned in the same commit; renamed or renumbered
   headings — grep inbound `](…#…)` links site-wide and fix them in the same
   commit.
5. Acronym chapter: inside the `sed -n '/^## 2\. 缩略语/,/^## 3\./p' <article>`
   slice the `^| ` line count must be 0 (tables forbidden); the
   `^\*\*[^*]+\*\*\s*$` term-line count == the source table's data-row count
   (check row set and order line by line — this chapter drifts most easily in
   long sessions: adc_driver once turned 18 source rows into 16 entries and
   passed every check; term lines may carry trailing whitespace —
   bswm/ethernet_interface and several other articles have it).
6. Derived indexes: `gen_api_list.py --check` exits 0. Glossary: the run's
   own terms are present in `glossary.md` (grep spot-check) — the page is
   manually extended in the same commit that translates them.
7. API-chapter sync: `python
   .agents/skills/autosar-translate/scripts/check_api_sync.py <source.md>
   <article>` exits 0 — source 8.2.x/8.3.x heading names, counts and order
   match the article's 7.2.x/7.3.x, and the `**说明**` block count in §7.3
   equals the function count. The script is a tripwire for missing, renamed,
   reordered or untranslatable entries (baseline 2026-10-24: all six IO
   articles pass); prose fidelity inside an entry stays Phase B work.
8. Link audit: every link in the article must resolve — nothing else in the
   gate catches link rot.
   - Internal `](…*.md*)` targets exist, and the strict build output shows no
     "no such anchor" notice for this article — missing same-page anchors are
     INFO-level and do **not** fail `--strict`, so grep the build output
     explicitly (a literal `#xxx` placeholder survived as INFO in
     `eb_tresos/safety_os`).
   - External `](http…)` URLs **and plain-text URLs from the source**
     (blockquote/reference lines are links too):
     `curl -sIL -o /dev/null -w '%{http_code}' --max-time 15` each — 2xx/3xx
     pass; 4xx/5xx/timeout fails. Retry once with a browser UA before
     declaring failure (the 2026-10-24 first audit misread a live port.de URL
     as dead from one timed-out probe). Anti-bot hosts (iso.org, weixin)
     403/302 curl: verify manually in a browser and record the outcome —
     never delete a link for being curl-blocked, never wave a 404/500 through
     as "probably fine". Prefer the smallest **verified** fix — same path on
     https (OMG DDS/1.4: http 500 → https 200), or the publisher's current
     URL for the same document, checked in a browser; record it in TODO.md's
     Backlog, never guess a replacement (the 2026-10-24 audit nearly wrote an
     ieeexplore MACsec link into an 802.1AS article — different document).

9. Potential-links census (mechanical): run
   `scripts/link_candidates.py --list <article>` and RECORD the counts in the
   gate evidence: identifier mentions by chapter (applied class:
   identifier-titled ch.7 headings — types, functions, callbacks, callouts,
   scheduled functions, port interfaces; scanned through 时序图 prose,
   counted but never applied inside 配置规范 tables), dev-error codes §6.6.x
   (applied class, 错误-titled §6 sections), §7.2 constant-bullet
   mentions (report-only), 参见/详见 refs, prose `[n]` citations (whole
   article; registry lines, 译者注 lines and code excluded) split into
   already-linked / UNLINKED-resolved with inline context (verify each
   context names the entry's own document before trusting apply — a
   document-name mismatch re-runs apply with `--ref-skip n`) / UNRESOLVED
   (number not in the §3.1 registry — source typo, never link, record it and
   consider a 译者注), with their SITE/EXTERNAL two-hop resolutions, and
   cross-article
   module mentions (case-insensitive — articles render "Port Driver" as
   **PORT**/**Port**; §2 acronym term lines skipped). An explicit "0
   candidates" is a valid result; **silence is a failed gate**. This rule
   failed to activate for six runs when it lived only in Phase B prose — the
   counter exists so that cannot recur. `--apply` writes only the applied
   class; verify idempotency with a second run (0 lines changed) before
   committing.

**Phase B — automation-blind checks** (presented at the Step 8 gate as
evidence, not asserted):

- Coverage map: every translatable source `##` section ↔ an article section;
  the forbidden source chapters listed as deliberate omissions. **Internal
  structure of pre-existing chapters is part of the map** (adc lesson
  2026-10-25): a realignment must verify that already-translated chapters
  follow the source release's own sub-section convention (e.g. R23-11's
  *Background & Rationale* / *Requirements* split inside functional-spec
  subsections) — chapter-level heading equality hides a legacy topical
  layout underneath. **Diagrams embedded in non-forbidden chapters are
  chapter content and translate with it**: state diagrams inside the
  functional-spec chapter (e.g. ADC 7.3) belong to §6 — only the traceability
  and appendix chapters are exempt.
- Terminology: ch.2 row set and order checked **cell by cell** against the
  source tables — the Phase A term-line count alone can pass with reordered
  or renamed rows (that is how adc_driver's 18→16 drift hid under a ✅).
- Types and functions: type tables compared value + hex + description per
  Range row; every function's requirement texts mapped one-to-one (look-alike
  but distinct requirements kept separate — PWM `10xx`/`20xx`); content
  mismatches against the source release (neighbor-copied ranges, rows that
  only exist in a newer release) are **user decisions** recorded in the queue
  row, never silent fixes.
- Fidelity: doubtful passages verified against the **SWS** (not SRS);
  pseudo-code verbatim in fences; figures omitted or local PNGs only.
- Scope discipline: existing translated content untouched, gaps filled in
  place, chapter numbering stable.
- Decisions applied: every mid-run user decision in the queue row's Notes is
  reflected in the article (and in STANDARD.md when a canonical term changed).
- Potential links: the PDF→markdown conversion lost the source's internal
  hyperlinks, so translations cite things that could be links but aren't.
  Classes (all observed in real articles):
  - Intra-article: constant/type mentions → their ch.7.2 definition
    (Icu_SetMode's 说明 cites **ICU_MODE_SIGNAL_EDGE_DETECT** → §7.2.10;
    a signature's `Icu_ModeType` → §7.2.1); function mentions → their
    defining ch.7 heading at any level (§7.2.9's type description cites
    **Icu_GetEdgeNumbers()**; EcuM's scheduled function
    **EcuM_MainFunction** → `#### 7.6.1`, missed until 2026-10-26 because
    the old rule only scanned §7.2–7.5);
    `参见下表` → the table below; prose `[n]` → the §3.1 entry
    (iohwab: 参见参考文档[9]) — the `[n]` class is applied since
    2026-10-26 (`<a id="ref-n">` + `[n](#ref-n)`); source-typo numbers and
    document-name mismatches stay prose (see Step 5).
  - Cross-article: module names (Det/Dem/CanIf…) whose site article exists.
  - Un-linked plain-text source URLs (see Phase A check 8).
  - **Not linkable — record, don't link**: the target lives in a Type
    A-forbidden chapter (config parameters — port_driver 参见**PORT117**,
    pwm 参见**PwmPowerStateReadyCbkRef** → 配置规范) or an omitted
    sequence-diagram chapter. Keep as prose; list under deliberate omissions;
    never half-link.
  Detection is mechanical: `grep -n '参见\|参考\|详见'` + prose `\[n\]`
  markers; per-module identifier prefixes (`ICU_[A-Z_]*`, `Icu_[A-Za-z]*`)
  mentioned outside their ch.7.2 definition lines. Candidates go into the
  Phase B evidence; adding links is a user decision (queue in TODO.md's
  Backlog), never a silent addition — intra-article links are restoration of
  the source's own hyperlinks, the easiest case to approve.

**Repo workflow:**

1. **Git/PR/issue mechanics are external to this skill** (user decision
   2026-10-25): the user provides dedicated git instruments — the skill does
   not prescribe how branches, commits, issues or PRs are created. Only the
   gate ordering matters here: content work happens before the Step 8
   confirmation, and the queue row records whatever identifiers the
   instruments return (commit hash, PR link).
2. New pages must be registered in `mkdocs.yml` nav (paths are `docs/`-relative)
   or the strict build fails. Removal of pages requires nav cleanup in the
   same commit.

## Step 8 — Confirm, then maintain the progress file

**Confirmation gate — before the final commit and the PR.** Present to the
user, in one message: the queue row's current state (steps + Notes), the
Phase A results, the Phase B coverage map and deviations, and the proposed
`docs/autosar/TODO.md` status row with its source-release note. Wait
for explicit confirmation. Passing Phase A alone never finishes a run — the
gate exists precisely for what the build cannot see. A decision the user
already gave mid-run settles *that item*, not the gate. On any objection: fix,
re-run Phase A, re-present. Never write `确认待补` / "confirmation deferred" in
the queue row — capture the confirmation when it is given, or keep the step
open.

**After confirmation, finish in this order:**

1. Update `docs/autosar/TODO.md` in the same PR: flip the touched article's
   status, refresh its source-release note, update the `Last updated` date.
   Format
   and status definitions: `references/progress-file.md`. TODO.md is the
   status ledger of the whole program (the execution queue is
   `docs/autosar/sync-todo/`) — coverage questions are answered from them (or
   by regenerating them), never by re-inventing an inventory; if a section has
   drifted badly, regenerate it from a fresh gap analysis.
2. Commit (article + queue file + TODO.md), push, open the PR, then record the
   commit hash and PR link on the row's Step 6 note and flip the row `[x]`
   (an immediate follow-up commit is fine). No step is `[x]` before its
   verification passed; no step stays `[ ]` past this point.
3. Report and stop: changes, decisions, deviations, PR link. All 6 steps `[x]`
   = run finished — tell the user which row is next (or that the batch is
   complete). Anything still `[ ]` → say exactly what remains; never report
   the run as finished with an open step.

## Repository quirks that burn you

- `github.com` HTTPS is intermittently flaky — push/fetch via
  `git@github.com:melodypapa/melodypapa.github.io.git`; `gh` (API) always works.
- A failed fetch can break `refs/remotes/origin/master`; repair with
  `git update-ref refs/remotes/origin/master <sha>`.
- `.gitignore` has stale root-anchored Jekyll-era patterns; trust `git ls-files`
  over `git check-ignore`.
- No CI on PRs — the strict build you run locally is the only gate there is.

## Common mistakes (all observed in real runs)

| Mistake | Consequence | Counter |
| --- | --- | --- |
| Skipping Step 0, trusting an older article's structure | Forbidden-chapter residue (需求追踪) and legacy wording spread — the pre-standard IO articles did exactly this | STANDARD.md is read first, always |
| Translating before emitting the todo list | Coverage decisions unreviewable until the work is done | Step 4 output contract |
| Opening figure files (`Figure*.png`) during gap analysis | Pipeline/API image errors | Text-only rule in Step 3 |
| Flagging STANDARD.md-forbidden chapters as "missing" | False work items on compliant articles | Step 3 compliance rule: omissions the standard mandates are compliance |
| Taking the SRS wording as ground truth | "Fixing" faithful SWS translations into errors | Step 4 + source-resolution.md |
| Renaming a heading to STANDARD.md's listed term when most of the site uses a different one (DIO run: STANDARD listed 周期函数, 7 articles used 调度函数 — user kept 调度函数) | Churn in the wrong direction; the standard itself was stale | Before aligning wording, `grep` the heading across `docs/autosar`; if STANDARD.md and the site majority disagree, put the choice in the todo list as a user decision and update STANDARD.md in the same PR |
| Shortening a source heading to fit the canonical list (DIO §3.1: *Input documents & related standards and norms* renamed 「输入文件」 per the then-canonical; user reverted 2026-10-25 to the direct translation 「输入文件和相关标准与规范」 — STANDARD.md updated in the same change) | The canonical list ends up codifying the drift it was meant to prevent — headings drift away from the source wording, site-wide | Headings are direct translations of the source headings; a source heading longer than the §2 rendering is translated in full, never shortened |
| Translating *Configurable Interfaces* as `可配置的接口` because the pre-2026-10-24 §2 listed it (baseline test 2026-10-24: an agent handed the old §2 line reproduced the rejected heading verbatim, while agents given no wording guidance naturally wrote `可配置接口` — the danger is the stale authority, not free translation) | New articles silently diverge from the canonical term — the site's 5 IO articles all read `可配置接口` (user decision 2026-10-24, issue #54; STANDARD.md §2 updated in the same PR) | Phase A check 2's §2 `不用` sweep: grep every forbidden variant on the article to 0 hits |
| Posting the todo list to chat instead of writing the todo file (DIO run, 2026-10-24) | The run's decisions and tick state die with the session; nothing to resume from, nothing to audit | Step 4 output contract + `references/todo-format.md` — the file is the todo, chat is a copy |
| Batch-checking todo items at the end of the run | The list shows progress the work doesn't have; an unverified item hides until the PR review or never | Tick each item in the file the moment its verification passes (Step 4) |
| Finishing on the strict build alone — or opening the PR before the Step 8 gate | The build is blind to coverage, fidelity and wording; the user reviews a PR that was never confirmed | Phase A ≠ done; present Phase A + Phase B evidence and wait for confirmation, then commit/PR (Step 8) |
| Writing "confirmation deferred" / `确认待补` on a todo item | Creates a backlog of rows whose real state nobody knows | Capture the confirmation when given, or leave the item `[ ]` (Step 8) |
| Letting the 缩略语 chapter drift on format or row set (2026-10-24 finding: 6 articles render it as a table, adc_driver dropped API/HW/SW + reordered DET/DEM + split Conversion Mode — 18 source rows became 16 entries, all under ✅ status) | Site-wide format split; silent content loss in the one chapter whose rows are pure lookups | Step 5 acronym-chapter rules; Phase A check 5 makes table-vs-blockquote and row count mechanical. Baseline tests (2026-10-24) show fresh agents comply — the drift happens in long loaded sessions, which is exactly why the check must be a grep, not judgment |
| Trusting the API chapter's shape without checking it entry by entry (PWM run 2026-10-24: ✅-rated article carried `Pwm_ChannelType` with the neighbor type's "8..32 bit" range, and a `PWM_FULL_POWER (0x00)` row that R23-11 does not define — it only exists from R25-11 on) | Silent infidelity in the chapter readers use as a lookup reference; a wrong Range or an unsourced enum value is indistinguishable from the standard to a site reader | Step 5 API-chapter rules: cell-by-cell type-table read; per-requirement function text mapping; Phase A check 7 `check_api_sync.py` for count/name/order; content-vs-source mismatches go to the user as decisions |
| Realigning only the measurable chapters (ch.2/§3/API/new ch.8-9) and leaving a pre-existing §6 with legacy internal structure — the ADC article carried a topical 6.1.x layout under R23-11's Background-&-Rationale/Requirements convention, and its source 7.3 State Diagrams were never translated (found 2026-10-25) | The chapter-level coverage map passes while the body diverges from the source's structure; embedded diagram chapters get skipped as "figures" | Phase B: internal-structure verification per pre-existing chapter (see Coverage map); a realignment that cannot verify internal structure says so in its gate evidence |
| Writing a rule as Phase B prose without a mechanical trigger (potential-links lived as a Phase B bullet for six runs — dio/port/pwm/ocu/icu/ecu/bswm — and was never executed once; its own "user decision" semantics made doing nothing always compliant) | Codified rules that only a gate presentation could surface get dropped when presentations lengthen; the omission is invisible in a deviations-framing | Any new rule gets (a) a tick-box in the step it executes in, and/or (b) a mechanical counter whose zero-output is explicit. Test rules at RUN level ("did a full sync execute it?"), not comprehension level |
