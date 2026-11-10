# Sync todo: finished rows — condensed archive

Consolidated 2026-11-11 from the former per-batch `Group-<section>.md` queue files (the two-group regroup that matches [`../TODO.md`](../TODO.md) `## Finished（已完成）`).
One condensed record per done row: article · spec · done date · commits · PRs — the full row blocks (Notes, 6-step evidence) live in the git history of the deleted per-batch files and in the article's [`../TODO.md`](../TODO.md) row. Reopening a row: recreate it in [Group-unfinished.md](Group-unfinished.md) with `- Note: reopen <reason> <date>` (todo-format.md reopen rule).

---

## Sync todo: Group io — IO section wrap-up — source batch `Group-io.md` (7 done)

- [x] dio_driver (SWS_DIODriver) — done 2026-10-24 · commits de11d8a/493ed12/e21067f/04a009f/a5e12c2 · PR #53/#66
- [x] port_driver (SWS_PortDriver) — done 2026-10-24 · commits ee486aa · PR #53
- [x] pwm_driver (SWS_PWMDriver) — done 2026-10-24 · commits 1b5e44b/b156916 · PR #57
- [x] ocu_driver (SWS_OCUDriver) — done 2026-10-24 · commits b156916/05418fb · PR #63/#66
- [x] icu_driver (SWS_ICUDriver) — done 2026-10-24 · commits d11d759/9cb8764 · PR #68
- [x] adc_driver (SWS_ADCDriver) — commits 3d8dd12/625d437 · PR #76
- [x] iohwab (SWS_IOHardwareAbstraction) — commits 72a103c · PR #120

---

## Sync todo: Group general — general/base specifications — source batch `Group-general.md` (4 done)

- [x] platform_types (SWS_StandardTypes) — PR #120/#135
- [x] bsw_general (SWS_BSWGeneral) — commits 2bc57c2
- [x] platform_types_2 (SWS_PlatformTypes) — PR #123/#135
- [x] communication_stack_types (SWS_CommunicationStackTypes) — commits faa0806

---

## Sync todo: Group crypto — crypto section — source batch `Group-crypto.md` (4 done)

- [x] crypto_service_manager (SWS_CryptoServiceManager) — PR #221
- [x] crypto_driver (SWS_CryptoDriver) — commits 8b73b6f
- [x] cryif (SWS_CryptoInterface) — commits c2cba4b
- [x] keym (SWS_KeyManager) — commits 6e52dca

---

## Sync todo: Group system_services — system services section — source batch `Group-system_services.md` (7 done)

- [x] det (SWS_DefaultErrorTracer) — commits 30510c9
- [x] function_inhibition_manager (SWS_FunctionInhibitionManager) — commits 534d5d1
- [x] time_service (SWS_TimeService) — commits 5c57d0a
- [x] comm (SWS_COMManager) — commits bcf713d · PR #230
- [x] swcluc (SWS_SoftwareClusterConnection) — commits f1a0b2a · PR #272
- [x] hwtestmanager (SWS_HWTestManager) — commits 04ea38b · PR #272
- [x] operating_system (SWS_OS) — commits ca7ecda/fb8e565 · PR #110

---

## Sync todo: Group mode_management — mode management section — source batch `Group-mode_management.md` (2 done)

- [x] basic_software_mode_manager (SWS_BSWModeManager) — commits e7b893e · PR #229/#70
- [x] ecu_state_manager (SWS_ECUStateManager) — commits 37ee564 · PR #70/#92

## Not queued (deliberately skipped)
- 📖 guide_to_mode_management — EXP_ModeManagementGuide (skeleton-exempt; a retranslation/update needs its own run)
  - Note: 2026-10-27 PDF ground-truth census (`--list --pdf`): 167 annotations, 96 in body; all 6 citations `registry MATCH`, 9/9 figures mentioned by number, 17/17 section refs resolve once the chapter map falls back to same-number identity for non-Type-A titles (EXP guides drop nothing). `--apply`: 13 citation links + 6 registry anchors + 17 chapter-ref links — exactly the 17 section links the source PDF carries. Script guard added from this dry-run: 清单3.4 / 示例3.4 are the source's `lstlisting.3.N` code-listing numbers, not sections (they had linked to §3.4 通信管理) — 清单/示例 now join the 图/表 prefix guard. 3 source footnote links vs 0 `<sup>` markers — NOT a gap: all three are translated inline (§2 "在R4.0中…限于单个分区" parenthetical, §3.1 "本文档假定…很大程度上被生成", Listing 3.24's 注意 on BswMJ1939Rm). ARTechTerm dests (mode manager, mode user, …) are the guide's §4.1 glossary terms, anchor-less by design.
  - Note: 2026-10-25 audit-fix pass (5 parallel chapter reviews vs R23-11 source) applied WITHOUT queueing: NEW unnumbered `## 参考文献` (References [1]–[6], source position before ch.1 — the article's inline [1]/[2]/[3] citations were previously unresolvable); §1.1 后续工作 restored as a heading + the omitted "enhanced in further releases" sentence; LOW fixes: sample-ECU framing (code listings together form the config), possible-assignments wording + [2] metamodel citation marker, ModeControlContainer name, "Among other things" ≠ 尤其, 3 typos (将会话/以下/会解释了), translator's note on Listing 3.32's PNC2/PNC3 source-extraction corruption. Verified NON-issues: the review agent's "~20 missing figures in §3.4" refuted by size/hash forensics — all are ~7.9KB page-decoration placeholders; the guide's defensible normalizations (OnExtry, requested-State hyphen, ETH_MODE_ACTIV) kept. Strict build 0 WARNING.
  - Note: 2026-10-25 potential links (user: "improve the potential link for this document"): the guide has NO applied-class candidates (EXP doc — no API-chapter heading structure; identifier defs 0 by design). Census improvements landed in link_candidates.py: (a) `## 参考文献` now recognized as a citation registry (fallback when the article's §3.1 holds no [n] entries — guide chapters number their sections 3.1 too); (b) guide References reformatted to the house registry style (line-start [n] Title / > DOCID); (c) DOC_TARGETS + swsdiagnosticcommunicationmanager→SITE Dcm article, +TPS_SWCT/TPS_BSWModuleDescriptionTemplate labels; (d) EcuM regression unchanged. Guide citation census: [4] BswM article SITE x4, [5] Dcm article SITE x2, [6] Glossary SITE x1, [1] TPS_SWCT/[2] MetaModel/[3] TPS_BSWMDT EXTERNAL. Report-only candidates awaiting user decision: module mentions BswM x104 (guide's own subject — linking every mention would be noise), EcuM x29, ComM x27, Dcm x14, Nm x9; SITE citations [4] x4, [5] x2.

---

## Sync todo: Group diagnostics — diagnostics section — source batch `Group-diagnostics.md` (3 done)

- [x] diagnostic_event_manager (SWS_DiagnosticEventManager) — commits c5b4a25/1f4ef62/c9eb370/3b24e95/bef51d2/e0a20f3/b53d643/7a0055d · PR #183/#186
- [x] j1939dcm (SWS_SAEJ1939DiagnosticCommunicationManager) — commits 8795b71 · PR #200/#225
- [x] diagnostic_communication_manager (SWS_DiagnosticCommunicationManager) — commits 24c7a36 · PR #196/#225

---

## Sync todo: Group memory — memory section — source batch `Group-memory.md` (12 done)

- [x] memory_access (SWS_MemoryAccess) — commits 702c88d/afacc02 · PR #131
- [x] memory_mapping (SWS_MemoryMapping) — commits fc5a540 · PR #144
- [x] bulk_nv_data_manager (SWS_BulkNvDataManager) — commits 6cfad2c · PR #223
- [x] flash_driver (SWS_FlashDriver) — commits 34fa711 · PR #223
- [x] nvram_manager (SWS_NVRAMManager) — commits afba0fe · PR #223
- [x] flash_eeprom_emulation (SWS_FlashEEPROMEmulation) — commits b440607 · PR #248
- [x] ea (SWS_EEPROMAbstraction) — commits b19e4a8 · PR #248
- [x] eep (SWS_EEPROMDriver) — commits 75b9fcf · PR #248
- [x] memory_abstraction_interface (SWS_MemoryAbstractionInterface) — commits df003cd · PR #248
- [x] memory_driver (SWS_MemoryDriver) — commits 04145b5 · PR #248
- [x] flstst (SWS_FlashTest) — commits 1040e9e · PR #248
- [x] ramtst (SWS_RAMTest) — commits 95babf9 · PR #248

## Not queued (deliberately skipped)
- 📖 nv_data_handling_guideline — EXP_NVDataHandling (skeleton-exempt; an update needs its own run)

---

## Sync todo: Group communication — communication section — existing articles + backbone — source batch `Group-communication.md` (24 done)

- [x] can_network_management (SWS_CANNetworkManagement) — commits 3a7fa89 · PR #139
- [x] udp_network_management (SWS_UDPNetworkManagement) — commits 3a7fa89 · PR #139
- [x] can_driver (SWS_CANDriver) — commits 3a7fa89 · PR #139
- [x] can_transceiver_driver (SWS_CANTransceiverDriver) — commits e48b58e/3a7fa89 · PR #181
- [x] pdu_router (SWS_PDURouter) — commits f915d45/3a7fa89 · PR #181
- [x] ethernet_interface (SWS_EthernetInterface) — commits a08b183/3a7fa89 · PR #181
- [x] lin_interface (SWS_LINInterface) — commits c6dd02b/aad6b21/3a7fa89 · PR #181
- [x] com_based_transformer (SWS_COMBasedTransformer) — commits 3562899/3a7fa89 · PR #181
- [x] e2e_transformer (SWS_E2ETransformer) — commits 4d5ff96/3a7fa89 · PR #181
- [x] data_distribution (SWS_DataDistributionService) — commits b2c1ffb/3a7fa89 · PR #188
- [x] sec_oc (SWS_SecureOnboardCommunication) — commits 3d584a2/3a7fa89 · PR #188
- [x] soad (SWS_SocketAdaptor) — commits 1b9bf69 · PR #188
- [x] mirror (SWS_BusMirroring) — commits c3e84ef · PR #192
- [x] ethernet_switch_driver (SWS_EthernetSwitchDriver) — commits 7f5fc5e/3a7fa89 · PR #192
- [x] service_discovery (SWS_ServiceDiscovery) — commits 23b20e5/3a7fa89 · PR #192
- [x] com (SWS_COM) — commits 17cdb70/3a7fa89 · PR #192
- [x] cansm (SWS_CANStateManager) — commits a803400/3a7fa89 · PR #192
- [x] cantp (SWS_CANTransportLayer) — commits 5e2624d/3a7fa89 · PR #192/#206
- [x] tcpip (SWS_TcpIp) — commits bcbd61e/3a7fa89 · PR #206
- [x] nm (SWS_NetworkManagementInterface) — commits 5036abf/3a7fa89 · PR #206
- [x] ethsm (SWS_EthernetStateManager) — commits 37c98ec/3a7fa89 · PR #206
- [x] ipdum (SWS_IPDUMultiplexer) — commits 5cef2ca/3a7fa89 · PR #206
- [x] someipxf (SWS_SOMEIPTransformer) — commits e411562/3a7fa89 · PR #206
- [x] someiptp (SWS_SOMEIPTransportProtocol) — commits af4d193/3a7fa89 · PR #206

## Not queued (deliberately skipped)
- 📖 fvm/fvm.md — topic article derived from SecOC appendix A (no standalone specification)
- 📖 cp/others/full_can_vs_basic_can/ — topic sub-page (moved out of can_driver 2026-11-04)
- 📖 can_network_management/r21_11/ — R21-11 historical snapshot
> Suggested backbone order: Com → CanTp → CanSM → Nm → TcpIp → EthSM → IpduM → SomeIpXf → SomeIpTp
> (CanSM/Nm/EthSM depend on terminology already translated in CanIf/CanNm; the sources cross-reference heavily — check existing article wording before translating a cross-reference.)

---

## Sync todo: Group mcal — MCAL section (new section) — source batch `Group-mcal.md` (3 done)

- [x] mcu (SWS_MCUDriver) — commits 2f0e714 · PR #104/#94
- [x] gpt (SWS_GPTDriver) — commits 065baee · PR #106
- [x] coretest (SWS_CoreTest) — commits 1abff90 · PR #108

---

## Sync todo: Group globaltime — global time cluster (new section) — source batch `Group-globaltime.md` (4 done)

- [x] stbm (SWS_SynchronizedTimeBaseManager) — commits 53cd591
- [x] can_tsyn (SWS_TimeSyncOverCAN) — commits 364c4fd
- [x] eth_tsyn (SWS_TimeSyncOverEthernet) — commits 8f01771
- [x] fr_tsyn (SWS_TimeSyncOverFlexRay)

---

## Sync todo: Group libraries — libraries section (new section) — source batch `Group-libraries.md` (9 done)

- [x] crc (SWS_CRCLibrary) — commits 209cfc5 · PR #244/#250
- [x] e2e (SWS_E2ELibrary) — commits cd14a65 · PR #250
- [x] bfx (SWS_BFXLibrary) — commits b11a226 · PR #250
- [x] bmc (SWS_BSWMulticoreLibrary) — commits 18f9ee6 · PR #265
- [x] mfl (SWS_MFLLibrary) — commits f47a7ee · PR #265
- [x] mfx (SWS_MFXLibrary) — commits 71821da · PR #265
- [x] ifl (SWS_IFLLibrary) — commits da855e3 · PR #265
- [x] ifx (SWS_IFXLibrary) — commits 1089ec8 · PR #265
- [x] efx (SWS_EFXLibrary) — commits bed2f8c · PR #265

---

## Sync todo: Group safety — safety section (new section) — source batch `Group-safety.md` (3 done)

- [x] wdgm (SWS_WatchdogManager) — done 2026-10-26 · commits 24c7a36 · PR #118/#116/#196
- [x] wdgif (SWS_WatchdogInterface) — done 2026-10-26 · commits 24c7a36 · PR #196
- [x] wdg (SWS_WatchdogDriver) — done 2026-10-27 · commits 24c7a36 · PR #196

---

## Sync todo: Group security — security section (new section) — source batch `Group-security.md` (2 done)

- [x] firewall (SWS_Firewall) — PR #286
- [x] idsm (SWS_IntrusionDetectionSystemManager) — PR #286

---

## Sync todo: Group rte-swarch — RTE / SWArch section (new section) — source batch `Group-rte-swarch.md` (2 done)

- [x] rte (SWS_RTE) — done 2026-10-25 · commits 67b0783/bc7d8e6/585938b/278e287/8f94429/b4861ac/9143a4a/011c599 · PR #116/#295
- [x] arti (SWS_ARTI) — commits b4861ac · PR #295

---

## Sync todo: Group communication-2 — communication section — remaining missing documents (38) — source batch `Group-communication-2.md` (38 done)

- [x] spi (SWS_SPIHandlerDriver) — PR #141
- [x] ldcom (SWS_LargeDataCOM) — PR #177
- [x] lsdu (SWS_LSduRouter) — PR #177
- [x] dlt (SWS_DiagnosticLogAndTrace) — PR #177
- [x] doip (SWS_DiagnosticOverIP) — PR #177
- [x] xcp (SWS_XCP) — PR #177
- [x] canxl_driver (SWS_CANXLDriver) — PR #190
- [x] canxl_transceiver_driver (SWS_CANXLTransceiverDriver) — PR #190
- [x] eth_trcv (SWS_EthernetTransceiverDriver) — PR #190
- [x] wlan_driver (SWS_WirelessEthernetDriver) — PR #190
- [x] wlan_transceiver_driver (SWS_WirelessEthernetTransceiverDriver) — PR #190
- [x] flexray_driver (SWS_FlexRayDriver) — PR #190
- [x] flexray_interface (SWS_FlexRayInterface) — PR #208
- [x] flexray_nm (SWS_FlexRayNetworkManagement) — PR #208
- [x] flexray_sm (SWS_FlexRayStateManager) — PR #208
- [x] flexray_trcv (SWS_FlexRayTransceiverDriver) — PR #208
- [x] flexray_ar_tp (SWS_FlexRayARTransportLayer) — PR #208
- [x] flexray_iso_tp (SWS_FlexRayISOTransportLayer) — commits a65bdec · PR #232
- [x] linsm (SWS_LINStateManager)
- [x] lintrcv (SWS_LINTransceiverDriver)
- [x] ttcan_driver (SWS_TTCANDriver)
- [x] ttcan_interface (SWS_TTCANInterface)
- [x] j1939nm (SWS_SAEJ1939NetworkManagement)
- [x] j1939rm (SWS_SAEJ1939RequestManager)
- [x] j1939tp (SWS_SAEJ1939TransportLayer)
- [x] ieee1722tp (SWS_IEEE1722TransportLayer)
- [x] macsec (SWS_MACsecKeyAgreement)
- [x] cellularv2x_driver (SWS_CellularV2XDriver) — PR #269
- [x] chargingmanager (SWS_ChargingManager) — PR #269
- [x] chinesev2x_mgmt (SWS_ChineseV2XManagement) — PR #269
- [x] chinesev2x_msg (SWS_ChineseV2XMessage) — PR #269
- [x] chinesev2x_net (SWS_ChineseV2XNetwork) — PR #269
- [x] chinesev2x_sec (SWS_ChineseV2XSecurity) — PR #269
- [x] v2x_basictp (SWS_V2XBasicTransport) — PR #269
- [x] v2x_datamgr (SWS_V2XDataManager) — PR #269
- [x] v2x_facilities (SWS_V2XFacilities) — PR #269
- [x] v2x_geonet (SWS_V2XGeoNetworking) — PR #269
- [x] v2x_mgmt (SWS_V2XManagement) — PR #269

---

## Sync todo: Group exp — missing EXP guides (20) — source batch `Group-exp.md` (21 done)

- [x] exp vfb (AUTOSAR_CP_EXP_VFB) — commits d6cf2ec · PR #158
- [x] exp layered_software_architecture (AUTOSAR_CP_EXP_LayeredSoftwareArchitecture) — commits f60d11a · PR #157
- [x] exp vfb (AUTOSAR_EXP_VFB) — PR #158
- [x] exp bsw_distribution_guide (AUTOSAR_CP_EXP_BSWDistributionGuide) — commits 668adfc · PR #159
- [x] exp application_level_error_handling (AUTOSAR_CP_EXP_ApplicationLevelErrorHandling) — commits 52d4d5c · PR #160
- [x] exp error_description (AUTOSAR_CP_EXP_ErrorDescription) — commits 9088a60 · PR #161
- [x] exp cdd_design_and_integration (AUTOSAR_CP_EXP_CDDDesignAndIntegrationGuideline) — commits 4e5d294 · PR #162
- [x] exp utilization_of_crypto_services (AUTOSAR_CP_EXP_UtilizationOfCryptoServices) — commits bcbaf51 · PR #163
- [x] exp macro_encapsulation_of_interpolation_calls (AUTOSAR_CP_EXP_MacroEncapsulationofInterpolationCalls) — commits f385e42 · PR #164
- [x] exp firmware_over_the_air (AUTOSAR_CP_EXP_FirmwareOverTheAir) — commits 30ee49d · PR #165
- [x] exp adas_vmc (AUTOSAR_CP_EXP_AIADASAndVMC) — commits a8f5273 · PR #166
- [x] exp body_and_comfort (AUTOSAR_CP_EXP_AIBodyAndComfort) — commits 9055f25 · PR #167
- [x] exp chassis (AUTOSAR_EXP_Chassis) — commits b1f1d8a · PR #179
- [x] exp hmi (AUTOSAR_EXP_HMI) — commits 29ee0f3 · PR #179
- [x] exp occupant_safety (AUTOSAR_EXP_OccupantSafety) — commits ed312b3 · PR #179
- [x] exp powertrain (AUTOSAR_EXP_Powertrain) — commits 7909111 · PR #179
- [x] exp user_guide (AUTOSAR_EXP_UserGuide) — commits 2453865 · PR #179
- [x] exp arti (AUTOSAR_EXP_ARTI) — commits 89cd317 · PR #179
- [x] exp functional_safety_measures (AUTOSAR_EXP_FunctionalSafetyMeasures) — commits c1ed1da · PR #179
- [x] exp safety_use_case (AUTOSAR_EXP_SafetyUseCase) — commits 5fa1e61 · PR #179
- [x] exp sw_cluster_design_and_integration (AUTOSAR_EXP_SwClusterDesignAndIntegration) — commits 26625e4 · PR #179

## Not queued (deliberately skipped)
- 📄 methodology_templates/ — moved 2026-11-06 to [Group-cp-methodology.md](Group-cp-methodology.md) (user request): all 17 MethodologyAndTemplates documents now queued there; TPS_BSWModuleDescriptionTemplate stays an existing-article alignment row (the old note here carried a name typo: "basic_software_mode_manager")
- 📖 template/ — template example pages removed 2026-11-04 (landing only)
- 📖 power/ — bespoke topic article (no standalone specification)

---

## Sync todo: Group foundation exp — Foundation R23-11 guide/template/report documents (20) — source batch `Group-foundation-exp.md` (19 done, 1 open row(s) → Group-unfinished.md)

- [x] tr_glossary (AUTOSAR_FO_TR_Glossary) — commits 2304e43 · PR #112
- [x] tr_list_of_known_issues_secure_hardware_extensions (AUTOSAR_FO_TR_ListOfKnownIssuesSecureHardwareExtensions) — commits 4f4954e
- [x] exp_system_health_monitoring (AUTOSAR_FO_EXP_SystemHealthMonitoring) — commits 4320445 · PR #256
- [x] tr_predefined_names (AUTOSAR_FO_TR_PredefinedNames) — commits 912e70e
- [x] exp_time_sensitive_network_features (AUTOSAR_FO_EXP_TimeSensitiveNetworkFeatures) — commits 442b230
- [x] exp_security_overview (AUTOSAR_FO_EXP_SecurityOverview) — commits 510d645
- [x] tr_release_overview (AUTOSAR_FO_TR_ReleaseOverview) — commits 55e2c99
- [x] exp_sw_architectural_decisions (AUTOSAR_FO_EXP_SWArchitecturalDecisions) — commits f3fd5cd
- [x] tps_log_and_trace_extract (AUTOSAR_FO_TPS_LogAndTraceExtract) — commits 61cda1d
- [x] exp_safety_overview (AUTOSAR_FO_EXP_SafetyOverview) — commits 123e21b
- [x] tps_arxml_serialization_rules (AUTOSAR_FO_TPS_ARXMLSerializationRules) — commits b1ec226
- [x] asws_health_monitoring (AUTOSAR_FO_ASWS_HealthMonitoring) — commits e956feb · PR #258
- [x] tps_abstract_platform_specification (AUTOSAR_FO_TPS_AbstractPlatformSpecification) — commits 510c6d7 · PR #260
- [x] tps_xml_schema_production_rules (AUTOSAR_FO_TPS_XMLSchemaProductionRules) — commits 07a9324
- [x] tr_secure_hardware_extensions (AUTOSAR_FO_TR_SecureHardwareExtensions) — commits 7b7ea04
- [x] tps_security_extract_template (AUTOSAR_FO_TPS_SecurityExtractTemplate) — commits 2329c2d
- [x] tps_feature_model_exchange_format (AUTOSAR_FO_TPS_FeatureModelExchangeFormat) — commits 2c5f4f1
- [x] tr_timing_analysis (AUTOSAR_FO_TR_TimingAnalysis) — commits 66da8d4
- [x] tps_standardization_template (AUTOSAR_FO_TPS_StandardizationTemplate) — commits ceefe4f

---

## Sync todo: Group foundation rs-prs — Foundation R23-11 requirement/protocol specifications (32) — source batch `Group-foundation-rs-prs.md` (32 done)

- [x] rs_project_objectives (AUTOSAR_FO_RS_ProjectObjectives)
- [x] rs_ieee1722 (AUTOSAR_FO_RS_IEEE1722)
- [x] rs_debug_trace_profile (AUTOSAR_FO_RS_DebugTraceProfile)
- [x] rs_someip_service_discovery_protocol (AUTOSAR_FO_RS_SOMEIPServiceDiscoveryProtocol)
- [x] prs_v2x_remote_access_layer (AUTOSAR_FO_PRS_V2XRemoteAccessLayer)
- [x] rs_ipsec_protocol (AUTOSAR_FO_RS_IPsecProtocol)
- [x] rs_security_extract_template (AUTOSAR_FO_RS_SecurityExtractTemplate)
- [x] rs_feature_model_exchange_format (AUTOSAR_FO_RS_FeatureModelExchangeFormat)
- [x] prs_secoc_protocol (AUTOSAR_FO_PRS_SecOcProtocol)
- [x] rs_data_distribution_service (AUTOSAR_FO_RS_DataDistributionService)
- [x] prs_network_management_protocol (AUTOSAR_FO_PRS_NetworkManagementProtocol)
- [x] rs_e2e (AUTOSAR_FO_RS_E2E)
- [x] rs_intrusion_detection_system (AUTOSAR_FO_RS_IntrusionDetectionSystem) — commits 9633fc6 · PR #274/#289
- [x] rs_firewall (AUTOSAR_FO_RS_Firewall)
- [x] rs_health_monitoring (AUTOSAR_FO_RS_HealthMonitoring)
- [x] rs_someip_protocol (AUTOSAR_FO_RS_SOMEIPProtocol)
- [x] rs_macsec (AUTOSAR_FO_RS_MACsec)
- [x] rs_methodology (AUTOSAR_FO_RS_Methodology)
- [x] prs_intrusion_detection_system (AUTOSAR_FO_PRS_IntrusionDetectionSystem)
- [x] rs_timing_extensions (AUTOSAR_FO_RS_TimingExtensions)
- [x] rs_safety (AUTOSAR_FO_RS_Safety) — PR #289
- [x] rs_network_management (AUTOSAR_FO_RS_NetworkManagement) — PR #289
- [x] rs_main (AUTOSAR_FO_RS_Main) — PR #289
- [x] rs_log_and_trace (AUTOSAR_FO_RS_LogAndTrace) — PR #289
- [x] rs_time_sync (AUTOSAR_FO_RS_TimeSync) — PR #289
- [x] rs_standardization_template (AUTOSAR_FO_RS_StandardizationTemplate) — PR #289
- [x] prs_time_sync_protocol (AUTOSAR_FO_PRS_TimeSyncProtocol) — PR #289
- [x] prs_someip_protocol (AUTOSAR_FO_PRS_SOMEIPProtocol) — PR #289
- [x] rs_diagnostics (AUTOSAR_FO_RS_Diagnostics) — PR #289
- [x] prs_someip_service_discovery_protocol (AUTOSAR_FO_PRS_SOMEIPServiceDiscoveryProtocol) — PR #289
- [x] prs_log_and_trace_protocol (AUTOSAR_FO_PRS_LogAndTraceProtocol) — commits 0ee8268 · PR #328
- [x] prs_e2e_protocol (AUTOSAR_FO_PRS_E2EProtocol) — commits 2d7fe61 · PR #328


## Sync todo: Group cp-methodology — CP R23-11 methodology and template documents (17) — source batch `Group-cp-methodology.md` (10 done, 7 open row(s) → Group-unfinished.md)

> Part 1 (rows 1–10) tracked by issue #365, delivered as PR #366 (commits 79587d7…d1f2094, merged 2026-11-11). Full per-row Notes live in the git history of the deleted `Group-cp-methodology.md`.

- [x] rs_ecu_resource_template (AUTOSAR_CP_RS_ECUResourceTemplate) — done 2026-11-10 · commit 79587d7 · PR #366
- [x] rs_ecu_configuration (AUTOSAR_CP_RS_ECUConfiguration) — done 2026-11-10 · commit 5d8eb30 · PR #366
- [x] rs_bsw_module_description_template (AUTOSAR_CP_RS_BSWModuleDescriptionTemplate) — done 2026-11-10 · commit fc72209 · PR #366
- [x] rs_system_template (AUTOSAR_CP_RS_SystemTemplate) — done 2026-11-10 · commit 2ab7249 · PR #366
- [x] tps_ecu_resource_template (AUTOSAR_CP_TPS_ECUResourceTemplate) — done 2026-11-10 · commit ffe57b8 · PR #366
- [x] rs_diagnostic_extract_template (AUTOSAR_CP_RS_DiagnosticExtractTemplate) — done 2026-11-10 · commit da4d88e · PR #366
- [x] rs_software_component_template (AUTOSAR_CP_RS_SoftwareComponentTemplate) — done 2026-11-10 · commit 0afb28d · PR #366
- [x] tr_franca_integration (AUTOSAR_CP_TR_FrancaIntegration) — done 2026-11-10 · commit 8498905 · PR #366
- [x] tr_general_blueprints_supplement (AUTOSAR_CP_TR_GeneralBlueprintsSupplement) — done 2026-11-11 · commit b3f31e4 · PR #366
- [x] tr_modeling_show_cases (AUTOSAR_CP_TR_ModelingShowCases) — done 2026-11-11 · commit d1f2094 · PR #366
