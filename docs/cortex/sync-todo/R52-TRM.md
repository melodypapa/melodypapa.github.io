# Sync todo: Group R52-TRM — Cortex-R52 TRM r1p0 (`R52/cortex_r52_trm_100026_0100_00_en.md`, 44,511 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the TRM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines, incl. running headers — re-locate by title, first occurrence wins): ch1 Introduction L694–1370 (677) · ch2 Programmers Model L1371–1849 (479) · ch3 System Control L1850–12962 (~11.1k, ⏸) · ch4 Clocking and Resets L12963–13326 (364) · ch5 Power Management L13327–13946 (620) · ch6 Initialization L13947–14250 (304) · ch7 Memory System L14251–17182 (2,932, ⏸) · ch8 MPU L17183–17952 (770) · ch9 GIC L17953–27056 (9,104, ⏸) · ch10 Generic Timer L27057–27400 (344) · ch11 Debug L27401–32260 (4,860, ⏸) · ch12 PMU L32261–35485 (3,225, ⏸) · ch13 Cross Trigger L35486–37043 (1,558) · ch14 ETM L37044–… (⏸) · ch15 Advanced SIMD and floating-point support (tail; no reliable marker — locate by title) · Appendices A–D (Signal Descriptions / Cycle Timings / UNPREDICTABLE / Revisions — tail).

**Legacy revision shift:** `references/mapping.md` evidence for `programmers_model` (`Table3-1`) and `system_control` (`Table4-48`, "ch4 System Control") predates r1p0 — in this mirror Programmers Model = **ch2**, System Control = **ch3**. Legacy images (`Figure8_*` in memory_system, `Table9-*` in memory_protection_unit) carry old chapter numbers; keep the files, verify by caption text.

## Queue

- [ ] programmers_model — verify-only (article `r52p_processor/programmers_model/`, 190 ln vs ch2, 479 ln)
  - Note (S6): article's `##1 关于程序员模型` + `##2 Armv8-R AArch32 架构概念` mirror ch2's 2.1 + 2.2 — expect aligned; record evidence, fix only real gaps.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] memory_protection_unit — verify-only (article 483 ln, 27 imgs vs ch8, 770 ln)
  - Note (S6): legacy `Table9-*` images illustrate the r1p0 `Table 8-*` set — verify row sets by caption text; never rename images.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] memory_system — verify-only (article 362 ln, 13 `##` vs ch7, 2,932 ln)
  - Note (S6): article sections (TCM / L1 caches / AXIM / LLPP / Flash / AXIS / error handling / exclusive access / bus timeouts / peripherals map / MBIST) look chapter-complete; confirm no dropped section.
  - Resolved 2026-11-07: 8.12 Peripherals memory map and 8.13 On-line MBIST are absent from the R52 TRM (ch7 ends at 7.11); sections 12/13 were restored from the Cortex-R52+ TRM (`R52/arm_cortex_r52plus_processor_trm_102199_0001_03_en.pdf`, ch8.12/8.13).
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ⏸ system_control — completion (article 236 ln vs ch3 System Control ~11.1k parse ln: 3.1 About / 3.2 Register summary / 3.3 AArch32 register descriptions — the largest single item in the corpus)
  - Note: >1500-line rule — segment the chapter (register groups) and agree the run plan before S2; deliberate overlap + dedupe at segment boundaries (RTE pattern) only if the user approves a multi-run scope.
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch4 → new article (Clocking and Resets, 364 ln; e.g. `clocking_and_resets/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [x] ch6 → new article `r52p_processor/initialization/` (Initialization, 304 ln; 6.1 Initialization + 6.1.1 MPU / 6.1.2 FPU / 6.1.3 Caches, 6.2 TCM + 6.2.1-6.2.3, 6.3 Booting into EL1 — no figures, no tables)
  - Note (S1): the mirror moved from `private-docs/ARM/` to `reference-docs/arm/cortex-r52/`; the parse loses the whole 6.1 body (heading only), so that section was read from the PDF pages 6-201 to 6-204. Nav and landing reordered to chapter order while inserting the new page.
  - [x] S1 [x] S2 [x] S3 (n/a — no figures) [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [ ] ch5 → new article (Power Management, 620 ln; e.g. `power_management/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch10 → new article (Generic Timer, 344 ln; e.g. `generic_timer/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch13 → new article (Cross Trigger, 1,558 ln; e.g. `cross_trigger/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch1 → new article (Introduction, 677 ln; low value, propose folding vs standalone at S1)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch12 → new article (Performance Monitor Unit, 3,225 ln — >1500-line rule)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch11 → new article (Debug, 4,860 ln — >1500-line rule)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch14 → new article (Embedded Trace Macrocell, ~7.5k ln — >1500-line rule)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch9 → new article (Generic Interrupt Controller, 9,104 ln — largest R52 chapter; >1500-line rule; consider splitting GICD/GICC at the plan gate)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch15 → new article (Advanced SIMD and floating-point support; locate by title in the tail; e.g. `asimd_floating_point/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately)

- Appendices A–D (Signal Descriptions, Cycle Timings and Interlock Behavior, Processor UNPREDICTABLE Behaviors, Revisions) — reference/chrome material; revisit on explicit request.
- `R52/DDI0553B_y_armv8m_arm.md` — see [ARMv8-M](ARMv8-M.md) (deferred group).
