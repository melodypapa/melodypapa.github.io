# Sync todo: Group memory — memory section

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit

## Queue

- [ ] memory_access (SWS_MemoryAccess · R23-11 markdown · ⚠️ missing API chapter)
  - Note: missing "API 规范" chapter (one of the "6 articles missing only the API chapter"); 3.1 "输入文件及相关标准规范" → "输入文件"; 4.2 "适用于汽车领域" → "汽车域的适用性"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] memory_mapping (SWS_MemoryMapping · R23-11 markdown · ⛔ stub — full translation)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] bulk_nv_data_manager (SWS_BulkNvDataManager · R23-11 markdown · 🔶 alignment)
  - Note: ch.1 "介绍和功能概述" → "简介和功能概述"; 3.1 variant → "输入文件"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] flash_driver (SWS_FlashDriver · R23-11 markdown · 🔶 alignment)
  - Note: delete the bespoke "错误处理" chapter (folded into 6.6 error classification) and the forbidden "配置规范" chapter
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] nvram_manager (SWS_NVRAMManager · R23-11 markdown · 🔶 alignment)
  - Note: delete the forbidden "需求追踪" chapter; "功能说明" → "功能规格"; 4.2 "汽车领域的适用性" → "汽车域的适用性"
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] flash_eeprom_emulation (SWS_FlashEEPROMEmulation · R23-11 markdown · ⚠️ gaps)
  - Note: missing constraints/dependencies chapters; 3.1 "输入文件" ✓; 4.2 currently "地址计算" — verify ch.4's actual subsections against the source structure
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] ea (SWS_EEPROMAbstraction · R23-11 markdown · ❌ new article, short name Ea)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] eep (SWS_EEPROMDriver · R23-11 markdown · ❌ new article, short name Eep)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] memory_abstraction_interface (SWS_MemoryAbstractionInterface · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] memory_driver (SWS_MemoryDriver · R23-11 markdown · ❌ new article)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] flstst (SWS_FlashTest · R23-11 markdown · ❌ new article, short name FlsTst)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] ramtst (SWS_RAMTest · R23-11 markdown · ❌ new article, short name RamTst)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- 📖 nv_data_handling_guideline — EXP_NVDataHandling (skeleton-exempt; an update needs its own run)
