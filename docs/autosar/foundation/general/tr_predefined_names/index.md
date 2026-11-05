---
title: "Predefined Names in AUTOSAR（AUTOSAR 预定义名称）"
spec: AUTOSAR_FO_TR_PredefinedNames
release: R23-11
---

<!-- 源文档 AUTOSAR_FO_TR_PredefinedNames（R23-11），技术报告（TR），不受 Type A 七章骨架约束；章节结构镜像源文档自身编号（1–4 与附录 A–B）。封面表格、Disclaimer、Contents 属于文档框架信息，不译；源文档开头的 References 列表保留为文末不编号的「参考文献」注册表。源文档中的规范项 ID（[TR_PDN_xxxxx]、[TPS_STDT_xxxxx]、[TPS_GST_xxxxx]）按 2026-11-03 决议丢弃，仅保留并翻译条文内容。被 PDF 换行切断的 shortName 列的名称按源文档自己的说明拼接（保留名称不含空白）。表格列单元与行序严格对应源文档。 -->

## 1. 引言

本文档描述 AUTOSAR 模型和文档中使用的各种预定义名称。本文档的主要目的是作为一个入口，用于查找 AUTOSAR 在以下文档之外预定义的名称：

- [\[1\]](#ref-1) 基础软件模块列表
- [\[2\]](#ref-2) 应用接口
- [\[3\]](#ref-3) ECU 配置参数

请注意，本文档中的定义也以 AUTOSAR XML 模型的形式提供。在该模型中，预定义名称按照 [\[4\]](#ref-4) 表示为关键字（**Keyword**）。它们以具有以下各列的表表示：

- shortName：缩写的唯一名称，取自 Keyword 的 shortName。
- abbrName：这是按照 [\[4\]](#ref-4) 的保留名称本身。注意，为了放入表格单元格，名称可能以换行方式渲染；该列中的保留名称绝不包含空白，因此应忽略换行。
- longName：这是该保留名称的 longName（关于 longName 的细节见 [\[5\]](#ref-5)）。
- Classification、Description：这是关键字分类（**keyword classification**）的列表，如 [\[4\]](#ref-4)、[\[5\]](#ref-5) 中所引用的那样。除此之外，还显示关键字的 desc，以便理解保留名称的用途。

## 2. 虚拟模块（Virtual Modules）

**虚拟模块的定义**：该关键字集包含两个关键字分类：

- ModuleDesignator：abbrName 表示由 AUTOSAR 定义的有效模块命名符（见 [\[5\]](#ref-5)）。
- AUTOSAR-Document：shortName 表示用于实现 AUTOSAR 所提供规范的模块名称。

表2.1：虚拟模块（**Virtual Modules**）

| shortName | abbrName | longName | Classification, Description |
|---|---|---|---|
| AISpecification | AISpecification | XML Specification of Application Interfaces | AUTOSAR-Document、ModuleDesignator。这表示应用接口。 |
| EcuC | EcuC | Ecu Configuration | ModuleDesignator。EcuC 是一个伪模块，它定义适用于所有其他 BSW 模块的参数。 |
| GeneralBlueprints | GenBlpr | General Blueprints | ModuleDesignator。用于 AUTOSAR M1 模型的蓝图集合。 |
| GeneralDefinitions | GenDef | General Definitions | ModuleDesignator。这表示既可以应用于基础（BSW）软件也可以应用于应用（ASW）软件、但没有为其维护显式 AUTOSAR 文档的通用元素。该虚拟模块中的对象例如生命周期定义、角色定义等元素。 |
| V2X | V2X | Vehicle-2-X | ModuleDesignator。V2X 被 Vehicle-2-X 通信模块所使用的所有跨模块类型用作簇缩写。 |

## 3. AUTOSAR 信息类别（AUTOSAR Information Categories）

**AUTOSAR 信息类别的定义**：该关键字集包含以下关键字分类：

- DocumentCategory：关键字（abbrName）表示 AUTOSAR 所提供文档的有效类别（见 [\[4\]](#ref-4)）。
- TraceCategory：关键字（abbrName）表示 AUTOSAR 所提供文档中可追溯文本的有效类别（见 [\[4\]](#ref-4)）。
- InternalDocumentCategory：关键字（abbrName）表示 AUTOSAR 内部的、不对外发布但仍遵循约定的文档的有效类别。

表3.1：AUTOSAR 信息类别（**AUTOSAR Information Categories**）

| shortName | abbrName | longName | Classification, Description |
|---|---|---|---|
| ASWS | ASWS | Abstract SWS Software Specification | DocumentCategory、TraceCategory。AUTOSAR 基础软件模块的通用规范。 |
| ATR | ATR | Acceptance Test Requirement | DocumentCategory、TraceCategory。验收测试需求的规范。 |
| ATS | ATS | Acceptance Test Specification | DocumentCategory、TraceCategory。用于执行验收测试的测试规范与脚本。 |
| CONC | CONC | Concept Document | DocumentCategory、TraceCategory。描述为下一个小版本或大版本所计划变更的概念文档。 |
| CTCF | CTCF | Configuration Settings | DocumentCategory、TraceCategory。用于执行一致性测试的配置设置。 |
| CTSP | CTSP | Conformance Test Specification | DocumentCategory、TraceCategory。用于执行一致性测试的测试规范与脚本。 |
| EXP | EXP | Explanation | DocumentCategory、TraceCategory。对其他文档中已展示内容进行讨论的说明性材料。 |
| MMOD | MetaModel | MetaModel | DocumentCategory、TraceCategory。元层级 2（元模型）上的建模内容（模型或由模型生成）。 |
| MOD | MOD | Model | DocumentCategory、TraceCategory。元层级 1（模型）上的建模内容（模型或由模型生成）。 |
| PD | PD | Process Description | DocumentCategory、TraceCategory。对 AUTOSAR 标准化活动中所应用过程的描述。 |
| PDEP | PDEP | Profile of Data Exchange Point | DocumentCategory、TraceCategory。包含为特定数据交换点裁剪 AUTOSAR 规范与模板的模型。 |
| PRS | PRS | Protocol Specification | DocumentCategory、TraceCategory。AUTOSAR 标准化的协议的规范。 |
| RS | RS | Requirement Specification | DocumentCategory、TraceCategory。软件规范之外的需求的规范。 |
| SRC | SRC | Source | DocumentCategory、TraceCategory。源代码制品。 |
| SRS | SRS | Software Requirement Specification | DocumentCategory、TraceCategory。软件规范的需求的规范。 |
| SWS | SWS | Software Specification | DocumentCategory、TraceCategory。AUTOSAR 软件的规范。 |
| TMPL | TMPL | Template | InternalDocumentCategory。预定义的文档模板。 |
| TPS | TPS | Template Specification | DocumentCategory、TraceCategory。AUTOSAR 模板的规范，包含元模型信息、约束等。 |
| TR | TR | Technical Report | DocumentCategory、TraceCategory。描述任意 AUTOSAR 相关主题的一般技术报告。 |
| UC | UC | Use Case Specification | TraceCategory。用例的规范，需求由其派生。注意，有些文档在其需求规范中维护用例，因此该 documentCategory 即使不是一个独立的制品也可能存在。 |
| ZAUX | ZAUX | Auxilary material | InternalDocumentCategory。标准创建过程中在内部使用的辅助文件。可与 ZSUPP 合并。 |
| ZGEN | ZGEN | Generated intermediate material | InternalDocumentCategory。在 AUTOSAR 的 SCM 系统中维护、并在标准创建过程中内部使用的生成中间产品。 |
| ZSUPP | ZSUPP | Supplemental material | InternalDocumentCategory。标准创建过程中在内部使用的补充材料。 |

## 4. AUTOSAR 文档缩写（AUTOSAR Document Abbreviations for Trace Prefixes）

**用于追溯前缀的文档缩写的定义**：该关键字集包含以下关键字分类：

- DocumentAbbreviation：abbrName 表示追溯标签中的有效文档缩写（见 [\[5\]](#ref-5)）。

注意，存在一个文档使用多个缩写的情况（例如 [SWMC, SWNR]、[MCM, MCG, MCA]），也存在一个缩写跨多个文档使用的情况（例如 [BSW]）。

表4.1：AUTOSAR 文档缩写（**AUTOSAR Document Abbreviations for Trace Prefixes**）

| shortName | abbrName | longName | Classification, Description |
|---|---|---|---|
| ARTI | ARTI | AUTOSAR Run-Time Interface | DocumentAbbreviation。本文档解释"AUTOSAR 运行时接口"（**AUTOSAR Run-Time Interface**）的接口。 |
| AIBodyAndComfort | AIBC | Application Interfaces "Body and Comfort" | DocumentAbbreviation。本文档解释"车身与舒适"（**Body and Comfort**）的应用接口。 |
| AIChassis | AICS | Application Interfaces "Chassis" | DocumentAbbreviation。本文档解释"底盘"（**Chassis**）的应用接口。 |
| AIDesignPatternCatalogue | AIDPC | Application Interface Design Pattern Catalogue | DocumentAbbreviation。本文档包含应用接口设计模式目录。 |
| IntrusionDetectionSystemManager | AIDSM | Intrusion Detection System Manager | DocumentAbbreviation。本文档解释自适应平台的入侵检测系统管理器（**Intrusion Detection System Manager**）。 |
| AIHMIMultimediaAndTelematics | AIHMI | Application Interfaces "HMI Multimedia and Telematics" | DocumentAbbreviation。本文档解释"HMI 多媒体与远程信息处理"（**HMI Multimedia And Telematics**）的应用接口。 |
| AIOccupantAndPedestrianSafety | AIOPS | Application Interfaces "Occupant and pedestrian Safety" | DocumentAbbreviation。本文档解释"乘员与行人安全"（**Occupant and pedestrian Safety**）的应用接口。 |
| AIPowertrain | AIPT | Application Interfaces "Powertrain" | DocumentAbbreviation。本文档解释"动力总成"（**Powertrain**）的应用接口。 |
| AISpecificationExamples | AISE | XML Examples of Application Interfaces | DocumentAbbreviation。这表示应用接口的 XML 示例。 |
| AIUserGuide | AIUG | Application Interfaces User Guide | DocumentAbbreviation。本文档旨在解释 AI 表的所有相关细节。 |
| ApplicationLevelErrorHandling | ALEH | Application Level Error Handling | DocumentAbbreviation。本文档解释应用层错误处理。 |
| AdaptiveNetworkManagement | ANM | Adaptive Network Management | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| AdaptivePlatformDemonstrator | APD | Adaptive Platform Demonstrator | DocumentAbbreviation。本文档规定自适应平台演示器（**Adaptive Platform Demonstrator**）。 |
| AdaptivePlatformDemonstratorTestdata | APDT | Adaptive Platform Demonstrator Testdata | DocumentAbbreviation。本文档规定自适应平台演示器测试数据（**Adaptive Platform Demonstrator Testdata**）。 |
| AutosarModelConstraints | ArModC | Autosar Model Constraints | DocumentAbbreviation。本文档解释 Autosar 模型约束。 |
| ARXMLSerializationRules | ASR | ARXML Serialization Rules | DocumentAbbreviation。本文档解释如何将 AUTOSAR 模型序列化为 ARXML 文件，以及反向操作。 |
| ATBM | ATBM | Interaction with Behavioral Models | DocumentAbbreviation。本文档描述与行为模型的交互。 |
| BSWAndRTEFeatures | BRF | AUTOSAR BSW and RTE Features | DocumentAbbreviation。本文档规定 BSW 架构与 RTE 的特性。 |
| BSW | BSW | Basic Software | DocumentAbbreviation。该缩写表示所有 BSW 软件需求规范的超集。也就是说，该缩写用于所有基础软件规范。 |
| BSWModuleDescriptionTemplate | BSWMDT | Basic Software Module Description Template | DocumentAbbreviation。本文档规定如何描述基础软件。 |
| BSWModuleList | BSWML | Basic Software Module List | DocumentAbbreviation。本文档列出 BSW 模块。 |
| BSWUMLModelModelingGuide | BSWUMG | BSW UML Model Modeling Guide | DocumentAbbreviation。本指南描述 BSW UML 模型的建模。 |
| BSWUML | BSWUML | Basic Software UML model | DocumentAbbreviation。该缩写表示 BSW UML 模型。也就是说，该缩写用于 BSW UML 模型中维护的所有元素。 |
| BWCStatement | BWC | BWC Statement | DocumentAbbreviation。本文档描述向后兼容性声明。 |
| CDDDesignAndIntegrationGuideline | CDDG | CDD Design And Integration Guideline | DocumentAbbreviation。本指南描述 CDD 的设计与集成。 |
| CommunicationCan | COMCAN | Communication on Can | DocumentAbbreviation。与 CAN 上的通信相关。 |
| CommunicationFlexray | COMFR | Communication on Flexray | DocumentAbbreviation。与 FlexRay 上的通信相关。 |
| CommunicationLin | COMLIN | Communication on Lin | DocumentAbbreviation。与 LIN 上的通信相关。 |
| CommunicationManagement | COMMGMT | Communication Management | DocumentAbbreviation。与通信管理相关。 |
| CommunicationViaBus | COMVB | Communication via a bus | DocumentAbbreviation。与经由总线的通信相关。 |
| DiagnosticExtractTemplate | DEXT | Diagnostic Extract Template | DocumentAbbreviation。本文档规定诊断交换数据。 |
| Diagnostic | DIAG | Requirements on Diagnostic | DocumentAbbreviation。AUTOSAR 诊断工作组与本文档的目标是：定义诊断基础软件的元素在多大程度上必须是可配置的，以及它们应遵守哪些前提条件以满足裁剪需求。同时还应实现法定 OBD 与增强诊断的处理。 |
| AdaptiveDiagnostics | DM | Adaptive Diagnostics | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| ECUConfiguration | ECUC | Specification of ECU Configuration | DocumentAbbreviation。本文档规定 ECU 配置的技术细节。 |
| ECUConfigurationParameters | ECUCP | ECU Configuration Parameters | DocumentAbbreviation。本文档描述 ECU 配置参数。 |
| EcuModeManagement | ECUMGMT | ECU Mode Management | DocumentAbbreviation。与 ECU 模式管理相关。 |
| ECUResourceTemplate | ECUR | Specification of ECU Resource Template | DocumentAbbreviation。本文档规定如何描述 ECU 的资源。 |
| ErrorDescription | ED | Error Description | DocumentAbbreviation。本文档解释错误描述。 |
| ExecutionManagement | EM | Execution Management | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| ErrataSheet | ERSH | Errata Sheet | DocumentAbbreviation。本文档解释勘误表。 |
| FrancaIntegration | FCAINT | Franca Integration | DocumentAbbreviation。本文档描述 Franca 集成。 |
| Features | Feature | Feature Specification Acceptance Tests | DocumentAbbreviation。验收测试的特性规范。 |
| FeatureModelExchangeFormat | FMDT | Specification of Feature Model Exchange Format | DocumentAbbreviation。本文档规定如何描述特性模型交换格式。 |
| FreeRunningTimer | FRT | Free Running Timer | DocumentAbbreviation。本文档描述自由运行定时器。 |
| Glossary | GLOS | Glossary | DocumentAbbreviation。本文档列出所有术语表条目。 |
| GenericStructureTemplate | GST | Generic Structure Template | DocumentAbbreviation。本文档规定适用于所有模板的公共方面。 |
| Gateway | GTW | Gateway | DocumentAbbreviation。本文档解释网关。 |
| HealthManagement | HM | Health Management | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| InteroperabilityOfAutosarTools | IOAT | Interoperability of AUTOSAR Tools | DocumentAbbreviation。本文档描述 AUTOSAR 工具互操作性的各个方面。 |
| InteroperabilityOfAutosarToolsSupplement | IOATS | Interoperability of AUTOSAR Tools Supplement | DocumentAbbreviation。本文档包含数据交换点的基本配置文件与示例。 |
| IOHWAbstraction | IOHWAB | IO Hardware Abstraction | DocumentAbbreviation。本文档描述 I/O 硬件抽象。 |
| InterruptHandlingExplanation | IRH | Interrupt Handling Explanation | DocumentAbbreviation。本文档解释中断处理。 |
| SRSLibraries | LIBS | Requirements on Libraries | DocumentAbbreviation。本文档规定对 AUTOSAR 库的需求。 |
| AdaptiveLogAndTrace | LOG | Adaptive Log and Trace | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| LayeredSoftwareArchitecture | LSA | Layered Software Architecture | DocumentAbbreviation。本文档描述分层软件架构。 |
| MainRequirements | Main | AUTOSAR Main Requirements | DocumentAbbreviation。本文档规定 AUTOSAR 主要需求。 |
| AIMeasurementCalibrationDiagnostics | MCAI | Unique Names for Documentation, Measurement and Calibration: Modeling and Naming Aspects including Automatic Generation | DocumentAbbreviation。本文档讨论如何为测量、标定和诊断工具（MCD）自动生成显示名称。 |
| AIMeasurementCalibrationDiagnostics_Assumptions | MCA | Assumptions in Unique Names for Documentation, Measurement and Calibration: Modeling and Naming Aspects including Automatic Generation | DocumentAbbreviation。该关键字反映如何为测量、标定和诊断工具（MCD）自动生成显示名称的假设。该关键字用于文档内部追溯。 |
| AIMeasurementCalibrationDiagnostics_GenerationRules | MCG | Generation Rules in Unique Names for Documentation, Measurement and Calibration: Modeling and Naming Aspects including Automatic Generation | DocumentAbbreviation。该关键字反映如何为测量、标定和诊断工具（MCD）自动生成显示名称的生成规则。该关键字用于文档内部追溯。 |
| AIMeasurementCalibrationDiagnostics_ModelingRules | MCM | Modeling Rules in Unique Names for Documentation, Measurement and Calibration: Modeling and Naming Aspects including Automatic Generation | DocumentAbbreviation。该关键字反映如何为测量、标定和诊断工具（MCD）自动生成显示名称的建模规则。该关键字用于文档内部追溯。 |
| AIMeasurementCalibrationDiagnostics_Requirements | MCR | Requirements in Unique Names for Documentation, Measurement and Calibration: Modeling and Naming Aspects including Automatic Generation | DocumentAbbreviation。该关键字反映如何为测量、标定和诊断工具（MCD）自动生成显示名称的需求。该关键字用于文档内部追溯。 |
| MemoryServices | MEM | Requirements on Memory Services | DocumentAbbreviation。本文档规定对存储服务的基础软件模块的需求。 |
| Methodology | METH | AUTOSAR Methodology | DocumentAbbreviation。本文档描述 AUTOSAR 方法论。 |
| MethodologyModelRules | MethModR | Methodology Model Rules | DocumentAbbreviation。本文档描述方法论模型规则。 |
| MiscSupport | MICS | Miscellaneous Support | DocumentAbbreviation。本文档包含杂项支持条目。 |
| MetaModel | MM | Meta Model | DocumentAbbreviation。本文档描述元模型。 |
| MemoryHWAbstractionLayer | MMHWABLY | Memory Hardware Abstraction Layer | DocumentAbbreviation。本文档描述存储硬件抽象层。 |
| ModeManagementGuide | MMG | Mode Management Guide | DocumentAbbreviation。本指南描述模式管理。 |
| ModeMgm | ModeMgm | Mode Management | DocumentAbbreviation。本文档规定 AUTOSAR 中的模式管理。 |
| MultiCoreGuide | MTCG | Multi Core Guide | DocumentAbbreviation。本指南描述多核。 |
| MethodologyAndTemplatesGeneral | MTG | General Requirements on Methodology and Templates | DocumentAbbreviation。本文档的目的在于收集与多个文档相关的方法论与模板需求。 |
| OperatingSystemInterface | OSI | Operating System Interface | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| Pesistency | PER | Persistency | DocumentAbbreviation。Adaptive Platform——待正确填写。 |
| PredefinedNames | PDN | AUTOSAR PredefinedNames | DocumentAbbreviation。本文档描述 AUTOSAR 中使用的各种预定义名称。 |
| ProjectObjectives | PO | AUTOSAR Project Objectives | DocumentAbbreviation。本文档规定 AUTOSAR 项目目标。 |
| ReferenceBase | RefBase | Reference Base | DocumentAbbreviation。本文档包含参考基础（**Reference Base**）条目。 |
| Requirements | Requirement | Requirements Acceptance Tests | DocumentAbbreviation。验收测试的需求。 |
| ReleaseOverviewAndRevHistory | RORH | Release Overview And Rev History | DocumentAbbreviation。本文档提供发布概览与版本历史。 |
| RTE | RTE | Runtime Environment | DocumentAbbreviation。本文档规定 AUTOSAR 运行时环境。 |
| SAE | SAE | Society of Automotive Engineers | DocumentAbbreviation。本文档描述由美国汽车工程师学会开发的网络标准。 |
| SafetyExtensions | SAFEX | Specifcation of Safety Extensions | DocumentAbbreviation。本文档规定如何描述 AUTOSAR 系统的安全相关属性和需求。 |
| XMLSchemaSupplement | SchemaSupp | XML Schema Supplement | DocumentAbbreviation。本文档解释 XML 模式。 |
| SecurityExtractTemplate | SECXT | Security Extract Template | DocumentAbbreviation。本文档规定安全交换数据。 |
| SomeIpExample | SIPEX | SomeIp Example | DocumentAbbreviation。本文档包含 SOME/IP 示例。 |
| SPAL | SPAL | Standard Peripheral Abstraction Layer | DocumentAbbreviation。本文档描述标准外设抽象层。 |
| SafetyUseCase | SUC | Safety Use Case | DocumentAbbreviation。本文档解释安全用例。 |
| SWCModeling | SWCM | Software Component Modeling | DocumentAbbreviation。本文档描述软件组件的建模。 |
| SoftwareComponentTemplate | SWCT | Software Component Template | DocumentAbbreviation。本文档规定如何描述软件组件。 |
| SWCModelingGuide | SWMG | SW-C and System Modeling Guide | DocumentAbbreviation。本文档给出关于使用 AUTOSAR 模型元素以构建 AUTOSAR 系统的指南和约定。 |
| SWCModelingGuide_NamingRules | SWNR | Naming Rules in SW-C and System Modeling Guide | DocumentAbbreviation。本文档给出关于使用 AUTOSAR 模型元素以构建 AUTOSAR 系统的指南和约定，特别是其中的命名规则。 |
| StandardizationTemplate | STDT | Standardization Template | DocumentAbbreviation。本文档规定 AUTOSAR 标准化如何表示为 ARXML 文件。 |
| SystemTemplate | SYST | System Template | DocumentAbbreviation。本文档规定如何描述 AUTOSAR 系统。 |
| TimingAnalysis | TIMAY | Specification of Timing Analysis | DocumentAbbreviation。本文档解释时序分析。 |
| TimingExtensions | TIMEX | Specification of Timing Extensions | DocumentAbbreviation。本文档规定如何描述 AUTOSAR 系统的时序。 |
| TTCAN | TTCAN | Requirements on TTCAN | DocumentAbbreviation。本文档规定 CAN BSW 协议栈的附加 TTCAN 需求。 |
| UtilizationOfCryptoServices | UOC | Utilization Of Crypto Services | DocumentAbbreviation。本文档解释加密服务的使用。 |
| VirtualFunctionalBus | VFB | Virtual Functional Bus | DocumentAbbreviation。本文档描述虚拟功能总线。 |
| XMLSchema | XMLSchema | XML Schema | DocumentAbbreviation。本文档描述 XML 模式。 |
| XMLSchemaProductionRules | XMLSPR | XML Schema Production Rules | DocumentAbbreviation。本文档描述如何从 AUTOSAR 元模型编译出符合 W3C XML schema 规范的 XML 模式。 |

## A. 所提及的类表

为完整起见，本章包含一组类表，它们表示本文档语境中所提及、但不直接包含在描述特定元模型语义范围之内的元类。

**表A.1：Identifiable（Identifiable）**

| 属性 | 值 |
|---|---|
| Class | Identifiable（抽象） |
| Package | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable |
| Note | 本类的实例可以通过其标识符（在命名空间边界内）被引用。除此之外，Identifiable 是对 AUTOSAR 描述的整体结构有显著贡献的对象。特别地，Identifiable 可以包含 Identifiable。 |
| Base | ARObject、MultilanguageReferrable、Referrable |
| Subclasses | ARPackage, AbstractSecurityEventFilter, AbstractSecurityIdsmInstanceFilter, AbstractServiceInstance, ApplicationEndpoint, ApplicationError, AppliedStandard, ArtifactChecksum, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpFeature, AutosarOperationArgumentInstance, AutosarVariableInstance, BlockState, BuildActionEntity, BuildActionEnvironment, Chapter, ClassContentConditional, ClientIdDefinition, ClientServerOperation, Code, CollectableElement, ComManagementMapping, CommConnectorPort, CommunicationConnector, CommunicationController, Compiler, ConsistencyNeeds, ConsumedEventGroup, CouplingPort, CouplingPortStructuralElement, CryptoKeySlot, CryptoServiceMapping, DataPrototypeGroup, DataTransformation, DdsCpDomain, DdsCpPartition, DdsCpQosProfile, DdsCpTopic, DependencyOnArtifact, DiagEventDebounceAlgorithm, DiagnosticAuthTransmitCertificateEvaluation, DiagnosticConnectedIndicator, DiagnosticDataElement, DiagnosticDebounceAlgorithmProps, DiagnosticFunctionInhibitSource, DiagnosticParameterElement, DiagnosticRoutineSubfunction, DltApplication, DltArgument, DltMessage, DoIpInterface, DoIpLogicAddress, DoIpRoutingActivation, EndToEndProtection, EthernetWakeupSleepOnDatalineConfig, EventHandler, ExclusiveArea, ExecutableEntity, ExecutionTime, FMAttributeDef, FMFeatureMapAssertion, FMFeatureMapCondition, FMFeatureMapElement, FMFeatureRelation, FMFeatureRestriction, FMFeatureSelection, FlexrayArTpNode, FlexrayTpPduPool, FrameTriggering, GeneralParameter, GlobalTimeGateway, GlobalTimeMaster, GlobalTimeSlave, HeapUsage, HwAttributeDef, HwAttributeLiteralDef, HwPin, HwPinGroup, IEEE1722TpAcfBus, IEEE1722TpAcfBusPart, IPSecRule, IPv6ExtHeaderFilterList, ISignalToIPduMapping, ISignalTriggering, IdentCaption, ImpositionTime, InternalTriggeringPoint, Keyword, LifeCycleState, Linker, MacMulticastGroup, MacSecKayParticipant, McDataInstance, MemorySection, ModeDeclaration, ModeDeclarationMapping, ModeSwitchPoint, NetworkEndpoint, NmCluster, NmNode, PackageableElement, ParameterAccess, PduActivationRoutingGroup, PduToFrameMapping, PduTriggering, PerInstanceMemory, PhysicalChannel, PortGroup, PortInterfaceMapping, PossibleErrorReaction, ResourceConsumption, RootSwCompositionPrototype, RptComponent, RptContainer, RptExecutableEntity, RptExecutableEntityEvent, RptExecutionContext, RptProfile, RptServicePoint, RunnableEntityGroup, SdgAttribute, SdgClass, SecureCommunicationAuthenticationProps, SecureCommunicationFreshnessProps, SecurityEventContextProps, ServiceNeeds, SignalServiceTranslationEventProps, SignalServiceTranslationProps, SocketAddress, SomeipTpChannel, SpecElementReference, StackUsage, StaticSocketConnection, StructuredReq, SwGenericAxisParamType, SwServiceArg, SwcServiceDependency, SystemMapping, TimeBaseResource, TimingClock, TimingClockSyncAccuracy, TimingCondition, TimingConstraint, TimingDescription, TimingExtensionResource, TimingModeInstance, Topic1, TpAddress, TraceableTable, TraceableText, TracedFailure, TransformationProps, TransformationTechnology, Trigger, VariableAccess, VariationPointProxy, ViewMap, VlanConfig, WaitPoint |

| 属性 | 类型 | 多重性 | 种类 | 备注 |
|---|---|---|---|---|
| adminData | AdminData | 0..1 | aggr | 这表示可标识对象的管理数据。构造型：atpSplitable；标签：atp.Splitkey=adminData、xml.sequenceOffset=-40 |
| annotation | Annotation | * | aggr | 在定义模型元素（例如 ECU 配置参数值）时提供附加注释的可能性。这些并非用作文档，而只是设计注记。标签：xml.sequenceOffset=-25 |
| category | CategoryString | 0..1 | attr | category 是一个特化 Identifiable 语义的关键字。它影响属性预期是否存在以及约束的适用性。标签：xml.sequenceOffset=-50 |
| desc | MultiLanguageOverviewParagraph | 0..1 | aggr | 这表示关于所论对象是什么的一般而简短（单段落）的描述。它只有一个段落！desc 旨在被收集到概览表中。该属性帮助人类读者识别所论对象。更详尽的文档（特别是对象如何构建或使用）应放入"introduction"。标签：xml.sequenceOffset=-60 |
| introduction | DocumentationBlock | 0..1 | aggr | 这表示关于所论对象如何构建或如何使用的更多信息，因此它是一个 DocumentationBlock。标签：xml.sequenceOffset=-30 |
| uuid | String | 0..1 | attr | 该属性的目的是为元类的实例提供全局唯一标识符。该属性的取值应是全局唯一的字符串，并以标识符类型作为前缀。例如，要包含 The Open Group 定义的 DCE UUID，UUID 将以"DCE:"开头。该属性的取值可用于支持不同 AUTOSAR 模型之间的合并。UUID（通用唯一标识符）的形式取自 The Open Group（原 Open Software Foundation）定义的标准。该标准被广泛使用，包括 Microsoft 将其用于 COM（GUID）以及许多公司将其用于基于 CORBA 的 DCE。这些 128 位 ID 的生成方法已在标准中公布，其 ID 的有效性和唯一性在实践中没有争议。如果省略 id 命名空间，则假定为 DCE。一个例子是"DCE:2fac1234-31f8-11b4-a222-08002b34c003"。uuid 属性对 AUTOSAR 模型没有语义含义，也不要求 AUTOSAR 工具管理时间戳。标签：xml.attribute=true |

**表A.2：Keyword（Keyword）**

| 属性 | 值 |
|---|---|
| Class | Keyword |
| Package | M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Keyword |
| Note | 该元类表示预定义关键字的能力，这些关键字随后可用于按照给定命名约定（例如 AUTOSAR 命名约定）构造名称。注意，这样的名称不仅是 shortName，也可以是 symbol 甚至 longName。关键字的应用不限于特定名称。 |
| Base | ARObject、Identifiable、MultilanguageReferrable、Referrable |
| Aggregated by | KeywordSet.keyword |

| 属性 | 类型 | 多重性 | 种类 | 备注 |
|---|---|---|---|---|
| abbrName | NameToken | 1 | attr | 该属性规定关键字的缩写名。例如，该缩写可用于按照 AUTOSAR 命名约定构造有效的 shortName。与 shortName 不同，它可以包含任意名称记号，例如可以只由数字组成。 |
| classification | NameToken | * | attr | 该属性允许为关键字附加分类，例如 MEAN、ACTION、CONDITION、INDEX、PREPOSITION。 |

**表A.3：MultilanguageReferrable（MultilanguageReferrable）**

| 属性 | 值 |
|---|---|
| Class | MultilanguageReferrable（抽象） |
| Package | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable |
| Note | 本类的实例可以通过其标识符（在命名空间边界内）被引用。它们也可以具有 longName，但不被认为对 AUTOSAR 描述的整体结构有实质贡献。特别地，它不包含其他 Referrable。 |
| Base | ARObject、Referrable |
| Subclasses | Caption, DefItem, DocumentationContext, Identifiable, SdgCaption, TraceReferrable, Traceable |

| 属性 | 类型 | 多重性 | 种类 | 备注 |
|---|---|---|---|---|
| longName | MultilanguageLongName | 0..1 | aggr | 这规定对象的 long name。long name 面向人类读者，作用类似于标题。 |

**表A.4：Referrable（Referrable）**

| 属性 | 值 |
|---|---|
| Class | Referrable（抽象） |
| Package | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable |
| Note | 本类的实例可以通过其标识符（在命名空间边界内）被引用。 |
| Base | ARObject |
| Subclasses | AtpDefinition, BswDistinguishedPartition, BswModuleCallPoint, BswModuleClientServerEntry, BswVariableAccess, CouplingPortTrafficClassAssignment, DiagnosticEnvModeElement, EthernetPriorityRegeneration, ExclusiveAreaNestingOrder, HwDescriptionEntity, ImplementationProps, ModeTransition, MultilanguageReferrable, PncMappingIdent, SingleLanguageReferrable, SoConIPduIdentifier, SocketConnectionBundle, TimeSyncServerConfiguration, TpConnectionIdent |

| 属性 | 类型 | 多重性 | 种类 | 备注 |
|---|---|---|---|---|
| shortName | Identifier | 1 | attr | 这规定对象的标识性 shortName。它在其上下文中必须唯一，面向人类但更面向技术引用。构造型：atpIdentityContributor；标签：xml.enforceMinMultiplicity=true、xml.sequenceOffset=-100 |
| shortNameFragment | ShortNameFragment | * | aggr | 这规定 Referrable.shortName 如何由若干 shortNameFragment 组成。标签：xml.sequenceOffset=-90 |

## B. AUTOSAR 可追溯项变更历史

### B.1. 按照 AUTOSAR 发布 R23-11 的本文档变更历史

#### B.1.1. R23-11 中新增的规范项

无

#### B.1.2. R23-11 中变更的规范项

无

#### B.1.3. R23-11 中删除的规范项

无

## 参考文献

<a id="ref-1"></a>[1] List of Basic Software Modules
> AUTOSAR_CP_TR_BSWModuleList

<a id="ref-2"></a>[2] XML Specification of Application Interfaces
> AUTOSAR_CP_MOD_AISpecification

<a id="ref-3"></a>[3] Specification of ECU Configuration Parameters (XML)
> AUTOSAR_CP_MOD_ECUConfigurationParameters

<a id="ref-4"></a>[4] Standardization Template
> AUTOSAR_FO_TPS_StandardizationTemplate

<a id="ref-5"></a>[5] Generic Structure Template
> AUTOSAR_FO_TPS_GenericStructureTemplate
