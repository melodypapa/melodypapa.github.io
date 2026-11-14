# Sync todo: Group ARMv7-M — DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines): Part A L739 — A1 Introduction L743–880 (137) · A2 The Application Level Model L880–4060 (3,180, ⏸) · A3 The Memory Model L4060–6099 (2,039, ⏸) · A4 The Armv7-M Instruction Set L6099–7082 (983) · A5 The Thumb Instruction Set Encoding L7082–8272 (1,190) · A6 The Floating-point Instruction Set Encoding L8272–8634 (362) · A7 Instruction Details L8634–28616 (19,982, ⏸ deferred). Part B L28620 — B1 System Level Programmers' Model L28620–32964 (4,344, ⏸; B1.5 = Armv7-M exception model) · B2 System Memory Model L32964–34504 (1,540) · B3 System Address Map L34504–38282 (3,778, ⏸; B3.5 = PMSAv7) · B4 The CPUID Scheme L38282–39914 (1,632) · B5 System Instruction Details L39914–40432 (518). Part C Debug Architecture — C1 Armv7-M Debug L40436–46188 (5,752, ⏸ deferred). Part D Appendixes — D1 CoreSight Infrastructure IDs … D8 Register Index, L46192–end (deferred).

Existing-article mappings (mapping.md, evidence re-checked at census): `arm_architecture_memory_mode` ← A3 · `programmers_model` ← B1.5 (evidence `Figure2-*` unverified — confirm at S1) · `mpu` ← B3.5 (`TableB3-1…11`) · `system_address_map` ← B3.1–B3.4 (article sections SCS/SysTick/NVIC = B3.2/B3.3/B3.4) · `instruction_set` ← A4 (completed 2026-11-08; extracted 2026-11-15 to `armv7-m/part-a/instruction_set/index.md`, the TRM page keeps only its implementation summary); A5 and A6 are separate articles, queued below.

## Layout migration (2026-11-13, issue #389 / PR #390)

The source document is organised into Parts containing Chapters, so every
chapter article (glossary included) now lives in its Part subfolder `part-<designator>/<topic>/index.md`, with the Part index page at `part-<designator>/index.md`. This is the arm-translate rule from uncertainty#119 / #120. Old flat URLs are kept alive by `redirect_maps` entries in `mkdocs.yml`.

| Old article path | New article path |
| --- | --- |
| `armv7-m/arm_architecture_memory_mode/index.md` | `armv7-m/part-a/arm_architecture_memory_mode/index.md` |
| `armv7-m/fp_instruction_set_encoding/index.md` | `armv7-m/part-a/fp_instruction_set_encoding/index.md` |
| `armv7-m/thumb_instruction_set_encoding/index.md` | `armv7-m/part-a/thumb_instruction_set_encoding/index.md` |
| `armv7-m/cpuid_scheme/index.md` | `armv7-m/part-b/cpuid_scheme/index.md` |
| `armv7-m/system_address_map/index.md` | `armv7-m/part-b/system_address_map/index.md` |
| `armv7-m/system_instructions/index.md` | `armv7-m/part-b/system_instructions/index.md` |
| `armv7-m/system_memory_model/index.md` | `armv7-m/part-b/system_memory_model/index.md` |
| `armv7-m/glossary/index.md` | `armv7-m/part-d/glossary/index.md` |

## Queue

- [x] exception_model — completed (article `m7-trm/programmers_model/index.md`, 1,834 ln, 5 imgs vs B1.5 of the 4,344-ln chapter B1)
  - S1 result: mapping confirmed at the figure/table evidence — `Figure2-1`/`Figure2-2`/`Table 2-14` are TRM ch2 derivatives, and the exception-model prose aligns with B1.5.1–B1.5.19, so the page was completed in place against B1.5.
  - S2 result: §6–§8 kept (TRM ch2 front matter, aligned to B1.5.1 and completed: DebugMonitor inserted, disable/escalation notes, ICSR control bits, 496 external interrupts), §9 异常编号定义 (Table B1-4) added, §10 向量表 completed (Table B1-5), §11 异常优先级与抢占 (Table B1-6), §12 中断优先级分组 (Table B1-7), §13 执行优先级与优先级提升 (Example B1-1, ExecutionPriority pseudocode, priority escalation, SVCall/PendSV model), §14 复位行为 (TakeReset), §15 异常进入和返回 (ExceptionEntry/PushStack/ExceptionTaken/ReturnAddress/UpdateFPCCR, stack alignment, EXC_RETURN Tables B1-8/B1-9, ExceptionReturn/DeActivate/PopStack), §16–§26 = B1.5.9–B1.5.19, §27 参考文献.
  - S3 result: `FigureB1-3.png` (p536) and `FigureB1-4.png` (p538) cropped; all six numbered tables (B1-4…B1-9) and the three unnumbered fault tables rendered as GFM.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 (gaps only) [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] protected_memory_system_archi_pmsav7 — verified (article `m7-trm/mpu/index.md`, 611 ln, 5 bit-field images vs B3.5)
  - S1 result: structure matches B3.5 exactly — `## 4.` ← B3.5 intro, `## 5.` ← B3.5.1, `## 6.` ← B3.5.2, `## 7.` ← B3.5.3 (7.1 sub-region / 7.2 Armv7-M specific / 7.3 MPU pseudocode / 7.4 MPU fault support), `## 8.` ← B3.5.4, `## 9.` ← B3.5.5 MPU_TYPE, `## 10.` ← B3.5.6 MPU_CTRL (10.3 = TRM-derived non-privileged instruction impact), `## 11.` ← B3.5.7 MPU_RNR, `## 12.` ← B3.5.8 MPU_RBAR, `## 13.` ← B3.5.9 MPU_RASR (13.3 sub-regions / 13.4 attributes / 13.5 XN), `## 14.` ← B3.5.10 alias support.
  - S6 result: Tables B3-11…B3-16 all present as GFM; the 5 images are bit-field bars, which stay images. Three defects fixed: stray `**` on the `XN：MPU_RASR[28]` bullet (broken bold run), garbled Table B3-12 lead sentence, garbled Region 0–15 alias sentence.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 (N/A: verify-only, no gaps) [x] S3 (N/A: bit-bar images already present) [x] S4 (N/A: page already registered) [x] S5 (N/A: no text changed) [x] S6 [x] S7 [x] S8
- [x] system_address_map — completed (article `armv7-m/part-b/system_address_map/index.md`, 2,392 ln, 33 bit-bar imgs vs B3.1–B3.4)
  - S1 result (split decision): **no split against the sibling pages.** `nested_vectored_interrupt_controller` and `system_control` are TRM implementation pages whose own prose defers the architectural register definitions to the ARM, so B3.2 (2.2–2.26 SCB/ID registers), B3.3 (SysTick) and B3.4 (NVIC) were translated in full here. Page tree = B3.1 (## 1) → B3.2 (## 2) → B3.3 (## 3) → B3.4 (## 4); only cross-link added is the PMSAv7 pointer to `mpu/`.
  - S2 result: §2.2–§2.26 added (Tables B3-4/B3-5/B3-6; CPUID, ICSR, VTOR, AIRCR, SCR, CCR, SHPR1–3, SHCSR, CFSR + MMFSR/BFSR/UFSR, HFSR, MMFAR, BFAR, AFSR, CPACR + FP enable, FPCCR, FPCAR, FPDSCR, ICTR, ACTLR, STIR); §3 added (SysTick operation, Table B3-7, SYST_CSR/RVR/CVR/CALIB); §4 added (NVIC operation + external-interrupt-input pseudocode, implemented interrupts, Tables B3-8/B3-9/B3-10, NVIC_ISER/ICER/ISPR/ICPR/IABR/IPR). Stale §2 overview bullet list replaced with pointers to the new subsections.
  - S3 result: 33 bit bars cropped from the ARM PDF (the chapter has no raster figures; the bars are vector) named by register, `CPUID.png` … `NVIC_IPR.png`; no other figures in B3.1–B3.4.
  - S6 result: every numbered table (B3-4 … B3-10) rendered as GFM.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] arm_architecture_memory_mode — completed (article `armv7-m/part-a/arm_architecture_memory_mode/index.md`, 1,194 ln, 7 imgs vs A3 The Memory Model, 2,039 ln)
  - S1 result: the page already mirrored A3 at h2 level (`## 1.` = A3 intro, `### 1.1`–`### 1.8` = A3.1–A3.8 with the 1.x.y subsections), so the gaps were missing subsections rather than a restructuring: A3.2.1 对齐行为 absent, A3.4.1–A3.4.6 absent, A3.5.7 truncated after rule 2, and A3.6/A3.7/A3.8 present only as condensed paraphrase.
  - S2 result: §1.2.1 added (faulting/non-faulting access lists, IMPLEMENTATION DEFINED note, alignment pseudocode, PC-update rules); §1.4.1–1.4.6 added (local monitor, global monitor, Tables A3-2/A3-3, 标记与标记内存块的大小, 上下文切换支持, 使用限制, 同步原语与内存顺序模型); §1.5.7 extended with rules 3–6, the software-coherency sub-rules and the race-condition note; §1.6 rewritten to A3.6.1/A3.6.2 (data/instruction privilege access control); §1.7 rewritten (reads and writes, observability/completion, address & control dependency, Figure A3-8, the six barriers CSDB/DMB/DSB/ISB/PSSBB/SSBB, SCS synchronization); §1.8.2/1.8.3 completed (Figure A3-9, hierarchy note, data/instruction coherency).
  - S3 result: `FigureA3-6.png` (p71 local monitor state machine), `FigureA3-7.png` (p74 global monitor state machine), `FigureA3-9.png` (p97 memory hierarchy). Figure A3-8 is a plain row/column ordering matrix, so it was rendered as GFM instead of a crop.
  - S6 result: Tables A3-2 and A3-3 (monitor state transitions) and the A3-8 matrix are GFM; the existing A3-1/A3-4 tables were already GFM.
  - S8 result: merged as `fe022df` (PR #322).
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] instruction_set — completed (A4 only; article `m7-trm/instruction_set/index.md`, 878 ln, 1 img vs A4 The Armv7-M Instruction Set, 983 ln)
  - S1 result: scope fixed to A4 by decision — A4 is one page. A5 and A6 are separate articles and are now their own queue rows below. The page keeps its TRM-derived 200-row instruction summary as `## 1.`, and the A4 translation is appended as `## 2.` (no restructuring of the existing summary).
  - S2 result: `## 2.` added — chapter intro list of 13 sections; §2.1 关于指令集 (2.1.1 互工作支持, 2.1.2 条件执行), §2.2 统一汇编语言 (2.2.1 条件指令, 2.2.2 在 UAL 指令语法中使用标签), §2.3 分支指令, §2.4 数据处理指令 (2.4.1–2.4.8), §2.5 状态寄存器访问指令, §2.6 加载和存储指令 (2.6.1–2.6.5), §2.7 加载多个和存储多个指令 (2.7.1), §2.8 杂项指令, §2.9 产生异常的指令, §2.10 协处理器指令, §2.11 浮点加载和存储指令, §2.12 浮点寄存器传送指令, §2.13 浮点数据处理指令.
  - S3 result: A4 has no figures — every instruction encoding lives in chapters A5/A6 as numbered tables, so no crops were needed.
  - S6 result: all 22 A4 tables (A4-1 … A4-22) rendered as GFM, footnotes kept as `a.` / `b.` lines; cross-references phrased as `MLA（第 A7-289 页）`.
  - S8 result: merged as `2d7e17f` (PR #324).
  - 2026-11-15 extraction: A4 moved out of the TRM page into a standalone Part A article `armv7-m/part-a/instruction_set/index.md` with front matter, the chapter intro as page intro, and A4.1–A4.13 renumbered to `## 1.`–`## 13.` (subsections `1.1`–`4.8`, `6.1`–`6.5`, `7.1`). Fidelity re-checked section by section against PDF pp. 102–124 (13 sections, 22 tables, all rows and page references). The TRM page keeps its 200-row summary as `## 1.` plus a pointer link. Nav entry inserted before 指令集编码; `part-a/index.md` and `armv7-m/index.md` lists renumbered.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] A5 → new article (The Thumb Instruction Set Encoding, 916 ln; e.g. `armv7-m/part-a/thumb_instruction_set_encoding/`)
  - Note: encoding tables are textual — GFM by default; raw HTML only when the structure qualifies (see .agents/skills/arm-translate/references/article-format.md §Tables). A7 instruction-by-instruction details are NOT in this row (deferred tail).
  - S1 result: A5 = PDF pp. 125–158; structure fixed to 3 chapters — §1 Thumb 指令集编码 (1.1 UNDEFINED/UNPREDICTABLE 空间, 1.2 0b1111 寄存器说明符, 1.3 0b1101/SP 支持 1.3.1–1.3.3), §2 16 位编码 (2.1–2.6, 2.5.1 If-Then 与提示), §3 32 位编码 (3.1–3.18, 3.4.1 提示, 3.4.2 杂项控制, 3.11.1 移动寄存器和立即数移位).
  - S2 result: article `armv7-m/part-a/thumb_instruction_set_encoding/index.md` written in place; numbering restarts at 1; source typos preserved.
  - S3 result: 30 encoding-bar crops at 3× (`EncodingA5-2.png`, `EncodingA5-2-1`…`EncodingA5-2-6`, `EncodingA5-2-5-1`, `EncodingA5-3.png`, `EncodingA5-3-1`…`EncodingA5-3-18`, `EncodingA5-3-4-1`, `EncodingA5-3-4-2`, `EncodingA5-3-11-1`); p143/p150/p152/p156 each yield two bars.
  - S4 result: nav entry added after the instruction-set page; landing item inserted as Cortex-M7 no. 5 with 5–18 renumbered to 6–19.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py` OK (324 nav targets, 0 broken links); `check_heading_lang.py` OK.
  - S6 result: all 30 tables (A5-1 … A5-30) rendered as GFM with merged cells expanded by repeating the spanning value; footnotes as `a.` / `b.` lines; cross-references phrased as `MOV（立即数）（第 A7-291 页）`.
  - S8 result: merged as `de13acc` (PR #327).
  - Verify result (2026-11-15): re-checked against PDF pp. 125–158 section by section — 3 chapters, 27 subsections (1.1–1.3.3, 2.1–2.6 + 2.5.1, 3.1–3.18 + 3.4.1/3.4.2/3.11.1) and tables A5-1 … A5-30 all match the source row for row. Fixed: p126 Note re-rendered as `**注意：**`; the two "deprecated" sentences reworded to the series form `**Arm** 不推荐使用`; Table A5-11 rows `01001`–`01011` restored to 8-bit groups.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] A6 → new article (The Floating-point Instruction Set Encoding, 362 ln; `armv7-m/part-a/fp_instruction_set_encoding/`)
  - S1 result: A6 = PDF pp. 160–170; structure fixed to 7 chapters — §1 概述, §2 浮点指令语法 (2.1 数据类型说明符, 2.2 寄存器说明符, 2.3 寄存器列表), §3 寄存器编码, §4 浮点数据处理指令 (4.1 修改立即数常量的运算), §5 扩展寄存器加载或存储指令, §6 32 位传送, §7 64 位传送. Census: 9 tables (A6-1 … A6-9) + 5 unnumbered encoding bars.
  - S2 result: article written in place; numbering restarts at 1; source typo `{<Dd[x]>,<Dd+2[x]}` preserved; table A6-5 rebuilt from the PDF cell grid (merged opc/instruction cells expanded per block).
  - S3 result: 5 encoding bars cropped at 3× — `EncodingA6-4.png` (p164 register encoding), `EncodingA6-5.png` (p165 data-processing), `EncodingA6-7.png` (p167 load/store), `EncodingA6-8.png` (p168 32-bit transfer), `EncodingA6-9.png` (p169 64-bit transfer).
  - S4 result: nav entry added after `thumb_instruction_set_encoding`; landing item inserted as Cortex-M7 no. 6 with 6–19 renumbered to 7–20.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (0 broken links); `check_heading_lang.py` OK.
  - S6 result: all 9 tables (A6-1 … A6-9) rendered as GFM; Table A6-5 expanded to 22 rows from the merged-cell grid; footnotes as `a.` lines; cross-references phrased as `VSEL（第 A7-497 页）`.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B2 → new article (System Memory Model — caches, branch predictors, memory-system pseudocode, 1,540 ln; `armv7-m/part-b/system_memory_model/`)
  - S1 result: B2 = PDF pp. 570–590; structure fixed to 3 chapters — §1 关于系统内存模型, §2 缓存与分支预测器 (2.1–2.9, with 2.3/2.5/2.6/2.7 unnumbered source headings kept as bold sub-headings), §3 通用内存系统操作的伪代码细节 (3.1–3.11). Census: 1 table (B2-1) + 1 set/way format bar (unnumbered) + Example B2-1.
  - S2 result: article written in place; §3 keeps every pseudocode block verbatim in `arm` fences; terminology fixed as 一致性点 PoC / 统一化点 PoU / 按 MVA / 按 set/way.
  - S3 result: 1 bar cropped at 3× — `EncodingB2-1.png` (p580 set/way register format); Example B2-1 is an assembly listing, not a figure.
  - S4 result: nav entry added before `system_address_map` (source chapter B2 precedes B3); landing item inserted as Cortex-M7 no. 10 with 10–20 renumbered to 11–21.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK; `check_heading_lang.py` OK.
  - S6 result: Table B2-1 rendered as GFM (13 address rows incl. the three reserved entries), footnote `a.` kept; set/way fields A/B/L/S derived lines kept as in source.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B4 → new article (The CPUID Scheme, 1,632 ln; `armv7-m/part-b/cpuid_scheme/`)
  - S1 result: B4 = PDF pp. 644–668; structure fixed to 8 chapters — §1 关于 CPUID 方案 (1.1 约定, 1.2 汇总), §2 处理器特性 ID (2.1–2.2), §3 调试特性 ID (3.1), §4 辅助特性 ID (4.1), §5 内存模型特性 (5.1–5.4), §6 指令集属性 (6.1 描述约定 + 6.2–6.6, 含 同步原语支持), §7 浮点特性标识 (7.1–7.4), §8 缓存控制标识 (8.1–8.4). Census: 4 tables (B4-1 … B4-4) + 19 register bit bars.
  - S2 result: article written in place; register subsections follow the M7 house pattern (**用途** / **使用限制** / **配置** / **属性** + bar + 位/名称/值/功能 table); §1.2 Table B4-1 covers 19 register rows.
  - S3 result: 19 bars cropped at 3× — `FigureB4-1.png` … `FigureB4-19.png` (PFR0, PFR1, DFR0, AFR0, MMFR0–2, ISAR0–4, MVFR0–2, CLIDR, CCSIDR, CSSELR, CTR); ID_MMFR3 has no bar in the source and is rendered as a table only.
  - S4 result: nav entry added after `mpu` (source chapter B4 follows B3.5); landing item inserted as Cortex-M7 no. 13 with 13–21 renumbered to 14–22.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (331 nav targets); `check_heading_lang.py` OK.
  - S6 result: Tables B4-1 … B4-4 rendered as GFM; every register field table uses the four-column `位 / 名称 / 值 / 功能` grid with one row per field value.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B5 → new article (System Instruction Details, 518 ln; `armv7-m/part-b/system_instructions/`)
  - S1 result: B5 = PDF pp. 670–678; structure fixed to 2 chapters — §1 关于 Armv7-M 系统指令 (1.1 特殊寄存器编码), §2 系统指令描述 (2.1 CPS, 2.2 MRS, 2.3 MSR). Census: 2 tables (B5-1, B5-2) + 3 encoding bars (T1 for CPS/MRS/MSR) + assembler-syntax and operation pseudocode.
  - S2 result: article written in place; each instruction keeps the source order 汇编器语法 → 操作 → 异常 → 备注 → 编码 T1; pseudocode and assembler syntax verbatim in `arm` fences.
  - S3 result: 3 bars cropped at 3× — `EncodingB5-1.png` (CPS), `EncodingB5-2.png` (MRS), `EncodingB5-3.png` (MSR).
  - S4 result: nav entry added after `cpuid_scheme` (source chapter B5 follows B4); landing item inserted as Cortex-M7 no. 14 with 14–22 renumbered to 15–23.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (332 nav targets); `check_heading_lang.py` OK.
  - S6 result: Tables B5-1 and B5-2 rendered as GFM; the two-bullet Note under §2 kept as a `**注意：**` block.
  - S7 result: confirmed by the user; shipped as PR #334 (issue #333).
  - S8 result: merged as `6c283e6` (PR #334).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8

## Not queued (deliberately deferred)

- A7 Instruction Details (19,982 ln), C1 Armv7-M Debug (5,752 ln — overlaps the M7 TRM debug chapters; prefer the TRM for implementation), D1–D8 appendixes (pseudocode/register indexes) — start on explicit request only.

## Part A / Part B completion batch (2026-11-14)

Source is the PDF text layer only: `reference-docs/arm/cortex-m7/DDI0403E_e_armv7m_arm.pdf`
(858 pp) — the ima-parsed `.md` listed in the span map is no longer on disk.

- [x] **A1 Introduction** — article `armv7-m/part-a/introduction/index.md` (A1.1–A1.3, Table A1-1, 0 figures); nav + both landing pages updated.
- [x] **B1 System Level Programmers' Model (remaining sections)** — completed in place on `m7-trm/programmers_model/index.md`, the merged chapter page. New §2 系统级简介 (B1.1), §3 关于 Armv7-M 内存映射架构 (B1.2), §4 系统级术语与操作概述 (B1.3, §4.1–§4.4: 模式/特权/栈 Table B1-1, 异常类别与状态, 执行状态, 调试状态), §5 寄存器 (B1.4, §5.1–§5.7: 核心寄存器, xPSR with Figure B1-1 + Tables B1-2/B1-3, 掩码寄存器 with Figure B1-2, CONTROL, 保留位, 内存顺序模型, 伪代码定义 with LookUpSP), §30 浮点支持 (B1.6, Table B1-10, ExecuteFPCheck/CheckVFPEnabled/PreserveFPState/TakePreserveFPException). The old condensed TRM §2 操作模式与执行状态 was dropped (subsumed by B1.3); §3–§27 renumbered to §6–§31. Figures `FigureB1-1.png` (p517) and `FigureB1-2.png` (p519) cropped at 4×.
- [x] **A2 The Application Level Programmers' Model** — article `armv7-m/part-a/application_level_model/index.md` (§1 关于应用程序级程序员模型 + 1.1; §2 数据类型与运算 incl. LSL/LSR/ASR/ROR/RRX, AddWithCarry, SignedSatQ/UnsignedSatQ/SatQ; §3 寄存器与执行状态 + 3.1–3.4 with APSR; §4 异常、故障与中断 + 4.1; §5 可选的浮点扩展 with 5.1–5.4 and 5.4.1–5.4.21 covering the full FP pseudocode set; §6 协处理器支持). 6 figures cropped at 4×: `FigureA2-1.png` (p35, FP 寄存器双视图), `FigureA2-2.png` (p31, APSR), `FigureA2-3.png` (p37, FPSCR), `FigureA2-4.png` (p39, 单精度), `FigureA2-5.png` (p40, 双精度), `FigureA2-6.png` (p42, 半精度); Tables A2-1…A2-4 as GFM.
- [x] **A7 Instruction Details** — article `cortex/armv7-m/part-a/instruction_details/index.md`, **completed** (single-page decision: the whole chapter as one article; encoding bit grids rendered as GFM bit tables instead of image crops, per requester). Done: §1–§6 (A7.1 指令描述格式, A7.2 标准汇编语法字段, A7.3 条件执行 + Table A7-1/A7-2, A7.4 施加于寄存器的移位, A7.5 存储器访问, A7.6 提示指令) and all 263 entries 7.1–7.263 (A–Y 段，ADC … YIELD), with encoding-specific pseudocode, T1/T2… bit tables, assembler syntax, `where：` fields, operation pseudocode and exception lines per entry.
