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
  - Note: source 4,084 lines; article ~2.8k lines. ch.6 Requirements Tracing + appendix A dropped per mandate; message-format tables 7.1–7.19 as GFM; figures 1-1/1-2/5-1/7-1..7-4/9-1..9-6/10-1..10-11 embedded
  - Note: appendix B ID fences reconstructed from the R23-11 PDF pp.129-130 (markdown table for B.1.2 was hyphen-garbled; PDF is authoritative — 54 changed items)
  - Note: §9 config 18 containers with [ECUC_CanTSyn_*] cells; §9.3 约束 keeps [SWS_CanTSyn_CONSTR_*] as data
  - Note: check_api_sync OK (2/2 types, 3/3 functions); link_candidates applied (86 lines, idempotent); 10 glossary terms added
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (batch gate after all 4 rows — user instruction 2026-10-30)
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] eth_tsyn (SWS_TimeSyncOverEthernet · R23-11 markdown · ❌ new article, short name EthTSyn)
  - Note: source 3,950 lines; article ~2.65k lines. ch.6 Requirements Tracing + appendix A dropped per mandate; §3.1 registry 10 entries; ch.7 → §6 (7 subsections + figures 7-1/7-2, Pdelay protocol, secure time sync, dynamic port config); ch.8 → §7 API (2 types + 5 functions + 5 callbacks incl. TrcvLinkStateChg/Icv indications + 调度函数 + 期望接口 mandatory-none/optional-28); ch.9 → §8 时序图 (10 figure parts 9-1..9-9b; source 9.3/9.7 carry no own diagram content in the markdown — noted in place); ch.10 → §9 配置规范 (15 containers, [ECUC_EthTSyn_*] cells, 6 container diagrams Figure10-1..10-6, 5 [constr_*] constraints + note)
  - Note: source annexes B (Changed Traces History) AND C (Changed Constraints History) both translated as ## B. / ## C. (source-lettered annexes, rte precedent)
  - Note: check_api_sync N/A — EthTSyn source numbers its API chapter as 8.1.1–8.1.6 (4-level nesting), not the flat 8.2.x/8.3.x the script parses; counts verified manually: 2/2 types, 5/5 functions, 5/5 callbacks
  - Note: link_candidates applied (80 lines, idempotent); 7 glossary terms added (2 EthTSyn entries kept separate — module definition + scope sentence)
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (batch gate — user instruction 2026-10-30; run stopped after row 3 per user)
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
