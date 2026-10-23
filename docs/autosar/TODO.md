# AUTOSAR 文章翻译进度

> 由 autosar-sync 技能按 [STANDARD.md](STANDARD.md) 维护；每次同步后更新对应条目与「最后更新」。
> 状态：✅ 符合 Type A · 🔶 已翻译待对齐 · ⚠️ 部分翻译 · ⛔ 空壳 · ❌ 缺失 · 📖 指南/专题（豁免骨架）
> 基准：R23-11（`~/Workspace/autosar_standard/markdown/`）· 最后更新：2026-10-24

## 待办清单

**补深（现有文章）**

- [ ] 6 篇 ⚠️ 只缺「API 规范」一章：pdu_router、can_interface、crypto_driver、ethernet_interface、lin_interface、operating_system
- [ ] 其余 11 篇 ⚠️ 补齐各自缺失章节（com_based_transformer、data_distribution、e2e_transformer、sec_oc、SoAd、mirror、dem、iohwab、fee、memory_access、dcm）
- [ ] 4 篇 ⛔ 空壳全量翻译：ethernet_switch_driver、service_discovery、memory_mapping、platform_types（platform_types 需同修 front-matter 标题与 nav 标签）
- [ ] 12 篇 🔶 对齐 Type A：icu/iohwab 删「时序图」章；flash_driver/time_service 删「配置规范」章；nvram 删「需求追踪」章并改「功能说明」；can_driver 专题章去留决策；其余旧译名统一为 STANDARD.md 用词
- [ ] IO 分区 ✅ 文章标题用词对齐（DIO 已于 2026-10-24 完成，同类偏差仍在）：port/pwm 4.2「对汽车域的适用性」、adc/icu 4.2「适用车型域」→「汽车域的适用性」；ocu 3.1「输入文档与相关标准和规范」→「输入文件」
- [ ] 4.2「适用于汽车领域」→「汽车域的适用性」（STANDARD.md 2026-10-24 定名）：bswm、ecu_state_manager、crypto_driver、crypto_service_manager、memory_access、data_distribution；「对汽车领域的适用性」：ethernet_driver、can_interface；「汽车领域的适用性」：nvram_manager
- [ ] *Scheduled functions* 统一为「调度函数」（STANDARD.md 2026-10-24 定名）：bswm 7.3 / can_network_management 7.3「周期函数」、crypto_service_manager 7.12「Scheduled 函数」
- [ ] 缩略语章统一为「粗体术语 + 引用块」+ 行集对齐（STANDARD.md §1，2026-10-24 普查 20:6）：格式 — dio/port/pwm/ocu/lin_driver/udp_network_management 6 篇现为 GFM 表格；行集（对照 R23-11 源逐行核对）— adc 补回 API/HW/SW、恢复 DEM→DET 源序、Conversion Mode 合回一条（18 行→16 条），ocu 补 MCU 行（14→13），lin_driver 缺 14 行（40→26），udp_network_management 缺 14 行（26→12）；icu 已核对一致（12:12）
- [ ] 卫生修复：udp_network_management 微信页脚改 `<h4>`；dem 编号断档；`data_distribution service` 目录改名去空格；SoAd/mirror 改 index.md 布局；`timimg_extension/indx.md` 拼写（需同改 nav）

**补广（新文章）**

- [ ] 通信主干：Com、CanSM、CanTp、TcpIp、Nm、EthSM、IpduM、SomeIpXf/SomeIpTp
- [ ] 系统服务：ComM、Det（篇幅小，先做 Det）
- [ ] 全局时间簇：StbM + CanTSyn/EthTSyn/FrTSyn
- [ ] MCAL：Mcu、Gpt、CorTst
- [ ] 存储收尾：Ea、Eep
- [ ] 库：Crc、E2E
- [ ] 安全：WdgM、WdgIf、Wdg
- [ ] 落地页补全：crypto、memory、system_services、general、methodology_templates

## 概览

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| ✅ 符合 Type A | 8 | 拿来即用 |
| 🔶 已翻译待对齐 | 12 | 七章齐全，旧译名 / 禁止章残留 |
| ⚠️ 部分翻译 | 17 | 缺 ≥1 章（多数缺 API 规范） |
| ⛔ 空壳 | 4 | 仅 9–19 行 |
| ❌ 缺失（SWS） | 86 | R23-11 共 127 篇 SWS，覆盖 41（32.3%） |
| ❌ 缺失（EXP） | 20 | R23-11 共 22 篇 EXP，覆盖 2 |
| 📖 指南/专题 | 8 | 豁免 Type A 骨架 |

## communication

- ✅ [CAN 网络管理](can_network_management/) — SWS_CANNetworkManagement（待对齐用词：7.3「周期函数」→「调度函数」）
- ✅ [UDP 网络管理](udp_network_management/) — SWS_UDPNetworkManagement → 待修：微信页脚误用 `##` 标题
- 🔶 [CAN 驱动](can_driver/) — SWS_CANDriver（专题章"术语/优先级反转/CAN 硬件单元"+旧译名）
- 🔶 [CAN 收发器驱动](can_transceiver_driver/) — SWS_CANTransceiverDriver（第 1 章"介绍"）
- 🔶 [以太网驱动](ethernet_driver/) — SWS_EthernetDriver（旧译名）
- 🔶 [LIN 驱动](lin_driver/) — SWS_LINDriver（旧译名）
- ⚠️ [CAN 接口](can_interface/) — SWS_CANInterface（缺 API 规范）
- ⚠️ [COM 基转换器](com_based_transformer/) — SWS_COMBasedTransformer（缺缩略语/依赖）
- ⚠️ [数据分发服务](data_distribution%20service/) — SWS_DataDistributionService（缺 API 规范；目录名含空格待改名）
- ⚠️ [E2E 转换器](e2e_transformer/) — SWS_E2ETransformer（缺缩略语/约束/API）
- ⚠️ [以太网接口](ethernet_interface/) — SWS_EthernetInterface（缺 API 规范）
- ⚠️ [LIN 接口](lin_interface/) — SWS_LINInterface（缺 API 规范）
- ⚠️ [PDU 路由器](pdu_router/) — SWS_PDURouter（缺 API 规范）
- ⚠️ [SecOC](sec_oc/) — SWS_SecureOnboardCommunication（缺相关文档/API）
- ⚠️ [SoAd](SoAd/SoAd.md) — SWS_SocketAdaptor（缺缩略语；目录大写、文件名非 index.md）
- ⚠️ [Bus Mirror](mirror/mirror.md) — SWS_BusMirroring（缺缩略语/API；文件名非 index.md）
- ⛔ [以太网交换机驱动](ethernet_switch_driver/) — SWS_EthernetSwitchDriver（空壳）
- ⛔ [服务发现](service_discovery/) — SWS_ServiceDiscovery（空壳）
- 📖 [FvM 专题](fvm/fvm.md) — SecOC 附录 A 派生专题（无独立规范）
- 📖 [Full-CAN vs Basic-CAN](can_driver/full_can_vs_basic_can.md) — 专题子页
- 📖 [CanNm R21-11 历史版](can_network_management/r21_11/index_r21_11.md) — 历史快照

❌ 缺失（47）：SWS_COM（Com）、SWS_CANStateManager（CanSM）、SWS_CANTransportLayer（CanTp）、SWS_CANXLDriver、SWS_CANXLTransceiverDriver、SWS_TcpIp（TcpIp）、SWS_SOMEIPTransformer（SomeIpXf）、SWS_SOMEIPTransportProtocol（SomeIpTp）、SWS_IPDUMultiplexer（IpduM）、SWS_LargeDataCOM（LdCom）、SWS_LSduRouter（LsDu）、SWS_DiagnosticLogAndTrace（Dlt）、SWS_DiagnosticOverIP（DoIp）、SWS_XCP（XCP）、SWS_SPIHandlerDriver（Spi）、SWS_EthernetStateManager（EthSM）、SWS_EthernetTransceiverDriver（EthTrcv）、SWS_WirelessEthernetDriver、SWS_WirelessEthernetTransceiverDriver、SWS_NetworkManagementInterface（Nm）、SWS_FlexRayDriver、SWS_FlexRayInterface、SWS_FlexRayNetworkManagement、SWS_FlexRayStateManager、SWS_FlexRayTransceiverDriver、SWS_FlexRayARTransportLayer、SWS_FlexRayISOTransportLayer、SWS_LINStateManager（LinSM）、SWS_LINTransceiverDriver（LinTrcv）、SWS_TTCANDriver、SWS_TTCANInterface、SWS_SAEJ1939NetworkManagement（J1939Nm）、SWS_SAEJ1939RequestManager（J1939Rm）、SWS_SAEJ1939TransportLayer（J1939Tp）、SWS_IEEE1722TransportLayer、SWS_MACsecKeyAgreement、SWS_CellularV2XDriver、SWS_ChargingManager、SWS_ChineseV2XManagement、SWS_ChineseV2XMessage、SWS_ChineseV2XNetwork、SWS_ChineseV2XSecurity、SWS_V2XBasicTransport、SWS_V2XDataManager、SWS_V2XFacilities、SWS_V2XGeoNetworking、SWS_V2XManagement

## crypto

- ✅ [Csm 加密服务管理器](crypto_service_manager/) — SWS_CryptoServiceManager（待对齐用词：4.2「适用于汽车领域」、7.12「Scheduled 函数」→「调度函数」）
- ⚠️ [Crypto 驱动](crypto_driver/) — SWS_CryptoDriver（缺 API 规范）

❌ 缺失（2）：SWS_CryptoInterface（CryIf）、SWS_KeyManager（KeyM）

## diagnostics

- ⚠️ [Dcm 诊断通信管理器](diagnostic_communication_manager/) — SWS_DiagnosticCommunicationManager（仅简介+缩略语；源 2.4 万行）
- ⚠️ [Dem 诊断事件管理器](diagnostic_event_manager/) — SWS_DiagnosticEventManager（缺约束/依赖/API；有未编号标题断档）

❌ 缺失（1）：SWS_SAEJ1939DiagnosticCommunicationManager（J1939Dcm）

## general

- ⛔ [platform_types](../general/platform_types/) — SWS_StandardTypes（空壳；front-matter 标题误写为 ECU State Manager，nav 标签需同改）

❌ 缺失（3）：SWS_BSWGeneral、SWS_PlatformTypes（与 StandardTypes 是两份文档）、SWS_CommunicationStackTypes

## io

- ✅ [ADC 驱动](io/adc_driver/) — SWS_ADCDriver（待对齐用词：4.2「适用车型域」）
- ✅ [DIO 驱动](io/dio_driver/) — SWS_DIODriver（2026-10-24 对齐 STANDARD.md 用词：3.1 / 4.2；内容与 R23-11 源逐章一致）
- ✅ [OCU 驱动](io/ocu_driver/) — SWS_OCUDriver（待对齐用词：3.1「输入文档与相关标准和规范」）
- ✅ [Port 驱动](io/port_driver/) — SWS_PortDriver（待对齐用词：4.2「对汽车域的适用性」）
- ✅ [PWM 驱动](io/pwm_driver/) — SWS_PWMDriver（待对齐用词：4.2「对汽车域的适用性」）
- 🔶 [ICU 驱动](io/icu_driver/) — SWS_ICUDriver（含禁止章"时序图"；待对齐用词：4.2「适用车型域」）
- ⚠️ [I/O 硬件抽象](io/iohwab/) — SWS_IOHardwareAbstraction（缺约束和假设；含禁止章"时序图"）

## memory

- 🔶 [BndM](bulk_nv_data_manager/) — SWS_BulkNvDataManager（第 1 章"介绍和功能概述"）
- 🔶 [Flash 驱动](flash_driver/) — SWS_FlashDriver（含"错误处理"+禁止章"配置规范"）
- 🔶 [NvM](nvram_manager/) — SWS_NVRAMManager（含禁止章"需求追踪"；"功能说明"旧译名）
- ⚠️ [Fee](flash_eeprom_emulation/) — SWS_FlashEEPROMEmulation（缺约束/依赖）
- ⚠️ [MemIf 存储访问](memory_access/) — SWS_MemoryAccess（缺 API 规范）
- ⛔ [内存映射](memory_mapping/) — SWS_MemoryMapping（空壳）
- 📖 [NV 数据处理指南](nv_data_handling_guideline/) — EXP_NVDataHandling（豁免）

❌ 缺失（6）：SWS_EEPROMAbstraction（Ea）、SWS_EEPROMDriver（Eep）、SWS_MemoryAbstractionInterface、SWS_MemoryDriver、SWS_FlashTest（FlsTst）、SWS_RAMTest（RamTst）

## mode_management

- ✅ [BswM](basic_software_mode_manager/) — SWS_BSWModeManager（待对齐用词：4.2「适用于汽车领域」、7.3「周期函数」→「调度函数」）
- 🔶 [EcuM](ecu_state_manager/) — SWS_ECUStateManager（第 2 章"定义和缩写"；4.2「适用于汽车领域」）
- 📖 [模式管理指南](guide_to_mode_management/) — EXP_ModeManagementGuide（豁免）

## system_services

- 🔶 [FiM](function_inhibition_manager/) — SWS_FunctionInhibitionManager（"功能规范"旧译名）
- 🔶 [时间服务](time_service/) — SWS_TimeService（含禁止章"配置规范"；第 2 章旧译名）
- ⚠️ [OS](operating_system/) — SWS_OS（缺 API 规范；源 1.2 万行）

❌ 缺失（4）：SWS_COMManager（ComM）、SWS_DefaultErrorTracer（Det）、SWS_HWTestManager、SWS_SoftwareClusterConnection（SwCluC）

## methodology_templates / template

- 📄 [BSW 模块描述模板](../methodology_templates/basic_software_module_description_template/) — TPS_BSWModuleDescriptionTemplate（豁免）
- 📖 [时序扩展示例](../template/timimg_extension/indx.md)、[通用结构示例](../template/generic_structure/) — 模板示例（不同步）

## 缺失分区（整区无文章）

- **GlobalTime（4）**：SWS_SynchronizedTimeBaseManager（StbM）、SWS_TimeSyncOverCAN（CanTSyn）、SWS_TimeSyncOverEthernet（EthTSyn）、SWS_TimeSyncOverFlexRay（FrTSyn）
- **Libraries（9）**：SWS_CRCLibrary（Crc）、SWS_E2ELibrary（E2E）、SWS_BFXLibrary（Bfx）、SWS_BSWMulticoreLibrary（Bmc）、SWS_MFLLibrary（Mfl）、SWS_MFXLibrary（Mfx）、SWS_IFLLibrary（Ifl）、SWS_IFXLibrary（Ifx）、SWS_EFXLibrary（Efx）
- **MCAL（3）**：SWS_MCUDriver（Mcu）、SWS_GPTDriver（Gpt）、SWS_CoreTest
- **RTE / SWArch（2）**：SWS_RTE、SWS_ARTI
- **Safety（3）**：SWS_WatchdogManager（WdgM）、SWS_WatchdogInterface（WdgIf）、SWS_WatchdogDriver（Wdg）
- **Security（2）**：SWS_Firewall、SWS_IntrusionDetectionSystemManager（IdsM）

## 缺失 EXP 指南（20）

ApplicationInterfaces 7 篇（ADAS/VMC、BodyAndComfort、Chassis、HMI、OccupantSafety、Powertrain、UserGuide）、BSWGeneral 4 篇（ApplicationLevelErrorHandling、BSWDistributionGuide、CDDDesignAndIntegration、ErrorDescription）、Crypto 1（UtilizationOfCryptoServices）、General 2（LayeredSoftwareArchitecture、VFB）、Libraries 1（MacroEncapsulationofInterpolationCalls）、Memory 1（FirmwareOverTheAir）、SWArch 1（ARTI）、Safety 2（FunctionalSafetyMeasures、SafetyUseCase）、SystemServices 1（SwClusterDesignAndIntegration）

## 建议优先级（2026-10-23 快照）

1. **小工作量补齐**：17 篇 ⚠️ 中只缺 API 规范一章的（pdu_router、can_interface、crypto_driver、ethernet_interface、lin_interface、operating_system 等）
2. **空壳全量翻译**：4 篇 ⛔（platform_types 需同修标题与 nav 标签）
3. **通信主干**：Com、CanSM、CanTp、TcpIp、Nm、EthSM、IpduM、SomeIp 系
4. **系统服务**：ComM、Det（篇幅小）
5. **对齐清理**：12 篇 🔶 的旧译名/禁止章 + 已知卫生问题（目录空格、SoAd/mirror 文件名、indx.md 拼写、platform_types 标题）
