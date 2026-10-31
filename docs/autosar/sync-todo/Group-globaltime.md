# Sync todo: Group globaltime — global time cluster (new section)

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> This batch must first create the section landing page `docs/autosar/globaltime/index.md` (STANDARD.md §6 format) and register it in the nav — folded into the first row's Step 2.

## Queue

- [x] stbm (SWS_SynchronizedTimeBaseManager · R23-11 markdown · ❌ new article, short name StbM)
  - Note: the first run also creates the `globaltime/` landing page + nav registration
  - Note: source 8,777 lines; article 5,314+ lines. ch.6 Requirements Tracing + appendix A dropped per mandate; ch.2 → 定义和缩略语 (source order: 2.1 缩略语 23 rows + 2.2 定义 27 rows)
  - Note: formulas (7.1)–(7.15) restored from the R23-11 PDF (`<!-- formula-not-decoded -->` in the conversion); Figure 9.6 extracted from PDF p.204 (diagram lost in the markdown conversion — only a 911x53 strip survived); 12 container UML diagrams embedded in §9 per gpt precedent (Figure10-1..10-12, source captions Figure 10.1–10.12)
  - Note: §3.1 registry in house format ([n] Title + > DOCID); citation/identifier/chapter-ref links applied (506 lines + 5 citation links + 11 anchors), idempotent; comma-form citations ([4, SWS BSW General] etc.) stay prose (open user question on the apply trigger)
  - Note: §9 配置规范 SWS 条目 cells filled with [ECUC_StbM_*] (new-article default, 2026-10-26 decision); §9.3 约束 keeps [SWS_StbM_CONSTR_*] as data (config constraints referenced by appendix B); PDF ground-truth census recorded: registry MATCH on all cited [n], 87 section refs all resolve, anchor-less classes (port-interface codes E_OK/E_NOT_OK, config parameters, ARTechTerm) report-only
  - Note: check_api_sync counts match (3/3 types, 39/39 functions); two name diffs are source-conversion artifacts — 8.2.1 "Extension to Std_ReturnType" multi-word heading (script captures first token only) and 8.3.27 source heading carries a stray space "StbM_ FrSetSlaveTimingData" (PDF p.140 confirms the real name; article uses the correct name)
  - Note: OMISIONS under the placeholder exception (user to verify): source 4.3 Conflicts = "None." → omitted entirely
  - Note: glossary +33 terms (flat alphabetical sections); TODO.md +## globaltime section + counts (22 ✅ / 50 covered 39.4%)
  - Note: heading-language fix 2026-10-30 — 12 untranslated `###`+ headings (4.1.1–4.1.6, 5.1, 5.2, 6.16.1, 6.17.1.3, 6.17.2.3, 7.2.1) translated to Chinese; 7.2.1 now reads 「Std_ReturnType 的扩展」 (crypto_driver/key_manager/crypto_interface precedent) — the article's own `Extension to Std_ReturnType` had been the source text copied verbatim; identifier-titled headings (StbM_Init, StbMGeneral, GlobalTime_Master, …) stay English by rule
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (confirmed 2026-10-30, batch gate)
  - [x] Step 6 — TODO.md row + commit/PR (commits 53cd591, batch confirmed 2026-10-30)
- [x] can_tsyn (SWS_TimeSyncOverCAN · R23-11 markdown · ❌ new article, short name CanTSyn)
  - Note: source 4,084 lines; article ~2.8k lines. ch.6 Requirements Tracing + appendix A dropped per mandate; message-format tables 7.1–7.19 as GFM; figures 1-1/1-2/5-1/7-1..7-4/9-1..9-6/10-1..10-11 embedded
  - Note: appendix B ID fences reconstructed from the R23-11 PDF pp.129-130 (markdown table for B.1.2 was hyphen-garbled; PDF is authoritative — 54 changed items)
  - Note: §9 config 18 containers with [ECUC_CanTSyn_*] cells; §9.3 约束 keeps [SWS_CanTSyn_CONSTR_*] as data
  - Note: check_api_sync OK (2/2 types, 3/3 functions); link_candidates applied (86 lines, idempotent); 10 glossary terms added
  - Note: heading-language fix 2026-10-30 — 52 untranslated `###`+ headings translated to Chinese (§5.1 file structure, §6.2–§6.6 functional spec incl. all #####/###### levels, §8 时序图, §9.2.1 变体); 19 inbound anchors re-pointed at the new Material slugs (32 references); 3 self-referential 「」 glosses updated to the new section names; the leftover English connectives "either/or" in §6.2.1's bullet list translated to 要么
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (confirmed 2026-10-30, batch gate)
  - [x] Step 6 — TODO.md row + commit/PR (commit 364c4fd, batch confirmed 2026-10-30)
- [x] eth_tsyn (SWS_TimeSyncOverEthernet · R23-11 markdown · ❌ new article, short name EthTSyn)
  - Note: source 3,950 lines; article ~2.65k lines. ch.6 Requirements Tracing + appendix A dropped per mandate; §3.1 registry 10 entries; ch.7 → §6 (7 subsections + figures 7-1/7-2, Pdelay protocol, secure time sync, dynamic port config); ch.8 → §7 API (2 types + 5 functions + 5 callbacks incl. TrcvLinkStateChg/Icv indications + 调度函数 + 期望接口 mandatory-none/optional-28); ch.9 → §8 时序图 (10 figure parts 9-1..9-9b; source 9.3/9.7 carry no own diagram content in the markdown — noted in place); ch.10 → §9 配置规范 (15 containers, [ECUC_EthTSyn_*] cells, 6 container diagrams Figure10-1..10-6, 5 [constr_*] constraints + note)
  - Note: source annexes B (Changed Traces History) AND C (Changed Constraints History) both translated as ## B. / ## C. (source-lettered annexes, rte precedent)
  - Note: check_api_sync N/A — EthTSyn source numbers its API chapter as 8.1.1–8.1.6 (4-level nesting), not the flat 8.2.x/8.3.x the script parses; counts verified manually: 2/2 types, 5/5 functions, 5/5 callbacks
  - Note: heading-language fix 2026-10-30 — 51 untranslated `###`+ headings translated to Chinese (§4.2 精度, §5.1 file structure, §6.1–§6.9 functional spec incl. all ##### levels, §8 时序图); 8 inbound anchors re-pointed at the new Material slugs; 3 self-referential 「」 glosses updated to the new section names (「ICV 生成」/「ICV 验证」)
  - Note: link_candidates applied (80 lines, idempotent); 7 glossary terms added (2 EthTSyn entries kept separate — module definition + scope sentence)
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (confirmed 2026-10-30, batch gate; run stopped after row 3 per user — fr_tsyn row stays open for the next run)
  - [x] Step 6 — TODO.md row + commit/PR (commit 8f01771, batch confirmed 2026-10-30)
- [ ] fr_tsyn (SWS_TimeSyncOverFlexRay · R23-11 markdown · ❌ new article, short name FrTSyn)
  - Note: 2026-10-30 — translate every `###`+ heading title, not just the level-2 chapters (rows 1–3 shipped 115 English headings; fixed in the same PR). Run `python .agents/skills/autosar-translate/scripts/check_heading_lang.py docs/autosar/globaltime/fr_tsyn/index.md` in Step 3 — exit 0 required. Identifier-titled headings (FrTSyn_*, FrTSynGlobalTimeDomain, port/interface names) stay English; every prose title translates
  - Note: Source confirmed: R23-11 markdown `AUTOSAR_CP_SWS_TimeSyncOverFlexRay.md` (3,167 lines); the new article path does not exist.
  - Note: Mapping: source ch.1–5 → article §§1–5; ch.6 Requirements Tracing and appendix A are deliberately omitted per mandate; ch.7→§6, ch.8→§7, ch.9→§8, ch.10→§9, appendix B→`## B. AUTOSAR 可追溯项变更历史`.
  - Note: Source inventory: 24 ch.2 rows; API has 2 types, 3 functions, 4 callbacks, 1 scheduled function; ch.9 has 3 sequence diagrams; ch.10 has 14 configuration containers.
  - Note: Source API uses nested 8.1.2/8.1.3 numbering rather than the flat 8.2.x/8.3.x parsed by `check_api_sync.py`; verify names, order, and counts manually.
  - Note: No Known Limitations chapter or additional `None.`/`N/A.`-only sections found in the initial scan. Appendix B `none` values and API `None` cells carry content and are not omissions; verify during coverage review.
  - Note: Plan: create `fr_tsyn/index.md`, translate all required source sections and glossary terms, restore applicable in-article links, update nav + section/CP AUTOSAR indexes, regenerate the API list, then run Phase A and Phase B.
  - Note: Article completed: source ch.1–5, 7–10, and appendix B map to §§1–5, 6–9, and B; source ch.6 and appendix A are omitted per mandate.
  - Note: Embedded all 18 content diagrams (3 overview/dependency, 3 functional-spec, 3 sequence, 9 config); all source tables are GFM; translated 14 configuration containers.
  - Note: PDF cross-checks: formula restored on p.33; split Tables 7.3/7.7 reconstructed (pp.22/24); Appendix B IDs reconstructed (pp.102–104); security-event name verified on p.52.
  - Note: API inventory: 2 types, 3 functions, 4 callbacks, 1 scheduled function, 5 mandatory and 20 optional interfaces.
  - Note: `link_candidates.py --apply` changed 51 lines (16 chapter refs, 20 citation links, 0 anchors); second run changed 0 lines.
  - Note: Glossary extended with 10 new terms and FrTSyn source attribution on 20 existing entries; `SC` is listed as “Sequence Counter” to avoid the existing “Supervision Cycle” definition.
  - Note: Source anomalies for confirmation: PDF p.58 spells `SduLength` as `SduLengh`; article uses the API field `SduLength`. PDF p.98 describes `FrTSynIcvVerificationFvIdRef` as FV for ICV generation despite its verification container; article translates the apparent intended use.
  - Note: User decision (2026-10-31): keep `docs/index.md` unchanged. Phase A `check_indexes.py` remains blocked by the pre-existing missing home link to the top-level `音乐` tab; no out-of-scope fix made.
  - Note: User decision superseded later (2026-10-31): add the one-line `音乐` home link in `docs/index.md`; `check_indexes.py` now passes.
  - Note: API listing regenerated on `origin/master`'s current article-based generator; it lists 2 types and 8 functions (3 APIs, 4 callbacks, 1 scheduled function); `--check` passes.
  - Note: Phase A passed (2026-10-31): strict build exit 0 with zero MkDocs WARNINGs; heading-language and index checks passed (207 nav targets, 129 overview pages, 18 landings, 12 tabs).
  - Note: Hygiene passed: 0 body H1, `{DRAFT}`, broken `\<` placeholders, or requirement IDs before configuration; acronym table is 24/24 in source order; Annex B and constraint IDs are permitted data.
  - Note: Derived checks passed: API listing `--check`, glossary `--check`; `check_api_sync.py` is N/A for source 8.1.x numbering, manual inventory verified 2 types/3 functions/4 callbacks/1 schedule/5 mandatory/20 optional.
  - Note: Link audit passed: no external URLs; all anchors resolve; census 133 identifier mentions (§5 1/§6 35/§7 14/§9 83), 27 reference lines, 6 chapter refs (0 unresolved), 20/20 linked citations (0 unresolved), BswM SITE ×2, Det NO-ARTICLE ×9.
  - Note: Phase B map: source ch.1–5 → §§1–5; ch.7 → §6, including all numbered subsections and descendants; ch.8 → §7; ch.9 → §8; ch.10 → §9; appendix B → §B.
  - Note: Phase B API coverage: 22 imported types, 2 definitions, 3 functions, 4 callbacks, 1 scheduled function, and 5 mandatory/20 optional interfaces; signatures and service IDs manually checked.
  - Note: Fidelity checks: 24/24 acronym rows match source order; message tables 7.1–7.8 present; all 56 unique ECUC IDs match; 14 config containers and 9 config diagrams included.
  - Note: Appendix B lists match the R23-11 PDF: R22-11 added/changed/deleted 55/40/1 IDs; R23-11 added/changed/deleted 20/35/1 IDs, plus 1 added constraint.
  - Note: Omissions verified: only mandated ch.6 Requirements Tracing and appendix A; no Known Limitations or additional None/N.A.-only sections; appendix B `none` values translated as 无.
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (confirmed 2026-10-31; coverage, source corrections, and TODO status row approved)
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
