# Sync todo: Group io — IO section wrap-up

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [x] dio_driver (SWS_DIODriver · R23-11 markdown · done 2026-10-24 incl. reopen for acronym reformat · commits de11d8a/493ed12/e21067f · PR #53)
  - Note: 2026-10-24 finished the 3.1/4.2/6.7/7.4 alignment (commits de11d8a/493ed12 · PR #53); the same-day acronym census found §2 still a GFM table (row set 15:15 identical) → reformatted as blockquotes per STANDARD.md §1
  - Note: reopen 2026-10-24 for the acronym-chapter format → finished in commit e21067f; the earlier per-article audit trail is [dio_driver.md](dio_driver.md)
  - Note: 2026-10-24 review (user named dio): source ch.1–8 checked chapter by chapter, no gaps; acronyms 15:15 in source order; `gen_glossary/gen_api_list --check` both exit 0 → no edits, no reopen. The newer R25-11 source differs structurally (7.1.2 expanded, 7.6.3 Transient Faults removed) — following a newer release needs its own reopen row
  - [x] Step 1 — Source resolution + gap analysis (source §2 table 15 rows; article 15:15; gap = format only)
  - [x] Step 2 — In-place translation/completion (table → 15 bold-term + blockquote entries, source order; English full names bolded; intro "下表"→"以下")
  - [x] Step 3 — Phase A mechanical checks (0 table rows, 15 term lines, source order preserved, no h1/requirement IDs, strict build 0 WARNING)
  - [x] Step 4 — Phase B coverage map + fidelity (15↔15 same order; content reuses the already-verified translation, layout only)
  - [x] Step 5 — User confirmation gate (user instruction "run skill to find and fix it" authorised this run; evidence presented in the report, PR #53 could veto)
  - [x] Step 6 — TODO.md row + commit/PR (commit e21067f · PR #53)
- [x] port_driver (SWS_PortDriver · R23-11 markdown · done 2026-10-24 · commit ee486aa · PR #53 / issue #54)
  - Note: acronym chapter was a GFM table → blockquotes (row set 7:7 verified); 4.2 "对汽车域的适用性" → "汽车域的适用性"
  - Note: 2026-10-24 Step 1 gap analysis (issue #54): new gap = §1 missing the source ch.1 mapping table (Driver / Port Pin / Channel Group, 2 rows × 4 columns); §4.2 wording and §2 format as noted; §7.6.3 "可配置接口" conflicted with STANDARD.md's "可配置的接口" (5 site articles use the former) → user decision; the rest of §3/§5/§6/§7 matches the source item by item
  - Note: user decision (2026-10-24): keep "可配置接口" in 7.6.3; STANDARD.md §2 and its decision log updated to that term
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion (§1 mapping table translated; §2 table → 7 bold-term + blockquote entries in source order; §4.2 → 汽车域的适用性)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING; 7-chapter skeleton; ch.2 zero table rows, 7 term lines; no h1/requirement IDs/forbidden chapters; glossary regenerated, `--check` 0, api `--check` 0)
  - [x] Step 4 — Phase B coverage map + fidelity (source ch.1–8 mapped section by section; ch.6/9/10/A deliberately omitted; §1 table translated 4 columns × 2 rows verbatim; ch.2 7:7 same order)
  - [x] Step 5 — User confirmation gate (2026-10-24 confirmed: Phase A/B evidence + TODO.md row; 7.6.3 decision keeps "可配置接口")
  - [x] Step 6 — TODO.md row + commit/PR (commit ee486aa · PR #53 · Closes #54)
- [ ] pwm_driver (SWS_PWMDriver · R23-11 markdown · ✅ alignment only)
  - Note: acronym chapter table → blockquotes (row set 13:13 verified); 4.2 "对汽车域的适用性" → "汽车域的适用性"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] ocu_driver (SWS_OCUDriver · R23-11 markdown · ✅ alignment + row set)
  - Note: acronym chapter table → blockquotes, restore the MCU row (source 14 rows → article 13 entries), drop the "Term definition:" pseudo-row; 3.1 "输入文档与相关标准和规范" → "输入文件"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] icu_driver (SWS_ICUDriver · R23-11 markdown · 🔶 alignment)
  - Note: delete the forbidden "时序图" chapter; 4.2 "适用车型域" → "汽车域的适用性"; acronym row set 12:12 already verified
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] adc_driver (SWS_ADCDriver · R23-11 markdown · ✅ alignment + deep completion)
  - Note: acronym row-set repair — source 18 rows → article 16 entries: restore API/HW/SW, restore the DEM→DET source order, merge Conversion Mode back into one entry, keep aliases on the term line (ADC Result Buffer (…,…)); 4.2 "适用车型域" → "汽车域的适用性"; deep completion (gaps measured by eval-2): ~78 SWS requirement texts in the API chapter untranslated, §3.1 stale 13-item list to be replaced by the two R23-11 items, §7.4.1 Background untranslated
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] iohwab (SWS_IOHardwareAbstraction · R23-11 markdown · ⚠️ gaps)
  - Note: missing "约束和假设" chapter; delete the forbidden "时序图" chapter; 3.1 is already "输入文件"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none — all 7 IO SWS documents are queued)
