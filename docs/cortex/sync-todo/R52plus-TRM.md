# Sync todo: Group R52plus-TRM — Cortex-R52+ TRM 102199_0001_03 (`arm_cortex_r52plus_processor_trm_102199_0001_03_en.pdf`, 719 pp, PDF only)

Generated: 2026-11-07 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the same PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

**Source shape:** this document has **no ima Markdown parse** — the PDF text layer is the only source, so the "never translate from the PDF when a `.md` exists" rule does not apply here. Crops and table cells come from the same PDF. Section numbers below are the R52+ ones; the older [R52-TRM](R52-TRM.md) group follows `100026` and numbers the same chapters two lower (Programmers Model ch2, System Control ch3, Clocking ch4, Initialization ch6, Memory System ch7, MPU ch8).

Chapter span map (PDF pages): ch1 Introduction 24–27 (4) · ch2 The Cortex-R52+ processor 28–44 (17) · ch3 Programmers Model 45–53 (9) · ch4 System Control 54–218 (165) · ch5 Clocking and Resets 219–222 (4) · ch6 Power Management 223–230 (8) · ch7 Initialization 231–235 (5) · ch8 Memory System 236–275 (40) · ch9 Memory Protection Unit 276–283 (8) · ch10 Generic Interrupt Controller 284–382 (99) · ch11 Generic Timer 383–385 (3) · ch12 Debug 386–435 (50) · ch13 Performance Monitor Unit 436–462 (27) · ch14 Cross Trigger 463–479 (17) · ch15 Embedded Trace Macrocell 480–563 (84) · ch16 Advanced SIMD and floating-point support 564–575 (12) · A Signal Descriptions 576–615 (40) · B Cycle Timings and Interlock Behavior 616–638 (23) · C Processor UNPREDICTABLE Behaviors 639–652 (14) · D PMC-R52+ 653–715 (63) · E Revisions 716–719 (4).

## Queue

- [ ] ch3 programmers_model — verify-only (article `r52p_processor/programmers_model/`, 292 ln, 2 `##` vs 9 pp)
  - Note (S6): R52+ ch3.1 About the programmers model + ch3.2 Armv8-R AArch32 architecture concepts; the article was built from R52 ch2 — compare section by section, fix only real gaps.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ch5 clocking_and_resets — verify-only (article 114 ln, 3 `##` vs 4 pp)
  - Note (S6): ch5.1 Clock and clock enables / 5.2 Reset signals / 5.3 Reset-related signals; check every signal row against the R52+ set (the R52+ adds `Clock and clock enable signals` to appendix A, which this chapter summarises).
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ch7 initialization — verify-only (article created 2026-11-07 from R52 ch6, 128 ln, 3 `##` vs 5 pp)
  - Note (S6): R52+ renumbers 6.3 Booting into EL1 as **7.3 Entering EL1** — confirm the heading/section wording and that 7.1/7.2 carry no R52+-only text.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ch8 memory_system — verify-only (article 1050 ln, 13 `##` vs 40 pp)
  - Note (S6): 8.12 Peripherals memory map and 8.13 On-line MBIST were already restored into the article on 2026-11-07 from this PDF (see [R52-TRM](R52-TRM.md)); confirm all other sections and tables (AXIM/LLPP/Flash/AXIS) match the R52+ text.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ch9 memory_protection_unit — verify-only (article 606 ln, 5 `##` vs 8 pp)
  - Note (S6): ch9.3 Virtualization support (EL2 MPU registers) must be present; legacy `Table9-*` images carry R52 numbers — verify row sets by caption, never rename.
  - [ ] S1 [ ] S6 [ ] S7 (if changed) [ ] S8 (if changed)
- [ ] ⏸ ch4 system_control — completion (article 233 ln, 1 `##` vs 165 pp: 4.1 About, 4.2 Register summary, 4.3 AArch32 register descriptions)
  - Note: >1500-line rule — segment by register group (cache/MPU/EL2/timer/debug) and agree the run plan before S2.
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch11 → new article (Generic Timer, 3 pp; e.g. `generic_timer/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch1 → new article (Introduction — product revision, audience, conventions, useful resources, 4 pp; low value, propose folding vs standalone at S1)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch6 → new article (Power Management — local/regional and architectural clock gating, power gating, 8 pp; e.g. `power_management/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch16 → new article (Advanced SIMD and floating-point support, 12 pp; e.g. `asimd_floating_point/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch2 → new article (The Cortex-R52+ processor — component blocks, interfaces, supported standards, design process, 17 pp; e.g. `introduction/` or fold into the ch1 page at S1)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch14 → new article (Cross Trigger — trigger inputs/outputs, CTM, register summary/descriptions, 17 pp; e.g. `cross_trigger/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] D → new article (PMC-R52+ appendix — MBIST usage models, March algorithm, test code, programmers model, 63 pp; e.g. `pmc_r52plus/`)
  - Note: chapter 8.12 and 8.13 both point at appendix D; the memory-system article's "第 653 页的 D.PMC-R52+" references resolve here once this page exists.
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch13 → new article (Performance Monitor Unit — 27 pp incl. 13.6 Events, 13.8 Exporting PMU events)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch12 → new article (Debug — 50 pp: system and memory-mapped register descriptions, external debug interface, ROM table)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch10 → new article (Generic Interrupt Controller — 99 pp: GIC functional description, programmers model, distributor/redistributor registers; consider splitting GICD/GICR at the plan gate)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ ch15 → new article (Embedded Trace Macrocell — 84 pp: ETM resources, event connectivity, operation, register descriptions)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately)

- A Signal Descriptions (40 pp signal tables), B Cycle Timings and Interlock Behavior, C Processor UNPREDICTABLE Behaviors, E Revisions — reference/chrome material per skill Step 3; revisit on explicit request. Appendix A overlaps `clocking_and_resets` (clock/reset signals) and the interface chapters (AXIM/AXIS/LLPP/Flash signal groups).
- The document glossary and cover/proprietary notice — chrome.
