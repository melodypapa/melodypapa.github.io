# Sync todo: Group SDEN — Cortex-M7/M7 FPU Software Developer Errata Notice, SDEN-1068427 v11.0 (`M7/cortex_m7_at610_at611_sden_1068427_v11_0_en.md`, 2,851 ln)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

## Blocker (recorded 2026-11-04 census)

- **The PDF on disk is BOGUS**: `M7/cortex_m7_at610_and_cortex_m7_with_fpu_at611_software_developer_errata_notice_sden_1068427_v11_0_en.pdf` is byte-identical (md5 `f30dd19c331a3ee47bedde67ef73a104`, 1,251,689 B) to `DDI0489F_cortex_m7_trm.pdf` — a mis-download. Do NOT crop figures from it and do not trust any page whose content differs from the errata notice. The `.private/ARM/README.md` ".md only" row is the correct record; the reference in `source-resolution.md` that lists a PDF pair predates this discovery. Never edit `.private/ARM/` — re-download the genuine SDEN PDF externally if figures are needed (official PDF behind Akamai bot protection; older v8 mirrored at `state-machine.com/doc/ARM-AT610-611.pdf`).
- Source shape: front matter (cover/notice/contents) · Change Control (v1.0→v11.0 history — chrome, droppable) · Errata summary table (L337+) · Errata descriptions (Category A implicit / **Category B (rare)** L90 / **Category C** L94) · Product and document information (L141+). The parse carries 1 `![` image ref (unresolved artefact path).

## Queue

- [ ] errata notice → new article (text-only; e.g. `m7_processor/sden_errata/`; front-matter title proposes 每个条目以标识符加粗，分类小节 B/C 保留源分组)
  - Note: translate the Errata summary table (GFM) + errata descriptions verbatim; drop Change Control history + document chrome. No figures in this run (blocker above); if the source turns out to reference a figure the parse lost, record it and defer to the genuine-PDF run.
  - [ ] S1 [ ] S2 [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately)

- Change Control version history, proprietary notice, product/document information — document chrome per skill Step 3.
