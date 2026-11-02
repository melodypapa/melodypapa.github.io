# Sync todo: Group libraries — libraries section (new section)

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> This batch must first create the section landing page `docs/autosar/cp/libraries/index.md` (STANDARD.md §6 format) and register it in the nav — folded into the first row's Step 2.

## Queue

- [ ] crc (SWS_CRCLibrary · R23-11 markdown · ❌ new article, short name Crc)
  - Note: 2026-11-03 batch run — user pre-approved per-article commits without the per-article Step 5 gate; all confirmations collected once at batch end.
  - Note: the `libraries/` landing page + nav group already existed (PR #244); this run added the nav entry "CRC" + landing-page/CP-overview rows instead.
  - Note: batch decision (gate pending) — literal "None." groups inside the §7 API chapter render as one-sentence statements and keep source positions 8.1–8.7 → 7.1–7.7 (7.2 类型定义/7.4 回调通知/7.6.1–7.6.3/7.7; check_api_sync is positional 7.2=types/7.3=functions, omission+renumber would fail it); outside §7 the placeholder rule applies: source 7.5 Debugging concept "None" omitted, §7.6→§6.5 renumbered.
  - Note: check_api_sync N/A — source 8.3.x leaf headings are prose ("8-bit SAE J1850 CRC Calculation") that translate to Chinese by design; manual verification: source 8.3.1–8.3.5 groups ↔ article 7.3.1–7.3.5, 8 function entries (CRC8/8H2F/16/16ARC/32/32P4/64/GetVersionInfo) in source order with 8 **说明** blocks.
  - Note: §6.1 formulas reconstructed from the bundled R22-11 PDF (R23-11 markdown carries `formula-not-decoded`); figures: 7 sequence diagrams (Figure9-1..9-7) + 2 container-diagram page fragments (Figure10-1/10-2), deco images triaged out by 345x36 hash cluster.
  - Note: [5] ITU-T X.25 URL replaced — source http dologin_pub.asp returns 500; publisher's current https://www.itu.int/rec/T-REC-X.25-199610-I/en verified 200. [7] en.wikipedia.org unreachable from this machine (curl 000 incl. root domain) — link kept as-is.
  - Note: appendix B ID lists verbatim in fences; B.1.2 23 IDs diffed against source — exact match.
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (deferred to batch-end joint confirmation)
  - [x] Step 6 — TODO.md row + commit/PR (commit 209cfc5; TODO.md ✅ row added; batch PR pending user confirmation)
- [ ] e2e (SWS_E2ELibrary · R23-11 markdown · ❌ new article, short name E2E; note this is a different document from cp/communication/e2e_transformer)
  - Note: 2026-11-03 batch run — committed without the per-article Step 5 gate (batch-end joint confirmation), same as the crc row.
  - Note: check_api_sync GREEN (62 types / 91 functions / 91 **说明** blocks, names+order match) — this document's identifier-named leaves align with the script's positional 7.2/7.3 assumption.
  - Note: source 7.1.5 Extended Production Errors has NO body even in the R22-11 PDF (heading is the last line of page 33) — omitted per the placeholder rule. Source ch.6 Requirements Tracing + annex C dropped per mandate. Annex A (safety manual) → §10, Annex B (application hints) → §11, Annex D → ## B.
  - Note: P01 CheckStatusType E2E_P01STATUS_OK=0x00 row lost in the R23-11 markdown conversion — recovered from the bundled R22-11 PDF (UML + table); the P02 MapStatusToSM INITIAL-row merge-cell artifact likewise reconstructed from the PDF.
  - Note: ~20 service tables were page-break scrambled in the conversion (e.g. [SWS_E2E_00600] mapping table landed inside the P04mProtect section) — content restored to its owning entry; P04mForward/P08mProtect/P44mProtect syntax tails truncated by the converter, reconstructed from the R22-11 PDF or the entry's own parameter table.
  - Note: Figure B.20 (Mapping of Data elements into I-PDU) image is absent from the source conversion — caption kept as text.
  - Note: --apply converted the bit-offset example's Data[1]/Data[2] table cells as citation markers — reverted manually (they are array subscripts, not [n] citations); comma forms [1, ...]/[3, ...] converted to #ref links; constant-bullet mentions (207) stay report-only.
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (deferred to batch-end joint confirmation)
  - [x] Step 6 — TODO.md row + commit/PR (commits cd14a65 (crc caption fixup) + 0a3139e; batch PR pending user confirmation)
- [ ] bfx (SWS_BFXLibrary · R23-11 markdown · ❌ new article, short name Bfx)
  - Note: 2026-11-03 batch run — RUN STOPPED HERE per user instruction mid-batch ("stop when this translation finished"); bmc/mfl/mfx/ifl/ifx/efx rows still pending.
  - Note: committed without the per-article Step 5 gate (batch-end joint confirmation), same as the crc/e2e rows.
  - Note: source ch.9 Sequence diagrams = "Not applicable" → omitted per the placeholder rule; ch.10 配置规范 renumbered to §8 (no 时序图 chapter present).
  - Note: check_api_sync trivially OK but N/A in substance — source functions live under 8.4 with stem-titled headings (Bfx_SetBit) whose templated prototypes expand one stem into 4 concrete functions (u8/u16/u32/u64); manual verification: 24 sections in source order + 8.8 GetVersionInfo → §7.8.
  - Note: source §3.2 prose names "IFX Library" (source copy-paste artifact from the IFX document) — translated verbatim, faithful to source.
  - Note: source §8.1 cites [6] Platform_Types.h but the §3.1 registry only has [1]–[4] — dangling source reference, left as prose (UNRESOLVED per census).
  - Note: appendix B is "History of Specification Items" with a numbered GFM table (Table B.1) including empty Heading cells — translated as table with IDs as data.
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (deferred to batch-end joint confirmation)
  - [x] Step 6 — TODO.md row + commit/PR (commit b11a226; batch PR pending user confirmation)
- [ ] bmc (SWS_BSWMulticoreLibrary · R23-11 markdown · ❌ new article, short name Bmc)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] mfl (SWS_MFLLibrary · R23-11 markdown · ❌ new article, short name Mfl)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] mfx (SWS_MFXLibrary · R23-11 markdown · ❌ new article, short name Mfx)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] ifl (SWS_IFLLibrary · R23-11 markdown · ❌ new article, short name Ifl)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] ifx (SWS_IFXLibrary · R23-11 markdown · ❌ new article, short name Ifx)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] efx (SWS_EFXLibrary · R23-11 markdown · ❌ new article, short name Efx)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
