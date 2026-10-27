# Sync todo: Group general — general/base specifications

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] platform_types (SWS_StandardTypes · R23-11 markdown · ⛔ stub — full translation + title fix)
  - Note: 9-line stub, translate in full; **the front-matter title is wrongly "ECU State Manager" and the nav label collides with the real EcuM — the fix must also change the `mkdocs.yml` nav** (recorded in AGENTS.md)
  - Note: Step 1 measured 2026-10-27 — source `BSWGeneral/AUTOSAR_CP_SWS_StandardTypes.md` (R23-11) 661 lines; ch.5 is "Software Architecture" (5.1 Dependencies EMPTY + 5.2 File structure) → §5 软件架构 (direct translation; the canonical 对其他模块的依赖 applies only to sources whose ch.5 IS the dependencies chapter); ch.8 groups types at 8.1 + symbols at 8.2 + 8.3 "Not applicable." → §7.1 类型定义 (7 entries) / §7.2 符号定义 (5 entries) / §7.3 函数定义 = 不适用; ch.9/10 exist as "Not applicable." → §8/§9 = 不适用; appendix B "History of Requirements" → `## B. 需求历史` (direct translation of THIS source's title; the canonical 可追溯项变更历史 rendering belongs to the "Change history of AUTOSAR traceable items" title — flagged for review)
  - Note: figures — the iohwab triage hashes (f5f4bf49/8c27c74a/cad1600a/31a8ee06) are all deco here too; ONE content image: Figure 8.1 Layout of Std_Return_Type (547×367 px) → extracted as Figure8-1.png, embedded in 7.1.1; its spilled chrome text (MSB/LSB/Reserved by RTE) dropped
  - Note: title fixed to "AUTOSAR Standard Types（标准类型）"; mkdocs.yml nav label "EcuM" → "Standard Types" (collision resolved); article directory renamed general/platform_types/ → general/standard_types/ (2026-10-27, the honest slug for SWS_StandardTypes — general/platform_types/ stays reserved for the SWS_PlatformTypes document)
  - [x] Step 1 — Source resolution + gap analysis (R23-11 source 661 ln; full translation; no release fallback)
  - [x] Step 2 — In-place translation/completion (full Type A article ~330 ln; type entries = prose folds + literal bullets per the gpt/mcu house style; Table 8.1 Safety Transformer Error Codes = GFM with caption; {DRAFT} markers + "(draft)" name suffix dropped; E_OK/E_NOT_OK OSEK-compat definition block as a code fence; appendix B item-ID lists verbatim in fences, none → 无; glossary +3 (OSEK/VDX, STD new; API 来源 append))
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING after the drive-by removal of master's dead CanNm r21_11 link in communication/index.md — identical to the fix already in PR #120; headings ## 1–9 + ## B. 需求历史, continuous sub-numbering; no h1/{DRAFT}/requirement IDs outside the appendix-B fences; ch.2 3 term lines == source rows, 0 table rows; Figure8-1 resolves; gen_api_list --check 0; check_api_sync: source 8.2.x headings are comma-separated dual names ("E_OK, E_NOT_OK") which SRC_RE truncates at the comma — known parser artifact, manual verification: 5↔5 entries identical names+order (8.2.1–8.2.5 ↔ 7.2.1–7.2.5), 8.1.x 7↔7, 8.3 ↔ 7.3 = 不适用; census: 14 identifier mentions applied + 7 citation markers applied (bracket form), 1 UNRESOLVED [26] (stale "ASWS Transformer General" — never linked), 17 constant-bullet mentions report-only; idempotent re-run 0 lines)
  - [x] Step 4 — Phase B coverage map + fidelity (src ch.1–8 + ch.9/10 + appendix B ↔ §1–§9 + B mapped section by section; ch.6 Requirements Tracing + appendix A dropped as forbidden; empty source 5.1 kept as a bare heading (source-faithful); type tables folded to prose+literal bullets per the mcu/gpt house style, cell-by-cell verified; Table 8.1 error table = GFM with source caption; spilled figure chrome dropped; glossary anchored on master state — the iohwab PR #120 appends to the same API entry, trivial merge)
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 "no confirmed one by one" — per-row gate waived; evidence recorded here and reviewable in the PR)
  - [x] Step 6 — TODO.md row + commit/PR (branch feature/platform-types-sync · PR recorded after push (issue #122))
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
  - [x] Step 6 — TODO.md row + commit/PR (commit faa0806 on feature/comm-stack-types-sync; no push/PR — parent session handles GitHub)

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
