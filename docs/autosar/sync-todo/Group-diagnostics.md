# Sync todo: Group diagnostics — diagnostics section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] diagnostic_event_manager (SWS_DiagnosticEventManager · R23-11 markdown · ⚠️ gaps)
  - Note: missing constraints/dependencies/API chapters; unnumbered heading break (dem numbering gap, already tracked in TODO.md)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] j1939dcm (SWS_SAEJ1939DiagnosticCommunicationManager · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] diagnostic_communication_manager (SWS_DiagnosticCommunicationManager · R23-11 markdown · ⚠️ 24k-line source, giant — last)
  - Note: currently only the introduction + acronyms; present a chapter-by-chapter plan first per SKILL.md Step 3 (suggest splitting the 7-chapter skeleton across several runs)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
