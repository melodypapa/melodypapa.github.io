# Sync todo: Group ARMv7-M — DDI0403E Armv7-M ARM E.e (`reference-docs/arm/cortex-m7/DDI0403E_e_armv7m_arm.md`, 36,478 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Last refresh: 2026-11-18 — the `.md` was re-parsed (51,102 → 36,478 ln; every section is now a real `## A3.x` / `## B1.x` / `## C1.x` h2), so the span map below was recomputed and the Part C/D tail was turned into executable queue rows.
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (re-parsed 2026-11-18, 36,478 ln; spans are exact because every section carries a numbered heading): Part A L471 — A1 Introduction L473–560 (88) · A2 The Application Level Programmers' Model L561–1707 (1,147) · A3 The Memory Model L1708–3023 (1,316) · A4 The Armv7-M Instruction Set L3024–3765 (742) · A5 The Thumb Instruction Set Encoding L3766–4760 (995) · A6 The Floating-point Instruction Set Encoding L4761–5058 (298) · A7 Instruction Details L5059–21470 (16,412). Part B L21471 — B1 System Level Programmers' Model L21475–23805 (2,331; B1.5 = Armv7-M exception model) · B2 System Memory Model L23806–24501 (696) · B3 System Address Map L24502–27448 (2,947; B3.5 = PMSAv7) · B4 The CPUID Scheme L27449–28948 (1,500) · B5 System Instruction Details L28949–29237 (289). Part C L29238 — C1 Armv7-M Debug L29240–33316 (4,077). Part D L33317 — D1 Armv7-M CoreSight Infrastructure IDs L33321–33390 (70) · D2 Legacy Instruction Mnemonics L33391–33574 (184) · D3 Deprecated Features in Armv7-M L33575–33626 (52) · D4 Debug ITM and DWT Packet Protocol L33627–34402 (776) · D5 Armv7-R Differences L34403–34491 (89) · D6 Pseudocode Definition L34492–35328 (837) · D7 Pseudocode Index L35329–35648 (320) · D8 Register Index L35649–35833 (185) · Glossary L35834–36054 (221); the trailing alphabetical Index L36055–36478 is chrome and never translates.

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
- [ ] ⏸ C1 → new article `armv7-m/part-c/debug/` (Armv7-M Debug; parse L29240–33316, 4,077 ln; PDF pp. 682–765; Step 3.5 stub exists — fill it in place)
  - Note: 11 sections C1.1–C1.11 with 49 numbered subsections. Census: 1 figure (`Figure C1-1` ITM/component relationship, parse L30815) and 23 numbered tables (`Table C1-1` … `Table C1-23`). Content: DAP rules + ROM table, debug authentication (halting/non-invasive, DAP permission tables C1-4…C1-7), debug/reset, debug events + stepping + vector catch + prioritisation (C1-8/C1-9), debug system registers DFSR/DHCSR/DCRSR/DCRDR/DEMCR (C1-10), ITM (C1.7, 6 register sections C1-11/C1-12), DWT (C1.8, 17 register sections C1-21), ETM support (C1.9), TPIU (C1.10, C1-22), FPB (C1.11, C1-23). >1500-line rule: present the run plan before S2.
  - Overlap rule: the ITM/DWT/TPIU/FPB register descriptions restate the M7 TRM ch9 (Debug, incl. FPB), ch10 (TPIU), ch12 (ITM) and ch13 (DWT) pages; translate this chapter as the architectural reference and cross-link the TRM implementation pages — never copy sections between them.
  - S1 result: source resolved to the re-parsed `.md` (L29240–33316, 4,077 ln) with the PDF (pp. 682–765) as fallback; census confirmed 11 sections C1.1–C1.11 with 49 numbered subsections, 23 tables (C1-1 … C1-23) and 1 figure (C1-1). Gap analysis: the Step 3.5 stub held only front matter → full translation in place, no split (the TRM ch9/ch10/ch12/ch13 pages are cross-linked, never copied).
  - S2 result: article written in place (3,888 ln) — §1 引言 (1.1 PPB 调试区域 + C1-1/C1-2, 1.2 推荐的调试级别) · §2 调试访问端口 (2.1 一般规则, 2.2 ROM 表 C1-3) · §3 调试特性 (3.1 调试认证 C1-4…C1-7 + 3.1.1/3.1.2, 3.2 调试功能 3.2.1 SCS / 3.2.2 DWT / 3.2.3 ITM / 3.2.4 ETM, 3.3 多处理器支持 3.3.1–3.3.3) · §4 调试与复位 · §5 调试事件行为 (C1-8; 5.1 单步 C1-9 + 5.1.1/5.1.2, 5.2 向量捕获, 5.3 优先级, 5.4 退出) · §6 调试系统寄存器 (C1-10; 6.1–6.5, 6.3.1, 6.4.1) · §7 ITM (C1-11; 7.1.1–7.1.8, 7.2 汇总, 7.3–7.6 + 7.6.1) · §8 DWT (8.1 比较器 8.1.1–8.1.13, 8.2, 8.3 + 8.3.1/8.3.2, 8.4 + 8.4.1, 8.5, 8.6 汇总 C1-21, 8.7–8.17) · §9 ETM · §10 TPIU (C1-22; 10.1–10.6) · §11 FPB (11.1–11.5, C1-23). Pseudocode (InstructionAddressMatch / DataAddressMatch / CycCountMatch / DataValueMatch) kept verbatim in `arm` fences.
  - S3 result: `FigureC1-1.png` cropped from PDF p. 713 at 300 dpi (4 % margin); the chapter's register bit bars are vector-only and carry no raster image, so they stay text + GFM.
  - S4 result: N/A — `armv7-m/part-c/debug/` was already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: all 23 tables rendered as GFM — multi-level headers flattened, merged cells expanded per row (C1-3/C1-4/C1-5/C1-18), multi-item cells joined with `<br>•` (C1-2); no HTML table needed.
  - PDF fallback: Table C1-4/C1-5 lost cells, Table C1-14/C1-16 lost footnotes, the DCRSR REGSEL list was scrambled, and DEMCR / DFSR / DHCSR / DWT_CTRL / DWT_FUNCTIONn bit order was displaced; the POSTCNT ICNT formula came through as `formula-not-decoded` — all re-read from PDF pp. 689–690, 700, 707, 722, 726, 734.
  - Parse quirk: the source splices C1.3.2 Multi-processor support between the DWT and ITM passages; the article restores the logical order (3.2.1–3.2.4) and numbers the unnumbered h2s in parent order.
  - S7 result: confirmed by the user.
  - [x] plan gate [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D1 → `armv7-m/part-d/coresight_infrastructure_ids/` (CoreSight Infrastructure IDs; L33321–33390, 70 ln; PDF pp. 766–769; 1 section, 2 tables, 0 figures; stub exists)
  - Note: the CoreSight ID-register set (component/part IDs) as two tables; text-only run.
  - S1 result: source resolved to the re-parsed `.md` (L33321–33390, 70 ln) with PDF pp. 766–768 as fallback; census = 1 section (D1.1), 2 tables (D1-1, D1-2), 0 figures. The Step 3.5 stub held front matter only → full translation in place.
  - S2 result: article written in place (65 ln) — `## 1.` + Table D1-1 (component/peripheral ID registers, footnote a: X bits CoreSight-defined, Y IMPLEMENTATION DEFINED) and Table D1-2 (LSR/LAR) as GFM.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: 2/2 tables present and complete; every ID row and the LSR/LAR fields were verified cell-by-cell against PDF pp. 766–768.
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D2 → `armv7-m/part-d/legacy_instruction_mnemonics/` (Legacy Instruction Mnemonics; L33391–33574, 184 ln; PDF pp. 770–777; 4 sections, 2 tables, 0 figures; stub exists)
  - Note: pre-UAL mnemonics mapped to their UAL equivalents; the two tables are the mapping reference, GFM by default.
  - S1 result: source resolved to the re-parsed `.md` (L33391–33574, 184 ln) with PDF pp. 770–777 as fallback; census = 4 sections (D2.1–D2.3 + D2.3.1), 2 tables, 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (175 ln) — §1 Thumb 指令助记符 (Table D2-1, 119 rows after splitting the parse's 6 merged rows), §2 UAL 之前的伪指令 NOP, §3 UAL 之前的浮点指令助记符 (Table D2-2) + 3.1 FLDMX, FSTMX. The source's `<Rd>` typo in the CMP row is kept faithfully.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: both tables complete; the mnemonic/operand row set matches the source one-to-one (no row added, dropped or merged).
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D3 → `armv7-m/part-d/deprecated_features/` (Deprecated Features in Armv7-M; L33575–33626, 52 ln; PDF pp. 778–779; 3 sections, 0 tables, 0 figures; stub exists)
  - Note: a cross-reference appendix pointing at the Part A–C sections that carry each deprecated feature — translate the list and resolve every pointer to the site article that now covers it.
  - S1 result: source resolved to the re-parsed `.md` (L33575–33626, 52 ln) with PDF pp. 778–779 as fallback; census = 3 sections (D3.1 + D3.1.1–D3.1.3 + D3.2), 0 tables, 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (52 ln) — `## 1.` + `### 1.1.` with `#### 1.1.1. 四字节栈对齐`, `#### 1.1.2. 通过不压栈 LR 优化上下文切换`, `#### 1.1.3. 同时把 DWT_CTRL.PCSAMPLENA 与 DWT_CTRL.CYCEVTENA 置 1`, and `### 1.2. Armv7-M Thumb 指令集的已弃用特性`; every source cross-reference resolves to the local section.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: no table or figure; the deprecated-item set matches the source (3 architecture items + the Thumb instruction-set list).
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D4 → `armv7-m/part-d/debug_itm_and_dwt_packet_protocol/` (Debug ITM and DWT Packet Protocol; L33627–34402, 776 ln; PDF pp. 780–797; 3 chapters / 19 subsections, 7 tables, 22 figures; stub exists)
  - Note: packet-format reference — 22 figures numbered D4-1 … D4-22. `Figure D4-4` and `Figure D4-10` are present in the re-parsed `.md` as `## Figure …` headings, so no caption is missing at this revision. Protocol byte/bit layouts are figures only when drawn as packet diagrams; a row/column grid becomes a GFM table.
  - S1 result: source resolved to the re-parsed `.md` (L33627–34402, 776 ln) with PDF pp. 780–797 as fallback; census = 3 chapters / 19 subsections, 7 tables (D4-1 … D4-7), 22 figures (D4-1 … D4-22). Stub held front matter only → full translation in place.
  - S2 result: article written in place (748 ln) — §1 关于 ITM 与 DWT 包 (1.1–1.3), §2 包描述 (2.1–2.9 incl. 2.2.1, 2.4.1–2.4.3, 2.6.1, 2.8.1), §3 DWT 对硬件源包的使用 (3.1–3.4 incl. 3.3.1/3.3.2 and 3.4.1–3.4.3).
  - S3 result: `FigureD4-1.png` cropped from the PDF at 3× with a 4 % margin. The other 21 packet diagrams are byte-row × bit-column grids and are transcribed as GFM bit tables labelled 图 D4-2 … 图 D4-22 in source figure order; the 7 source tables stay GFM labelled 表 D4-1 … 表 D4-7.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: figure/table numbering reconciled with the source — 22 figures + 7 tables, every label unique and in source order; Figure D4-19 sits after its introducing sentence and before the header field list, as in the source; bit assignments re-read from the PDF word coordinates.
  - PDF fallback: the parse merged or misaligned the bit grids of Figures D4-8, D4-9, D4-10, D4-11, D4-16, D4-19 and D4-21; their cell rows were rebuilt from the PDF text coordinates.
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D5 → `armv7-m/part-d/armv7r_differences/` (Armv7-R Differences; L34403–34491, 89 ln; PDF pp. 798–803; 5 sections, 0 tables, 0 figures; stub exists)
  - Note: profile-difference summary (A/R vs M); text-only run.
  - S1 result: source resolved to the re-parsed `.md` (L34403–34491, 89 ln) with PDF pp. 798–803 as fallback; census = 5 sections, 0 tables, 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (90 ln) — §1 关于 Armv7-M 与 Armv7-R 体系结构配置文件, §2 端序支持, §3 应用级支持, §4 系统级支持, §5 调试支持.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: no table or figure; the five profile-difference sections match the source scope and order.
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D6 → `armv7-m/part-d/pseudocode_definition/` (Pseudocode Definition; L34492–35328, 837 ln; PDF pp. 804–827; 64 sections, 1 table, 0 figures; stub exists)
  - Note: the formal pseudocode language definition (operators, statements, functions); keep every grammar production and `arm`-fenced sample verbatim, translate only the surrounding prose.
  - S1 result: source resolved to the re-parsed `.md` (L34492–35328, 837 ln) with PDF pp. 804–827 as fallback; census = 7 chapters / 96 subsections, 1 table (D6-1), 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (1,042 ln) — §1 指令编码图与伪代码, §2 伪代码的限制, §3 数据类型 (3.1–3.9), §4 表达式, §5 运算符与内建函数 (5.1–5.4 incl. 5.1.1/5.1.2, 5.3.1–5.3.9, 5.4.1–5.4.9), §6 语句与程序结构 (6.1.1–6.1.7, 6.2.1–6.2.6), §7 其他辅助过程与函数 (7.1–7.38, ArchVersion … VFPExcBarrier). All pseudocode stays verbatim in `arm` fences.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK after the five pseudocode-construct headings took a Chinese prefix (`#### 6.2.1. 条件语句 if ... then ... else ...` etc.).
  - S6 result: Table D6-1 complete; §7 carries all 38 helper functions in source order, and every grammar production / sample block is character-identical to the source.
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D7 → `armv7-m/part-d/pseudocode_index/` (Pseudocode Index; L35329–35648, 320 ln; PDF pp. 828–841; 2 sections, 2 index tables, 0 figures; stub exists)
  - Note: the operator/keyword/function index — two long tables whose entries stay verbatim while the headers translate.
  - S1 result: source resolved to the re-parsed `.md` (L35329–35648, 320 ln) with PDF pp. 828–841 as fallback; census = 2 sections, 2 index tables (D7-1, D7-2), 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (270 ln) — §1 伪代码运算符与关键字 (Table D7-1), §2 伪代码函数与过程 (Table D7-2, ~170 entries); merged *See* cells expanded per row and the `||` operator row written as `<code>&#124;&#124;</code>` so GFM renders it.
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: both index tables complete against the source — every operator/keyword row and every function/procedure entry present, entry order preserved, entry text and the *See* references untranslated.
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8
- [ ] D8 → `armv7-m/part-d/register_index/` (Register Index; L35649–35833, 185 ln; PDF pp. 842–846; 6 sections, 3 index tables, 0 figures; stub exists)
  - Note: the register index as three tables; every entry links the register to the article section that describes it.
  - S1 result: source resolved to the re-parsed `.md` (L35649–35833, 185 ln) with PDF pp. 842–848 as fallback; census = 4 sections (D8.1–D8.4, with D8.2.1/D8.2.2), 3 index tables (D8-1 … D8-3), 0 figures. Stub held front matter only → full translation in place.
  - S2 result: article written in place (174 ln) — §1 Arm 内核寄存器 (D8-1), §2 浮点扩展寄存器 (2.1/2.2), §3 内存映射的系统寄存器 (D8-2, links to `../../part-b/system_address_map/`, `../../part-b/cpuid_scheme/`, `../../part-b/system_memory_model/`), §4 内存映射的调试寄存器 (D8-3, links to `../../part-c/debug/`).
  - S3 result: N/A — no figures.
  - S4 result: N/A — page already registered by the Step 3.5 scaffold.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK (417 nav targets); `check_heading_lang.py` OK.
  - S6 result: 3/3 tables complete and every in-site link resolves; Table D8-3 footnote a re-read from PDF p. 848 ("除表中列出的寄存器外，调试支持还包括 ICSR 中的若干位…"); the MPU registers stay plain text because no article section describes them.
  - [x] S1 [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [ ] S8

## Tail status

- Every chapter of Part A and Part B is translated and registered. C1 and the Part D appendices D1–D8 are translated in place and passed the S7 user gate on 2026-11-18; all three gates pass for the batch (`--strict` 0 WARNINGs, `check_indexes.py` 417 nav targets / 0 broken links, `check_heading_lang.py` OK). The batch is shipped in PR #406 on `feature/docs-bsw-template-cortex-m7-corpus`, so only S8 (merge) remains.
- A7 Instruction Details (16,412 ln) was completed on 2026-11-14 and is not queued again; the part-D index tables (D7/D8) describe its pseudocode and registers.

## Part A / Part B completion batch (2026-11-14)

That batch was translated from the PDF text layer (`reference-docs/arm/cortex-m7/DDI0403E_e_armv7m_arm.pdf`, 858 pp) because the ima-parsed `.md` was missing from disk at the time. The `.md` was re-parsed on 2026-11-18 (36,478 ln) and is the primary source again for every run from C1 onwards.

- [x] **A1 Introduction** — article `armv7-m/part-a/introduction/index.md` (A1.1–A1.3, Table A1-1, 0 figures); nav + both landing pages updated.
- [x] **B1 System Level Programmers' Model (remaining sections)** — completed in place on `m7-trm/programmers_model/index.md`, the merged chapter page. New §2 系统级简介 (B1.1), §3 关于 Armv7-M 内存映射架构 (B1.2), §4 系统级术语与操作概述 (B1.3, §4.1–§4.4: 模式/特权/栈 Table B1-1, 异常类别与状态, 执行状态, 调试状态), §5 寄存器 (B1.4, §5.1–§5.7: 核心寄存器, xPSR with Figure B1-1 + Tables B1-2/B1-3, 掩码寄存器 with Figure B1-2, CONTROL, 保留位, 内存顺序模型, 伪代码定义 with LookUpSP), §30 浮点支持 (B1.6, Table B1-10, ExecuteFPCheck/CheckVFPEnabled/PreserveFPState/TakePreserveFPException). The old condensed TRM §2 操作模式与执行状态 was dropped (subsumed by B1.3); §3–§27 renumbered to §6–§31. Figures `FigureB1-1.png` (p517) and `FigureB1-2.png` (p519) cropped at 4×.
- [x] **A2 The Application Level Programmers' Model** — article `armv7-m/part-a/application_level_model/index.md` (§1 关于应用程序级程序员模型 + 1.1; §2 数据类型与运算 incl. LSL/LSR/ASR/ROR/RRX, AddWithCarry, SignedSatQ/UnsignedSatQ/SatQ; §3 寄存器与执行状态 + 3.1–3.4 with APSR; §4 异常、故障与中断 + 4.1; §5 可选的浮点扩展 with 5.1–5.4 and 5.4.1–5.4.21 covering the full FP pseudocode set; §6 协处理器支持). 6 figures cropped at 4×: `FigureA2-1.png` (p35, FP 寄存器双视图), `FigureA2-2.png` (p31, APSR), `FigureA2-3.png` (p37, FPSCR), `FigureA2-4.png` (p39, 单精度), `FigureA2-5.png` (p40, 双精度), `FigureA2-6.png` (p42, 半精度); Tables A2-1…A2-4 as GFM.
- [x] **A7 Instruction Details** — article `cortex/armv7-m/part-a/instruction_details/index.md`, **completed** (single-page decision: the whole chapter as one article; encoding bit grids rendered as GFM bit tables instead of image crops, per requester). Done: §1–§6 (A7.1 指令描述格式, A7.2 标准汇编语法字段, A7.3 条件执行 + Table A7-1/A7-2, A7.4 施加于寄存器的移位, A7.5 存储器访问, A7.6 提示指令) and all 263 entries 7.1–7.263 (A–Y 段，ADC … YIELD), with encoding-specific pseudocode, T1/T2… bit tables, assembler syntax, `where：` fields, operation pseudocode and exception lines per entry.

## Part C / Part D scaffold (2026-11-15)

The remaining Parts now have their tree: one Part index page plus one title-only stub per chapter (arm-translate Step 3.5), all registered in nav, `armv7-m/index.md` and their Part index in the same change. Chapter titles and order were read from the PDF contents (pp. 7–8) and the "Using this manual" Part overview (p. 12).

- `part-c/index.md` → Part C Debug Architecture; stub `part-c/debug/` (Chapter C1 Armv7-M Debug).
- `part-d/index.md` → Part D Appendices, now listing D1–D8 followed by the glossary in source order; stubs `part-d/coresight_infrastructure_ids/` (D1), `part-d/legacy_instruction_mnemonics/` (D2), `part-d/deprecated_features/` (D3), `part-d/debug_itm_and_dwt_packet_protocol/` (D4), `part-d/armv7r_differences/` (D5), `part-d/pseudocode_definition/` (D6), `part-d/pseudocode_index/` (D7), `part-d/register_index/` (D8). `part-d/glossary/` was already translated.

The stubs carry front-matter `title` only — no body, no placeholder sentence. A later run detects them as `Partial / stub` at S1 and writes the translation in place (same directory), never opening a second page.
