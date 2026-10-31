---
name: autosar-translate
description: >
  Use when working on the AUTOSAR articles of the melodypapa.github.io MkDocs
  site: translating, completing, updating, verifying, or inventorying any
  article under docs/autosar/; syncing a specification document (AUTOSAR
  SWS/EXP/SRS/TPS, releases R22-11/R23-11/R25-11, docs/autosar_pdf PDFs, or
  the ../autosar_standard markdown tree) into a Type A article;
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
   `../autosar_standard/markdown/Classic_Platform/Releases/R23-11/<Category>/AUTOSAR_CP_<Type>_<Name>.md`
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
  applicable requirements*). Their absence is compliance, not a gap — and so is
  a section whose **entire content is a placeholder** (`None.` / `N/A.`):
  omitted entirely per the 2026-10-28 rule (KeyM's Known Limitations `None.`
  precedent, generalized to every section class on the user's instruction) —
  no heading with a lone 无/不适用 body; covers pre-chapters, the optional
  时序图/配置规范 chapters, and placeholder sub-sections inside a chapter with
  other real content; the mandatory §7 API规范 chapter stays with a
  one-sentence statement (STANDARD.md §1/§3). Every omission applied under it
  is **reported** (queue row note + Step 8 gate) and the user reminded to
  verify it — an omission is never silent. The
  absence of ANY other source section is a gap — including *Known
  Limitations* (translates as unnumbered `## 已知限制` before §1 when it has
  actual content), appendix B
  (translates as `## B. …`, Step 5 rule), expected/port-interface chapters
  (EcuM's source 8.7/8.8 were missing from a ✅-rated article — found by the
  2026-10-25 diff), and content diagrams inside translated chapters. The
  配置规范 chapter translates as `## 8. 配置规范` (or `## 9.` when a 时序图
  chapter is also present) and the 时序图 chapter as `## 8. 时序图` when the
  source has them **with actual content** (Step 5 rules; `N/A.`-only chapters
  are omitted and a surviving chapter renumbers down).

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
  requirement IDs, front-matter title only, footer pattern, nav registration
  and the three derived index pages (Step 6.3).
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

- **The main session does the translating — never a subagent** (user
  decision 2026-10-28): article text is written by the session running this
  skill, sequentially, no matter how large the source. The giant-source
  pattern of segmenting a long document by line range across parallel
  subagent writers (RTE/OS runs, 2026-10-25/26) is retired. Read-only
  subagent use (gap analysis, censuses, verification) is not forbidden — but
  a subagent dispatch never produces translated article text: split writers
  cannot carry one terminology, one numbering scheme and the in-place
  insertion discipline across segments, and provider concurrency caps have
  repeatedly blocked dispatches mid-run.
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
    folded into `**说明**` per site convention (Service ID [hex] when
    present, sync/async, re-entrancy, in/out parameters, return value,
    available via `<X>.h`);
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
  present iff the source document has a *Sequence diagrams* chapter **with
  actual content** — a source chapter that is only `N/A.` is omitted entirely
  (user decision 2026-10-28; a following 配置规范 chapter renumbers down,
  grep inbound anchors); source
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
  present iff the source document has a configuration specification **with
  actual content** (an `N/A.`-only chapter is omitted entirely — user decision
  2026-10-28); source
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
  config-container mentions (identifier-titled headings inside the 配置规范
  chapter — `EcuMDriverInitListZero` is §9.1.7, not ch.7, and its pre-ch.9
  参见 mentions must still link; user decision 2026-10-27. Module-named top
  containers are NEVER targets — they are the module NAME, not a container
  mention, and an article never links its own module name. The FIRST
  identifier-titled config heading covers the single-module layout
  (`#### 9.1.1. EcuM`, `#### 9.1.1. Gpt`, `#### 9.1.1. Mcu`); documents with
  TWO config modules (LIN Interface: `#### 9.3.1. LinIf` +
  `#### 9.4.1. LinTp`) are caught by the title check — a config heading
  whose title is a ch.7 identifier prefix (`LinTp_` of **LinTp_Init**) is a
  module name wherever the config chapter puts it, while a real container
  (`EcuMDriverInitListZero` — no ch.7 identifier starts with
  `EcuMDriverInitListZero_`) stays linkable; fixed 2026-10-29 after the LIN
  run's apply linked 9 LinTp self-references. §2 acronym term lines are
  definitions, never mentions — the whole §2 region is skipped by the
  identifier scan (the old bare `**Term**` regex missed term lines with a
  parenthetical like `**LIN TP**（**LinTp**）`). --apply still stops at
  配置规范, so only pre-config-chapter prose converts; the config tables
  stay definitional. A same-named ch.7 heading always wins over the config
  heading),
  chapter-number refs (可参见第**6.3**章 / 章节**6.1.1** / 可参考章节6.3启动…和
  6.4 关闭 — link text is the number token with its bold markers:
  第[**6.3**](#63-startup阶段)章, matching the hand-written
  [6.6.4 WakeupValidation序列中的活动](#664-…) convention; user decision
  2026-10-27. A ref is 第N章/第N节/章节N or a dotted number followed by CJK
  text, AND only converts when a heading with that number exists. Never a
  ref: figure/table numbers (图 9.5 所示, 表 7.3 — captions carry no anchor
  and 表7.x would collide with the §7.x API sections), code-listing numbers
  (清单3.4 / 示例3.4 — the mode-management guide's `lstlisting.3.N`
  artifacts, which collide with its §3.4; guard added 2026-10-27), bare-integer 第N part
  numbers (第1部分 in figure captions), identifier tails (B.2.2), decimals
  followed by ASCII units (3.3 V), and a number whose preceding window names
  another AUTOSAR document — by doc id (按照AUTOSAR_SWS_Mcu_Driver第9.1章 is
  the MCU driver's §9.1, not this article's), by 《title》 or a bolded
  English "Specification …" title (《基础软件模块通用规范》（**General
  Specification of Basic Software Modules**）的第7.2章 is SWS_BSWGeneral's
  §7.2 — it had linked to BswM's own §7.2 类型定义), or by a citation marker
  [n] in the window (参见相关文档[6]中第13.6.5节; guards added 2026-10-27 from
  the mode_management dry-runs). A number no heading carries
  (EcuM's 参见7.9节多核 — source renumbering artifact) is census-reported
  UNRESOLVED and never linked; a 译者注/fix is a user decision),
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
- **The link census is article-only.** `link_candidates.py --list <article>`
  is the required report, and `--apply` remains limited to the applied
  intra-article classes above. A PDF annotation census is not part of routine
  syncs: it is report-only, expensive, and does not authorize individual link
  edits. Keep cross-article, anchor-less, and other report-only candidates
  unlinked unless a user explicitly approves them. PDFs remain available as
  source references for translation and content fidelity checks.
- **Citation markers `[n]` mean "Related documentation, entry n"** — a
  two-hop reference: citation → §3.1 entry → an external document or a page
  on this site. **Hop 1 is an applied class (user decision 2026-10-26)**: the
  marker itself links to the §3.1 entry, restoring the source PDF's own
  citation hyperlink — `--apply` prefixes every registry entry line with an
  invisible anchor (`<a id="ref-n"></a>`) and converts prose `[n]` to
  `[\[n\]](#ref-n)` (brackets kept visible in the rendered link — user
  decision 2026-10-27; the earlier plain `[n](#ref-n)` form rendered as bare
  n and was migrated), but ONLY for numbers the registry defines. Three things
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

## Step 6 — Regenerate the derived indexes (glossary, API list, site indexes)

`docs/autosar/api/` (landing page + type list + function list) is a
**pure derivation** (regenerate via `gen_api_list.py` when its source data
changed); `glossary.md` is
**manually extended during translation runs** (see below — user decision
2026-10-24).

1. **Glossary `glossary.md`** — **manually extended during translation
   runs** (user decisions 2026-10-24/25, superseding the script scan): when
   an article or TR batch is translated, the run adds that article's/batch's
   terms to the page by hand with 来源 attribution (document title as link
   text, spec). **Page format (2026-10-25): flat alphabetical** —
   `## <letter>` sections, all entries A–Z across documents (no
   per-document sections, no methodology prose on the page); each entry =
   `**Term**` + one definition line + one 「来源：」 line carrying **all**
   contributing documents. Terms are extracted from the SOURCE
   during translation — never machine-extracted from the translated article
   afterwards; `gen_glossary.py` is retired. **One term is translated once**
   (user rule 2026-10-24): the same term appearing in another document is NOT
   re-translated — keep the one definition and append that document to the
   same 「来源：」 line; a substantively different definition is a user
   decision, never a silent second line. The
   Foundation TR glossary's translation state is tracked in
   `scripts/tr_glossary.json` (source-extraction workfile, not a build
   input).

   **Entry format (2026-10-30)** — the definition and its attribution are
   separate paragraphs, so the attribution is visually demoted (a
   `.glossary-source` rule in `docs/stylesheets/extra.css` shrinks and
   lightens it) instead of running on from the definition as one paragraph:

   ```markdown
   **Term**
   > 释义正文
   >
   > 来源：[Doc A](a.md)（SWS_A）、[Doc B](b.md)（SWS_B）
   {: .glossary-source}
   ```

   - the `>` separator line makes the attribution its own paragraph —
     **without it** python-markdown merges the definition and the 来源 into
     one `<p>` and the two read as one continuous sentence;
   - the trailing `{: .glossary-source}` attribute is what the CSS targets;
     it must follow the attribution line directly;
   - multiple sources sit on **one** 来源 line, separated by `、` (not one
     line per document);
   - the release is **not** repeated per line — the page intro states
     `R23-11` once, and each 来源 item carries only its spec id
     (`（SWS_A）`);
   - a term heading is followed by a **blank line** before its definition
     block; a `**Term**` line glued to the previous entry's attribution is
     swallowed into that entry's `<blockquote>` and loses its heading;
   - entries are sorted alphabetically inside their letter section, and a
     term's section is decided by **its own first letter** (not by where it
     was pasted). `scripts/rewrite_glossary.py` normalizes the whole page
     (format, ordering, duplicate handling) and is re-runnable; it refuses
     to guess at a substantively different definition.
2. **API listing `docs/autosar/api/`** — landing page plus two A–Z pages
   (types 8.2 / functions 8.3), **article-based**: only identifiers whose
   translated article carries a matching heading are listed, and each
   identifier deep-links to that heading's anchor. Regenerate after any
   front-matter `spec:` change, article addition, or API-chapter change:
   `python .agents/skills/autosar-translate/scripts/gen_api_list.py`. Its
   `dropped (no heading in article)` report lines are recorded limitations,
   not errors to silence — they mark API chapters the article does not
   deliver yet.
3. **Site indexes — nav + three landing-page levels** (user decision
   2026-10-29). `mkdocs.yml`'s `nav` is the single source of truth; every
   index page is derived from it, so a nav change and its index updates ship
   in the same commit. `navigation.indexes` is enabled, so a section's
   landing page is the **unlabeled first child** of its nav list
   (`- autosar/general/index.md`), never a labeled sibling.
   - **`mkdocs.yml` nav** — every published page is registered under its
     section with `docs/`-relative paths; renames and removals update the nav
     in the same commit. A nav page label is the **simple name** — the module
     abbreviation or short domain name (`Powertrain`, `Chassis`, `ARTI`,
     `VFB`, `FOTA`, `SwCluC`) — never the full bilingual title (user rule
     2026-10-29); the full name belongs to the article title and the index
     link labels. A page can build cleanly and still be unreachable from the
     indexes: `--strict` only catches a nav entry with no file.
   - **Section landing page** (`docs/autosar/<section>/index.md`) — fixed
     shape: front-matter `title`, one intro paragraph, `## 文章`,
     `## 相关内容`. `## 文章` lists **every** page of that nav branch in nav
     order (nested `*` bullets for sub-groups); link text is the target's
     front-matter `title`, never a directory identifier, and it keeps the
     `English（中文）` structure below.
   - **CP AUTOSAR overview** (`docs/autosar/index.md`) — mirrors the whole
     `CP AUTOSAR` nav branch: one `###` group per nav section in nav order,
     each starting with its landing page, every content page appearing
     exactly once underneath it; standalone pages (`autosar/power`) get their
     own group. `## 相关内容` keeps 术语表 / API 清单 / 首页.
   - **Site home** (`docs/index.md`) — one bullet per top-level nav tab, in
     nav order, label = nav label (including its `（…）` gloss), target = the
     section's landing page or its first page when the section has none;
     `About` last.
   - **Entry structure** — a bilingual article title/label is
     `English（中文）`: the English document or module name first, its Chinese
     rendering in full-width parentheses, matching the sibling entries
     (`AUTOSAR Crypto Driver（加密驱动程序）`,
     `Layered Software Architecture（分层软件架构）`). `中文（English）` is
     invalid (user rule 2026-10-29;
     `加密服务使用指南（Utilization of Crypto Services）` was corrected to
     `Utilization of Crypto Services（加密服务使用指南）`). A Chinese-first
     title is fixed at the front-matter `title`, not only in the link label,
     and the rename propagates to the landing page, the overview,
     `glossary.md` 来源 lines and the API listing (`docs/autosar/api/`) in the same commit.
     The three levels are deliberately different (user rule 2026-10-29):
     the **article front-matter `title` and every index link label** carry the
     full `English（中文）` name (`Powertrain Engine Domain（动力总成（发动机）域）`),
     while the **`mkdocs.yml` page label** stays the simple name (`Powertrain`,
     `Chassis`, `ARTI`). Section
     landing-page titles and nav section labels keep the existing
     `中文（English）` form (`通信（Communication）`). A `中文（English）`
     article title or an empty Chinese half (`Title（）`) is invalid. Both
     language halves must describe the same document/module: verify the
     English name and Chinese rendering against the `spec:` source and
     authoritative acronym expansion, rather than only checking their order.
     A standard acronym may pair with its Chinese expansion
     (`VFB（虚拟功能总线）`). `check_indexes.py --titles` detects structural
     issues only; it cannot judge translation meaning. Fix a confirmed
     mismatch in the front-matter `title`, every index link label,
     `glossary.md` 来源 line and the API listing (`docs/autosar/api/`) in the same commit.
   - Link targets are relative to the file that contains them; angle-bracket
     a target containing a space
     (`<communication/data_distribution service/index.md>`). An empty `（）`
     is a defect in the title itself: fill in the Chinese half and propagate
     the fixed title to every link label in the same commit.
   - Mechanical check: `python
     .agents/skills/autosar-translate/scripts/check_indexes.py` — exit 0
     means every nav target exists, the overview and every section landing
     page link their full branch, the home links every tab, and no index link
     is broken. Add `--titles` to audit the `English（中文）` structure of
     article titles, including empty halves and reversed order (report-only;
     semantic equivalence must be checked against the source).

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
   `## 已知限制` before `## 1.` when the source's Known Limitations
   chapter has actual content (a `None.`-only chapter is omitted — user
   decision 2026-10-28); `###`/`####` numbering
   is continuous (no numbering gaps); no appendix A (`## A.`), and no forbidden
   chapter title (需求可追溯性 / 需求追踪) anywhere; `## B.` is allowed only
   as the 可追溯项变更历史 appendix; `## 8.` is
   allowed only as `## 8. 时序图` and `## 9.` only as `## 9. 配置规范`
   (both optional — only when the source has ch.9 / ch.10 **with actual
   content**; `N/A.`-only chapters are omitted and a surviving chapter takes
   the lower number); a **numbered
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
   **Sub-heading language**: every `###`+ heading title is a direct translation
   of its source heading and therefore carries Chinese — the `grep '^## '` audit
   above only sees the level-2 skeleton, so an untranslated `###`/`####`
   sub-heading passes it silently (the GlobalTime batch shipped 115 of them:
   StbM 12, CanTSyn 52, EthTSyn 51 — the prose was translated but the source
   heading text was copied verbatim). Run
   `python .agents/skills/autosar-translate/scripts/check_heading_lang.py <article>`:
   exit 0 proves every sub-heading is translated. Identifier-titled headings
   are exempt — API/type/container/port names stay verbatim (STANDARD.md §4):
   the script recognizes them by shape (`StbM_Init`, `StbMGeneral`, `ISRType`,
   `IOC`) and by the configuration container's own `模块名称`/`容器名称` table
   cell (`Dio`, `Crypto`, `Spi`). Every prose title — including single words
   that read like names (`General`, `Common`, `Accuracy`, `Variants`) — is
   flagged and must be translated. `--site` sweeps the whole corpus; use it
   to find the same defect in articles already published.
3. Hygiene greps: no `^# ` in the body; no requirement IDs
   (`\[[A-Z][A-Za-z]*_[A-Za-z0-9]*_[0-9]+\]`) and no `{DRAFT}`; a WeChat
   footer, if present, is `<section id="wechat">` + `<h4>`, never a markdown
   heading; angle-bracket placeholders (`<X>`, `<Service>`, `<#channel>`)
   render as `&lt;…&gt;` — `grep -c '\\<' <article>` must be 0 (the
   `\<…\>` form renders a stray backslash on this site, STANDARD.md §4).
4. Nav, indexes and anchors: new pages registered in `mkdocs.yml` (paths
   `docs/`-relative), removed pages cleaned in the same commit; renamed or
   renumbered headings — grep inbound `](…#…)` links site-wide and fix them in
   the same commit. Then run
   `python .agents/skills/autosar-translate/scripts/check_indexes.py`: exit 0
   proves nav, the CP AUTOSAR overview, every section landing page and the
   site home agree (Step 6.3). A page present in nav but missing from its
   landing page or the overview is a failed gate, not a pass — the build
   cannot see it.
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
   scheduled functions, port interfaces — PLUS identifier-titled 配置规范
   container headings with the module-named top container excluded; scanned
   through 时序图 prose, counted but never applied inside 配置规范 tables),
   chapter-number refs (applied class, with their UNRESOLVED list — numbers
   no heading carries), dev-error codes §6.6.x
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
   committing. The article-only census is the complete required link-census
   output; no PDF annotation census is needed.

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
    2026-10-26 (`<a id="ref-n">` + `[\[n\]](#ref-n)`, bracket-preserving
    since 2026-10-27); source-typo numbers and
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
   same commit. Nav registration alone is not publication: the same commit
   updates the section landing page, the CP AUTOSAR overview and (for a new
   tab) the site home, then runs `scripts/check_indexes.py` (Step 6.3).

## Step 8 — Confirm, then maintain the progress file

**Confirmation gate — before the final commit and the PR.** Present to the
user, in one message: the queue row's current state (steps + Notes), the
Phase A results, the Phase B coverage map and deviations, and the proposed
`docs/autosar/TODO.md` status row with its source-release note. The
coverage map must list **every section omitted under the placeholder
exception** (`None.`/`N.A.`-only sections) as a deliberate omission, each
with a reminder for the user to verify it before confirmation. Wait
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
| Copying the source's heading text verbatim into the article instead of translating it (GlobalTime batch 2026-10-30: 115 `###`+ headings shipped in English — StbM 12, CanTSyn 52, EthTSyn 51 — while the prose beneath them was Chinese; the `grep '^## '` audit saw only the level-2 skeleton and passed) | A bilingual-looking article whose table of contents reads as a list of English source section names — the reader sees untranslated content the standard's own chapter titles never were | Every heading title is a direct translation of its source heading; identifier-titled headings (API/type/container/port names) stay verbatim, prose titles translate even when they look like names (General, Common, Accuracy, Variants). Phase A check 2 runs `check_heading_lang.py`, which flags CJK-less `###`+ titles |
| Translating *Configurable Interfaces* as `可配置的接口` because the pre-2026-10-24 §2 listed it (baseline test 2026-10-24: an agent handed the old §2 line reproduced the rejected heading verbatim, while agents given no wording guidance naturally wrote `可配置接口` — the danger is the stale authority, not free translation) | New articles silently diverge from the canonical term — the site's 5 IO articles all read `可配置接口` (user decision 2026-10-24, issue #54; STANDARD.md §2 updated in the same PR) | Phase A check 2's §2 `不用` sweep: grep every forbidden variant on the article to 0 hits |
| Posting the todo list to chat instead of writing the todo file (DIO run, 2026-10-24) | The run's decisions and tick state die with the session; nothing to resume from, nothing to audit | Step 4 output contract + `references/todo-format.md` — the file is the todo, chat is a copy |
| Batch-checking todo items at the end of the run | The list shows progress the work doesn't have; an unverified item hides until the PR review or never | Tick each item in the file the moment its verification passes (Step 4) |
| Finishing on the strict build alone — or opening the PR before the Step 8 gate | The build is blind to coverage, fidelity and wording; the user reviews a PR that was never confirmed | Phase A ≠ done; present Phase A + Phase B evidence and wait for confirmation, then commit/PR (Step 8) |
| Writing "confirmation deferred" / `确认待补` on a todo item | Creates a backlog of rows whose real state nobody knows | Capture the confirmation when given, or leave the item `[ ]` (Step 8) |
| Letting the 缩略语 chapter drift on format or row set (2026-10-24 finding: 6 articles render it as a table, adc_driver dropped API/HW/SW + reordered DET/DEM + split Conversion Mode — 18 source rows became 16 entries, all under ✅ status) | Site-wide format split; silent content loss in the one chapter whose rows are pure lookups | Step 5 acronym-chapter rules; Phase A check 5 makes table-vs-blockquote and row count mechanical. Baseline tests (2026-10-24) show fresh agents comply — the drift happens in long loaded sessions, which is exactly why the check must be a grep, not judgment |
| Trusting the API chapter's shape without checking it entry by entry (PWM run 2026-10-24: ✅-rated article carried `Pwm_ChannelType` with the neighbor type's "8..32 bit" range, and a `PWM_FULL_POWER (0x00)` row that R23-11 does not define — it only exists from R25-11 on) | Silent infidelity in the chapter readers use as a lookup reference; a wrong Range or an unsourced enum value is indistinguishable from the standard to a site reader | Step 5 API-chapter rules: cell-by-cell type-table read; per-requirement function text mapping; Phase A check 7 `check_api_sync.py` for count/name/order; content-vs-source mismatches go to the user as decisions |
| Realigning only the measurable chapters (ch.2/§3/API/new ch.8-9) and leaving a pre-existing §6 with legacy internal structure — the ADC article carried a topical 6.1.x layout under R23-11's Background-&-Rationale/Requirements convention, and its source 7.3 State Diagrams were never translated (found 2026-10-25) | The chapter-level coverage map passes while the body diverges from the source's structure; embedded diagram chapters get skipped as "figures" | Phase B: internal-structure verification per pre-existing chapter (see Coverage map); a realignment that cannot verify internal structure says so in its gate evidence |
| Writing a rule as Phase B prose without a mechanical trigger (potential-links lived as a Phase B bullet for six runs — dio/port/pwm/ocu/icu/ecu/bswm — and was never executed once; its own "user decision" semantics made doing nothing always compliant) | Codified rules that only a gate presentation could surface get dropped when presentations lengthen; the omission is invisible in a deviations-framing | Any new rule gets (a) a tick-box in the step it executes in, and/or (b) a mechanical counter whose zero-output is explicit. Test rules at RUN level ("did a full sync execute it?"), not comprehension level |
| Turning report-only link candidates into individual edits | Unreviewed candidates can create wrong or unwanted links, and one-by-one patching is costly | Use article-only `--list` for the required census; `--apply` handles only documented classes, while other candidates stay report-only until a user decision |
| Registering a new page in `mkdocs.yml` only (the five `general` guides shipped in nav on 2026-10-29 but absent from `general/index.md` and the CP AUTOSAR overview) | The page is reachable from the sidebar but invisible to a reader browsing the section or the landing page; the strict build cannot see the gap | Step 6.3 + Phase A check 4: `check_indexes.py` fails when any branch page is missing from its landing page or the overview |
| Letting an index entry copy a Chinese-first title verbatim (`加密服务使用指南（Utilization of Crypto Services）`) | The entry breaks the list's `English（中文）` structure, so the same list mixes two conventions | Step 6.3 entry-structure rule: fix the article's front-matter `title` to `English（中文）`, then propagate to the index labels, `glossary.md` 来源 line and the API listing (`docs/autosar/api/`); `check_indexes.py --titles` lists remaining drift |
| Delegating translation to subagents — the RTE/OS runs segmented giant sources by line range across parallel writer agents (2026-10-25/26), and provider concurrency caps repeatedly blocked dispatches mid-run | Split writers cannot carry one terminology, one numbering scheme and the in-place insertion discipline across segments; a capped dispatch stalls the run with half-translated segments; the queue-row ticks and user decisions live in the main session, not in the writers | Step 5 rule 1: the main session translates sequentially; subagent dispatches never write article text (user decision 2026-10-28) |
| Writing a glossary entry without the `>` separator line before its 「来源：」 line, or gluing the next `**Term**` heading straight onto the previous entry's attribution | Without the separator, python-markdown merges definition and attribution into one `<p>` — the attribution reads as part of the definition (found on all 558 entries, 2026-10-30); a glued heading is swallowed into the previous entry's `<blockquote>` and loses its own heading (13 entries) | Step 6.1 entry format: `**Term**` / `> 释义` / `>` / `> 来源：…` / `{: .glossary-source}`; `scripts/rewrite_glossary.py` normalizes the page and the strict build shows the resulting HTML |
