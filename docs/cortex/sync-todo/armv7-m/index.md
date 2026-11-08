# Sync todo: Group ARMv7-M — DDI0403E Armv7-M ARM E.e (`M7/DDI0403E_e_armv7m_arm.md`, 51,102 ln, PDF ✅)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Chapter span map (parse lines): Part A L739 — A1 Introduction L743–880 (137) · A2 The Application Level Model L880–4060 (3,180, ⏸) · A3 The Memory Model L4060–6099 (2,039, ⏸) · A4 The Armv7-M Instruction Set L6099–7082 (983) · A5 The Thumb Instruction Set Encoding L7082–8272 (1,190) · A6 The Floating-point Instruction Set Encoding L8272–8634 (362) · A7 Instruction Details L8634–28616 (19,982, ⏸ deferred). Part B L28620 — B1 System Level Programmers' Model L28620–32964 (4,344, ⏸; B1.5 = Armv7-M exception model) · B2 System Memory Model L32964–34504 (1,540) · B3 System Address Map L34504–38282 (3,778, ⏸; B3.5 = PMSAv7) · B4 The CPUID Scheme L38282–39914 (1,632) · B5 System Instruction Details L39914–40432 (518). Part C Debug Architecture — C1 Armv7-M Debug L40436–46188 (5,752, ⏸ deferred). Part D Appendixes — D1 CoreSight Infrastructure IDs … D8 Register Index, L46192–end (deferred).

Existing-article mappings (mapping.md, evidence re-checked at census): `arm_architecture_memory_mode` ← A3 · `programmers_model` ← B1.5 (evidence `Figure2-*` unverified — confirm at S1) · `mpu` ← B3.5 (`TableB3-1…11`) · `system_address_map` ← B3.1–B3.4 (article sections SCS/SysTick/NVIC = B3.2/B3.3/B3.4) · `instruction_set` ← A4 (completed 2026-11-08, appended to the TRM summary); A5 and A6 are separate articles, queued below.

> **Layout:** one folder per source document, one file per source chapter. This `index.md` carries the document-level material; every queue row (title, notes, `- Sx result:` bullets, S1–S8 step line) lives on its own chapter file. The previous single-file ledger was `ARMv7-M.md`.

## Chapter files

Listed in **queue order** — resume = the first `[ ]` row in this order.

| # | Chapter | File | Queue row | State |
| --- | --- | --- | --- | --- |
| 1 | B1.5 Exception model | [b1.5-exception-model](b1.5-exception-model.md) | `exception_model` | complete |
| 2 | B3.5 PMSAv7 | [b3.5-pmsav7](b3.5-pmsav7.md) | `protected_memory_system_archi_pmsav7` | complete |
| 3 | B3.1–B3.4 System address map | [b3.1-b3.4-system-address-map](b3.1-b3.4-system-address-map.md) | `system_address_map` | complete |
| 4 | A3 The Memory Model | [a3-memory-model](a3-memory-model.md) | `arm_architecture_memory_mode` | complete |
| 5 | A4 The Armv7-M Instruction Set | [a4-instruction-set](a4-instruction-set.md) | `instruction_set` | complete |
| 6 | A5 The Thumb Instruction Set Encoding | [a5-thumb-encoding](a5-thumb-encoding.md) | `A5` | complete |
| 7 | A6 The Floating-point Instruction Set Encoding | [a6-fp-encoding](a6-fp-encoding.md) | `A6` | complete |
| 8 | B2 System Memory Model | [b2-system-memory-model](b2-system-memory-model.md) | `B2` | complete |
| 9 | B4 The CPUID Scheme | [b4-cpuid](b4-cpuid.md) | `B4` | complete |
| 10 | B5 System Instruction Details | [b5-system-instructions](b5-system-instructions.md) | `B5` | complete |

## Not queued (deliberately deferred)

- A1 Introduction (137 ln), A2 The Application Level Model (3,180 ln), A7 Instruction Details (19,982 ln), C1 Armv7-M Debug (5,752 ln — overlaps the M7 TRM debug chapters; prefer the TRM for implementation), D1–D8 appendixes (pseudocode/register indexes) — start on explicit request only.
