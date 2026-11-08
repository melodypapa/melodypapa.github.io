# Sync todo: Group R52-TRM — Cortex-R52 TRM r1p0 (`R52/cortex_r52_trm_100026_0100_00_en.md`, 44,511 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the TRM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines, incl. running headers — re-locate by title, first occurrence wins): ch1 Introduction L694–1370 (677) · ch2 Programmers Model L1371–1849 (479) · ch3 System Control L1850–12962 (~11.1k, ⏸) · ch4 Clocking and Resets L12963–13326 (364) · ch5 Power Management L13327–13946 (620) · ch6 Initialization L13947–14250 (304) · ch7 Memory System L14251–17182 (2,932, ⏸) · ch8 MPU L17183–17952 (770) · ch9 GIC L17953–27056 (9,104, ⏸) · ch10 Generic Timer L27057–27400 (344) · ch11 Debug L27401–32260 (4,860, ⏸) · ch12 PMU L32261–35485 (3,225, ⏸) · ch13 Cross Trigger L35486–37043 (1,558) · ch14 ETM L37044–… (⏸) · ch15 Advanced SIMD and floating-point support (tail; no reliable marker — locate by title) · Appendices A–D (Signal Descriptions / Cycle Timings / UNPREDICTABLE / Revisions — tail).

**Legacy revision shift:** `references/mapping.md` evidence for `programmers_model` (`Table3-1`) and `system_control` (`Table4-48`, "ch4 System Control") predates r1p0 — in this mirror Programmers Model = **ch2**, System Control = **ch3**. Legacy images (`Figure8_*` in memory_system, `Table9-*` in memory_protection_unit) carry old chapter numbers; keep the files, verify by caption text.

> **Layout:** one folder per source document, one file per source chapter. This `index.md` carries the document-level material; every queue row (title, notes, `- Sx result:` bullets, S1–S8 step line) lives on its own chapter file. The previous single-file ledger was `R52-TRM.md`.

## Chapter files

Listed in **queue order** — resume = the first `[ ]` row in this order.

| # | Chapter | File | Queue row | State |
| --- | --- | --- | --- | --- |
| 1 | ch2 Programmers Model | [ch02-programmers-model](ch02-programmers-model.md) | `programmers_model` | open |
| 2 | ch8 Memory Protection Unit | [ch08-mpu](ch08-mpu.md) | `memory_protection_unit` | open |
| 3 | ch7 Memory System | [ch07-memory-system](ch07-memory-system.md) | `memory_system` | open |
| 4 | ch3 System Control | [ch03-system-control](ch03-system-control.md) | `system_control` | ⏸ gated |
| 5 | ch4 Clocking and Resets | [ch04-clocking-and-resets](ch04-clocking-and-resets.md) | `ch4` | open |
| 6 | ch6 Initialization | [ch06-initialization](ch06-initialization.md) | `ch6` | complete |
| 7 | ch5 Power Management | [ch05-power-management](ch05-power-management.md) | `ch5` | open |
| 8 | ch10 Generic Timer | [ch10-generic-timer](ch10-generic-timer.md) | `ch10` | open |
| 9 | ch13 Cross Trigger | [ch13-cross-trigger](ch13-cross-trigger.md) | `ch13` | open |
| 10 | ch1 Introduction | [ch01-introduction](ch01-introduction.md) | `ch1` | open |
| 11 | ch12 Performance Monitor Unit | [ch12-pmu](ch12-pmu.md) | `ch12` | ⏸ gated |
| 12 | ch11 Debug | [ch11-debug](ch11-debug.md) | `ch11` | ⏸ gated |
| 13 | ch14 Embedded Trace Macrocell | [ch14-etm](ch14-etm.md) | `ch14` | ⏸ gated |
| 14 | ch9 Generic Interrupt Controller | [ch09-gic](ch09-gic.md) | `ch9` | ⏸ gated |
| 15 | ch15 Advanced SIMD and floating-point support | [ch15-asimd-floating-point](ch15-asimd-floating-point.md) | `ch15` | open |

## Not queued (deliberately)

- Appendices A–D (Signal Descriptions, Cycle Timings and Interlock Behavior, Processor UNPREDICTABLE Behaviors, Revisions) — reference/chrome material; revisit on explicit request.
- `R52/DDI0553B_y_armv8m_arm.md` — see [ARMv8-M](../armv8-m/index.md) (deferred group).
