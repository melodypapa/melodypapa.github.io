# Todo files — batch queue format and rules

The translation program's todo is a set of **persistent batch-queue files**
(SKILL.md Step 4), modelled on py-armodel `sync-autosar-class`'s Group files
(Rules 0016.6/0016.7/0018 there), adapted to one article per run.

- **Status ledger** = `docs/autosar/TODO.md` — what each article currently IS
  (✅/🔶/⚠️/⛔/❌/📖) and site-wide counts.
- **Execution queue** = `docs/autosar/sync-todo/` — what to do next: one
  `Group-<section>.md` per batch, one row per document; `index.md` holds the
  recommended batch order.

Both live in the repo, excluded from the site build (`exclude_docs`), updated
in the same PR as the article.

## Files

```
docs/autosar/sync-todo/
  index.md            # 批次顺序 + 计数 + 恢复规则
  Group-io.md         # 每分区/主题一个批次文件
  Group-general.md
  ...
  Group-exp.md
```

**Resume rule:** pick the batch (user names it, or the first unfinished batch
in index order) → read the file → take the **first row still `[ ]`** → run the
6 steps. Do not re-derive scope from TODO.md or the source tree; do not re-ask
decisions already in the row's Notes.

## Row format

```markdown
- [ ] <article-dir-or-slug>（SWS_<Name> · R23-11 markdown · <状态/缺口>）
  - Note: <known gaps — from TODO.md row + prior audits; run findings appended>
  - [ ] Step 1 — 源定位 + 差距分析
  - [ ] Step 2 — 就地翻译/补齐
  - [ ] Step 3 — Phase A 机械检查
  - [ ] Step 4 — Phase B 覆盖映射 + 忠实度
  - [ ] Step 5 — 用户确认门
  - [ ] Step 6 — TODO.md 行 + 提交/PR
```

- The parenthetical carries the short fixed fields only: 规范名 · 源 · 状态
  标签（✅ 仅余对齐 / ⚠️ 补齐 / ⛔ 空壳全译 / ❌ 新文章 / 📖 豁免骨架）。
- **Findings, counts and decisions go on `- Note:` bullets under the row**,
  never on the checkbox line — long markup-heavy lines break the exact-line
  toggle (the py-armodel Group 4 incident). A line past ~200 characters is a
  violation to split before touching the row.
- One verifiable action per step; **tick in the file the moment a step
  passes** — never batch at the end. A legitimately N/A step is ticked with
  the reason (`- [x] Step 4 — … (N/A: 纯对齐无新增内容)`), not deleted.
- Step 6's note records the commit hash and PR link. The row flips `[ ]` →
  `[x]` only then — **no `[x]` before the commit exists** (py-armodel Rule
  0017.2).
- **重开**: to redo a finished row (new release, drift, user request), reset
  it to `[ ]` with `- Note: 重开 <原因> <日期>` — never delete the finished
  state.
- **Not queued** section per file records deliberate exclusions (豁免 📖/📄
  articles, 专题/历史快照) so a resumed session never re-flags them.
- **Never work around a failed row edit** with a side section ("已确认",
  "批量确认") elsewhere in the file — fix the row shape (split the long
  line), then flip the row in place.

## Historical format

`dio_driver.md` in this directory is a completed run in the earlier
per-article format (superseded by batch rows); kept as an audit trail and
format example.
