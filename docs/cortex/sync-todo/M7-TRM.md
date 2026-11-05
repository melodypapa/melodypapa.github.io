# Sync todo: Group M7-TRM — DDI0489F Cortex-M7 TRM r1p2 (`M7/DDI0489F_cortex_m7_trm_r1p2.md`, 8,778 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Last run: 2026-11-05 — instruction_set, nvic, program_status_register, ch3, ch4, ch6, ch8, ch9, ch10, ch11, ch12, ch1 done (PR #276). Remaining: ch5 (⏸ plan gate), ch14, ch13.
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the TRM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines, incl. running headers): ch1 Introduction L482–1104 (623) · ch2 Programmers Model L1105–1343 (239) · ch3 System Control L1344–2008 (665) · ch4 Initialization L2009–2271 (263) · ch5 Memory System L2272–4197 (1,926; ⏸) · ch6 MPU L4198–4403 (206) · ch7 NVIC L4404–4645 (242) · ch8 FPU L4646–4897 (252) · ch9 Debug L4898–5586 (689) · ch10 CTI L5587–6068 (482) · ch11 DWT L6069–6450 (382) · ch12 ITM L6451–6738 (288) · ch13 TPIU L6739–7878 (1,140) · ch14 Fault detection L7879–8778 (900; tail includes Appendix A Revisions + glossary). Chapters 6–14 have NO `# Chapter` markers — plain-text lines; re-locate by title at run time.

## Queue

- [x] instruction_set — repair the corrupted heading (article `m7_processor/instruction_set/index.md`, 139 ln)
  - Note: live defect — `## ARM=-0987654321   yhn 4esx1` under §1 指令集总结; replace with a proper heading (or drop if it duplicates §1). Content alignment to the Armv7-M instruction chapters is tracked in [ARMv7-M](ARMv7-M.md); this row is the 1-line hygiene fix only, can ride any other M7 row's PR.
  - [x] S1 (heading target) [x] S2 [x] S5 [x] S8
- [x] nvic — completion (M7 TRM ch7 NVIC, 242 ln; article = 26-ln stub `m7_processor/nested_vectored_interrupt_controller/`)
  - Note (S1): source ch7 L4404–4645; architectural cross-check Armv7-M B3.4 NVIC (`.private/ARM/M7/DDI0403E_e_armv7m_arm.md`, B3 = L34504–38282). TRM = implementation (priorities, interrupt interfaces), ARM = architectural rules; state the choice in the PR.
  - Note: `docs/cortex/index.md` M7 list misses the NVIC link — add in this run (skill Step 7). mkdocs nav already registers the page.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] program_status_register — completion/alignment (M7 TRM ch2.6 Processor core registers + ch2.7 Exceptions; article 86 ln `m7_processor/program_status_register/`)
  - Note (S1): TRM ch2 L1105–1343; cross-check Armv7-M B1.4 Registers (mapping.md's "B1.2" evidence predates the current mirror). 6 legacy images — verify against the r1p2 PDF before re-cropping; keep file names.
  - [x] S1 [x] S2 [x] S3 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch3 → new article `m7_processor/system_control/` (System Control, 665 ln — register summary + register descriptions; naming collides with `r52p_processor/system_control/` only in text, different tree, OK)
  - [x] S1 [x] S2 [x] S3 [x] S4 (new nav entry) [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch4 → new article (Initialization, 263 ln; directory name proposed at S1, e.g. `initialization/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch6 → new article (Memory Protection Unit, 206 ln; e.g. `mpu/` — distinct from the Armv7-M PMSAv7 article)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch8 → new article (Floating Point Unit, 252 ln; e.g. `fpu/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [ ] ⏸ ch5 → new article (Memory System, 1,926 ln, sections 5.1–5.7 incl. AXIM/AHBP/AHBS interfaces — >1500-line rule: present the run plan first)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [x] ch9 → new article (Debug, 689 ln; e.g. `debug/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch10 → new article (Cross Trigger Interface, 482 ln; e.g. `cti/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch11 → new article (Data Watchpoint and Trace Unit, 382 ln; e.g. `dwt/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch12 → new article (Instrumentation Trace Macrocell Unit, 288 ln; e.g. `itm/`)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [ ] ch14 → new article (Fault detection and handling, 900 ln; e.g. `fault_detection/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ch13 → new article (Trace Port Interface Unit, 1,140 ln; e.g. `tpiu/`)
  - [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [x] ch1 → new article (Introduction — about the processor, component blocks, configuration options, 623 ln; lowest value, last in this group; propose `introduction/` or fold its §1.2 Component blocks into an existing article at the gate)
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8

## Not queued (deliberately)

- ch7 NVIC as a NEW article — covered by the `nvic` completion row above (same chapter).
- Appendix A Revisions + glossary tail (after ch14) — document chrome per skill Step 3.
