# Sync todo: Group ARMv7-M — A3 The Memory Model

> Source: DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅) · Part A ch A3 · parse L4060–6099 (2,039)
> Steps: S1 source · S2 translate · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR — defined in the [group index](index.md).

## Queue row

- [x] arm_architecture_memory_mode — completed (article `m7_processor/arm_architecture_memory_mode/index.md`, 1,194 ln, 7 imgs vs A3 The Memory Model, 2,039 ln)
  - S1 result: the page already mirrored A3 at h2 level (`## 1.` = A3 intro, `### 1.1`–`### 1.8` = A3.1–A3.8 with the 1.x.y subsections), so the gaps were missing subsections rather than a restructuring: A3.2.1 对齐行为 absent, A3.4.1–A3.4.6 absent, A3.5.7 truncated after rule 2, and A3.6/A3.7/A3.8 present only as condensed paraphrase.
  - S2 result: §1.2.1 added (faulting/non-faulting access lists, IMPLEMENTATION DEFINED note, alignment pseudocode, PC-update rules); §1.4.1–1.4.6 added (local monitor, global monitor, Tables A3-2/A3-3, 标记与标记内存块的大小, 上下文切换支持, 使用限制, 同步原语与内存顺序模型); §1.5.7 extended with rules 3–6, the software-coherency sub-rules and the race-condition note; §1.6 rewritten to A3.6.1/A3.6.2 (data/instruction privilege access control); §1.7 rewritten (reads and writes, observability/completion, address & control dependency, Figure A3-8, the six barriers CSDB/DMB/DSB/ISB/PSSBB/SSBB, SCS synchronization); §1.8.2/1.8.3 completed (Figure A3-9, hierarchy note, data/instruction coherency).
  - S3 result: `FigureA3-6.png` (p71 local monitor state machine), `FigureA3-7.png` (p74 global monitor state machine), `FigureA3-9.png` (p97 memory hierarchy). Figure A3-8 is a plain row/column ordering matrix, so it was rendered as GFM instead of a crop.
  - S6 result: Tables A3-2 and A3-3 (monitor state transitions) and the A3-8 matrix are GFM; the existing A3-1/A3-4 tables were already GFM.
  - S8 result: merged as `fe022df` (PR #322).
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
