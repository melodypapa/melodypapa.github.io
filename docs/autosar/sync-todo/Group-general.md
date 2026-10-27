# Sync todo: Group general — general/base specifications

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] platform_types (SWS_StandardTypes · R23-11 markdown · ⛔ stub — full translation + title fix)
  - Note: 9-line stub, translate in full; **the front-matter title is wrongly "ECU State Manager" and the nav label collides with the real EcuM — the fix must also change the `mkdocs.yml` nav** (recorded in AGENTS.md)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion (title + nav changed together)
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] bsw_general (SWS_BSWGeneral · R23-11 markdown · ❌ new article)
  - Note: general specification of Basic Software modules — input document [2] of every module article, global foundation, worth translating early; directory `general/bsw_general/` (naming per mapping.md, lowercase snake_case)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] platform_types_2 (SWS_PlatformTypes · R23-11 markdown · ❌ new article)
  - Note: a different document from SWS_StandardTypes (noted in TODO.md); directory must not collide with platform_types (suggest `platform_types_std/`, or decide in Step 1 and propose to the user if unclear)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] communication_stack_types (SWS_CommunicationStackTypes · R23-11 markdown · ❌ new article)
  - Note (S1): source `~/Workspace/.../R23-11/BSWGeneral/AUTOSAR_CP_SWS_CommunicationStackTypes.md` (565 lines, direct run); new article `docs/autosar/general/communication_stack_types/index.md` (naming per mapping.md). Shape: ch.1 2 paras · ch.2 TWO tables = 9 acronyms + 4 abbreviations = 13 blockquote entries (incl. the long OSEK/VDX history row) · 3.1 3 entries / 3.2 · 4.1–4.3 (4.3 安全相关环境的适用性 per core_test precedent) · ch.5 · ch.6 Requirements Tracing DROPPED (droppable set) · ch.7 → §6: 7.1 General issues = 3 reqs (00004/00015/00030), 7.2 Error classification 7.2.1–7.2.5 all "none", 7.3 Security Events · ch.8 → §7: 8.1 14 types → §7.1.1–.14 (PduIdType/PduLengthType/PduInfoType/PNCHandleType/TPParameterType/BufReq_ReturnType/TpDataStateType/RetryInfoType/NetworkHandleType/CbkHandleIdType/TimeTupleType/TimeStampType/TimeStampQualType/ListElemStructType), 8.2 "Not applicable." → §7.2 函数定义 不适用 · ch.9 "Not applicable." → §8 时序图 不适用 · ch.10 → §9 配置规范 (9.1 发布信息 cross-ref to [2] ch.10.3) · appendix A DROPPED; no appendix B in source.
  - Note (S2 decisions): {DRAFT} markers + "(draft)" name suffix + "Tags: atp.Status=draft" dropped on the 5 draft types (91001–91005, per the no-{DRAFT} rule); source cell typo "ComStackTypes.h" (8.1.11/8.1.12/8.1.13) normalized to ComStack_Types.h; source Latin typo "it est" restored to "id est"; PDF mojibake "fÃ 1 4 r" restored to "für" (OSEK row).
  - Note (S3): strict build exit 0, zero WARNINGs; heading audit §1–§9 continuous; hygiene greps 0; §2 slice 0 `^| ` lines, 13 term lines = 13 source rows, order verified line by line; check_api_sync trivially OK (0:0) — the script's 8.2/8.3 pattern does not parse this doc's 8.1-based type layout, so the 14 type names/order were verified manually (8.1.1–8.1.14 = §7.1.1–.14, identical); gen_api_list --check passes; figures 0 — all images are page-chrome strips (5 known deco hashes + 5 further same-size strips d9461527 ×2 / e61809f4 / d09ad847 / de989782, 343×36–346×42, no captions → dropped).
  - Note (S3 census): identifier mentions 9 lines, 8 intra-article links applied (idempotency 0 lines); prose citations 4/4 converted ([1] ×1, [2] ×3), 0 UNRESOLVED, no --ref-skip needed; two-hop: [1] 术语表 and [2] SWS_BSWGeneral resolve EXTERNAL (no site article yet — report-only, user decision); cross-article module mentions 0; no plain-text URLs in source.
  - Note (S3): master's dead CanNm r21_11 link in communication/index.md is already absent (fixed 2026-10-27) — no change needed.
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 "no confirmed one by one" — per-row gate waived; evidence in Notes)
  - [x] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
- [ ] tr_glossary (AUTOSAR_FO_TR_Glossary · Foundation R23-11 markdown · 📖 reference doc, user-named run #78)
  - Note: 4646 source lines: ch.2.1 = 206 acronym rows; ch.4 = 343 definition terms (6-row tables). Article = docs/autosar/foundation/general/tr_glossary/ (TR reference structure, §7 exemption). 术语表 mechanism (user decision 2026-10-24): entries come from `scripts/tr_glossary.json` — extracted from the SOURCE during each translation batch; gen_glossary never re-parses the translated article. Tranche 1 + ch.4 batch 1 seeded. Tranches committed per batch.
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion (tranches)
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
