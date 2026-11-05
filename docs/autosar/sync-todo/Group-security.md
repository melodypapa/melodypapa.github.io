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
  - [x] Step 5 — User confirmation gate (batch gate 2026-11-06 — user confirmed both rows together per batch instruction)
  - [ ] Step 6 — TODO.md row + commit/PR (TODO.md row + article commit done: f9a5075 firewall / 27415df idsm)
- [ ] idsm (SWS_IntrusionDetectionSystemManager · R23-11 markdown · ❌ new article, short name IdsM)
  - Note: 2026-11-06 run — source ch.2 has no 2.1/2.2 subsections; rendered flat with the source's own table order (32 Abbreviation/Acronym rows then 17 Terms rows) separated by the table-header lead-ins 「缩写 / 首字母缩略词」 / 「术语」
  - Note: source 3.1/3.2 order reversed vs canonical (3.1 Related Specification, 3.2 Input Documents) — mirrored as the source has it
  - Note: source heading typo kept: 10.1.17 "IdsMEventTpTxPdu" (container name IdsMTpTxPdu); 8.3.11 "IdsMContextDataModifierCallout_Name" missing underscore → article uses the correct identifier, check_api_sync ALIASES entry added (CoreTest precedent)
  - Note: source 5.2 file-structure image is the recurring page chrome (345×35) — dropped; 22 content figures embedded (Figure5-1, 7-1..7, 9-1..3, 10-1..11)
  - Note: source 9.2 Timestamp Sequence Diagrams contains both StbM (Fig 9.2) and custom (Fig 9.3) diagrams — merged into article §8.2; the 6.7 prose ref "see 9.3" renumbered to §8.2
  - Note: appendix lettered A in the source (Change history of AUTOSAR traceable items) → ## A. with GFM tables A.1/A.2 (sanctioned ID location)
  - Note: §7.5 调度函数 has no entries in the source (intro prose only) — chapter kept with the intro sentence
  - Note: glossary +4 new entries (Filter/Sensor/Sink/Timestamp Provider) + 10 来源 appends (one-term-once)
  - Note: links --apply 104 lines (identifier 104 incl. §6/§7, chapter-ref 10, citation 13, registry anchors 7), idempotent re-run 0
  - [x] Step 1 — Source resolution + gap analysis
  - [x] Step 2 — In-place translation/completion
  - [x] Step 3 — Phase A mechanical checks (strict build 0 WARNING; check_indexes/heading-lang/api-sync OK incl. alias; hygiene greps clean — IDs only in appendix A)
  - [x] Step 4 — Phase B coverage map + fidelity
  - [x] Step 5 — User confirmation gate (batch gate 2026-11-06 — user confirmed both rows together per batch instruction)
  - [ ] Step 6 — TODO.md row + commit/PR (TODO.md row + article commit done: f9a5075 firewall / 27415df idsm)

## Not queued (deliberately skipped)
- (none)
