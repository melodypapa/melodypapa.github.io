# Sync todo: Group ARMv8-M — DDI0553B Armv8-M ARM B.y (`reference-docs/arm/cortex-r52/DDI0553B_y_armv8m_arm.md`, 37,382 ln, PDF ✅)

Generated: 2026-11-04 · Opened: 2026-11-10 · **Status: ACTIVE** — the M-profile architecture series `docs/cortex/armv8-m/` is open; Part A chapter A1 is translated and registered. Queue order = row order (resume = the first row still `[ ]`).
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Pairing note: the file lives under `cortex-r52/` in the mirror but documents the **Armv8-M (M-profile)** architecture. The Cortex-R52+ is **Armv8-R AArch32**, so DDI0553B is NOT the R52+ architecture manual; it is a separate M-profile series. The PDF is complete (9,561,121 B = ima media_size — the README "⏳ retrying" row is stale; there is no README on disk, the pairing ledger is the `sync-todo/index.md` Sources table).

Chapter span map (parse lines): Part A L3834–4284 — A1 Introduction, 451 ln (translated). Part B L4285–~33105 — B1 Resets from L4288, B2 Power Management from L4339, B3 Programmers' Model from L4548; B4–B16 body boundaries are located by title at S1 because the parse interleaves TOC entries, running page headers and `# Bn.y`/`Chapter Bn` headings. The TOC at L225–L715 is the authoritative B1–B16 chapter list. Part C body begins ~L33106, followed by Parts D/E/F/G. Front matter L1–3833 (cover, proprietary notice, document history, contents, preface, feedback) is droppable chrome.

## Inventory (TOC = authoritative chapter list)

| Part | Chapters | Content | Status |
| --- | --- | --- | --- |
| A | A1 Introduction | overview of the architecture and its profiles | A1 done |
| B | B1 Resets · B2 Power Management · B3 Programmers' Model · B4 Floating-point Support · B5 Vector Extension · B6 Pointer Authentication / BTI Extension · B7 Memory Model · B8 The System Address Map · B9 Synchronization and Semaphores · B10 The Armv8-M Protected Memory System Architecture · B11 The System Timer, SysTick · B12 Nested Vectored Interrupt Controller · B13 Debug · B14 Debug and Trace Components · B15 The Performance Monitors Extension · B16 RAS Extension | architecture rules | queued below |
| C | C1–C2 | instruction set + alphabetical instruction specification | deferred (reference) |
| D | D1+ | registers and payload specification | deferred (reference) |
| E | E1–E2 | pseudocode | deferred (reference) |
| F | F1 | debug packet protocols | deferred (reference) |
| G | — | glossary | deferred (chrome) |

Parts C/D/E/F/G are reference material (instruction encodings, register payloads, pseudocode) — queued Parts A/B chapter-by-chapter first; C–G are deliberately deferred the way [ARMv7-M](ARMv7-M.md) defers its tail.

## Queue

All Part B rows carry ⏸: measure the parse span at S1, and any chapter over ~1500 lines needs the per-run plan gate before translating.

- [x] A1 → new article `armv8-m/introduction/` (Introduction, 451 ln; 1 figure, 0 tables)
  - S1 result: Part A has exactly one chapter A1 (no A2); body L3834–4284. Census: 1 caption-less Mermaid rule-anatomy diagram (source L3862), 0 tables. All chrome is outside A1 (L1–3833); running page headers, the duplicate heading L3883 and the duplicate sentence L4010 were dropped. The intro's "It contains the following sections" list (L3842–3846) was dropped as a redundant section list that omits A1.4. ARMv7-M deliberately deferred its own A1, but this standalone architecture series has no TRM intro page, so A1 is the orientation chapter.
  - S2 result: article written in place; numbering restarts at 1 (`## 1` ← A1.1, `### 1.1`–`### 1.5` ← A1.1.1–A1.1.5, `## 2` ← A1.2, `## 3` ← A1.3 with `### 3.1`–`### 3.3`, `## 4` ← A1.4 with `### 4.1`–`### 4.13`). Seven terminology items and three architecture profiles kept as bold body runs; HP half-precision kept as a bold run under §4.5; four Note blocks rendered as `**注意：**`. OCR artifacts verified against the PDF text layer ("an MPU" and "optional MPU" in A1.4.7; "Digital Signal Procession" is a source typo). No `# ` in the body.
  - S3 result: `FigureA1-1.png` cropped from PDF page 49 at 3× with an 11.65 pt margin (synthetic number — the source has no `Figure A1-n` caption); embedded with a lead-in sentence.
  - S4 result: nav group `Armv8-M 架构参考手册` added at source position after Cortex-R52+ TRM; landing `armv8-m/index.md` created; `docs/cortex/index.md` §4 added.
  - S5 result: `--strict` build 0 WARNINGs; `check_indexes.py --root .` OK; `check_heading_lang.py` OK on both new pages.
  - S6 result: 1 figure present, 0 tables; 4 sections and 21 numbered subsections all present; no untranslated English paragraph; numbering continuity 1.1–1.5 / 2 / 3.1–3.3 / 4.1–4.13.
  - S7 result: confirmed by the user (plan approval 2026-11-10).
  - S8 result: shipped with `Closes #361` in this PR; merge SHA and PR number to be recorded post-merge per the ledger convention.
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B1 resets — new article (article 55 ln, 1 `##` vs 7 rules)
  - S1 result: Part B opens at L4285; B1 body L4288–4337 with the single section B1.1 "Resets, Cold reset, and Warm reset" (seven rules), then the chapter's See also list (B13, B16). Census: 0 figures, 0 tables. The chapter-front "It contains the following section" list was dropped as a redundant section list (A1 precedent); the random rule IDs (`R_BDPL` …) are not rendered, matching the existing `armv7-m/` and `armv8-m/` articles.
  - S2 result: `docs/cortex/armv8-m/resets/index.md`; numbering restarts at 1 (`## 1.` ← B1.1); each rule keeps its `适用于 **Armv8.0-M** 及以后架构版本的实现。` line verbatim; `TakeReset()` kept in a code span; the See also block rendered as `参见：` bullets. No `# ` in the body.
  - S3 result: N/A — the chapter has no figures.
  - S4 result: nav entry `"复位"` after 简介 in the Armv8-M group; landing list entry 2.
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` 0 broken links; heading-language check OK.
  - S6 result: 7/7 rules present in source order with no dropped applicability line; 0 figures, 0 tables; numbering continuity (`## 1.` only).
  - S7 result: PR opened, awaiting user confirmation.
  - S8 result: PR #364 (merge SHA to be recorded post-merge).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [ ] S7 [x] S8
- [ ] ⏸ B2 → new article (Power Management; body from L4339; e.g. `power_management/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B3 → new article (Programmers' Model; body from L4548; e.g. `programmers_model/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B4 → new article (Floating-point Support; e.g. `floating_point_support/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B5 → new article (Vector Extension; e.g. `vector_extension/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B6 → new article (Pointer Authentication and Branch Target Identification Extension; e.g. `pacbti/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B7 → new article (Memory Model; e.g. `memory_model/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B8 → new article (The System Address Map; e.g. `system_address_map/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B9 → new article (Synchronization and Semaphores; e.g. `synchronization_and_semaphores/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B10 → new article (The Armv8-M Protected Memory System Architecture; e.g. `protected_memory_system_architecture/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B11 → new article (The System Timer, SysTick; e.g. `system_timer_systick/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B12 → new article (Nested Vectored Interrupt Controller; e.g. `nested_vectored_interrupt_controller/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B13 → new article (Debug; e.g. `debug/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B14 → new article (Debug and Trace Components; e.g. `debug_and_trace_components/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B15 → new article (The Performance Monitors Extension; e.g. `performance_monitors_extension/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8
- [ ] ⏸ B16 → new article (Reliability, Availability, and Serviceability (RAS) Extension; e.g. `ras_extension/`)
  - [ ] plan gate [ ] S1 [ ] S2 [ ] S3 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately deferred)

- Part C Armv8-M Instruction Set (C1–C2, instruction encodings and alphabetical instruction specification), Part D Armv8-M Registers and Payload Specification, Part E Armv8-M Pseudocode, Part F Debug Packet Protocols, Part G Glossary — reference/chrome material, start on explicit request only. A1.1.1 notes that architectural rules in these parts are not identified by a rule prefix and random subscript letters.
