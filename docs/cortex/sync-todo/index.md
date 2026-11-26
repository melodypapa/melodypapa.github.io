# Cortex sync-todo — Arm document → article queue

> Maintained per the [arm-translate](../../../.agents/skills/arm-translate/SKILL.md) skill; update the touched row and this index after every sync.
> Ledgers whose **whole source document** is translated live in [`finished/`](finished/) — move a ledger there once every chapter row is `[x]`; the remaining group files carry the chapter plan, the finished-chapter ticks and the per-chapter S1–S8 checklist.
> Execution queue: the Group files below, one-article-at-a-time — **resume = the first `[ ]` row in group order**; all `[x]` = batch complete.
> Census: 2026-11-04, generated from `private-docs/ARM/` (mirror 2026-11-03) vs the `docs/cortex/` article trees; the corpus moved to `reference-docs/arm/` on 2026-11-07 (now tracked in the parent repo) and the R52+ TRM (102199) was catalogued then. **Refreshed 2026-11-18**: every `.md` was re-parsed and every ledger's span map, parse-line figure and queue was rebuilt from the files now on disk. This directory is excluded from the site build (`exclude_docs` in `mkdocs.yml`). **Status refresh 2026-11-19**: the Armv7-M C1 + D1–D8 batch (PR #406) and its D4 table fix (PR #410) are merged, so that group is closed.

## Sources (`reference-docs/arm/`, read-only; formerly `private-docs/ARM/`)

| Document | Revision | Parse lines | PDF pair | Status |
| --- | --- | ---: | --- | --- |
| `cortex-m7/DDI0489F_cortex_m7_trm` | r1p2 | 4,934 | ✅ byte-identical (1,251,689 B) | pair complete |
| `cortex-m7/DDI0403E_e_armv7m_arm` | E.e | 36,478 | ✅ size = ima media_size (5,957,561 B) | pair complete (2026-11-18 re-parse) |
| `cortex-m7/cortex_m7_at610_and_cortex_m7_with_fpu_at611_software_developer_errata_notice_sden_1068427_v11_0_en` | v11.0 | 4,934 — **but it is the M7 TRM parse** | ⚠️ **BOGUS** — md5 identical to the M7 TRM PDF (a mis-download) | ⛔ no genuine source on disk (`.md` = TRM, PDF = TRM); re-download before S1 (official PDF behind Akamai; v8 mirror at state-machine.com) |
| `cortex-r52/cortex_r52_trm_100026_0100_00_en` | r1p0 | 44,511 | ✅ byte-identical (3,696,889 B), 610 pp | pair complete |
| `cortex-r52/arm_cortex_r52plus_processor_trm_102199_0001_03_en` | r0p3 | — (**no parse**) | ✅ 719 pp, text layer usable | PDF only — translate from the PDF |
| `cortex-r52/DDI0553B_y_armv8m_arm` | B.y | 37,382 | ✅ size = ima media_size (9,561,121 B) | pair complete — parse stops at printed p.500 (see quirks) |

There is no `README.md` on disk; this table is the pairing ledger and supersedes the stale "⏳ retrying" rows. Never edit `reference-docs/arm/`. Note that `DDI0553B` documents the **Armv8-M (M-profile)** architecture — the Cortex-R52+ is Armv8-R AArch32, so this file is not the R52+ architecture manual.

## Parse quirks (plan-level)

- **M7 TRM**: the 2026-11-18 parse (4,934 ln) gives every chapter a `## Chapter <n>` marker — locate boundaries by that marker, sections are `## n.x` h2.
- **R52 TRM**: every chapter is plain text; running headers repeat the chapter title on every page — the FIRST occurrence is the chapter start. Sections are `# N.x` h1.
- **R52+ TRM (102199)**: no parse exists, so the PDF text layer is the source; its chapter numbers sit two above 100026 (Programmers Model ch3, System Control ch4, Clocking ch5, Initialization ch7, Memory System ch8, MPU ch9) and appendix D PMC-R52+ exists only in this revision.
- **Legacy revision shift**: the three r52p articles and some m7 articles were built against an older TRM revision — `system_control` evidence `Table4-48` and `programmers_model` evidence `Table3-1` predate r1p0, where System Control = ch3 and Programmers Model = ch2; legacy images (`Figure8_*` in memory_system, `Table9-*` in memory_protection_unit) carry old chapter numbers. Confirm chapters by heading/caption text, never by file name; never rename existing images.
- **Armv7-M**: the 2026-11-18 parse (36,478 ln) is clean — Part A opens at L471, every section is a `## Ax.y` / `## Bx.y` / `## C1.y` h2 and every appendix a `## Dn.y`, so spans are exact and no title-location is needed. Body ends at the glossary (L35834–36054); the alphabetical index (L36055–36478) is chrome.
- **Armv8-M**: body chapters start at L3834 (Part A); Part B is L4285–33105 (B4–B16 boundaries located by title — the parse interleaves TOC rows, running headers and body headings; the TOC at L225–L715 is the authoritative B1–B16 list), Part C is L33106 (C1 L33110, C2 L35188). The parse **stops at L37381 (printed p.500)**: the C2.4 body and the Part D/E/F/G bodies exist only in the PDF, so those pages translate from the PDF text layer.

## Coverage summary (refreshed 2026-11-18; `concept/` articles cite external sources — outside the skill, not queued)

| Group | Doc | Articles | Mapped chapters | New-article chapters | Defects found at census |
| --- | --- | ---: | ---: | ---: | --- |
| [M7-TRM](finished/M7-TRM.md) | DDI0489F r1p2 | 16 (all registered) | 3 (ch2, ch7, ch13) | 12 — all translated | finished (nvic stub fixed; batch shipped 2026-11-06; full verification 2026-11-18) |
| [R52-TRM](R52-TRM.md) | 100026 r1p0 | provenance only | all rows closed 2026-11-18 | 11 + appendices — built from the R52+ pages | superseded by the R52+ articles; span map re-verified, no new queue |
| [R52plus-TRM](R52plus-TRM.md) | 102199 r0p3 | 17 (all registered) | ch3/ch5/ch7/ch8/ch9 verified; ch4 completion done (5,655 ln) | 16 chapters + appendix D translated 2026-11-09 | appendices A–C queued as the deferred tail |
| [ARMv7-M](finished/ARMv7-M.md) | DDI0403E E.e | 22 translated (all registered) | A1–A7 (incl. the 263-entry instruction details), B1–B5, C1, D1–D8, glossary | A1–A7, B1–B5, C1, D1–D8, glossary done | finished (batch merged 2026-11-18 as #406; D4 table fix merged 2026-11-19 as #410) |
| [SDEN](SDEN.md) | SDEN-1068427 v11.0 | 0 | — | 1 (errata notice) | ⛔ both `.md` and PDF on disk are the M7 TRM — re-download the genuine notice before S1 |
| [ARMv8-M](ARMv8-M.md) | DDI0553B B.y | 1 A + 16 B + 2 C + 4 D/E/F + 1 G | A1, B1–B16, C1, C2.1–C2.3, C2.4 A–C, G done | C2.4 D–Z (437 entries); D1/E1/E2/F1 scaffolded | in progress — next is C2.4 D–F, then the remaining bands and the D/E/F tail; the parse stops at printed p.500, so the deferred tail is PDF-sourced |

## Group order (execution priority)

1. [M7-TRM](finished/M7-TRM.md) — **finished** (all rows `[x]`, batch finished 2026-11-06; verified 2026-11-18)
2. [R52plus-TRM](R52plus-TRM.md) — **authoritative for `r52plus-trm/`**; all chapters and appendix D done, resume at appendix A (deferred reference tail)
3. [R52-TRM](R52-TRM.md) — older 100026 revision; provenance ledger for pages built before 2026-11-07 — every row closed 2026-11-18, do not resume work from it
4. [ARMv7-M](finished/ARMv7-M.md) — **finished**: Parts A–D shipped (C1 + D1–D8 merged 2026-11-18 as PR #406; the D4 table fix merged 2026-11-19 as PR #410)
5. [SDEN](SDEN.md) — ⛔ blocked: no genuine source on disk (both the parse and the PDF are the M7 TRM)
6. [ARMv8-M](ARMv8-M.md) — **ACTIVE** (opened 2026-11-10): B1–B16, C1–C2.3, C2.4 A–C and G shipped; resume at **C2.4 D–F**, then the remaining bands and the D/E/F deferred tail

## Rules

- Steps per row: **S1** source resolution + gap analysis · **S2** in-place translation (main session, never a subagent) · **S3** figures cropped from the PDF into the article dir · **S4** mkdocs nav + `docs/cortex/index.md` landing update · **S5** Phase A mechanical gate · **S6** Phase B fidelity · **S7** user confirmation gate · **S8** commit/PR.
- Chapters whose parse span exceeds ~1500 lines are marked ⏸ in the row — present the per-run plan and get user confirmation before translating (skill Step 3).
- Verify (S6-only) rows: no rewrite unless the source comparison finds real gaps; record the evidence, then `[x]`.
- Row status: a row flips to `[x]` **only when every step is checked**; an inapplicable step is ticked with its reason (`S4 (N/A: page already registered)`), never deleted — on closure the step line carries all of S1–S8, so a verify-only row that planned only S1/S6/S7/S8 gains the N/A ticks when it closes.
- Provenance: S8 ticks only once the commit exists, and every completed row carries `- S8 result: merged as `<sha>` (PR #N).` or `- S8 result: shipped as `<sha>`.` when the batch went straight to `master`; findings, counts and decisions go on `- Note:` / `- Sx result:` bullets, never on the row's checkbox line.
- Table format policy: GFM is the default; a raw HTML `<table>` is a narrow exception for structurally complex tables — see `.agents/skills/arm-translate/references/article-format.md` §Tables for the exhaustive criteria.
