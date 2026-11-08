# Sync todo: Group R52plus-TRM — Cortex-R52+ TRM 102199_0001_03 (`arm_cortex_r52plus_processor_trm_102199_0001_03_en.pdf`, 719 pp, PDF only)

Generated: 2026-11-07 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the same PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

**Source shape:** this document has **no ima Markdown parse** — the PDF text layer is the only source, so the "never translate from the PDF when a `.md` exists" rule does not apply here. Crops and table cells come from the same PDF. Section numbers below are the R52+ ones; the older [R52-TRM](R52-TRM.md) group follows `100026` and numbers the same chapters two lower (Programmers Model ch2, System Control ch3, Clocking ch4, Initialization ch6, Memory System ch7, MPU ch8).

Chapter span map (PDF pages): ch1 Introduction 24–27 (4) · ch2 The Cortex-R52+ processor 28–44 (17) · ch3 Programmers Model 45–53 (9) · ch4 System Control 54–218 (165) · ch5 Clocking and Resets 219–222 (4) · ch6 Power Management 223–230 (8) · ch7 Initialization 231–235 (5) · ch8 Memory System 236–275 (40) · ch9 Memory Protection Unit 276–283 (8) · ch10 Generic Interrupt Controller 284–382 (99) · ch11 Generic Timer 383–385 (3) · ch12 Debug 386–435 (50) · ch13 Performance Monitor Unit 436–462 (27) · ch14 Cross Trigger 463–479 (17) · ch15 Embedded Trace Macrocell 480–563 (84) · ch16 Advanced SIMD and floating-point support 564–575 (12) · A Signal Descriptions 576–615 (40) · B Cycle Timings and Interlock Behavior 616–638 (23) · C Processor UNPREDICTABLE Behaviors 639–652 (14) · D PMC-R52+ 653–715 (63) · E Revisions 716–719 (4).

## Queue

- [x] ch3 programmers_model — verified (article `r52plus-trm/programmers_model/index.md`, 289 ln, 2 `##` vs 9 pp, 2026-11-09)
  - Note (S6): R52+ ch3.1 About the programmers model + ch3.2 Armv8-R AArch32 architecture concepts; the article was built from R52 ch2 — compare section by section, fix only real gaps.
  - S1 result: structure matches ch3 exactly — `## 1.` ← 3.1 with 1.1 Advanced SIMD and Floating-point … 1.6 Security state, `## 2.` ← 3.2 with 2.1 Execution state … 2.13 GIC Architecture (2.4.1–2.4.3 under 2.4). Source has no figures and two tables (Table 3-1 processor modes, Table 3-2 Armv8 memory types), both already GFM.
  - S6 result: three real gaps fixed — 2.8 `相关参考` still carried the R52 numbers/pages (ch9 9-247 / ch10 10-332 / ch11 11-336 / ch12 12-383), replaced with the R52+ chapters (ch10 p284, ch11 p383, ch12 p386, ch13 p436); the `Related information` of 3.2 (`Supported standards on page 40`, i.e. 2.4) was missing, added; the `1.4 支持的标准（第 1-24 页）` reference closing 2.13 does not exist in R52+ ch3 (ch1.4 is Useful resources) and was removed. Wording aligned to r0p3: 1.4 reads `PSTATE.T` (was `CPSR.T`). Table 3-1/3-2 row sets match the source. Stray blank lines after the front matter removed.
  - S8 result: PR #350.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch5 clocking_and_resets — verified (article 124 ln, 3 `##` vs 4 pp, 2026-11-09)
  - Note (S6): ch5.1 Clock and clock enables / 5.2 Reset signals / 5.3 Reset-related signals; check every signal row against the R52+ set (the R52+ adds `Clock and clock enable signals` to appendix A, which this chapter summarises).
  - S1 result: structure matches ch5.1–5.3; Tables 5-1/5-2/5-3/5-4/5-5 all present as GFM with the full R52+ signal sets (CLKIN/CLKINDCLS, eight clock enables, eight reset signals, five reset-related signals).
  - S6 result: four fixes — core name `Cortex-R52` → `Cortex®-R52+` throughout; the clock-gating pointer retargeted from R52 `5-194 5.3` to R52+ `第 223 页的 6.3 Architectural clock gating`; the unnumbered `Reset assertion sequence` / `Reset deassertion sequence` subsections of 5.2 were missing and are now `2.1`/`2.2` with full text; bullet 2.1(1) wording corrected to `冷复位（Cold reset）`.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch7 initialization — verified (article 141 ln, 3 `##` vs 5 pp, 2026-11-09)
  - Note (S6): R52+ renumbers 6.3 Booting into EL1 as **7.3 Entering EL1** — confirm the heading/section wording and that 7.1/7.2 carry no R52+-only text.
  - S1 result: structure matches ch7.1–7.3; source has one table (Table 7-1 speculation types), now present.
  - S6 result: five gaps fixed — 7.1.4 Speculation (with Table 7-1) was missing entirely; the `CFGINITREG` paragraph was out of source order, lacked the 4.2 Register summary page ref and the Integration Manual citation; FPU/MPU/TCM page refs retargeted from R52 `3-x` to R52+ 4.3.1 p82 / 4.3.76 p182 / 4.3.92 p203 / 4.3.53 p147; `CFGRAMPROTEN` corrected to `CFGTCMBOOTx` in both 7.2.2 and 7.2.3; heading `引导进入 EL1` → `进入 EL1` and the missing `编程 SPSR` bullet restored.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch8 memory_system — verified (article 1076 ln, 13 `##` vs 40 pp, 2026-11-09)
  - Note (S6): 8.12 Peripherals memory map and 8.13 On-line MBIST were already restored into the article on 2026-11-07 from this PDF (see [R52-TRM](R52-TRM.md)); confirm all other sections and tables (AXIM/LLPP/Flash/AXIS) match the R52+ text.
  - S1 result: 8.1–8.13 all present (`Error detection and handling` is the R52+ name of the old 7.9 `Fault detection and handling`, already reflected); eight figures and every table (8-1 … AXIS/LLPP limits) are GFM.
  - S6 result: four fixes — 8.1 `Related information` block added (TCM p238, AXIM p250, LLPP p256, Flash p264); 8.9.3 `相关参考` replaced the invented "第 3 章" sentence with the four record-register page refs (155/105/207/114); 8.9.4 `Related information` added (AXIM p250, AXIM signals p586, AXIS p267, AXIS signals p592); the stale `第 12 章 12.6 Events` pointer retargeted to `第 455 页的 13.6 Events`. Table 8-1 keeps the article's 32KB index `[12:6]` — the PDF prints `[10:6]`, which cannot address 128 sets and is an obvious source typo; recorded here rather than propagated.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
- [x] ch9 memory_protection_unit — verified (article 624 ln, 5 `##` vs 8 pp, 2026-11-09)
  - Note (S6): ch9.3 Virtualization support (EL2 MPU registers) must be present; legacy `Table9-*` images carry R52 numbers — verify row sets by caption, never rename.
  - S1 result: 9.3 with 9.3.1 attribute combining present; Tables 9-1 … 9-7 GFM and row sets match (memory-type 12 rows, cacheability 5, shareability 7).
  - S6 result: three fixes — 9.5 register summaries (Tables 9-8/9-9, 9 + 16 rows) were missing and are now at the head of §5 with the direct-access summary; five junk inline PNGs of register-bit names (`SCTLR.M`, `SCTLR.BR`, `HSCTLR.M`, `HSCTLR.BR`, `HCR.DC`) removed with their files (the chapter has no figures); the stale `第 3-148 页表 3-106/3-107` pointer retargeted to `第 174 页表 4-163/4-164`.
  - S8 result: PR #352.
  - [x] S1 [x] S6 [x] S7 [x] S8
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
