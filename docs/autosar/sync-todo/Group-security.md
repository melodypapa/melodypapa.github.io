# Sync todo: Group security — security section (new section)

Base: R23-11 · Generated: 2026-10-24 · Queue order = row order
(Resume = the first row still `[ ]`; all `[x]` = batch complete)
Steps: ① source resolution + gap analysis · ② in-place translation/completion · ③ Phase A mechanical checks · ④ Phase B evidence · ⑤ user confirmation gate · ⑥ TODO.md row + commit
> This batch must first create the section landing page `docs/autosar/security/index.md` (STANDARD.md §6 format) and register it in the nav — folded into the first row's Step 2.

## Queue

- [ ] firewall (SWS_Firewall · R23-11 markdown · ❌ new article)
  - Note: the first run also creates the `security/` landing page + nav registration
  - Note: 2026-11-06 run — new section created: `docs/autosar/cp/security/index.md` landing + nav group 「网络安全」 (label choice user-confirmable; existing 信息安全 group = crypto) + CP overview block
  - Note: source heading 10.2.1 "FirewallGeneral" rendered as module heading Firewall (conversion artifact — the section opens with the module table [ECUC_Fw_00001])
  - Note: source places FirewallSomeipMajorVersion/MinorVersion container tables before the 10.2.3.8 heading; placed inside §9.2.3.8 after their Included-Containers row (logical position)
  - Note: Fw_InspectPacket source Syntax line is truncated; signature reconstructed with Fw_InspectionResultType* InspectionResultPtr (out-param row confirms it)
  - Note: source typos kept verbatim (user-decision list): FirewallTransportLayerFilterConfig range requirement repeats FirewallFilterPortLowerValue for the DestPort upper bound; param names FirwallEnableSecurityEventReporting / FirewallPaylodByteOffset / FirewallPaylodByteValue / FirewallITrafficClass; FirewallDoipDestAddress + FirewallDoipSrcAddress descriptions say "source port filter"; FirewallDoipSrcAddressUpperValue description "filter port upper value"; FirewallingWithPerStreamFiltering description duplicates FirewallEthIfSwitchRef's; FirewallNetworkLayerIpv4FilterConfig description says "for IPv6"
  - Note: check_api_sync.py extended with _reconcile_module_prefix (source headings are bare Init/ConfigType/etc., article uses Fw_*); applied class links --apply 42 lines, idempotent re-run 0
  - Note: 26 content figures embedded by source caption number (Figure7-1..5, 9-1..3, 10-1..18); deco cluster (345×36-39 page chrome, 21×21 icons) excluded by hash+pixel census
  - Note: glossary +10 new entries (Allowlist/Blocklist/DDS/DDS-RTPS/DoIP/Firewall Rule/Firewall State/OSI Layer/TCAM/UCM) + 11 来源 appends (one-term-once)
  - Note: omissions — source ch.6 Requirements Tracing + appendix A dropped (droppable set); no N/A.-only sections encountered
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks (strict build 0 WARNING; check_indexes/heading-lang/api-sync OK; hygiene greps clean)
  - [x] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate (batch gate — user asked for combined confirmation at batch end)
  - [ ] Step 6 — TODO.md row + commit/PR
- [ ] idsm (SWS_IntrusionDetectionSystemManager · R23-11 markdown · ❌ new article, short name IdsM)
  - [ ] Step 1 — Source resolution + gap analysis
  - [ ] Step 2 — In-place translation/completion
  - [ ] Step 3 — Phase A mechanical checks
  - [ ] Step 4 — Phase B coverage map + fidelity
  - [ ] Step 5 — User confirmation gate
  - [ ] Step 6 — TODO.md row + commit/PR

## Not queued (deliberately skipped)
- (none)
