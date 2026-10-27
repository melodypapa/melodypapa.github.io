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
- [x] bsw_general (SWS_BSWGeneral · R23-11 markdown · ❌ new article)
  - Note: general specification of Basic Software modules — input document [2] of every module article, global foundation, worth translating early; directory `general/bsw_general/` (naming per mapping.md, lowercase snake_case)
  - Note: Step 1 findings (2026-10-27): source 2558 lines, R23-11 markdown confirmed. Droppable = source ch.6 Requirements Tracing only; no Known-Limitations chapter (source 4.1 Limitations is a normal section). Source appendix "A Change History" is a change-history annex (NOT the droppable NA-requirements appendix) — translates per the appendix-B rule as `## B. AUTOSAR 可追溯项变更历史` (content-class match; the heading audit forbids `## A.`); item-ID lists verbatim in fences, R23-11 changed list = none, deleted = [SWS_BSW_00039].
  - Note: figure triage (sips): one real content figure — image_000057 (hash bf1073d6, 798×342, near the "Figure 7.1" caption in source 7.2.5.6) → copied as Figure7-1.png. All other refs are known deco (8c27c74a ×50, f5f4bf49 ×6, cad1600a ×4, 31a8ee06 ×6) or recurring chrome (a133f680 ×5, c94f11d1 ×5, d9461527 ×8, e61809f4 ×2) or a 22×21 px icon (d29690e1).
  - Note: 5 `formula-not-decoded` placeholders reconstructed from context + the R4.3.1 PDF: `<Mip> = <Ma>[_<vi>_<ai>]`, `<Mip>[_<Ie>]*.*`, `<Mip>_<Vn>`, `<Ma><Tn>`, `<MIP>_<PI>`. R4.3.1 Table 1 has 4 extra header-file rows vs R23-11 Table 5.1 — R25-11 has the same 8 rows as R23-11, kept 8.
  - Note: two R23-11-vs-other-release discrepancies kept as parsed from R23-11 (source of record): OS-services table row CheckObjectOwnership = RTE/MCAL/StbM only (R22-11 and R25-11 mark all five); config-template Scope row lists only LOCAL (the R4.3.1 PDF also has an ECU bullet; R25-11 markdown lost the row entirely).
  - Note: source quirks kept verbatim: "ModeSwitchInferface" (8.7), the Det_ReportRuntimeError mention in 7.2.4.4's closing sentence; 6.1.16's "See Table in [SWS_BSW_00257]" rendered as the single table under that item.
  - Note: Step 2 decisions: source appendix "A Change History" → `## B. AUTOSAR 可追溯项变更历史` (content-class match with the standard's appendix-B rule; heading audit forbids `## A.`). Intra-document requirement references ("See also [SWS_BSW_xxxxx]") → bold item titles, anchor-less (items carry no anchors on this site); references to OTHER documents' requirements kept verbatim escaped per source ([SWS_Rte_01006], [SWS_Rte_07131], [SRS_BSW_00337], [SWS_Dem_00256], RS_Arti_00042); chapter references to the *respective module's own* SWS (its ch.7/8/10) deliberately NOT renumbered.
  - Note: Phase A census (2026-10-27): identifier mentions (applied class) 0 — the source ch.8 defines no concrete API items, so §7 has no identifier-titled headings; §7.2 constant bullets 0; 参见/参考/详见 lines 13 (report-only); prose [n] citations 72 applied + 18 registry anchors, 0 UNRESOLVED, idempotent (second --apply: 0 lines); two-hop classes: [3] Glossary → SITE (site glossary), [1]-[2],[4]-[18] EXTERNAL (need curated URLs — user decision, Backlog class); cross-article module mentions (report-only): DEM ×23 → diagnostics/diagnostic_event_manager, EcuM ×5 → mode_management/ecu_state_manager, BswM ×3 → mode_management/basic_software_mode_manager, NvM ×2, Dcm ×1 (SITE), Det ×19 / CanIf ×5 / Nm ×2 / Mcu ×1 / Sd ×1 NO-ARTICLE.
  - Note: link_candidates.py fix in this run: `_registry_sec` gained a fallback for a §3.1 registry with NO §3.2 (bsw_general's source ch.3 has no "Related specifications" section) — the slice now ends at the next `## ` heading; without it all 90 citations were misclassified UNRESOLVED.
  - Note: check_api_sync exit 1 = known parser artifact, manually verified: source 8.3.x headings are prose titles (General specification on API functions / Initialization function / De-Initialization function / Get Version Information — the script truncates them to first words), not function identifiers; article §7.3.1–7.3.4 are their site-convention Chinese translations, count 4↔4, names and order 1:1; 0 `**说明**` blocks is correct (prose template sections, not per-function entries — same class as CoreTest's manual verification).
  - Note: Phase B coverage map: ch.1→§1 (1.1, 1.2) · ch.2→§2 (13 rows, order verified line by line) · ch.3→§3 (3.1 [1]–[18]; no 3.2 in source = compliance) · ch.4→§4 · ch.5→§5 (5.1–5.1.8 incl. 5.1.6.1–4, 5.1.7.1–2) · ch.6 Requirements Tracing → dropped (forbidden) · ch.7→§6 (6.1.1–6.1.19 incl. 6.1.18.1–2/6.1.18.2.1–2, 6.2.1–6.2.6, 6.3.1–6.3.4, 6.4, 6.5) · ch.8→§7 (7.1–7.7) · ch.9→§8 (one-sentence chapter per source) · ch.10→§9 (9.1–9.3, template tables, no containers) · appendix A→`## B.`. No Known-Limitations chapter in source (compliance). 1 content figure (Figure7-1.png) embedded; all deco/chrome images dropped. Source-table conversions: Table 5.1 (8 rows, R25-11-verified), Table 7.1 (66 rows; two R23-11 conversion-garbled cells "√ √" resolved to single √), Table 10.1 (8 rows), config-template tables (merged cells collapsed; Range row keeps both sentences; footnotes 1–6 as blockquotes).
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (N/A per user instruction 2026-10-27 "no confirmed one by one" — per-row gate waived; evidence recorded in Notes and the PR)
  - [x] Step 6 — TODO.md row + commit/PR (commit 2bc57c2 on feature/bsw-general-sync; no PR — parent session handles GitHub)
- [ ] platform_types_2 (SWS_PlatformTypes · R23-11 markdown · ❌ new article)
  - Note: a different document from SWS_StandardTypes (noted in TODO.md); directory must not collide with platform_types (suggest `platform_types_std/`, or decide in Step 1 and propose to the user if unclear)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] communication_stack_types (SWS_CommunicationStackTypes · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

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
