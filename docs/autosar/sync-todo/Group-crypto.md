# Sync todo: Group crypto — crypto section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] crypto_service_manager (SWS_CryptoServiceManager · R23-11 markdown · ✅ alignment only)
  - Note: 4.2 "适用于汽车领域" → "汽车域的适用性"; 7.12 "Scheduled 函数" → "调度函数"
  - Note: run 2026-10-27 — beyond the two wording items, Step 1 found the article carries a DUPLICATE `### 7.12.` (回调通知 and Scheduled 函数 both numbered 7.12) → renumbered Scheduled 函数 to 7.13 (7.12.1 Csm_MainFunction → 7.13.1; no inbound anchor links site-wide). Observation for a future realignment row: the API chapter is legacy-structured (its own 7.1–7.13 grouping, 37 说明 blocks vs the source's 27 functions / 13 types; check_api_sync cannot parse this source — its 8.3.x headings are thematic prose titles, the known artifact class). Census observation: 5 prose [n] citations all UNRESOLVED against the 17-entry §3.1 registry (never linked, per rule); 17 registry anchors added; 15 identifier mentions applied; idempotent re-run 0 lines
  - [x] Step 1 — Source resolution + gap analysis (wording items + the duplicate-7.12 numbering bug; no chapter-coverage re-derivation per the alignment-only scope)
  - [x] Step 2 — In-place translation/completion (3 heading fixes: 4.2 → 汽车域的适用性; 7.12 "Scheduled 函数" → 7.13 调度函数 with 7.13.1 renumber)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING / no crypto_service_manager notices; heading numbering continuous incl. the 7.13 renumber; gen_api_list --check 0; check_api_sync artifact class as noted — thematic prose-titled source 8.3.x, manual observation recorded; census applied + idempotent)
  - [x] Step 4 — Phase B coverage map + fidelity (alignment-only: existing content untouched except the 3 heading lines; no coverage re-derivation; legacy-API-chapter observation recorded above)
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 "no confirmed one by one" — per-row gate waived; evidence in Notes and the PR)
  - [x] Step 6 — TODO.md row + commit/PR (branch feature/crypto-service-manager-sync · PR recorded after push)
- [ ] crypto_driver (SWS_CryptoDriver · R23-11 markdown · ⚠️ missing API chapter)
  - Note: missing "API 规范" chapter (one of the "6 articles missing only the API chapter" in TODO.md); 4.2 "适用于汽车领域" → "汽车域的适用性"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] cryif (SWS_CryptoInterface · R23-11 markdown · ❌ new article, short name CryIf)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] keym (SWS_KeyManager · R23-11 markdown · ❌ new article, short name KeyM)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
