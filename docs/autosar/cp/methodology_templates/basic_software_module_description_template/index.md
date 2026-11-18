---
title: "AUTOSAR BSWMDT（基础软件模块描述模板）"
spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
release: R23-11
---




## 1. 一般信息

### 1.1. 文档范围

本文介绍了基本软件模块描述模板 BSWMDT (**the template for the Basic Software Module Description**) 。

**BSWMD** 是属于某个 BSW 工件，如：BSW模块（**BSW module**） 或 BSW集群（**BSW cluster**），以及该工件的实现的所有信息的正式符号。这种描述有几种可能的用例，详情请参见 3.1。

**BSWMDT** 是用于 **BSWMD** 的模板，它是 **AUTOSAR** 中必须用于此部分描述的标准化格式。该模板在 **UML** 中表示为整个 **AUTOSAR** 元模型的一部分，并且是从该元模型生成的 **XML** 模式的一部分。本文档描述了属于该模板的所有元素。

这些元素在 **AUTOSAR** 元模型的两个不同包中维护：

* **BswModuleTemplate** 包中包含了 **BSWMDT** 专用的所有元素。
* **BSWMDT** 的一些元素，例如：用于描述实现方面和资源消耗的元素，也在软件组件模板 (**SWCT**) 中使用。这些元素属于元模型的 **CommonStructure** 包，也在本文中进行了描述。

为了清楚起见，请注意元模型的 **GenericStructure** 包中包含了一些基本的基础设施的元类和文档[1]中描述的通用模式。这些元素也在 **BswModuleTemplate** 中使用，但有关详细信息，请参阅[1]。

通用结构（**Generic Structure**）提供有关的详细信息：

* AUTOSAR顶层结构
* 常用的元类和原语
* 变体处理
* 文档

本文档适用于需要更深入了解元模型的 **BSWMDT** 部分的人员，例如：工具开发人员和维护元模型的人员。它不打算作为必须提供实际 **BSWMD** 的 **BSW** 开发人员的指南，即：必须填写（fill out）模板的人员。有关本文档总体目标的更多信息，请参阅相关要求文档，参见[2]。

由于元模型的复杂性，本文档中某些类图中的文本太小，无法在正常尺寸的打印纸上阅读。如果需要，建议使用电子文档并在计算机屏幕上放大这些图表。

### 1.2. 输入文件

以下输入文档已用于开发 BSWMDT：

* Generic Structure Template [1]
* Requirements on BSW Module Description Template [2]
* General Requirements on Basic Software Modules [3]
* AUTOSAR Methodology [4]
* AUTOSAR Glossary [5]
* Software Component Template [6]
* System Template [7]
* XML Schema Production Rules [8]

### 1.3. 约束的施加时间

在本文档的上下文中，只有一个强制时间适用：“在 **BSW** 模块配置完成时”。

### 1.4. 缩略语（Abbreviations）

The following table contains a list of abbreviations used in the scope of this document along with the spelled-out meaning of each of the abbreviations.

**BSW** 
> Basic Software

**BSWMD** 
> Basic Software Module Description

**BSWMDT** 
> Basic Software Module Description Template

**DEM** 
> Diagnostic Event Manager

**ECU** 
> Electronic Control Unit

**ECUC** 
> ECU Configuration

**ICC1, ICC2, ICC3** 
> AUTOSAR Implementation Conformance Class 1...3

**ISR** 
> Interrupt Service Routine

**ICS** 
> Implementation Conformance Statement

**IOC** 
> Inter OS-Application Communication

**MC** 
> Measurement and Calibration

**MSR** 
> Manufacturer Supplier Relationship

**NvM** 
> Non Volatile Memory

**NVRAM** 
> Non Volatile RAM

**OS** 
> Operating System

**RAM** 
> Random Access Memory

**ROM** 
> Read-only Memory

**SWC** 
> Software Component

**SWS** 
> Software Specification

**SWCT** 
> Software Component Template

**UML** 
> Unified Modeling Language

**ARXML** 
> AUTOSAR XML

**XML** 
> Extensible Markup Language

## 2. 用例和建模方法

### 2.1. 用例

**BSWMDT** 有几种可能的用例。以下用例可应用于 **BSW** 模块（ICC3 一致性等级）或 **BSW** 集群（ICC2 一致性等级）和库。为了方便起见，我们经常在本文档中使用模块（**module**）一词作为所有三种工件的同义词。

库（**Library**）可以看作是一种特殊的模块，它提供在基础或应用软件中使用的服务，并通过直接函数调用访问，所以以下用例也可以应用于库。库和普通的 BSW 模块之间的主要区别在于，库服务可以直接从应用程序 **SWC** 调用，而无需通过 **RTE**。所以可用于库的模型元素将受到某些限制，例如：库不应该有预定的（scheduled）功能。 但是，这些限制目前尚未正式确定。

* **BSWMDT** 可用于在实际实现之前根据接口和依赖项，指定 **BSW** 模块或集群（即：一组**BSW** 模块）。在此用例中，内部行为和实现的详细信息未被填写。由于 **BSWMDT** 包含变体点（**variation points**），BSW 模块或集群的多个变体可以由单个规范描述）。根据方法论[4]，作为设计基础软件（**Design Basic Software**）活动的结果，此级别的工件作为 **BSW** 设计包（**BSW Design Bundle**）交付。
* **BSWMDT** 可用作一致性测试的输入，测试产品（模块、集群或库）与 **AUTOSAR** 标准的一致性。换句话说，这意味着对于一致性测试，**BSWMD** 应可用作 ICS（实施一致性声明）。根据方法论，此级别的工件作为 **BSW** 模块 **ICS** 捆绑包交付。请注意，此交付必须与以下交付（BSW 模块交付捆绑包）区分开来，因为一致性测试需要完全配置的软件。
* **BSWMDT** 可用于描述交付给 **AUTOSAR ECU** 集成商的实际实现的 **BSW** 模块或集群。它将包含内部行为、实现和约束 w.r.t. 的详细信息。规范，特别是，可能有不止一种实现（例如针对不同的处理器）具有相同的规范。根据方法论，此级别的工件是 **BSW** 模块交付包（**BSW Module Delivered Bundle**）的一部分，作为开发 BSW 模块（**Develop BSW Module**）活动的结果（相同的交付也包含代码，因为它不是在集成期间生成的）。
* **BSWMDT** 不仅用作上游（**upstream**）模板（如：作为在 ECU 配置时间之前提供的信息的格式），而且集成商可以使用 **BSWMD** 的某些部分来添加更多信息或调整当模块的交付时间时不可用的信息。在方法论中，此级别的工件是 BSW 模块集成包（**BSW Module Integration Bundle**）的一部分，它们是在 ECU 集成软件（**Integrate Software for ECU**）活动期间创建或完善的。此用例包括：例如添加有关实际资源消耗的文档，以及添加信息以响应集成在 ECU 上的软件组件和其他 BSW 模块的需求。
* 与最后一种情况类似，**BSWMDT** 允许添加从上游描述生成的数据，以支持测量和校准工具。
* 实现 **RTE** 和 **BSW** 调度程序（**BSW Scheduler**）的源代码，通常在 **ECU** 集成期间完全生成。因此记录此代码实现的 **BSWMD** 部分（例如：版本信息、内存部分、用于校准支持的数据结构）应由 **RTE** 生成器（**RTE generator**）生成或更新。

不同用例的工作流程细节不在本文档的范围内，但在这些不同步骤中提供的信息会影响 **BSWMDT** 的元模型。

**BSWMDT** 根据 **ICC1** 一致性等级描述软件的用途有限。因为在这种情况下，**ECU** 上的完整 **BSW**（包括 RTE）由一个单独的集群组成，所以 **BSW** 内的接口或依赖项无法通过这个模板来被描述，这也意味着模板的相关部分将是空的。然而即使在这种情况下，**BSWMDT** 也可用于记录实现方面（例如：所需的编译器、资源消耗或供应商特定配置参数）。

### 2.2. 三层方法

BSWMDT 的元模型由三个类似于 SWCT 的抽象层组成。这种方法允许能够更好地重用更抽象部分的描述。概览如下图 3.1 所示。

![Figure3_1](Figure3_1.png)

上层 **BswModuleDescription** 包含了所有提供和需要的接口（**provided and required interfaces**）的规范，包括对其他模块的依赖性。

中间层 **BswInternalBehavior** 包含模块内部一些基本活动的模型。该模型定义了模块对操作系统（**OS**）和 BSW 调度程序（**BSW Scheduler**）配置的要求。可能有多个基于相同的 **BswModuleDescription** 的不同的 **BswInternalBehavior** 实例，甚至在相同的 **CPU** 上。例如：多个驱动程序遵循相同的 **BswModuleDescription**。 术语行为（**behavior**）的选择类似于 **SWCT** 中的类似术语。注意这里只限于调度行为，不描述模块或集群的算法行为。

底层 **BswImplementation** 包含有关各个代码的信息。同样，同一个 **BswInternalBehavior** 可能有多个 **BswImplementation** 实例。

### 2.3. 可拆分聚合的使用（The usage of splitable aggregations）

这些层之间的引用不是普通聚合，允许 **XML** 工件中的更多灵活性。例如：如果 **BswInternalBehavior** 将聚合 **BswImplementation**，则必须为 **BswImplementation** 的每个实例复制 **BswInternalBehavior** 的具体 **XML** 工件。通过使用可拆分的聚合和引用，层可以保存在单独的文件中，并且可以在以后的项目阶段修改较低的层。这类似于在 C 源文件中包含头文件：多个实现文件可以共享同一个头文件，该头文件通常将更抽象的东西声明为函数原型等。从 **BswModuleDescription** 到 **BswInternalBehavior** 的关系是一个可拆分的聚合，而不是 **SWCT** 出于语义原因和类比的引用。

### 2.4. 同一个 BSW模块或 BSW 集群的几种实现

根据三层方法，元类 **BswModuleDescription** 和聚合的 **BswInternalBehavior** 描述了一种 **BSW** 模块或集群，可能存在不同的实现，由不同的 **BswImplementations** 表示。请注意元类 **BswModuleDescription** 的名称在这里具有误导性，因为此元类不包含模块或集群的完整描述。

如果 **BSW** 模块或集群的不同实现是为不同的 **CPU** 编译的，则相应的 **BSWMD** 可以被视为单独的工件，它们可以共享 **BswModuleDescription** 和 **BswInternalBehavior**。

如果实现是为同一个 **CPU** 编译的，即集成在同一个 **ECU** 并且在同一个地址空间上。例如：多个 **CAN** 通道的 **CAN** 驱动程序。它们的 **BSWMD** 仍然应该共享 **BswModuleDescription** 和 相等的 **BswInternalBehavior** ，但必须有一种机制来确保从 **BswModuleDescription** 和 **BswInternalBehavior** 派生的全局可见的 C 符号是唯一的。这是通过 **BSWMDT** 的实现部分中定义的中缀（**infixes**）来处理的。

### 2.5. 与 SwComponentType 的关系

一些 **BSW** 模块或集群，不仅具有与其他 **BSW** 模块或集群的接口，而且还具有通过 **RTE** 从应用程序 **SW-C** 访问的更多抽象接口。这些 **BSW** 模块或集群可以是 **AUTOSAR** 服务（**AUTOSAR Services**）、**ECU** 抽象（**ECU Abstraction**）的一部分，或者是复杂驱动程序（Complex Drivers）。

这里需要的更抽象的接口称为 **AUTOSAR** 接口（参见 [6] 和 [5]）。

这些 **AUTOSAR** 接口通过软件组件模板 (**SWCT**) 进行描述，它们由端口（**ports**）、端口接口（**port interfaces**）及其进一步详细信息组成。用于为 **BSW** 模块描述这些元素的 **SWCT** 的根类是 **ServiceSwComponentType**、**EcuAbstractionSwComponentType** 和 **ComplexDeviceDriverSwComponentType**（参见 [6]），它们都派生自 **AtomicSwComponentType**。

此外，从 **RTE** 到这些 **BSW** 模块的函数调用，需建模为同样包含在 **SWCT** 中的 **RunnableEntity-s**。 用于描述 **RunnableEntity-s**（以及其他一些东西）的 **SWCT** 的根类称为 **SwcInternalBehavior**。

### 2.6. 具有 AUTOSAR 接口的 BSW 模块

对于可以通过 **AUTOSAR** 接口访问的 **BSW** 模块或集群，除了 **BSWMD** 之外，还应该有一个定义 **AtomicSwComponentType** 和 **SwcInternalBehavior** 的 XML 工件。

生成 **RTE** 需要这些额外的描述。请注意，在 **AUTOSAR** 服务的情况下，这些附加描述的内容在不同的 **ECU** 之间可能会有所不同。例如：由于 **RTE** 必须为 **AUTOSAR** 服务创建的端口数量，所以必须为每个 **ECU** 创建。参加 [6] 中描述了创建这些工件的详细步骤。

为了跟踪这些额外的 **SWCT** 描述和关联的 **BSWMD** 之间的依赖关系，在 **SwcInternalBehavior** 类和 **BswInternalBehavior** 类之间存在映射，详情请参阅第 6.11 章。

由于使用了两种不同的模板来描述上述模块，即：那些具有用于连接到应用软件的端口的模板，所以如何描述调度（**scheduling**）存在一定的歧义：

1. 使用在 **BSWMDT** 中定义的事件模型 （请参阅本文档的BSW Beahvior）。
2. 使用在 **SWCT** 的 **SwcInternalBehavior** 中定义的事件模型。

两种不同的事件模型导致针对 **RTE** 的不同接口。BSW 调度程序（**BSW-Scheduler**）风格的 C 接口和 SWC 风格的 C 接口都在 RTE 合同阶段（**RTE contract phase**）生成。 对于到目前为止定义的标准化 **AUTOSAR** 服务，SWC 样式的接口仅用于与通过端口进行通信直接相关的函数调用。而例如BSW 调度程序（**BSW-Scheduler**）的接口需使用周期的事件。 请注意，对于未标准化的 **BSW** 部件，如：ECU 抽象和复杂驱动程序，则没有这样的规则。

另一种特殊情况，当 BSW 调度程序（**BSW Scheduler**）或中断例程（**interrupt routine**）触发周期函数时，接着必须通过调用 **RTE** 才能访问 **SWC**。为了使用当前 **SWCT** 的方式生成 **RTE API**，在这种情况下需要指定一个 **RunnableEntity**，即使它不是由RTE事件触发的。

## 3. BSW 模块描述概述

图 3.1 及下面的类表展示了 **BSWMDT** 顶层 **BswModuleDescription** 的所有关系。

对于符合 **ICC3** 一致性等级的标准化模块，**BswModuleDescription.shortName** 应选择与 [11] 中定义的模块缩写（ resp. 库缩写）相同。

此外，**BswModuleDescription** 包含一个属性 **moduleId**：

**BSW 模块标识符**：如果适用，**BswModuleDescription.moduleId** 应指向 [11] 中定义的标准化 **AUTOSAR** 模块的标识符。否则（例如对于 **ICC2** 集群），该标识符应为空，或选择不同于 [11] 中给出的标识符。

> 1 注意，在 ECU 软件中可能存在多个具有相同标识符的模块，例如根据标准，复杂驱动程序（**Complex Drivers**）全部具有相同的标识符。

**模块标识符与 category 的使用**：无论如何，BSWMD 中的该标识符用于记录某个工件与标准的关系，因此对于一致性测试是有用的信息。除此之外，通用 **category** 属性（继承自 **Identifiable**）应用于对 **BswModuleDescription** 进行一般分类，如下表所示。这样可以检查约束。

**BswModuleDescription 允许的 category**：

表 3.1：BswModuleDescription 允许的 category（**Allowed categories of BswModuleDescription**）

| category | 说明 |
| --- | --- |
| BSW_MODULE | 指定单个 BSW 模块（ICC3 粒度）。 |
| BSW_CLUSTER | 指定 BSW 模块集群（ICC2 粒度）。 |
| LIBRARY | 指定库（不限于在 BSW 内使用）。 |

请注意，**BswModuleDescription** 不允许其他值或空值。

**将 SwComponentDocumentation 附加到 BSWMD**：可以通过元类 **SwComponentDocumentation** 向 **BswModuleDescription** 附加文档。这使用与软件组件文档相同的概念，并在 [6] 中详细描述。

元类 **BswModuleEntry** 描述单个 C 函数原型（见第 4.1 章），在此使用如下：

**提供 BswModuleEntry**：由 **BswModuleDescription** 导出的接口是提供给其他模块使用的 **implementedEntry** 集合（包括由 **BSW Scheduler** 调用的 "main" 函数）。

**使用 BswModuleEntry**：由 **BswModuleDescription** 所需的接口是由其他模块实现的 **expectedEntry** 集合。

**BswModuleEntry 的链接**：由一个 **BswModuleDescription** 作为 **implementedEntry** 引用的 **BswModuleEntry**，与另一个 **BswModuleDescription** 作为 **expectedEntry** 引用的 **BswModuleEntry**，在符合下列条件之一时是匹配的：

* 引用了同一个 **BswModuleEntry**；
* 两个 **BswModuleEntry.shortName** 相同。

**链接到 BswModuleEntry 的条目应具有兼容的签名**：按照上述匹配规则匹配的 **BswModuleEntry**，在下列条件满足时是兼容的：

* 二者都定义或都不定义 **returnType**；
* 当定义了 **returnType** 时，扮演 **returnType** 角色的 **SwServiceArg** 必须兼容；
* 二者定义相同数量的兼容参数，且顺序相同。

**returnType 角色中 SwServiceArg 的兼容性**：扮演 **returnType** 角色的 **SwServiceArg** 在类型完全相同时是兼容的。

**参数角色中 SwServiceArg 的兼容性**：扮演参数角色的 **SwServiceArg** 在下列条件满足时是兼容的：

* 它们类型完全相同；
* 并且两者具有相同的 **shortName**。

**匹配的 BswModuleEntry 应具有兼容的属性**：按照上述匹配规则匹配的 **BswModuleEntry** 应使用下列属性的相同值定义：

* **callType**
* **executionContext**
* **isReentrant**
* **isSynchronous**
* **serviceId**
* **swServiceImplPolicy**
* **bswEntryKind**

**BswModuleDescription.providedModeGroup**：通过可选属性 **providedModeGroup**，BSW 模块可以提供一组模式（模式组），以控制其他 BSW 模块，而后者又必须声明相应的 **requiredModeGroup**。

**BswModuleDescription.releasedTrigger**：通过可选属性 **releasedTrigger**，BSW 模块可以声明它释放的一个触发器。**trigger** 用于在其它 BSW 模块中引发事件，而后者又必须声明相应的 **requiredTrigger**。

**BswModuleDescription.internalBehavior**：通过在 **BswModuleDescription** 中聚合 **BswInternalBehavior** 类，可以在描述中加入调度方面的内容。

函数声明、依赖、触发器和模式构成了模块或集群的接口，用于同一存储器和处理器核上的模块间通信。详情见第 4 章。

对于分区和/或核边界之间的通信，需要额外的声明，见第 4.6 章。

关于 **BswInternalBehavior**，见第 5 章。

表 3.2：BswModuleDescription（**BswModuleDescription**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswOverview |
| Note | — | — | — | 用于描述单个 BSW 模块或 BSW 集群的根元素。若描述的是 BSW 模块，则该元素的短名称等于 BSW 模块的名称。标签：atp.recommendedPackage=BswModuleDescriptions |
| Base | — | — | — | ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable |
| Aggregated by | — | — | — | ARPackage.element, AtpClassifier.atpFeature |
| bswModuleDependency | BswModuleDependency | * | aggr | 描述对另一个 BSW 模块的依赖。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=bswModuleDependency.shortName, bswModuleDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20 |
| bswModuleDocumentation | SwComponentDocumentation | 0..1 | aggr | 为 BSW 模块添加文档。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=bswModuleDocumentation, bswModuleDocumentation.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=6 |
| expectedEntry | BswModuleEntry | * | ref | 指示本模块所需的 entry。替代 outgoingCallback / requiredEntry。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=expectedEntry.bswModuleEntry, expectedEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| implementedEntry | BswModuleEntry | * | ref | 指定本模块提供、可被其他模块调用的 entry。这包括 "main" 函数、中断例程和回调。替代 providedEntry / expectedCallback。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=implementedEntry.bswModuleEntry, implementedEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| internalBehavior | BswInternalBehavior | * | aggr | 与一个 BswModuleDescription 关联的各个 BswInternalBehavior 可以分布在多个物理文件中，因此该聚合为 <<atpSplitable>>。构造型：atpSplitable 标签：atp.Splitkey=internalBehavior.shortName |
| moduleId | PositiveInteger | 0..1 | attr | 指向 AUTOSAR 标准定义的 BSW 模块标识符。对于非标准化模块，可以选择专有标识符。 |
| providedClientServerEntry | BswModuleClientServerEntry | * | aggr | 指定本模块提供一个可从另一个分区或核调用的 client-server entry。该 entry 在本地上下文中声明，并通过 BSW Scheduler 的配置连接到其他模块或同一模块的 requiredClientServerEntry。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=providedClientServerEntry.shortName, providedClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| providedData | VariableDataPrototype | * | aggr | 指定本模块提供的一个数据原型，以供另一个分区或核读取。providedData 在本地上下文中声明，并通过 BSW Scheduler 的配置连接到其他模块或同一模块的 requiredData。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=providedData.shortName, providedData.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=55 |
| providedModeGroup | ModeDeclarationGroupPrototype | * | aggr | 一组由本模块或集群拥有并提供的模式。它可以通过 BswScheduler 的配置连接到其他模块或集群的 requiredModeGroups。它也可以与关联的 ServiceSwComponentType、EcuAbstractionSwComponentType 或 ComplexDeviceDriverSwComponentType 通过端口提供的模式同步。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=providedModeGroup.shortName, providedModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=25 |
| releasedTrigger | Trigger | * | aggr | 由本模块或集群释放的一个 Trigger。它可以通过 BswScheduler 的配置连接到其他模块或集群的 requiredTriggers。它也可以与关联的 ServiceSwComponentType、EcuAbstractionSwComponentType 或 ComplexDeviceDriverSwComponentType 通过端口提供的 Trigger 同步。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=releasedTrigger.shortName, releasedTrigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| requiredClientServerEntry | BswModuleClientServerEntry | * | aggr | 指定本模块需要一个可在另一个分区或核上实现的 client-server entry。该 entry 在本地上下文中声明，并通过 BSW Scheduler 的配置连接到其他模块或同一模块的 providedClientServerEntry。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=requiredClientServerEntry.shortName, requiredClientServerEntry.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=50 |
| requiredData | VariableDataPrototype | * | aggr | 指定本模块所需的一个数据原型，以由另一个分区或核提供。requiredData 在本地上下文中声明，并通过 BswScheduler 的配置连接到其他模块或同一模块的 providedData。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=requiredData.shortName, requiredData.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=60 |
| requiredModeGroup | ModeDeclarationGroupPrototype | * | aggr | 指定本模块或集群依赖于某个模式组。requiredModeGroup 是本地于本上下文的，并将通过 BswScheduler 的配置连接到另一个模块或集群的 providedModeGroup。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=requiredModeGroup.shortName, requiredModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=30 |
| requiredTrigger | Trigger | * | aggr | 指定本模块或集群对外部触发器作出反应。该 requiredTrigger 在本地上下文中声明，并将通过 BswScheduler 的配置连接到另一个模块或集群的 providedTrigger。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=requiredTrigger.shortName, requiredTrigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=40 |



## 4. BSW 接口

本章描述用于定义 BSW 模块接口层的元模型元素：对 **implementedEntry**、**expectedEntry** 的描述，模式组的声明，触发器的声明，来自其他模块的依赖，以及用于分区间通信的接口。

### 4.1. BSW 模块入口

元类 **BswModuleEntry** 用于建模 C 函数调用的签名，见图 4.1。

**BswModuleEntry** 元类的属性如下表所示。属性 **serviceId** 用于标识 C 函数，因此是 **AUTOSAR** 一致性测试的重要信息。

**BSW 服务标识符**：对于标准化接口，该标识符在模块的 **AUTOSAR 软件规范（SWS）** 中定义。如果 entry 所表示的 C 函数原型不是标准化的，它仍然可以可选地使用，但其值应与标准化的值不同。

**functionPrototypeEmitter 的使用**：如果属性 **functionPrototypeEmitter** 设置为 "RTE"，则 **RTE** 应在模块互连头文件（**Module Interlink Header File**）中生成函数原型。如果该属性设置为其他任何值或不存在，则 BSW 模块应在其头文件中生成并提供该原型。

表 4.1：BswModuleEntry（**BswModuleEntry**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | — | — | — | 本类表示进入 BSW 模块或集群的单个 API 入口（C 函数原型）。C 函数的名称等于本元素的短名称，但有一个例外：在同一 CPU 上存在多个模块实例的情况下，适用关于 "infixes" 的特殊规则，见 **BswImplementation** 类的描述。标签：atp.recommendedPackage=BswModuleEntrys |
| Aggregated by | — | — | — | ARPackage.element |
| argument (ordered) | SwServiceArg | * | aggr | 属于本 BswModuleEntry 的一个参数。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=argument.shortName, argument.variationPoint.shortLabel vh.latestBindingTime=blueprintDerivationTime xml.sequenceOffset=45 |
| bswEntryKind | BswEntryKindEnum | 0..1 | attr | 描述该 entry 是具体的还是抽象的。如果缺少该属性，则该 entry 被视为具体的。标签：xml.sequenceOffset=40 |
| callType | BswCallType | 0..1 | attr | 与该服务关联的调用类型。标签：xml.sequenceOffset=25 |
| executionContext | BswExecutionContext | 0..1 | attr | 指定该服务所需（对于进入本模块的 entry）或保证（对于从本模块调用的 entry）的执行上下文。标签：xml.sequenceOffset=30 |
| functionPrototypeEmitter | NameToken | 0..1 | attr | 该属性用于控制函数原型的生成。如果设置为 "RTE"，则 **RTE** 在模块互连头文件中生成函数原型。 |
| isReentrant | Boolean | 0..1 | attr | 从函数调用者角度的重入性：• **true**：允许在服务完成之前再次调用该服务。• **false**：禁止在服务完成之前再次调用该服务。标签：xml.sequenceOffset=15 |
| isSynchronous | Boolean | 0..1 | attr | 从函数调用者角度的同步性：• **true**：调用同步服务，即调用返回时该服务已完成。• **false**：调用返回时该服务（在语义层面）可能尚未完成。标签：xml.sequenceOffset=20 |
| returnType | SwServiceArg | 0..1 | attr | 属于本 bswModuleEntry 的返回类型。标签：xml.sequenceOffset=40 |
| role | Identifier | 0..1 | attr | 指定该 entry 在给定上下文中的角色。它应等于服务调用的标准化名称，特别是在未指定 **ServiceIdentifier** 的情况下（例如对于回调）。请注意 **ShortName** 并不总是足够，因为它可能是特定于供应商的（例如可以有多个实例的回调）。标签：xml.sequenceOffset=10 |
| serviceId | PositiveInteger | 0..1 | attr | 指向 **AUTOSAR** 基本软件标准化接口的服务标识符。对于非标准化接口，可以可选地用于专有标识。标签：xml.sequenceOffset=5 |
| swServiceImplPolicy | SwServiceImplPolicyEnum | 0..1 | attr | 表示实现策略为标准函数调用、内联函数或宏。这必须在接口层指定，因为它决定了调用的签名。标签：xml.sequenceOffset=35 |

**BswModuleEntry.callType 属性的存在性**：对于每个 **BswModuleEntry**，在 BSW 模块配置完成时属性 **callType** 必须存在。

**BswModuleEntry.executionContext 属性的存在性**：对于每个 **BswModuleEntry**，在 BSW 模块配置完成时属性 **executionContext** 必须存在。

**BswModuleEntry.isReentrant 属性的存在性**：对于每个 **BswModuleEntry**，在 BSW 模块配置完成时属性 **isReentrant** 必须存在。

**BswModuleEntry.isSynchronous 属性的存在性**：对于每个 **BswModuleEntry**，在 BSW 模块配置完成时属性 **isSynchronous** 必须存在。

**BswModuleEntry.swServiceImplPolicy 属性的存在性**：对于每个 **BswModuleEntry**，在 BSW 模块配置完成时属性 **swServiceImplPolicy** 必须存在。

表 4.2：BswEntryKindEnum（**BswEntryKindEnum**）

| 枚举 | BswEntryKindEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | 表示调用进入 Bsw 模块的机制。 |
| Aggregated by | BswModuleEntry.bswEntryKind |
| 字面值 | 说明 |
| abstract | 本 **BswModuleEntry** 指定 C 函数的抽象签名。该签名需要由具体的 **BswModuleEntry** 实现。标签：atp.EnumerationLiteralIndex=0 |
| concrete | 本 **BswModuleEntry** 指定带有签名的具体 C 函数。标签：atp.EnumerationLiteralIndex=1 |

表 4.3：BswExecutionContext（**BswExecutionContext**）

| 枚举 | BswExecutionContext |
| --- | --- |
| Package | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | 指定与该服务关联的调用所需或保证的执行上下文。 |
| Aggregated by | BswModuleEntry.executionContext |
| 字面值 | 说明 |
| hook | 始终是 OS "hook" 例程的上下文。标签：atp.EnumerationLiteralIndex=0 |
| interruptCat1 | 始终是 CAT1 中断上下文。标签：atp.EnumerationLiteralIndex=1 |
| interruptCat2 | 始终是 CAT2 中断上下文。标签：atp.EnumerationLiteralIndex=2 |
| task | 始终是任务上下文。标签：atp.EnumerationLiteralIndex=3 |
| unspecified | API 未指定执行上下文。标签：atp.EnumerationLiteralIndex=4 |

**RTE** 和基本软件调度器（**Basic Software Scheduler**）在某些特殊情况下确实支持通过直接函数调用来调用被触发的 **ExecutableEntity**。尽管如此，必须防止来自特定执行上下文的 **ExecutableEntity** 调用需要更多权限执行上下文的被触发 **ExecutableEntity**。下表列出了支持的组合。

表 4.4：根据 **BswExecutionContext** 通过直接函数调用调用 **ExecutableEntity** 的可能组合

| 调用方的 BswExecutionContext | task | interruptCat2 | interruptCat1 | hook | unspecified |
| --- | --- | --- | --- | --- | --- |
| task | 支持 | 支持 | 支持 | — | 支持 |
| interruptCat2 | — | 支持 | 支持 | — | 支持 |
| interruptCat1 | — | — | 支持 | — | 支持 |
| hook | — | — | — | — | — |
| unspecified | 支持 | — | — | — | 支持 |

**RunnableEntity** 的执行上下文被视为 **task**。

**根据 BswExecutionContext 通过直接函数调用调用 ExecutableEntity**：如果调用方 **BswModuleEntry** 的 **BswExecutionContext** 设置为 **task**、**interruptCat2** 或 **interruptCat1**，则对具有 **interruptCat1** 的 **ExecutableEntity** 的调用可以通过直接函数调用实现。

这适用于通过 **SchM_Trigger**、**SchM_ActMain** 或 **Rte_Trigger** API 调用被触发的 **ExecutableEntity**，或通过 **SchM_Switch** 或 **Rte_Switch** API 调用 **OnEntry ExecutableEntity**、**OnTransition ExecutableEntity**、**OnExit ExecutableEntity** 或模式切换确认 **ExecutableEntity**。有关技术术语的更多信息，请参见 [10]。

表 4.5：BswCallType（**BswCallType**）

| 枚举 | BswCallType |
| --- | --- |
| Package | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | 表示调用进入 Bsw 模块的机制。 |
| Aggregated by | BswModuleEntry.callType |
| 字面值 | 说明 |
| callback | 回调（即调用方指定签名）。标签：atp.EnumerationLiteralIndex=0 |
| callout | Callout——提供扩展现有模块功能的已定义手段。此时调用方指定签名。标签：atp.EnumerationLiteralIndex=4 |
| interrupt | 中断例程。标签：atp.EnumerationLiteralIndex=1 |
| regular | 常规 API 调用。标签：atp.EnumerationLiteralIndex=2 |
| scheduled | 由调度器调用。标签：atp.EnumerationLiteralIndex=3 |

表 4.6：SwServiceImplPolicyEnum（**SwServiceImplPolicyEnum**）

| 枚举 | SwServiceImplPolicyEnum |
| --- | --- |
| Package | M2::MSR::DataDictionary::ServiceProcessTask |
| Note | 本表规定服务实现策略的合法值（在 AUTOSAR 中即 BswModuleEntry）。 |
| Aggregated by | BswModuleEntry.swServiceImplPolicy |
| 字面值 | 说明 |
| inline | 内联服务定义。标签：atp.EnumerationLiteralIndex=0 |
| inlineConditional | 该服务（在 AUTOSAR 中即 BswModuleEntry）的实现方式使其根据稍后设定的条件解析为内联函数或标准函数。以下两个值是标准化的（仅用于代码段且彼此互斥）：• **INLINE** —— 代码段用关键字 "inline" 声明。• **LOCAL_INLINE** —— 代码段用关键字 "static inline" 声明。在两种情况下（**INLINE** 和 **LOCAL_INLINE**），内联展开取决于编译器。据此，代码段要么对应内存中的实际段，要么被放入调用方的段中。标签：atp.EnumerationLiteralIndex=1 |
| macro | 宏服务定义。标签：atp.EnumerationLiteralIndex=2 |
| standard | 标准服务，未定义任何内容时的默认值。标签：atp.EnumerationLiteralIndex=3 |

**调用类型与执行上下文**：在给定的 **BswModuleEntry** 内，其属性适用以下约束：

* **callType == 'interrupt'** 不允许与 **executionContext == 'task'** 或 **'hook'** 同时使用；
* **callType == 'scheduled'** 不允许与 **executionContext == 'interruptCat1'** 或 **'interruptCat2'** 同时使用；
* 这两个枚举的其他组合是允许的。

**BswModuleEntry 的 C 符号**：**BswModuleEntry** 的 **shortName** 应等于实现它的 C 函数的名称，但有一个例外：当单个 CPU 上存在同一模块的多个实例（例如多个 CAN 驱动程序）时，必须通过插入称为 "infixes" 的额外字符使 C 函数名称唯一。由于每个 BSW 模块实例由一段独立的代码实现，infixes 被定义为提供模块各自 **BswImplementation** 的一部分。详情见第 6 章。

因此，要求带有 infixes 的 **BswModuleEntry** 的模块代码也需要一些调整，但这种调整只能在集成时进行。目前 **AUTOSAR** 中没有针对此任务的标准化机制，但可以通过（要求模块的）特定于供应商的配置参数来解决，其值在集成时根据实际提供模块的 infixes 设定。

**SwServiceArg 的使用**：类 **SwServiceArg** 用于声明函数参数以及返回类型的属性。

**SwServiceArg.swImplPolicy 值的限制**：属性 **SwServiceArg.swImplPolicy** 只能具有以下值之一：

* **SwImplPolicyEnum.const**
* **SwImplPolicyEnum.standard**

**SwServiceArg 的 swImplPolicy**：**SwServiceArg** 的属性 **swImplPolicy** 的覆盖值应为 **standard** 或 **const**。该规则应在 BSW 模块配置完成时施加。

**关于 SwServiceArg.category 值的限制**：属性 **SwServiceArg.category** 只能具有以下值：

* **VALUE**
* **DATA_REFERENCE**


> 1 **SwServiceArg** 及其属性属于从 MSR-SW 重构的元模型部分。**MSR-SW** 的这个子集由 **AUTOSAR** 元模型和作为 AUTOSAR 发布版一部分发布的 XML schema 定义。相关类在类图中以绿色显示。更多说明见 [6] 和 [12]。

> 2 此选项的有效用例非常少，例如以原生 C 表示法定义函数指针，例如：`int (*SwCluC_BManif_VoidFncPtrType)(void);`

请注意，在 TPS 软件组件模板 [6] 的上下文中，对 **SwServiceArg** 的使用存在一些规定。

表 4.7：SwServiceArg（**SwServiceArg**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::MSR::DataDictionary::ServiceProcessTask |
| Note | — | — | — | 指定在 SwService 调用期间交换的数据对象的属性，例如参数或返回值。**SwServiceArg** 也可用于 C 宏的参数列表。为此，category 应设置为 "MACRO"。如果实际参数具有 implementationDataType，则可以可选地添加对它的引用。 |
| Base | — | — | — | ARObject, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswModuleEntry.argument, BswModuleEntry.returnType |
| direction | ArgumentDirectionEnum | 0..1 | attr | 指定数据传输的方向。该方向应指示调用方和/或被调方所消耗的实际信息的方向，而不是 C 中形式参数的方向。出于向后兼容的原因，该属性是可选的。例如，如果使用指针传递预期结果的内存地址，则方向应为 "out"。如果使用指针传递内容供被调方读取的内存地址，则其方向应为 "in"。标签：xml.sequenceOffset=10 |
| swArraysize | ValueList | 0..1 | aggr | 这将服务的参数变为数组。标签：xml.sequenceOffset=20 |
| swDataDefProps | SwDataDefProps | 0..1 | aggr | 本 **SwServiceArg** 的数据属性。构造型：atpSplitable 标签：atp.Splitkey=swDataDefProps xml.sequenceOffset=30 |

**SwServiceArg.swDataDefProps.implementationDataType**：应用于将数据定义与可重用的类型定义（对应于 C typedef）关联起来。因为 **ImplementationDataType** 是一个 **ARElement** 且自身包含 **SwDataDefProps**，所以可以将所需的数据属性声明为 **ImplementationDataType** 的一部分，并通过引用它作为数据类型来重用它。

**ImplementationDataType** 中的 **ImplementationDataTypeElement** 允许声明复合类型（对应于 C 结构体或数组）。

**SwServiceArg.swDataDefProps.swPointerTargetProps**：连同其 category（见 [6]）一起，用于将一个参数或返回类型声明为指向另一个数据对象或函数的指针。

表 4.8：SwPointerTargetProps（**SwPointerTargetProps**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::MSR::DataDictionary::DataDefProperties |
| Note | — | — | — | 本元素定义：由聚合元素指定的数据对象在 CPU 代码中包含对另一个数据对象或函数的引用。这对应于 C 语言中的指针。本元素的属性描述目标的 category 和详细属性，目标要么是数据描述，要么是函数签名。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | SwDataDefProps.swPointerTargetProps |
| functionPointerSignature | BswModuleEntry | 0..1 | ref | 被引用的 **BswModuleEntry** 用作函数指针定义的签名。主要用例：作为实参传递给其他函数的函数指针。标签：xml.sequenceOffset=40 |
| swDataDefProps | SwDataDefProps | 0..1 | aggr | 目标数据类型的属性。构造型：atpSplitable 标签：atp.Splitkey=swDataDefProps xml.sequenceOffset=30 |
| targetCategory | Identifier | 0..1 | attr | 指定目标的 category：• 对于数据指针，应指定被引用数据的 category。• 对于函数指针，可用于表示被引用 **BswModuleEntry** 的 category。标签：xml.sequenceOffset=5 |

**函数指针目标的实现策略**：只有当 **BswModuleEntry** 的 **swServiceImplPolicy** 为 'standard' 时，它才能用作函数指针的目标（**SwPointerTargetProps.functionPointerSignature**）。

有关 **ImplementationDataType**、**SwBaseType** 以及 **SwServiceArg.category** 与 **SwDataDefProps** 相关使用的更多信息，见 [6]。这包括使用 **SwServiceArg.category** 的 **VALUE** 来支持用 C-build-in 数据类型建模 C 签名，或使用指向 C 签名（使用 C-build-in 数据类型）的函数指针。例如：`int (*SwCluC_BManif_VoidFncPtrType)(void);`。

请注意，对于 **AUTOSAR** 基本软件，这被视为一种例外情况，因为通常此类类型通过平台类型（**Platform Types**）抽象。

包含 C 关键字 **void** 的函数签名需要特别注意：

**无 returnType 的 BswModuleEntry**：在返回类型为空（C 中为 'void'）的情况下，不应设置引用 **BswModuleEntry.Type**。

**无 argument 的 BswModuleEntry**：在参数列表为空（C 中为 'void'）的情况下，不应设置任何引用 **BswModuleEntry.argument**。

请注意，尽管如此，仍然存在一个表示 void 类型作为指针目标的 **SwBaseType**。

**category "MACRO" 的使用**：只有当拥有该 **SwServiceArg** 的 **BswModuleEntry** 的 **swServiceImplPolicy** 属性设置为 **macro** 时，才允许对该 **SwServiceArg** 使用 category "MACRO"。

此外，[6] 中 "Data Categories" 一章定义的 category "MACRO" 的使用仅限于如上所述的 **SwServiceArg**。仍然支持作为宏的 **BswModuleEntry** 用 [6] 中表 5.7 定义的其他 category 描述其 **SwServiceArg**，以表达假定的返回值类型和宏参数类型。

**SwServiceArg.direction**：允许声明数据流的方向（该属性在 R4.0.3 中引入，出于向后兼容原因可选）：

表 4.9：ArgumentDirectionEnum（**ArgumentDirectionEnum**）

| 枚举 | ArgumentDirectionEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes |
| Note | 用例：• **ClientServerOperation** 中的参数可以有不同的方向，需要正式指出，因为它们会影响最终函数签名的形式。• **BswModuleEntry** 中的参数已经确定了函数签名，但方向用于指定语义，尤其是指针参数的语义。 |
| Aggregated by | ArgumentDataPrototype.direction, SwServiceArg.direction |
| 字面值 | 说明 |
| in | 参数值传递给被调方。标签：atp.EnumerationLiteralIndex=0 |
| inout | 参数值传递给被调方，同时也从被调方传回调用方。标签：atp.EnumerationLiteralIndex=1 |
| out | 参数值从被调方传递给调用方。标签：atp.EnumerationLiteralIndex=2 |

该值的选择应与 **SwServiceArg** 实例的角色和形式签名兼容：

**BswModuleEntry returnType 的方向**：**BswModuleEntry.returnType.direction** 不得取值 **in** 或 **inout**。

**BswModuleEntry argument 的方向**：如果 **BswModuleEntry.argument.direction** 取值 **out** 或 **inout**，则相应的 **BswModuleEntry.argument.swDataDefProps** 加上最终被引用的 **ImplementationDataType** 应使得它们产生一个指针声明。

也可以指定在 C 中包含关键字 **enum** 的函数签名：

**C 中包含关键字 enum 的函数签名**：相应的 **ImplementationDataType** 或 **ImplementationDataTypeElement** 必须在关联的 **SwDataDefProps.additionalNativeTypeQualifier** 中包含字符串 'enum'，并使用关联的 **CompuMethod**，其 category 为 **TEXTTABLE**。

提示：代码生成器可以使用此信息生成正确的签名。如果应用此方法生成 C 风格枚举，应避免使用相同的 **CompuMethod** 作为生成器（例如 **RTE** 生成器）的输入，因为后者会改为生成预处理器字面量。否则，枚举字面量和预处理器字面量可能发生冲突。

### 4.2. BSW 模式声明

**BswModuleDescription.providedModeGroup 的使用**：通过可选属性 **providedModeGroup**，BSW 模块可以声明一个或多个 **ModeDeclarationGroupPrototype**，每个定义一组模式（模式组），用于控制其他 BSW 模块的活动。那些需要被该模式组控制的模块，必须声明一个兼容的 **ModeDeclarationGroupPrototype** 作为 **requiredModeGroup** 属性。更多信息见图 4.2。

关于 **ModeDeclarationGroupPrototype** 的兼容性，见 [6] [constr_1074]。这些声明允许 **BSW Scheduler** 适当地生成 API 并协调模式切换。请注意，**BSW Scheduler** 的配置实际上决定了哪个提供的模式组连接到哪个要求的模式组。这使得单个模块的规范独立于整个 BSW 设置。

**ModeDeclarationGroupPrototype** 基于元类 **ModeDeclarationGroup** 的类型定义。由于可以在基本软件中和 **RTE** 之上的软件组件中使用相同的 **ModeDeclarationGroup**，因此 **ModeDeclarationGroupPrototype** 和 **ModeDeclarationGroup** 都是元模型 **CommonStructure** 包的一部分。有关模式语义的更多信息，见 [6]。

通过聚合 **ModeErrorBehavior**，**ModeDeclarationGroup** 可以定义模式管理器和/或模式用户在出错时的行为。这在 [6] 的 "Mode Error Behavior" 一章中进一步说明。

表 4.10：ModeDeclarationGroupPrototype（**ModeDeclarationGroupPrototype**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | **ModeDeclarationGroupPrototype** 指定在给定上下文中提供或要求的一组模式（**ModeDeclarationGroup**）。 |
| Base | — | — | — | ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, BswModuleDescription.providedModeGroup, BswModuleDescription.requiredModeGroup, FirewallStateSwitchInterface.firewallStateMachine, FunctionGroupSet.functionGroup, ModeSwitchInterface.modeGroup, Process.processStateMachine, StateManagementStateNotification.stateMachine |
| swCalibrationAccess | SwCalibrationAccessEnum | 0..1 | attr | 这允许指定封闭的 **ModeDeclarationGroupPrototype** 是否可以在运行时被测量。 |
| type | ModeDeclarationGroup | 0..1 | tref | 组件支持的 "ModeDeclarations 的集合"（即 **ModeDeclarationGroup**）。构造型：isOfType |

请注意，通过在角色 **swCalibrationAccess** 中聚合 **SwCalibrationAccessEnum**，**ModeDeclarationGroupPrototype** 获得了可测量的能力。关于 **swCalibrationAccess** 可能值的约束，请参见 [6]。


表 4.11：ModeDeclarationGroup（**ModeDeclarationGroup**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | 模式声明的集合。同时显式标识初始模式。标签：atp.recommendedPackage=ModeDeclarationGroups |
| Base | — | — | — | ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement |
| Aggregated by | — | — | — | ARPackage.element |
| initialMode | ModeDeclaration | 0..1 | ref | **ModeDeclarationGroup** 的初始模式。该模式在任何模式切换发生之前处于活动状态。 |
| modeDeclaration | ModeDeclaration | * | aggr | 收集在本 **ModeDeclarationGroup** 中的 **ModeDeclaration**。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=modeDeclaration.shortName, modeDeclaration.variationPoint.shortLabel vh.latestBindingTime=blueprintDerivationTime |
| modeManagerErrorBehavior | ModeErrorBehavior | 0..1 | aggr | 表示定义模式管理器在模式用户侧出错（例如模式用户终止）时期望的错误行为的能力。 |
| modeTransition | ModeTransition | * | aggr | 表示 **ModeDeclarationGroup** 可用的 **ModeTransition**。 |
| modeUserErrorBehavior | ModeErrorBehavior | 0..1 | aggr | 表示定义模式用户在模式管理器侧出错（例如模式管理器终止）时期望的错误行为的能力。 |
| onTransitionValue | PositiveInteger | 0..1 | attr | **RTE** 生成器应考虑本属性的值，以编程方式表示用于两个状态之间转换的值。 |

表 4.12：ModeDeclaration（**ModeDeclaration**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | 声明一个模式。特定模式的名称和语义不在元模型中定义。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, ModeDeclarationGroup.modeDeclaration |
| value | PositiveInteger | 0..1 | attr | **RTE** 应取本属性的值来生成本 **ModeDeclaration** 的源代码表示。 |

表 4.13：ModeTransition（**ModeTransition**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | 本元类表示在 **ModeDeclarationGroup** 上下文中描述可能的 **ModeTransition** 的能力。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, ModeDeclarationGroup.modeTransition |
| enteredMode | ModeDeclaration | 0..1 | ref | 表示 **ModeTransition** 进入的模式。 |
| exitedMode | ModeDeclaration | 0..1 | ref | 表示 **ModeTransition** 退出的模式。 |

表 4.14：ModeErrorBehavior（**ModeErrorBehavior**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | 表示在模式处理上下文中定义错误行为的能力。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | ModeDeclarationGroup.modeManagerErrorBehavior, ModeDeclarationGroup.modeUserErrorBehavior |
| defaultMode | ModeDeclaration | 0..1 | ref | 表示在封闭的 **ModeDeclarationGroup** 上下文中被视为错误模式的 **ModeDeclaration**。 |
| errorReactionPolicy | ModeErrorReactionPolicyEnum | 0..1 | attr | 表示以何种策略定义在发生错误时应应用哪个默认模式的能力。 |

表 4.15：ModeErrorReactionPolicyEnum（**ModeErrorReactionPolicyEnum**）

| 枚举 | ModeErrorReactionPolicyEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | 表示指定对模式错误作出反应的能力。 |
| Aggregated by | ModeErrorBehavior.errorReactionPolicy |
| 字面值 | 说明 |
| defaultMode | 表示在模式错误时切换到 **defaultMode** 的能力。标签：atp.EnumerationLiteralIndex=0 |
| lastMode | 表示在模式错误时保持上一个模式的能力。标签：atp.EnumerationLiteralIndex=1 |

为了避免可能包含在同一 C 文件中的生成头文件中的冲突，适用以下约束：

**BSWM 引用的不同模式组应具有不同的名称**：一个 **BswModuleDescription** 不得引用具有相同 **shortName** 但元素不同的不同 **ModeDeclarationGroup**（通过 **requiredModeGroup** 和/或 **providedModeGroup**）。

属性 **ModeDeclaration.value**、**ModeDeclarationGroup.onTransitionValue** 以及 **ModeDeclarationGroup** 的 category 允许从形式定义确定源代码的生成。关于这些属性的约束，请参见 [6]。

**BSW 中的 ModeRequestTypeMap**：此外，需要定义一个 **ModeRequestTypeMap**，以显式指定 **ModeDeclarationGroup** 由哪种数据类型实现：

表 4.16：ModeRequestTypeMap（**ModeRequestTypeMap**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | — | — | — | 指定 **ModeDeclarationGroup** 与 **ImplementationDataType** 之间的映射。该 **ImplementationDataType** 应用于实现 **ModeDeclarationGroup**。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | DataTypeMappingSet.modeRequestTypeMap |
| implementationDataType | AbstractImplementationDataType | 0..1 | ref | 这是相应的 **AbstractImplementationDataType**。它应按照 "类似无符号整数" 数据类型的思想建模。 |
| modeGroup | ModeDeclarationGroup | 0..1 | ref | 这是相应的 **ModeDeclarationGroup**。 |

**BSW 中 ModeRequestTypeMap 的限制**：对于 **BswModuleDescription** 中使用的 **ModeDeclarationGroupPrototype** 所引用的每个 **ModeDeclarationGroup**，必须存在一个 **ModeRequestTypeMap**，它既指向该 **ModeDeclarationGroup**，也指向一个合适的 **ImplementationDataType**。

该 **ModeRequestTypeMap** 应由一个 **DataTypeMappingSet** 聚合，而该 **DataTypeMappingSet** 由 **BswModuleDescription** 聚合的 **BswInternalBehavior** 引用。

关于可用于此类映射的 **ImplementationDataType** 的限制，请参见 [6]。由于提供和要求模式是通过 ECU 配置连接的，因此无法仅在 BSWMD 层面检查这些 **ImplementationDataType** 的约束。

### 4.3. BSW 触发器声明

**BSW 中 Trigger 的使用**：通过可选属性 **releasedTrigger**，BSW 模块可以声明它释放一个或多个 **Trigger**，这些 **Trigger** 用于跨 BSW 模块触发事件。希望对此类触发器作出反应的其他模块，必须声明一个兼容的 **Trigger** 作为 **requiredTrigger** 属性（关于 **Trigger** 的兼容性，见 [6] [constr_1038]）。这些声明连同关联的事件模型允许 **BSW Scheduler** 适当地生成 API 并进行协调。详情见第 5.7 章。

请注意，**BSW Scheduler** 的配置实际上决定了哪个释放的触发器连接到哪个要求的触发器。这使得单个模块的规范独立于整个 BSW 设置。

表 4.17：Trigger（**Trigger**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration |
| Note | — | — | — | 在给定上下文中提供（即释放）或要求（即用于激活某物）的触发器。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, BswModuleDescription.releasedTrigger, BswModuleDescription.requiredTrigger, ServiceInterface.trigger, TriggerInterface.trigger |
| swImplPolicy | SwImplPolicyEnum | 0..1 | attr | 当本属性设置为 **queued** 时，允许对 **Trigger** 进行排队处理。 |
| triggerPeriod | MultidimensionalTime | 0..1 | aggr | 对于周期性（时间或角度）驱动的外部触发器，可选地定义周期。 |

**Trigger** 声明可以可选地设置一个属性来定义其排队行为。这在 [6] 中有更详细的说明。枚举类型 **SwImplPolicyEnum** 在 **Trigger.swImplPolicy** 中的使用受到如下限制：

**BSW 中 Trigger.swImplPolicy 的允许值**：属性 **Trigger.swImplPolicy** 唯一允许的值是 **STANDARD**（此时 **Trigger** 处理不使用队列）或 **QUEUED**（此时 **Trigger** 的处理肯定使用队列）。

### 4.4. BSW 模块依赖

#### 4.4.1. 概述

图 4.3 及下表展示了类 **BswModuleDependency** 的详情。该类表示一个 BSW 模块或集群对另一个 BSW 模块或集群的期望。

应当注意，为了定义依赖，并不需要拥有目标 **BswModuleDescription** 的完整模型。这允许分别维护每个 BSWMD。尽管如此，目标模块需要通过属性 **BswModuleDependency.targetModuleId** 和/或 «atpUriDef» 引用 **BswModuleDependency.targetModuleRef** 来标识。当然，如果同时使用这两个属性，它们的值应保持一致。

由于模块标识符并不总能足以标识目标模块（例如复杂驱动程序都具有相同的模块 ID），因此推荐使用 **targetModuleRef**。

一个模块不能声明对自身的依赖：

**bswModuleDependency 应指向不同的模块**：


* **BswModuleDescription.bswModuleDependency.targetModuleId**（如果给出）应不同于 **BswModuleDescription.moduleId**。当值为 254（用于 IO 硬件抽象模块）或 255（用于复杂驱动程序模块）时，此规则不适用。
* **BswModuleDependency.targetModuleRef**（如果给出）应不同于拥有该 **BswModuleDependency** 的 **BswModuleDescription** 的包位置。

**expectedEntry** 集合表示以函数调用形式从另一个模块导入的接口。

#### 4.4.2. 依赖与包

重要的是要注意，通过 **BswModuleDependency**，拥有依赖的模块描述引用了一些模型元素，这些元素也被它所依赖的模块的描述所引用。这对于 **BswModuleEntry** 的实例尤其如此，但也适用于其他 **ARElement**，例如从那里引用的数据类型。为了避免不一致，应将此类共同使用的 M1 元素放在 **ARPackage** 方面定义明确的位置。

标准化 M1 模型元素的包位置规则在 [1] 的 "Identifying M1 elements in packages" 一章中给出。因此我们可以表述为：

**标准化 BswModuleEntry 的位置**：为 AUTOSAR 模块 &lt;module&gt; 定义的标准化 **BswModuleEntry** 实例应位于包 AUTOSAR\_&lt;module&gt;/BswModuleEntrys/ 之下。

> 4 此处 &lt;module&gt; 是 API 所属的标准化 ICC3 模块的模块缩写。

例如：

AUTOSAR\_Can/BswModuleEntrys/Can\_SetControllerMode

**对标准化 BswModuleEntry 的引用**：如果 BSWMD 通过 **implementedEntry** 或 **expectedEntry** 引用标准化 **BswModuleEntry**，它还必须使用路径 AUTOSAR\_&lt;module&gt;/BswModuleEntrys/，从而表明它依赖于所引用 API 函数的符合 AUTOSAR 的实现。

强烈建议对非标准化 **ARElement** 的包名也遵循类似的模式（但不以 AUTOSAR 开头）。如果 BSWMD 在其依赖中引用如下路径：

&lt;vendor\_specific\_prefix&gt;\_&lt;module&gt;/BswModuleEntrys/

例如 VendorX\_Can/BswModuleEntrys/Can\_SpecialFunction，这将表明 BSWMD 依赖于所引用模块（例如 **Can**）的特定于供应商的函数或回调。

此外，**targetModuleRef** 的值应设置为：

VendorX\_Can/BswModuleDescriptions/Can

在本示例中，如果被引用模块是复杂驱动程序，我们将使用非标准化模块名代替 **Can**。在这种情况下，模块名将等于该复杂驱动程序的 BSWMD 的 **BswModuleDescription.shortName**。

#### 4.4.3. 依赖：示例与约束

请注意，**expectedEntry** 确实也包括中断上下文中的调用。示例如下：

假设我们要描述一个外部 EEPROM 驱动程序模块对（标准化的）AUTOSAR SPI 模块的回调依赖。假设 SPI 驱动程序提供一个总是在中断上下文中调用的传出回调 "EndJobNotification"。为了描述该依赖，我们需要创建一个 **BswModuleDescription.bswModuleDependency** 实例并进行如下赋值：

* **bswModuleDependency.targetModuleId** = SPI 驱动程序的模块标识符（或者，我们可以使用 **bswModuleDependency.targetModuleRef**）

图 4.4 展示了两个假设 BSW 模块之间依赖关系的 M1 模型的另一个示例。该依赖包括一个由下层模块 'Any' 实现的常规函数（可以代表 MCAL 模块）和两个由上层模块 'MyComplexDriver' 实现的回调。

> 5 作为给定元类（派生自 **ARElement**）实例的直接容器的包的推荐名称定义为 UML 标签，可在相应的类表中查看。

> 6 **AUTOSAR** BSW 架构区分 **callback** 和 **callout** 的语义：callback 向上层模块通知某件事，而 callout 用于向调用模块添加功能。在 BSWMD 中，这两种机制可以用相同的方式描述。

请注意，传出回调的模型通常只能在配置时完成，因为用作回调的 **BswModuleEntry** 的数量和名称在交付下层模块的 BSWMD 时可能是未知的。然而，在那个时候仍然可以通过使用预期 **BswModuleEntry** 的 **AtpBlueprint** 来描述回调函数的签名，并将该描述与下层模块的 BSWMD 一起交付。关于 blueprint 概念的更多细节，见 [9]。

除了直接函数调用之外，两个 BSW 模块还可以通过其接口中声明的触发器或模式连接。这不会显示为依赖，因为实际连接是由 **BSW Scheduler** 的配置创建的。

请注意，**BswModuleDependency** 也可以包含 **ServiceNeeds**。然而，这是一个已弃用的关系（仅允许用于向后兼容），因为 **ServiceNeeds** 的声明已移至内部行为层，见第 12 章。

### 4.5. BswModuleEntry 关系集

**BswEntryRelationshipSet** 描述 **BswEntryRelationship** 的集合。**BswEntryRelationship** 描述两个 **BswModuleEntry** 之间的关系以及关系类型。这通常用于表示具体的 **BswModuleEntry** 派生自抽象的 **BswModuleEntry**。在这种情况下，**bswEntryRelationshipType** 设置为 **drivedFrom**，**BswEntryRelationship.from** 引用抽象的 **BswModuleEntry**，**BswEntryRelationship.to** 引用具体的 **BswModuleEntry**。

表 4.25：BswEntryRelationshipSet（**BswEntryRelationshipSet**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | — | — | — | 描述两个 BswModuleEntry 之间的一组关系。标签：atp.recommendedPackage=BswEntryRelationshipSets |
| Base | — | — | — | ARElement, ARObject, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable |
| Aggregated by | — | — | — | ARPackage.element |
| bswEntryRelationship | BswEntryRelationship | * | aggr | 两个 BswModuleEntry 之间的关系。 |

**BswEntryRelationshipSet.bswEntryRelationship 属性的存在性**：对于每个 **BswEntryRelationshipSet**，在 BSW 模块配置完成时属性 **bswEntryRelationship** 必须至少存在一次。

表 4.26：BswEntryRelationship（**BswEntryRelationship**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | — | — | — | 描述两个 BswModuleEntry 之间的关系以及关系类型。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | BswEntryRelationshipSet.bswEntryRelationship |
| bswEntryRelationshipType | BswEntryRelationshipEnum | 0..1 | attr | 表示关系的类型。标签：xml.sequenceOffset=5 |
| from | BswModuleEntry | 0..1 | ref | 引用抽象 **BswModuleEntry** 的关系类型。请注意，此时 **bswEntryRelationshipType** 应设置为 **drivedFrom**。 |
| to | BswModuleEntry | 0..1 | ref | 引用具体 **BswModuleEntry** 的关系类型。 |

**BswEntryRelationship.bswEntryRelationshipType 属性的存在性**：对于每个 **BswEntryRelationship**，在 BSW 模块配置完成时属性 **bswEntryRelationshipType** 必须存在。

**BswEntryRelationship.from 角色中引用的存在性**：对于每个 **BswEntryRelationship**，在 BSW 模块配置完成时角色 **from** 中的引用必须存在。

**BswEntryRelationship.to 角色中引用的存在性**：对于每个 **BswEntryRelationship**，在 BSW 模块配置完成时角色 **to** 中的引用必须存在。

表 4.27：BswEntryRelationshipEnum（**BswEntryRelationshipEnum**）

| 枚举 | BswEntryRelationshipEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | 定义两个 BswModuleEntry 之间关系的类型。 |
| Aggregated by | BswEntryRelationship.bswEntryRelationshipType |
| 字面值 | 说明 |
| derivedFrom | 表示作为 "to" 引用的 **BswModuleEntry** 需要与作为 "from" 引用的 "抽象" **BswModuleEntry** 具有相同的签名。标签：atp.EnumerationLiteralIndex=0 |

### 4.6. BSW 分区间接口

#### 4.6.1. 概述

**AUTOSAR** BSW 具有跨分区边界通信的能力，包括跨处理器核边界的通信。

虽然这通常可以通过 **RTE** 使用端口和位于 BSW 模块之上的软件组件（例如复杂驱动程序）来实现，但借助作为 **RTE** 一部分的 **BSW Scheduler** 提供的 "胶水代码"，存在更高效的机制。详细指南见 [13]。

这些机制遵循 **VFB** 的 Client-Server 通信模式或 Sender-Receiver 通信模式——见 [14]——但不能用于 interECU 通信。

所需的元模型部分如图 4.6 所示。

#### 4.6.2. Client-Server

表 4.28：BswModuleClientServerEntry（**BswModuleClientServerEntry**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces |
| Note | — | — | — | 本元类表示进入 BSW 模块或集群的单个 API 入口，它能够通过 **BSW Scheduler** 以 client-server 方式调用。在这方面它比 **BswModuleEntry** 更特殊，可以看作是对它所引用的 **BswModuleEntry**（属性 **encapsulatedEntry**）的包装。标签：atp.recommendedPackage=BswModuleEntrys |
| Base | — | — | — | ARObject, Referrable |
| Aggregated by | — | — | — | BswModuleDescription.providedClientServerEntry, BswModuleDescription.requiredClientServerEntry |
| encapsulatedEntry | BswModuleEntry | 0..1 | ref | 底层的 **BswModuleEntry**。标签：xml.sequenceOffset=5 |
| isReentrant | Boolean | 0..1 | attr | 从通过 **BSW Scheduler** 调用服务的客户端角度的重入性：• **true**：允许在服务完成之前再次调用该服务。• **false**：禁止在服务完成之前再次调用该服务。标签：xml.sequenceOffset=10 |
| isSynchronous | Boolean | 0..1 | attr | 从通过 **BSW Scheduler** 调用服务的客户端角度的同步性：• **true**：调用同步服务，即调用返回时该服务已完成。• **false**：调用返回时该服务（在语义层面）可能尚未完成。标签：xml.sequenceOffset=15 |

请注意，**executionContext** 应始终遵循上述规则。

**BSW Scheduler** 的配置决定哪个 **providedClientServerEntry** 实际连接到哪个 **requiredClientServerEntry**。这使得单个模块的规范独立于整个 BSW 设置。

**BswModuleClientServerEntry 属性的语义**：可选属性 **BswModuleClientServerEntry.isReentrant** 和 **isSynchronous**……

> 7 这并不排除客户端和服务器在同一分区中执行 configurations。

**BswModuleClientServerEntry.encapsulatedEntry 角色中引用的存在性**：对于每个 **BswModuleClientServerEntry**，在 BSW 模块配置完成时角色 **encapsulatedEntry** 中的引用必须存在。

**BswModuleClientServerEntry 的声明**：通过可选属性 **providedClientServerEntry**，BSW 模块可以声明它提供一个 **BswModuleClientServerEntry**，可在服务器角色中用于跨分区边界的 client-server 通信。客户端模块（可以是不同的或相同的模块）必须声明一个兼容的 **BswModuleClientServerEntry** 作为属性 **requiredClientServerEntry**。这些声明连同关联的事件模型允许 **BSW Scheduler** 适当地生成 API 并进行协调。详情见第 5.7 章。

**BswModuleClientServerEntry 的兼容性**：两个 **BswModuleClientServerEntry** 兼容当且仅当下列所有条件成立：

* 它们的同步性值相同。这些值取自属性 **isSynchronous**，或者如果未定义，则取自 **encapsulatedEntry.isSynchronous**；
* 作为 **encapsulatedEntry** 引用的两个 **BswModuleEntry** 具有相同的 **SwServiceArg**、**returnType**、**serviceId** 和 **swServiceImplPolicy**。

**BswModuleClientServerEntry.isSynchronous** 可以具有与被引用的 **BswModuleClientServerEntry.encapsulatedEntry** 的对应属性不同的值，因为前者描述通过 **BSW Scheduler** 调用的客户端所看到的属性，而后者包含直接调用者所看到的属性。如果其中一个属性未定义，则其值被视为等于被引用的 **encapsulatedEntry** 的相应属性。

**引用 BswModuleEntry 的不同方式**：在给定 BSWMD 中，**BswModuleEntry**（即函数签名的声明）可以通过两种不同方式引用：

1. 作为 "直接" 模块接口的一部分，即作为 **implementedEntry** 或 **expectedEntry**；
2. 作为通过 **BswModuleClientServerEntry.encapsulatedEntry** 的 client-server "远程" 接口的一部分。

如果某个 **BswModuleEntry** 既被直接调用又通过 client-server 调用，则可以在同一 BSWMD 中对同一个 **BswModuleEntry** 组合使用这两种可能性。但是，如果 **BswModuleEntry** 仅以 client-server 方式使用，建议不要额外使用第一种方式。

特别地，在这种情况下不需要声明 **bswModuleDependency**，因为实际连接是在配置时完成的，两个模块环境不需要交换头文件。

通过 **BSW Scheduler** 的 Client-Server 通信对服务器侧函数调用的性质施加了一些约束：

**用于 Client-Server 的 BswModuleEntry 的约束**：在角色 **BswModuleClientServerEntry.encapsulatedEntry** 中使用的 **BswModuleEntry** 应具有如下属性值：

* **callType** 应为 **regular** 或 **callback**；
* **executionContext** 应为 **task**。

#### 4.6.3. Sender-Receiver

**providedData 与 requiredData 的声明**：通过可选属性 **providedData**，BSW 模块可以声明它提供一个 **VariableDataPrototype**，可在发送者角色中用于跨分区边界的 sender-receiver 通信。接收模块（可以是不同的或相同的模块）必须声明一个兼容的 **VariableDataPrototype** 作为属性 **requiredData**（关于 **VariableDataPrototype** 的兼容性，见 [6] [constr_1068]）。这些声明连同关联的事件模型和 ECU 配置允许 **BSW Scheduler** 适当地生成 API 并进行协调。详情见第 5.7 章。

> 8 这并不排除发送者和接收者在同一分区中执行 configurations。

**providedData 与 requiredData 的约束**：BSW 中的 SenderReceiver 通信仅限于所谓的显式通信模式（与 [6] 中为软件组件描述的相同），且具有排队行为。这导致对角色 **BswModuleDescription.providedData** 或 **BswModuleDescription.requiredData** 中引用的 **VariableDataPrototype** 的一些约束：

* 它不应具有 **initValue**；
* 其 **swDataDefProps.swImplPolicy** 应设置为 **queued**；
* 其 **swDataDefProps.swCalibrationAccess** 应设置为 **notAccessible**。

对于在这些角色中使用的 **VariableDataPrototype** 的属性或底层 **AutosarDataPrototype**，没有进一步的形式约束。

请注意，**BSW Scheduler** 的 ECU 配置决定哪个 **providedData** 实际连接到哪个 **requiredData**。这使得单个模块的规范独立于整个 BSW 设置。

### 4.7. 计数值集合

#### 4.7.1. 背景

当大量软件组件集成到 ECU 上时，**RTE** 通信缓冲区（例如用于隐式通信）的分配或特定函数的分配正在成为关键的性能因素。有了对 **RTE API** 调用频率以及由此对数据访问执行频率的了解，就可以优化实现。例如，将具有高访问频率的缓冲区放入低延迟的存储器中。

#### 4.7.2. AccessCountSets

元类 **AccessCountSet** 提供了一组计数值，表示一个实现针对特定 **ExecutableEntity** 的某个 **AbstractAccessPoint** 调用 **RTE** / **SchM** API 的频率。

表 4.29：AccessCountSet（**AccessCountSet**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount |
| Note | — | — | — | 本元类提供一组根据特定 **countProfile** 的规则评估的计数值。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | ResourceConsumption.accessCountSet |
| accessCount | AccessCount | * | aggr | 针对一个 **AbstractAccessPoint** 的计数值。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=accessCount, accessCount.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| countProfile | NameToken | 0..1 | attr | 本属性定义用于确定 **AccessCount.value** 数字的计数配置文件的名称。 |

**AccessCountSet.countProfile 属性的存在性**：对于每个 **AccessCountSet**，在 BSW 模块配置完成时属性 **countProfile** 必须存在。

表 4.30：AccessCount（**AccessCount**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount |
| Note | — | — | — | 本元类为一个 **AbstractAccessPoint** 提供一个计数值。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | AccessCountSet.accessCount |
| accessPoint | AbstractAccessPoint | 0..1 | ref | 计数值所适用的 **AbstractAccessPoint**。 |
| value | PositiveInteger | 0..1 | attr | 本属性表示确定的访问次数。构造型：atpVariation 标签：vh.latestBindingTime=preCompileTime |

**AccessCount.value 属性的存在性**：对于每个 **AccessCount**，在 BSW 模块配置完成时属性 **value** 必须存在。

表 4.31：AbstractAccessPoint（**AbstractAccessPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount |
| Note | — | — | — | 指示来自 **ExecutableEntity** 的访问点的抽象类。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | AsynchronousServerCallResultPoint, ExternalTriggeringPointIdent, InternalTriggeringPoint, ModeAccessPointIdent, ModeSwitchPoint, ParameterAccess, ServerCallPoint, VariableAccess |
| Aggregated by | — | — | — | AtpClassifier.atpFeature |
| returnValueProvision | RteApiReturnValueProvisionEnum | 0..1 | attr | 本属性控制为与封闭访问点对应的 **RTE API** 提供返回值的方式。 |

**AccessCount.value 描述固有属性**：**AccessCountSet** 中的 **AccessCount.value** 是关于单个 **ExecutableEntity** 在代码执行时关于 **RTE/SchM API** 使用的实现的陈述。这些值独立于特定 **ExecutableEntity** 的各个 **AbstractAccessPoint** 的后期集成。

这意味着这些数字是特定 **ExecutableEntity** 的单个 **AbstractAccessPoint** 的特征，并且根据产生的调用图，可能需要计算合并后的访问次数作为集成决策的基础。例如，如果某个服务器 runnable 在循环中被周期性调度的 runnable 通过直接函数调用调用 5 次，则服务器 runnable 中数据访问的固有计数值需要乘以 5，以获得每个时间段合并后的有效访问次数。

一般来说，计数值的提供者和计数值的使用者需要对如何确定这些值有共同的理解，以便在优化中适当地考虑它们。由于优化主题可能会进一步增强，**AccessCountSet** 通过属性 **countProfile** 提供有关计数策略的信息。

**属性 countProfile 表示计数规则**：属性 **countProfile** 表示用于确定 **AccessCount.value** 的适用计数规则的集合。

**属性 countProfile 的标准化值**：**AUTOSAR** 定义属性 **countProfile** 的以下标准化值：

* **DISTINGUISH\_SINGULAR\_ACCESSES**

请注意，将来可能会定义更多的计数配置文件。

#### 4.7.3. countProfile 的定义：DISTINGUISH_SINGULAR_ACCESSES

**countProfile** **DISTINGUISH\_SINGULAR\_ACCESSES** 的目的是一方面确定 **RTE API** 调用的典型频率，以支持内存分配的调整。另一方面，它应足够信息丰富，以提供关于通过隐式通信模式访问数据的最大次数的精确信息，该信息也可用于优化内存分配，甚至质疑缓冲区是否根本存在。**AccessCountSet** 提供一组计数值，表示一个实现针对特定 **ExecutableEntity** 的某个 **AbstractAccessPoint** 调用 **RTE** / **SchM** API 的频率。在隐式通信数据访问的情况下，**RTE API** 可以返回对内存中可访问数据位置的数据引用。对于那种 **AbstractAccessPoint**，仅统计 API 调用次数是不够的，而通过数据引用对复合数据元素实现的访问次数才是重要的。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，显式通信，单次访问**：如果相应 **RunnableEntity** 的实现在任何条件下每次执行该 **RunnableEntity** 最多调用一次相应 **RTE API**，则应用于角色 **dataReceivePointByArgument**、**dataReceivePointByValue**、**dataSendPoint** 中的 **VariableAccess**，或应用于引用 **explicitInterRunnableVariable** 的角色 **writtenLocalVariable** / **readLocalVariable** 中的 **VariableAccess** 的 **AccessCount.value** 应给定为 **1**。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，显式通信，多次访问**：如果相应 **RunnableEntity** 的实现每次执行该 **RunnableEntity** 可能多次调用相应 **RTE API**，则应用于角色 **dataReceivePointByArgument**、**dataReceivePointByValue**、**dataSendPoint** 中的 **VariableAccess**，或应用于引用 **explicitInterRunnableVariable** 的角色 **writtenLocalVariable** / **readLocalVariable** 中的 **VariableAccess** 的 **AccessCount.value** 应给定为大于 **1**。因此，**AccessCount.value** 应说明典型执行条件下的调用次数。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，隐式通信和参数访问，单次访问**：如果相应 **ExecutableEntity** 的实现在任何条件下每次执行该 **RunnableEntity** 最多访问一次一个基本数据或最多一次一个基本复合数据元素，则应用于 **ParameterAccess** 或角色 **dataWriteAccess**、**dataReadAccess** 中的 **VariableAccess**，或应用于引用 **implicitInterRunnableVariable** 的角色 **writtenLocalVariable** 或 **readLocalVariable** 中的 **VariableAccess** 的 **AccessCount.value** 应给定为 **1**。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，隐式通信和参数访问，多次访问**：如果相应 **RunnableEntity** 的实现每次执行该 **RunnableEntity** 可能多次访问基本数据或多个基本复合数据元素，则应用于 **ParameterAccess** 或角色 **dataWriteAccess**、**dataReadAccess** 中的 **VariableAccess**，或应用于引用 **implicitInterRunnableVariable** 的角色 **writtenLocalVariable** 或 **readLocalVariable** 中的 **VariableAccess** 的 **AccessCount.value** 应给定为大于 **1**。因此，**AccessCount.value** 应说明典型执行条件下对基本数据的访问次数或对基本复合数据元素的访问次数。

例如，在一个执行 5 次的循环中访问一个由 3 个类型为 **uint8**、**uint16** 和 **uint64** 的元素组成的结构体，计为 **15**。

例如，一个 **RunnableEntity** 以如下方式访问大小为 42 的数组：每次执行该 **RunnableEntity** 恰好通过隐式访问读取该数组的一个元素。这计为 **1**。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，服务器调用、发出的触发器、模式切换通知，单次访问**：如果相应 **ExecutableEntity** 的实现在任何条件下每次执行该 **ExecutableEntity** 最多调用一次相应 **RTE API**，则应用于 **ServerCallPoint**、**AsynchronousServerCallResultPoint**、**InternalTriggeringPoint**、**ExternalTriggeringPoint**、**ModeSwitchPoint**、**ModeAccessPoint** 的 **AccessCount.value** 应给定为 **1**。

**countProfile DISTINGUISH_SINGULAR_ACCESSES，服务器调用、发出的触发器、模式切换通知，多次访问**：如果相应 **ExecutableEntity** 的实现每次执行该 **ExecutableEntity** 可能多次调用相应 **RTE API**，则应用于 **ServerCallPoint**、**AsynchronousServerCallResultPoint**、**InternalTriggeringPoint**、**ExternalTriggeringPoint**、**ModeSwitchPoint**、**ModeAccessPoint** 的 **AccessCount.value** 应给定为大于 **1**。因此，**AccessCount.value** 应说明典型执行条件下的调用次数。

例如，如果在一个循环中调用服务器，则 **AccessCount.value** 设置为典型的循环迭代次数。

#### 4.7.4. AccessCountSets 的结构

一般而言，**AccessCountSet** 如何用于构建 M1 模型的详细用法并未标准化。尽管如此，本节提供一些提示，说明如何将其应用于不同用例。无论 **AccessCountSet** 的详细子结构如何，有效的 AUTOSAR 模型对于特定 **AbstractAccessPoint** 根据特定 **countProfile** 最多只能提供一个值。否则计数值将是不明确的，因为对于一种访问会陈述多个值。

**AccessCount.value 需要明确**：**AUTOSAR** 模型对于每个 **countProfile** 针对特定 **AbstractAccessPoint** 最多应定义一个 **AccessCount.value**。

**根据 ExecutableEntity 结构化**：元类 **AccessCountSet** 应用于对某个特定 **ExecutableEntity** 的 **AccessCount.value** 进行分组。

**根据变体结构化**：元类 **AccessCountSet** 应用于对适用于软件的某个特定变体的 **AccessCount.value** 进行分组。如果 **AccessCount.value** 是通过代码解析评估的，则可以使用这种分组，因为解析可能针对 C 实现的特定变体进行。

**根据不同 countProfile 定义结构化**：元类 **AccessCountSet** 应用于对适用于某个特定 **countProfile** 值的 **AccessCount.value** 进行分组。


## 5. BSW 行为

### 5.1. BSW 行为概述

图 5.1 及下面的类表展示了类 **BswInternalBehavior** 的属性和描述。由于该层次的若干属性对于 BSW 模块和 SWC 是相同的，它们由抽象类 **InternalBehavior** 聚合，该类显示在同一图中以及单独的类表中。

以下各小节给出了各种属性的更详细解释。

表 5.1：InternalBehavior（**InternalBehavior**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | — | — | — | 软件组件和基本软件模块/集群的内部行为的公共基类（抽象）。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | BswInternalBehavior, SwcInternalBehavior |
| Aggregated by | — | — | — | AtpClassifier.atpFeature |
| constantMemory | ParameterDataPrototype | * | aggr | 描述一个只读存储器对象，包含由本 **InternalBehavior** 实现的特征值。该对象的 **shortName** 必须等于所描述常量的 'C' 标识符。特征值可以在同一 **SwComponentType** 的 **SwComponentPrototype** 之间共享。**constantMemory** 的聚合受可变性约束，目的是支持软件组件或模块实现中的可变性。通常实现中的不同算法需要不同数量的存储器对象。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=constantMemory.shortName, constantMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| constantValueMapping | ConstantSpecificationMappingSet | * | ref | 指向要应用于特定 **InternalBehavior** 的 **ConstantSpecificationMapping** 的引用。构造型：atpSplitable 标签：atp.Splitkey=constantValueMapping |
| dataTypeMapping | DataTypeMappingSet | * | ref | 指向要应用于特定 **InternalBehavior** 的 **DataTypeMapping** 的引用。构造型：atpSplitable 标签：atp.Splitkey=dataTypeMapping |
| exclusiveArea | ExclusiveArea | * | aggr | 为本 **InternalBehavior** 指定一个 **ExclusiveArea**。该 **exclusiveArea** 是组件或模块本地的。**ExclusiveArea** 的聚合受可变性约束。注意：**ExclusiveArea** 的数量可能因 **RunnableEntity** 或 **BswModuleEntity** 的条件存在而变化。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=exclusiveArea.shortName, exclusiveArea.variationPoint.shortLabel |
| exclusiveAreaNestingOrder | ExclusiveAreaNestingOrder | * | aggr | 表示由 **InternalBehavior** 拥有的 **ExclusiveAreaNestingOrder** 集合。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=exclusiveAreaNestingOrder.shortName, exclusiveAreaNestingOrder.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| staticMemory | VariableDataPrototype | * | aggr | 描述一个可读写静态存储器对象，表示由本软件组件实现的测量变量。术语 "static" 用于表示 "非临时" 的含义，并不一定指定链接器封装。这种存储器仅在 **supportsMultipleInstantiation** 为 **FALSE** 时受支持。**VariableDataPrototype** 的 **shortName** 必须等于所描述变量的 'C' 标识符。**staticMemory** 的聚合受可变性约束，目的是支持软件组件实现中的可变性。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=staticMemory.shortName, staticMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |

表 5.2：BswInternalBehavior（**BswInternalBehavior**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定 BSW 模块或 BSW 集群关于 **BSW Scheduler** 可见的代码实体的行为。可以有多个不同的 **BswInternalBehavior** 引用同一个 **BswModuleDescription**。 |
| Base | — | — | — | ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, InternalBehavior, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, BswModuleDescription.internalBehavior |
| arTypedPerInstanceMemory | VariableDataPrototype | * | aggr | 定义一个 **AUTOSAR** 类型的存储块，需要为基本软件模块的每个实例提供。**arTypedPerInstanceMemory** 的聚合受可变性约束，目的是支持基本软件模块实现中的可变性。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=arTypedPerInstanceMemory.shortName, arTypedPerInstanceMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| bswPerInstanceMemoryPolicy | BswPerInstanceMemoryPolicy | * | aggr | 针对 **arTypedPerInstanceMemory** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=bswPerInstanceMemoryPolicy, bswPerInstanceMemoryPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| clientPolicy | BswClientPolicy | * | aggr | 针对 **requiredClientServerEntry** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=clientPolicy, clientPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| distinguishedPartition | BswDistinguishedPartition | * | aggr | 指示一个抽象的分区上下文，封闭的 **BswModuleEntity** 可在其中执行。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=distinguishedPartition.shortName, distinguishedPartition.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=60 |
| entity | BswModuleEntity | * | aggr | 描述其行为的代码实体。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=entity.shortName, entity.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=5 |
| event | BswEvent | * | aggr | 本模块行为所需的事件。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=event.shortName, event.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=10 |
| exclusiveAreaPolicy | BswExclusiveAreaPolicy | * | aggr | 针对本 **BswInternalBehavior** 中某个 **ExclusiveArea** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=exclusiveAreaPolicy, exclusiveAreaPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| includedDataTypeSet | IncludedDataTypeSet | * | aggr | **includedDataTypeSet** 由基本软件模块用于其实现。构造型：atpSplitable 标签：atp.Splitkey=includedDataTypeSet |
| includedModeDeclarationGroupSet | IncludedModeDeclarationGroupSet | * | aggr | 本聚合表示所包含的 **ModeDeclarationGroup**。构造型：atpSplitable 标签：atp.Splitkey=includedModeDeclarationGroupSet |
| internalTriggeringPoint | BswInternalTriggeringPoint | * | aggr | 一个内部触发点。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=internalTriggeringPoint.shortName, internalTriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=2 |
| internalTriggeringPointPolicy | BswInternalTriggeringPointPolicy | * | aggr | 针对本 **BswInternalBehavior** 中某个 **internalTriggeringPoint** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=internalTriggeringPointPolicy, internalTriggeringPointPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| modeReceiverPolicy | BswModeReceiverPolicy | * | aggr | 接收模式切换的实现策略。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=modeReceiverPolicy, modeReceiverPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=25 |
| modeSenderPolicy | BswModeSenderPolicy | * | aggr | 提供模式组的实现策略。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=modeSenderPolicy, modeSenderPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=20 |
| parameterPolicy | BswParameterPolicy | * | aggr | 针对本 **BswInternalBehavior** 中某个 **perInstanceParameter** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=parameterPolicy, parameterPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| perInstanceParameter | ParameterDataPrototype | * | aggr | 描述一个只读存储器对象，包含本 **BswInternalBehavior** 所需的特征值。角色名 **perInstanceParameter** 的选择类似于 **SwcInternalBehavior** 上下文中的类似角色。与 **constantMemory** 相比，该对象不是由模块代码本地分配的，而是由 **BSW Scheduler** 分配的，并且通过 **BSW Scheduler** API 从 BSW 模块访问。主要用例是支持校准数据的软件仿真。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=perInstanceParameter.shortName, perInstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| receptionPolicy | BswDataReceptionPolicy | * | aggr | 分区间和/或核间通信的数据接收策略。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=receptionPolicy, receptionPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=55 |
| releasedTriggerPolicy | BswReleasedTriggerPolicy | * | aggr | 针对 **releasedTrigger** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=releasedTriggerPolicy, releasedTriggerPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| schedulerNamePrefix | BswSchedulerNamePrefix | * | aggr | 可选定义一个或多个用于 **BswScheduler** 的前缀。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=schedulerNamePrefix.shortName, schedulerNamePrefix.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=50 |
| sendPolicy | BswDataSendPolicy | * | aggr | 针对 **providedData** 的策略。该策略选择 **Schedule Manager** API 生成的选项。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=sendPolicy, sendPolicy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| serviceDependency | BswServiceDependency | * | aggr | 定义针对特定项目的 **AUTOSAR** 服务的需求。该聚合受可变性约束，目的是支持 **ServiceNeeds** 的条件存在。该聚合是可拆分的，以支持 **ServiceNeeds** 可能在后续开发步骤中提供。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=serviceDependency.ident.shortName, serviceDependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=40 |
| triggerDirectImplementation | BswTriggerDirectImplementation | * | aggr | 指定一个通过 **OS** 调用直接实现的触发器。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=triggerDirectImplementation, triggerDirectImplementation.variationPoint.shortLabel vh.latestBindingTime=preCompileTime xml.sequenceOffset=15 |
| variationPointProxy | VariationPointProxy | * | aggr | C/C++ 实现中可变点的代理。构造型：atpSplitable 标签：atp.Splitkey=variationPointProxy.shortName |

### 5.2. BSW 模块实体

#### 5.2.1. 概述

图 5.2 及接下来的类表展示了 **BswModuleEntity**、其基类 **ExecutableEntity** 以及针对被调用、被调度和中断实体的特化的属性。这些属性主要是配置 **BSW Scheduler** 所需的。

理解 **BswModuleEntity** 与 **BswModuleEntry** 之间的区别很重要：前者描述代码片段的属性，而后者仅描述用于调用代码片段的接口（即签名）。

**BSW 中的可执行实体**：抽象元类 **ExecutableEntity** 并非基本软件特有，它是从元模型的 **CommonStructure** 包导入的，定义如下：

表 5.3：ExecutableEntity（**ExecutableEntity**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | — | — | — | 可执行代码的抽象。 |
| Base | — | — | — | ARObject, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | BswModuleEntity, RunnableEntity |
| activationReason | ExecutableEntityActivationReason | * | aggr | 如果 **ExecutableEntity** 提供至少一个 **activationReason** 元素，则 **RTE** 或 **BSW Scheduler** 应提供读取该可执行实体执行的激活向量的手段。如果未提供 **activationReason** 元素，则对该 **ExecutableEntity** 禁用确定激活 **RTEEvent** 的功能。 |
| canEnter | ExclusiveArea | * | ref | 表示可执行实体可以通过显式 API 调用进入/离开所引用的排他区。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=canEnter.exclusiveArea, canEnter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| exclusiveAreaNestingOrder | ExclusiveAreaNestingOrder | * | ref | 表示本 **ExecutableEntity** 识别的 **ExclusiveAreaNestingOrder** 集合。 |
| minimumStartInterval | TimeValue | 0..1 | attr | 以秒为单位指定两次连续启动 **ExecutableEntity** 之间保证间隔的时间。 |
| reentrancyLevel | ReentrancyLevelEnum | 0..1 | attr | 本 **ExecutableEntity** 的重入级别。详情见枚举类型 **ReentrancyLevelEnum** 的文档。请注意，非重入接口也可以有重入或多核重入实现，重入接口也可以有多核重入实现。 |
| runsInside | ExclusiveArea | * | ref | 可执行实体完全在所引用的排他区内运行。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=runsInside.exclusiveArea, runsInside.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| swAddrMethod | SwAddrMethod | 0..1 | ref | 与本代码实体相关的寻址方法。通过与同一 **SwAddrMethod** 的关联，可以指定多个代码实体（即使来自不同模块或组件）应位于同一存储器中，而无需指定存储器段本身。 |

表 5.4：BswModuleEntity（**BswModuleEntity**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定在 AUTOSAR 中可为 BSW 模块或集群描述的最小代码片段。 |
| Base | — | — | — | ARObject, ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | BswCalledEntity, BswInterruptEntity, BswSchedulableEntity |
| Aggregated by | — | — | — | BswInternalBehavior.entity |


表 5.5：BswModuleEntity 属性（续）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| accessedModeGroup | ModeDeclarationGroupPrototype | * | ref | 本实体通过 API 调用访问的模式组。它应是本模块或集群要求的 **ModeDeclarationGroupPrototype**。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=accessedModeGroup.modeDeclarationGroupPrototype, accessedModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| activationPoint | BswInternalTriggeringPoint | * | ref | 模块实体用于激活一个或多个内部触发器的激活点。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=activationPoint.bswInternalTriggeringPoint, activationPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| callPoint | BswModuleCallPoint | * | aggr | 本实体代码中使用的调用点。该关联的可变性特别针对调试场景：可以有一个变体调用 **AUTOSAR** 调试模块，而另一个变体不调用。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=callPoint.shortName, callPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| dataReceivePoint | BswVariableAccess | * | aggr | 数据通过 **BSW Scheduler** 接收。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=dataReceivePoint.shortName, dataReceivePoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| dataSendPoint | BswVariableAccess | * | aggr | 数据通过 **BSW Scheduler** 发送。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=dataSendPoint.shortName, dataSendPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| implementedEntry | BswModuleEntry | 0..1 | ref | 由本模块实体实现的 entry。 |
| issuedTrigger | Trigger | * | ref | 本实体通过 **BSW Scheduler** API 调用发出的触发器。它应是由本模块或集群释放（即拥有）的 **BswTrigger**。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=issuedTrigger.trigger, issuedTrigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| managedModeGroup | ModeDeclarationGroupPrototype | * | ref | 由本实体管理的模式组。它应是本模块或集群提供的 **ModeDeclarationGroupPrototype**。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=managedModeGroup.modeDeclarationGroupPrototype, managedModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| schedulerNamePrefix | BswSchedulerNamePrefix | 0..1 | ref | 在本 **BswModuleEntity** 上下文中用于 **BswModuleScheduler** 生成名称（例如入口点原型、处理排他区的宏、头文件名称）的前缀。细节在 SWS RTE 中定义。该前缀取代这些名称前缀的默认规则。 |

**BswModuleEntity.implementedEntry 角色中引用的存在性**：对于每个 **BswModuleEntity**，在 BSW 模块配置完成时角色 **implementedEntry** 中的引用必须存在。

#### 5.2.2. BSW 模块实体属性

**用于模式和触发器交换的 BswModuleEntity 属性**：属性 **BswModuleEntity.managedModeGroup**、**BswModuleEntity.accessedModeGroup** 和 **BswModuleEntity.issuedTrigger** 指定本 **BswModuleEntity** 通过使用 **BSW Scheduler** API 发起或接收其他模块的模式切换或激活触发器。这是配置 **BSW Scheduler** 的必备信息。

关于属性 **callPoint** 的说明见第 5.3 章。

关于属性 **dataSendPoint** 和 **dataReceivePoint** 的说明见第 5.4 章。

**BswModuleEntity 重入级别**：通过可选属性 **reentrancyLevel**，**BswModuleEntity** 可以在其接口给定的范围内（见约束）声明其实现的重入级别。该属性特别针对多核场景。

如果省略该属性，则假定重入按属性 **BswModuleEntity.implementedEntry.isReentrant** 的定义实现，此时 **true** 表示单核重入。

表 5.6：ReentrancyLevelEnum（**ReentrancyLevelEnum**）

| 枚举 | ReentrancyLevelEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | 指定实体是否以及在何种环境中是重入的。 |
| Aggregated by | ExecutableEntity.reentrancyLevel |
| 字面值 | 说明 |
| multicoreReentrant | 本实体可以无限制地并发执行，包括在多核系统上的抢占和并行执行。标签：atp.EnumerationLiteralIndex=0 |
| nonReentrant | 本实体不可能并发执行。标签：atp.EnumerationLiteralIndex=1 |
| singleCoreReentrant | 在单核系统上本实体可以伪并发执行（即抢占）。标签：atp.EnumerationLiteralIndex=2 |

#### 5.2.3. BswModuleEntity 约束

实际实现的重入级别只能比接口级别声明的 "更好"，如下约束所述：

**BswModuleEntity.reentrancyLevel 的约束**：

* 如果由 **BswModuleEntity** 在角色 **implementedEntry** 中引用的 **BswModuleEntry** 的属性 **isReentrant** 值为 **true**，则同一 **BswModuleEntity** 的属性 **reentrancyLevel**（如果存在）只能取值 **singleCoreReentrant** 或 **multicoreReentrant**。
* 如果由 **BswModuleEntity** 在角色 **implementedEntry** 中引用的 **BswModuleEntry** 的属性 **isReentrant** 值为 **false**，则同一 **BswModuleEntity** 的属性 **reentrancyLevel**（如果存在）的取值没有限制。

**BswModuleEntity 仅使用模块的接口**：一个 **BswModuleEntity** 只能实现/使用已在相应模块或集群接口层声明的元素，换言之：

* **BswModuleEntity.implementedEntry** 应引用一个声明为封闭 **BswModuleDescription** 的 **implementedEntry** 的元素；
* **BswModuleEntity.callPoint.calledEntry**（其中 **callPoint** 实例化自 **BswDirectCallPoint**）应引用一个声明为封闭 **BswModuleDescription** 的 **expectedEntry** 或 **implementedEntry** 的元素；
* **BswModuleEntity.callPoint.calledEntry**（其中 **callPoint** 实例化自 **BswSynchronousServerCallPoint** 或 **BswAsynchronousServerCallPoint**）应引用一个声明为封闭 **BswModuleDescription** 的 **requiredClientServerEntry** 的元素；
* **BswModuleEntity.callPoint**（其中 **callPoint** 实例化自 **BswAsynchronousServerCallResultPoint**）应引用一个同样声明为同一 **BswModuleEntity** 的 **callPoint** 的 **BswAsynchronousServerCallPoint**；
* **BswModuleEntity.issuedTrigger** 应引用一个声明为封闭 **BswModuleDescription** 的 **releasedTrigger** 的元素；
* **BswModuleEntity.managedModeGroup** 应引用一个声明为封闭 **BswModuleDescription** 的 **providedModeGroup** 的元素；
* **BswModuleEntity.accessedModeGroup** 应引用一个声明为封闭 **BswModuleDescription** 的 **requiredModeGroup** 的元素；
* **BswModuleEntity.dataSendPoint.accessedVariable** 应引用一个声明为封闭 **BswModuleDescription** 的 **providedData** 的元素；
* **BswModuleEntity.dataReceivePoint.accessedVariable** 应引用一个声明为封闭 **BswModuleDescription** 的 **requiredData** 的元素；
* 应允许 **accessedModeGroup** 引用一个声明为 **providedModeGroup** 的元素。

#### 5.2.4. BswCalledEntity

表 5.7：BswCalledEntity（**BswCalledEntity**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 设计为从另一个 BSW 模块或集群调用的 BSW 模块实体。 |
| Base | — | — | — | ARObject, BswModuleEntity, ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.entity |

**BswCalledEntity** 表示一种 "普通" 函数调用，适用以下约束：

**BswCalledEntity 约束**：

* **BswCalledEntity.implementedEntry.callType** 应为 'regular' 或 'callback'；
* **BswCalledEntity.implementedEntry.executionContext** 一般不受限制，但关于 ClientServer 通信服务器侧的约束见其他规则；
* **BswInterruptEvent** 只应触发属性 **interruptCategory** 设置为 **BswInterruptCategory.cat2** 的 **BswInterruptEntity**。

#### 5.2.5. BswSchedulableEntity

表 5.8：BswSchedulableEntity（**BswSchedulableEntity**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 设计为由 **BSW Scheduler** 控制的 BSW 模块实体。例如，它可以实现所谓的 "main" 函数。 |
| Base | — | — | — | ARObject, BswModuleEntity, ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.entity |

**BswSchedulableEntity** 表示一种被调度的函数调用，适用以下约束：

**BswSchedulableEntity 约束**：

* **BswModuleEntity.implementedEntry.callType** 应为 'scheduled'；
* **BswModuleEntity.implementedEntry.executionContext** 应为 'task'。

#### 5.2.6. BswInterruptEntity

表 5.9：BswInterruptEntity（**BswInterruptEntity**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 设计为由中断触发的 BSW 模块实体。 |
| Base | — | — | — | ARObject, BswModuleEntity, ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.entity |
| interruptCategory | BswInterruptCategory | 0..1 | attr | 中断的类别。 |
| interruptSource | String | 0..1 | attr | 允许对预期中断源进行文本描述。 |

**BswInterruptEntity.interruptCategory 属性的存在性**：对于每个 **BswInterruptEntity**，在 BSW 模块配置完成时属性 **interruptCategory** 必须存在。

**BswInterruptEntity.interruptSource 属性的存在性**：对于每个 **BswInterruptEntity**，在 BSW 模块配置完成时属性 **interruptSource** 必须存在。


表 5.10：BswInterruptCategory（**BswInterruptCategory**）

| 枚举 | BswInterruptCategory |
| --- | --- |
| Package | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | 中断服务的类别。 |
| Aggregated by | BswInterruptEntity.interruptCategory |
| 字面值 | 说明 |
| cat1 | Cat1 中断例程不受 **OS** 控制，只允许进行非常有限的选择性 **OS** 调用以启用和禁用所有中断。**BswInterruptEntity** 由中断服务例程实现，该例程直接从中断向量调用（不经过 **OS**）。标签：atp.EnumerationLiteralIndex=0 |
| cat2 | Cat2 中断例程受 **OS** 控制，允许进行 **OS** 调用。**BswInterruptEntity** 由从 **OS** 调用的中断处理程序实现。标签：atp.EnumerationLiteralIndex=1 |

**BswInterruptEntity** 表示一种中断例程，适用以下约束：

**BswInterruptEntity 约束**：

* **BswInterruptEntity.implementedEntry.callType** 应为 'interrupt'；
* 当且仅当 **BswInterruptEntity.interruptCategory** 为 'Cat1' 时，**BswInterruptEntity.implementedEntry.executionContext** 应为 'interruptCat1'；
* 当且仅当 **BswInterruptEntity.interruptCategory** 为 'Cat2' 时，**BswInterruptEntity.implementedEntry.executionContext** 应为 'interruptCat2'。

### 5.3. BSW 模块调用点

#### 5.3.1. 概述

通过聚合 **BswModuleCallPoint**，**BswModuleEntity** 定义它如何使用 **BswModuleEntry** 来调用其他（或同一）BSW 模块。

表 5.11：BswModuleCallPoint（**BswModuleCallPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示 **BswModuleEntity** 处理对 **BswModuleEntry** 的过程调用的点，可以直接调用，也可以通过 **BSW Scheduler** 调用。 |
| Base | — | — | — | ARObject, Referrable |
| Subclasses | — | — | — | BswAsynchronousServerCallPoint, BswAsynchronousServerCallResultPoint, BswDirectCallPoint, BswSynchronousServerCallPoint |
| Aggregated by | — | — | — | BswModuleEntity.callPoint |
| contextLimitation | BswDistinguishedPartition | * | ref | 该引用的存在表示调用点仅在所引用的 **BswDistinguishedPartition** 的上下文中使用。 |

#### 5.3.2. 直接调用点

**BswDirectCallPoint 的使用**：在 **BswModuleEntity** 中作为 **callPoint** 聚合的元类 **BswDirectCallPoint** 允许声明给定 **BswModuleEntity** 的代码中直接调用（即不通过 **BSW Scheduler**）其他模块（或同一模块）的哪个 entry。

表 5.12：BswDirectCallPoint（**BswDirectCallPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示代码中直接（即不通过 **BSW Scheduler**）调用 **BswModuleEntry** 的具体点。该信息可用于分析调用树和资源锁定场景。配置 **BSW Scheduler** 不需要该信息。 |
| Base | — | — | — | ARObject, BswModuleCallPoint, Referrable |
| Aggregated by | — | — | — | BswModuleEntity.callPoint |
| calledEntry | BswModuleEntry | 0..1 | ref | 在此点调用的 **BswModuleEntry**。 |
| calledFromWithinExclusiveArea | ExclusiveAreaNestingOrder | 0..1 | ref | 表示调用点位于按给定顺序嵌套的一个或多个 **ExclusiveArea** 内最深的层次。 |

**BswDirectCallPoint.calledEntry 角色中引用的存在性**：对于每个 **BswDirectCallPoint**，在 BSW 模块配置完成时角色 **calledEntry** 中的引用必须存在。

请注意，这对于能够集成模块并不是强制信息，但如果集成者想要分析多个模块之间的调用链以设置适当的调度，则该信息非常重要。还需要注意的是，与 **BswModuleDescription.bswModuleDependency** 相比，该属性包含额外信息，因为后者仅表示模块接口之间的依赖关系，而 **calledEntry** 显示实际从哪个代码片段调用。

此外，**BswDirectCallPoint** 包含有关资源锁定的信息，见第 5.5 节。

当然，在直接调用期间执行上下文（如 task、interrupt 等）会保留：

**直接调用的 calledEntry 约束**：如果 **callPoint** 作为 **BswDirectCallPoint** 的实例聚合，则适用以下规则：

* **BswModuleEntity.callPoint.calledEntry.executionContext** 应与 **BswModuleEntity.implementedEntry.executionContext** 相同；
* **BswModuleEntity.callPoint.calledEntry.callType** 应取值 'regular' 或 'callback'。

#### 5.3.3. Client-Server 调用点

**BswSynchronousServerCallPoint 的使用**：在 **BswModuleEntity** 中作为 **callPoint** 聚合的元类 **BswSynchronousServerCallPoint** 允许声明在客户端 **BswModuleEntity** 的代码中通过 **BSW Scheduler** 同步调用其他模块（或同一模块）的哪个 entry。

预期用例是分区间或核间通信。请注意，对于给定 **BswInternalBehavior**，有两个最终运行在不同分区和/或处理器核上的不同 **BswModuleEntity** 是有效用例。

表 5.13：BswSynchronousServerCallPoint（**BswSynchronousServerCallPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示通过 **BSW Scheduler** 的同步过程调用点。 |
| Base | — | — | — | ARObject, BswModuleCallPoint, Referrable |
| Aggregated by | — | — | — | BswModuleEntity.callPoint |
| calledEntry | BswModuleClientServerEntry | 0..1 | ref | 要调用的 entry。 |
| calledFromWithinExclusiveArea | ExclusiveAreaNestingOrder | 0..1 | ref | 表示调用点位于按给定顺序嵌套的一个或多个 **ExclusiveArea** 内最深的层次。 |

**BswSynchronousServerCallPoint.calledEntry 角色中引用的存在性**：对于每个 **BswSynchronousServerCallPoint**，在 BSW 模块配置完成时角色 **calledEntry** 中的引用必须存在。

与 **BswDirectCallPoint** 一样，**BswSynchronousServerCallPoint** 也包含有关资源锁定的信息，见第 5.5 节。

**BswAsynchronousServerCallPoint 的使用**：在 **BswModuleEntity** 中作为 **callPoint** 聚合的元类 **BswAsynchronousServerCallPoint** 允许声明在客户端 **BswModuleEntity** 的代码中通过 **BSW Scheduler** 异步调用其他模块（或同一模块）的哪个 entry。

预期用例是分区间或核间通信。请注意，对于给定 **BswInternalBehavior**，有两个最终运行在不同分区和/或处理器核上的不同 **BswModuleEntity** 是有效用例。

> 1 这并不排除在 **contextLimitation** 定义的范围内客户端和服务器在同一分区中执行的配置。

表 5.14：BswAsynchronousServerCallPoint（**BswAsynchronousServerCallPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示通过 **BSW Scheduler** 的异步过程调用点。 |
| Base | — | — | — | ARObject, BswModuleCallPoint, Referrable |
| Aggregated by | — | — | — | BswModuleEntity.callPoint |
| calledEntry | BswModuleClientServerEntry | 0..1 | ref | 要调用的 entry。 |

**BswAsynchronousServerCallPoint.calledEntry 角色中引用的存在性**：对于每个 **BswAsynchronousServerCallPoint**，在 BSW 模块配置完成时角色 **calledEntry** 中的引用必须存在。

**BswAsynchronousServerCallResultPoint 的使用**：在 **BswModuleEntity** 中作为 **callPoint** 聚合的元类 **BswAsynchronousServerCallResultPoint** 表示客户端 **BswModuleEntity** 有可能检索通过关联的 **BswAsynchronousServerCallPoint** 先前完成的异步调用的结果（返回值和参数）。

表 5.15：BswAsynchronousServerCallResultPoint（**BswAsynchronousServerCallResultPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | **BswAsynchronousServerCallPoint** 的回调点，即可以从 **BSW Scheduler** 检索结果的点。 |
| Base | — | — | — | ARObject, BswModuleCallPoint, Referrable |
| Aggregated by | — | — | — | BswModuleEntity.callPoint |
| asynchronousServerCallPoint | BswAsynchronousServerCallPoint | 0..1 | ref | 调用该结果所属调用的调用点。 |

**BswAsynchronousServerCallResultPoint.asynchronousServerCallPoint 角色中引用的存在性**：对于每个 **BswAsynchronousServerCallResultPoint**，在 BSW 模块配置完成时角色 **asynchronousServerCallPoint** 中的引用必须存在。

请注意，检索此类结果的 **BswModuleEntity** 可以以不同方式调度：它可以通过 **BswAsynchronousServerCallReturnsEvent** 和/或其他类型的 **BswEvent** 启动。

**client-server 调用的 calledEntry 约束**：

* 在 **BswSynchronousServerCallPoint** 中作为 **calledEntry** 聚合的 **BswModuleClientServerEntry** 应具有属性 **isSynchronous = true**；
* 在 **BswAsynchronousServerCallPoint** 中作为 **calledEntry** 聚合的 **BswModuleClientServerEntry** 应具有属性 **isSynchronous = false**。


### 5.4. BSW Sender-Receiver 数据访问

通过聚合元类 **BswVariableAccess**，**BswModuleEntity** 定义它如何访问数据以与另一个（或同一）BSW 模块进行（潜在的）分区间通信。

表 5.16：BswVariableAccess（**BswVariableAccess**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | **BswVariableAccess** 的存在意味着 **BswModuleEntity** 需要通过 **BSW Scheduler** 访问 **VariableDataPrototype**。访问的种类由使用该类的角色指定。 |
| Base | — | — | — | ARObject, Referrable |
| Aggregated by | — | — | — | BswModuleEntity.dataReceivePoint, BswModuleEntity.dataSendPoint |
| accessedVariable | VariableDataPrototype | 0..1 | ref | 通过 **BSW Scheduler** 访问的数据。 |
| contextLimitation | BswDistinguishedPartition | * | ref | 该引用的存在表示该变量仅在所引用的 **BswDistinguishedPartition** 的上下文中接收或发送。 |

**BswVariableAccess.accessedVariable 角色中引用的存在性**：对于每个 **BswVariableAccess**，在 BSW 模块配置完成时角色 **accessedVariable** 中的引用必须存在。

**用于 sender-receiver 数据交换的 BswModuleEntity 属性**：属性 **BswModuleEntity.dataSendPoint** 和 **BswModuleEntity.dataReceivePoint** 指定本 **BswModuleEntity** 可以访问 **BSW Scheduler** 以发送或接收所引用的 **VariableDataPrototype** 中声明的数据。这针对分区间和/或多核通信场景。

### 5.5. BSW 排他区

**BSW 中的排他区**：元类 **ExclusiveArea**（包括来自 **ExecutableEntity** 的关联）并非基本软件特有，它是从元模型的 **CommonStructure** 包导入的，定义如下：

表 5.17：ExclusiveArea（**ExclusiveArea**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | — | — | — | 防止在该区域内运行的可执行实体被抢占。 |
| Base | — | — | — | ARObject, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | InternalBehavior.exclusiveArea |

对于 **ExclusiveArea** 机制的某些实现，如果每个 **BswModuleEntity** 使用不同的进入和退出 API 集合是有利的。这组不同的 API 支持这样的 **ExclusiveArea** 实现：对于最高优先级的 **RunnableEntity** 省略锁。当最高优先级的 **BswModuleEntity** 在任何情况下都不会被以较低优先级调度的 **BswModuleEntity** 中断时，这是可能的。为了支持这种实现，软件组件描述必须声明它请求每个以 **canEnterExclusiveArea** 方式访问 **ExclusiveArea** 的 **BswModuleEntity** 单独的 API。

表 5.18：BswExclusiveAreaPolicy（**BswExclusiveAreaPolicy**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 使用本策略的 **BSW Scheduler** 所对应的 **ExclusiveArea**。 |
| Base | — | — | — | ARObject, BswApiOptions |
| Aggregated by | — | — | — | BswInternalBehavior.exclusiveAreaPolicy |
| apiPrinciple | ApiPrincipleEnum | 0..1 | attr | 为本 **ExclusiveArea** 指定：是向 **SchM** 请求整个 BSW 模块共用的单一进入和退出 API 集合，还是期望每个 **BswModuleEntity** 各有一套进入和退出 API。默认值为 "common"。 |
| exclusiveArea | ExclusiveArea | 0..1 | ref | 使用本策略的 **BSW Scheduler** 所对应的 **ExclusiveArea**。 |

**BswExclusiveAreaPolicy.exclusiveArea 角色中引用的存在性**：对于每个 **BswExclusiveAreaPolicy**，在 BSW 模块配置完成时角色 **exclusiveArea** 中的引用必须存在。

表 5.19：ApiPrincipleEnum（**ApiPrincipleEnum**）

| 枚举 | ApiPrincipleEnum |
| --- | --- |
| Package | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | 本枚举表示控制 API 生成粒度的能力。 |
| Aggregated by | BswExclusiveAreaPolicy.apiPrinciple, SwcExclusiveAreaPolicy.apiPrinciple |
| 字面值 | 说明 |
| common | **Rte** 或 **SchM** API 为整个软件组件/BSW 模块提供。标签：atp.EnumerationLiteralIndex=0 |
| perExecutable | **Rte** 或 **SchM** API 为软件组件/BSW 模块的特定 **ExecutableEntity** 提供。标签：atp.EnumerationLiteralIndex=1 |

**通过公共 API 集合进入和退出 ExclusiveArea**：如果 **BswExclusiveAreaPolicy.apiPrinciple** 设置为 "common"，则 **SchM** 为整个 BSW 模块提供一套进入和退出 API。

在这种情况下，所有受影响的 **BswModuleEntity** 执行相同的进入和退出代码，无法对在最高优先上下文中执行的 **BswModuleEntity** 进行特殊处理。

**通过单独 API 集合进入和退出 ExclusiveArea**：如果 **BswExclusiveAreaPolicy.apiPrinciple** 设置为 "perExecutable"，则 **SchM** 为每个受影响的 **BswModuleEntity** 提供单独的进入和退出 API 集合。

在这种情况下，在最高优先上下文中执行的 **BswModuleEntity** 的进入和退出代码可以留空。

为了避免对一个 **ExclusiveArea** 的 **BswExclusiveAreaPolicy** 设置相互矛盾，适用相关约束。

**BswExclusiveAreaPolicy 数量的限制**：一个 **ExclusiveArea** 最多只能被一个 **BswExclusiveAreaPolicy** 引用。

图 5.5 展示了 BSW 中排他区的详细元模型。

除了定义 **BswModuleEntity** 可以进入排他区或完全在排他区中运行之外，还可以定义排他区的可能嵌套顺序。此外，可以定义在嵌套顺序的哪个层次上从 **BswModuleEntity** 调用函数。嵌套顺序的信息可用于分析关于资源锁定场景的调用树。

表 5.20：ExclusiveAreaNestingOrder（**ExclusiveAreaNestingOrder**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::InternalBehavior |
| Note | — | — | — | 本元类表示定义 **ExclusiveArea** 嵌套顺序的能力。正式定义一种（可能出现在可执行代码中的）嵌套顺序，以便分析资源锁定行为。 |
| Base | — | — | — | ARObject, Referrable |
| Aggregated by | — | — | — | InternalBehavior.exclusiveAreaNestingOrder |
| exclusiveArea (ordered) | ExclusiveArea | * | ref | 表示在嵌套顺序方面如何使用排他区的具体场景。 |

**ExclusiveAreaNestingOrder**：可选的 **ExclusiveAreaNestingOrder**（如果使用）应描述 **BswModuleEntity** 中可能出现的嵌套顺序（包括单个 **ExclusiveArea**）。每种可能的锁定情况都需要自己的 **ExclusiveAreaNestingOrder**。

**指示 BswModuleEntity 的锁定行为已被完整描述**：在 **InternalBehavior** 中配置的所有 **ExclusiveArea** 都应被某个 **ExclusiveAreaNestingOrder** 引用，以指示相应 **BswModuleEntity** 的锁定行为已被完整描述。

**未描述 BswModuleEntity 的锁定行为**：如果 **ExclusiveArea** 未被任何 **ExclusiveAreaNestingOrder** 引用（这是默认情况），这意味着未描述相应 **BswModuleEntity** 的锁定行为，并且所提供的信息可能不完整，不能用于锁定行为的全局离线分析。

**BswModuleCallPoint 与 ExclusiveAreaNestingOrder 的关系**：如果从 **BswModuleEntity** 内部调用其他 **BswModuleEntity**，则 **ExclusiveAreaNestingOrder** 可以被一个或多个 **BswModuleCallPoint** 引用，以指定被调用函数关于 **ExclusiveArea** 的调用环境。

### 5.6. BSW Scheduler 名称前缀

**BswSchedulerNamePrefix 的使用**：基本软件调度器（**Basic Software Scheduler**）API 定义了若干生成的工件（宏代码和头文件名），其中包含所谓的模块前缀。默认情况下，该前缀从属性 **BswModuleDescription.shortName** 派生。

然而，为了允许对这些工件进行更细粒度的定义，可以在 **BswInternalBehavior** 中指定自己的前缀，并将其单独分配给每个 **BswSchedulableEntity**。这样的分配将取代由 **BswModuleDescription.shortName** 给出的前缀。如果所讨论的 BSWMD 表示多个其他模块的集群，这尤其有用。

请注意，此前缀不能用于修改模块接口中对其他模块可见的任何名称，即作为 **BswModuleEntry.shortName** 一部分的模块缩写不能被它取代。

图 5.6 及下面的类表展示了元类 **BswSchedulerNamePrefix** 如何放置在元模型中。关于 **RTE** 生成器如何使用此信息的细节，请参见 [10]。

表 5.21：BswSchedulerNamePrefix（**BswSchedulerNamePrefix**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 用于构成 BSW 模块对 **BswScheduler** 接口的生成代码工件名称的前缀。 |
| Base | — | — | — | ARObject, ImplementationProps, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.schedulerNamePrefix |

表 5.22：ImplementationProps（**ImplementationProps**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::Implementation |
| Note | — | — | — | 定义一个符号，根据具体情形，在生成代码工件时用作完整替代或前缀。 |
| Base | — | — | — | ARObject, Referrable |
| Subclasses | — | — | — | BswSchedulerNamePrefix, ExecutableEntityActivationReason, SectionNamePrefix, SymbolProps, SymbolicNameProps |
| symbol | CIdentifier | 0..1 | attr | 根据具体情形用作完整替代或前缀的符号。 |


### 5.7. BSW 事件

#### 5.7.1. 概述

**BswEvent 的使用**：抽象类 **BswEvent** 用作所有可以启动 **BswModuleEntity** 的事件种类的基类（这意味着它不包括对 **BSW Scheduler** 不可见的直接函数调用）。图 5.7 给出了这些事件及其与不同种类 **BswModuleEntity** 关联的概述。

表 5.23：BswEvent（**BswEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 用于触发本 BSW 模块或集群的 **BswModuleEntity** 的各种事件的基类。该事件是 BSW 模块或集群本地的。元类实例的短名称旨在作为配置 **BSW Scheduler** 所需 API 的输入。 |
| Base | — | — | — | ARObject, AbstractEvent, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | BswInterruptEvent, BswOperationInvokedEvent, BswScheduleEvent |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| contextLimitation | BswDistinguishedPartition | * | ref | 该引用的存在表示该事件的使用仅限于所引用的 **BswDistinguishedPartition** 的上下文。 |
| disabledInMode | ModeDeclaration | * | iref | 禁用该事件的模式。构造型：atpSplitable 标签：atp.Splitkey=disabledInMode.contextModeDeclarationGroup, disabledInMode.targetModeInstanceRef 实现者：ModeInBswModuleDescriptionInstanceRef |
| startsOnEvent | BswModuleEntity | 0..1 | ref | 由该事件启动的实体。 |

**BswEvent.startsOnEvent 角色中引用的存在性**：对于每个 **BswEvent**，在 BSW 模块配置完成时角色 **startsOnEvent** 中的引用必须存在。

表 5.24：BswScheduleEvent（**BswScheduleEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 能够启动 **BswSchedulableEntity** 的 **BswEvent**。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable |
| Subclasses | — | — | — | BswAsynchronousServerCallReturnsEvent, BswBackgroundEvent, BswDataReceivedEvent, BswExternalTriggerOccurredEvent, BswInternalTriggerOccurredEvent, BswModeManagerErrorEvent, BswModeSwitchEvent, BswModeSwitchedAckEvent, BswOsTaskExecutionEvent, BswTimingEvent |
| Aggregated by | — | — | — | BswInternalBehavior.event |

**startsOnEvent 引用对 BswScheduleEvent 的适用性**：引用 **BswScheduleEvent.startsOnEvent** 只能指向 **BswSchedulableEntity**。

**startsOnEvent 引用对 BswOperationInvokedEvent 的适用性**：引用 **BswOperationInvokedEvent.startsOnEvent** 只能指向 **BswCalledEntity**。

表 5.25：BswInterruptEvent（**BswInterruptEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 本元类表示由中断触发的事件。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |

#### 5.7.2. 定时与后台事件

**BSW 的定时与后台事件**：**BswTimingEvent** 和 **BswBackgroundEvent** 由调度器或 **OS** 直接驱动，无需外部源。

表 5.26：BswTimingEvent（**BswTimingEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 由时间段驱动的周期性 **BswEvent**。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| period | TimeValue | 0..1 | attr | 触发该事件的时间段（以秒为单位）的要求。 |

**BswTimingEvent.period 属性的存在性**：对于每个 **BswTimingEvent**，在 BSW 模块配置完成时属性 **period** 必须存在。

**BswTimingEvent 的周期**：**BswTimingEvent.period** 应大于 0。

表 5.27：BswBackgroundEvent（**BswBackgroundEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 用于执行后台活动的周期性 **BswEvent**。它类似于 **BswTimingEvent**，但没有固定时间段，并且仅以低优先级激活。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |

表 5.28：BswOsTaskExecutionEvent（**BswOsTaskExecutionEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 本 **BswEvent** 用于执行必须对特定 **OsTask** 的执行作出反应的 **BswSchedulableEntity**。因此，只要映射到它的 **OsTask** 被执行，该事件就会无条件引发。该事件的主要用例是调度必须对任务执行作出反应的复杂驱动程序的 **Runnable**。标签：atp.Status=draft |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |

#### 5.7.3. 触发器事件

图 5.8 及下面的表格给出了由内部或外部触发器驱动的事件的更详细图景。

注意内部触发事件与定时事件在激活方式上的区别：

**BSW 的内部触发器与定时事件**：**BswModuleEntity** 可以借助由 **BSW Scheduler** 生成的 API 触发（同一模块的）**BswInternalTriggerOccurredEvent**，而 **BswTimingEvent** 由 **BswScheduler** 通过 **OS** 定时器触发。更多信息见 [10]。

**BSW 的外部触发事件**：**BswExternalTriggerOccurredEvent** 指定该事件是为响应另一个 BSW 模块发出的触发器而引发的事实。例如，这可用于在 BSW 模块之间直接传递 ECU 外部事件，如唤醒事件或曲轴事件。

**外部触发器应属于接口**：**BswExternalTriggerOccurredEvent** 应引用一个通过同一模块的 **BswModuleDescription.requiredTrigger** 声明的 **Trigger**。

表 5.29：BswInternalTriggeringPoint（**BswInternalTriggeringPoint**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示一个或多个 **BswInternalTriggerOccurredEvent** 的激活点。 |
| Base | — | — | — | ARObject, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.internalTriggeringPoint |
| swImplPolicy | SwImplPolicyEnum | 0..1 | attr | 当本属性设置为 **queued** 时，指定对内部触发事件的排队处理。 |

与外部触发器类似，**BswInternalTriggeringPoint** 可以设置一个属性来定义其排队行为：

**BswInternalTriggeringPoint.swImplPolicy 的允许值**：属性 **BswInternalTriggeringPoint.swImplPolicy** 唯一允许的值是 **STANDARD**（此时内部触发处理不使用队列）或 **QUEUED**（此时内部触发处理使用队列）。

表 5.30：BswInternalTriggerOccurredEvent（**BswInternalTriggerOccurredEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 一种可能零星发生的 **BswEvent**。该事件由模块对 **BSW Scheduler** 的显式调用激活。此类事件的主要目的是引起上下文切换，例如从 ISR 上下文切换到任务上下文。激活和切换仅在同一模块或集群内处理。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| eventSource | BswInternalTriggeringPoint | 0..1 | ref | 激活点是本事件的来源。 |

**BswInternalTriggerOccurredEvent.eventSource 角色中引用的存在性**：对于每个 **BswInternalTriggerOccurredEvent**，在 BSW 模块配置完成时角色 **eventSource** 中的引用必须存在。


表 5.31：BswExternalTriggerOccurredEvent（**BswExternalTriggerOccurredEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 由另一个模块或集群释放的触发器所产生的 **BswEvent**。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| trigger | Trigger | 0..1 | ref | 与本事件关联的触发器。该触发器对本模块是外部的。 |

**BswExternalTriggerOccurredEvent.trigger 角色中引用的存在性**：对于每个 **BswExternalTriggerOccurredEvent**，在 BSW 模块配置完成时角色 **trigger** 中的引用必须存在。

除了这些机制之外，外部事件还可以通过中断直接触发 **BswInterruptEntity**。这种情况不属于事件模型，因为它不通过 **BSW Scheduler** 处理，并且是 BSW 模块本地的。

#### 5.7.4. 模式事件

图 5.9 及下面的表格给出了与模式切换相关的事件和其他类的更详细图景。

模式切换可以通过不同机制影响 **BswEvent** 的激活：

**BSW 中的模式切换与事件**：

* 通过可选属性 **disabledInMode**，**BswEvent** 可以指定在某个特定模式下必须被抑制；
* 一种特殊的事件 **BswModeSwitchEvent** 可用于在特定模式的进入或退出时启动 **BswModuleEntity**；
* 在模式切换的发送侧（即管理模式组的模块中），**BswModeSwitchedAckEvent** 可用于在模式切换被 **BSW Scheduler** 确认后启动 **BswModuleEntity**；
* 在模式切换的发送侧（即管理模式组的模块中），**BswModeManagerErrorEvent** 可用于在宣布错误后启动 **BswModuleEntity**。该事件将在导致所涉及的某个分区终止的错误之后由 **BSW Scheduler** 抛出。这可能是管理模式切换的分区，也可能是使用它的分区。

所引用的 **ModeDeclaration** 和枚举 **ModeActivationKind** 都是从元模型的 **CommonStructure** 包导入的。

**BSW 模式切换事件的语义**：如果 **BswModeSwitchEvent.activation** 取值 **onTransition**，则 **BswModeSwitchEvent** 应引用属于同一 **ModeDeclarationGroup** 实例的两个不同模式，其顺序定义转换的方向。在所有其他情况下，**BswModeSwitchEvent** 应恰好引用一个模式。

**BswModeSwitchEvent 与 ModeTransition 的定义**：对于由 **BswModeSwitchEvent**（其属性 **activation** 设置为 **onTransition**）引用的每对 **ModeDeclaration**，应在相应方向上定义一个 **ModeTransition**（即从 **exitedMode** 到 **enteredMode**）。该约束仅当相应的 **ModeDeclarationGroup** 定义了至少一个 **modeTransition** 时才适用。

**BSW 模式切换事件使用的模式**：**BswModeSwitchEvent** 使用的 **ModeDeclaration** 应属于作为封闭 **BswInternalBehavior** 的 **BswInternalBehavior.entity.accessedModeGroup** 引用的 **ModeDeclarationGroupPrototype**。

**BSW 模式切换确认事件使用的模式组**：**BswModeSwitchedAckEvent** 使用的 **ModeDeclarationGroupPrototype** 应由同一模块引用为 **BswModuleDescription.providedModeGroup**。

**BSW 模式管理器错误事件使用的模式组**：**BswModeManagerErrorEvent** 使用的 **ModeDeclarationGroupPrototype** 应由同一模块引用为 **BswModuleDescription.providedModeGroup**。

表 5.32：BswModeSwitchEvent（**BswModeSwitchEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 由模式切换产生的 **BswEvent**。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| activation | ModeActivationKind | 0..1 | attr | 关于所引用模式的激活种类。 |
| mode (ordered) | ModeDeclaration | 0..2 | iref | 对引发模式切换事件的一个或两个模式的引用。InstanceRef 实现者：ModeInBswModuleDescriptionInstanceRef |

**BswModeSwitchEvent.activation 属性的存在性**：对于每个 **BswModeSwitchEvent**，在 BSW 模块配置完成时属性 **activation** 必须存在。

表 5.33：BswModeSwitchedAckEvent（**BswModeSwitchedAckEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 在所引用模式组的切换被确认或发生错误后引发该事件。所引用的模式组应由本模块提供。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| modeGroup | ModeDeclarationGroupPrototype | 0..1 | ref | 由本模块提供的模式组。该组切换的确认引发本事件。 |

**BswModeSwitchedAckEvent.modeGroup 角色中引用的存在性**：对于每个 **BswModeSwitchedAckEvent**，在 BSW 模块配置完成时角色 **modeGroup** 中的引用必须存在。

表 5.34：BswModeManagerErrorEvent（**BswModeManagerErrorEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 表示对模式处理期间发生的错误作出反应的能力。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| modeGroup | ModeDeclarationGroupPrototype | 0..1 | ref | 表示模式管理器的错误行为所适用的 **ModeDeclarationGroupPrototype**。 |

**BswModeManagerErrorEvent.modeGroup 角色中引用的存在性**：对于每个 **BswModeManagerErrorEvent**，在 BSW 模块配置完成时角色 **modeGroup** 中的引用必须存在。

表 5.35：ModeActivationKind（**ModeActivationKind**）

| 枚举 | ModeActivationKind |
| --- | --- |
| Package | M2::AUTOSARTemplates::CommonStructure::ModeDeclaration |
| Note | 用于事件激活的模式切换条件的种类，各枚举字段进一步说明。 |
| Aggregated by | BswModeSwitchEvent.activation, SwcModeSwitchEvent.activation |
| 字面值 | 说明 |
| onEntry | 进入所引用模式时。标签：atp.EnumerationLiteralIndex=0 |
| onExit | 退出所引用模式时。标签：atp.EnumerationLiteralIndex=1 |
| onTransition | 从第 1 个引用模式转换到第 2 个引用模式时。标签：atp.EnumerationLiteralIndex=2 |

#### 5.7.5. 用于 Client-Server 通信的 BSW 事件

图 5.10 及下面的表格给出了由 client-server 调用驱动的事件的更详细图景。预期用例是分区间和/或核间通信。

> 3 这并不排除客户端和服务器在同一分区中执行的配置。

表 5.36：BswOperationInvokedEvent（**BswOperationInvokedEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 本事件在通过 **BSW Scheduler** 进行 Client-Server 通信时因操作调用而抛出。其 "entry" 引用提供随后被调用的 **BswClientServerEntry**。注意，在直接函数调用的情况下不需要该事件。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| entry | BswModuleClientServerEntry | 0..1 | ref | 由本事件调用的 **providedClientServerEntry**。 |

**BswOperationInvokedEvent.entry 角色中引用的存在性**：对于每个 **BswOperationInvokedEvent**，在 BSW 模块配置完成时角色 **entry** 中的引用必须存在。

**BswOperationInvokedEvent 的一致使用**：由属性 **BswOperationInvokedEvent.startsOnEvent** 引用的 **BswCalledEntity** 应引用与 **BswOperationInvokedEvent**（通过其属性 **entry.encapsulatedEntry**）相同的 **BswModuleEntry**（通过其属性 **implementedEntry**）。

**BswOperationInvokedEvent 不使用模式禁用**：**BswOperationInvokedEvent** 不得在角色 **disabledInMode** 中具有对 **ModeDeclaration** 的引用。


表 5.37：BswAsynchronousServerCallReturnsEvent（**BswAsynchronousServerCallReturnsEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 这是通过 **BSW Scheduler** 进行异步 Client-Server 通信的 "回调" 事件，在异步 Client-Server 调用完成后抛出。其 **eventSource** 指定用于检索结果的调用点。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| eventSource | BswAsynchronousServerCallResultPoint | 0..1 | ref | 用于检索结果的调用点。 |

**BswAsynchronousServerCallReturnsEvent.eventSource 角色中引用的存在性**：对于每个 **BswAsynchronousServerCallReturnsEvent**，在 BSW 模块配置完成时角色 **eventSource** 中的引用必须存在。

#### 5.7.6. 用于 Sender-Receiver 通信的 BSW 事件

图 5.11 及下面的表格给出了由 sender-receiver 调用驱动的事件的更详细图景。预期用例是分区间和/或核间通信。

> 4 这并不排除发送者和接收者在同一分区中执行的配置。

表 5.38：BswDataReceivedEvent（**BswDataReceivedEvent**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 本事件在通过 **BSW Scheduler** 的 Sender-Receiver 通信接收到所引用数据时抛出。 |
| Base | — | — | — | ARObject, AbstractEvent, BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.event |
| data | VariableDataPrototype | 0..1 | ref | 接收到的数据。 |

**BswDataReceivedEvent.data 角色中引用的存在性**：对于每个 **BswDataReceivedEvent**，在 BSW 模块配置完成时角色 **data** 中的引用必须存在。

### 5.8. BSW 模块实体的激活原因

通过多个 **BswEvent** 激活给定的 **BswModuleEntity** 是可行的。因此在许多情况下，需要从 **BswModuleEntity** 的实现内部检索关于激活它的 **BswEvent** 的信息。

作为一个典型用例，考虑一个由 **BswTimingEvent** 周期性激活的 **BswSchedulableEntity**，此外它还必须零星执行，例如响应模式切换（**BswModeSwitchEvent**）。

通过使用图 5.12 所示的元模型摘录（在 [6] 中进一步说明），可以生成 **RTE**，使其向 **BswModuleEntity** 提供一个表示激活原因的位向量。

**访问激活原因**：相同的机制对应用软件和基本软件都可用，因此 [6] 中定义的相应规范项和约束也适用于 **BSWMDT**。

激活原因只能提供给那些可能被 **BswEvent** 触发并因此由 **RTE** 处理的 **BswModuleEntity**。作为进一步限制，当前的 **RTE** 规范 [10] 不支持为 **BswCalledEntity** 检索激活原因，即使它们是通过 **BSW Scheduler** 触发的。这导致以下约束：

**BswModuleEntity.activationReason 的适用性**：不得在以下情况下设置 **activationReason**：

* 对于 **BswInterruptEntity** 的实例；
* 对于 **BswCalledEntity** 的实例。

### 5.9. BSW 通信策略

触发器、模式切换和 sender-receiver 通信的实现可以遵循各种策略，**RTE** 或 **BSW Scheduler** 的生成者必须知道这些策略，以便生成正确的 "胶水" 代码。所需的属性如图 5.13 和图 5.14 所示，并在下面的类表中解释。

这类信息类似于 VFB 通信中所谓的 **ComSpecs** 所表示的内容，见 [6]。

表 5.39：BswTriggerDirectImplementation（**BswTriggerDirectImplementation**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定一个释放的触发器，通过 **OS** 调用直接实现，例如在复杂驱动程序模块中。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | BswInternalBehavior.triggerDirectImplementation |
| cat2Isr | Identifier | 0..1 | attr | 由所引用触发器控制的 **OS** category 2 ISR 的名称。这意味着模块管理 category 2 ISR（例如根据硬件初始化和 ISR 启用）。该 ISR 不调用 **RTE** / **SchM** API 来在接收触发器的组件或模块中引发相应事件，而是直接调度被触发的 **ExecutableEntity**。集成者需要 ISR 名称来将 **BswEvent** 和 **RTEEvent** 映射到该 ISR。 |
| masteredTrigger | Trigger | 0..1 | ref | 由本模块直接掌控的触发器。可能有多个不同的 **BswTriggerDirectImplementation** 掌控同一个 **Trigger**。例如，这可能是由于存储器分区所必需的。 |
| task | Identifier | 0..1 | attr | 由所引用触发器控制的 **OS** 任务的名称。这意味着模块使用触发条件直接激活 **OS** 任务，而不是调用 **BswScheduler** 的 API。**RTE** 生成器或 **BswScheduler** 需要任务名称来在接收触发器的组件或模块中引发相应事件。 |

**BswTriggerDirectImplementation.masteredTrigger 角色中引用的存在性**：对于每个 **BswTriggerDirectImplementation**，在 BSW 模块配置完成时角色 **masteredTrigger** 中的引用必须存在。

**属性 task 或 cat2Isr 的使用**：只允许存在其中一个属性。应配置 **task** 或 **cat2Isr** 之一。

表 5.40：BswModeSenderPolicy（**BswModeSenderPolicy**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定针对所引用模式组发送模式切换的细节。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | BswInternalBehavior.modeSenderPolicy |
| ackRequest | BswModeSwitchAckRequest | 0..1 | aggr | 确认请求。 |
| enhancedModeApi | Boolean | 0..1 | attr | 这控制创建返回关于上一个模式和下一个模式信息的增强模式 API。如果设置为 **TRUE**，则应生成增强模式 API。更多细节请参见 **SWS_RTE**。 |
| providedModeGroup | ModeDeclarationGroupPrototype | 0..1 | ref | 指定策略的所提供模式组。 |
| queueLength | PositiveInteger | 0..1 | attr | 发送侧调用队列的长度。队列由 **RTE** 或 **BswScheduler** 实现。该值应大于或等于 0。将 **queueLength** 设置为 0 意味着非排队通信。 |

**BswModeSenderPolicy.providedModeGroup 角色中引用的存在性**：对于每个 **BswModeSenderPolicy**，在 BSW 模块配置完成时角色 **providedModeGroup** 中的引用必须存在。

**BswModeSenderPolicy.queueLength 属性的存在性**：对于每个 **BswModeSenderPolicy**，在 BSW 模块配置完成时属性 **queueLength** 必须存在。

表 5.41：BswModeSwitchAckRequest（**BswModeSwitchAckRequest**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 请求确认模式切换已成功处理。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | BswModeSenderPolicy.ackRequest |
| timeout | TimeValue | 0..1 | attr | 报告错误之前的秒数。 |

**BswModeSwitchAckRequest.timeout 属性的存在性**：对于每个 **BswModeSwitchAckRequest**，在 BSW 模块配置完成时属性 **timeout** 必须存在。

表 5.42：BswModeReceiverPolicy（**BswModeReceiverPolicy**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定针对所引用模式组接收模式切换的细节。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | BswInternalBehavior.modeReceiverPolicy |
| enhancedModeApi | Boolean | 0..1 | attr | 这控制创建返回关于上一个模式和下一个模式信息的增强模式 API。如果设置为 **TRUE**，则应生成增强模式 API。更多细节请参见 **SWS_RTE**。 |
| requiredModeGroup | ModeDeclarationGroupPrototype | 0..1 | ref | 指定策略的所要求模式组。 |
| supportsAsynchronousModeSwitch | Boolean | 0..1 | attr | 指定模块是否能处理异步模式切换的接收（**true**）或不能（**false**）。 |


**BswModeReceiverPolicy.requiredModeGroup 角色中引用的存在性**：对于每个 **BswModeReceiverPolicy**，在 BSW 模块配置完成时角色 **requiredModeGroup** 中的引用必须存在。

**BswModeReceiverPolicy.supportsAsynchronousModeSwitch 属性的存在性**：对于每个 **BswModeReceiverPolicy**，在 BSW 模块配置完成时属性 **supportsAsynchronousModeSwitch** 必须存在。

**数据接收策略**：通过聚合 **BswDataReceptionPolicy**，**BswInternalBehavior** 指定所引用 **VariableDataPrototype** 的详细接收策略。注意，对于本模块中相应 **VariableDataPrototype** 的所有接收点（通过 **BswModuleEntity.dataReceivePoint** 定义），接收策略是相同的。

请注意，由于 BSW 中 sender-receiver 通信机制的限制（与 VFB 通信相比），只能指定排队接收。此外，发送侧没有通信属性。

表 5.43：BswDataReceptionPolicy（**BswDataReceptionPolicy**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 指定通过 **BSW Scheduler** 进行 sender-receiver 通信时所引用数据的接收策略。用于分区间和/或核间通信。 |
| Base | — | — | — | ARObject, BswApiOptions |
| Subclasses | — | — | — | BswQueuedDataReceptionPolicy |
| Aggregated by | — | — | — | BswInternalBehavior.receptionPolicy |
| receivedData | VariableDataPrototype | 0..1 | ref | 使用本策略通过 **BSW Scheduler** 接收的数据。 |

**BswDataReceptionPolicy.receivedData 角色中引用的存在性**：对于每个 **BswDataReceptionPolicy**，在 BSW 模块配置完成时角色 **receivedData** 中的引用必须存在。

表 5.44：BswQueuedDataReceptionPolicy（**BswQueuedDataReceptionPolicy**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 特定于排队接收的接收策略属性。 |
| Base | — | — | — | ARObject, BswApiOptions, BswDataReceptionPolicy |
| Aggregated by | — | — | — | BswInternalBehavior.receptionPolicy |
| queueLength | PositiveInteger | 0..1 | attr | 接收事件的队列长度。 |

**BswQueuedDataReceptionPolicy.queueLength 属性的存在性**：对于每个 **BswQueuedDataReceptionPolicy**，在 BSW 模块配置完成时属性 **queueLength** 必须存在。

**接收策略的存在**：如果某个 **VariableDataPrototype** 在给定 **BswInternalBehavior** 中从任何 **BswModuleEntity** 的 **dataReceivePoint** 被引用，则该 **BswInternalBehavior** 必须聚合恰好一个相应的 **BswDataReceptionPolicy**。

### 5.10. BSW 本地数据

BSW 模块（或集群）需要有能力在其 BSWMD 中声明数据，例如：

* 为了使这些数据可用于测量和校准工具（见第 9 章）；
* 为了将这些数据与 **ServiceNeeds** 相关联地声明，例如作为 NvM 块（见第 12 章）。

**无 RTE 或 BSW Scheduler 支持的本地 BSW 数据**：在许多情况下，模块（或集群）上下文中的此类数据不需要 **RTE** 或 **BSW Scheduler** 的任何支持。它们只是由模块的代码分配，但仍然可以从模块外部访问以进行测量、校准或作为 NvM 镜像。这些数据由以下角色描述：

* **BswInternalBehavior.staticMemory** —— 用于变量数据；
* **BswInternalBehavior.constantMemory** —— 用于常量数据。

**通过 BSW Scheduler API 访问的本地 BSW 数据**：然而，也可以由 **BSW Scheduler** 分配本地数据。这在通过软件仿真进行校准的情况下尤其需要。这类数据通过以下方式声明：

* **BswInternalBehavior.perInstanceParameter**

出于与 **SWCT** 的兼容性原因，这些不同的数据在行为层使用抽象类 **InternalBehavior** 声明，如图 5.15 所示。**InternalBehavior** 的类表已在第 5.1 章列出。

**通过 BSW Scheduler API 访问的 BSW 测量数据**：也可以由 **BSW Scheduler** 分配本地数据。这类数据通过以下方式声明：

* **BswInternalBehavior.arTypedPerInstanceMemory**

这些数据使用 **AutosarDataPrototype** 的类型系统，在 [6] 中有更详细的解释：

表 5.45：ParameterDataPrototype（**ParameterDataPrototype**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes |
| Note | — | — | — | **ParameterDataPrototype** 表示一种形式化的通用信息片段，通常对应用层软件不可变，但可被测量和校准工具更改。**ParameterDataPrototype** 用于各种上下文，特定上下文为原本通用的 **ParameterDataPrototype** 赋予专门的语义。 |
| Base | — | — | — | ARObject, AtpFeature, AtpPrototype, AutosarDataPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | AtpClassifier.atpFeature, BswInternalBehavior.perInstanceParameter, InternalBehavior.constantMemory, NvBlockDescriptor.romBlock, ParameterInterface.parameter, SwcInternalBehavior.perInstanceParameter, SwcInternalBehavior.sharedParameter |
| initValue | ValueSpecification | 0..1 | aggr | 指定 **ParameterDataPrototype** 的初始值。 |

表 5.46：VariableDataPrototype（**VariableDataPrototype**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes |
| Note | — | — | — | **VariableDataPrototype** 表示一种形式化的通用信息片段，通常可由应用层软件更改。**VariableDataPrototype** 用于各种上下文，特定上下文为原本通用的 **VariableDataPrototype** 赋予专门的语义。 |
| Base | — | — | — | ARObject, AtpFeature, AtpPrototype, AutosarDataPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable |
| Aggregated by | — | — | — | ApplicationInterface.indication, AtpClassifier.atpFeature, BswInternalBehavior.arTypedPerInstanceMemory, BswModuleDescription.providedData, BswModuleDescription.requiredData, BulkNvDataDescriptor.bulkNvBlock, InternalBehavior.staticMemory, NvBlockDescriptor.ramBlock, NvDataInterface.nvData, SenderReceiverInterface.dataElement, ServiceInterface.event, SwcInternalBehavior.arTypedPerInstanceMemory, SwcInternalBehavior.explicitInterRunnableVariable, SwcInternalBehavior.implicitInterRunnableVariable |
| initValue | ValueSpecification | 0..1 | aggr | 指定 **VariableDataPrototype** 的初始值。 |

### 5.11. 与相应 SWC 的同步

实现 **ServiceSwComponentType**、**EcuAbstractionSwComponentType** 或 **ComplexDeviceDriverSwComponentType** 的 BSW 模块需要在其 SWC 描述和 BSWM 描述之间进行若干映射，以生成 **RTE** 或 **BSW Scheduler**。

一个用例如下：

**模式切换或触发器的同步**：通过 **RTE** 通信的 BSW 模块既能在基本软件内部也能向 **RTE** 之上的 SWC 提供触发器和模式切换（例如实现 **EcuAbstractionSwComponentType** 的 BSW 模块）。可能出现这样的情况：一个模块想要向 BSW 和 "RTE 之上" 的 SWC 都发出模式切换或触发器，即通过 **BSW Scheduler** API 的调用应产生与通过 **RTE** 端口 API 的调用相同的触发器或模式切换（细节在 [10] 中规定）。在这种情况下，BSW 中提供的 **Trigger** 或 **ModeDeclarationGroupPrototype** 应映射到端口接口提供的 **Trigger** 或 **ModeDeclarationGroupPrototype**。该信息是相应配置 **RTE** 的输入。

另一个用例是在 BSW 模块中指定 **RunnableEntity**，以允许通过端口调用 **RTE** 或从 **RTE** 调用：

**BSW 中用于 RTE 访问的 RunnableEntity**：在这种情况下，还应指定一个 **BswModuleEntity** 以允许 BSW 特定的描述，并且这两个元素必须关联。例如，当 **RTE** 需要确定某个 **RunnableEntity** 是否在中断上下文中运行时，这是必需的。

表 5.47：SwcBswMapping（**SwcBswMapping**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::SwcBswMapping |
| Note | — | — | — | 将 **SwcInternalBehavior** 映射到 **BswInternalBehavior**。这需要协调 **RTE** 和 BSW 调度机制对 AUTOSAR 服务组件、ECU 抽象组件和复杂驱动程序组件的 API 生成和调度。标签：atp.recommendedPackage=SwcBswMappings |
| Base | — | — | — | ARElement, ARObject, AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable |
| Aggregated by | — | — | — | ARPackage.element, AtpClassifier.atpFeature |
| bswBehavior | BswInternalBehavior | 0..1 | ref | 被映射的 **BswInternalBehavior**。 |
| runnableMapping | SwcBswRunnableMapping | * | aggr | 一对 SWC 和 BSW runnable 之间的映射。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=runnableMapping, runnableMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| swcBehavior | SwcInternalBehavior | 0..1 | ref | 被映射的 **SwcInternalBehavior**。 |
| synchronizedModeGroup | SwcBswSynchronizedModeGroupPrototype | * | aggr | 一对要由调度器同步的 SWC 和 BSW 模式组原型。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=synchronizedModeGroup, synchronizedModeGroup.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| synchronizedTrigger | SwcBswSynchronizedTrigger | * | aggr | 一对要由调度器同步的 SWC 和 BSW **Trigger**。构造型：atpSplitable; atpVariation 标签：atp.Splitkey=synchronizedTrigger, synchronizedTrigger.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |

表 5.48：SwcBswRunnableMapping（**SwcBswRunnableMapping**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::SwcBswMapping |
| Note | — | — | — | 如果某个 **BswModuleEntity** 作为 BSW 模块的一部分（在 AUTOSAR 服务、复杂驱动程序或 ECU 抽象的情况下）实现，则将其映射到 **RunnableEntity**。工具可以使用该映射查找有关行为的相关信息，例如 **bswEntity** 是否应在中断上下文中运行。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | SwcBswMapping.runnableMapping |
| bswEntity | BswModuleEntity | 0..1 | ref | 被映射的 **BswModuleEntity**。 |
| swcRunnable | RunnableEntity | 0..1 | ref | 被映射的 SWC runnable。 |

**SwcBswRunnableMapping.bswEntity 角色中引用的存在性**：对于每个 **SwcBswRunnableMapping**，在 BSW 模块配置完成时角色 **bswEntity** 中的引用必须存在。

**SwcBswRunnableMapping.swcRunnable 角色中引用的存在性**：对于每个 **SwcBswRunnableMapping**，在 BSW 模块配置完成时角色 **swcRunnable** 中的引用必须存在。

表 5.49：SwcBswSynchronizedModeGroupPrototype（**SwcBswSynchronizedModeGroupPrototype**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::SwcBswMapping |
| Note | — | — | — | 将组件通过端口提供的模式组与 BSW 模块或集群提供的模式组同步。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | SwcBswMapping.synchronizedModeGroup |
| bswModeGroup | ModeDeclarationGroupPrototype | 0..1 | ref | BSW 模式组原型。 |
| swcModeGroup | ModeDeclarationGroupPrototype | 0..1 | iref | 由特定端口提供的 SWC 模式组原型。InstanceRef 实现者：PModeGroupInAtomicSwcInstanceRef |

**SwcBswSynchronizedModeGroupPrototype.bswModeGroup 角色中引用的存在性**：对于每个 **SwcBswSynchronizedModeGroupPrototype**，在 BSW 模块配置完成时角色 **bswModeGroup** 中的引用必须存在。

**SwcBswSynchronizedModeGroupPrototype.swcModeGroup 角色中 instanceRef 的存在性**：对于每个 **SwcBswSynchronizedModeGroupPrototype**，在 BSW 模块配置完成时角色 **swcModeGroup** 中的 instanceRef 必须存在。

表 5.50：SwcBswSynchronizedTrigger（**SwcBswSynchronizedTrigger**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::CommonStructure::SwcBswMapping |
| Note | — | — | — | 将组件通过端口提供的 **Trigger** 与 BSW 模块或集群提供的 **Trigger** 同步。 |
| Base | — | — | — | ARObject |
| Aggregated by | — | — | — | SwcBswMapping.synchronizedTrigger |
| bswTrigger | Trigger | 0..1 | ref | BSW **Trigger**。 |
| swcTrigger | Trigger | 0..1 | iref | 由特定端口提供的 SWC **Trigger**。InstanceRef 实现者：PTriggerInAtomicSwcTypeInstanceRef |

**SwcBswSynchronizedTrigger.bswTrigger 角色中引用的存在性**：对于每个 **SwcBswSynchronizedTrigger**，在 BSW 模块配置完成时角色 **bswTrigger** 中的引用必须存在。

**SwcBswSynchronizedTrigger.swcTrigger 角色中 instanceRef 的存在性**：对于每个 **SwcBswSynchronizedTrigger**，在 BSW 模块配置完成时角色 **swcTrigger** 中的 instanceRef 必须存在。

**通过端口调用的 BSW 函数的实参名称确定**：在通过 **RTE** 进行端口函数调用的情况下，**RTE API** 生成器应根据通过映射引用的 **BswModuleEntry** 的签名确定函数实参的名称（仅用于声明目的）。

规则如下：函数实参的名称应（按给定顺序）取自相关 **PortPrototype** 所类型化的 **ClientServerInterface** 所属的 **ClientServerOperation**（依次被 **OperationInvokedEvent** 引用、被 **RunnableEntity** 引用、在 **SwcBswRunnableMapping** 中映射的 **BswModuleEntity** 引用、被 **BswModuleEntry** 引用）中定义的 **SwServiceArg** 的 **shortName**（按给定顺序）。

该规则同样适用于 **PortDefinedArgumentValue** 和 "普通" 端口操作参数。

如果存在 **SwcBswRunnableMapping**，则上述规则取代由属性 **RunnableEntity.argument** 对任何实参标识符的定义。

一个组件/模块的所有映射都聚合在属于元模型 **CommonStructure** 的 **SwcBswMapping** 中。该映射被视为内部行为的附加物（因为它主要用于设置 **RTE**），但可以指定为模块 **Implementation** 可以引用的单独工件。因此 **SwcBswMapping** 派生自 **ARElement**。

**BswModuleEntry 符号的确定**：**BswModuleEntry** 的符号组成如下：&lt;bsnp&gt;[\_&lt;vi&gt;\_&lt;ai&gt;]\_&lt;name&gt;，其中：

* &lt;bsnp&gt;：如果没有定义 **BswSchedulerNamePrefix**，则为 **BswModuleDescription** 的 **shortName**；如果定义了 **BswSchedulerNamePrefix**，则为该 **BswModuleEntity** 的 **BswSchedulerNamePrefix** 的 **symbol** 属性的值；
* &lt;vi&gt;：BSW 模块的 **vendorId**；
* &lt;ai&gt;：BSW 模块的 **vendorApiInfix**；
* &lt;name&gt;：被引用为 **implementedEntry** 的 **BswModuleEntry shortName** 中 "&lt;bsnp&gt;\_" 之后的字符串。

但是，如果 &lt;bsnp&gt;\_ 不是相关 **BswModuleEntry shortName** 的前缀，则 &lt;name&gt; 与 **BswModuleEntry.shortName** 相同。

更多细节另请参见 **SWS_RTE**。

软件组件与 BSW 模块之间的这种同步机制仅限于基本软件的相关部分：

**SwcBswMapping 的语义**：只有当被引用的 **SwcInternalBehavior** 由 **ServiceSwComponentType**、**EcuAbstractionSwComponentType** 或 **ComplexDeviceDriverSwComponentType** 聚合时，**SwcBswMapping** 才有效。

**InternalBehavior 引用的一致性**：由 **SwcImplementation.swcBswMapping** 确定的 **SwcBswMapping** 中 **SwcBswMapping.swcBehavior** 引用的 **SwcInternalBehavior**，应与 **SwcImplementation.behavior** 引用的 **SwcInternalBehavior** 相同。

**InternalBehavior 引用的一致性**：由 **BswImplementation.swcBswMapping** 确定的 **SwcBswMapping** 中 **SwcBswMapping.bswBehavior** 引用的 **BswInternalBehavior**，应与 **BswImplementation.behavior** 引用的 **BswInternalBehavior** 相同。

更多约束如下：

**同步的 runnable 与可调度实体应一致**：在 **RunnableEntity** 映射到 **BswCalledEntity** 或 **BswSchedulableEntity** 的情况下，**RTE Generator** 仅为 **BswCalledEntity** 或 **BswSchedulableEntity** 发出入口点原型（取决于为 SWC 或 BSW 指定的事件）。控制这种情况的 **SwcBswRunnableMapping** 实例仅在所映射的 **RunnableEntity** 和 **BswSchedulableEntity** 的若干属性一致时才有效，特别是以下所有约束都适用于给定 **SwcBswRunnableMapping** 实例的属性：

* **swcRunnable.symbol** 应与 [上述规则] 定义的 **bswEntity** 符号相同；
* **swcRunnable.minimumStartInterval** 应与 **bswEntity.minimumStartInterval** 相同；
* **swcRunnable.canBeInvokedConcurrently** 应与 **bswEntity.implementedEntry.isReentrant** 相同；
* **swcRunnable.swAddrMethod** 应为空，或与通过 **bswEntity.swAddrMethod** 定义的 **SwAddrMethod** 具有相同属性。这是为确保底层代码实体的存储器段具有唯一配置所必需的；
* **swcRunnable.activationReason** 和 **bswEntity.activationReason** 如果定义相同的 **bitPosition**，应具有相同的 **shortName**；如果定义相同的 **shortName**，应具有相同的 **bitPosition**。

更多细节另请参见 **SWS_RTE**。

**同步模式组应具有相同类型**：**SwcBswSynchronizedModeGroupPrototype** 只能引用类型相同的 **ModeDeclarationGroupPrototype**，即具有相同的 **ModeDeclarationGroup**。

**同步模式组应具有相同上下文**：**SwcBswSynchronizedModeGroupPrototype** 定义的映射意味着提供一个模式组原型的组件也通过在 **SwcBswMapping** 中同步各自的行为而映射到提供另一个模式组原型的模块。

**同步触发器应具有相同上下文**：**SwcBswSynchronizedTrigger** 定义的映射意味着提供一个触发器的组件也通过在 **SwcBswMapping** 中同步各自的行为而映射到提供另一个触发器的模块。

**同步触发器应实现相同策略**：只有当属性 **SwcBswSynchronizedTrigger.swcTrigger.swImplPolicy** 与属性 **SwcBswSynchronizedTrigger.bswTrigger.swImplPolicy** 具有相同值时，**SwcBswSynchronizedTrigger** 定义的映射才有效。

下一个约束是为了避免生成的头文件中的冲突，原因与第 4.2 节中一个模块内的约束相同：

**映射的 BSWM 和 SWC 中不同模式组应具有不同名称**：如果 **SwcInternalBehavior** 映射到 **BswInternalBehavior**，则相应的 SWC 和 BSW 模块描述不得引用具有相同 **shortName** 但元素不同的不同 **ModeDeclarationGroup**。当这些模式组不同步而是独立使用时，尤其如此。

### 5.12. 分布在多个分区的 BSW 行为

存在一些有效用例，其中给定 BSW 模块的部分在一个 ECU 内与不同处理器核相关的不同分区上执行（见需求文档和 [13]）。这包括这样的情况：在给定 ECU 上，同一模块的不同服务运行在不同分区中，也包括在同一 ECU 上同一服务在不同分区中可用。

在 BSWMD 中，没有关于软件实体与分区或处理器核关联的严格信息。这些信息稍后在 ECU 配置阶段通过将 **BswEvent** 映射到 **OS** 任务（而后者又映射到分配给分区和/或处理器核的 **OsApplication**）来添加（见 [15]）。由这些 **BswEvent** 驱动的 **BswModuleEntity** 随后被间接映射到分区和核。

请注意，在某些情况下（例如无存储器保护、重入），可以使用未映射到任务但仍可从多个分区访问的 **BswModuleEntity** 和 **BswOperationInvokedEvent**（详情见 [13]）。

同样，服务是否可能跨分区边界被调用的信息，也是通过 **BSW Scheduler** 的 ECU 配置（在 BSW 通信的情况下）或通过在 ECU 配置时创建的端口连接器（在 AUTOSAR 服务的情况下）添加的。

尽管如此，**BswInternalBehavior** 必须为此类配置做好准备，因为模块代码中可能在不同分区中运行且必须显式映射到不同任务的部分必须由不同的 **BswEvent** 驱动。此外，区分每个分区的 **BswModuleEntity** 的通信行为是有用的，例如，当在一个处理器核上运行时发送数据而在另一个核上运行时接收数据。此类信息可能需要用于 **RTE** 和 **IOC** 的细粒度配置以及文档、时序和调用树分析。

特别地，可以陈述以下规则：

**包含在不同分区上执行的 BswModuleEntity 的 BswInternalBehavior**：如果一个模块被设计为让相同的代码实体（经过适当的 ECU 配置后）在不同分区中运行，则每个代码实体应仅由一个 **BswModuleEntity** 描述。换言之，对于给定代码，不应存在每个分区单独的 **BswModuleEntity**。

此外，如果需要区分每个分区的行为，则应在模块的 **BswInternalBehavior** 中提供以下元素：

* 每个可能运行某些所含 **BswModuleEntity** 的分区上下文都应通过元类 **BswDistinguishedPartition** 实例的聚合来建模。注意这是一种抽象表示法，具体分区应在流程后期作为 "虚拟" 模块 **EcuC** 配置的一部分来定义，见 [16]；
* 启动本 **BswInternalBehavior** 的 **BswModuleEntity** 的 **BswEvent** 应按可能分区分别设置，并且——在有限制的情况下——通过引用 **BswEvent.contextLimitation** 指示允许它们映射到哪个分区；
* 本 **BswInternalBehavior** 的 **BswModuleCallPoint** 应——在有限制的情况下——通过引用 **BswModuleCallPoint.contextLimitation** 指示它们在哪些分区中使用；
* 本 **BswInternalBehavior** 的 **BswVariableAccess** 元素应——在有限制的情况下——通过引用 **BswVariableAccess.contextLimitation** 指示它们在哪些分区中被访问。

> 5 代码有可能检索其运行在哪个处理器核上的信息——见 [13]——和/或它是由哪个事件启动的，见第 5.8 节。

请注意，对于仅提供给单个分区内调用者的函数，不需要 **BswOperationInvokedEvent** 和 **BswModuleClientServerEntry**。

此外，该规则不适用于应始终在调用者任务上下文中运行的 **BswCalledEntity**。

**在不同分区上提供的同一 AUTOSAR 服务的 BswInternalBehavior**：如果一个模块被设计为实现一项 AUTOSAR 服务——表示为一个特定的 **ServiceSwComponentType**——该服务应在（经过适当的 ECU 配置后）通过相同的代码在多个不同 BSW 分区的显式映射任务中运行，那么为每个 **RunnableEntity** 定义一个 **SwcBswRunnableMapping** 和一个映射的 **BswModuleEntity** 就足够了。但是，必要的 **RTEEvent** 对于每个可能的分区应不同。

该规则不适用于那些不应映射到任务的 **RTEEvent** 及其对应的 **RunnableEntity** 和 **BswModuleEntity**。

如果所涉及的 **BswModuleEntity** 的行为需要按分区区分，则额外适用上述规则。

表 5.51：BswDistinguishedPartition（**BswDistinguishedPartition**）

| 属性 | 类型 | 多重性 | 种类 | 说明 |
| --- | --- | --- | --- | --- |
| Package | — | — | — | M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior |
| Note | — | — | — | 本元类的每个实例表示一个抽象分区，封闭的 **BswModuleBehavior** 的代码可在该分区的上下文中执行。预期用例是区分多个分区以实现每个分区不同的行为，例如在具有共享 BSW 代码的多核 ECU 中充当主节点或从节点。 |
| Base | — | — | — | ARObject, Referrable |
| Aggregated by | — | — | — | BswInternalBehavior.distinguishedPartition |

**BswDistinguishedPartition 只能在特定 BswInternalBehavior 的上下文中使用**：所有引用某个 **BswDistinguishedPartition** 的 **BswEvent**、**BswModuleCallPoint** 和 **BswVariableAccess** 实例，必须属于同样聚合了被引用 **BswDistinguishedPartition** 的同一 **BswInternalBehavior**。
