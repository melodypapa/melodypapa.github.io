# Progress file — docs/autosar/TODO.md

The TODO file is the running work queue of the AUTOSAR translation program.
It lives in the repo at `docs/autosar/TODO.md`, is excluded from the site
build (`exclude_docs` in `mkdocs.yml`), and is maintained by this skill.

## Maintenance rules

1. After **every** sync that touches an article, update that article's row in
   the same PR: new status, refreshed note, and bump `最后更新` at the top.
2. When creating a brand-new article, move its row from the ❌ list into the
   section list with the appropriate status.
3. Never reorder or reformat sections casually — the file is diffed across
   PRs; keep one bullet per spec, stable ordering (alphabetical by spec name
   within a section).
4. If the file has drifted badly (many syncs skipped it), regenerate the
   affected sections from a fresh gap analysis instead of patching blindly.

## Format

```markdown
# AUTOSAR 文章翻译进度

> 由 autosar-translate 技能按 [STANDARD.md](STANDARD.md) 维护；每次同步后更新对应条目与「最后更新」。
> 状态：✅ 符合 Type A · 🔶 已翻译待对齐 · ⚠️ 部分翻译 · ⛔ 空壳 · ❌ 缺失 · 📖 指南/专题（豁免骨架）
> 基准：R23-11 · 最后更新：YYYY-MM-DD

## 概览
(one summary table: counts per status, coverage %)

## <section>            (one section per site dir: communication, io, …)
- ✅ [文章名](相对链接) — SWS_规格名
- 🔶 [文章名](相对链接) — SWS_规格名（一句偏差原因）
- ⚠️ [文章名](相对链接) — SWS_规格名（缺什么）
- ⛔ [文章名](相对链接) — SWS_规格名（空壳）
- ❌ SWS_规格名（缩写）— 无文章
- 📖 [指南文章](相对链接) — EXP_规格名（豁免骨架）
```

## Work todo lists (per-run)

The execution queue is the **persistent batch-queue files** in
`docs/autosar/sync-todo/` (`Group-<section>.md`, one row per document with a
6-step sub-checklist; `index.md` orders batches) — one row consumed per run,
never conversation-only (`todo.md` alongside the outputs for a workspace run).
Format, row template, resume and tick rules: `references/todo-format.md`.
Program-level fixes outside single-article runs (wording sweeps, hygiene)
live in the `## 待办清单` section at the top of `TODO.md` as `- [ ]` items.

Rules for queue rows:

- One verifiable action per step; findings and decisions on `- Note:` bullets
  under the row, appended when they happen.
- A row's inputs: STANDARD.md rule checklist, the article's current row in
  this file, and the fresh gap analysis — plus mid-run user decisions.
- Ticked items in `## 待办清单` get removed (or archived) once the
  corresponding status row has been updated — a work item is done only when
  its status row says so.
- The two files are linked: a status row flips (Step 7) only after the queue
  row's 6 steps are `[x]` and the Step 7 user confirmation was given; the
  flipped queue row (with commit hash + PR link) is the evidence behind the
  status row.

## Status definitions

| Status | Meaning |
| --- | --- |
| ✅ 符合 Type A | Seven chapters present, canonical wording, no forbidden chapters |
| 🔶 已翻译待对齐 | Complete seven chapters but with legacy wording, extra site-specific chapters, or forbidden-chapter residue |
| ⚠️ 部分翻译 | Skeleton incomplete — missing ≥1 chapter (often just API规范) |
| ⛔ 空壳 | ≤ ~19 lines, effectively empty |
| ❌ 缺失 | No article for the spec |
| 📖 指南/专题 | EXP guides, TPS templates, bespoke topic articles — exempt from the Type A skeleton (STANDARD.md §7) |

## Status transitions

- ⛔/⚠️ → ✅: after a sync completes the missing chapters AND aligns wording.
- 🔶 → ✅: after a wording/forbidden-chapter alignment pass.
- ❌ → ⚠️/✅: after a first translation (⚠️ if delivered partial by agreement).
- Never mark ✅ without running the strict build and comparing chapter headings
  against STANDARD.md §1/§2.
