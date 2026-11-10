# Sync todo: Group ARMv8-M — DDI0553B Armv8-M ARM B.y (`reference-docs/arm/cortex-r52/DDI0553B_y_armv8m_arm.md`, 37,382 ln, PDF ✅)

Generated: 2026-11-04 · Opened: 2026-11-10 · **Status: ACTIVE** — the M-profile architecture series `docs/cortex/armv8-m/` is open; Part A chapter A1 is translated and registered. Queue order = row order (resume = the first row still `[ ]`).
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures (PyMuPDF crop from the ARM PDF) · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

Pairing note: the file lives under `cortex-r52/` in the mirror but documents the **Armv8-M (M-profile)** architecture. The Cortex-R52+ is **Armv8-R AArch32**, so DDI0553B is NOT the R52+ architecture manual; it is a separate M-profile series. The PDF is complete (9,561,121 B = ima media_size — the README "⏳ retrying" row is stale; there is no README on disk, the pairing ledger is the `sync-todo/index.md` Sources table).

Chapter span map (parse lines): Part A L3834–4284 — A1 Introduction, 451 ln (translated). Part B L4285–~33105 — B1 Resets from L4288, B2 Power Management from L4339, B3 Programmers' Model from L4548; B4–B16 body boundaries are located by title at S1 because the parse interleaves TOC entries, running page headers and `# Bn.y`/`Chapter Bn` headings. The TOC at L225–L715 is the authoritative B1–B16 chapter list. Part C body begins ~L33106, followed by Parts D/E/F/G. Front matter L1–3833 (cover, proprietary notice, document history, contents, preface, feedback) is droppable chrome.

## Inventory (TOC = authoritative chapter list)

| Part | Chapters | Content | Status |
| --- | --- | --- | --- |
| A | A1 Introduction | overview of the architecture and its profiles | A1 done |
| B | B1 Resets · B2 Power Management · B3 Programmers' Model · B4 Floating-point Support · B5 Vector Extension · B6 Pointer Authentication / BTI Extension · B7 Memory Model · B8 The System Address Map · B9 Synchronization and Semaphores · B10 The Armv8-M Protected Memory System Architecture · B11 The System Timer, SysTick · B12 Nested Vectored Interrupt Controller · B13 Debug · B14 Debug and Trace Components · B15 The Performance Monitors Extension · B16 RAS Extension | architecture rules | B1–B9 done; B10–B16 queued below |
| C | C1–C2 | instruction set + alphabetical instruction specification | deferred (reference) |
| D | D1+ | registers and payload specification | deferred (reference) |
| E | E1–E2 | pseudocode | deferred (reference) |
| F | F1 | debug packet protocols | deferred (reference) |
| G | — | glossary | G done — `docs/cortex/armv8-m/glossary/index.md`, 285 entries, PDF pp. 2122–2148 |

Parts C/D/E/F are reference material (instruction encodings, register payloads, pseudocode) — queued Parts A/B chapter-by-chapter first; they are deliberately deferred the way [ARMv7-M](ARMv7-M.md) defers its tail. Part G (glossary) is translated and registered.

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
- [x] B2 → new article `armv8-m/power_management/` (Power Management; body L4339–4546)
  - S1 result: B2 body L4339–4546: B2.1 "Power management" (12 rules) with B2.1.1 WFE and B2.1.2 WFI, then B2.2 "Sleep on exit" (4 rules). Census: 0 figures, 0 tables. The chapter-front section list was dropped (A1/B1 precedent). Two parse OCR artifacts were checked against PDF pp. 63–66 and corrected in translation: "WFE makeup event" → "WFE wakeup event", "unprovided debug" → "unprivileged debug".
  - S2 result: `docs/cortex/armv8-m/power_management/index.md`; numbering restarts at 1 (`## 1.` ← B2.1 with `### 1.1`/`### 1.2` ← B2.1.1/B2.1.2, `## 2.` ← B2.2); every rule keeps its applicability line, the Armv8.1-M rule keeps `扩展要求为 - DB && UDE。`, and the `DB` rule carries the source's DebugMonitor note; both See also blocks rendered as `参见：` bullets. No `# ` in the body.
  - S3 result: N/A — the chapter has no figures.
  - S4 result: nav entry `"电源管理"` after 复位 in the Armv8-M group; landing list entry 3.
  - S5 result: strict build 0 WARNING; index checks 0 broken links; heading-language check OK.
  - S6 result: 12/12 B2.1 rules and 4/4 B2.2 rules present in source order; both subsections present; 0 figures, 0 tables; numbering continuity 1–1.2/2.
  - S7 result: covered by the user-approved single-loop run; the confirmation gate is taken once at the end of B2–B16.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (PR #364).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B3 → new article `armv8-m/programmers_model/` (Programmers' Model; body from L4548; PDF pp. 87–158)
  - S1 result: B3 has 37 sections (B3.1–B3.37) with sub-sections B3.27.1–B3.27.7 and B3.37.1–B3.37.3. The `.md` parse is disordered for B3 (content misplaced across the chapter), so the translation was taken from the PDF text layer page by page with the PDF page index = printed page − 1. Census: 9 content figures (B3.5 XPSR, B3.13 priority mapping, B3.16 call stack frame, B3.17 FNC_RETURN bar, B3.19 exception stack frame, B3.23 integrity signature, B3.26 three tail-chaining timing diagrams), 6 tables (B3.5 MRS/MSR mnemonics, B3.13 PRIGROUP and the 0x00–0xFE mapping, B3.14 NS attribute, B3.19/B3.21 stack-limit register sets, B3.27 EPSR.ICI, B3.28 LO_BRANCH_INFO, B3.30 vector table).
  - S2 result: `docs/cortex/armv8-m/programmers_model/index.md`, 3423 ln; numbering restarts at 1 (`## 1.` ← B3.1 … `## 37.` ← B3.37, `### 27.1`–`### 27.7`, `### 37.1`–`### 37.3`); every rule keeps its applicability line and the source's extension requirement (`- S`, `- M`, `- FP || MVE`, `- CDE && MVE && LOB`, …) with source notes appended as `注意，…。`; all See-also blocks rendered as `参见：` bullets; the `memcpy`/BF listings kept verbatim in ```arm blocks.
  - S3 result: 8 new figures cropped from the PDF at 300 dpi with a ~4 % margin per side — `FigureB3-5.png` (B3.19 stack frame), `FigureB3-6.png` (B3.23 integrity signature, both bars), `FigureB3-7/8/9.png` (B3.26 tail-chaining diagrams); each verified visually for clipping. No table was cropped as an image.
  - S4 result: nav entry `"编程模型"` after 电源管理 and before 术语表 in the Armv8-M group; landing list entry 4 (术语表 moved to 5).
  - S5 result: strict build 0 WARNING; index checks OK (353 nav targets, 0 broken links); heading-language check OK; 37 `##` headings 1–37 with no `# ` in the body, all 9 `![]()` targets present, no `![Table…]` images.
  - S6 result: all 37 sections present in source order with their rule groups; 9/9 figures and all tables rebuilt as GFM text; numbering continuity 1–37 and 27.1–27.7 / 37.1–37.3.
  - S7 result: covered by the user-approved single-loop run; the confirmation gate is taken once at the end of B2–B16.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (commit fbf7353).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [ ] S8
- [x] B4 → new article `armv8-m/floating_point_support/` (Floating-point Support; PDF pp. 160–176, 12 sections)
  - S1 result: B4 spans PDF pages printed 160–176 (the B5 divider is on printed 177); 12 sections B4.1–B4.12 with the single sub-section B4.8.1. The `.md` parse cannot be used for body recovery here (same interleaving as B3), so the text was taken from the PDF layer page by page. Census: 4 vector diagrams (B4.1 S/D register map, B4.2–B4.4 the half/single/double encoding bit bars) and 5 tables (B4.2 two coprocessor register maps, B4.4 terminology, B4.6 interpretation, B4.10 Default NaN). The bit bars and the Default NaN table carry no `Figure B4-n` caption in this edition — the figure numbers are synthetic, per the A1 precedent.
  - S2 result: `docs/cortex/armv8-m/floating_point_support/index.md`, 552 ln; numbering restarts at 1 (`## 1.` ← B4.1 … `## 12.` ← B4.12, `### 8.1` ← B4.8.1). 68 rule applicability lines plus the B4.8.1 section-level line match the source's `Applies to an implementation …` lines; the B4.8.1 rules keep the source's `Note, !8.0.` as `注意，不适用于 **Armv8.0-M**。`; the B4.10 spanning header ("IEEE 754-2008 interpretation" over the three format columns) is carried by the lead-in sentence rather than a merged cell; all See-also blocks render as `参见：` bullets. No `# ` in the body.
  - S3 result: 4 figures cropped from the PDF at 300 dpi — `FigureB4-1.png` (B4.3 register map), `FigureB4-2/3/4.png` (B4.6 half/single/double encoding); each verified visually for clipping. No table was cropped as an image.
  - S4 result: nav entry `"浮点支持"` after 编程模型 and before 术语表 in the Armv8-M group; landing list entry 5 (术语表 moved to 6).
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` OK (354 nav targets, 0 broken links); `check_heading_lang.py` OK (the `## 10. Default NaN` heading was retitled `## 10. Default NaN 值` to satisfy the check); 12 `##` headings 1–12 continuous, 4 `![]()` targets present, no `![Table…]` images.
  - S6 result: 12/12 sections in source order; the 5 exceptions of B4.7, the 15 B4.8 rules + 5 B4.8.1 rules, the 6 B4.9 NaN rules, the B4.10 table, the 2 B4.11 combination rules and the B4.12 priority rule are all present; 4 figures, 5 tables.
  - S7 result: covered by the user-approved single-loop run; the confirmation gate is taken once at the end of B2–B16.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (commit ffbd561).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [ ] S8
- [x] B5 → new article `armv8-m/vector_extension/` (Vector Extension; PDF pp. 177–191, 6 sections)
  - S1 result: B5 spans printed 177–191 (the B6 divider is on printed 192); 6 sections B5.1–B5.6 with sub-sections B5.5.1–B5.5.4. Census: 5 vector diagrams (B5.2 vector register file, B5.3 four lane-number rows, B5.4 beat-number bar, B5.4 dual-beat overlap timing, B5.6 VLD4 de-interleave grid) and 2 tables (B5.5.2 VPT variants, B5.5.3 lane width vs VPR.P0 bits). The Q\<n\> bit assignment on p. 180 is a numbered list (rows 1, 2, 3 = …, 4), not a table. No figure captions exist in this edition — numbering is synthetic, per the A1 precedent.
  - S2 result: `docs/cortex/armv8-m/vector_extension/index.md`, 511 ln; numbering restarts at 1 (`## 1.` ← B5.1 … `## 6.` ← B5.6, `### 5.1`–`### 5.4` ← B5.5.1–B5.5.4). 76 applicability lines match the source's 76 `Applies to an implementation …` lines exactly (12 / 4 / 2 / 16 / 38 / 4 per section); the two `Note, Debug state requires HDBG.` lines are kept as `注意，调试状态要求 **HDBG**。`; **Lanes**/**Beats** are glossed in the headings as 通道/节拍 and bolded at first use in the body; the dual-beat example keeps its two ``` blocks of three instructions. No `# ` in the body.
  - S3 result: 5 figures cropped at 300 dpi — `FigureB5-1` (register file map, recropped wider after the S-column border clipped), `FigureB5-2` (lane numbers), `FigureB5-3` (beat number), `FigureB5-4` (dual-beat timing), `FigureB5-5` (VLD4 grid); all verified visually.
  - S4 result: nav entry `"向量扩展"` after 浮点支持; landing list entry 6 (术语表 moved to 7).
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` OK (355 nav targets, 0 broken links); `check_heading_lang.py` OK; 6 `##` headings 1–6 continuous, 5 `![]()` targets present, no `![Table…]` images.
  - S6 result: 6/6 sections and 4/4 sub-sections in source order; both tables rebuilt as GFM text; the B5.1 multi-access BusFault rule pair (RFBRZ/IKPFV) kept as two rules.
  - S7 result: covered by the user-approved single-loop run; the confirmation gate is taken once at the end of B2–B16.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (commit 7405a36).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [ ] S8
- [x] B6 → new article `armv8-m/pacbti/` (Pointer authentication and branch target identification Extension; PDF pp. 192–200, 1 section + 2 sub-sections)
  - S1 result: B6 spans printed 192–200 (the B7 divider is on printed 201, body from printed 202); the chapter has a single section B6.1 "Implementing PAC and BTI" with sub-sections B6.1.1 Pointer authentication and B6.1.2 Branch target identification — there is no B6.2. The text was recovered from the PDF layer page by page (the `.md` parse interleaves TOC rows and running headers). Census: 0 figures, 1 table (the four 128-bit PAC keys, rows 特权/非特权 × columns Non-secure/Secure), 2 numbered ```arm listings (the PAC example, 36 lines; the BTI example, 53 lines). The `find_tables()` hits on printed 196/199 are the code box grids, not tables. The chapter-front "It contains the following sections" list was dropped (A1/B1 precedent).
  - S2 result: `docs/cortex/armv8-m/pacbti/index.md`; numbering restarts at 1 (`## 1.` ← B6.1, `### 1.1`/`### 1.2` ← B6.1.1/B6.1.2). 40 applicability lines match the source's 40 `Applies to an implementation …` lines (3 / 17 / 20 per section); the two `- PACBTI && S` requirements keep their Secure qualifier; **BTI setting**/**BTI clearing** are glossed as **BTI 置位指令**/**BTI 清零指令**; the 12 QARMA pseudocode function names stay in code spans; both listings keep their source line numbers 1–36 and 1–53 with the wrapped comments folded onto the owning instruction; the See-also block (B3.4) renders as `参见：`. No `# ` in the body.
  - S3 result: N/A — the chapter has no figures.
  - S4 result: nav entry `"指针认证与分支目标识别"` after 向量扩展 and before 术语表 in the Armv8-M group; landing list entry 7 (术语表 moved to 8).
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` OK (356 nav targets, 0 broken links); `check_heading_lang.py` OK; 1 `##` heading plus 2 `###` headings, no `# ` in the body, no `![]()` images.
  - S6 result: 40/40 rules present in source order across the three groups; the key matrix rebuilt as GFM text under a lead-in sentence; both listings reproduced line for line (36 and 53 lines, comments preserved); 0 figures, 1 table.
  - S7 result: covered by the user-approved single-loop run; the confirmation gate is taken once at the end of B2–B16.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (commit b5938c7).
  - [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [ ] S8
- [x] B7 → new article `armv8-m/memory_model/` (Memory Model; PDF pp. 202–262, 29 sections; 344 applicability lines)
  - S1 result (part 1): B7 spans printed 202–262 (the B8 divider is on printed 263); §1–§7 occupy printed 202–229 with 167 `Applies to an implementation …` lines. Structure: B7.1 Definition of the Armv8 memory model (with B7.1.1 Locations and nine unnumbered group headings), B7.2 Atomicity (B7.2.1–B7.2.16, including B7.2.4.1 Ordering relations), B7.3 Memory accesses, B7.4 Address space, B7.5 Endianness, B7.6 Alignment behavior, B7.7 Concurrent modification and execution of instructions. Census for this span: 2 figures, 1 table (the endianness element-size table). The chapter-front section list of B7.1 was kept because it sits inside the IJRPK rule and is the chapter's only navigation aid; its source numbering (B7.1.1, B7.2.3, B7.2.5, B7.2.7, B7.2.6, B7.2.9) was reproduced verbatim.
  - S2 result (part 1): `docs/cortex/armv8-m/memory_model/index.md`, 1132 ln; numbering restarts at 1 (`## 1.` ← B7.1 with `### 1.1` ← B7.1.1; `## 2.` ← B7.2 with `### 2.1`–`### 2.16` ← B7.2.1–B7.2.16 and `#### 2.4.1` ← B7.2.4.1; `## 3.`–`## 7.` ← B7.3–B7.7). Unnumbered source sub-heads became `####`. All 167 applicability lines are present with their extension requirements (`- M`, `- !M`, `- MVE`, `- PACBTI && S` style kept verbatim); source notes render as `注意，…。`; every See-also block is a `参见：` bullet list. Two transparent typo fixes: `RW1` duplicated in the RPXPQ bullet and `semanitcs` in the RPXQQ bullet. No `# ` in the body.
  - S3 result (part 1): `FigureB7-1.png` (little-endian and big-endian data layout) and `FigureB7-2.png` (instruction alignment and byte ordering) cropped from printed 225 at 300 dpi; both re-cropped after visual inspection clipped the panel titles and the "Least significant bit" legends. The source has no `Figure B7-n` captions, so the numbering is synthetic (A1 precedent).
  - S4 result (part 1): nav entry `"内存模型"` after 指针认证与分支目标识别 and before 术语表; landing list entry 8 (术语表 moved to 9).
  - S5 result (part 1): strict build 0 WARNING; index checks OK; heading-language check OK.
  - S6 result (part 1): 167/167 rules in source order across the seven sections; 2 figures embedded with lead-in sentences; 1 GFM table; group headings preserved; numbering continuity 1–1.1 / 2–2.16 with 2.4.1 / 3 / 4 / 5 / 6 / 7.
  - S2 result (part 2): §8–§29 appended to the same page (§8 Access rights … §29 Branch predictor maintenance operations); B7.27's Set/Way register format embedded as `FigureB7-4.png`, and the self-modifying-code sequence kept as a ```arm listing with the source comments. B7.20/B7.21/B7.26 have no See-also block in the source, so none was invented; B7.27's See-also continues onto the next printed page (B7.10) and was joined into one list.
  - S3 result (part 2): `FigureB7-3.png` (Shareability domains, printed 241) and `FigureB7-4.png` (Set/Way register format, printed 259) cropped at 300 dpi and verified visually.
  - S5 result (part 2): strict build 0 WARNING; `check_indexes.py --root .` OK (357 nav targets, 0 broken links); `check_heading_lang.py` OK; 29 `##` headings, no `# ` in the body, all 4 `![]()` targets present.
  - S6 result (part 2): 344/344 applicability lines match the source's 344 `Applies to an implementation …` lines across all 29 sections, and §20–§29 are 63/63. Two format defects found by that check and fixed: the B7.12 RLJKD rule had been split into two blocks (duplicating its applicability line), and a translated sentence in B7.2.4 began with 适用于, which the counter read as an applicability line.
  - S7 result: covered by the user-approved single-loop run.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets` (commit a1e82e4, sections 8–29; sections 1–7 in ef8ae64).
  - [x] plan gate [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B8 → new article `armv8-m/system_address_map/` (The System Address Map; PDF pp. 265–268, 3 sections, 18 rules)
  - S1 result: B8 spans printed 265–268 (the B9 divider is on printed 269, the chapter divider on 264); B8.1 System address map (4 rules), B8.2 The System region of the system address map (10 rules), B8.3 The System Control Space (SCS) (4 rules), plus the chapter-front section list, which was dropped (A1 precedent). Census: 1 figure (the system-region address diagram on printed 266, with its †/††/††† footnote block), 1 table (the nine-row address-region table on printed 265, including the WT/RA/WBWA/XN footnote list). Text and the table grid were read from the PDF layer page by page.
  - S2 result: `docs/cortex/armv8-m/system_address_map/index.md`; numbering restarts at 1 (`## 1.`–`## 3.` ← B8.1–B8.3). All 18 applicability lines are present with their extension requirements (`- M && !S`, `- S` kept verbatim), the RMXRW note renders as `注意，若 !M 则产生 **HardFault**。`, and the four See-also blocks are `参见：` lists (B8.1 and B8.3 block names stay English in 《…》). The address table is GFM with each 2-line address range collapsed to one row, and the WT/RA/WBWA/XN footnotes follow as a bullet list. No `# ` in the body.
  - S3 result: `FigureB8-1.png` cropped from printed 266 at 300 dpi with a ~18 pt margin; verified visually — top `0x00000000`, the right-hand "System region of the address map" bracket and the three dagger footnotes are all inside the crop.
  - S4 result: nav entry `"系统地址映射"` after 内存模型 and before 术语表; landing list entry 9 (术语表 moved to 10).
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` OK (358 nav targets, 0 broken links); `check_heading_lang.py` OK; 3 `##` headings, no `# ` in the body, the single `![]()` target exists.
  - S6 result: 18/18 rules present in source order (4 / 10 / 4); 1 figure, 1 table (9 rows × 7 columns, all 9 rows carry their region, memory type, XN, cache, shareability and usage); numbering continuity 1 / 2 / 3.
  - S7 result: covered by the user-approved single-loop run.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets`.
  - [x] plan gate [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
- [x] B9 → new article `armv8-m/synchronization_and_semaphores/` (Synchronization and Semaphores; PDF pp. 270–279, 5 sections + 2 sub-sections, 56 rules)
  - S1 result: B9 spans printed 270–279 (the B10 divider is on printed 280); B9.1 Exclusive access instructions (6 rules), B9.2 The local monitors (10), B9.3 The global monitor (11) with B9.3.1 Load-Exclusive and Store-Exclusive (5) and B9.3.2 Load-Exclusive and Store-Exclusive in Shareable memory (6), B9.4 Exclusive access instructions and the monitors (3), B9.5 Load-Exclusive and Store-Exclusive instruction constraints (15). The chapter-front section list was dropped (A1 precedent). Census: 2 figures (the local-monitor and global-monitor state diagrams, printed 271 and 275, each with its `*`/`‡` legend and footnote text), 1 table (the synchronization-primitive table on printed 270). Text read from the PDF layer page by page.
  - S2 result: `docs/cortex/armv8-m/synchronization_and_semaphores/index.md`; numbering restarts at 1 (`## 1.`–`## 5.` ← B9.1–B9.5, `### 3.1`/`### 3.2` ← B9.3.1/B9.3.2). All 56 applicability lines are present; the primitive table is GFM with the merged Function column expanded per row (Load-Exclusive/Store-Exclusive × Byte/Halfword/Word, then Clear-Exclusive); the RHLHS note keeps `M && MPU` / `M` verbatim; RMFGC and RDTRN/RDFNB keep their nested status-value lists; the four See-also blocks are `参见：` lists. No `# ` in the body.
  - S3 result: `FigureB9-1.png` (local monitor, printed 271) and `FigureB9-2.png` (global monitor for PE(n), printed 275) cropped at 300 dpi; both verified visually — the two state boxes, every transition label, the `*`/`‡` notes and the diagram legend are inside the crops.
  - S4 result: nav entry `"同步与信号量"` after 系统地址映射 and before 术语表; landing list entry 10 (术语表 moved to 11).
  - S5 result: strict build 0 WARNING; `check_indexes.py --root .` OK (359 nav targets, 0 broken links); `check_heading_lang.py` OK; 5 `##` and 2 `###` headings, no `# ` in the body, both `![]()` targets exist.
  - S6 result: 56/56 rules present in source order (6 / 10 / 11 + 5 + 6 / 3 / 15); 2 figures, 1 table; numbering continuity 1–5 with 3.1–3.2.
  - S7 result: covered by the user-approved single-loop run.
  - S8 result: committed on `feature/cortex-armv8m-b1-resets`.
  - [x] plan gate [x] S1 [x] S2 [x] S3 [x] S4 [x] S5 [x] S6 [x] S7 [x] S8
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
