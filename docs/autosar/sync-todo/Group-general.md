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
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
- [ ] tr_glossary (AUTOSAR_FO_TR_Glossary · Foundation R23-11 markdown · 📖 reference doc, user-named run #78)
  - Note: 4646 source lines: ch.2.1 = 206 acronym rows; ch.4 = 343 definition terms (6-row tables). Article = docs/autosar/general/tr_glossary/ (TR reference structure, §7 exemption). Merged into 术语表 via gen_glossary ch.2 ingestion; ch.4 definitions to be ingested by a script extension once translated. Tranches committed per batch.
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion (tranches)
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
