# AUTOSAR translation queue — index

> Regrouped 2026-11-11 into the two-group model (matching [`../TODO.md`](../TODO.md)'s `## Unfinished（未完成）` / `## Finished（已完成）`): all former per-batch `Group-<section>.md` files (19 batches, 267 rows) were consolidated —
> done rows into [Group-finished.md](Group-finished.md) (condensed records: article · spec · date · commits · PRs; full row blocks remain in the git history of the deleted files), open rows into [Group-unfinished.md](Group-unfinished.md) (verbatim, with 6-step checklists).
> Base: R23-11 (`~/Workspace/autosar_standard/markdown/` — `Classic_Platform/` for CP, `Foundation/` for FO).
> **Resume = the first row still `[ ]` in [Group-unfinished.md](Group-unfinished.md)**; format and tick rules: `references/todo-format.md` (autosar-translate skill).
> The status ledger (what each article currently IS) is [`../TODO.md`](../TODO.md); this directory is the execution queue (what to do next).

## Open work (Group-unfinished.md)

| Source batch | Open rows | State |
| --- | ---: | --- |
| [Group-cp-methodology.md] — CP 方法论与模板 (RS 6 / TPS 7 / TR 4) | 17 | Actively running in worktree `~/Workspace/melodypapa-cp-methodology` (branch `feature/cp-methodology-queue`, 9/17 ticked locally, batch-gate-at-end); the file's original header (scope, slug rule, article shape, open item-ID decision) is preserved in Group-unfinished.md |
| [Group-foundation-exp.md] — Foundation guide/template/report docs | 1 | `tps_generic_structure_template` — fully worked (Steps 1–6), PR #320 open against master; row flips `[x]` at merge |

**Total: 18 open rows.** Everything else in the R23-11 program is delivered: CP SWS 127/127, CP EXP guides 22/22, Foundation FO 51/52 merged (the 52nd is the GST row above).

## Former batch order (all complete — archived in Group-finished.md)

| # | Batch | Rows done | Completed |
| --- | --- | ---: | --- |
| 1 | Group-io.md | 7 | 2026-10-27 |
| 2 | Group-general.md | 4 | 2026-11-02 |
| 3 | Group-crypto.md | 4 | 2026-10-31 |
| 4 | Group-system_services.md | 7 | 2026-11-05 |
| 5 | Group-mode_management.md | 2 | 2026-11-01 |
| 6 | Group-diagnostics.md | 3 | 2026-11-01 |
| 7 | Group-memory.md | 12 | 2026-11-04 |
| 8 | Group-communication.md | 24 | 2026-10-31 |
| 9 | Group-mcal.md | 3 | 2026-10-26 |
| 10 | Group-globaltime.md | 4 | 2026-10-31 |
| 11 | Group-libraries.md | 9 | 2026-11-04 |
| 12 | Group-safety.md | 3 | 2026-10-27 |
| 13 | Group-security.md | 2 | 2026-11-06 |
| 14 | Group-rte-swarch.md | 2 | 2026-11-06 |
| 15 | Group-communication-2.md | 38 | 2026-11-04 |
| 16 | Group-exp.md | 20 | 2026-10-29 |
| 17 | Group-foundation-exp.md | 19 (+1 open → unfinished) | 2026-11-08 |
| 18 | Group-foundation-rs-prs.md | 32 | 2026-11-08 |

## Rules

- **One document per run**: take one open row, run all 6 steps (including the user confirmation gate), flip the row + its sub-checklist, record the commit hash, then stop (autosar-translate SKILL.md Steps 7/8).
- **A `[x]` row is never reopened** unless the user changes the baseline or a drift review is requested — recreate the row in Group-unfinished.md with `- Note: reopen <reason> <date>` (todo-format.md reopen rule).
- If an already-aligned article carries unfixed gaps, they live in TODO.md's Backlog — Step 1 only verifies them, it does not re-derive scope.
- Program-level fixes outside single-article runs (wording sweeps, hygiene) live in `## Unfinished（未完成）` → `### Backlog` in [`../TODO.md`](../TODO.md).
