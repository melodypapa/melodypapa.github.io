# Progress file — docs/autosar/TODO.md

The TODO file is the running work queue of the AUTOSAR translation program.
It lives in the repo at `docs/autosar/TODO.md`, is excluded from the site
build (`exclude_docs` in `mkdocs.yml`), and is maintained by this skill.

## Maintenance rules

1. After **every** sync that touches an article, update that article's row in
   the same PR: new status, refreshed note, and bump the `Last updated` date
   at the top.
2. When creating a brand-new article, move its row from the ❌ list into the
   section list with the appropriate status.
3. Never reorder or reformat sections casually — the file is diffed across
   PRs; keep one bullet per spec, stable ordering (alphabetical by spec name
   within a section).
4. If the file has drifted badly (many syncs skipped it), regenerate the
   affected sections from a fresh gap analysis instead of patching blindly.

## Format

```markdown
# AUTOSAR Article Translation Progress

> Maintained by the autosar-translate skill per [STANDARD.md](STANDARD.md); update the touched entry and the `Last updated` date after every sync.
> Status: ✅ Type A-compliant · 🔶 Translated pending alignment · ⚠️ Partial · ⛔ Stub · ❌ Missing · 📖 Guide/topic (exempt from the skeleton)
> Baseline: R23-11 · Last updated: YYYY-MM-DD

## Overview
(one summary table: counts per status, coverage %)

## <section>            (one section per site dir: communication, io, …)
- ✅ [article title](relative link) — SWS_spec
- 🔶 [article title](relative link) — SWS_spec (one-line deviation reason)
- ⚠️ [article title](relative link) — SWS_spec (what's missing)
- ⛔ [article title](relative link) — SWS_spec (stub)
- ❌ SWS_spec (abbreviation) — no article
- 📖 [guide article](relative link) — EXP_spec (exempt from the skeleton)
```

## Work todo lists (per-run)

The execution queue is the **persistent batch-queue files** in
`docs/autosar/sync-todo/` (`Group-<section>.md`, one row per document with a
6-step sub-checklist; `index.md` orders batches) — one row consumed per run,
never conversation-only (`todo.md` alongside the outputs for a workspace run).
Format, row template, resume and tick rules: `references/todo-format.md`.
Program-level fixes outside single-article runs (wording sweeps, hygiene)
live in the `## Backlog` section at the top of `TODO.md` as `- [ ]` items.

Rules for queue rows:

- One verifiable action per step; findings and decisions on `- Note:` bullets
  under the row, appended when they happen.
- A row's inputs: STANDARD.md rule checklist, the article's current row in
  this file, and the fresh gap analysis — plus mid-run user decisions.
- Ticked items in `## Backlog` get removed (or archived) once the
  corresponding status row has been updated — a work item is done only when
  its status row says so.
- The two files are linked: a status row flips (Step 8) only after the queue
  row's 6 steps are `[x]` and the Step 8 user confirmation was given; the
  flipped queue row (with commit hash + PR link) is the evidence behind the
  status row.

## Status definitions

| Status | Meaning |
| --- | --- |
| ✅ Type A-compliant | Seven chapters present, canonical wording, no forbidden chapters |
| 🔶 Translated pending alignment | Complete seven chapters but with legacy wording, extra site-specific chapters, or forbidden-chapter residue |
| ⚠️ Partial | Skeleton incomplete — missing ≥1 chapter (often just 「API规范」) |
| ⛔ Stub | ≤ ~19 lines, effectively empty |
| ❌ Missing | No article for the spec |
| 📖 Guide/topic | EXP guides, TPS templates, bespoke topic articles — exempt from the Type A skeleton (STANDARD.md §7) |

## Status transitions

- ⛔/⚠️ → ✅: after a sync completes the missing chapters AND aligns wording.
- 🔶 → ✅: after a wording/forbidden-chapter alignment pass.
- ❌ → ⚠️/✅: after a first translation (⚠️ if delivered partial by agreement).
- Never mark ✅ without running the strict build and comparing chapter headings
  against STANDARD.md §1/§2.
