# Cortex sync-todo — Arm document → article queue

> Maintained per the [arm-translate](../../../.agents/skills/arm-translate/SKILL.md) skill; update the touched row and this index after every sync.
> Execution queue: the Group files below, one-article-at-a-time — **resume = the first `[ ]` row in group order**; all `[x]` = batch complete.
> Census: 2026-11-04, generated from `.private/ARM/` (mirror 2026-11-03) vs `docs/cortex/*_processor/` headings. This directory is excluded from the site build (`exclude_docs` in `mkdocs.yml`).

## Sources (`.private/ARM/`, read-only)

| Document | Revision | Parse lines | PDF pair | Status |
| --- | --- | ---: | --- | --- |
| `M7/DDI0489F_cortex_m7_trm` | r1p2 | 8,778 | ✅ byte-identical (1,251,689 B) | pair complete |
| `M7/DDI0403E_e_armv7m_arm` | E.e | 51,102 | ✅ size = ima media_size (5,957,561 B) | pair complete — README "⏳ retrying" row is STALE |
| `M7/cortex_m7_at610_at611_sden_1068427` | v11.0 | 2,851 | ⚠️ **the PDF on disk is BOGUS** — md5 identical to the M7 TRM PDF (a mis-download) | `.md` only; figures blocked until a genuine PDF is obtained (official PDF behind Akamai; v8 mirror at state-machine.com) |
| `R52/cortex_r52_trm_100026_0100_00_en` | r1p0 | 44,511 | ✅ byte-identical (3,696,889 B) | pair complete |
| `R52/DDI0553B_y_armv8m_arm` | B.y | 37,382 | ✅ size = ima media_size (9,561,121 B) | pair complete — README "⏳ retrying" row is STALE |

`README.md` is the recorded pairing ledger but predates the finished downloads and the bad SDEN fetch; this table supersedes it. Never edit `.private/ARM/`.

## Parse quirks (plan-level)

- **M7 TRM**: chapters 1–5 carry `# Chapter N` markers; chapters 6–14 are plain-text `Chapter N` lines (sections mix `# N.x` h1 with plain text). Locate chapter/section boundaries by title, number headings by source order (RTE lesson).
- **R52 TRM**: every chapter is plain text; running headers repeat the chapter title on every page — the FIRST occurrence is the chapter start. Sections are `# N.x` h1.
- **Legacy revision shift**: the three r52p articles and some m7 articles were built against an older TRM revision — `system_control` evidence `Table4-48` and `programmers_model` evidence `Table3-1` predate r1p0, where System Control = ch3 and Programmers Model = ch2; legacy images (`Figure8_*` in memory_system, `Table9-*` in memory_protection_unit) carry old chapter numbers. Confirm chapters by heading/caption text, never by file name; never rename existing images.
- **Armv7-M / Armv8-M**: body chapters start after the TOC block (Armv7-M from L739; Armv8-M Part A from L3834); sections are `# Bx.y`-style h1.

## Coverage summary (11 core articles; `concept/` articles cite external sources — outside the skill, not queued)

| Group | Doc | Articles | Mapped chapters | New-article chapters | Defects found at census |
| --- | --- | ---: | ---: | ---: | --- |
| [M7-TRM](M7-TRM.md) | DDI0489F r1p2 | 3 (1 stub) | 2 (ch2 partial, ch7 stub) | 12 | nvic = 26-ln stub + missing from landing page; ch6+ chapters all untranslated |
| [R52-TRM](R52-TRM.md) | 100026 r1p0 | 4 | 4 (ch3 covers ~2%) | 10 + appendices | system_control article 236 ln vs ~11k-ln chapter |
| [ARMv7-M](ARMv7-M.md) | DDI0403E E.e | 4 | 4 partial | 3 + deferred tail | instruction_set carries a corrupted heading `## ARM=-0987654321   yhn 4esx1` |
| [SDEN](SDEN.md) | SDEN-1068427 v11.0 | 0 | — | 1 (errata notice) | PDF mis-download blocks figure cropping |
| [ARMv8-M](ARMv8-M.md) | DDI0553B B.y | 0 | — | deferred | no article cites it yet |

## Group order (execution priority)

1. [M7-TRM](M7-TRM.md) — stub/hygiene repairs first, then new chapters small→large
2. [R52-TRM](R52-TRM.md) — verify-only rows first, then the ch3 System Control completion, then new chapters
3. [ARMv7-M](ARMv7-M.md) — alignments/completions, then new chapters; instruction-details tail deferred
4. [SDEN](SDEN.md) — text-only run (figures blocked)
5. [ARMv8-M](ARMv8-M.md) — deferred until an M-profile architecture series opens

## Rules

- Steps per row: **S1** source resolution + gap analysis · **S2** in-place translation (main session, never a subagent) · **S3** figures cropped from the PDF into the article dir · **S4** mkdocs nav + `docs/cortex/index.md` landing update · **S5** Phase A mechanical gate · **S6** Phase B fidelity · **S7** user confirmation gate · **S8** commit/PR.
- Chapters whose parse span exceeds ~1500 lines are marked ⏸ in the row — present the per-run plan and get user confirmation before translating (skill Step 3).
- Verify (S6-only) rows: no rewrite unless the source comparison finds real gaps; record the evidence, then `[x]`.
- Table format policy: GFM is the default; a raw HTML `<table>` is a narrow exception for structurally complex tables — see `.agents/skills/arm-translate/references/article-format.md` §Tables for the exhaustive criteria.
