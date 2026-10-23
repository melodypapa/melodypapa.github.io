---
name: autosar-sync
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
list** and show it to the user. Two sources feed it:

- **The rule**: expand `docs/autosar/STANDARD.md` into a per-article checklist
  — 7-chapter skeleton, canonical chapter wording, no forbidden chapters, no
  requirement IDs, front-matter title only, footer pattern, nav registration.
- **The progress**: the article's current row in `docs/autosar/TODO.md` plus
  the gap-analysis results.

Emit it as checkbox items ordered by risk/effort, e.g.
`- [ ] 补齐第 7 章 API 规范（17 个函数）`、`- [ ] 第 2 章标题改为「缩略语」`.

**Output contract:** the todo list is the run's *first deliverable*, emitted
before any translation editing. For file-based work, save it as `todo.md`
alongside the outputs (or post it to the user) and get a check-off for every
item as it passes verification. Observed failure when this step is skipped
(iteration-1 baseline): the agent translated end-to-end and only surfaced its
plan afterwards, as prose — coverage decisions were never reviewable before
the work was done. The todo list drives translation, and its final state is
recorded in `docs/autosar/TODO.md` (Step 7). For a full-program run
(inventory or batch sync), extend the program-level 待办清单 at the top of
`TODO.md` instead.

## Step 5 — Translate in place

- Existing translated content is never rewritten; fill gaps only, inserting
  at the position where the source has them.
- Faithful translation of the standard's own wording — not a summary in your
  own words. Verify doubtful passages against the SWS, not the SRS (they
  genuinely differ; the ADC driver "works on channel groups" is SWS-faithful).
- Pseudo-code listings stay verbatim in code fences (reconstruct the
  PDF-extraction garbling into readable formatting); prose is translated;
  figures are omitted.
- Chapter numbering stays stable; when insertion forces a renumber, grep for
  inbound anchor links first and fix them in the same commit.

## Step 6 — Repo workflow

1. `gh issue create` (tracking) → `git switch -c feature/<topic> origin/master`.
2. Gate before every commit: `mkdocs build --strict` via the venv recipe in
   the repo `AGENTS.md`; zero WARNINGs expected (pre-existing INFO anchor
   notices are fine).
3. Commit per article (`docs: translate/complete <module> from <source doc>`),
   `Closes #N` in commit + PR body.
4. New pages must be registered in `mkdocs.yml` nav (paths are `docs/`-relative)
   or the strict build fails. Removal of pages requires nav cleanup in the
   same commit.

## Step 7 — Maintain the progress file

Every sync run ends by updating `docs/autosar/TODO.md` in the same PR: flip the
touched article's status, refresh its source-release note, and update the
`最后更新` date. Format spec and status definitions: read
`references/progress-file.md`. The TODO file is the running work queue for the
whole translation program — coverage questions should be answered from it (or
by regenerating it) rather than by re-inventing an inventory. If it has drifted
badly from reality, regenerate the affected sections with a fresh gap analysis.

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
