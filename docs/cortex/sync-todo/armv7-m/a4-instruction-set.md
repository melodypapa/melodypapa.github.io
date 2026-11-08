# Sync todo: Group ARMv7-M — A4 The Armv7-M Instruction Set

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part A ch A4 · parse L6099–7082 (983)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] instruction_set — completed (A4 only; article `m7_processor/instruction_set/index.md`, 878 ln, 1 img vs A4 The Armv7-M Instruction Set, 983 ln)
  - S1 result: scope fixed to A4 by decision — A4 is one page. A5 and A6 are separate articles and are now their own queue rows below. The page keeps its TRM-derived 200-row instruction summary as `## 1.`, and the A4 translation is appended as `## 2.` (no restructuring of the existing summary).
  - S2 result: `## 2.` added — chapter intro list of 13 sections; §2.1 关于指令集 (2.1.1 互工作支持, 2.1.2 条件执行), §2.2 统一汇编语言 (2.2.1 条件指令, 2.2.2 在 UAL 指令语法中使用标签), §2.3 分支指令, §2.4 数据处理指令 (2.4.1–2.4.8), §2.5 状态寄存器访问指令, §2.6 加载和存储指令 (2.6.1–2.6.5), §2.7 加载多个和存储多个指令 (2.7.1), §2.8 杂项指令, §2.9 产生异常的指令, §2.10 协处理器指令, §2.11 浮点加载和存储指令, §2.12 浮点寄存器传送指令, §2.13 浮点数据处理指令.
  - S3 result: A4 has no figures — every instruction encoding lives in chapters A5/A6 as numbered tables, so no crops were needed.
  - S6 result: all 22 A4 tables (A4-1 … A4-22) rendered as GFM, footnotes kept as `a.` / `b.` lines; cross-references phrased as `MLA（第 A7-289 页）`.
  - S8 result: merged as `2d7e17f` (PR #324).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
