# Cortex sync-todo — Arm document → article queue

> Maintained per the [arm-translate](../../../.agents/skills/skills/arm-translate/SKILL.md) skill; update the touched row and this index after every sync.
> Execution queue: the Group files below, one-article-at-a-time — **resume = the first `[ ]` row in group order**; all `[x]` = batch complete.
> Census: 2026-11-04, generated from `private-docs/ARM/` (mirror 2026-11-03) vs the `docs/cortex/` article trees; the corpus moved to `reference-docs/arm/` on 2026-11-07 (now tracked in the parent repo) and the R52+ TRM (102199) was catalogued then. This directory is excluded from the site build (`exclude_docs` in `mkdocs.yml`).

## Sources (`reference-docs/arm/`, read-only; formerly `private-docs/ARM/`)

| Document | Revision | Parse lines | PDF pair | Status |
| --- | --- | ---: | --- | --- |
| `cortex-m7/DDI0489F_cortex_m7_trm` | r1p2 | 8,778 | ✅ byte-identical (1,251,689 B) | pair complete |
| `cortex-m7/DDI0403E_e_armv7m_arm` | E.e | 51,102 | ✅ size = ima media_size (5,957,561 B) | pair complete — README "⏳ retrying" row is STALE |
| `cortex-m7/cortex_m7_at610_at611_sden_1068427` | v11.0 | 2,851 | ⚠️ **the PDF on disk is BOGUS** — md5 identical to the M7 TRM PDF (a mis-download) | `.md` only; figures blocked until a genuine PDF is obtained (official PDF behind Akamai; v8 mirror at state-machine.com) |
| `cortex-r52/cortex_r52_trm_100026_0100_00_en` | r1p0 | 44,511 | ✅ byte-identical (3,696,889 B) | pair complete |
| `cortex-r52/arm_cortex_r52plus_processor_trm_102199_0001_03_en` | r0p3 | — (**no parse**) | ✅ 719 pp, text layer usable | PDF only — translate from the PDF |
| `cortex-r52/DDI0553B_y_armv8m_arm` | B.y | 37,382 | ✅ size = ima media_size (9,561,121 B) | pair complete — README "⏳ retrying" row is STALE |

There is no `README.md` on disk; this table is the pairing ledger and supersedes the stale "⏳ retrying" rows. Never edit `reference-docs/arm/`. Note that `DDI0553B` documents the **Armv8-M (M-profile)** architecture — the Cortex-R52+ is Armv8-R AArch32, so this file is not the R52+ architecture manual.

## Parse quirks (plan-level)

- **M7 TRM**: chapters 1–5 carry `# Chapter N` markers; chapters 6–14 are plain-text `Chapter N` lines (sections mix `# N.x` h1 with plain text). Locate chapter/section boundaries by title, number headings by source order (RTE lesson).
- **R52 TRM**: every chapter is plain text; running headers repeat the chapter title on every page — the FIRST occurrence is the chapter start. Sections are `# N.x` h1.
- **R52+ TRM (102199)**: no parse exists, so the PDF text layer is the source; its chapter numbers sit two above 100026 (Programmers Model ch3, System Control ch4, Clocking ch5, Initialization ch7, Memory System ch8, MPU ch9) and appendix D PMC-R52+ exists only in this revision.
- **Legacy revision shift**: the three r52p articles and some m7 articles were built against an older TRM revision — `system_control` evidence `Table4-48` and `programmers_model` evidence `Table3-1` predate r1p0, where System Control = ch3 and Programmers Model = ch2; legacy images (`Figure8_*` in memory_system, `Table9-*` in memory_protection_unit) carry old chapter numbers. Confirm chapters by heading/caption text, never by file name; never rename existing images.
- **Armv7-M / Armv8-M**: body chapters start after the TOC block (Armv7-M from L739; Armv8-M Part A from L3834); sections are `# Bx.y`-style h1. The Armv8-M parse interleaves TOC entries, running page headers and body headings, so Part B chapter boundaries are located by title at S1 and the TOC (L225–L715) is the authoritative B1–B16 list.

## Coverage summary (29 core articles — m7 22, r52p 6, armv8-m 1; `concept/` articles cite external sources — outside the skill, not queued)

| Group | Doc | Articles | Mapped chapters | New-article chapters | Defects found at census |
| --- | --- | ---: | ---: | ---: | --- |
| [M7-TRM](M7-TRM.md) | DDI0489F r1p2 | 22 (all registered) | 3 (ch2, ch7, ch13) | 12 — all translated | none open (nvic stub fixed; batch shipped 2026-11-06) |
| [R52-TRM](R52-TRM.md) | 100026 r1p0 | 4 | 5 (ch2/ch7/ch8 verify-only pending; ch6 done) | 11 + appendices | system_control article 236 ln vs ~11k-ln chapter |
| [R52plus-TRM](R52plus-TRM.md) | 102199 r0p3 | 6 | 6 (ch3, ch5, ch7, ch8, ch9 verify-only; ch4 completion) | 10 + appendix D | 9 chapters untranslated (GIC, Debug, PMU, CTM, ETM, SIMD/FP, timer, power, intro); system_control 233 ln vs 165 pp |
| [ARMv7-M](ARMv7-M.md) | DDI0403E E.e | 10 | 5 complete (B1.5, A3, A4, B3.1–B3.5) | A5, A6, B2, B4, B5 done | none open (corrupted heading fixed; A3/A4/A5 shipped in PRs #322/#324/#327, A6/B2/B4/B5 in this batch) |
| [SDEN](SDEN.md) | SDEN-1068427 v11.0 | 0 | — | 1 (errata notice) | PDF mis-download blocks figure cropping |
| [ARMv8-M](ARMv8-M.md) | DDI0553B B.y | 1 | 1 (A1) | 16 — queued (B1–B16) | none open (series opened 2026-11-10; A1 shipped) |

## Group order (execution priority)

1. [M7-TRM](M7-TRM.md) — complete (all rows `[x]`, batch finished 2026-11-06)
2. [R52plus-TRM](R52plus-TRM.md) — **authoritative for `r52plus-trm/`** (the site tree is the R52+ core); verify-only rows first, then the ch4 System Control completion, then new chapters
3. [R52-TRM](R52-TRM.md) — older 100026 revision; keep as the provenance ledger for pages built before 2026-11-07, do not queue new work from it
4. [ARMv7-M](ARMv7-M.md) — batch complete (A3–A6, B2, B4, B5); instruction-details tail (A7) deferred
5. [SDEN](SDEN.md) — text-only run (figures blocked)
6. [ARMv8-M](ARMv8-M.md) — **ACTIVE** (opened 2026-11-10): A1 shipped; resume at the first `[ ]` row (B1). Parts C–G deliberately deferred.

## Rules

- Steps per row: **S1** source resolution + gap analysis · **S2** in-place translation (main session, never a subagent) · **S3** figures cropped from the PDF into the article dir · **S4** mkdocs nav + `docs/cortex/index.md` landing update · **S5** Phase A mechanical gate · **S6** Phase B fidelity · **S7** user confirmation gate · **S8** commit/PR.
- Chapters whose parse span exceeds ~1500 lines are marked ⏸ in the row — present the per-run plan and get user confirmation before translating (skill Step 3).
- Verify (S6-only) rows: no rewrite unless the source comparison finds real gaps; record the evidence, then `[x]`.
- Row status: a row flips to `[x]` **only when every step is checked**; an inapplicable step is ticked with its reason (`S4 (N/A: page already registered)`), never deleted — on closure the step line carries all of S1–S8, so a verify-only row that planned only S1/S6/S7/S8 gains the N/A ticks when it closes.
- Provenance: S8 ticks only once the commit exists, and every completed row carries `- S8 result: merged as `<sha>` (PR #N).` or `- S8 result: shipped as `<sha>`.` when the batch went straight to `master`; findings, counts and decisions go on `- Note:` / `- Sx result:` bullets, never on the row's checkbox line.
- Table format policy: GFM is the default; a raw HTML `<table>` is a narrow exception for structurally complex tables — see `.agents/skills/skills/arm-translate/references/article-format.md` §Tables for the exhaustive criteria.
