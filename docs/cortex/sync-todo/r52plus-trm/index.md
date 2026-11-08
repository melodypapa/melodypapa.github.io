# Sync todo: Group R52plus-TRM — Cortex-R52+ TRM 102199_0001_03 (`arm_cortex_r52plus_processor_trm_102199_0001_03_en.pdf`, 719 pp, PDF only)

Generated: 2026-11-07 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the same PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

**Source shape:** this document has **no ima Markdown parse** — the PDF text layer is the only source, so the "never translate from the PDF when a `.md` exists" rule does not apply here. Crops and table cells come from the same PDF. Section numbers below are the R52+ ones; the older [R52-TRM](../r52-trm/index.md) group follows `100026` and numbers the same chapters two lower (Programmers Model ch2, System Control ch3, Clocking ch4, Initialization ch6, Memory System ch7, MPU ch8).

Chapter span map (PDF pages): ch1 Introduction 24–27 (4) · ch2 The Cortex-R52+ processor 28–44 (17) · ch3 Programmers Model 45–53 (9) · ch4 System Control 54–218 (165) · ch5 Clocking and Resets 219–222 (4) · ch6 Power Management 223–230 (8) · ch7 Initialization 231–235 (5) · ch8 Memory System 236–275 (40) · ch9 Memory Protection Unit 276–283 (8) · ch10 Generic Interrupt Controller 284–382 (99) · ch11 Generic Timer 383–385 (3) · ch12 Debug 386–435 (50) · ch13 Performance Monitor Unit 436–462 (27) · ch14 Cross Trigger 463–479 (17) · ch15 Embedded Trace Macrocell 480–563 (84) · ch16 Advanced SIMD and floating-point support 564–575 (12) · A Signal Descriptions 576–615 (40) · B Cycle Timings and Interlock Behavior 616–638 (23) · C Processor UNPREDICTABLE Behaviors 639–652 (14) · D PMC-R52+ 653–715 (63) · E Revisions 716–719 (4).

> **Layout:** one folder per source document, one file per source chapter. This `index.md` carries the document-level material; every queue row (title, notes, `- Sx result:` bullets, S1–S8 step line) lives on its own chapter file. The previous single-file ledger was `R52plus-TRM.md`.

## Chapter files

Listed in **queue order** — resume = the first `[ ]` row in this order.

| # | Chapter | File | Queue row | State |
| --- | --- | --- | --- | --- |
| 1 | ch3 Programmers Model | [ch03-programmers-model](ch03-programmers-model.md) | `ch3` | open |
| 2 | ch5 Clocking and Resets | [ch05-clocking-and-resets](ch05-clocking-and-resets.md) | `ch5` | open |
| 3 | ch7 Initialization | [ch07-initialization](ch07-initialization.md) | `ch7` | open |
| 4 | ch8 Memory System | [ch08-memory-system](ch08-memory-system.md) | `ch8` | open |
| 5 | ch9 Memory Protection Unit | [ch09-mpu](ch09-mpu.md) | `ch9` | open |
| 6 | ch4 System Control | [ch04-system-control](ch04-system-control.md) | `ch4` | ⏸ gated |
| 7 | ch11 Generic Timer | [ch11-generic-timer](ch11-generic-timer.md) | `ch11` | open |
| 8 | ch1 Introduction | [ch01-introduction](ch01-introduction.md) | `ch1` | open |
| 9 | ch6 Power Management | [ch06-power-management](ch06-power-management.md) | `ch6` | open |
| 10 | ch16 Advanced SIMD and floating-point support | [ch16-asimd-floating-point](ch16-asimd-floating-point.md) | `ch16` | open |
| 11 | ch2 The Cortex-R52+ processor | [ch02-the-cortex-r52plus-processor](ch02-the-cortex-r52plus-processor.md) | `ch2` | open |
| 12 | ch14 Cross Trigger | [ch14-cross-trigger](ch14-cross-trigger.md) | `ch14` | open |
| 13 | Appendix D PMC-R52+ | [appendix-d-pmc-r52plus](appendix-d-pmc-r52plus.md) | `D` | open |
| 14 | ch13 Performance Monitor Unit | [ch13-pmu](ch13-pmu.md) | `ch13` | ⏸ gated |
| 15 | ch12 Debug | [ch12-debug](ch12-debug.md) | `ch12` | ⏸ gated |
| 16 | ch10 Generic Interrupt Controller | [ch10-gic](ch10-gic.md) | `ch10` | ⏸ gated |
| 17 | ch15 Embedded Trace Macrocell | [ch15-etm](ch15-etm.md) | `ch15` | ⏸ gated |

## Not queued (deliberately)

- A Signal Descriptions (40 pp signal tables), B Cycle Timings and Interlock Behavior, C Processor UNPREDICTABLE Behaviors, E Revisions — reference/chrome material per skill Step 3; revisit on explicit request. Appendix A overlaps `clocking_and_resets` (clock/reset signals) and the interface chapters (AXIM/AXIS/LLPP/Flash signal groups).
- The document glossary and cover/proprietary notice — chrome.
