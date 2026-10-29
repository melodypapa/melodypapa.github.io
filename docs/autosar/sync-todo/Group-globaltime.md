# Sync todo: Group globaltime — global time cluster (new section)

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> This batch must first create the section landing page `docs/autosar/globaltime/index.md` (STANDARD.md §6 format) and register it in the nav — folded into the first row's Step 2.

## Queue

- [ ] stbm (SWS_SynchronizedTimeBaseManager · R23-11 markdown · ❌ new article, short name StbM)
  - Note: the first run also creates the `globaltime/` landing page + nav registration
  - Note: source 8,777 lines; article 5,314+ lines. ch.6 Requirements Tracing + appendix A dropped per mandate; ch.2 → 定义和缩略语 (source order: 2.1 缩略语 23 rows + 2.2 定义 27 rows)
  - Note: formulas (7.1)–(7.15) restored from the R23-11 PDF (`<!-- formula-not-decoded -->` in the conversion); Figure 9.6 extracted from PDF p.204 (diagram lost in the markdown conversion — only a 911x53 strip survived); 12 container UML diagrams embedded in §9 per gpt precedent (Figure10-1..10-12, source captions Figure 10.1–10.12)
  - Note: §3.1 registry in house format ([n] Title + > DOCID); citation/identifier/chapter-ref links applied (506 lines + 5 citation links + 11 anchors), idempotent; comma-form citations ([4, SWS BSW General] etc.) stay prose (open user question on the apply trigger)
  - Note: §9 配置规范 SWS 条目 cells filled with [ECUC_StbM_*] (new-article default, 2026-10-26 decision); §9.3 约束 keeps [SWS_StbM_CONSTR_*] as data (config constraints referenced by appendix B); PDF ground-truth census recorded: registry MATCH on all cited [n], 87 section refs all resolve, anchor-less classes (port-interface codes E_OK/E_NOT_OK, config parameters, ARTechTerm) report-only
  - Note: check_api_sync counts match (3/3 types, 39/39 functions); two name diffs are source-conversion artifacts — 8.2.1 "Extension to Std_ReturnType" multi-word heading (script captures first token only) and 8.3.27 source heading carries a stray space "StbM_ FrSetSlaveTimingData" (PDF p.140 confirms the real name; article uses the correct name)
  - Note: OMISIONS under the placeholder exception (user to verify): source 4.3 Conflicts = "None." → omitted entirely
  - Note: glossary +33 terms (flat alphabetical sections); TODO.md +## globaltime section + counts (22 ✅ / 50 covered 39.4%)
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (batch gate after all 4 rows — user instruction 2026-10-30)
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] can_tsyn (SWS_TimeSyncOverCAN · R23-11 markdown · ❌ new article, short name CanTSyn)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] eth_tsyn (SWS_TimeSyncOverEthernet · R23-11 markdown · ❌ new article, short name EthTSyn)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] fr_tsyn (SWS_TimeSyncOverFlexRay · R23-11 markdown · ❌ new article, short name FrTSyn)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
