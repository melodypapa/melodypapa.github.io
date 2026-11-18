# Sync todo: Group SDEN — Cortex-M7/M7 FPU Software Developer Errata Notice, SDEN-1068427 v11.0 (`reference-docs/arm/cortex-m7/cortex_m7_at610_and_cortex_m7_with_fpu_at611_software_developer_errata_notice_sden_1068427_v11_0_en.md`, 4,934 ln — but see the blocker: it is the TRM parse, not the SDEN)

Generated: 2026-11-04 · Queue order = row order (resume = the first row still `[ ]`)
Last refresh: 2026-11-18 — the re-parsed `.md` was checked and found to be the Cortex-M7 TRM, not the errata notice (see Blocker 2); the old "2,851 ln" figure belonged to the missing genuine parse.
Steps: S1 source resolution + gap analysis · S2 in-place translation · S3 figures · S4 nav + landing · S5 Phase A · S6 Phase B · S7 user gate · S8 commit/PR

## Blocker (recorded 2026-11-04 census)

1. **The PDF on disk is BOGUS**: `cortex_m7_at610_and_cortex_m7_with_fpu_at611_software_developer_errata_notice_sden_1068427_v11_0_en.pdf` is byte-identical (md5 `f30dd19c331a3ee47bedde67ef73a104`, 1,251,689 B) to `DDI0489F_cortex_m7_trm.pdf` — a mis-download. Do NOT crop figures from it and do not trust any page whose content differs from the errata notice. Never edit `reference-docs/arm/` — re-download the genuine SDEN PDF externally if figures are needed (official PDF behind Akamai bot protection; older v8 mirrored at `state-machine.com/doc/ARM-AT610-611.pdf`).
2. **The `.md` parse on disk is also the TRM** (found 2026-11-18): the file is 4,934 lines — exactly the M7 TRM parse length — and `diff` against `DDI0489F_cortex_m7_trm.md` yields only image-path lines (136 diff lines, all `![Figure…]` links); every chapter marker sits at the same line number (Introduction L364, Programmers Model L836, System Control L1028, …). It is the TRM parse with a different filename, so it carries **no SDEN content**. There is currently **no genuine source for this notice on disk** (no errata text, no summary table), and the old 2,851-line span map described a parse that no longer exists.
3. Consequence: the queue row cannot enter S1. Re-download the genuine notice first (`.md` preferred, PDF as the fallback for figures), then rebuild this ledger's span map and start from S1.

## Queue

- [ ] ⛔ errata notice → new article (text-only; e.g. `m7-trm/sden_errata/`; blocked — no genuine source on disk, see Blocker 1–3)
  - Note: translate the Errata summary table (GFM by default; raw HTML only when the structure qualifies) + errata descriptions verbatim; drop Change Control history + document chrome. No figures in this run; if the source turns out to reference a figure the parse lost, record it and defer to the genuine-PDF run. Re-download the notice before S1, then rewrite this row's size/spans from the new parse.
  - [ ] S1 [ ] S2 [ ] S3 (N/A: no figures in this notice) [ ] S4 [ ] S5 [ ] S6 [ ] S7 [ ] S8

## Not queued (deliberately)

- Change Control version history, proprietary notice, product/document information — document chrome per skill Step 3.
