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
  exists. If the article intentionally omits chapters that `STANDARD.md`
  forbids (tracing, sequence diagrams, config specs, appendices), that is
  compliance, not a gap.

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
inventory) is the "translate one by one" backbone; `TODO.md`'s 待办清单 keeps
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
- **缩略语章（ch.2）格式**：源文档的缩略语表改排为「粗体术语行 + `>` 引用块释义」——
  **不保留 GFM 表格**，即使源是表格且每条释义都只有一行（站内曾 20 篇引用块 vs 6 篇表格
  分裂，表格在长释义下不可读）。细则：
  - 术语行 = 源 Abbreviation/Acronym 单元格**逐字加粗**，含括号别名
    （`**ADC Result Buffer**（**ADC Streaming Buffer**，**ADC Stream Buffer**）`式）；
  - 纯缩写词的释义写 `中文全称（**English Full Name**）`；术语条目译描述句，英文术语加粗；
    `[n]` 引用标记丢弃；源行内的 Note 译为释义内的 `**注意：**` 段；
  - **行集与行序与源表严格一致**：一条不多不少、不拆分（源一行 *Conversion Mode* 讲两种
    模式就译成一条）、不重排、不删"看起来太通用"的行（adc_driver 曾丢 API/HW/SW 三条、
    DET/DEM 对调、一行拆二，✅ 评级下无人察觉）；
  - 源有散文导语句则译出保留，"the following table"式措辞随格式改为"以下"；源只有表题
    （Table 2.1）则不造导语句。
- Chapter numbering stays stable; when insertion forces a renumber, grep for
  inbound anchor links first and fix them in the same commit.

## Step 6 — Regenerate the derived indexes (glossary + API list)

Two files under `docs/autosar/` are **pure derivations** — regenerate and
commit them in the same PR whenever their input changed; **never hand-edit
them**.

1. **术语表 `glossary.md`** — every ch.2 term across all articles, A–Z,
   deduplicated per module, each definition attributed to its source article
   with the document and release (front-matter `spec:` / `release:`).
   Regenerate after any 缩略语 chapter edit:
   `python .agents/skills/autosar-translate/scripts/gen_glossary.py`.
   Read its report: a `! article: ch.2 present but no entries parsed` line is
   a drift signal (that ch.2 is prose or intro-only — fix the article, don't
   silence the line); `(table — 待改排)` flags a legacy GFM-table ch.2.
2. **API 清单 `api_reference.md`** — every type (8.2) and function (8.3)
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
   skeleton with §2 wording, numbered `1.`–`7.` only; `###`/`####` numbering
   is continuous (no 断档); no `## 8.`, lettered appendix, or forbidden chapter
   title (需求可追溯性 / 需求追踪 / 时序图 / 配置规范) anywhere. **Before renaming
   a heading to a STANDARD.md term, grep that heading across `docs/autosar`** —
   if the standard and the site majority disagree, it is a user decision
   (record it; update STANDARD.md in the same PR), not a silent rename.
   Then sweep §2's `不用` variants mechanically: for every variant STANDARD.md
   §2 forbids (`可配置的接口`, `周期函数`, `适用于汽车领域`, …),
   `grep -nE '^#+.*VARIANT'` on the article must return 0 hits (canonical:
   `可配置接口`, `调度函数`, `汽车域的适用性`). §2 governs chapter heading
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
5. 缩略语章：`sed -n '/^## 2\. 缩略语/,/^## 3\./p' <article>` 切片内 `^| ` 行数
   必须为 0（禁表格）；`^\*\*[^*]+\*\*\s*$` 术语行条数 == 源表数据行数（逐行核对行集与
   行序 — 该章在长会话中最易漂移：adc_driver 曾 18 源行译成 16 条而通过所有检查；
   术语行允许尾随空格 — bswm/ethernet_interface 等多篇文章的行尾都有空格）。
6. Derived indexes: both `gen_glossary.py --check` and `gen_api_list.py
   --check` exit 0 — the committed `glossary.md` / `api_reference.md` match
   the articles and front-matter (regenerate per Step 6 if stale).

**Phase B — automation-blind checks** (presented at the Step 8 gate as
evidence, not asserted):

- Coverage map: every translatable source `##` section ↔ an article section;
  the forbidden source chapters listed as deliberate omissions.
- Fidelity: doubtful passages verified against the **SWS** (not SRS);
  pseudo-code verbatim in fences; figures omitted or local PNGs only.
- Scope discipline: existing translated content untouched, gaps filled in
  place, chapter numbering stable.
- Decisions applied: every mid-run user decision in the queue row's Notes is
  reflected in the article (and in STANDARD.md when a canonical term changed).

**Repo workflow:**

1. `gh issue create` (tracking) → `git switch -c feature/<topic> origin/master`
   — **before the first edit**, so every change lands on the branch.
2. Commit per article (`docs: translate/complete <module> from <source doc>`),
   `Closes #N` in commit + PR body, naming the source release used. The PR is
   opened only after the Step 8 confirmation.
3. New pages must be registered in `mkdocs.yml` nav (paths are `docs/`-relative)
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
   status, refresh its source-release note, update the `最后更新` date. Format
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
| Skipping Step 0, trusting an older article's structure | Forbidden-chapter residue (时序图/配置规范/需求追踪) and legacy wording spread — the pre-standard IO articles did exactly this | STANDARD.md is read first, always |
| Translating before emitting the todo list | Coverage decisions unreviewable until the work is done | Step 4 output contract |
| Opening figure files (`Figure*.png`) during gap analysis | Pipeline/API image errors | Text-only rule in Step 3 |
| Flagging STANDARD.md-forbidden chapters as "missing" | False work items on compliant articles | Step 3 compliance rule: omissions the standard mandates are compliance |
| Taking the SRS wording as ground truth | "Fixing" faithful SWS translations into errors | Step 4 + source-resolution.md |
| Renaming a heading to STANDARD.md's listed term when most of the site uses a different one (DIO run: STANDARD listed 周期函数, 7 articles used 调度函数 — user kept 调度函数) | Churn in the wrong direction; the standard itself was stale | Before aligning wording, `grep` the heading across `docs/autosar`; if STANDARD.md and the site majority disagree, put the choice in the todo list as a user decision and update STANDARD.md in the same PR |
| Translating *Configurable Interfaces* as `可配置的接口` because the pre-2026-10-24 §2 listed it (baseline test 2026-10-24: an agent handed the old §2 line reproduced the rejected heading verbatim, while agents given no wording guidance naturally wrote `可配置接口` — the danger is the stale authority, not free translation) | New articles silently diverge from the canonical term — the site's 5 IO articles all read `可配置接口` (user decision 2026-10-24, issue #54; STANDARD.md §2 updated in the same PR) | Phase A check 2's §2 `不用` sweep: grep every forbidden variant on the article to 0 hits |
| Posting the todo list to chat instead of writing the todo file (DIO run, 2026-10-24) | The run's decisions and tick state die with the session; nothing to resume from, nothing to audit | Step 4 output contract + `references/todo-format.md` — the file is the todo, chat is a copy |
| Batch-checking todo items at the end of the run | The list shows progress the work doesn't have; an unverified item hides until the PR review or never | Tick each item in the file the moment its verification passes (Step 4) |
| Finishing on the strict build alone — or opening the PR before the Step 8 gate | The build is blind to coverage, fidelity and wording; the user reviews a PR that was never confirmed | Phase A ≠ done; present Phase A + Phase B evidence and wait for confirmation, then commit/PR (Step 8) |
| Writing "confirmation deferred" / `确认待补` on a todo item | Creates a backlog of rows whose real state nobody knows | Capture the confirmation when given, or leave the item `[ ]` (Step 8) |
| Letting the 缩略语 chapter drift on format or row set (2026-10-24 finding: 6 articles render it as a table, adc_driver dropped API/HW/SW + reordered DET/DEM + split Conversion Mode — 18 source rows became 16 entries, all under ✅ status) | Site-wide format split; silent content loss in the one chapter whose rows are pure lookups | Step 5 缩略语 rules; Phase A check 5 makes table-vs-blockquote and row count mechanical. Baseline tests (2026-10-24) show fresh agents comply — the drift happens in long loaded sessions, which is exactly why the check must be a grep, not judgment |
