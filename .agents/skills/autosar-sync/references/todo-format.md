# Per-run todo file — format and rules

The run's todo list is a **persistent reference document** (SKILL.md Step 4):
written before any editing, ticked in place as items pass verification,
committed with the article, and kept after the run as the audit trail. The
file is the todo; anything posted to chat is a copy of it.

Modelled on py-armodel's `sync-autosar-class` todo file (Rules 0016.6 / 0016.7 /
0018 there), adapted to one article per run.

## Location — one file per run, named by the article

| Run kind | Path |
| --- | --- |
| Repo article sync | `docs/autosar/sync-todo/<module>.md` — excluded from the site build (`exclude_docs` in `mkdocs.yml`) |
| Workspace / eval run | `todo.md` alongside the run's outputs |

**Resume rule:** a file for the article already exists ⇒ read it and take the
first item still `[ ]`. Do not re-run the gap analysis, do not re-ask a decision
already in 决策记录, do not re-flag an omission already in 未纳入.

**Drift/extension:** to redo a finished item (new release, user request), reset
that item to `[ ]` with a `- Note: 重开 <reason> <date>` bullet — never delete
the finished state.

## Template

```markdown
# Sync todo: <module>

文章：`docs/autosar/<section>/<module>/index.md` · 源：`AUTOSAR_CP_SWS_<Name>.md`（R23-11 markdown）·
生成：YYYY-MM-DD · Issue：#N
（恢复 = 第一个仍为 `[ ]` 的条目；全部 `[x]` + TODO.md 行已更新 = 本次同步完成）

## 规则检查（STANDARD.md 展开）
- [x] 七章骨架齐全、编号 1–7 连续
- [x] 无禁止章节（需求追踪 / 时序图 / 配置规范 / 附录）
- [ ] 第 4.2 节标题改为「汽车域的适用性」
  - Note: 现为「对汽车域的适用性」；port/pwm 同样偏差 → 另列 TODO.md 待办

## 内容差距（vs 源文档）
- [ ] 补齐第 7 章 API 规范（17 个函数）
  - Note: 源 §8.3.1–8.3.17；现有 7.1–7.3 不动，自 7.4 起就地插入

## 验证与收尾
- [ ] Phase A 机械检查（strict build 0 WARNING · 标题审计 · 卫生 grep · nav/锚点）
- [ ] Phase B 覆盖映射 + 忠实度抽查（在确认门呈现）
- [ ] 用户确认门（Step 7）
- [ ] 更新 `docs/autosar/TODO.md` 行 + 最后更新
- [ ] 提交 + PR
  - Note: commit <hash> · PR #M

## 决策记录（追加式）
- YYYY-MM-DD 用户：<decision> → <where it was applied>

## 未纳入（有意跳过）
- 源 ch.6 需求追踪 / ch.9 时序图 / ch.10 配置规范 / 附录 A — STANDARD.md 禁止章，合规省略
```

The three work sections mirror the three sources of Step 4: **规则检查**
expands STANDARD.md, **内容差距** comes from the gap analysis, and the
**验证与收尾** block is fixed and always present — it is the Step 6/7 gate
written as checkboxes so a dead session can see how far the finish got.

## Rules

- **One verifiable action per checkbox line**, ordered by risk/effort
  (`补齐第 7 章 API 规范（17 个函数）`, not `完善文章`). Already-satisfied rule
  items are written `[x]` at creation — they are evidence that the check was
  made, not noise.
- **The checkbox line is the action only.** Findings, evidence, counts and
  decisions go on a `- Note:` bullet directly under the item, never on the
  line. A line past ~200 characters is a violation to split before touching the
  row: long, markup-heavy lines make the exact-line toggle fail, and a failed
  toggle then gets "recorded" in an out-of-band note instead of the row (the
  py-armodel Group 4 incident).
- **Tick in the file the moment an item passes verification** — never batch at
  the end, never tick because a later step re-verifies it. An item that turns
  out to be N/A is ticked with the reason (`- [x] … (N/A: 源无回调章)`), not
  deleted.
- **决策记录 is append-only and written when the decision is given**, not
  reconstructed at the end. A decision that changes a canonical term also
  names the STANDARD.md edit it caused.
- **未纳入 lists deliberate omissions** (forbidden chapters, scope cuts,
  source-release fallback) so a resumed session does not re-flag them as gaps.
- **验证与收尾 flips in order**: Phase A → Phase B → confirmation → TODO.md →
  commit/PR, and the last note carries the commit hash and PR link. No item is
  `[x]` before its verification passed; nothing stays `[ ]` after the report.
- **The finished file keeps every item `[x]` with its notes** — never strip,
  collapse or delete it. It is the run's audit trail and the evidence behind
  the article's status row in `docs/autosar/TODO.md`.
- **Never work around a failed row edit** with a side section ("已确认",
  "批量确认"). Fix the row shape (split the long line), then flip the row.
