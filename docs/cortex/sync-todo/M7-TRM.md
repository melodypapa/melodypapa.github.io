# Sync todo: Group M7-TRM — DDI0489F Cortex-M7 TRM r1p2 (`reference-docs/arm/cortex-m7/DDI0489F_cortex_m7_trm.md`, 4,934 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Last run: 2026-11-18 — full-document verification against the refreshed parse (queue already complete).
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the TRM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (refreshed parse, 2026-11-18): ch1 Introduction L364–835 (472) · ch2 Programmers Model L836–1027 (192) · ch3 System Control L1028–1766 (739) · ch4 Initialization L1767–1927 (161) · ch5 Memory System L1928–3318 (1,391) · ch6 MPU L3319–3386 (68) · ch7 NVIC L3387–3488 (102) · ch8 FPU L3489–3592 (104) · ch9 Debug L3593–3837 (245) · ch10 CTI L3838–3953 (116) · ch11 DWT L3954–4056 (103) · ch12 ITM L4057–4168 (112) · ch13 TPIU L4169–4672 (504) · ch14 Fault detection L4673–4821 (149) · Appendix A Revisions L4822–4935 (114). All chapters carry a `## Chapter <n>` marker in this parse (ch7, ch10, ch14 without a trailing title); the older 8,778-line parse was replaced and its spans are obsolete.

## Queue

- [x] instruction_set — repair the corrupted heading (article `m7-trm/instruction_set/index.md`, 139 ln)
  - Note: live defect — `## ARM=-0987654321   yhn 4esx1` under §1 指令集总结; replace with a proper heading (or drop if it duplicates §1). Content alignment to the Armv7-M instruction chapters is tracked in [ARMv7-M](ARMv7-M.md); this row is the 1-line hygiene fix only, can ride any other M7 row's PR.
  - S8 result: shipped as `d160f99`.
  - [x] S1 (heading target) [x] S2 [x] S3 (N/A: no figures) [x] S4 (N/A: page already registered) [x] S5 [x] S6 (N/A: one-line hygiene fix) [x] S7 [x] S8
- [x] nvic — completion (M7 TRM ch7 NVIC, 242 ln; article = 26-ln stub `m7-trm/nested_vectored_interrupt_controller/`)
  - Note (S1): source ch7 L4404–4645; architectural cross-check Armv7-M B3.4 NVIC (`private-docs/ARM/M7/DDI0403E_e_armv7m_arm.md`, B3 = L34504–38282). TRM = implementation (priorities, interrupt interfaces), ARM = architectural rules; state the choice in the PR.
  - Note: `docs/cortex/index.md` M7 list misses the NVIC link — add in this run (skill Step 7). mkdocs nav already registers the page.
  - S8 result: shipped as `aca78d7`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] program_status_register — completion/alignment (M7 TRM ch2.6 Processor core registers + ch2.7 Exceptions; article 86 ln `m7-trm/program_status_register/`)
  - Note: merged with `exception_model` into one-per-chapter article `m7-trm/programmers_model/` on 2026-11-06.
  - Note (S1): TRM ch2 L1105–1343; cross-check Armv7-M B1.4 Registers (mapping.md's "B1.2" evidence predates the current mirror). 6 legacy images — verify against the r1p2 PDF before re-cropping; keep file names.
  - S8 result: shipped as `853df31`.
  - [x] S1 [x] S2 [x] S3 [x] S4 (N/A: merged into the existing programmers_model page) [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch3 → new article `m7-trm/system_control/` (System Control, 665 ln — register summary + register descriptions; naming collides with `r52plus-trm/system_control/` only in text, different tree, OK)
  - S8 result: shipped as `be6a7c5`.
  - [x] S1 [x] S2 [x] S3 [x] S4 (new nav entry) [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch4 → new article (Initialization, 263 ln; directory name proposed at S1, e.g. `initialization/`)
  - S8 result: shipped as `b25aefb`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch6 → new article (Memory Protection Unit, 206 ln; e.g. `mpu/` — distinct from the Armv7-M PMSAv7 article)
  - Note: the Armv7-M PMSAv7 article was merged into `m7-trm/mpu/` (sections 4–14) on 2026-11-06.
  - S8 result: shipped as `6d8fbec`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch8 → new article (Floating Point Unit, 252 ln; e.g. `fpu/`)
  - S8 result: shipped as `319551a`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch5 → new article (Memory System, 1,926 ln, sections 5.1–5.9 incl. AXIM/AHBP/AHBS interfaces; `memory_system/`)
  - S8 result: shipped as `898f8b0`.
  - [x] plan gate (whole-chapter translation approved) [x] S1 [x] S2 [x] S3 (no figures, 38 tables as GFM) [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch9 → new article (Debug, 689 ln; e.g. `debug/`)
  - S8 result: shipped as `bb45fd6`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch10 → new article (Cross Trigger Interface, 482 ln; e.g. `cti/`)
  - S8 result: shipped as `6fec217`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch11 → new article (Data Watchpoint and Trace Unit, 382 ln; e.g. `dwt/`)
  - S8 result: shipped as `d44f6bd`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch12 → new article (Instrumentation Trace Macrocell Unit, 288 ln; e.g. `itm/`)
  - S8 result: shipped as `4e4131f`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch14 → new article (Fault detection and handling, 900 ln; `fault_detection/`)
  - S8 result: shipped as `91d6243`.
  - [x] S1 [x] S2 [x] S3 (no figures, tables 14-1/14-2 as GFM) [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch13 → new article (Trace Port Interface Unit, 1,140 ln; `tpiu/`)
  - S8 result: shipped as `1a13e66`.
  - [x] S1 [x] S2 [x] S3 (Figure13-1…13-12, 12 tables as GFM) [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] ch1 → new article (Introduction — about the processor, component blocks, configuration options, 623 ln; lowest value, last in this group; propose `introduction/` or fold its §1.2 Component blocks into an existing article at the gate)
  - S8 result: shipped as `4c13559`.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8

## Not queued (deliberately)

- ch7 NVIC as a NEW article — covered by the `nvic` completion row above (same chapter).
- Appendix A Revisions + glossary tail (after ch14) — document chrome per skill Step 3.

## Verification (2026-11-18, refreshed parse)

Full-document check against `reference-docs/arm/cortex-m7/DDI0489F_cortex_m7_trm.md` after the corpus re-parse. Section counts and figure/table sets align; no article change was needed.

| Chapter | Source sections | Article headings | Source fig / table | Article img / GFM table |
| --- | --- | --- | --- | --- |
| ch1 Introduction | 37 | 7 `##` + 30 `###` | 3 / 1 | 3 / 1 |
| ch2 Programmers Model | 14 | 31 `##` + 60 `###` | 1 / 1 | 7 / 18 |
| ch3 System Control | 15 | 3 `##` + 12 `###` | 12 / 15 | 12 / 15 |
| ch4 Initialization | 9 | 1 `##` + 8 `###` | 0 / 0 | 0 / 0 |
| ch5 Memory System | 36 | 9 `##` + 27 `###` | 0 / 38 | 0 / 38 |
| ch6 MPU | 2 | 14 `##` + 18 `###` | 0 / 1 | 5 / 7 |
| ch7 NVIC | 6 | 3 `##` + 3 `###` | 1 / 2 | 1 / 2 |
| ch8 FPU | 6 | 3 `##` + 3 `###` | 0 / 2 | 0 / 2 |
| ch9 Debug | 9 | 3 `##` + 6 `###` | 1 / 7 | 1 / 7 |
| ch10 CTI | 3 | 3 `##` | 1 / 3 | 1 / 3 |
| ch11 DWT | 3 | 3 `##` | 0 / 1 | 0 / 1 |
| ch12 ITM | 4 | 3 `##` + 1 `###` | 1 / 2 | 1 / 2 |
| ch13 TPIU | 16 | 3 `##` + 14 `###` | 12 / 12 | 12 / 12 |
| ch14 Fault detection | 10 | 3 `##` + 7 `###` | 0 / 2 | 0 / 2 |

- ch6 MPU and ch2 Programmers Model exceed the source counts by design: the merged PMSAv7 and Armv7-M material recorded in the rows above.
- ch9 table count matches after de-duplicating the source's `Table 9-7 (continued)` repeat.
- The source glossary chapter is a pointer to the Arm Glossary only (no local term rows), so `m7-trm/glossary/` correctly stays a link-only page.
