# Sync todo: Group crypto — crypto section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [x] crypto_service_manager (SWS_CryptoServiceManager · R23-11 markdown · ✅ alignment only)
  - Note: 4.2 "适用于汽车领域" → "汽车域的适用性"; 7.12 "Scheduled 函数" → "调度函数"
  - Note: run 2026-10-27 — beyond the two wording items, Step 1 found the article carries a DUPLICATE `### 7.12.` (回调通知 and Scheduled 函数 both numbered 7.12) → renumbered Scheduled 函数 to 7.13 (7.12.1 Csm_MainFunction → 7.13.1; no inbound anchor links site-wide). Observation for a future realignment row: the API chapter is legacy-structured (its own 7.1–7.13 grouping, 37 说明 blocks vs the source's 27 functions / 13 types; check_api_sync cannot parse this source — its 8.3.x headings are thematic prose titles, the known artifact class). Census observation: 5 prose [n] citations all UNRESOLVED against the 17-entry §3.1 registry (never linked, per rule); 17 registry anchors added; 15 identifier mentions applied; idempotent re-run 0 lines
  - [x] Step 1 — Source resolution + gap analysis (wording items + the duplicate-7.12 numbering bug; no chapter-coverage re-derivation per the alignment-only scope)
  - [x] Step 2 — In-place translation/completion (3 heading fixes: 4.2 → 汽车域的适用性; 7.12 "Scheduled 函数" → 7.13 调度函数 with 7.13.1 renumber)
  - [x] Step 3 — Phase A mechanical checks (strict build exit 0 / 0 WARNING / no crypto_service_manager notices; heading numbering continuous incl. the 7.13 renumber; gen_api_list --check 0; check_api_sync artifact class as noted — thematic prose-titled source 8.3.x, manual observation recorded; census applied + idempotent)
  - [x] Step 4 — Phase B coverage map + fidelity (alignment-only: existing content untouched except the 3 heading lines; no coverage re-derivation; legacy-API-chapter observation recorded above)
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 "no confirmed one by one" — per-row gate waived; evidence in Notes and the PR)
  - [x] Step 6 — TODO.md row + commit/PR (branch feature/crypto-service-manager-sync · PR #133, merged 2026-10-27 as 82efc13; row flipped by the Group-crypto batch run 2026-10-27)
- [ ] crypto_driver (SWS_CryptoDriver · R23-11 markdown · ⚠️ missing API chapter)
  - Note: missing "API 规范" chapter (one of the "6 articles missing only the API chapter" in TODO.md); 4.2 "适用于汽车领域" → "汽车域的适用性"
  - Note: Step 1 measured 2026-10-27 — the ⚠️ tag understated the gap: source `Crypto/AUTOSAR_CP_SWS_CryptoDriver.md` (R23-11) 3398 lines; the 180-line article stopped inside source 7.1.1 (one untranslated English requirement as its last paragraph). Missing: 7.1.1-tail/7.1.2/7.1.3, all of 7.2 (7.2.1–7.2.7 incl. key formats + crypto profiles), 7.3–7.5, ch.8 entirely (2 types, 20 functions in 5 groups, 4 NvBlock callbacks, 1 scheduled function, expected interfaces), ch.9 ("n/a" → `## 8. 时序图` 不适用), ch.10 (16 containers → `## 9. 配置规范`), 5.1/5.1.1 file structure. No appendix B, no Known-Limitations chapter in source; ch.6 Requirements Tracing dropped (forbidden)
  - Note: release drift in the EXISTING head — §3.1 carried an older release's 11-entry registry ([1] Layered SW Architecture … [8] Glossary …) while R23-11 has 6 entries ([1] SWS_CryptoInterface … [6] TR_SecureHardwareExtensions) and ch.7/8 prose cites those numbers; kept numbering would mis-link every new [n] → §3 realigned to the R23-11 source (3.1 = 6 entries, 3.2 = BSW General sentence + the 7 external standards as a list; old 3.2/3.3 split removed), §1 and §5 citations renumbered [4]→[1], [5]→[2]. Decision recorded for the batch confirmation
  - Note: ch.2 audit — 9 acronym rows + 10 term rows match the source row set/order (Operation's START/UPDATE/FINISH sub-rows = one entry with bullets, as in the source's spanning rows); Key Element definition completed with the source's last sentence (NV/RAM memory areas); `(see [SWS_Crypto_00225])` → 参见第6.2章 (hygiene rule); `### 2.1. 专业术语` → `术语表` (direct translation of "Glossary of Terms"; no inbound anchors)
  - Note: figures — 17 content images by hash/size triage: Figure7_1 (existing higher-res copy kept), SWS_Crypto_00018.png (the uncaptioned job state-machine diagram that IS the requirement — Csm's `SWS_Csm_01041.png` precedent), Figure7_2/7_3, Figure10_1–10_13 (Figure 10.11's caption is lost in the conversion; its image sits between 10.10 and 10.12 → named by order). Deco set here: f5f4bf49 ×42, cad1600a ×25, 31a8ee06 ×13, 8c27c74a ×8, a133f680/d9461527 ×4, e61809f4 ×3 + 9 inline icons ≤29px
  - Note: translation dispatched as 6 line-range segments (312–617, 618–1114, 1115–1472, 1473–2197, 2198–2881, 2882–3398) to general-purpose agents under `/tmp/crypto_contract.md`; known hazards flagged to them: 7.2.7.2's two page-split mapping tables (rejoin + R22-11 PDF check), [SWS_Crypto_00261] table's spanning chrome row, 7.1.3 `formula-not-decoded` list item, `&lt;NvBlock&gt;` callback headings
  - [x] Step 1 — Source resolution + gap analysis (R23-11 source 3398 ln; near-full translation, not an API-chapter patch; no release fallback)
  - Note: Step 3 evidence — strict build exit 0 / 0 WARNING / no crypto_driver notices; headings §1–§9 continuous at every depth (script-checked, 0 issues; deepest level `###### 7.3.4.x.y`); hygiene: 0 h1, 0 {DRAFT}, 0 `\<`, 0 glyph/chrome, [ECUC_Crypto_*] only in SWS 条目 cells, 1 cross-document id `[SWS_Csm_01022]` kept verbatim in §6.2.5.3 per the bsw_general precedent; ch.2 slice 0 table rows, 19 term lines = 9 acronyms + 10 terms (source rows); 17 figure refs all resolve; gen_api_list --check 0; check_api_sync = known grouped-8.3.x artifact class — manual check 24↔24 identifiers (19 functions + 4 callbacks + MainFunction) identical names and order, 19 说明 blocks in §7.3 = 19 functions
  - Note: Step 3 census — identifier mentions 231 lines (§6 48 / §7 90 / §9 93, applied pre-配置规范); chapter-number refs 11 (7 linked; UNRESOLVED L867 "SHE 1.1" = a version number, correctly never linked); prose [n] citations 7/7 converted ([1]×2 [2]×2 [3]×2 [6]×1 — every context names its registry document, no --ref-skip), 6 registry anchors; §7.2 constant bullets 36 report-only; 参见 lines 6 report-only; cross-article: NvM ×23 → SITE memory/nvram_manager, Det ×65 NO-ARTICLE (report-only); two-hop: [1] CryIf / [2] Csm resolve EXTERNAL:? although the Csm article exists — link_candidates.py DOC_TARGETS lacks SWS_CryptoInterface/SWS_CryptoServiceManager (script gap, Backlog class); idempotent second --apply 0 lines
  - Note: Step 4 coverage map — src ch.1→§1 · ch.2 (+2.1)→§2 (+2.1 术语表) · ch.3 (3.1/3.2)→§3 (3.1/3.2) · ch.4→§4 · ch.5 (+5.1/5.1.1)→§5 (+5.1/5.1.1) · ch.6 Requirements Tracing DROPPED · ch.7 (7.1–7.5 incl. 7.2.5.x/7.2.6.x/7.2.7.x)→§6 · ch.8 (8.1–8.6)→§7 (7.1–7.6) · ch.9 n/a→§8 不适用 · ch.10 (10.1 folded into intro, 10.2.1–16, 10.3)→§9 (9.1.1–16, 9.2); no appendix in source. Agent reconstructions from the R22-11 PDF (all reported, none invented): 7.2.7.2 two page-split mapping tables rejoined per-cell; [SWS_Crypto_00261] table spanning chrome row dropped + its requirement sentence recovered; dispatchId formula's lost `||` restored; ASN.1 key-format listings reformatted; 7.1.3 `formula-not-decoded` = `- ID = 1` sub-bullet; [SWS_Crypto_00071] footnotes + 00134/00203/00204/00135 identifier chains rebuilt; config "All Variants" cells and 4 NvBlock callback config paths restored; 5 enumerations rejoined (47/24/37/18/2 literals, PDF-counted — R23-11 adds CRYPTO_ALGOMODE_AESKEYWRAP). Source typos kept verbatim: unit8*/unit32, dispacthId, cryIfKeyId in CRYPTO_E_KEY_NOT_VALID texts, keyPtr (00234), pubValueLengthPtr, cryptoKeyId (00257), CRYPTO_SIGNATUREVERIFY `0x8`
  - Note: glossary +15 new terms (CDD, CSM, CRYIF, CRYPTO, SHE, Crypto Driver Object, Key, Key Type, Key Element, Channel, Job, Crypto Primitive, Operation, Priority, Service — new `## K` section) + 4 来源 appends (DET, HSM, HW, SW); api_reference unchanged (--check 0, spec: already mapped)
  - [x] Step 2 — In-place translation/completion (article 180 → ~2,140 lines; §1–§5 head realigned, §6 completed from 6.1.1-tail, §7/§8/§9 new; 16 figures added)
  - [x] Step 3 — Phase A mechanical checks (evidence above)
  - [x] Step 4 — Phase B coverage map + fidelity (evidence above)
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 — commit first, batched confirmation list at the end of the run; the §3 registry realignment is the one decision flagged for that list)
  - [x] Step 6 — TODO.md row + commit/PR (branch feature/group-crypto-sync · commit recorded below) (SWS_CryptoInterface · R23-11 markdown · ❌ new article, short name CryIf)
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
