# Sync todo: Group ARMv7-M — DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines): Part A L739 — A1 Introduction L743–880 (137) · A2 The Application Level Model L880–4060 (3,180, ⏸) · A3 The Memory Model L4060–6099 (2,039, ⏸) · A4 The Armv7-M Instruction Set L6099–7082 (983) · A5 The Thumb Instruction Set Encoding L7082–8272 (1,190) · A6 The Floating-point Instruction Set Encoding L8272–8634 (362) · A7 Instruction Details L8634–28616 (19,982, ⏸ deferred). Part B L28620 — B1 System Level Programmers' Model L28620–32964 (4,344, ⏸; B1.5 = Armv7-M exception model) · B2 System Memory Model L32964–34504 (1,540) · B3 System Address Map L34504–38282 (3,778, ⏸; B3.5 = PMSAv7) · B4 The CPUID Scheme L38282–39914 (1,632) · B5 System Instruction Details L39914–40432 (518). Part C Debug Architecture — C1 Armv7-M Debug L40436–46188 (5,752, ⏸ deferred). Part D Appendixes — D1 CoreSight Infrastructure IDs … D8 Register Index, L46192–end (deferred).

Existing-article mappings (mapping.md, evidence re-checked at census): `arm_architecture_memory_mode` ← A3 · `programmers_model` ← B1.5 (evidence `Figure2-*` unverified — confirm at S1) · `mpu` ← B3.5 (`TableB3-1…11`) · `system_address_map` ← B3.1–B3.4 (article sections SCS/SysTick/NVIC = B3.2/B3.3/B3.4) · `instruction_set` ← A4/A5/A6 summary.

## Queue

- [x] exception_model — completed (article `m7_processor/programmers_model/index.md`, 1,834 ln, 5 imgs vs B1.5 of the 4,344-ln chapter B1)
  - S1 result: mapping confirmed at the figure/table evidence — `Figure2-1`/`Figure2-2`/`Table 2-14` are TRM ch2 derivatives, and the exception-model prose aligns with B1.5.1–B1.5.19, so the page was completed in place against B1.5.
  - S2 result: §6–§8 kept (TRM ch2 front matter, aligned to B1.5.1 and completed: DebugMonitor inserted, disable/escalation notes, ICSR control bits, 496 external interrupts), §9 异常编号定义 (Table B1-4) added, §10 向量表 completed (Table B1-5), §11 异常优先级与抢占 (Table B1-6), §12 中断优先级分组 (Table B1-7), §13 执行优先级与优先级提升 (Example B1-1, ExecutionPriority pseudocode, priority escalation, SVCall/PendSV model), §14 复位行为 (TakeReset), §15 异常进入和返回 (ExceptionEntry/PushStack/ExceptionTaken/ReturnAddress/UpdateFPCCR, stack alignment, EXC_RETURN Tables B1-8/B1-9, ExceptionReturn/DeActivate/PopStack), §16–§26 = B1.5.9–B1.5.19, §27 参考文献.
  - S3 result: `FigureB1-3.png` (p536) and `FigureB1-4.png` (p538) cropped; all six numbered tables (B1-4…B1-9) and the three unnumbered fault tables rendered as GFM.
  - [x] S1 [x] S2 (gaps only) [x] S3 [x] S5 [x] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] protected_memory_system_archi_pmsav7 — verify-only (article `m7_processor/mpu/` sections 4–14, 13 imgs vs B3.5)
  - Note (S6): article covers PMSAv7 concept → MPU registers (MPU_TYPE…MPU_RASR + aliasing) — confirm against B3.5 subsection list; record evidence.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] system_address_map — completion (article 157 ln vs B3.1–B3.4; B3.4 NVIC detail overlaps the `nvic` article — decide the split boundary at S1 and record it)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ arm_architecture_memory_mode — completion (article 493 ln vs A3 The Memory Model, 2,039 ln — >1500-line rule: present the run plan first)
  - Note (S1): article has only `## 1.` + `## 3. 参考文献` at h2 level — likely blog-prose vs the chapter's real section tree; expect substantial in-place insertion.
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] instruction_set — content alignment (article 139 ln vs A4 + A5 + A6; heading repair is tracked in [M7-TRM](M7-TRM.md) as a hygiene row — do it in this run if it happens here first)
  - Note: A5 encoding tables are textual — GFM tables by default; raw HTML only when the structure qualifies (see .agents/skills/arm-translate/references/article-format.md §Tables). A7/C1 instruction-by-instruction details are NOT in this row (deferred tail).
  - [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B2 → new article (System Memory Model — caches, branch predictors, memory-system pseudocode, 1,540 ln; e.g. `m7_processor/system_memory_model/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B4 → new article (The CPUID Scheme, 1,632 ln; e.g. `cpuid_scheme/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] B5 → new article (System Instruction Details, 518 ln; e.g. `system_instructions/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately deferred)

- A1 Introduction (137 ln), A2 The Application Level Model (3,180 ln), A7 Instruction Details (19,982 ln), C1 Armv7-M Debug (5,752 ln — overlaps the M7 TRM debug chapters; prefer the TRM for implementation), D1–D8 appendixes (pseudocode/register indexes) — start on explicit request only.
