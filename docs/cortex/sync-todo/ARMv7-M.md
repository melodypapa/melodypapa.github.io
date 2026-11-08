# Sync todo: Group ARMv7-M — DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines): Part A L739 — A1 Introduction L743–880 (137) · A2 The Application Level Model L880–4060 (3,180, ⏸) · A3 The Memory Model L4060–6099 (2,039, ⏸) · A4 The Armv7-M Instruction Set L6099–7082 (983) · A5 The Thumb Instruction Set Encoding L7082–8272 (1,190) · A6 The Floating-point Instruction Set Encoding L8272–8634 (362) · A7 Instruction Details L8634–28616 (19,982, ⏸ deferred). Part B L28620 — B1 System Level Programmers' Model L28620–32964 (4,344, ⏸; B1.5 = Armv7-M exception model) · B2 System Memory Model L32964–34504 (1,540) · B3 System Address Map L34504–38282 (3,778, ⏸; B3.5 = PMSAv7) · B4 The CPUID Scheme L38282–39914 (1,632) · B5 System Instruction Details L39914–40432 (518). Part C Debug Architecture — C1 Armv7-M Debug L40436–46188 (5,752, ⏸ deferred). Part D Appendixes — D1 CoreSight Infrastructure IDs … D8 Register Index, L46192–end (deferred).

Existing-article mappings (mapping.md, evidence re-checked at census): `arm_architecture_memory_mode` ← A3 · `programmers_model` ← B1.5 (evidence `Figure2-*` unverified — confirm at S1) · `mpu` ← B3.5 (`TableB3-1…11`) · `system_address_map` ← B3.1–B3.4 (article sections SCS/SysTick/NVIC = B3.2/B3.3/B3.4) · `instruction_set` ← A4 (completed 2026-11-08, appended to the TRM summary); A5 and A6 are separate articles, queued below.

## Queue

- [x] exception_model — completed (article `m7_processor/programmers_model/index.md`, 1,834 ln, 5 imgs vs B1.5 of the 4,344-ln chapter B1)
  - S1 result: mapping confirmed at the figure/table evidence — `Figure2-1`/`Figure2-2`/`Table 2-14` are TRM ch2 derivatives, and the exception-model prose aligns with B1.5.1–B1.5.19, so the page was completed in place against B1.5.
  - S2 result: §6–§8 kept (TRM ch2 front matter, aligned to B1.5.1 and completed: DebugMonitor inserted, disable/escalation notes, ICSR control bits, 496 external interrupts), §9 异常编号定义 (Table B1-4) added, §10 向量表 completed (Table B1-5), §11 异常优先级与抢占 (Table B1-6), §12 中断优先级分组 (Table B1-7), §13 执行优先级与优先级提升 (Example B1-1, ExecutionPriority pseudocode, priority escalation, SVCall/PendSV model), §14 复位行为 (TakeReset), §15 异常进入和返回 (ExceptionEntry/PushStack/ExceptionTaken/ReturnAddress/UpdateFPCCR, stack alignment, EXC_RETURN Tables B1-8/B1-9, ExceptionReturn/DeActivate/PopStack), §16–§26 = B1.5.9–B1.5.19, §27 参考文献.
  - S3 result: `FigureB1-3.png` (p536) and `FigureB1-4.png` (p538) cropped; all six numbered tables (B1-4…B1-9) and the three unnumbered fault tables rendered as GFM.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 (gaps only) [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] protected_memory_system_archi_pmsav7 — verified (article `m7_processor/mpu/index.md`, 611 ln, 5 bit-field images vs B3.5)
  - S1 result: structure matches B3.5 exactly — `## 4.` ← B3.5 intro, `## 5.` ← B3.5.1, `## 6.` ← B3.5.2, `## 7.` ← B3.5.3 (7.1 sub-region / 7.2 Armv7-M specific / 7.3 MPU pseudocode / 7.4 MPU fault support), `## 8.` ← B3.5.4, `## 9.` ← B3.5.5 MPU_TYPE, `## 10.` ← B3.5.6 MPU_CTRL (10.3 = TRM-derived non-privileged instruction impact), `## 11.` ← B3.5.7 MPU_RNR, `## 12.` ← B3.5.8 MPU_RBAR, `## 13.` ← B3.5.9 MPU_RASR (13.3 sub-regions / 13.4 attributes / 13.5 XN), `## 14.` ← B3.5.10 alias support.
  - S6 result: Tables B3-11…B3-16 all present as GFM; the 5 images are bit-field bars, which stay images. Three defects fixed: stray `**` on the `XN：MPU_RASR[28]` bullet (broken bold run), garbled Table B3-12 lead sentence, garbled Region 0–15 alias sentence.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 (N/A: verify-only, no gaps) [x] S3 (N/A: bit-bar images already present) [x] S4 (N/A: page already registered) [x] S5 (N/A: no text changed) [x] S6 [x] S7 [x] S8
- [x] system_address_map — completed (article `m7_processor/system_address_map/index.md`, 2,392 ln, 33 bit-bar imgs vs B3.1–B3.4)
  - S1 result (split decision): **no split against the sibling pages.** `nested_vectored_interrupt_controller` and `system_control` are TRM implementation pages whose own prose defers the architectural register definitions to the ARM, so B3.2 (2.2–2.26 SCB/ID registers), B3.3 (SysTick) and B3.4 (NVIC) were translated in full here. Page tree = B3.1 (## 1) → B3.2 (## 2) → B3.3 (## 3) → B3.4 (## 4); only cross-link added is the PMSAv7 pointer to `mpu/`.
  - S2 result: §2.2–§2.26 added (Tables B3-4/B3-5/B3-6; CPUID, ICSR, VTOR, AIRCR, SCR, CCR, SHPR1–3, SHCSR, CFSR + MMFSR/BFSR/UFSR, HFSR, MMFAR, BFAR, AFSR, CPACR + FP enable, FPCCR, FPCAR, FPDSCR, ICTR, ACTLR, STIR); §3 added (SysTick operation, Table B3-7, SYST_CSR/RVR/CVR/CALIB); §4 added (NVIC operation + external-interrupt-input pseudocode, implemented interrupts, Tables B3-8/B3-9/B3-10, NVIC_ISER/ICER/ISPR/ICPR/IABR/IPR). Stale §2 overview bullet list replaced with pointers to the new subsections.
  - S3 result: 33 bit bars cropped from the ARM PDF (the chapter has no raster figures; the bars are vector) named by register, `CPUID.png` … `NVIC_IPR.png`; no other figures in B3.1–B3.4.
  - S6 result: every numbered table (B3-4 … B3-10) rendered as GFM.
  - S8 result: merged as `c054a6e` (PR #318).
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] arm_architecture_memory_mode — completed (article `m7_processor/arm_architecture_memory_mode/index.md`, 1,194 ln, 7 imgs vs A3 The Memory Model, 2,039 ln)
  - S1 result: the page already mirrored A3 at h2 level (`## 1.` = A3 intro, `### 1.1`–`### 1.8` = A3.1–A3.8 with the 1.x.y subsections), so the gaps were missing subsections rather than a restructuring: A3.2.1 对齐行为 absent, A3.4.1–A3.4.6 absent, A3.5.7 truncated after rule 2, and A3.6/A3.7/A3.8 present only as condensed paraphrase.
  - S2 result: §1.2.1 added (faulting/non-faulting access lists, IMPLEMENTATION DEFINED note, alignment pseudocode, PC-update rules); §1.4.1–1.4.6 added (local monitor, global monitor, Tables A3-2/A3-3, 标记与标记内存块的大小, 上下文切换支持, 使用限制, 同步原语与内存顺序模型); §1.5.7 extended with rules 3–6, the software-coherency sub-rules and the race-condition note; §1.6 rewritten to A3.6.1/A3.6.2 (data/instruction privilege access control); §1.7 rewritten (reads and writes, observability/completion, address & control dependency, Figure A3-8, the six barriers CSDB/DMB/DSB/ISB/PSSBB/SSBB, SCS synchronization); §1.8.2/1.8.3 completed (Figure A3-9, hierarchy note, data/instruction coherency).
  - S3 result: `FigureA3-6.png` (p71 local monitor state machine), `FigureA3-7.png` (p74 global monitor state machine), `FigureA3-9.png` (p97 memory hierarchy). Figure A3-8 is a plain row/column ordering matrix, so it was rendered as GFM instead of a crop.
  - S6 result: Tables A3-2 and A3-3 (monitor state transitions) and the A3-8 matrix are GFM; the existing A3-1/A3-4 tables were already GFM.
  - S8 result: merged as `fe022df` (PR #322).
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: page already registered) [x] S5 [x] S6 [x] S7 [x] S8
- [x] instruction_set — completed (A4 only; article `m7_processor/instruction_set/index.md`, 878 ln, 1 img vs A4 The Armv7-M Instruction Set, 983 ln)
  - S1 result: scope fixed to A4 by decision — A4 is one page. A5 and A6 are separate articles and are now their own queue rows below. The page keeps its TRM-derived 200-row instruction summary as `## 1.`, and the A4 translation is appended as `## 2.` (no restructuring of the existing summary).
  - S2 result: `## 2.` added — chapter intro list of 13 sections; §2.1 关于指令集 (2.1.1 互工作支持, 2.1.2 条件执行), §2.2 统一汇编语言 (2.2.1 条件指令, 2.2.2 在 UAL 指令语法中使用标签), §2.3 分支指令, §2.4 数据处理指令 (2.4.1–2.4.8), §2.5 状态寄存器访问指令, §2.6 加载和存储指令 (2.6.1–2.6.5), §2.7 加载多个和存储多个指令 (2.7.1), §2.8 杂项指令, §2.9 产生异常的指令, §2.10 协处理器指令, §2.11 浮点加载和存储指令, §2.12 浮点寄存器传送指令, §2.13 浮点数据处理指令.
  - S3 result: A4 has no figures — every instruction encoding lives in chapters A5/A6 as numbered tables, so no crops were needed.
  - S6 result: all 22 A4 tables (A4-1 … A4-22) rendered as GFM, footnotes kept as `a.` / `b.` lines; cross-references phrased as `MLA（第 A7-289 页）`.
  - S8 result: merged as `2d7e17f` (PR #324).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] A5 → new article (The Thumb Instruction Set Encoding, 1,190 ln; e.g. `m7_processor/thumb_instruction_set_encoding/`)
  - Note: encoding tables are textual — GFM by default; raw HTML only when the structure qualifies (see .agents/skills/arm-translate/references/article-format.md §Tables). A7 instruction-by-instruction details are NOT in this row (deferred tail).
  - S1 result: A5 = PDF pp. 125–158; structure fixed to 3 chapters — §1 Thumb 指令集编码 (1.1 UNDEFINED/UNPREDICTABLE 空间, 1.2 0b1111 寄存器说明符, 1.3 0b1101/SP 支持 1.3.1–1.3.3), §2 16 位编码 (2.1–2.6, 2.5.1 If-Then 与提示), §3 32 位编码 (3.1–3.18, 3.4.1 提示, 3.4.2 杂项控制, 3.11.1 移动寄存器和立即数移位).
  - S2 result: article `m7_processor/thumb_instruction_set_encoding/index.md` written in place; numbering restarts at 1; source typos preserved.
  - S3 result: 30 encoding-bar crops at 3× (`EncodingA5-2.png`, `EncodingA5-2-1`…`EncodingA5-2-6`, `EncodingA5-2-5-1`, `EncodingA5-3.png`, `EncodingA5-3-1`…`EncodingA5-3-18`, `EncodingA5-3-4-1`, `EncodingA5-3-4-2`, `EncodingA5-3-11-1`); p143/p150/p152/p156 each yield two bars.
  - S4 result: nav entry added after the instruction-set page; landing item inserted as Cortex-M7 no. 5 with 5–18 renumbered to 6–19.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py` OK (324 nav targets, 0 broken links); `check_heading_lang.py` OK.
  - S6 result: all 30 tables (A5-1 … A5-30) rendered as GFM with merged cells expanded by repeating the spanning value; footnotes as `a.` / `b.` lines; cross-references phrased as `MOV（立即数）（第 A7-291 页）`.
  - S8 result: merged as `de13acc` (PR #327).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [ ] A6 → new article (The Floating-point Instruction Set Encoding, 362 ln; e.g. `m7_processor/fp_instruction_set_encoding/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B2 → new article (System Memory Model — caches, branch predictors, memory-system pseudocode, 1,540 ln; e.g. `m7_processor/system_memory_model/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B4 → new article (The CPUID Scheme, 1,632 ln; e.g. `cpuid_scheme/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B5 → new article (System Instruction Details, 518 ln; e.g. `system_instructions/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately deferred)

- A1 Introduction (137 ln), A2 The Application Level Model (3,180 ln), A7 Instruction Details (19,982 ln), C1 Armv7-M Debug (5,752 ln — overlaps the M7 TRM debug chapters; prefer the TRM for implementation), D1–D8 appendixes (pseudocode/register indexes) — start on explicit request only.
