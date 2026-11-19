---
title: "Methodology（方法论）"
spec: AUTOSAR_CP_TR_Methodology
release: R23-11
---

## 参考文献

<a id="ref-1"></a>[1] Methodology Requirements（方法论需求）
> AUTOSAR_CP_RS_Methodology

<a id="ref-2"></a>[2] Standardization Template（标准化模板）
> AUTOSAR_FO_TPS_StandardizationTemplate

<a id="ref-3"></a>[3] Glossary（术语表）
> AUTOSAR_FO_TR_Glossary

<a id="ref-4"></a>[4] Software Process Engineering Meta-Model Specification
> http://www.omg.org/spec/SPEM/2.0/

<a id="ref-5"></a>[5] Integration of Franca IDL Software Component Descriptions
> AUTOSAR_CP_TR_FrancaIntegration

<a id="ref-6"></a>[6] Virtual Functional Bus（虚拟功能总线）
> AUTOSAR_CP_EXP_VFB

<a id="ref-7"></a>[7] Software Component Template（软件组件模板）
> AUTOSAR_CP_TPS_SoftwareComponentTemplate

<a id="ref-8"></a>[8] System Template（系统模板）
> AUTOSAR_CP_TPS_SystemTemplate

<a id="ref-9"></a>[9] General Specification of Basic Software Modules（基础软件模块通用规范）
> AUTOSAR_CP_SWS_BSWGeneral

<a id="ref-10"></a>[10] General Specification of Transformers（转换器通用规范）
> AUTOSAR_CP_ASWS_TransformerGeneral

<a id="ref-11"></a>[11] Basic Software Module Description Template（基础软件模块描述模板）
> AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate

<a id="ref-12"></a>[12] Specification of ECU Configuration（ECU 配置规范）
> AUTOSAR_CP_TPS_ECUConfiguration

<a id="ref-13"></a>[13] Specification of Memory Mapping（内存映射规范）
> AUTOSAR_CP_SWS_MemoryMapping

<a id="ref-14"></a>[14] Specification of Module E2E Transformer（模块 E2E 转换器规范）
> AUTOSAR_CP_SWS_E2ETransformer

<a id="ref-15"></a>[15] Diagnostic Extract Template（诊断提取模板）
> AUTOSAR_CP_TPS_DiagnosticExtractTemplate

<a id="ref-16"></a>[16] Specification of RTE Software（RTE 软件规范）
> AUTOSAR_CP_SWS_RTE

<a id="ref-17"></a>[17] ISO 26262:2018 (all parts) - Road vehicles - Functional Safety
> https://www.iso.org

<a id="ref-18"></a>[18] Generic Structure Template（通用结构模板）
> AUTOSAR_FO_TPS_GenericStructureTemplate

<a id="ref-19"></a>[19] Specification of ECU Resource Template（ECU 资源模板规范）
> AUTOSAR_CP_TPS_ECUResourceTemplate

## 1. 简介

### 1.1. 目标

AUTOSAR 要求系统开发的某些步骤采用统一的技术方法。该方法称为 AUTOSAR 方法论。本文档定义并描述这一 AUTOSAR 方法论。它涵盖了使用 AUTOSAR 开发系统的所有主要步骤：从虚拟功能总线的定义到 ECU 可执行文件的生成。

方法论的需求在文档 [\[1\]](#ref-1) 中定义。

### 1.2. 文档约定

本文档遵循一系列文档约定，如下所述。

AUTOSAR 的技术术语以等宽字体排版，例如 ECU。一般规则是，技术术语的复数形式通过在单数形式后加 "s" 构成，例如 ECU。

### 1.3. 范围

- 组织：方法论以模块化格式建模，允许组织对其进行裁剪并将方法论结合到自己的内部流程中，同时标识它们与其他组织交互的点。

- 工程师：方法论的范围设定允许各种角色的工程师快速找到与其特定需求相关的 AUTOSAR 信息。

> 1 示例聚合作为用例在第 [2](#2-用例) 章中提供。

- 工具供应商：方法论提供了一种在所有 AUTOSAR 成员之间共享的通用语言，并对工具应支持的能力形成共同的期望。

### 1.4. 术语和缩略语

术语和缩略语的主要列表在 [\[3, FO TR Glossary\]](#ref-3) 中定义。

### 1.5. 概述






> 2 已定义活动的集合在第 [3](#3-方法论库) 章中描述。

> 3 见图 2.9。

### 1.6. 方法论概念

#### 1.6.1. 方法论库元素

> 4 相关元素见第 [3](#3-方法论库) 章和第 [3.1](#31-公共元素) 章。

> 5 用例见第 [2](#2-用例) 章，总体概览见第 [2.1](#21-总体概览) 章。

> 6 RS_Methodology 文档在一般性地提及流程元素时使用术语 'Activity'。在本文档中，原子流程元素称为 'Task（任务）'，而 'Activity（活动）' 用于组织任务并定义过程。

> 7 方法论库元素见第 [1.6.1](#161-方法论库元素) 章，用例元素见第 [1.6.2](#162-用例规范) 章。> 8 见第 [3](#3-方法论库) 章。

- 任务定义

- 工作产品定义

- 角色定义

- 工具定义

- 指南

> 9 指南目前未在 AUTOSAR 方法论中使用。它可能在未来的 AUTOSAR 发布版中使用。

> 10 任务定义见第 [1.6.1.1](#1611-任务定义) 章，工作产品定义见第 [1.6.1.2](#1612-工作产品定义) 章，角色定义见第 [1.6.1.3](#1613-角色定义) 章，工具定义见第 [1.6.1.4](#1614-工具定义) 章，指南见第 [1.6.1.5](#1615-指南) 章。


##### 1.6.1.1. 任务定义

本文档中使用的任务的概览见图 1.2。

表1.1：任务定义（**Task Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 被扩展 | on demand: Extended By Task(s) | — |
| 扩展 | on demand: extended Task(s) | — |
| 执行者 | what Role performs the Task | 0..1 or 1 Description of the specific role needed |
| 消费 | what is consumed by the Task | 0..1 or 0..* Explanation on why this Element is needed. |
| 产出 | what is produced by the Task | 0..1 or 0..* Explanation on why this Element is needed. |
| 输入/输出 | what is produced and consumed by the Task | 0..1 or 0..* Explanation on why this Element is needed. |
| Used Tool | Tool used for that Task | 0..1 or 1 |

##### 1.6.1.2. 工作产品定义

工作产品可以是工件（**Artifact**）类型或交付物（**Deliverable**）类型：

  - AUTOSAR XML

  - 源代码

  - 目标代码

  - 可执行文件

  - 文本

  - 需要独立的版本控制

  - 需要专门的生命周期管理

  - 需要满足不同的交换要求

  - 负责角色的变化

  - 多重性的变化

  - 物理表示或格式的变化

  - 其中一个产品可能是交付给另一方的单独交付物

  - 将标准化部分与非标准化部分分离

> 11 更多细节见第 [3.1.1](#311-工作产品种类) 章。

表1.2：Category Definition（**Category Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 种类 | Work Product Kind, e.g. ARXML | — |
| 被扩展 | on demand: Extended By Work Product(s) | — |
| 扩展 | on demand: extended Work Product(s) | — |
| 聚合 | What Work Products (Artifacts) are aggregated | 0..1 or 0..* Description of the Aggregation. |
| 聚合于 | To which Work Product (Deliverable) is it aggregated | 0..1 or 1 Description of the context of the Aggregation. |
| 消费者 | Which task is consuming the Work Product | 0..1 or 1 Description of the context of the Work Product production and consumption. |
| 输入/输出 | Which task is producing and consuming the Work Product | 0..1 or 1 Description of the context of the Work Product production and consumption. |

##### 1.6.1.3. 角色定义

表1.3：角色定义（**Role Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 产出者 | Which task is producing the Work Product | 0..1 or 1 Description of the context of the Work Product production. |
| 使用的元模型元素 | MetamodelElement Relationship 0..1 or 1 Meta Model Class that implements or contributes to the implementation of the Work Product | — |
| 交付物 | Deliverable Name | — |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 种类 | Work Product Kind, e.g. ARXML | — |
| 被扩展 | on demand: Extended By Work Product(s) | — |
| 扩展 | on demand: extended Work Product(s) | — |
| 聚合 | What Work Products (Artifacts) are aggregated | 0..1 or 0..* Description of the Aggregation. |
| 聚合于 | To which Work Product (Deliverable) is it aggregated | 0..1 or 1 Description of the context of the Aggregation. |
| 消费者 | Which task is consuming the Work Product | 0..1 or 1 Description of the context of the Work Product production and consumption. |
| 输入/输出 | Which task is producing and consuming the Work Product | 0..1 or 1 Description of the context of the Work Product production and consumption. |
| 产出者 | Which task is producing the Work Product | 0..1 or 1 Description of the context of the Work Product production. |
| 使用的元模型元素 | MetamodelElement Relationship 0..1 or 1 Meta Model Class that implements or contributes to the implementation of the Work Product | — |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 执行 | In which task the performer is acting | 0..1 or 1 Description of the activities of role in task |

##### 1.6.1.4. 工具定义

| Tool | Tool Name |  |

| Package | Location in the MetaModel package |  |  |
| Brief Description | some description as summary |  |  |
| Description | some description as more detailed explanation |  |  |
| Kind | Tool Kind (e.g. Editor) |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Task where the tool is used | 0..1 or 1 | Description of the activites supported by the tool in this task |

##### 1.6.1.5. 指南

- 支持材料（**Supporting Material**）：支持材料是其他未在别处具体定义的指南类型的统称。它可以关联到各种内容元素，即也包括其他指南元素。AUTOSAR 方法论使用支持材料指南类型来定义扉页、变更历史、免责声明等。

- 工具导师（**Tool Mentor**）：工具导师展示如何在任务的上下文中或独立于任务或活动使用特定工具完成某项工作。在 AUTOSAR 方法论的上下文中，工具导师以与工具元素相同的方式使用。

- 白皮书（**White Paper**）：白皮书是经过外部评审或发布的概念指南，可以独立于其他方法内容阅读和理解。AUTOSAR 文档就是白皮书的例子。

#### 1.6.2. 用例规范

本节说明第 [2](#2-用例) 章中的用例是如何规定的。前两个子节介绍用例的主要组成部分。之后说明这些元素如何与方法论库元素一起用于描述用例。


> 12 元素符号见图 1.7。

##### 1.6.2.1. 活动

##### 1.6.2.2. 能力模式

引用方法论库元素（参见第 [1.6.1](#161-方法论库元素) 节），以便与活动一起描述所谓的能力模式（**Capability Patterns**）。

##### 1.6.2.3. 用例的描述

对于 AUTOSAR 方法论，主要用例用三种类型的图描述。

> 13 在 Enterprise Architect 中，SPEM 的 'Capability Pattern' 称为 'Process Pattern'。

> 14 见图 1.8。

图之后是其对应的表，详情如下：

| Process Pattern | Capability Pattern Name |  |

| Package | Location in the MetaModel package |  |  |
| Brief Description | some description as summary |  |  |
| Description | some description as more detailed explanation |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Activity nested to the Capability Pattern or to another Activity | 0..1 or 1 | Context explanation |
| Consumes | Deliverable consumed by the Capability Pattern | 0..1 or 0..* | Why this Capability Pattern needs to consume this Deliverable |
| Produces | Deliverable produced by the Capability Pattern | 0..1 or 0..* | Why this Capability Pattern is producing this Deliverable |

图之后是其对应的表，详情如下：

表1.4：Activity Definition（**Activity Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | Location in the MetaModel package | — |
| 简要描述 | some description as summary | — |
| 描述 | some description as more detailed explanation | — |
| 被扩展 | on demand: Extended By Activity(s) | — |
| 扩展 | on demand: extended Activity(s) | — |
| 聚合 | Nested task definition | 0..1 or 1 Task usage description if needed |
| 消费 | What is consumed by the Activity | 0..1 or 0..* Explanation on why this Element is needed. |
| 输入/输出 | What is produced and consumed by the activity | 0..1 or 0..* Explanation on why this Element is needed. |
| 产出 | What is produced by the activity | 0..1 or 0..* Explanation on why this Element is needed. |
| 前驱 | Predecessor of the activity | 0..1 or 1 Explanation on why the Predecessor is needed. |

> 15 见图 1.9。

> 16 参见第 [1.6.1.1](#1611-任务定义) 章，示例见图 2.16。

### 1.7. 需求追溯

本节说明本规范对相应需求文档 [\[1\]](#ref-1) 的响应。

| Requirement | Description | Satisfied by |  |

| [RS_METH_00006] | The methodology shall explain how to build an AUTOSAR system | [TR_METH_01003] [TR_METH_01039] [TR_METH_01044] [TR_METH_01045] [TR_METH_01046] [TR_METH_01047] [TR_METH_01048] [TR_METH_01049] [TR_METH_01061] [TR_METH_01085] [TR_METH_01087] [TR_METH_01092] [TR_METH_01093] [TR_METH_01109] [TR_METH_01110] [TR_METH_01111] [TR_METH_01112] [TR_METH_01114] [TR_METH_01134] [TR_METH_01135] [TR_METH_03002] [TR_METH_03003] [TR_METH_03004] |  |
| [RS_METH_00015] | The methodology shall be independent of programming languages | [TR_METH_01018] |  |
| [RS_METH_00016] | The methodology shall support building a system of both AUTOSAR and Non-AUTOSAR ECU s | [TR_METH_01019] [TR_METH_01128] [TR_METH_01129] |  |
| [RS_METH_00018] | The methodology shall be modular | [TR_METH_01000] [TR_METH_01002] [TR_METH_01004] [TR_METH_01006] [TR_METH_01007] [TR_METH_01021] [TR_METH_01022] [TR_METH_01029] [TR_METH_01030] [TR_METH_01084] [TR_METH_01110] |  |
| [RS_METH_00020] | The methodology shall support round-trip engineering | [TR_METH_01071] [TR_METH_01089] [TR_METH_02004] |  |
| [RS_METH_00032] | The methodology shall support different abstraction levels | [TR_METH_01000] [TR_METH_01040] |  |
| [RS_METH_00033] | The methodology should support the VFB concept | [TR_METH_01039] [TR_METH_01045] [TR_METH_01054] [TR_METH_02000] |  |
| [RS_METH_00041] | The methodology shall support top-down and bottom-up approaches | [TR_METH_01071] |  |
| [RS_METH_00042] | The methodology shall incorporate the usage of industry standard tools | [TR_METH_01010] [TR_METH_01013] [TR_METH_01025] [TR_METH_01093] |  |
| [RS_METH_00056] | The AUTOSAR methodology shall not be bound to a particular life-cycle model | [TR_METH_01002] [TR_METH_01004] [TR_METH_01006] [TR_METH_01012] [TR_METH_01024] [TR_METH_01030] [TR_METH_01031] [TR_METH_01035] |  |
| [RS_METH_00062] | The methodology shall support configuration of parameters with different binding time. | [TR_METH_01086] [TR_METH_01095] [TR_METH_01098] [TR_METH_01104] [TR_METH_01108] [TR_METH_01150] [TR_METH_01151] |  |
| [RS_METH_00066] | The methodology shall allow activities that reference tools | [TR_METH_01025] [TR_METH_01034] |  |
| [RS_METH_00069] | It shall be possible to add precise and human readable documentation to each work product | [TR_METH_01123] [TR_METH_01124] |  |
| [RS_METH_00074] | The methodology shall specify binding times | [TR_METH_00001] [TR_METH_00002] [TR_METH_00003] [TR_METH_02011] [TR_METH_02012] [TR_METH_02013] [TR_METH_02014] [TR_METH_02020] |  |
| Requirement | Description | Satisfied by |  |
| [RS_METH_00075] | The methodology shall specify the tasks of resolving variant | [TR_METH_00001] [TR_METH_02016] |  |
| [RS_METH_00076] | The methodology shall specify a work product for values of variant selectors | [TR_METH_02016] [TR_METH_02017] |  |
| [RS_METH_00077] | The methodology shall support different views on the SW-C structure by OEM s and suppliers | [TR_METH_01049] [TR_METH_01076] [TR_METH_01079] [TR_METH_01080] [TR_METH_01081] [TR_METH_01082] [TR_METH_01125] [TR_METH_01126] [TR_METH_01127] [TR_METH_01130] [TR_METH_01131] |  |
| [RS_METH_00078] | The methodology shall explain the typical usage of different views on the system of the OEM | [TR_METH_01044] [TR_METH_01050] [TR_METH_01068] |  |
| [RS_METH_00079] | The methodology shall explain the typical usage of different views on the system of the supplier | [TR_METH_01068] [TR_METH_01079] [TR_METH_01080] [TR_METH_01081] [TR_METH_01082] |  |
| [RS_METH_00080] | The AUTOSAR methodology shall support the concept of implicit communication behavior | [TR_METH_01120] |  |
| [RS_METH_00083] | The AUTOSAR methodology shall explain the description and handling of Data Exchange Points | [TR_METH_01202] [TR_METH_01204] [TR_METH_01205] |  |
| [RS_METH_00084] | The AUTOSAR methodology shall relate templates to a distributed development process | [TR_METH_01202] [TR_METH_01204] [TR_METH_01205] |  |
| [RS_METH_00208] | The methodology shall support the data exchange between different stakeholders | [TR_METH_01044] [TR_METH_01047] [TR_METH_01050] [TR_METH_01051] [TR_METH_01052] [TR_METH_01053] [TR_METH_01055] [TR_METH_01056] [TR_METH_01057] [TR_METH_01058] [TR_METH_01059] [TR_METH_01060] [TR_METH_01061] [TR_METH_01065] [TR_METH_01066] [TR_METH_01067] [TR_METH_01068] [TR_METH_01070] [TR_METH_01071] [TR_METH_01075] [TR_METH_01076] [TR_METH_01077] [TR_METH_01078] [TR_METH_01079] [TR_METH_01080] [TR_METH_01081] [TR_METH_01082] [TR_METH_01083] [TR_METH_01088] [TR_METH_01089] [TR_METH_01090] [TR_METH_01092] [TR_METH_01109] [TR_METH_01110] [TR_METH_01112] [TR_METH_01114] [TR_METH_01116] [TR_METH_01117] [TR_METH_01125] [TR_METH_01126] [TR_METH_01127] [TR_METH_01132] [TR_METH_01133] [TR_METH_01151] [TR_METH_01153] [TR_METH_02000] [TR_METH_02001] [TR_METH_02002] [TR_METH_02003] [TR_METH_02015] [TR_METH_02016] [TR_METH_02017] [TR_METH_02018] [TR_METH_03000] [TR_METH_03005] [TR_METH_03006] [TR_METH_03007] [TR_METH_03008] [TR_METH_03010] |  |

一些输入需求无法（或无法完全）追溯到本文档中的单个规范项。它们由 AUTOSAR 方法论以下列方式连同其他文档一起一般性地满足：

> 17 第 [3.4.1.14](#34114-定义一致性需求) 章和第 [3.4.2.15](#34215-一致性需求) 章描绘了允许定义相应一致性需求的任务和工件。

> 18 见第 [1.6](#16-方法论概念) 章。

> 19 例如源代码见第 [3.5.2.22](#35222-基础软件模块核心源代码) 章，文档见第 [3.4.2.4](#3424-软件组件文档) 章。

## 2. 用例

下面描述构建 AUTOSAR 系统的主要用例。第 [2.1](#21-总体概览) 章给出主要开发步骤的总体简要描述。这些步骤在第 [2.2](#22-开发抽象系统描述) 章至第 [2.7](#27-为-ecu-集成软件) 章中详细阐述。此外，第 [2.8](#28-组件和服务) 章至第 [2.17](#217-如何解决名称冲突) 章描述相关的一般性主题。

### 2.1. 总体概览

#### 2.1.1. 目的

本章给出构建 AUTOSAR 系统的设计步骤的粗略概貌。主要活动描绘于图 2.8。包括相关工作产品的总体工作流见图 2.9。这些主要步骤的简要描述见下文第 [2.1.2.2](#2122-总体工作流) 节。详细描述请参见相关章节 [2.2](#22-开发抽象系统描述) 至 2.7。

#### 2.1.2. 描述

##### 2.1.2.1. 系统的视图

在 AUTOSAR 系统的开发过程中，可以存在对系统的不同视图。这允许逐步细化系统，并在开发期间专注于相关部分。

下面区分对系统的三种不同视图：








##### 2.1.2.2. 总体工作流

下面简要描述开发 AUTOSAR 系统的主要活动。第一步聚焦于抽象系统的开发，随后描述 VFB 的开发，最后是细化和进一步开发系统的活动。

> 1 见图 2.1。抽象系统描述的开发在第 [2.2](#22-开发抽象系统描述) 章中详述。

> 2 更多细节见图 2.2 和第 [2.3](#23-开发-vfb-系统描述) 章。























> 3 见图 2.3。













> 4 系统提取和 ECU 系统描述的范围见图 2.4，细节见第 [2.5.3](#253-生成系统提取) 章至第 [2.5.5](#255-设计子系统) 章。

> 5 创建 ECU 提取的活动在第 [2.5.6](#256-生成-ecu-提取) 章中进一步阐述。

> 6 更多细节见图 2.5 和第 [2.4](#24-开发软件组件) 章。




















> 7 更多细节见图 2.6 和第 [2.6](#26-开发基础软件) 章。

> 8 见图 2.7。该步骤在第 [2.7](#27-为-ecu-集成软件) 章中详述。











#### 2.1.3. 工作流





| Process Pattern | Methodology Overview |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Methodology Overview |  |  |
| Brief Description | High level view of the AUTOSAR Methodology |  |  |
| Description | This Process Patterns contains the typical activities to develop an AUTOSAR system. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Develop Application Software | 1 |  |
| Aggregates | Develop Basic Software | 1 |  |
| Aggregates | Develop Sub-System | 1 |  |
| Aggregates | Develop System | 1 |  |
| Aggregates | Develop a VFB System Description | 1 |  |
| Aggregates | Develop an Abstract System Description | 1 |  |
| Aggregates | Integrate Software for ECU | 1 |  |




### 2.2. 开发抽象系统描述

#### 2.2.1. 目的

该活动给出创建抽象系统描述的粗略概貌。

#### 2.2.2. 描述

为了本用例的目的，该活动被拆分为子活动和任务（见图 2.10），它们在第 [2.3](#23-开发-vfb-系统描述) 章和第 [2.5.2](#252-设计系统) 章中详细描述：

- 数据模型开发

- 组件模型开发

- VFB 时序开发

- 定义 VFB 顶层

- 定义 VFB 组件约束

- 设计系统

- 在 VFB 层级集成非 AUTOSAR 系统

在数据模型开发活动中，定义在整个抽象 VFB 中使用的 VFB 接口、VFB 模式和 VFB 类型的集合。请注意，这些对象也可以在后续步骤中被 VFB 和子系统 VFB 使用。

#### 2.2.3. 工作流


表2.1：开发抽象系统描述（**Develop an Abstract System Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Develop System | — |
| 简要描述 | Develop an abstract or functional view on the system. | — |
| 描述 | This activity defines an abstract view on the overall system from an abstract or functional point of view. This activity is optional. | — |
| 消费 | System Constraint Description | 0..1 In the context of the "Develop an Abstract System Description" activity, the constraints for the abstract or functional view on the system can be provided by the "System Constraint Description". |
| 消费 | VFB AUTOSAR Standard Package | 1..* |
| 产出 | Abstract System Description | 1..* |
| 聚合 | Component Model Development | 1 |
| 聚合 | Data Model Development | 1 |
| 聚合 | Define VFB Component Constraints | 1 |
| 聚合 | Define VFB Top Level | 1 |
| 聚合 | Design System | 1 In the context of the "Develop an Abstract System Description" activity, not all tasks have to be performed. |
| 聚合 | Integrate Non AUTOSAR System at VFB level | 1 |
| 聚合 | VFB Timing Development | 1 |

### 2.3. 开发 VFB 系统描述

#### 2.3.1. 目的

该活动给出创建系统虚拟功能总线视图的粗略概貌。[\[4\]](#ref-4)

#### 2.3.2. 描述

关于 VFB 概念的更多信息见 [\[6, CP EXP VFB\]](#ref-6)。关于与 VFB 相关的元模型部分的详细信息见 [\[7, CP TPS Software Component Template\]](#ref-7)。

为了本用例的目的，该活动被拆分为以下子活动：

- 数据模型开发

- 组件模型开发

- VFB 时序开发

- 在 VFB 层级集成非 AUTOSAR 系统

- 定义 VFB 安全信息

> 9 见第 [3.2.2.7](#3227-autosar-应用接口规范) 章。

可以区分两种通用方法：

- **VFB 原子应用软件组件**是核心元素。它们用于实现功能算法。

- **VFB 参数组件**用于向软件组件提供特征值，例如标定参数。

- **VFB 传感器执行器组件**提供物理传感器/执行器与 VFB 原子应用软件组件之间的连接。

- **ECU 抽象软件组件**也可以在此层级建模，以建模传感器和执行器所使用的 ECU 输入和输出接口。

- **复杂驱动程序组件**也必须在此建模，尽管它们的实现是 ECU 特定的，因为它们的端口需要在 VFB 层级连接。

- 如果应用软件通过端口访问非易失性数据，**VFB NvBlock 软件组件**可以在此层级建模。

- 如果所需解决方案的详细结构不在本活动的范围内、将留待开发后期处理，则可以提供空的 **VFB 组合组件**。

> 10 更多细节见第 [3.3.1.14](#33114-定义系统视图映射) 章。

例如，车载信息娱乐组件通常不用 AUTOSAR 手段开发。而是采用针对信息娱乐系统开发的特定需求和条件的开发方法和平台，例如 GENIVI（http://www.genivi.org/）。

这些组件集成到整体系统中的问题应尽早处理。为此，必须将非 AUTOSAR 系统的描述纳入 VFB 系统描述（**VFB 系统**）。由于非 AUTOSAR 组件通常以非 AUTOSAR 格式规定，它们的描述必须转换为相应的 AUTOSAR 格式（任务 将非 AUTOSAR 描述转换为 AUTOSAR 描述）。此外，必须纳入组件互连的信息，以获得集成系统的统一视图。

这些活动完成后，系统的虚拟功能总线视图即被定义。此时，一些 **VFB 软件组件映射约束**可能已由设计获知，或基于诸如 定义 VFB 时序 的分析获知。可以描述这些约束，为下游活动提供指导。

> 11 见第 [2.14](#214-安全扩展) 章。

#### 2.3.3. 工作流


表2.2：Define VFB Safety Information（**Define VFB Safety Information**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 | This pattern describes the methodology to develop the Virtual Functional Bus view of the System. | — |
| 描述 | The Virtual Functional Bus (VFB) view of a System shows how the Systems software and hardware functions interact independent of any network topology or deployment of features across muliple ECUs. This Activity is split into three sub-activities: • Data Model Development • Component Model Development • Timing Model Development • Integrate Non AUTOSAR System at VFB level • Define VFB Safety Information. | — |
| 消费 | Abstract System Description | 0..* The abstract System Description is an optional input for the activity "Develop a VFB System Description". The VFB-related part of the Abstract System Description can be than refined to the concrete "Overall VFB System". Additionally, a mapping between those two views can be established. |
| 消费 | VFB AUTOSAR Standard Package | 1..* |
| 产出 | Overall VFB System | 1 |
|  | Component Model Development | 1 |
| 聚合 | Data Model Development | 1 |
| 聚合 | Define System View Mapping | 1 |
| 聚合 | Define VFB Component Constraints | 1 |
| 聚合 | Define VFB Safety Information | 1 |
| 聚合 | Define VFB Top Level | 1 |
| 聚合 | Integrate Non AUTOSAR System at VFB level | 1 |
| 聚合 | VFB Timing Development | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 |  | — |
| 描述 |  | — |
| 聚合 | Define VFB Constants | 1 |
| 聚合 | Define VFB Interfaces | 1 |
| 聚合 | Define VFB Modes | 1 |
| 聚合 | Define VFB Types | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 |  | — |
| 描述 |  | — |
| 聚合 | Define Complex Driver Component | 1 |
| 聚合 | Define ECU Abstraction Component | 1 |
| 聚合 | Define VFB Application Software Component | 1 |
| 聚合 | Define VFB Composition Component | 1 |
| 聚合 | Define VFB NvBlock Software Component | 1 |
| 聚合 | Define VFB Parameter Component | 1 |
| 聚合 | Define VFB Sensor or Actuator Component | 1 |
| 聚合 | Define VFB Variants | 1 |
| 聚合 | Define Wrapper Components to Integrate Legacy Software | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 |  | — |
| 描述 |  | — |
| 聚合 | Define VFB Timing | 1 |
| 前驱 | Component Model Development | 1 |
| 前驱 | Data Model Development | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 | Incorporate the description of the non-AUTOSAR system and its connection with the AUTOSAR system into the AUTOSAR methodology activities. | — |
| 描述 | Based on the description of the non-AUTOSAR system its connection with the AUTOSAR system is defined and specified using the VFB Integration Connector format. This is translated into an AUTOSAR description that becomes part of the VFB system description. | — |
| 聚合 | Define VFB Integration Connector | 1 |
| 聚合 | Translate Non-Autosar Description to Autosar Description | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::VFB::Develop VFB | — |
| 简要描述 | Defines all required safety information at VFB level. | — |
| 描述 | In this activity, the safety information at VFB level is defined. The safety information can be refined or completed in further development phases. | — |
| 扩展 | Define Safety Information | — |
| 消费 | VFB System | 1 |
| 产出 | VFB Safety Extensions | 1 |

### 2.4. 开发软件组件

#### 2.4.1. 开发原子软件组件

##### 2.4.1.1. 目的

该活动给出创建原子软件组件的粗略概貌。

##### 2.4.1.2. 描述

注意，实现方法、质量、测试等超出了本活动的范围。

在组件实现并成功编译之后，其资源被测量并作为软件组件描述的一部分存储，供下游过程进一步使用。

该模式还包括创建时序模型、绑定预构建变体和求值变体的可选任务，都在原子软件组件的范围内。注意，这些可选任务在该活动中的顺序只是一个可能的示例。

##### 2.4.1.3. 工作流

> 12 安全方面见第 [2.14](#214-安全扩展) 章。

表2.3：Define Software Component Safety Information（**Define Software Component Safety Information**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Atomic SWC | — |
| 简要描述 |  | — |
| 描述 | This is the generic pattern valid for several kinds of Atomic Software Components. The first step is to create design, including the runnables, events, interrunnable variables, etc. Once this is complete, the contract header files can be created and the software component can be implemented. Note that the method of implementation, quality, testing, etc. are beyond the scope of this capability pattern. After the component is implemented and successfully compiled, its resources are measured and stored as part of the software component for further usage by downstream processes. The pattern also includes the optional tasks of creating a timing model, defining safety relevant information, binding prebuild-variants and evaluating variants, all in the scope of the Atomic Software Component. Note that the sequence of these optional tasks within the capability pattern is only one possible example. | — |
| 被扩展 | Develop Application Software, Develop a Complex Driver Component, Develop a Sensor Actuator Component, Develop an ECU Abstraction Component, Develop an NvBlock Software Component, Optimize a Software Component for a Specific Target | — |
| 聚合 | Compile Atomic Software Component | 1 |
| 聚合 | Define Atomic Software Component Internal Behavior | 1 |
| 聚合 | Define Consistency Needs | 1 Used for defining the consistency relations between a group of RunnableEntitys and a group of Data Prototypes. |
| 聚合 | Define Software Component Safety Information | 1 |
| 聚合 | Define Software Component Timing | 1 |
| 聚合 | Define SymbolProps for Types | 1 Used for solving name conflicts on the level of component or data types. |
| 聚合 | Evaluate Variant | 1 |
| 聚合 | Generate Atomic Software Component Contract Header Files | 1 |
| 聚合 | Generate Component Prebuild Data Set | 1 |
| 聚合 | Implement Atomic Software Component | 1 |
| 聚合 | Measure Component Resources | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Atomic SWC | — |
| 简要描述 | Defines all required safety information for a software component. | — |
| 描述 |  | — |
| 扩展 | Define Safety Information | — |
| 消费 | Overall VFB System | 1 |
| 消费 | Software Component Internal Behavior | 1 |
| 消费 | VFB Safety Extensions | 1 |
| 产出 | Software Component Safety Extensions | 1 |

#### 2.4.2. 开发应用软件

##### 2.4.2.1. 目的

该活动给出创建一个或多个应用软件组件的粗略概貌。

##### 2.4.2.2. 描述

##### 2.4.2.3. 工作流

详细工作流可以从通用活动 开发原子软件组件 派生。

表2.4：开发应用软件（**Develop Application Software**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Application SWC | — |
| 简要描述 |  | — |
| 描述 | This pattern describes the workflow and the necessary activities in terms of the AUTOSAR methodology for the development of application software components. The workflow shall allow a more or less independent development of the software component core functionality. These activities have to be performed for every application software component. | — |
| 扩展 | Develop an Atomic Software Component | — |
| 消费 | Diagnostic System Extract | 0..* The Diagnostic System Extract contains diagnostic information that serves as a requirement for the software developer. |
| 消费 | Overall VFB System | 1 The application software needs to refer to the relevant elements of the overall VFB system such as Software Component Types, Port Interfaces and Data Types. |
| 产出 | Delivered Atomic Software Components | 1..* Complete description of a set of AtomicSoftware Components including implementation (incl. source or object code files) |
| 产出 | Diagnostic System Extract | 0..* Diagnostic information relevant to the SW-Cs is provided as a part of the Diagnostic System Extract and can contain relationships to the SW-C's service needs. |

#### 2.4.3. 更专用软件组件的用例

##### 2.4.3.1. 目的

这些活动给出创建更专用组件以及软件组件的 ECU 特定优化的粗略概貌。

##### 2.4.3.2. 描述

这些活动按 AUTOSAR 方法论描述开发更专用组件（它们可能部分依赖硬件或 ECU）的工作流和必要活动。

##### 2.4.3.3. 工作流

这些工作流大部分派生自通用活动 开发原子软件组件。图示给出了所需的扩展。

注意，服务组件的开发不属于这一类用例，因为它大部分在集成期间生成。

VFB 参数组件的开发参见标定用例 2.9。

表2.5：Optimize a Software Component for a Specific Target（**Optimize a Software Component for a Specific Target**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Sensor-Actuator Component | — |
| 简要描述 | Show how to develop a Sensor Actuator Component | — |
| 描述 | Activities to develop a VFB Sensor Actuator Component, i.e. component that represents a sensor or actuator. | — |
| 扩展 | Develop an Atomic Software Component | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Ecuabs Component | — |
| 简要描述 | Show how to develop an ECU Abstraction Component. | — |
| 描述 | Activities to develop an ECU Abstraction Software Component, i.e. a component that implements an ECU Abstraction.. | — |
| 扩展 | Develop an Atomic Software Component | — |
| 聚合 | Define BSW Module Timing | 1 |
| 聚合 | Map Software Component to BSW | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop CDD Component | — |
| 简要描述 | Show how to develop a Complex Driver Component | — |
| 描述 | Show how to develop a Complex Driver Component | — |
| 扩展 | Develop an Atomic Software Component | — |
| 聚合 | Map Software Component to BSW | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Develop Block Software Component | — |
| 简要描述 |  | — |
| 描述 | Activities to develop an NvBlock Software Component. An NvBlockSoftwareComponentType (designed as part of activity Component Model Development) allows the application software to access non-volatile data in a convenient way via ports. The NvBlock Software Component takes over the management and buffering of data within blocks including data exchange with the underlying basic software (NvM). Optionally, it implements special writing strategies (e.g. cyclic writing). The development activities are similar to the generic activity Develop an Atomic Software Component with the following differences: • The description of the NvBlockNeeds within a NvBlockSoftwareComponentType is done in response to requirements given by the application software as part of their own NvBlockNeeds. These are part of their Software Component Internal Behavior which means that this level must be available when the NvBlockSoftwareComponentType is finally designed. • The creation of an Software Component Internal Behavior within NvBlockSoftwareComponent Type is optional. This artifact is only needed if special writing strategies have to implemented by the RTE or if the application software needs a direct access (via client-server ports) to the NvM. • The source code of an NvBlockSoftwareComponentType will be generated during integration as part of the artifact RTE Source Code. Therefore no source code and no Atomic Software Component Implementation needs to be created during this activity. Note that if non-volatile data are accessed by the application software via an NvBlockSoftware | — |
| 扩展 | Develop an Atomic Software Component | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::Software Component::Optimize Software Component | — |
| 简要描述 | Show how to optimize a software component for a specific target. | — |
| 描述 | In practice the integration of an application software component has to consider some optimizations to meet performance or resource requirements. The Component API might be much more efficient, if it will be generated particularly adapted to the concrete ECU configuration, e.g. via using macro definitions instead of function calls for some RTE interaction. In fact this should not change the Component Implementation (i.e. the C-sources). That means now we have a different set of component headers, which include the ECU-configuration-specific optimizations. Note: This use case shows the typical steps needed until the recompilation with the optimized header file can be done. It does not show all the other steps needed for the ECU build. | — |
| 扩展 | Develop an Atomic Software Component | — |
| 聚合 | Create Service Component | 1 |
| 聚合 | Generate Base Ecu Configuration | 1 |
| 聚合 | Generate Component Header File in Vendor Mode | 1 |
| 聚合 | Re-compile Component in ECU context | 1 Compile Atomic SWC ECU Specific: |

### 2.5. 开发系统和子系统

#### 2.5.1. 概述

##### 2.5.1.1. 目的

在系统层级开发工件的活动包括抽象系统的可选开发（见第 [2.2](#22-开发抽象系统描述) 章）、整体（技术）系统的开发，以及可选地细化为一个或多个子系统。之所以这样拆分，是因为后者可能由另一个组织完成，正如第 [2.1.2](#212-描述) 节已经指出的那样。

##### 2.5.1.2. 描述

注意，活动 生成 ECU 提取 和 定义系统安全信息 可以作为 设计系统 和 设计子系统 两者的组成部分执行。

1. 创建一个或多个所谓的系统提取，作为进一步细化为子系统的基础；

2. 或生成直接包含要在 ECU 上集成的所有相关信息的 ECU 提取。

在第一种情况下，只定义一个外层系统。基于该外层系统，可以交付一个或多个系统提取。系统提取未被完全分解，在它构成 ECU 配置的基础之前仍需要细化。为了区分交付的系统提取与细化后的子系统，一个或多个 ECU 系统描述

> 13 设计系统见图 2.24，设计子系统见图 2.25，不同系统视图之间的映射见第 [3.3.1.14](#33114-定义系统视图映射) 章。

> 14 系统提取见第 [2.5.5](#255-设计子系统) 章，ECU 提取见第 [2.5.6](#256-生成-ecu-提取) 章。

注意，基于通用交付物系统描述的所有交付物以及 ECU 提取都由 ARXML 文件组成，这些文件使用元模型元素 System 作为根元素，其他信息可以从该根元素追溯。

表2.6：Develop Sub-System（**Develop Sub-System**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Develop | — |
| 简要描述 |  | — |
| 描述 | Develop the description of an overall AUTOSAR System as a basis to deliver System and/or ECU extracts. | — |
| 消费 | Abstract System Description | 0..* The abstract System Description is an optional input for the activity "Develop System". Please note, that in this step the Abstract System Description is refined to a System Description. |
| 消费 | Overall VFB System | 0..1 Usually the System refers to elements of an overall VFB descriptions. But for the description of a legacy system, this input might be empty. |
| 消费 | System Constraint Description | 0..1 |
| 产出 | ECU Extract | 1..* |
| 产出 | System Configuration Description | 1..* |
| 产出 | System Extract | 0..* |
| 产出 | Transformer Design Bundle | 0..* |
| 聚合 | Define System Safety Information | 0..1 |
| 聚合 | Define System View Mapping | 0..1 |
| 聚合 | Design Custom Transformer | 0..* |
| 聚合 | Design System | 1 |
| 聚合 | Generate ECU Extract | 1..* |
| 聚合 | Generate System Extract | 0..* |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Develop System | — |
| 简要描述 |  | — |
| 描述 | Develop the description of a sub-system based on a given System Extract. | — |
| 消费 | System Extract | 1 |
| 产出 | ECU Extract | 1..* |
| 聚合 | Create ECU System Description | 1 |
| 聚合 | Define System Safety Information | 0..1 |
| 聚合 | Design Sub-System | 1..* |
| 聚合 | Generate ECU Extract | 1..* |

#### 2.5.2. 设计系统

##### 2.5.2.1. 目的

该活动给出通向 AUTOSAR 系统配置描述以及抽象系统描述的系统特定部分（包括其拓扑、部署、通信矩阵等）的设计步骤的粗略概貌。

##### 2.5.2.2. 描述

**注意：** 软件组件到实现的映射是可选的，只有当那些组件被特别要求用于某个 ECU 时才需要。

##### 2.5.2.3. 工作流

表2.7：Design Communication（**Design Communication**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Design System | — |
| 简要描述 | Initial work to create a topology, map a VFB onto that topology and determine the ECU resources each ECU needs. | — |
| 描述 | The design of an AUTOSAR System involves the creation of a Topology, ECU Resources Descriptions, and the interconnection between ECU instances. The software components defined within the VFB Top Level System Composition are then deployed to the ECU instances. The required network signals are identified and a mapping is done to System Signals to implement the VFB. System Signal Groups, are defined to keep certain signals grouped together for atomic transmission. System Signals are then defined and form the initial input to design the Communication Matrix. During this stage, design constraints can also be defined (Mapping of Software Components to Implementations, Mapping of Software Components to ECUs, Signal Path Constraint). These constraints serve many purposes including the ability for tools to use them to optimization a system, to interface with legacy ECUs, and to "lock" design decision between iterations. Notes: The mapping of software components to implementations is optional and needed only if those components are specifically required to be used in an ECU. | — |
| 聚合 | Assign Top Level Composition | 1 |
| 聚合 | Define ECU Description | 1 |
| 聚合 | Define Signal Path Constraints | 1 |
| 聚合 | Define System Timing | 1 |
| 聚合 | Define System Topology | 1 |
| 聚合 | Define System Variants | 1 |
| 聚合 | Deploy Software Component | 1 |
| 聚合 | Derive Communication Needs | 1 |
| 聚合 | Design Communication | 1 |
| 聚合 | Generate or Adjust System Flat Map | 1 |
| 聚合 | Select Software Component Implementation | 1 |
| 聚合 | Set System Root | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Design System | — |
| 简要描述 |  | — |
| 描述 | Describe all communication layers. and define the mapping of the triggering elements within the Physical Channels to the communication connector ports for the individual ECUs. Because the triggering elements are aggregated as splitable elements within the Physical Channels it is possible to define them in an artifact separated from the Topology. | — |
| 聚合 | Define Communication Matrix | 1 |
| 聚合 | Define E2E Transformer Technology | 1 |
| 聚合 | Define Frames | 1 |
| 聚合 | Define Network Management | 1 |
|  | Define PDU Gateway | 1 |
|  | Define RTE Fan-out | 1 |
|  | Define Secured PDUs | 1 |
| 聚合 | Define Signal Gateway | 1 |
|  | Define Signal PDUs | 1 |
| 聚合 | Define TP | 1 |
| 聚合 | Define Transformation Chain | 1 |
|  | Define Transformation Technology | 1 |

#### 2.5.3. 生成系统提取

##### 2.5.3.1. 目的

该活动为特定子系统提供系统描述的一个提取。

##### 2.5.3.2. 描述

生成一个系统提取，作为开发子系统的基础。

##### 2.5.3.3. 工作流

生成系统提取的详细任务未被建模，因为它们被视为是平凡的——只是将输入描述的内容缩减到所讨论的子系统。

表2.8：生成系统提取（**Generate System Extract**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Generate System Extract | — |
| 简要描述 |  | — |
| 描述 | Generate for further development, a System Extract which represents the description of a part of the system (sub-system). This allows a start of work on ECU's even if the system is not completely described. | — |
| 消费 | System Configuration Description | 1 |
| 产出 | System Extract | 0..* |

#### 2.5.4. 创建 ECU 系统描述

##### 2.5.4.1. 目的

基于系统提取，该活动创建 ECU 系统描述，它们在子系统的设计期间被细化。

##### 2.5.4.2. 描述

从方法论的角度来看，创建 ECU 系统描述有两种选择。

该转换步骤的典型用例是：

##### 2.5.4.3. 工作流

表2.9：创建 ECU 系统描述（**Create ECU System Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Create ECU System Description | — |
| 简要描述 |  | — |
| 描述 | During the Develop Sub-System activity the supplier refines the received System Extract so that valid ECU Extracts can be generated. The refinement of the System Extract is done using the ECU System Description. Therefore, this activity creates one or more ECU System Descriptions based on the System Extract. The sub-system artifacts are designed in the ECU System Description during the activity "Design Sub-System". From the methodological point of view there are two choices for creating the ECU System Description. 1) The System Extract is taken as the structural basis for the ECU development. In this case the System Extract becomes an ECU System Description. 2) A new structure is created as a basis for the ECU development. The newly created ECU System Description is mapped to the initial System Extract. For this purpose the task "Define System View Mapping" is performed. | — |
| 消费 | System Extract | 1 |
| 产出 | ECU System Description | 1..* |
| 聚合 | Define System View Mapping | 0..* |

#### 2.5.5. 设计子系统

##### 2.5.5.1. 目的

该活动细化给定的 ECU 系统描述（先前从交付的系统提取创建）。

##### 2.5.5.2. 描述

该步骤可能影响系统视图映射。见 [TR_METH_01078]。

最终，所得子系统范围中的所有原子软件组件都包含在该子系统描述中。

##### 2.5.5.3. 工作流

注意，ECU 系统描述同时作为该活动的输入和输出出现，因为它被细化。

由于该活动的详细工作流使用的 方法论 库元素与第 [2.5.2.3](#2523-工作流) 节所述相同，因此这里不对任务分解建模。

表2.10：设计子系统（**Design Sub-System**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Design Sub-System | — |
| 简要描述 |  | — |
| 描述 | Design the sub-system artifacts based on an ECU System Description which was previously created from the delivered ECU Extract. It consists of the same tasks as the activity Design System. The description must be completed down to the ECU level, so that valid ECU extracts can be generated. | — |
| 消费 | ECU System Description | 1 System Extract as generated from the outer system. |
| 产出 | ECU System Description | 1 System Extract refined during design of the corresponding sub-system with elements needed to generate ECU Extract(s). |

#### 2.5.6. 生成 ECU 提取

##### 2.5.6.1. 目的

该活动为特定 ECU 建立 ECU 配置提供系统描述的一个提取。

##### 2.5.6.2. 描述

生成 ECU 提取，作为建立 ECU 配置和在 ECU 层级进一步开发的基础。

##### 2.5.6.3. 工作流

表2.11：生成 ECU 提取（**Generate ECU Extract**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Generate Ecu Extract | — |
| 简要描述 | Generate the ECU Extract out of the System Description in order to be delivered for integration for further development on ECU level. | — |
| 描述 | Generate the ECU extract which is a basis for setting up the ECU configuration and further development on ECU level. It can be generated either from a full system (System Configuration Description), a System Extract or a ECU System Description. | — |
| 消费 | ECU System Description | 0..1 |
| 消费 | System Configuration Description | 0..1 |
| 消费 | System Extract | 0..1 |
| 产出 | ECU Extract | 1 |
| 聚合 | Extract ECU Rapid Prototyping Scenario | 1 |
| 聚合 | Extract ECU Topology | 1 |
| 聚合 | Extract the ECU Communication | 1 |
| 聚合 | Flatten Software Composition | 1 |
| 聚合 | Generate or Adjust ECU Flat Map | 1 |
| 前驱 | Define Rapid Prototyping Scenario | 1 |

#### 2.5.7. 设计定制转换器

##### 2.5.7.1. 目的

该活动规定用于所选系统信号序列化的转换技术的功能方面。

##### 2.5.7.2. 描述

转换器使 AUTOSAR 系统能够使用数据转换机制来线性化和变换数据。它们可以串联成转换器链，并由 RTE 对配置为需要变换的 ECU 间通信执行。

转换技术（哪种通信使用哪个转换器）在设计通信活动的上下文中定义（任务 定义转换技术）。对于通信数据的变换，可以使用标准化转换器（例如 SOME/IP 转换器）或定制转换器。

所规定的转换器随后被实现（开发基础软件），并可用于设计通信活动。在那里，ECU 间通信可以被标记为需要变换。

转换器的规范应包含：

- 转换器的功能规范。细节见 [\[10, CP ASWS Transformer General\]](#ref-10)。最重要的问题有：

  - 转换器输出的规范

  - 转换器类

  - 转换器错误

- 开发错误、生产错误和扩展生产错误的定义。

- 转换器 API

- 特定转换器需要的转换器 EcuC 扩展

##### 2.5.7.3. 工作流

表2.12：设计定制转换器（**Design Custom Transformer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Design Custom Transformer | — |
| 简要描述 |  | — |
| 描述 | In this activity the functional specification of the custom transformer module is created and the corresponding parameter definition is specified. The creation of the functional specification of the Transformer can be seen as a part of the communication design. This activity is performed only if a custom transformer for the communication is required. | — |
| 产出 | Transformer Design Bundle | 1 |
| 聚合 | Create Transformer Specification | 1 |
| 聚合 | Define Vendor Specific Module Definition | 1 |

#### 2.5.8. 定义系统安全信息

##### 2.5.8.1. 目的

该活动允许在系统层级规定安全信息。

##### 2.5.8.2. 描述

在该活动中，定义系统或子系统层级的安全信息。显然，前序开发阶段定义的安全信息被细化。（详细任务见第 [2.14](#214-安全扩展) 章。）

##### 2.5.8.3. 工作流


表2.13：定义系统安全信息（**Define System Safety Information**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::System::Develop System | — |
| 简要描述 | Defines all required safety information at system level. | — |
| 描述 | In this activity, the safety information at system level is defined. The safety information can be refined or completed in further development phases. | — |
| 扩展 | Define Safety Information | — |
| 消费 | Software Component Safety Extensions | 1 |
| 消费 | System Description | 1 |
| 消费 | VFB Safety Extensions | 1 |
| 产出 | System Safety Extensions | 1 |

### 2.6. 开发基础软件

#### 2.6.1. 概述

##### 2.6.1.1. 目的

该活动给出如何开发 AUTOSAR 基础软件的总体用例。

##### 2.6.1.2. 描述

##### 2.6.1.3. 工作流

表2.14：开发基础软件（**Develop Basic Software**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::BSW::develop_bsw | — |
| 简要描述 |  | — |
| 描述 | Describes the overall activities to develop Basic Software, starting from the design down to delivery of modules. In case of custom transformer module development, the Transformer Design Bundle containing the functional specification and the parameter definition is taken as a basis for all required activities. | — |
| 消费 | BSW Standard Package | 1 |
|  | Diagnostic System Extract | 0..* |
|  | Transformer Design Bundle | 0..* |
| 产出 | BSW Module Delivered Bundle | 1..* |
| 产出 | Diagnostic System Extract | 0..* |
|  | Design Basic Software | 1 |
|  | Develop BSW Module | 1..* |

**它由两部分组成：**

- 设计基础软件

- 开发 BSW 模块

#### 2.6.2. 设计 BSW

##### 2.6.2.1. 目的

该活动给出为一个 ECU 或一组 ECU 进行基础软件设计的粗略概貌。

##### 2.6.2.2. 描述

注意，可以复用已有的描述，尤其是标准化的描述，最终只需设置可选元素或用户特定扩展。

##### 2.6.2.3. 工作流

表2.15：Design Basic Software（**Design Basic Software**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::BSW::develop_bsw | — |
| 简要描述 | Design the Basic Software for an ECU or a set of ECUs. | — |
| 描述 | Design the Basic Software for an ECU or a set of ECUs. This shall result in a set of complete and unambiguous Basic Software Module Description. Note that existing descriptions, especially standardized ones, can be reused, eventually setting only optional elements or user specific extension. This activity is conceptually separated from the activity Develop Basic Software Module, because it might be performed by a Basic Software Designer responsible for the complete Basic Software Design on a given ECU, which may be different (in general) from the Basic Software Module Developer who develops and/or delivers the single modules. | — |
| 消费 | BSW Standard Package | 1 |
| 产出 | BSW Design Bundle | 1..* |
| 聚合 | Define BSW Entries | 1 |
| 聚合 | Define BSW Interfaces | 1 |
| 聚合 | Define BSW Types | 1 |
| 聚合 | Define Vendor Specific Module Definition | 1 |

#### 2.6.3. 开发 BSW 模块

##### 2.6.3.1. 目的

该活动给出在 ECU 集成之前单个基础软件模块或 BSW 集群开发的粗略概貌。

##### 2.6.3.2. 描述

##### 2.6.3.3. 工作流

表2.16：开发 BSW 模块（**Develop BSW Module**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::BSW::develop_bsw | — |
| 简要描述 | Develop a single BSW module or BSW cluster prior to ECU integration. | — |
| 描述 | Develop a single BSW module or BSW cluster prior to ECU integration. To develop the core code (i.e. the code not generated during integration) of a single BSW module or BSW cluster prior to ECU integration including vendor specific configuration parameters and module generators. This activity focuses on the tasks which are common for most BSW modules. It is not valid for those modules (RTE, BSW Scheduler) which are completely generated at integration time. | — |
| 消费 | BSW Design Bundle | 1..* |
| 消费 | BSW Standard Package | 1 |
| 产出 | BSW Module Delivered Bundle | 1 |
| 聚合 | Compile BSW Core Code | 1 |
| 聚合 | Define BSW Behavior | 1 |
| 聚合 | Define BSW Module Timing | 1 |
| 聚合 | Develop BSW Module Generator | 1 |
| 聚合 | Generate BSW Module Prebuild Data Set | 1 |
| 聚合 | Generate BSWM Contract Header Files | 1 |
| 聚合 | Implement a BSW Module | 1 |
| 前驱 | Design Basic Software | 1 |
| 前驱 | Design Basic Software | 1 |

### 2.7. 为 ECU 集成软件

#### 2.7.1. 描述

本章描述针对一个 EcuInstance 的集成（注意，EcuInstance 表示经典平台协议栈的单个实例化，它可以直接在物理 ECU 上运行，也可以在虚拟机监控器下运行）。

- 预编译期

- 链接期

- 后构建期

#### 2.7.2. 概述

##### 2.7.2.1. 目的

该活动展示如何为一个 ECU 集成 AUTOSAR 软件的高层视图。

##### 2.7.2.2. 描述

- 准备 ECU 配置

- 配置 BSW 和 RTE

- 生成 BSW 和 RTE

- 构建可执行文件

ECU 配置在为一个 ECU 集成软件的过程中扮演重要角色。相关工作流描绘于图 2.42。全部三个活动（准备 ECU 配置、配置 BSW 和 RTE、生成 BSW 和 RTE）都使用工作产品 ECU 配置值，它包含（即引用）ECU 上所有 BSW 模块的所有配置信息。为了更好地理解这三个不同的活动，第 [2.7.9](#279-配置类) 章给出了配置类的介绍。

可以测量各种 BSW 模块和应用所使用的资源，并将该信息保存在基础软件模块实现描述或原子软件组件实现中。

此时还可以通过执行 生成 A2L 任务来生成 A2L 文件。

###### 2.7.2.2.1. ECU 配置的输入

> 15 为了更易于理解，该图隐藏了活动 生成 BSW 和 RTE 的一些输出。更多细节见所有聚合任务的输出。

后者在 [\[11, CP TPS BSW Module Description Template\]](#ref-11) 中更详细地描述。ECU 提取的概念描绘如下：

**ECU 提取**

只有生成了合理的系统配置描述和相应的 ECU 提取之后，才能开始 ECU 配置（见图 2.42）。系统配置描述的细节见 [\[8, CP TPS System Template\]](#ref-8)。

系统配置描述包含所有相关的系统级配置，例如

- 系统中存在的 ECU

- 互连这些 ECU 的通信系统及其配置

- 这些通信系统的通信矩阵（发送和接收的帧）

- 软件组件的定义，包括它们的端口、接口和连接（在 SWC 描述中定义，并在系统配置描述中引用）。

- SWC 到 ECU 的映射

ECU 提取是与系统配置描述格式相同的描述，但只包含与一个特定 ECU 的配置相关的元素。

###### 2.7.2.2.2. ECU 配置值描述

ECU 提取只定义必须在 ECU 之间达成一致的配置元素。为了生成可在 ECU 上运行的可执行文件，必须提供多得多的配置信息。

配置的其余部分是配置 ECU 内的所有 BSW 模块。ECU 内典型的 BSW 模块可以是：RTE、Com、Can、OS、NVRAM 等。配置 ECU 时还要考虑 BSW 模块之间的依赖关系。

> 16 见图 2.42。

配置完成后，进行配置数据的生成。即该过程既涉及配置编辑器，也涉及配置生成器。

为了获得 ECU 整体配置内部的一致性，AUTOSAR 定义了一种单一格式——ECU 配置值描述，用于 ECU 内的所有 BSW 模块。配置编辑器和配置生成器都面向 ECU 配置值描述工作。在 AUTOSAR 方法论中，ECU 配置值描述由工件 ECU 配置值 表示。

##### 2.7.2.3. 工作流

表2.17：为 ECU 集成软件（**Integrate Software for ECU**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 |  | — |
| 描述 | This activity contains all typical sub-activities required to integrate the software components and modules on an EcuInstance. ECU in this context means ECUInstance, one "ECU Delivered" will be needed for each ECUInstance. | — |
| 消费 | BSW Module Delivered Bundle | 1..* |
| 消费 | Delivered Atomic Software Components | 1..* |
| 消费 | Diagnostic ECU Extract | 0..1 complete DE: |
| 消费 | ECU Extract | 1 |
| 产出 | ECU Software Delivered | 1 |
| 聚合 | Build Executable | 1 |
| 聚合 | Configure BSW and RTE | 1 |
| 聚合 | Generate BSW and RTE | 1 |
| 聚合 | Model ECU Timing | 1 |
| 聚合 | Prepare ECU Configuration | 1 |
| 聚合 | Update ECU Configuration | 1 |

#### 2.7.3. 准备 ECU 配置

##### 2.7.3.1. 描述

构建基础 ECU 配置值描述时必须遵循的规则见 [\[12\]](#ref-12) 第 4.2 章。

##### 2.7.3.2. 工作流

表2.18：准备 ECU 配置（**Prepare ECU Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 |  | — |
| 描述 | Initial actions required to create the initial ECU Configuration. | — |
| 消费 | BSW Module Delivered Bundle | 1..* |
| 消费 | Diagnostic ECU Extract | 0..1 |
| 消费 | ECU Extract | 1 |
| 产出 | ECU Configuration Values | 1 |
| 聚合 | Define Integration Variant | 1 |
| 聚合 | Generate Base Ecu Configuration | 1 |
| 前驱 | Refine Rapid Prototyping Scenario | 1 |

#### 2.7.4. 配置 BSW 和 RTE

##### 2.7.4.1. 描述

方法论不规定这些配置步骤的特定顺序。由一个活动产生的 ECU 配置描述（例如 ECU 配置值）可以被另一个活动读取（例如 配置 RTE 生成一个描述，而 配置 Com 读取它）。通常，BSW 模块（例如 COM 和 OS）的配置活动读写 ECU 配置。

##### 2.7.4.2. 工作流

表2.19：配置 BSW 和 RTE（**Configure BSW and RTE**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 |  | — |
| 描述 | All the tasks used to configure the Basic Software Modules on an ECU. | — |
| 聚合 | Configure Com | 1 |
| 聚合 | Configure Diagnostics | 1 |
| 聚合 | Configure ECUC | 1 |
| 聚合 | Configure IO Hardware abstraction | 1 |
| 聚合 | Configure MCAL | 1 |
| 聚合 | Configure Memmap Allocation | 1 |
| 聚合 | Configure Mode Management | 1 |
| 聚合 | Configure NvM | 1 Since the configuration of the DEM usually has impact on the data to be stored in NvM, the task Configure Diagnostics is assumed to precede the task Configure NvM. |
| 聚合 | Configure OS | 1 |
| 聚合 | Configure RTE | 1 |
| 聚合 | Configure Transformer | 1 |
| 聚合 | Configure Watchdog Manager | 1 |
| 聚合 | Connect Service Component | 1 |
| 聚合 | Create Service Component | 1 |
| 前驱 | Prepare ECU Configuration | 1 |
| 输入/输出 | ECU Configuration Values | 1 |

#### 2.7.5. 更新 ECU 配置

##### 2.7.5.1. 描述

在后构建场景中，最终生成两个可加载文件——一个包含应用软件、基础软件以及基础软件的预编译和链接期配置（称为 ECU 可执行文件），另一个只包含基础软件的后构建期配置（可加载到 ECU 内存的 BSW 模块配置数据）。这两个可加载文件代表初始配置。该初始配置可以在后构建期通过生成两个新的可加载文件来更新。在此更新中，ECU 可执行文件不被修改。

##### 2.7.5.2. 工作流


表2.20：更新 ECU 配置（**Update ECU Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 | Tasks required to create the updated ECU Configuration. | — |
| 描述 | Tasks required to create the updated ECU Configuration. | — |
| 消费 | Diagnostic ECU Extract | 0..1 |
| 消费 | ECU Extract | 1 |
| 聚合 | Define Integration Variant | 1 |
| 聚合 | Generate Updated ECU Configuration | 1 |

#### 2.7.6. 为 ECU 建模时序

##### 2.7.6.1. 工作流

表2.21：为 ECU 建模时序（**Model ECU Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 |  | — |
| 描述 | ECU timing model depends on ECU configuration data (BSW and RTE) but the result of the ECU timing model shall help to optimize ECU configuration. The relation between "Configure BSW and RTE" and "Model ECU Timing" must be seen as an iterative work. | — |
| 聚合 | Define ECU Timing | 1 |
| 前驱 | Configure BSW and RTE | 1 |

#### 2.7.7. 生成 BSW 和 RTE

##### 2.7.7.1. 描述

生成是将裁剪后的 ECU 配置值描述应用于软件模块的过程。它可以以不同方式执行，取决于为不同模块选择的配置类（见 2.7.9），也取决于实现者的选择。

对于每个 BSW 模块，生成器从 ECU 配置值描述中读取相关参数，并创建实现所规定配置的代码。

在该生成步骤中，ECU 配置值描述的抽象参数被转换为适合相应软件模块实现的硬件和实现特定的数据结构。AUTOSAR 方法论规范不详细规定生成器工具。

不过，假定生成器对其生成所需的配置部分执行错误、一致性和完整性检查。

为特定模块生成代码时，如果配置了 ARTI，生成器还应导出 ARTI 信息。ARTI 导出应包含用于调试 AUTOSAR 模块以及通过 ARTI 钩子宏进行跟踪的信息，如该模块相应的 SWS 文档所定义。

如果配置了 ARTI 跟踪，则在构建可执行文件之前，跟踪工具会提供一个附加的 ARTI 源文件（arti.c），并且应将其包含在构建中。

关于配置数据的生成，存在一些替代方法。更多细节见 [\[12, CP TPS ECU Configuration\]](#ref-12) 的第 A.[1.2](#12-文档约定) 章。

##### 2.7.7.2. 工作流


表2.22：生成 BSW 和 RTE（**Generate BSW and RTE**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 | High Level view showing how to build software for an EcuInstance. | — |
| 描述 | High Level view showing how to build software for an EcuInstance. | — |
| 消费 | ECU Configuration Values | 1 |
| 产出 | BSW Module Configuration Data Source Code | 1 |
| 产出 | BSW Module Configuration Header File | 1 |
| 产出 | RTE Source Code | 1 |
| 聚合 | Generate BSW Configuration Code | 1 |
| 聚合 | Generate BSW Memory Mapping Header | 1 |
| 聚合 | Generate Local MC Data Support | 1 |
| 聚合 | Generate OS | 1 |
| 聚合 | Generate RTE | 1 |
| 聚合 | Generate RTE Prebuild Dataset | 1 |
| 聚合 | Generate SWC Memory Mapping Header | 1 |
| 前驱 | Configure BSW and RTE | 1 |

#### 2.7.8. 构建可执行文件

##### 2.7.8.1. 描述

> 17 各种编译和链接选项的细节在第 [2.7.9.1](#2791-配置类预编译期)、2.7.9.2、[2.7.9.3](#2793-配置类后构建期) 和 [2.7.9.4](#2794-配置类中不同后构建变体的处理) 章中解释。

##### 2.7.8.2. 工作流

表2.23：构建可执行文件（**Build Executable**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Integrate Software for ECU | — |
| 简要描述 |  | — |
| 描述 | Describes how to build one executable and related artifacts (A2L file) starting from the source code (and delivered object code). | — |
| 聚合 | Compile ECU Source Code | 1 |
| 聚合 | Generate A2L | 1 |
| 聚合 | Generate ECU Executable | 1 |
| 聚合 | Generate RTE Postbuild Dataset | 1 |
| 聚合 | Measure Resources | 1 |
| 前驱 | Generate BSW and RTE | 1 |

#### 2.7.9. 配置类

BSW 模块的开发涉及以下开发周期：编译、链接以及将可执行文件下载到 ECU 内存。参数配置可以在这些流程步骤中的任何一个中进行：预编译期、链接期甚至后构建期。

根据执行参数配置的流程步骤，配置类分类如下

- 预编译期

- 链接期

- 后构建期

不同流程步骤中的配置对 ECU 配置参数的处理有一定影响。如果一个配置参数被定义为预编译期，则编译之后该配置参数不能再更改。

而如果一个配置参数被定义为后构建期，则该配置参数必须存储在一个已知的内存位置。此外，BSW 模块的交付格式决定了参数以何种方式可变。BSW 模块的源代码交付或目标代码交付在配置方面具有不同的自由度。

参数的配置类取决于其所属 BSW 模块所选的实现变体。然而，一旦模块被实现，每个参数的配置类就固定了。为模块选择正确的实现变体取决于应用类型以及模块实现者所作的设计决策。

不同的配置类可以在一个模块内组合。例如，对于后构建期可配置的 BSW 实现，可能只有参数的一个子集可在后构建期配置。一些参数可能被配置为预编译期或链接期。

用于描述配置类的文件格式：

- .arxml（AUTOSAR 标准化的 xml 文件。）

- .exe（可下载到 ECU 的可执行文件。）

- .hex（可下载到 ECU 的二进制文件，但它不能自行执行。）

- .c（包含源代码或配置数据的 C 源文件。）

- .h（用于源代码或配置数据的头文件。）

- .obj（用于源代码或配置数据的目标文件。）

##### 2.7.9.1. 配置类：预编译期

###### 2.7.9.1.1. 描述

工作分解结构展示了两种方法：

不过，BSW 模块配置源文件（即 BSW 模块配置头文件和 BSW 模块配置数据源代码，另见图 2.55）仍然可以生成。这允许生成不同的

源文件内的 C 结构，以支持预编译配置可以包含未解析的后构建期变体点的用例。

两种方法同样有效。

只要参数值的决定必须在其他依赖参数的选择之前作出，预编译期配置就是正确的选择。例如，CRC 初始校验和参数的算法选择基于 CRC 类型（CRC16 或 CRC32）的选择。选择 CRC16 时，处理时间增加但内存使用减少；而选择 CRC32 时，处理时间减少但内存使用增加。正确的选择应由实现者根据需求和资源可用性在源代码编译之前作出。

可以采用预编译期配置的示例情形有：

- 配置 NVRAM 管理器的内存表和块描述符表的数量。

- 为软件模块的开发错误跟踪启用宏。

###### 2.7.9.1.2. 工作流


PreCompile 绑定时间的进一步描述见第 [2.16.3.6](#21636-precompiletime) 节。

表2.24：Do Pre Compile Configuration（**Do Pre Compile Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Pre Compile Conf | — |
| 简要描述 |  | — |
| 描述 | [from ecuc sws 1031] This type of configuration is a standalone configuration done before compiling the source code. That means parameter values for those configurable elements are defined before compiling and will be effective after compilation time. The value of the configurable parameter is decided in an earlier stage of software development process and any changes in the parameter value calls for a re-compilation. The contents of pre-compile time parameters cannot be changed at the subsequent development steps like link time or post-build time. | — |
| 聚合 | Compile Configured BSW | 1 |
| 聚合 | Compile Generated BSW | 1 |
| 聚合 | Generate BSW Precompile Configuration Header | 1 |
| 聚合 | Generate BSW Source Code | 1 |
| 聚合 | Link ECU Code after Precompile Configuration | 1 |

##### 2.7.9.2. 配置类：链接期

###### 2.7.9.2.1. 描述

该配置类为配置过程提供了一种模块化方法。一个单独的模块将处理配置细节，这些参数值将在链接过程中提供给其他模块。

可以采用链接期配置的示例情形有：

- 信号的初始值和无效值

- 为网络管理的相应实例配置的唯一通道标识符。

- CAN 网络的逻辑句柄。

- 硬件接收句柄和硬件发送的标识符和类型

- CAN 接口的句柄。

- ComFilterAlgorithm 的定义。

- 用于向 RTE 指示已失效信号接收的 COM 回调函数。

###### 2.7.9.2.2. 工作流

LinkTime 绑定时间的进一步描述见第 [2.16.3.8](#21638-linktime) 节。

表2.25：Do Link Time Configuration（**Do Link Time Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Link Time Conf | — |
| 简要描述 |  | — |
| 描述 | [from ecuc sws 1032] This type of configuration is done for the BSW module during link time. That means the object code of the BSW module receives parts of its configuration from another object code file or it is defined by linker options. Link time parameters are typically used when delivering object code to the integrator. | — |
| 聚合 | Compile BSW Configuration Data | 1 |
| 聚合 | Compile Unconfigured BSW | 1 |
| 聚合 | Generate BSW Configuration Code | 1 |
| 聚合 | Link ECU Code during Link Time Configuration | 1 |

##### 2.7.9.3. 配置类：后构建期

###### 2.7.9.3.1. 描述

后构建配置的生成是一个可以多次执行的过程。第一次是在创建初始 ECU 配置期间执行的，其中包括生成 ECU 可执行文件和可加载到 ECU 内存的 BSW 模块配置数据两个二进制文件。该方法见图 2.55。此后，可以按图 2.56 所示的过程，根据需要多次独立于 ECU 可执行文件更新后构建配置（更新通常源自 ECU 提取）。

可以采用后构建期配置的示例情形有：

- CAN 帧的标识符

- CAN 驱动程序波特率和传播延迟

- COM 传输模式、传输模式时间偏移和时间周期

- 启用/禁用信号传输

- 帧打包

- 信号网关

- LIN/FlexRay 调度表

###### 2.7.9.3.2. 工作流

PostBuild 绑定时间的进一步描述见第 [2.16.3.9](#21639-postbuild) 节。

表2.26：Do Post Build Configuration（**Do Post Build Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::ECU::Post Build Conf | — |
| 简要描述 |  | — |
| 描述 | [from ecuc sws 4006] This type of configuration is possible after building the BSW module or the ECU software. The BSW module gets the parameters of its configuration by downloading a separate file to the ECU memory, avoiding a re-compilation and re-build of the BSW module. | — |
| 聚合 | Compile BSW Configuration Data | 1 |
| 聚合 | Compile Unconfigured BSW | 1 |
| 聚合 | Generate BSW Postbuild Configuration Code | 1 |
| 聚合 | Generate ECU Executable | 1 |
| 聚合 | Link ECU Code during Post-Build Time | 1 |

##### 2.7.9.4. 配置类中不同后构建变体的处理

###### 2.7.9.4.1. 描述

### 2.8. 组件和服务

#### 2.8.1. 目的

本用例聚焦于使用和配置 AUTOSAR 服务所需的活动。因此它是总体用例的一个子集（见 2.1）。

> 18 这可以不考虑配置类地进行，如图 2.51、图 2.53 和图 2.55 中的注释所示。

#### 2.8.2. 描述

- 在 ECU 集成期间要连接到服务的端口（这是 定义 VFB 应用软件组件 的子任务）。用于服务端口的端口接口应是标准化的。

- 从单个软件组件的角度配置服务的需求（例如 NVM 块或诊断事件的符号名称）（这是 定义原子软件组件内部行为 的子任务。）

服务端口与任何其他端口一样会影响组件 API，因此在 API 生成方面，服务端口和 "普通" 端口没有区别。

当应用软件组件被映射到一个 ECU 时，它们的描述被放入相应的 ECU 提取中。这些活动属于系统域（见 2.5.6），未在本用例中显式展示。

作为 ECU 集成的一部分，会生成附加的工件以通过 RTE 连接服务端口：服务组件描述，包括它们到基础软件模块的映射，以及它们的端口与应用软件组件的服务端口之间的连接器。

本用例还展示了创建相应基础软件模块（例如 DEM、DCM、看门狗管理器等）的 ECU 配置。这必须针对连接到相应服务组件的所有应用软件组件的服务端口和服务需求来进行（图中仅以诊断的配置活动为例）。

#### 2.8.3. 工作流

| Process Pattern | Components and Services |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Components and Services |  |  |
| Brief Description | This use case focuses on the activities required to use and configure AUTOSAR Services. It is therefore a subset of the overall use case (Methodology Overview). |  |  |
| Process Pattern | Components and Services |  |  |
| Description | Atomic Software Components can use AUTOSAR Services. In order to do so, two things have to be defined: The ports which are to be connected to the Service during ECU integration and in addition the needs to configure the Service (for example NvM blocks or symbolic names for diagnostic events) from the perspecive of the single Software Component. The service ports have impact on the component API just like any other port, so there is no difference between service ports and "normal" ports with respect to API generation. Afterwards the Application Software Components are mapped to an ECU and their description is put into the corresponding ECU extract (deliverable Complete ECU Description). These activities belong to the system domain and are not explictly shown in this use case (see Methodology Overview). As part of the ECU integration, additional artifacts are generated to connect the service ports over the RTE: Service Component Descriptions, including their mapping to the Basic Software Modules, and the connectors between their ports and the service ports of the Appplication Software Components. The ECU configuration of the Basic Software Module (e.g. DEM, DCM, Watchdog Manager etc.) is then created with respect to the service ports and the SeviceNeeds of the Application Software Components connected to that Service. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Add Service Ports and Service Needs | 1 |  |
| Aggregates | Connect and Configure Service Module on ECU | 1 |  |
| Activity | Add Service Ports and Service Needs |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Components and Services |  |  |
| Brief Description |  |  |  |
| Description | Atomic Software Components can use AUTOSAR Services. In order to do so, two things have to be defined: • The ports which are to be connected to the Service during ECU integration (this is a sub-task of Define VFB Application Software Component). The port interfaces used for service ports should be standardized. • The needs to configure the Service (for example NvM blocks or symbolic names for diagnostic events) from the perspecive of the single Software Component (this is a sub-task of Define Atomic Software Component Internal Behavior) The service ports have impact on the component API just like any other port, so there is no difference between service ports and "normal" ports with respect to API generation. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Activity | Add Service Ports and Service Needs |  |  |
| Aggregates | Define Atomic Software Component Internal Behavior | 1 | Add Service Needs to Atomic Component: |
| Aggregates | Define VFB Application Software Component | 1 | Add Service Ports to Atomic Software Component: |
| Aggregates | Generate Atomic Software Component Contract Header Files | 1 | Re-generate Contract Header Files with Service Intefaces: |
| Aggregates | Implement Atomic Software Component | 1 | Re-Implement Atomic Software Component with Service Ports: |
| Activity | Connect and Configure Service Module on ECU |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Components and Services |  |  |
| Brief Description |  |  |  |
| Description | As part of the ECU integration, additional artifacts are generated to connect the service ports over the RTE: Service Component Descriptions, including their mapping to the Basic Software Modules, and the connectors between their ports and the service ports of the Appplication Software Components. The ECU configuration of the Basic Software Module (e.g. DEM, DCM, Watchdog Manager etc.) is then created with respect to the service ports and the SeviceNeeds of the Application Software Components connected to that Service (the diagram shows only the configuration activity of diagnostics as an example). The code gneration of the service module (e.g. DEM, DCM) and of the RTE is shown for completeness. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Create Service Component | 1 |  |
| Aggregates | Generate BSW Source Code | 1 |  |
| Aggregates | Generate Base Ecu Configuration | 1 |  |
| Aggregates | Generate RTE | 1 |  |
| Predecessor | Add Service Ports and Service Needs | 1 |  |

### 2.9. 标定概述

#### 2.9.1. 目的

本用例描述从标定参数的创建或更新到 A2L 文件的创建或更新所需的典型活动。

#### 2.9.2. 描述

本用例假定标定参数是在一个已有系统中更改的，因此省略了定义和构建新系统所需的任务，只显示与标定相关的步骤。

此外，本用例包括更新一组标定参数值作为 RTE 输入的（可选）任务。

就 AUTOSAR 工件而言，本用例可以划分为四个主要活动：

#### 2.9.3. 工作流

| Process Pattern | Calibration Overview |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Calibration Overview |  |  |
| Brief Description | Describe the required steps to update the calibrations data down to an update of the A2L files. |  |  |
| Description | This use case shows the typical steps required from an updated design of calibration data down to an update of the A2L file. The use cases assumes, that calibration parameters are changed in an already existing system, thus the steps required to define and build a new system are omitted, only the calibration relevant steps are shown. In addition, the use case includes the (optional) task of updating a set of calibration parameter values as input for the RTE. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Define Cross-component Calibration Parameters | 1 |  |
| Aggregates | Define Local Calibration Parameters | 1 |  |
| Aggregates | Generate A2L | 1 |  |
| Aggregates | Generate ECU Executable | 1 |  |
| Aggregates | Provide Unique Parameter Names | 1 |  |
| Aggregates | Re-generate RTE and Calibration Support | 1 |  |
| Activity | Define Cross-component Calibration Parameters |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Calibration Overview |  |  |
| Brief Description |  |  |  |
| Description | Contains the tasks used to define or update cross-component calibration parameters. These parameters are provided by Parameter Components. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Define VFB Composition Component | 1 |  |
| Aggregates | Define VFB Interfaces | 1 |  |
| Aggregates | Define VFB Parameter Component | 1 |  |
| Aggregates | Define VFB Types | 1 | Define VFB Types for Parameter Interfaces: Use this task to define VFB Types for Parameter Interfaces |
| Activity | Define Local Calibration Parameters |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Calibration Overview |  |  |
| Brief Description |  |  |  |
| Description | Contains the tasks used to define or update component-local (or module-local) calibration parameters. These parameters are declared within the Internal Behavior of the component (or BSW module) which uses them. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Define Atomic Software Component Internal Behavior | 1 | Define Calibration Parameters in Internal Behavior: Use this task to define local calibration parameters as part of the Internal Behavior of a software component. |
| Aggregates | Define BSW Behavior | 1 | Define local Calibration Parameters in BSW: Use this task to define local calibration parameters as part of the Internal Behavior of a BSW module. |
| Aggregates | Define Partial Flat Map | 1 | Define (optionally) a Partial Flat Map for one or more delivered components. |
| Activity | Provide Unique Parameter Names |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Calibration Overview |  |  |
| Brief Description |  |  |  |
| Description | Contains the tasks used to provide unique names for calibration parameters. A Flat Map is used to provide unique names for MCD tools. An Alias Name Set can be provided in cases, where this is not sufficient. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Define Alias Names | 1 |  |
| Aggregates | Generate ECU Extract | 1 | Use this activity to update the ECU Extract. This includes updating the ECU Flat Map if parameter names on ECU level have changed. |
| Aggregates | Generate or Adjust System Flat Map | 1 | Use this task if parameter names are defined on system level. |
| Predecessor | Define Cross-component Calibration Parameters | 1 |  |
| Predecessor | Define Local Calibration Parameters | 1 |  |
| Activity | Re-generate RTE and Calibration Support |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Calibration Overview |  |  |
| Brief Description |  |  |  |
| Description | Contains the tasks used to re-generate relevant artifacts during ECU integration (before the final build) after an update of calibration parameters. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Create MC Function Model | 1 | This use case shows the creation of an MC Function Model as part of the activity that generates also the RTE and calibration support data. This is only one possibility. It is also possible to create an MC Function Model earlier in the process (as part of the design activities) or later (shortly before the A2L is generated). |
| Activity | Re-generate RTE and Calibration Support |  |  |
| Aggregates | Generate BSW Configuration Code | 1 | Use this task to generate the description of calibration parameters in BSW that are a result of ECU configuration. Such parameters will be described within the artifact BSW Module Behavior Extension. |
| Aggregates | Generate Local MC Data Support | 1 | Use this task to generate support for calibration data that are not handled via the RTE. |
| Aggregates | Generate RTE | 1 | Use this task to generate support for calibration data that are handled over the RTE. This includes cross-component calibration as well as local calibration (in SWC and BSW) that needs emulation support by the RTE. |
| Aggregates | Provide RTE Calibration Dataset | 1 |  |
| Predecessor | Provide Unique Parameter Names | 1 |  |

### 2.10. 内存映射

#### 2.10.1. 目的

本用例全面展示了定义、配置和生成内存映射头文件所需的任务。其底层概念在 [\[13, CP SWS Memory Mapping\]](#ref-13) 中规定。

#### 2.10.2. 描述

借助 AUTOSAR，可以从 XML 工件派生（即生成）这些头文件的内容。本用例展示所需的工件和任务之间的关系。

#### 2.10.3. 工作流

注意，本用例以代码的编译结束。内存段到实际硬件的指派（通常通过链接器的配置完成）目前不被视为 AUTOSAR 方法论的一部分。



表2.27：Memory Mapping Overview（**Memory Mapping Overview**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Memory Mapping Overview | — |
| 简要描述 |  | — |
| 描述 | Overview of the work sequence for defining and configuration of memory sections. | — |
| 聚合 | Compile Atomic Software Component | 1 |
| 聚合 | Compile BSW Core Code | 1 |
| 聚合 | Compile ECU Source Code | 1 |
| 聚合 | Configure Memmap Allocation | 1 |
| 聚合 | Define Memory Addressing Modes | 1 |
| 聚合 | Generate BSW Memory Mapping Header | 1 |
| 聚合 | Generate SWC Memory Mapping Header | 1 |

### 2.11. E2E 保护

#### 2.11.1. 目的

该活动给出创建 E2E 保护以保护 AUTOSAR 架构中通信流的粗略概貌。[\[14\]](#ref-14)

#### 2.11.2. 描述

当安全相关的数据交换需要在运行时受到保护以抵御通信链路故障时，需要 E2E 保护机制。

#### 2.11.3. 工作流

### 2.12. 诊断提取

#### 2.12.1. 目的

本用例给出使用诊断提取模板 [\[15, CP TPS Diagnostic Extract Template\]](#ref-15) 进行诊断配置的粗略概貌。相关活动和交付物将根据现场经验在后续 AUTOSAR 发布版中细化。

#### 2.12.2. 描述

AUTOSAR 开发的分布式特性要求以优化的方式采集信息。特别是，诊断信息（即 DEM 和 DCM 配置）应由掌握最完整知识的人只采集一次，因此比某个集中式个人更能承担责任。ECU 配置不适合在 ECU 开发项目的伙伴之间交换。因此，AUTOSAR 定义了诊断提取模板，它代表诊断功能的标准化交换格式。诊断提取模板允许诊断方面的分散式配置。诊断提取模板的基本用法是在诊断开发过程中所涉及的不同参与方之间交换诊断数据，以便配置 DCM 和 DEM，并提供相应应用接口的描述以实现诊断服务和故障处理。在 AUTOSAR 方法论中，诊断提取

由交付物诊断提取及其子交付物表示。（注：源文档此处跨页断行，两句合并译出。）

- 诊断服务（例如 IOControl、MemoryByAddress）

- 诊断事件处理（例如事件、故障码、条件）

- 映射（服务映射、诊断映射等）

- 诊断抽象系统描述：该交付物表示一个高层定义，可以作为创建具体诊断系统提取或诊断 ECU 提取的模板。

- 诊断系统提取：该交付物表示多个 ECU 的诊断方面。

- 诊断 ECU 提取：该交付物表示单个 ECU 的诊断方面。

- 元素分离到多个物理文件：诊断提取模板的大多数元素可以拆分到多个物理文件。因此，这些元素的部分（例如某些属性）可以由例如 OEM 定义，而这些元素的其他部分由例如 ECU 供应商定义。

- 自包含映射的使用：许多诊断需求通过诊断元素之间的映射建立（例如 DTC 到 DemEvent 的映射）。然而，“分散式配置”方法要求这些映射能够在 ECU 开发过程中的几乎任何时间由任何所涉及的公司（ respective 角色）灵活定义。因此，

诊断提取模板定义了自包含的映射元素，这些元素引用两个（或可能更多）诊断元素来定义映射。诊断提取模板的使用将在后续 AUTOSAR 发布版中通过“角色和权限”概念的适当应用加以限制。

- 定义 DTC 的值

- 定义 ECU 支持的 UDS 服务和子服务

- 定义应用开发者实现的特定组合所需的事件

- 定义必须由特定 SW-C 实现的特定 ReadDataByIdentifier 的内容

- 定义某个 SW-C 所需的事件

另一方面，应用开发者可以作为诊断系统提取的一部分和/或使用服务需求来提供与 SW-C 相关的诊断信息。SW-C 描述中的服务需求仍然是

> 19 见图 2.66。

由于 AUTOSAR 方法论不限制在活动 集成诊断信息 中对 DID、UDS 服务的参数、事件、会话等元素的定义，集成者必须确保合并后完整信息仍然有效。通常，可以执行以下任务：

- DTC（诊断故障码）到事件的映射

- 事件的合并

- 服务的映射

在集成活动期间，可以考虑以下问题和冲突：

- 一些 DTC 可能已经映射到事件——特别是在两者来自同一方的情况下。但如果 DTC 由 OEM 定义，而软件组件由作为应用开发者的其他供应商实现，则集成者必须确保两者被映射在一起。

- 在某些情况下，一个诊断事件可能被多次定义。诊断请求者定义应由应用开发者实现的事件。一个供应商实现一个将在多个项目中使用的软件组件，该组件也检测这种类型的错误并定义了相同的事件。两个事件可能命名不同但含义相同。集成者必须在集成期间检测到这种冗余并将它们合并在一起。

- 诊断请求者需要一个特定的 ReadDataByIdentifier，而应用开发者实现它。如果实现只针对一个特定项目进行，应用开发者可以将诊断请求者的 DID 映射到其软件组件中已定义的作业。在应用开发者实现通用诊断作业的其他情况下，合并该信息并将作业映射到相应 DID 将是诊断集成者的任务。

在所有问题和冲突得到解决并且输入被合并之后，生成最终完整的诊断 ECU 提取。基于该交付物，生成相关基础软件模块的初始

配置（活动 为 ECU 集成软件）。

#### 2.12.3. 工作流


| Process Pattern | Diagnostic Extract Overview |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Diagnostic Extract Overview |  |  |
| Brief Description |  |  |  |
| Description |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Develop Application Software | 1 |  |
| Aggregates | Develop Basic Software | 1 |  |
| Aggregates | Develop Diagnostic Abstract System Description | 1 |  |
| Aggregates | Develop Diagnostic Requirements | 1 |  |
| Process Pattern | Diagnostic Extract Overview |  |  |
| Aggregates | Integrate Diagnostic Information | 1 |  |
| Aggregates | Integrate Software for ECU | 1 |  |
| Activity | Develop Diagnostic Abstract System Description |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Diagnostic Extract Overview |  |  |
| Brief Description |  |  |  |
| Description | This activity defines diagnostic requirements at functional/abstract level. The resulting Diagnostic Abstract System Description may be used by the following activity as a basis for the Diagnostic System Extract or the Diagnostic ECU Extract. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produces | Diagnostic Abstract System Description | 1 |  |
| Activity | Develop Diagnostic Requirements |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Diagnostic Extract Overview |  |  |
| Brief Description |  |  |  |
| Description | In this activity the OEM or diagnostic requirer defines the diagnostic interfaces of one or multiple ECUs. It may also define some InternalBehaviors as requirements for the ECU-Supplier or application developer. The following tasks may be relevant: • Define the values of the DTCs • Define the UDS services and sub-services supported by the ECUs • Define the required events needed by a specific composition Additionally, the OEM may also collect Diagnostic Extracts from different departments as well as from SW-C developers and merge the information into one Diagnostic Extract. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Consumes | Diagnostic System Extract | 0..* |  |
| Produces | Diagnostic ECU Extract | 0..* |  |
| Produces | Diagnostic System Extract | 0..* |  |
|  | Diagnostic Abstract System Description | 0..* |  |
| Activity | Integrate Diagnostic Information |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Diagnostic Extract Overview |  |  |
| Brief Description |  |  |  |
| Description | The main goal of this activity is to integrate all parts of the Diagnostic Description received from the OEM and from the application developer. Based on the complete Diagnostic Extract the initial ECUC can be generated. |  |  |
| Activity | Integrate Diagnostic Information |  |  |
| Relation Type | Related Element | Mult. | Note |
| Consumes | Diagnostic ECU Extract | 0..* | partially filled DE: |
| Consumes | Diagnostic System Extract | 0..* |  |
| Produces | Diagnostic ECU Extract | 1..* | complete DE: |

### 2.13. 快速原型

#### 2.13.1. 目的

本用例描述在 AUTOSAR 中启用快速原型的常见活动。

#### 2.13.2. 描述

快速原型可在电子控制单元开发期间用于评估和测试各种功能的新软件控制算法。

使用 Fullpass（全通过）技术时，原始 ECU 被快速原型单元（RPU）完全取代。使用旁路（**Bypass**）技术时，原始 ECU 和软件保持在控制回路中以支持大多数控制算法并与传感器、执行器和通信总线接口：只有要原型化的特定控制算法被移到 RPU 中执行（外部旁路），甚至直接在原始 ECU 中执行（内部旁路）。旁路主要在于在运行时用被测原型算法计算的值替换原始软件算法的输入和/或输出。

目前，AUTOSAR 支持两种快速原型方法：组件包装器方法和直接缓冲区访问方法。

为了使用该方法，必须正确配置 RTE（任务 配置 RTE，配置细节见 AUTOSAR_SWS_RTE [\[16, CP SWS RTE\]](#ref-16) 第 4.9.2 节）。此外，基于完整的快速原型场景的 ECU 提取工件，必须生成并编译相应的包装器代码（活动 封装 SW-C）。根据开发策略，包装器代码生成可以在开发过程的不同阶段进行。

#### 2.13.3. 工作流

| Process Pattern | Rapid Prototyping Overview |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Rapid Prototyping Overview |  |  |
| Brief Description |  |  |  |
| Description | This use case shows the typical steps required from an updated rapid prototyping scenario down to an update of the generated RTE and the produced A2L file. The use cases assumes, that rapid prototyping scenario is changed in an already existing system, thus the steps required to define and build a new system are omitted, only the calibration relevant steps are shown. In addition, the use case includes the (optional) task of updating a set of calibration parameter values as input for the RTE. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Configure BSW and RTE | 1 |  |
| Aggregates | Define Rapid Prototyping Scenario | 1 |  |
| Aggregates | Encapsulate SW-C | 1 |  |
| Aggregates | Generate A2L | 1 |  |
| Aggregates | Generate BSW and RTE | 1 |  |
| Aggregates | Generate ECU Executable | 1 |  |
| Aggregates | Generate ECU Extract | 1 |  |
| Aggregates | Prepare ECU Configuration | 1 |  |
| Aggregates | Refine Rapid Prototyping Scenario | 1 |  |
| Activity | Encapsulate SW-C |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Rapid Prototyping Overview |  |  |
| Brief Description |  |  |  |
| Description | Encapsulate the software component to enable rapid prototyping. During this activity the wrapper code is generated based on the Rapid Prototyping Scenario and the software component is compiled and linked with the generated wrapper. |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Compile Atomic Software Component | 1 |  |
| Aggregates | Generate Rapid Prototyping Wrapper | 1 |  |

### 2.14. 安全扩展

**R22-11 中移除的安全扩展**

请注意，安全扩展在 R21-11 中被标记为过时（**obsolete**），并在 R22-11 中被移除。因此，本节将在未来的 AUTOSAR 发布版中被重做或移除。

#### 2.14.1. 目的

本用例给出安全扩展用法的概览。

#### 2.14.2. 描述

ISO 26262 [\[17\]](#ref-17) 是道路车辆电子和软件系统功能安全的适用标准，它影响几乎所有的开发活动，包括软件规范、设计和实现。安全扩展支持在 AUTOSAR 上下文中标准化地交换安全信息，并为 ISO 26262 所要求的一致性管理提供基础。附加的安全相关信息可用于例如生成文档或检查 ASIL 约束（关于分配、映射、分解和层级），这些约束由 ISO 26262 规定。AUTOSAR 方法论聚焦于信息的创建和细化。相应的分析不在本文档的范围内。

根据 ISO 26262，安全扩展提供以下表达安全信息的手段：

- 安全需求（工件 安全需求）

- 安全措施（工件 安全措施）

- 安全完整性级别：安全需求、安全措施和任何 AUTOSAR 元素的属性

- 安全需求的分解：原始需求与分解后需求之间的引用（任务 分解安全需求）

- 安全需求的细化：原始需求与细化后需求之间的引用（任务 细化安全需求）

- 安全需求的分配：安全需求与 AUTOSAR 元素之间的引用（任务 分配安全需求）

- 安全措施的分配：安全措施与 AUTOSAR 元素之间的引用（任务 分配安全措施）

- 安全需求与安全措施之间的映射（任务 将安全需求映射到安全措施）

- 安全需求之间的独立性关系（任务 添加独立性关系）

安全相关信息可以独立交换，因此被合并到一个单独的交付物安全扩展中。

> 20 见图 2.68。

以下专用活动演示安全扩展在不同开发阶段的用法，并被集成到相应的用例中：

- 定义 VFB 安全信息

- 定义软件组件安全信息

- 定义系统安全信息

#### 2.14.3. 工作流


| Process Pattern | Safety Extensions Overview |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Safety Extensions Overview |  |  |
| Brief Description |  |  |  |
| Description |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Define Safety Information | 1 |  |
| Activity | Define Safety Information |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Safety Extensions Overview |  |  |
| Brief Description | Defines all required safety information. |  |  |
| Description | This activity represents a generic pattern for defining safety relevant information. The safety extensions are not restricted to specific AUTOSAR elements so that safety relevant information can be added and modified in several stages of the AUTOSAR Methodology. Thus, the AUTOSAR elements consumed by some of the nested tasks are modeled using the "General Autosar Artifact". |  |  |
| Extended By | Define Software Component Safety Information, Define System Safety Information, Define VFB Safety Information |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Add Independence Relation | 1 |  |
| Aggregates | Allocate Safety Measure | 1 |  |
| Aggregates | Allocate Safety Requirement | 1 |  |
| Aggregates | Decompose Safety Requirement | 1 |  |
| Aggregates | Define ASIL For AUTOSAR Element | 1 |  |
| Aggregates | Define Safety Measure | 1 |  |
| Aggregates | Define Safety Requirement | 1 |  |
| Aggregates | Map Safety Requirement to Safety Measure | 1 |  |
| Aggregates | Refine Safety Requirement | 1 |  |

### 2.15. 变体处理

#### 2.15.1. 概述

其次，存在预定义变体（**Predefined Variant**）。

#### 2.15.2. 绑定时间

AUTOSAR 定义了以下绑定时间（此处按时间顺序给出）：

- BlueprintDerivationTime

- SystemDesignTime

- CodeGenerationTime

- PreCompileTime

- LinkTime

- PostBuild

通用结构模板还提到另外两个绑定时间。第一个是 FunctionDesignTime，它位于 SystemDesignTime 之前，但独立于 BluePrintDerivationTime。第二个是 Runtime，它位于 PostBuild 之后。这些绑定时间不在 AUTOSAR 的覆盖范围内，这里仅为完整性而提及。

##### 2.15.2.1. 最晚绑定时间

> 21 BlueprintDerivationTime 和 PostBuild 不是元模型中使用的实际枚举的一部分，但它们由变体点的结构所蕴含。更多细节见通用结构模板 [\[18\]](#ref-18) 的第 7 章。

例如，作为组合一部分的软件组件的最晚绑定时间是 PostBuild。换句话说，可以配置 ECU 在启动时决定软件组件是否激活。

然而，并不总是能够在最晚可能的时间绑定变体。继续上面的例子，将所有软件组件设为 PostBuild 意味着可执行文件始终包含所有软件组件的代码和其他资源，无论它们是否被激活。因此，可执行文件可能变得太大而无法放入其指定的 ECU。如果是这种情况，软件组件需要更早地绑定，通常在 PreCompileTime 甚至 SystemDesignTime。

导致这一决定的并不只有这一种情形。例如，一个软件组件可能包含两个或多个子组件，每个子组件特定于某个供应商。在这种情况下，在将软件组件交付给特定供应商之前，通常的做法是移除针对其他供应商的子组件。这显然最晚可以在 PrecompileTime 完成。

还有一些情况，变体点的绑定时间存在隐式（即元模型未声明）的下限。例如，如果软件组件 A 中的一个变体使用了软件组件 B 中的一个变体，则需要协调绑定时间。如果组件 B 是 PostBuild 但使用了软件组件 A，则组件 A 不能是 SystemDesignTime。

##### 2.15.2.2. 实际绑定时间

如上一节所述，软件组件的组合可以在 PostBuild 绑定，但这并不总是合乎需要的，甚至不一定可行。在这种情况下，bindingTime 应声明更早的绑定时间。

此外，与最晚绑定时间不同——它是一个元模型元素、在 M2 层级声明——该绑定时间是一个与变体点关联的模型元素，在 M1 层级声明。

也就是说，变体点的绑定时间限制了特定变体点必须被绑定的时点，但该绑定时间又受最晚绑定时间的约束。

> 22 该属性名为 bindingTime，位于变体点的 ConditionByformula 元素中。对于 AttributeValueVariationPoint，它包含在属性 bindingTime 中。

#### 2.15.3. 定义变体

该信息是必要的，因为可能变体的数量极其庞大，但其中只有很小的子集是可行的。

#### 2.15.4. 选择变体

变体点是否被包含在系统中由一个或多个变量决定。如果变体点的绑定时间在 SystemDesignTime 到 LinkTime 之间的任何时点，则该变体点包含一个基于系统常量的表达式（见工件 系统常量值集合）。如果该表达式求值为 true，则该变体点被包含在系统中。PostBuild 使用一种简化方案，只允许与 PostBuildVariantCriterion（技术上是一个 ARElement）进行单次比较。

例如，决定一个 PreCompileTime 变体点的系统常量可能已经在 SystemDesignTime 被选定，但由于对另一个绑定时间为 PreCompileTime 的软件组件的依赖，实际绑定必须推迟到 PreCompileTime，如第 [2.15.2.2](#21522-实际绑定时间) 节所述。

此外，由于 PredefinedVariant 跨越多个变体点，这些变体点可能具有不同的绑定时间，一些变体点可能在 PredefinedVariant 被选择后立即具有绑定时间（最晚甚至实际），而其他变体点可能具有更晚的绑定时间。

最后，选择特定变体的决定通常与遵循自身时间线的供应商特定流程绑定。

因此，选择特定变体的时间通常不同于相关变体点被绑定的时间。总之，变体必须在绑定之前的某个时间被选择，但这一事件发生的实际时间不由 AUTOSAR 决定，而且相当依赖于供应商。

### 2.16. 绑定时间的定义

#### 2.16.1. 概述

绑定时间并不（如其名称可能暗示的那样）是一个精确的时间点，而是处理步骤的分类。例如，绑定时间 CodeGenerationTime 指的是从 ARXML 格式的 AUTOSAR 模型到代码的转换步骤。

在本节中，我们为方法论中的工件和任务定义绑定时间。

这特别意味着：

- 任何在模型上工作的任务都可以绑定具有绑定时间 SystemDesignTime 的变体点。

- 任何生成代码的任务都需要绑定具有绑定时间 CodeGenerationTime 的未绑定变体点。所有具有更早绑定时间的变体点届时必须已被绑定。

- 类似地，任何编译代码的任务都需要绑定具有绑定时间 PreCompileTime 的未绑定变体点。所有具有更早绑定时间的变体点届时必须已被绑定。

此时，变体点的 PostBuildVariantCondition 的值也必须被绑定。这些值的最晚绑定时间为 PreCompileTime。

在所有这些情况下，变体点的条件所需的系统常量显然必须在变体点被绑定之前定义。

这特别意味着，如果工件是任务的输入，则绑定时间为 X 的变体点应已被绑定，任务依赖于此。

如果工件是任务的输出，则保证这样创建的工件的所有绑定时间为 X 的变体点都已被绑定。

在方法论库中，这通过附加到 Consumes/ConsumedBy 或 Produces/ProducedBy 关系上的标签 Meth.bindingTime 的值来指示。

注意，标签 Meth.bindingTime 不适用于 inout 关系，因为按照上述定义，特定任务的输入和输出的绑定时间值通常是不同的。如果表达这些绑定时间很重要，则

> 23 注意，对于 RTE 代码，绑定 PreCompileTime 变体的技术步骤部分由一个在实际编译之前运行的准备任务完成，见 生成 RTE 预构建数据集。这特别意味着，相关系统常量必须在执行该准备任务之前定义。在这种情况下，实际编译任务 编译 ECU 源代码 的绑定时间被指示为 CompileTime。

> 24 该变体点仍是 PostBuild：PostBuildVariantCondition 在 PreCompileTime 固定，但与关联 PostBuildVariantCriterion 的比较发生在后构建。细节见通用结构模板 [\[18\]](#ref-18)。

#### 2.16.2. 按绑定时间对工件的分类

- 模型、需求、功能模型：这些指的不是 AUTOSAR 模型的模型。例如，模型可以是 Matlab/Simulink 模型或需求文档。

- ARXML：ARXML 工件是符合 AUTOSAR XML 模式的 XML 文档。

- 源代码：源代码工件是使用编程语言语法（例如 C 或 C++）编写的文本。

源代码可以手工生成，也可以是代码生成器的输出。

- 已绑定源代码：已绑定源代码工件包含不含任何未绑定预编译变体点的源代码。

- 目标代码：目标代码是编译器的输出。目标代码通常是机器码，但也可能包含 XML 等格式的描述性信息。

- 可执行文件：可执行文件是可以在 ECU 上运行的工件。它通常类似于目标代码；两者的区别在于前者不提供在 ECU 上执行的（完整）手段。

- 配置数据集合：配置数据集合是对 PostBuildVariantCriterion 的一组赋值。

#### 2.16.3. 绑定时间的分类

表 2.57 给出 AUTOSAR 变体处理中绑定时间的概览。

| Binding Time | AUTOSAR Metamodel | AUTOSAR Methodology |  |

| BlueprintDerivationTime | partially | yes |  |
| FunctionDesignTime | out of scope |  |  |
| InitialBindingTime | no | yes |  |
| SystemDesignTime | yes |  |  |
| CodeGenerationTime | yes |  |  |
| PreCompileTime | yes |  |  |
| CompileTime | unused | yes |  |
| LinkTime | yes |  |  |
| PostBuild | yes |  |  |
| Runtime | out of scope |  |  |

AUTOSAR 元模型中的变体处理支持以下绑定时间：

- BlueprintDerivationTime

- SystemDesignTime

- CodeGenerationTime

- PreCompileTime

- LinkTime

- PostBuild

AUTOSAR 方法论还利用另外两个绑定时间：InitialBindingTime 用于刻画没有变体点被绑定的工件，CompileTime 用于区分代码的预处理和编译。最后，FunctionDesignTime 和 Runtime 不在 AUTOSAR 变体处理的范围内，这里仅为完整性而提及。

##### 2.16.3.1. BlueprintDerivationTime

在 BlueprintDerivationTime，模型从蓝图（**Blueprint**）派生。例如，功能设计工具提供从预定义蓝图集合派生对象的选项。更多细节见 [\[2\]](#ref-2)。这不同于本章定义的变体处理，但它使用相同的元模型特性（见 [\[18\]](#ref-18)）。

BlueprintDerivationTime 不在本文档的范围内，但为完整性在此提及。

输入工件：

模型、需求

输出工件：

ARXML。

##### 2.16.3.2. FunctionDesignTime

在 FunctionDesignTime，开发（控制）系统的、独立于软件架构的模型。此阶段使用的典型工具是 Matlab/Simulink 或 ASCETMD。

如果功能设计工具支持按照 AUTOSAR 的变体处理，那么它在生成的 AUTOSAR 工件中别无选择，只能使用 CodeGenerationTime 或更晚作为绑定时间。

FunctionDesignTime 不在本文档的范围内（只要它不影响标定测量），但为完整性在此提及。

输入工件：

模型、需求

输出工件：


##### 2.16.3.3. InitialBindingTime

在 InitialBindingTime，没有变体点被绑定。需要该绑定时间来表达工件中没有任何 SystemDesignTime 变体点被绑定的状态

输入工件：模型、需求、功能模型、来自蓝图的 ARXML 格式的 AUTOSAR 模型。

输出工件：


##### 2.16.3.4. SystemDesignTime

SystemDesignTime 由以下任务表征：

- 设计 VFB

- 软件组件类型（接口）

- SWC 原型以及 SWC 原型之间的连接

- 设计拓扑

- ECU 和互连网络

- 设计通信矩阵和数据映射

输入工件：功能模型、需求、来自蓝图的 ARXML 格式的 AUTOSAR 模型。

输出工件：


##### 2.16.3.5. CodeGenerationTime

在这一步，生成代码。这可以手工完成，也可以使用工具完成，或两者的混合。

手写代码通常基于需求文档，而生成的代码通常从在 FunctionDesignTime 或 SystemDesignTime 设计的模型创建。

需求和模型都可能包含变体，但代码只为那些已被选择的、或需要稍后解析的变体生成。

输入工件：


输出工件：

输出工件：源代码。

##### 2.16.3.6. PreCompileTime

在 PreCompileTime，使用预处理器（例如 C 预处理器）进一步定制代码并将部分代码排除在编译过程之外。

这种排除有几个原因：所选变体不需要该代码、代码与所选变体不兼容、或代码需要所选变体中不存在的资源。在此阶段被排除的代码在后续阶段将不可用。

PreCompileTime 通常用于手写代码（对于它，SystemDesignTime 和 CodeGenerationTime 显然无法生效），或者当系统常量需要在代码生成之后绑定时。

输入工件：

输出工件：源代码。

输出工件：

输出工件：已绑定源代码。

##### 2.16.3.7. CompileTime

在 CompileTime，已经被宏处理器（例如 C 预处理器）处理过、并且剥离了所有 PreCompileTime 变体点的源代码被转换为目标代码。编译器可能通过移除未使用的代码路径来消除更多变体。

CompileTime 不在 AUTOSAR 元模型中使用，但在 AUTOSAR 方法论中用于区分预处理器和编译器。

输入工件：

输出工件：已绑定源代码。

输出工件：

输出工件：目标代码。

##### 2.16.3.8. LinkTime

此阶段的配置决定哪些模块被包含在所得的目标代码（可执行文件）中，以及根据所选变体省略哪些模块。

输入工件：

输出工件：目标代码。

输出工件：

输出工件：可执行程序。

##### 2.16.3.9. PostBuild

PostBuild 是最晚在 ECU 启动时绑定的绑定时间。换句话说，这是从可执行程序的创建到 ECU 启动之间的一切。

ECU 的启动即 PostBuild 绑定，显然它无法在模型中解析。

输入工件：可执行程序、配置数据集合。

输出工件：—

##### 2.16.3.10. 运行期

启动和初始化之后的一切都是 RunTime。RunTime 的变体处理不在本文档的范围内，但为完整性在此提及。

### 2.17. 如何解决名称冲突

#### 2.17.1. 名称冲突的原因

在 AUTOSAR 系统的高度分布式开发中，不同开发工件中使用的符号名称存在不唯一的一定风险，因此在应用软件工具时可能发生名称冲突。

然而，AUTOSAR XML 工件中规定的某些符号需要在后续流程步骤（“下游”）中传递到其他开发工件，并将例如作为 C 代码中的符号、文件名、标定工具显示的名称或文本文档中的名称出现。这里我们一般有两种命名冲突的原因（它们也可能组合发生）：

**· 未协调的协同开发**

由于 C 语言在一个编译单元内的全局名称空间，如果集成了由不同参与方开发、未协调符号定义的源代码片段，名称冲突的风险相当高。

头文件的名称或链接器可见的符号也可能发生同样的情况。

在 AUTOSAR 中，软件组件之间（以及在一定程度上基础软件模块之间）的编程语言接口被限制为特定模式并从 ARXML 生成，因此协调工作仅限于在 ARXML 中正确定义相关符号。

在若干情况下，ARElement 的 shortName 对应于代码中的标识符（或此类标识符的一部分），有时还对应于文件名或其一部分。由于 shortName 还用于 ARXML 元素之间的链接，因此很难在不影响整体设计的情况下更改这样的名称。例如，AtomicSwComponentType 的名称就是这种情况。

**· 多次实例化**

AUTOSAR 运行时环境（RTE）支持软件组件的多次实例化。这意味着，在一个系统中、甚至在一个 ECU 上，给定的 AtomicSwComponentType 可以有多个实例。每个实例拥有自己的数据（由 RTE 管理），但只有一个描述整个类型的工件（VFB 原子软件组件）。如果需要一个标识特定组件实例或属于该实例的特定数据的符号（例如用于在标定工具中显示），就会产生冲突。

如果外围元素在多个上下文中被复用，PortInterface 中或复合数据类型中的数据元素或操作实参也会发生类似的情况。

如果多个驱动模块实现相同的接口（仅通过实例标识符区分），基础软件中可能发生另一种 “多次实例化”。在这种情况下，我们实际上有代码的不同实现，模块只共享描述的上层（工件 基础软件模块描述 和 基础软件模块内部行为）。

#### 2.17.2. 方法论中解决名称冲突的时点

另一方面，方法论中存在多个可以解决这些冲突的时点。

一般而言，我们可以区分解决名称冲突的开发阶段与冲突发生（或将发生）的阶段。因为冲突通常会阻止某个任务的完成（例如编译），所以必须在冲突将发生的阶段或更早的阶段解决它。

#### 2.17.3. 解决名称冲突的机制

解决名称冲突的机制有：

该机制允许在默认情况下使用 shortName 生成与 RTE 相关的代码的情况下重定义名称。这避免了更改 ARXML 模型中的整体设计。

该机制可以在编码期应用（活动 开发原子软件组件，任务 为类型定义 SymbolProps），并解决由未协调开发引起的冲突。此类更改——即使不影响软件的整体设计——也应由所涉及的各方商定。

以下元模型元素提供了该机制：

**AtomicSwComponentType.symbolProps**

允许重定义 RTE 在其代码中使用的软件组件类型名称。这解决了偶然以相同 shortName 设计的不同软件组件类型之间的名称冲突。

**ImplementationDataType.symbolProps**

允许重定义 RTE 和/或组件代码中使用的实现数据类型名称。这解决了偶然以相同 shortName 设计的不同实现数据类型之间的名称冲突。

> 25 注意，该机制不适用于内存段的预处理器代码中使用的前缀。由于组件类型名称重复导致的这些预处理器符号之间的冲突对链接器不可见。但编译时可能发生冲突，必须手动解决。


该机制类似于前面描述的机制。它允许为 RTE 生成器合同阶段创建的预处理器字面量（例如枚举类型或上/下限的字面量）定义前缀。该机制同样解决由未协调开发引起的冲突，并且必须在编码期应用（任务 定义原子软件组件内部行为 的一部分）。

要操作的模型元素是：

**SwcInternalBehavior.includedDataTypeSet.literalPrefix**

**可运行实体名称中的冲突解决**

对于 RunnableEntity，代码中使用的符号已经独立于 shortName——它总是通过属性 RunnableEntity.symbol 建模。然而，由于这些符号需要在一个 RTE 实例的范围内唯一（见 [\[7, CP TPS Software Component Template\]](#ref-7) 中的 [constr_2025]），如果符号定义此前未协调，在集成时同样可能发生名称冲突。

该机制允许为模型元素的实例（例如软件组件实例或数据元素实例）指派标识符，使其在某个范围（例如系统或 ECU）内唯一。由此避免了如果简单地使用 ARXML 元素的 shortName 就会发生的名称冲突。换言之，该机制解决了 ARXML 模型中类型的多次实例化所引起的名称冲突。

以这种方式定义的标识符通常不在代码中使用，因为 AUTOSAR 组件不依赖全局变量。其主要用途是在需要处理 ARXML 模型包上下文之外的符号的其他工件中使用，例如文档中的引用（例如在工件 软件组件文档 中）或测量和

标定工具的输入（例如在工件 RTE 测量和标定支持数据 中）。ECU Flat Map 的一个特殊用例是从 System 到 ECU 提取的模型变换，其中它被用于定义组件原型的附加名称。

该机制应用的方法论时点当然取决于用例。方法论库中定义 Flat Map 的典型任务通常在集成期之前执行：生成或调整系统 Flat Map、定义部分 Flat Map 和 生成或调整 ECU Flat Map。但由于 FlatMap 中的标识符独立于代码，原则上即使在集成期发生冲突时也可以调整。

该机制类似于 FlatMap。它允许为模型元素定义附加名称，或者基于 FlatMap 中的条目，或者独立使用。用法也类似，但在与 AUTOSAR RTE 相关的方面没有标准化的用例。它可以在 FlatMap 格式过于受限的情况下使用。

如果一个基础软件模块的多个 “实例”（实现不同但接口定义相同）被链接在一起，名称冲突必须通过定义 “中缀（infixes）” 来解决。它们是表示模块供应商和实例角色的小字符串片段。它们用于扩展全局可见的 C 符号和某些头文件名。该机制也与任务 生成 BSWM 合同头文件 中生成的基础软件调度器 API 相关。

虽然该机制解决的是某一类多次实例化的冲突，但它与代码相关，因此必须在编码期应用。中缀的描述必须放入工件 基础软件模块实现描述 中。

### 2.18. 数据交换点

#### 2.18.1. 目的

数据交换点的画像（**Profile of Data Exchange Points**）旨在通过描述方法论中给定活动或任务所期望的数据来改善工具之间的互操作性。本用例描述创建这些画像的主要步骤以及它们在后续开发中的使用方式。

#### 2.18.2. 描述

整体汽车系统开发涉及由若干不同组织、伙伴和工具组成的复杂供应链。实际项目表明，利益相关者与工具之间的数据交换经常不能正常工作。互操作性问题往往在开发后期才被发现，通常需要在每个单独的项目中分析和适配工具。

最严重的问题与数据交换点的定义和协调不足有关：通常不清楚在整体方法论中什么时间需要什么数据、适用哪些约束。

为克服这一困难，AUTOSAR 将数据交换点的详细描述引入为开发过程的一个步骤。重要的是要注意，该步骤未在第 [2.1](#21-总体概览) 章的总体概览用例中显式建模，而是可以在任何数据交换可能导致不兼容的情况下执行。主要的交换点例如由图 2.9 所示的域边界给出。

数据交换点及相应元类的详细方法在 [\[2, FO TPS Standardization Template\]](#ref-2) 中描述。

- 分析 AUTOSAR 规范或通用非 AUTOSAR 工件（例如工具文档、先前使用的交换格式的文档（例如 FIBEX、DBC、LDF）或描述交换工件内容的公司特定文档），以识别 AUTOSAR 标准和 AUTOSAR 数据交换格式的哪些部分与特定数据交换点相关。该步骤可以“从零开始”，也可以基于已有的数据交换点画像。AUTOSAR 可以为典型的数据交换点提供预定义的数据交换点画像，必要时可在个别项目中细化。

- 分析通常在特定数据交换点交换的已有通用 AUTOSAR 工件（AUTOSAR 模型）。这有助于弄清元模型的哪些部分目前被使用。例如，如果通用 AUTOSAR 工件包含 FlexrayCluster，则派生的数据交换点

画像可能将 FlexrayCluster 视为相关信息。注意，这种分析只能作为初步提示。识别信息是否缺失、或模型中是否存在与特定数据交换点无关的信息，需要工程专业知识。

#### 2.18.3. 工作流

表2.28：Validate Compliance of Autosar Model against Profile for Data Exchange Point（**Validate Compliance of Autosar Model against Profile for Data Exchange Point**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Data Exchange Point Overview | — |
| 简要描述 | Create a Profile of Data Exchange Point | — |
| 描述 | There are several approaches of creating Profiles of Data Exchange Points, each of them is based on a Baseline Profile of Data Exchange Points, which defines default values, e.g.: (1) Analyze Autosar specifications or General Non-Autosar Artifacts such as tool documentation, documentation of previously used exchange formats (e.g. FIBEX, DBC, LDF) or company-specific documents describing contents for exchange artifacts in order to identify which parts of the Autosar specifications and Autosar templates are relevant at the specific Data Exchange Point. This step could be started "from Scratch" or based on an existing Profile of Data Exchange Point. Autosar could provide predefined Profiles of Data Exchange Point for typical exchange scenarios which could be refined if necessary in individual projects. (2) Analyze existing General Autosar Artifacts (Autosar models) that are typically exchanged at a specific Data Exchange Point. This can help to figure out, which parts of the meta model are currently used. E.g. if the General Autosar Artifact contains FlexrayClusters the derived Profile of Data Exchange Point should consider FlexrayClusters as relevant information. Note, that this analysis can only deal as a first hint. Engineer Know How is required in order to identify if information is missing or of information was in the model that is not relevant for the specific Data Exchange Point. In order to reduce the size of a Profile of Data Exchange Point it should only describe information that is not already provided by referenced Autosar standardized Baseline Profile of Data Exchange Point. | — |
| 消费 | Autosar Specification | 0..* The Autosar specifications that are analyzed in order to figure out which data is required for the given data exchange point. |
| 消费 | Baseline Profile of Data Exchange Point | 1 The Baseline Profile of Data Exchange Point defines the default values of the Profile. |
| 消费 | General Autosar Artifact | 0..* The analysis of existing Autosar models that are typically exchanged at a specific Data Exchange Point can help during the development of a Profile of Data Exchange Point. |
| 消费 | General Non Autosar Artifact | 0..* Custom specification for data exchange (textual or non-AUTOSAR exchange format (e.g. FIBEX, DBC, LDF)) |
| 消费 | Profile of Data Exchange Point | 0..* An existing Profile of Data Exchange Point that is used as a starting point for a new Profile of Data Exchange Point. E.g. start with a profile of an old tool version and tailor it so that new features are covered. |
| 产出 | Profile of Data Exchange Point | 1 The new Profile of Data Exchange Point |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Data Exchange Point Overview | — |
| 简要描述 | Analysis of input Profiles of Data Exchange Point with respect to tool interoperability issues and documentation of the results as an Agreed Profile of Data Exchange Point. | — |
| 描述 | In early phases of a project the Profiles of Data Exchange Point describe the requirements and assertions of the involved tools. These Profiles are then analyzed. Aspects that are common on all Profiles have low risk of interoperability issues and can directly be copied into the Agreed Profile of Data Exchange Point. If the Profiles are different, potential interoperability issues need to be investigated and an agreement needs to be developed. This is a highly manual step that requires negotiation between the stakeholders. | — |
| 消费 | Profile of Data Exchange Point | 1..* The Profiles of Data Exchange Point that are analyzed with respect to interoperability issues. |
| 产出 | Agreed Profile of Data Exchange Point | 1 The Agreed Profile of Data Exchange Point |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Use Cases::High Level::Data Exchange Point Overview | — |
| 简要描述 | Validate the compliance of AUTOSAR models against a Profile for Data Exchange Point. | — |
| 描述 | Once there is an agreement on a profile, this can be used to continuously validate if the exchanged General Autosar Artifgacts (Autosar models) still conform with the Agreed Profile of Data Exchange Point. This can e.g. help to unveil unintended modifications of the Autosar models because of changed tool configurations or tool updates. | — |
| 消费 | Agreed Profile of Data Exchange Point | 1 The DataFormatTailoring and Baseline sections of the Agreed Profile of Data Exchange Point can be used to configure the validation engine of Autosar Validation Tools (e.g. provide rules for existence of elements or switch on/off individual semantic constraints) |
| 消费 | Baseline Profile of Data Exchange Point | 1 The Baseline Profile of Data Exchange Point provides default values foe parameters that are not specified in the Agreed Profile of Data Exchange Point. |
| 消费 | General Autosar Artifact | 1 An Autosar model can be validated against the Agreed Profile for Data Exchange Point. Default values of attributes that are not defined in the Agreed Profile of Data Exchange Point are retrieved from the Baseline Profile of Data Exchange Point. |

## 3. 方法论库

### 3.1. 公共元素

本章包含在 AUTOSAR 开发的若干领域中使用的 工作产品和任务 的定义。相关元模型元素的定义参见 [\[18, FO TPS Generic Structure Template\]](#ref-18)。

#### 3.1.1. 工作产品种类

表3.1：Delivered（**Delivered**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | An artifact that conforms to the AUTOSAR XML schema. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | A human readable artifact that conforms to a defined programming language syntax, such as C or Java. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | A Bound Source Code artifact contains source code without any unbound precompile variation points. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | An Object Code is the output of a compiler. Object code is typically machine code, but may also include descriptive information in a format such as XML. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | This is a special kind of binary code containing configuration that can be loaded separately from the main ECU code. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | An Executable is an artifact that can run on an ECU. It is often similar to Object Code; the difference between the two is that the former does not provide means for execution on an ECU. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | A human readable artifact that is stored as plain text, rich text, PDF, etc. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | A custom artifact format which is not further specified in the AUTOSAR Methodology. | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Product Kinds | — |
| 简要描述 |  | — |
| 描述 | These are collections of delivered work products. They form the basis of exchange between organizations. | — |

#### 3.1.2. 任务

##### 3.1.2.1. 添加通用文档

表3.2：添加通用文档（**Add General Documentation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 |  | — |
| 描述 | Add General Documentation to work products (AR_MET_REQ069) | — |
| 产出 | General Documentation | 1 |

##### 3.1.2.2. 定义管理数据

表3.3：定义管理数据（**Define Admin Data**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 | Generic task to define admin data of an Identifiable within an AUTOSAR artifact. | — |
| 描述 | Generic task to define administration data (metamodel element AdminData) of an Identifiable within an AUTOSAR artifact. Note that administration data can be defined on several levels, namely for the top-level package of a General Autosar Artifact, but also for sub-packages and for other Identifiables within the XML description. Administration data include versioning information of the model element via the meta-class Doc Revision, and the aggregation of user specific data via so-called special data groups, meta-class Sdg. For more details on the administration data content refer to document ID 202 FO_TPS_Generic | — |
| 产出 | General Autosar Artifact | 1 |

##### 3.1.2.3. 定义替代名称

表3.4：定义替代名称（**Define Alias Names**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 | Define a set of alias names for AUTOSAR model elements. | — |
| 描述 | The usual mechanism for defining global names for nested elements within an AUTOSAR XML model is the Flat Map. However in the cooperation with non-AUTOSAR tools, there are uses cases which require additional alias names which can be defined by this task. It can be applied on System and on ECU level as well. Possible use cases are for example: • The names defined by an ECU Flat Map, System Flat Map or Partial Flat Map shall be superseded when used by an external tool (e.g. in order to use a more general string format). • Resolve name conflicts for elements which cannot be referred in the context of a Flat Map (e.g. for elements directly defined in the scope of ARPackages, like System Constants to be displayed by A2L tools). | — |
| 消费 | Delivered Atomic Software Components | 0..1 Needed for definition of alias names in the scope of delivered software components. |
| 消费 | System Description | 0..1 Needed for definition of alias names with system, system extract or ECU scope, depending of the role of the System Description. |
| 产出 | Alias Name Set | 1 |

##### 3.1.2.4. 求值变体

表3.5：求值变体（**Evaluate Variant**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 | Document the evaluation of variants in the software description. | — |
| 描述 | Create or modify an Evaluated Variant Set in order to document the outcome of an evaluation of particular variants. This namely means setting the "approval status" in relation to a given set of PredefinedVariants and a given set of model elements (e.g. a particular Software Component) which were evaluated. This is a general task which can be applied on different levels, therefore the input is modeled as General Autosar Artifact. | — |
| 消费 | General Autosar Artifact | 1..* |
| 消费 | Evaluated Variant Set | 0..1 |
| 消费 | Postbuild Variant Set | 0..* |
| 消费 | Predefined Variant | 0..* |
| 消费 | System Constant Value Set | 0..* |
| 产出 | Evaluated Variant Set | 1 |

##### 3.1.2.5. 定义内存寻址模式

表3.6：定义内存寻址模式（**Define Memory Addressing Modes**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define the compiler specific configuration used in a later task to generate the "pragmas" in memory mapping header files. The output (container MemMapAddressingModeSet) is treated as pre-configured configuration values for the "module" MemMap, because it can be prepared independently from the configuration for a specific integration project. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | Basic Software Module Developer | 1 |
| 执行者 | Software Component Developer | 0..1 |
| 产出 | BSW Module Preconfigured Configuration | 1..* MemMapAddressingModeSet: Meth.bindingTime = SystemDesignTime |

##### 3.1.2.6. 配置内存映射分配

表3.7：配置内存映射分配（**Configure Memmap Allocation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 |  | — |
| 描述 | Configure the ECU Configuration part MemMapAllocation for module "MemMap". The output is to be used for generating memory mapping headers during ECU integration as well as for BSW and SWC compiling/linking in local environments. MemMapAllocation defines a mapping between abstract memory sections used in BSW or SWC code and compiler specific configuration elements. The abstract sections are identified via links to SwAddrmethods (generic mapping) resp. MemorySections of the XML input files. The compiler specific configuration is given as a pre-configured configuration for module "MemMap" via the container MemMapAddressingModeSet. For more information refer to document ID 128 CP_SWS_MemoryMapping. | — |
| 执行者 | Basic Software Module Developer | 0..1 |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | BSW Module Preconfigured Configuration | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation and addressing modes. |
| 消费 | Atomic Software Component Implementation | 0..* MemorySections: |
| 消费 | Basic Software Module Implementation Description | 0..* MemorySections: |
| 消费 | VFB Types | 0..* SwAddrMethods: SwAddrMethods used for the generic mapping. Note that one SwAddrmethod can represent several memory sections. |
| 产出 | ECU Configuration Values | 1 MemMapAllocation: Meth.bindingTime = SystemDesignTime |

##### 3.1.2.7. 生成 BSW 内存映射头文件


表3.8：生成 BSW 内存映射头文件（**Generate BSW Memory Mapping Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 |  | — |
| 描述 | Generate a memory mapping header to be used for one BSW module (the default case) or a group of BSW modules (e.g. an ICC2 BSW cluster). Note that the usage of one MemMap.h for the complete BSW of one build environment is possible, but deprecated. This task can be used in ECU scope or with preliminary scope to test BSW modules. Note that the content of the generated file is compiler specific (#pragma statements). Inputs are: • From Basic Software Module Description: The shortName is used (in the default case) as the first part of the generated file name. • From VFB Types: Properties of abstract sections given by SwAddrmethods, which in turn are referred by MemorySection as well as by MemMapAllocation. • From Basic Software Module Implementation Description: Names of the individual abstract sections (preprocessor macros) used in the code (including optional prefixes overriding the default rule); optional infixes for the file name (if the default rule is used); optional declaration of file name (element DependencyOnArtifact) overriding the default rule. • From Preconfigured Configuration for module "MemMap": Collection of compiler specific configuration elements. • From ECU Configuration for module "MemMap" : MemMapAllocation - this is the concrete mapping for this environment. • From ECU Configuration: Find the list of used BSW modules in case the task is done for the whole BSW (EcucValueCollection.ecucValue.moduleDescription). | — |
| 执行者 | ECU Integrator | 1 |
| 执行者 | Basic Software Module Developer | 0..1 |
| 消费 | Basic Software Module Implementation Description | 1 DependencyOnArtifact: Can be used to override the default name of the memory mapping header file. Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Implementation Description | 1 MemorySections: MemorySections defined for a BSW module. This input includes optional prefixes for memory sections overriding the default rule. Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Implementation Description | 1 infixes: Optional infixes (denoting instance and vendor ID) to be used within the created header file name. Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Configuration Values | 1 MemMapAllocation: Mapping of the abstract sections (SwAddressMethods for generic mapping resp. Memory Section Elements for specific mapping) to the compiler specific MemMapAddressingModes. Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Module Preconfigured Configuration | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation. Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Types | 1..* SwAddrMethod: Referred SwAddrMethods Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Description | 0..1 shortName: The BSW module's shortName is used as the first part of the generated file name, in case the default rule applies. Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Configuration Values | 0..1 moduleDescription: List of used BSW modules (Ecuc ValueCollection.ecucValue.moduleDescription) Meth.bindingTime = SystemDesignTime |
| 产出 | Standard Header Files | 1 BSW_MemMap: The memory mapping header file to be used for one or more BSW modules in a given build environment. The file name has in the standardized case a form like {Mip}_MemMap.h in which the prefixes {Mip} are determined by the BSW module (or BSW cluster) name and optional infixes. However, it is also possible to create a completely different filename via explicit declaration in the BSW Module Implementation. For more detailed rules on the name of the generated file refer to document ID 128 CP_SWS_Memory Mapping. Meth.bindingTime = CodeGenerationTime |

##### 3.1.2.8. 生成 SWC 内存映射头文件

表3.9：生成 SWC 内存映射头文件（**Generate SWC Memory Mapping Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Tasks | — |
| 简要描述 |  | — |
| 描述 | Generate the memory mapping header file for one build environment and one Atomic Software Component. This task can be used in ECU scope or with preliminary scope to test software component. Note that the generated header file is compiler specific (#pragma statements). Inputs are: • From VFB Types: Properties of abstract sections given by SwAddrmethods, which in turn are referred by MemorySection as well as by MemMapAllocation • From Software Component Implementation, element MemorySection: Names of the individual abstract sections (preprocessor macros) used in the code. • From Preconfigured Configuration for module "MemMap": Collection of compiler specific configuration elements. • From ECU Configuration for module "MemMap" : MemMapAllocation - This is the concrete mapping for this environment. • From ECU Configuration: Find (optionally) the list of used software component implementations by usage of the RTE ECU Configuration "RteSwComponentType.RteImplementationRef" | — |
| 执行者 | ECU Integrator | 1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | Atomic Software Component Implementation | 1 MemorySections: MemorySections defined for an Atomic Software Component. Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Configuration Values | 1 MemMapAllocation: Mapipng of the abstract sections (SwAddressMethods for generic mapping resp. Memory Section Elements for specific mapping) to the compiler specific MemMapAddressingModes. Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Module Preconfigured Configuration | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation. Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Types | 1..* SwAddrMethod: Referred SwAddrMethods Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Configuration Values | 0..1 RteImplementationRef: Existence of SWCs could be identified by usage of the RTE ECU Configuration "Rte SwComponentType.RteImplementationRef" Meth.bindingTime = SystemDesignTime |
| 产出 | Standard Header Files | 1 SWC_MemMap: One header per software component type for a given build environment. The file name follows the pattern {componentType Name}_MemMap.h in which the prefix componentType Name is determined by the software component type name. For more detailed rules on the name of the generated file refer to document ID 128 CP_SWS_Memory Mapping. Meth.bindingTime = CodeGenerationTime |

#### 3.1.3. 工作产品

##### 3.1.3.1. 通用文档

表3.10：通用文档（**General Documentation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 |  | — |
| 描述 | General documentation link to a given work product | — |
| 种类 | Custom | — |
| 聚合于 | General Deliverable | 0..* |
| 产出者 | Add General Documentation | 1 |

##### 3.1.3.2. 替代名称集合

表3.11：替代名称集合（**Alias Name Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Set of alias names for AUTOSAR model elements for usage outside of AUTOSAR. | — |
| 描述 | Set of alias names, each consisting of the name (string) itself and the reference to the model element it renames. Each reference to a model element is either a reference to an Identifiable or to an entry in an ECU Flat Map or System Flat Map. For an explanation of uses cases see task Define Alias Names. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..1 Alias names valid in the context of the delivered components. |
| 聚合于 | System Description | 0..* |
| 产出者 | Define Alias Names | 1 |
| 消费者 | Add Documentation to the Software Component | 0..* Optional input in order to refer to unique names defined in an Alias Name Set (e.g. System Constants). |
| 消费者 | Generate A2L | 0..* |
| 使用的元模型元素 | AliasNameSet 1 | — |

##### 3.1.3.3. 已求值变体集合

表3.12：已求值变体集合（**Evaluated Variant Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | A set of evaluated variants | — |
| 描述 | This artifact represents a table defining which ArElements or ArPackages (referrred as "evaluated Elements") are able to support one or more particular variant. It can thus be used to document which variants are support by a certain delivery, e.g. of a software component or of a system. In other words, for a given set of evaluatedElements this element represents a table of evaluated variants, where each PredefinedVariant represents one column. In this column each descendant sw SystemConstantValue (part of System Constant Value Set) resp. postbuildVariantCriterionValue (part of Postbuid Variant Set) represents one entry. In a graphical representation each swSystemConstantValueSet / postBuildVariantCriterionValueSet could be used as an intermediate headline in the table column. The Evaluated Variant Set comes with an attribute "approvalStatus". If this is set to "APPROVED" it expresses that the evaluatedElements are known be valid for the given evaluated variants. Note that an evaluatedElement could be another Evaluated Variant Set. This allows to establish a hierarchy of EvaluatedVariantSets. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..1 |
| 聚合于 | ECU Extract of System Variant Model | 0..* |
| 聚合于 | System Description | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define System Variants | 1 |
| 产出者 | Evaluate Variant | 1 |
| 产出者 | Define Integration Variant | 0..1 Meth.bindingTime = SystemDesignTime |
| 产出者 | Define VFB Variants | 0..* |
| 消费者 | Evaluate Variant | 0..1 |
| 消费者 | Extract ECU System Variant Model | 0..* |
| 使用的元模型元素 | EvaluatedVariantSet 1 | — |

##### 3.1.3.4. AUTOSAR 规范

| Deliverable | Autosar Specification |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work |  |  |
| Brief Description |  |  |  |
| Description | An Autosar specification that is part of the Autosar standard. E.g. Software Component Template, Main Requirements, Autosar Model Constraints, Specification of Communication, etc. |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Deliverable | Autosar Specification |  |  |
| Consumed by | Create Profile of Data Exchange Point | 0..* | The Autosar specifications that are analyzed in order to figure out which data is required for the given data exchange point. |

##### 3.1.3.5. 通用 AUTOSAR 工件

表3.13：通用 AUTOSAR 工件（**General Autosar Artifact**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Describes the meta data for an AUTOSAR artifact. | — |
| 描述 | This artifact represents the data which are common to all AUTOSAR XML artifacts. Each file starts with the root element AUTOSAR. The content of such an artifact below this root element is organized by packages using the element ARPackage. Packages can be nested. It is important to understand, that the hierarchy defined via packages and other aggregated elements can (in general) span over several XML files, i.e. over several artifacts. That means, if an aggregation is "split" between several files, each file is considered as a separate artifact by the methodology, even if the elements are formally aggregated within the same package. All elements derived from meta-class Identifiable can carry documentation and administrative description based on the element AdminData. Note that ARPackage is itself derived from Identifiable, so there can be AdminData for the top-level package, for sub-packages and for more specific elements (derived from Identifiable) as well. The AdminData among other things contain revision information (including the artifact version) based on the metamodel element DocRevision . | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | General Deliverable | 0..* |
| 产出者 | Define ASIL For AUTOSAR Element | 1 |
| 产出者 | Define Admin Data | 1 |
| 产出者 | Allocate Safety Measure | 0..* Allocated Elements: |
| 产出者 | Allocate Safety Requirement | 0..* Allocated Elements: |
| 消费者 | Define ASIL For AUTOSAR Element | 1 |
| 消费者 | Validate Compliance of Autosar Model against Profile for Data Exchange Point | 1 An Autosar model can be validated against the Agreed Profile for Data Exchange Point. Default values of attributes that are not defined in the Agreed Profile of Data Exchange Point are retrieved from the Baseline Profile of Data Exchange Point. |
| 消费者 | Allocate Safety Measure | 1..* |
| 消费者 | Allocate Safety Requirement | 1..* |
| 消费者 | Evaluate Variant | 1..* |
| 消费者 | Create Profile of Data Exchange Point | 0..* The analysis of existing Autosar models that are typically exchanged at a specific Data Exchange Point can help during the development of a Profile of Data Exchange Point. |
| 消费者 | Define Safety Measure | 0..* |
| Consumed | Define Safety Requirement | 0..* |
| Use meta element | ARPackage | 1 |
| 使用的元模型元素 | AUTOSAR 1 | — |

##### 3.1.3.6. 通用交付物

| Deliverable | General Deliverable |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products |  |  |
| Brief Description | General data for an XML based deliverable within AUTOSAR. |  |  |
| Description | General data for an XML based deliverable within AUTOSAR : Especially it contains a catalog of all included artifacts. These can be AUTOSAR artifacts (see General Autosar Artifact) or non-AUTOSAR artifacts (see General Non AUTOSAR Artifact). An AUTOSAR XML artifact which is contained in the catalog may refer to an non AUTOSAR Artifact whithin the catalog via the metamodel element AutosarEngineeringObject (refer to document ID 202 FO_TPS_GenericStructureTemplate for further description). |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | General Autosar Artifact | 0..* |  |
| Aggregates | General Documentation | 0..* |  |
| Aggregates | General Non Autosar Artifact | 0..* |  |

##### 3.1.3.7. 通用非 AUTOSAR 工件

表3.14：General Non Autosar Artifact（**General Non Autosar Artifact**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Describes the data for a non AUTOSAR artifact. | — |
| 描述 | Describes the data for a non AUTOSAR artifact. | — |
| 种类 | Custom | — |
| 聚合于 | General Deliverable | 0..* |
| 消费者 | Provide RTE Calibration Dataset | 1..* input from calibration process |
| 消费者 | Create Profile of Data Exchange Point | 0..* Custom specification for data exchange (textual or non-AUTOSAR exchange format (e.g. FIBEX, DBC, LDF)) |

##### 3.1.3.8. 后构建变体集合

表3.15：后构建变体集合（**Postbuild Variant Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Set of Postbuild Variant Criterion Values used to define post-build variants of the software. | — |
| 描述 | Set of Postbuild Variant Criterion Values used to define post-build variants of the software. Such a set does not necessarily define a variant which is actually used. To define a meaningful variant in the production process, such a set is to be used via reference by artifact Predefined Variant. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..1 |
| 聚合于 | ECU Extract of System Variant Model | 0..* |
| 聚合于 | System Description | 0..* |
| 聚合于 | VFB System | 0..* |
| 输入/输出 | Define System Variants | 1 |
| 输入/输出 | Define Integration Variant | 0..* |
| 输入/输出 | Define VFB Variants | 0..* |
| 消费者 | Generate RTE Postbuild Dataset | 1 |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..1 |
| 消费者 | Generate RTE Prebuild Dataset | 0..1 |
| 消费者 | Evaluate Variant | 0..* |
| 消费者 | Extract ECU System Variant Model | 0..* |
| 使用的元模型元素 | PostBuildVariantCriterion ValueSet 1 | — |

##### 3.1.3.9. 预定义变体

表3.16：预定义变体（**Predefined Variant**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Defines a variant predefined for usage in subsequent process steps. | — |
| 描述 | Defines one variant of a software description for delivery and/or usage in subsequent process steps. The actual definition of all settings which make up this variant is given by attached System Constant Value Set (all settings which are resolved prior to post-build) and/or Postbuid Variant Set (all settings which are resolved after software build). These sets may be part of the same artifact or may be separated artifacts. Via these settings, the actual values which make up a particular variant, are selected. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | ECU Extract of System Variant Model | 0..* |
| 聚合于 | System Description | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define Integration Variant | 1 Meth.bindingTime = SystemDesignTime |
| 产出者 | Define System Variants | 1 |
| 产出者 | Define VFB Variants | 0..* |
| 消费者 | Generate BSW Module Prebuild Data Set | 1 |
| 消费者 | Generate RTE Postbuild Dataset | 1 |
| 消费者 | Generate RTE Prebuild Dataset | 1 |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..1 |
| 消费者 | Evaluate Variant | 0..* |
| 消费者 | Extract ECU System Variant Model | 0..* |
| 消费者 | Generate Component Prebuild Data Set | 0..* |
| 使用的元模型元素 | PredefinedVariant 1 | — |

##### 3.1.3.10. 标准头文件

表3.17：标准头文件（**Standard Header Files**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Overall header files to be included by each standardized BSW module, optionally also by Software Component code. | — |
| 描述 | Overall header files to be included by each standardized BSW module, optionally also by Software Component code. For simplicity of the methodology, these are modeled as one artifact though in practice these are several different files: • (<prefixes>_)MemMap.h - defines a common set of macros in order to define abstract memory sections for code and data in the source code . The prefixes indicates whether the scope is limited to a component, module or some other source code area (e.g. an ICC2 BSW cluster). Note that the usage of one MemMap.h for the complete BSW is possible, but deprecated. It is also possible to use a completely different filename via explicit declaration in the BSW Module Implementation Description. • Std_Types.h - defines a common set of C data types for usage within the basic software, this header includes the following two headers: | — |
| 种类 | Source Code | — |
| 产出者 | Generate BSW Memory Mapping Header | 1 BSW_MemMap: The memory mapping header file to be used for one or more BSW modules in a given build environment. The file name has in the standardized case a form like {Mip}_MemMap.h in which the prefixes {Mip} are determined by the BSW module (or BSW cluster) name and optional infixes. However, it is also possible to create a completely different filename via explicit declaration in the BSW Module Implementation. For more detailed rules on the name of the generated file refer to document ID 128 CP_SWS_Memory Mapping. |
| 产出者 | Generate SWC Memory Mapping Header | 1 SWC_MemMap: One header per software component type for a given build environment. The file name follows the pattern {componentType Name}_MemMap.h in which the prefix componentType Name is determined by the software component type name. For more detailed rules on the name of the generated file refer to document ID 128 CP_SWS_Memory Mapping. Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement a BSW Module | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Re-compile Component in ECU context | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement Atomic Software Component | 0..1 Meth.bindingTime = CodeGenerationTime |

##### 3.1.3.11. 系统常量值集合

表3.18：系统常量值集合（**System Constant Value Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Work Products | — |
| 简要描述 | Set of System Constant Values used to handle variants. | — |
| 描述 | Set of System Constant Values used to define pre-build variants of the software. Such a set does not necessarily define a variant which is actually used. To define a meaningful variant in the production process, such a set is to be used via reference by artifact Predefined Variant. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | ECU Extract of System Variant Model | 0..* |
| 聚合于 | System Description | 0..* |
| 聚合于 | VFB System | 0..* |
| 输入/输出 | Define System Variants | 1 |
| 输入/输出 | Define Integration Variant | 0..* |
| 输入/输出 | Define VFB Variants | 0..* |
| 消费者 | Generate BSW Module Prebuild Data Set | 1 |
| 消费者 | Generate RTE Prebuild Dataset | 1 |
| 消费者 | Generate Component Prebuild Data Set | 1..* Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Evaluate Variant | 0..* |
| 消费者 | Extract ECU System Variant Model | 0..* |
| 使用的元模型元素 | SwSystemconstantValue Set 1 | — |

#### 3.1.4. 角色

表3.19：Safety Engineer（**Safety Engineer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | The AUTOSAR Partnership development defines standard artifacts. | — |
| 描述 |  | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Role responsible for the overall design of the Basic Software. | — |
| 描述 | Role responsible for the overall design of the Basic Software. In contrast to the Basic Software Module Developer he is responsible for the consistency of interfaces and data types between modules. | — |
| 执行 | Define BSW Behavior | 1 |
| 执行 | Define BSW Entries | 1 |
| 执行 | Define BSW Interfaces | 1 |
| 执行 | Define BSW Types | 1 |
| 执行 | Create Transformer Specification | 0..1 |
| 执行 | Define VFB NvBlock Software Component | 0..1 |
| 执行 | Define Vendor Specific Module Definition | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Role responsible to develop and deliver a Basic Software Module. | — |
| 描述 |  | — |
| 执行 | Compile BSW Core Code | 1 |
| 执行 | Create Library | 1 |
| 执行 | Define BSW Entries | 1 |
| 执行 | Define BSW Interfaces | 1 |
| 执行 | Define BSW Module Timing | 1 |
| 执行 | Define BSW Types | 1 |
| 执行 | Define Memory Addressing Modes | 1 |
| 执行 | Develop BSW Module Generator | 1 |
| 执行 | Generate BSW Module Prebuild Data Set | 1 |
| 执行 | Generate BSWM Contract Header Files | 1 |
| 执行 | Implement a BSW Module | 1 |
| 执行 | Configure Memmap Allocation | 0..1 |
| 执行 | Define Vendor Specific Module Definition | 0..1 |
| 执行 | Generate BSW Memory Mapping Header | 0..1 |
| 执行 | Measure Component Resources | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | The calibration engieer determines the calibration parameters of an ECU. | — |
| 描述 |  | — |
| 执行 | Define VFB Parameter Component | 1 |
| 执行 | Generate A2L | 1 |
| 执行 | Create MC Function Model | 0..1 |
| 执行 | Define VFB Constants | 0..1 |
| 执行 | Provide RTE Calibration Dataset | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | The certification agency verifies the conformance of artifacts with respect to the standard artifacts defined by the autosar consortium. | — |
| 描述 |  | — |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Integrates the complete software on an ECU. | — |
| 描述 | Integrates the complete software on an ECU, which includes generating necessary code and completing the configuration of all software components and basic software modules. | — |
| 执行 | Compile ECU Source Code | 1 |
| 执行 | Configure Com | 1 |
| 执行 | Configure Diagnostics | 1 |
| 执行 | Configure ECUC | 1 |
| 执行 | Configure IO Hardware abstraction | 1 |
| 执行 | Configure MCAL | 1 |
| 执行 | Configure Mode Management | 1 |
| 执行 | Configure NvM | 1 |
| 执行 | Configure OS | 1 |
| 执行 | Configure RTE | 1 |
| 执行 | Configure Transformer | 1 |
| 执行 | Configure Watchdog Manager | 1 |
| 执行 | Connect Service Component | 1 |
| 执行 | Create Library | 1 |
| 执行 | Create Service Component | 1 |
|  | Define ECU Timing | 1 |
| 执行 | Define Integration Variant | 1 |
| 执行 | Extract the ECU Communication | 1 |
|  | Generate BSW Configuration Code | 1 |
|  | Generate BSW Memory Mapping Header | 1 |
|  | Generate Base Ecu Configuration | 1 |
| 执行 | Generate ECU Executable | 1 |
| 执行 | Generate Local MC Data Support | 1 |
|  | Generate OS | 1 |
|  | Generate RTE | 1 |
| 执行 | Generate RTE Postbuild Dataset | 1 |
| 执行 | Generate RTE Prebuild Dataset | 1 |
| 执行 | Generate SWC Memory Mapping Header | 1 |
| 执行 | Generate Scheduler | 1 |
|  | Generate Updated ECU Configuration | 1 |
|  | Measure Resources | 1 |
|  | Provide RTE Calibration Dataset | 1 |
|  | Configure Memmap Allocation | 0..1 |
|  | Create MC Function Model | 0..1 |
| 执行 | Define VFB NvBlock Software Component | 0..1 |
|  | Extend Topology | 0..1 |
| 执行 | Extract ECU Rapid Prototyping Scenario | 0..1 |
| 执行 | Extract ECU System Timing | 0..1 |
| 执行 | Extract ECU System Variant Model | 0..1 |
|  | Extract ECU Topology | 0..1 |
| 执行 | Flatten Software Composition | 0..1 |
| 执行 | Generate Component Header File in Vendor Mode | 0..1 |
| 执行 | Generate or Adjust ECU Flat Map | 0..1 |
| 执行 | Map Software Component to BSW | 0..1 |
| 执行 | Measure Component Resources | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Designer of software components and VFB systems. | — |
| 描述 |  | — |
| 执行 | Add Documentation to the Software Component | 1 |
| 执行 | Define Atomic Software Component Internal Behavior | 1 |
| 执行 | Define Complex Driver Component | 1 |
| 执行 | Define Consistency Needs | 1 |
| 执行 | Define ECU Abstraction Component | 1 |
| 执行 | Define VFB Application Software Component | 1 |
| 执行 | Define VFB Composition Component | 1 |
| 执行 | Define VFB Constants | 1 |
| 执行 | Define VFB Interfaces | 1 |
| 执行 | Define VFB Modes | 1 |
| 执行 | Define VFB Sensor or Actuator Component | 1 |
| 执行 | Define VFB Timing | 1 |
| 执行 | Define VFB Types | 1 |
| 执行 | Define VFB Variants | 1 |
| 执行 | Define Wrapper Components to Integrate Legacy Software | 1 |
| 执行 | Map Software Component to BSW | 1 |
| 执行 | Define Partial Flat Map | 0..1 |
| 执行 | Define VFB Component Constraints | 0..1 |
| 执行 | Define VFB NvBlock Software Component | 0..1 |
| 执行 | Define VFB Top Level | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Developer of the software component code. | — |
| 描述 |  | — |
| 执行 | Define Consistency Needs | 1 |
| 执行 | Define Software Component Timing | 1 |
| 执行 | Define SymbolProps for Types | 1 |
|  | Generate Atomic Software Component Contract Header Files | 1 |
|  | Generate Component Header File in Vendor Mode | 1 |
|  | Generate Component Prebuild Data Set | 1 |
|  | Implement Atomic Software Component | 1 |
|  | Measure Component Resources | 1 |
|  | Re-compile Component in ECU context | 1 |
|  | Add Documentation to the Software Component | 0..1 |
|  | Compile Atomic Software Component | 0..1 |
| 执行 | Configure Memmap Allocation | 0..1 |
| 执行 | Define Atomic Software Component Internal Behavior | 0..1 |
| 执行 | Define Memory Addressing Modes | 0..1 |
| 执行 | Define Partial Flat Map | 0..1 |
| 执行 | Generate SWC Memory Mapping Header | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Creation, management, developement and integration of systems within the vehicle | — |
| 描述 |  | — |
| 执行 | Assign Top Level Composition | 1 |
| 执行 | Create Transformer Specification | 1 |
| 执行 | Define Communication Matrix | 1 |
| 执行 | Define E2E Transformer Technology | 1 |
| 执行 | Define ECU Description | 1 |
| 执行 | Define Frames | 1 |
| 执行 | Define Network Management | 1 |
| 执行 | Define PDU Gateway | 1 |
| 执行 | Define RTE Fan-out | 1 |
| 执行 | Define Secured PDUs | 1 |
| 执行 | Define Signal Gateway | 1 |
|  | Define Signal PDUs | 1 |
| 执行 | Define Signal Path Constraints | 1 |
|  | Define System Timing | 1 |
| 执行 | Define System Topology | 1 |
| 执行 | Define System Variants | 1 |
|  | Define System View Mapping | 1 |
|  | Define TP | 1 |
| 执行 | Define Transformation Chain | 1 |
| 执行 | Define Transformation Technology | 1 |
|  | Deploy Software Component | 1 |
|  | Derive Communication Needs | 1 |
|  | Extend Composition | 1 |
|  | Extract the ECU Communication | 1 |
|  | Flatten Software Composition | 1 |
|  | Generate or Adjust System Flat Map | 1 |
|  | Select Design Time Variant | 1 |
|  | Select Software Component Implementation | 1 |
| 执行 | Set System Root | 1 |
| 执行 | Define VFB Component Constraints | 0..1 |
| 执行 | Define VFB Composition Component | 0..1 |
|  | Define VFB Constants | 0..1 |
| 执行 | Define VFB Top Level | 0..1 |
|  | Extend Topology | 0..1 |
|  | Extract ECU Rapid Prototyping Scenario | 0..1 |
|  | Extract ECU System Timing | 0..1 |
| 执行 | Extract ECU System Variant Model | 0..1 |
|  | Extract ECU Topology | 0..1 |
|  | Generate or Adjust ECU Flat Map | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 | Responsibility for the quality of the description of the non-AUTOSAR system and its integration into the AUTOSAR process. | — |
| 描述 | The non-AUTOSAR System Integrator is responsible for the quality of the Description of the non-AUTOSAR System, the correct definition of the VFB Integration Connector, and the integration of the non-AUTOSAR system into the AUTOSAR process via the translation of the non-AUTOSAR artifacts. | — |
| 执行 | Define VFB Integration Connector | 1 |
| 执行 | Translate Non-Autosar Description to Autosar Description | 1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 |  | — |
| 描述 |  | — |
| 执行 | Define Rapid Prototyping Scenario | 1 |
| 执行 | Generate Rapid Prototyping Wrapper | 1 |
| 执行 | Refine Rapid Prototyping Scenario | 1 |
| 执行 | Compile Atomic Software Component | 0..1 |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Roles | — |
| 简要描述 |  | — |
| 描述 | Responsibility for the safety relevant steps in the AUTOSAR development process | — |
| 执行 | Add Independence Relation | 1 |
| 执行 | Allocate Safety Measure | 1 |
| 执行 | Allocate Safety Requirement | 1 |
| 执行 | Decompose Safety Requirement | 1 |
| 执行 | Define ASIL For AUTOSAR Element | 1 |
| 执行 | Define Safety Measure | 1 |
| 执行 | Define Safety Requirement | 1 |
| 执行 | Map Safety Requirement to Safety Measure | 1 |
| 执行 | Refine Safety Requirement | 1 |

#### 3.1.5. 工具

##### 3.1.5.1. 编译器

| Tool | Compiler |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Guidance |  |  |
| Brief Description |  |  |  |
| Description |  |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Compile Atomic Software Component | 1 |  |
| Used | Compile BSW Configuration Data | 1 |  |
| Used | Compile BSW Core Code | 1 |  |
| Used | Compile Configured BSW | 1 |  |
| Used | Compile ECU Source Code | 1 |  |
| Used | Compile Generated BSW | 1 |  |
| Used | Compile Unconfigured BSW | 1 |  |
| Used | Re-compile Component in ECU context | 1 |  |

##### 3.1.5.2. 链接器

| Tool | Linker |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Guidance |  |  |
| Brief Description |  |  |  |
| Description |  |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Generate ECU Executable | 1 |  |
| Used | Link ECU Code after Precompile Configuration | 1 |  |
| Used | Link ECU Code during Link Time Configuration | 1 |  |
| Used | Link ECU Code during Post-Build Time | 1 |  |

#### 3.1.6. 诊断

##### 3.1.6.1. 工作产品


| Deliverable | Diagnostic Extract |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Diagnostics::Work Products |  |  |
| Brief Description |  |  |  |
| Description | Generic deliverable for defining diagnostic information. It is used in different roles (Diagnostic Extract categories). In each role, this deliverable may contain variation points in its ARXML artifacts which need to be bound in later steps. If such variation points are present, the Diagnostic Description may optionally include PredefinedVariants in order to predefine variants for later selection and an Evaluated Variant Set. |  |  |
| Kind |  |  |  |
| Extended By | Diagnostic Abstract System Description, Diagnostic ECU Extract, Diagnostic System Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Deliverable | Diagnostic Abstract System Description |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Diagnostics::Work Products |  |  |
| Brief Description |  |  |  |
| Description | This deliverable represents a more or less high-level definition of diagnostic information that can be taken as a template for creating Diagnostic System Extract or Diagnostic ECU Extract. It corresponds to an Diagnostic Extract with DiagnosticContributionSet of category DIAGNOSTICS_ ABSTRACT_SYSTEM_DESCRIPTION. |  |  |
| Kind |  |  |  |
| Extends | Diagnostic Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Develop Diagnostic Abstract System Description | 1 |  |
|  | Develop Diagnostic Requirements | 0..* |  |
| Deliverable | Diagnostic System Extract |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Diagnostics::Work Products |  |  |
| Brief Description |  |  |  |
| Description | This deliverable represents concrete diagnostic information for several ECUs. It corresponds to an Diagnostic Extract with DiagnosticContributionSet of category DIAGNOSTICS_SYSTEM_EXTRACT. |  |  |
| Kind |  |  |  |
| Extends | Diagnostic Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Develop Application Software | 0..* | Diagnostic information relevant to the SW-Cs is provided as a part of the Diagnostic System Extract and can contain relationships to the SW-C's service needs. |
| Produced by | Develop Basic Software | 0..* |  |
| Produced by | Develop Diagnostic Requirements | 0..* |  |
| Consumed by | Develop Application Software | 0..* | The Diagnostic System Extract contains diagnostic information that serves as a requirement for the software developer. |
| Consumed by | Develop Basic Software | 0..* |  |
| Consumed by | Develop Diagnostic Requirements | 0..* |  |
| Consumed by | Integrate Diagnostic Information | 0..* |  |
| Deliverable | Diagnostic ECU Extract |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Diagnostics::Work Products |  |  |
| Brief Description |  |  |  |
| Description | This deliverable represents concrete diagnostic information for a single ECUs. It corresponds to an Diagnostic Extract with DiagnosticContributionSet of category DIAGNOSTICS_ECU_EXTRACT. |  |  |
| Kind |  |  |  |
| Extends | Diagnostic Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Integrate Diagnostic Information | 1..* | complete DE: |
| Produced by | Develop Diagnostic Requirements | 0..* |  |
| Consumed by | Generate Base Ecu Configuration | 0..1 |  |
| Consumed by | Generate Updated ECU Configuration | 0..1 |  |
| Consumed by | Integrate Software for ECU | 0..1 | complete DE: |
| Consumed by | Prepare ECU Configuration | 0..1 |  |
| Consumed by | Update ECU Configuration | 0..1 |  |
| Consumed by | Integrate Diagnostic Information | 0..* | partially filled DE: |

#### 3.1.7. 安全

##### 3.1.7.1. 任务

###### 3.1.7.1.1. 定义安全需求


表3.20：定义安全需求（**Define Safety Requirement**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Add Safety Requirements to work products. | — |
| 描述 | This task creates a safety requirement and sets the corresponding attributes such as ASIL. The allocation to an AUTOSAR element and the mapping to a safety measure are not part of this task. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | General Autosar Artifact | 0..* |
| 产出 | Safety Requirement | 1 |

###### 3.1.7.1.2. 定义安全措施


表3.21：定义安全措施（**Define Safety Measure**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Add Safety Measures to work products. | — |
| 描述 | This task creates a safety measure and sets the corresponding attributes such as ASIL. The allocation to an AUTOSAR element and the mapping to a safety requirement are not part of this task. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | General Autosar Artifact | 0..* |
| 产出 | Safety Measure | 1 |

###### 3.1.7.1.3. 为 AUTOSAR 元素定义 ASIL

表3.22：为 AUTOSAR 元素定义 ASIL（**Define ASIL For AUTOSAR Element**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Provide ASIL attribute for AUTOSAR element. | — |
| 描述 | According to the safety extensions, AUTOSAR elements can carry ASIL attributes if they are safety relevant. This task assigns the ASIL attribute to an AUTOSAR element. The assignment of the ASIL attribute can also be done for safety requirements and safety measures. This is covered by the tasks "Define Safety Requirement" and "Define Safety Measure". | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | General Autosar Artifact | 1 |
| 产出 | General Autosar Artifact | 1 |

###### 3.1.7.1.4. 细化安全需求

表3.23：细化安全需求（**Refine Safety Requirement**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Refine existing Safety Requirements by adding more detailed safety requirements and organize them in an appropriate hierarchy. | — |
| 描述 | If safety requirements are not detailed enough to allocate them directly to appropriate AUTOSAR elements, it is necessary to refine them first. The refinement will add new safety requirements which are in a hierarchy relation to existing safety requirements. This task adds the corresponding "REFINEMENT" relation between the original requirement and the newly created requirements. This task can be done on different levels, depending on the level of details of the safety requirements. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Requirement | 1 Original Safety Requirement: |
| 产出 | Safety Requirement | 1..* Refined Safety Requirement: |

###### 3.1.7.1.5. 分解安全需求

表3.24：分解安全需求（**Decompose Safety Requirement**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Decompose existing Safety Requirements into independent Safety Requirements to tailor the ASIL. | — |
| 描述 | By ASIL decomposition it is possible to decompose a safety requirement into two new safety requirements with potentially lower ASILs. This can be done, if the independence (freedom of interference) for the resulting requirements can be demonstrated. The modeling of the corresponding INDEPENDENCE relation is covered by task "Add Independence Relation". This task adds the corresponding "DECOMPOSITION" reference. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Requirement | 1 Initial Safety Requirement: |
| 产出 | Safety Requirement | 2 Decomposed Safety Requirements: |

###### 3.1.7.1.6. 分配安全措施

表3.25：分配安全措施（**Allocate Safety Measure**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Allocate Safety Measure to AUTOSAR elements. | — |
| 描述 | Safety measures which are safety mechanisms realized in AUTOSAR are allocated to AUTOSAR elements in order to describe what elements are involved in the provision of a safety measure. This task adds the corresponding "ALLOCATION" reference. The reference can be contained by the AUTOSAR element or by the safety measure. The allocation can be done on different levels, depending on the granularity of the safety measures and the availability of the appropriate elements in the model. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Measure | 1 |
| 消费 | General Autosar Artifact | 1..* |
| 产出 | Safety Measure | 0..1 Allocated Safety Measure: |
| 产出 | General Autosar Artifact | 0..* Allocated Elements: |

###### 3.1.7.1.7. 分配安全需求

表3.26：分配安全需求（**Allocate Safety Requirement**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Allocate Safety Requirement to AUTOSAR elements. | — |
| 描述 | Safety requirements are allocated to AUTOSAR elements in order to fulfill the needs of ISO 26262. By this allocation, AUTOSAR elements obtain their ASIL attribute (if not defined e.g. during previous development of the element). This task adds the corresponding allocation reference to the AUTOSAR element. The reference can be contained by the AUTOSAR element or by the safety requirement. The allocation can be done on different levels, depending on the granularity of the safety requirements and the availability of the appropriate elements in the model. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Requirement | 1 |
| 消费 | General Autosar Artifact | 1..* |
| 产出 | Safety Requirement | 0..1 Allocated Requirement: |
| 产出 | General Autosar Artifact | 0..* Allocated Elements: |

###### 3.1.7.1.8. 将安全需求映射到安全措施

表3.27：将安全需求映射到安全措施（**Map Safety Requirement to Safety Measure**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Map Safety Requirements to Safety Measures | — |
| 描述 | The mapping relates safety requirements with safety measures. This task creates the corresponding MAPS_TO relation. The mapping relation can either be contained by the safety requirement or by the safety measure. The mapping can be done on different levels, depending on the granularity of the safety requirements and the safety measures. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Measure | 1 |
| 消费 | Safety Requirement | 1 |
| 产出 | Safety Measure | 0..1 |
| 产出 | Safety Requirement | 0..1 |

###### 3.1.7.1.9. 添加独立性关系

表3.28：添加独立性关系（**Add Independence Relation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Tasks | — |
| 简要描述 | Add Independence relation to decomposed requirements. | — |
| 描述 | This task establishes the INDEPENDENCE relation between requirements. The relation is established between a decomposed requirement and a requirement which express a means to achieve freedom from interference for the two requirements into which the decomposed requirement is decomposed by the task Decompose Safety Requirement. Obviously, this task is processed in the context of the decomposition of safety requirements. | — |
| 执行者 | Safety Engineer | 1 |
| 消费 | Safety Requirement | 1..* |
| 产出 | Safety Requirement | 1..* Linked Requirement: |

##### 3.1.7.2. 工作产品

###### 3.1.7.2.1. 安全扩展


| Deliverable | Safety Extensions |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products |  |  |
| Brief Description | Safety Extensions |  |  |
| Description | This element represents an abstract deliverable containing all safety relevant artifacts. Several specializations of this deliverable are used to demonstrate the handling of safety extensions in specific development activities. The explicit separation of the safety information from the AUTOSAR models allows an independent exchange and processing of them. |  |  |
| Kind | Delivered |  |  |
| Extended By | Software Component Safety Extensions, System Safety Extensions, VFB Safety Extensions |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Safety Measure | 0..* |  |
| Aggregates | Safety Requirement | 0..* |  |
| Deliverable | VFB Safety Extensions |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products |  |  |
| Brief Description | Vfb Safety Extensions |  |  |
| Description | This deliverable contains all safety information related to VFB elements. |  |  |
| Kind | Delivered |  |  |
| Extends | Safety Extensions |  |  |
| Deliverable | VFB Safety Extensions |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Define VFB Safety Information | 1 |  |
| Consumed by | Define Software Component Safety Information | 1 |  |
| Consumed by | Define System Safety Information | 1 |  |
| Deliverable | Software Component Safety Extensions |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products |  |  |
| Brief Description | Software Component Safety Extensions |  |  |
| Description | This deliverable contains all safety information related to software components. |  |  |
| Kind | Delivered |  |  |
| Extends | Safety Extensions |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Define Software Component Safety Information | 1 |  |
| Consumed by | Define System Safety Information | 1 |  |
| Deliverable | System Safety Extensions |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products |  |  |
| Brief Description | System Safety Extensions |  |  |
| Description | This deliverable contains all safety information related to system elements (see Deliverable "System Description" for more details). |  |  |
| Kind | Delivered |  |  |
| Extends | Safety Extensions |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Define System Safety Information | 1 |  |

###### 3.1.7.2.2. 安全需求

表3.29：安全需求（**Safety Requirement**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products | — |
| 简要描述 | Safety Requirement | — |
| 描述 | This artifact represents a safety requirement and the corresponding ASIL attribute. ISO 26262 defines a hierarchy of safety requirements: safety goals, technical, hardware and software. Furthermore, it might be the case that safety requirements are specified outside the AUTOSAR model (external) and are only referenced. Thus, the safety requirement can have one of the following categories: • SAFETY_GOAL • SAFETY_FUNCTIONAL • SAFETY_TECHNICAL • SAFETY_SOFTWARE • SAFETY_HARDWARE • SAFETY_EXTERNAL For details refer to ISO 26262-3, 4, 9. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Safety Extensions | 0..* |
| 产出者 | Decompose Safety Requirement | 2 Decomposed Safety Requirements: |
| 产出者 | Define Safety Requirement | 1 |
| 产出者 | Add Independence Relation | 1..* Linked Requirement: |
| 产出者 | Refine Safety Requirement | 1..* Refined Safety Requirement: |
| 产出者 | Allocate Safety Requirement | 0..1 Allocated Requirement: |
| 产出者 | Map Safety Requirement to Safety Measure | 0..1 |
| 消费者 | Allocate Safety Requirement | 1 |
| 消费者 | Decompose Safety Requirement | 1 Initial Safety Requirement: |
| 消费者 | Map Safety Requirement to Safety Measure | 1 |
| 消费者 | Refine Safety Requirement | 1 Original Safety Requirement: |
| 消费者 | Add Independence Relation | 1..* |
| 使用的元模型元素 | StructuredReq 1 | — |

###### 3.1.7.2.3. 安全措施

表3.30：安全措施（**Safety Measure**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Safety::Work Products | — |
| 简要描述 | Safety Measure | — |
| 描述 | This artifact represents a safety measure. A safety measure is an activity or solution to avoid systematic failures and to detect random hardware failures or control failures (see ISO 26262). The safety measure can have one of the following categories: • SAFETY_MEASURE • SAFETY_MECHANISM | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Safety Extensions | 0..* |
| 产出者 | Define Safety Measure | 1 |
| 产出者 | Allocate Safety Measure | 0..1 Allocated Safety Measure: |
| 产出者 | Map Safety Requirement to Safety Measure | 0..1 |
| 消费者 | Allocate Safety Measure | 1 |
| 消费者 | Map Safety Requirement to Safety Measure | 1 |
| 使用的元模型元素 | TraceableText 1 | — |

#### 3.1.8. 数据交换点

##### 3.1.8.1. 工作产品


| Deliverable | Baseline Profile of Data Exchange Point |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Data Exchange Point::Work Products |  |  |
| Brief Description | The Baseline Profile of Data Exchange Point specifies default values that are used when processing Profile of Data Exchange Points that do not specify all values. |  |  |
| Deliverable | Baseline Profile of Data Exchange Point |  |  |
| Description | The Baseline Profile of Data Exchange Point specifies default values that are used when processing Profile of Data Exchange Points that do not specify all values. Actual Profiles of Data Exchange Point only have to specify information that deviates from the default values provided in the Baseline Profile of Data Exchange Point. This Baseline Profile of Data Exchange Point is provided and standardized by AUTOSAR for each commonly used revision of the standard. |  |  |
| Kind | AUTOSAR XML |  |  |
| Relation Type | Related Element | Mult. | Note |
| Consumed by | Create Profile of Data Exchange Point | 1 | The Baseline Profile of Data Exchange Point defines the default values of the Profile. |
| Consumed by | Validate Compliance of Autosar Model against Profile for Data Exchange Point | 1 | The Baseline Profile of Data Exchange Point provides default values foe parameters that are not specified in the Agreed Profile of Data Exchange Point. |
| Deliverable | Profile of Data Exchange Point |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Data Exchange Point::Work Products |  |  |
| Brief Description | A Profile of Data Exchange Point specifies which parts of the Autosar standard are relevant for a specific data exchange scenario. |  |  |
| Description | A Profile of Data Exchange Point specifies which parts of the AUTOSAR standard are relevant for a specific data exchange scenario. Each Profile of Data Exchange Point shall specify the revision of the AUTOSAR standard that is used as the baseline. Additionally, it should contain a high-level description of the data exchange point by specifying the deliverable and the intended use as well a detailed specification of the relevant part of the meta model and the applicable constraints. A Profile of Data Exchange Point that describes an individual Data Exchange Point is based on a Baseline Profile of Data Exchange Point that is provided by AUTOSAR. The Profile of Data Exchange Point only needs to describe the parameters that differ from its Baseline Profile of Data Exchange Point. |  |  |
| Kind | AUTOSAR XML |  |  |
| Extended By | Agreed Profile of Data Exchange Point |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Create Profile of Data Exchange Point | 1 | The new Profile of Data Exchange Point |
| Consumed by | Create Agreed Profile for Data Exchange Point | 1..* | The Profiles of Data Exchange Point that are analyzed with respect to interoperability issues. |
| Consumed by | Create Profile of Data Exchange Point | 0..* | An existing Profile of Data Exchange Point that is used as a starting point for a new Profile of Data Exchange Point. E.g. start with a profile of an old tool version and tailor it so that new features are covered. |
| Deliverable | Agreed Profile of Data Exchange Point |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Common Elements::Data Exchange Point::Work Products |  |  |
| Brief Description | The Agreed Profile of Data Exchange Point is a Profile of Data Exchange Point that documents the agreed Data Exchange Point between partners |  |  |
| Deliverable | Agreed Profile of Data Exchange Point |  |  |
| Description | The Agreed Profile of Data Exchange Point is a Profile of Data Exchange Point that documents the agreed Data Exchange Point between partners. It can be used during the project to continuously evaluate if the exchanged AUTOSAR models still conform with the agreed contract. |  |  |
| Kind | AUTOSAR XML |  |  |
| Extends | Profile of Data Exchange Point |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Create Agreed Profile for Data Exchange Point | 1 | The Agreed Profile of Data Exchange Point |
| Consumed by | Validate Compliance of Autosar Model against Profile for Data Exchange Point | 1 | The DataFormatTailoring and Baseline sections of the Agreed Profile of Data Exchange Point can be used to configure the validation engine of Autosar Validation Tools (e.g. provide rules for existence of elements or switch on/off individual semantic constraints) |

### 3.2. 虚拟功能总线

本章包含用于开发 VFB 系统 的工作产品和任务 的定义。相关元模型元素的定义参见 [\[7, CP TPS Software Component Template\]](#ref-7)，VFB 概念参见 [\[6, CP EXP VFB\]](#ref-6)。

#### 3.2.1. 任务

##### 3.2.1.1. 定义 VFB 顶层

表3.31：定义 VFB 顶层（**Define VFB Top Level**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define the top level VFB composition of a concrete system. | — |
| 描述 | Define the top level composition of a VFB system. | — |
| 执行者 | Software Component Designer | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB Atomic Software Component | 0..* |
| 消费 | VFB Composition Component | 0..* |
| 消费 | VFB Modes | 0..* |
| 消费 | VFB Non AUTOSAR Component | 0..* |
| 消费 | VFB Parameter Component | 0..* |
| 产出 | VFB Top Level System Composition | 1 |

##### 3.2.1.2. 定义 VFB 组合组件

表3.32：定义 VFB 组合组件（**Define VFB Composition Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a Composition of VFB Software Components, i.e. a ComponentTypes which contains other Component Types. | — |
| 描述 | Define a Composition of VFB Software Components, i.e. a ComponentType which contains other Component Types. Iteration of this task can create a complete VFB system without the Atomic Software Components itself. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | VFB Atomic Software Component | 0..* |
| 消费 | VFB Composition Component | 0..* |
| 消费 | VFB Modes | 0..* |
| 消费 | VFB Non AUTOSAR Component | 0..* |
| 消费 | VFB Parameter Component | 0..* |
| 产出 | VFB Composition Component | 1 |

##### 3.2.1.3. 扩展组合

表3.33：扩展组合（**Extend Composition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Extend a software composistion with further compositions and atomic software components. | — |
| 描述 | This tasks describes the refinement of a delivered VFB System by extending an existing composition with further sub-elements, which could be software components (Atomic Software Components as well as Compositions), connectors or port groups, plus the related interfaces, data types and modes. The main use case is the refinement of the VFB description of a sub-system: New elements are added but the original delivery is not changed. | — |
| 执行者 | System Engineer | 1 |
| 消费 | VFB System | 1 initial system: |
| 产出 | VFB System | 1 extended system: |
| 产出 | VFB Atomic Software Component | 0..* |
| 产出 | VFB Composition Component | 0..* |
| 产出 | VFB Interfaces | 0..* |
| 产出 | VFB Modes | 0..* |
| 产出 | VFB Non AUTOSAR Component | 0..* |
| 产出 | VFB Parameter Component | 0..* |
| 产出 | VFB Software Component Mapping Constraints | 0..* |
| 产出 | VFB Types | 0..* |

##### 3.2.1.4. 定义 VFB 组件约束

表3.34：定义 VFB 组件约束（**Define VFB Component Constraints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define which components need to be deployed together, and which need to be deployed separately. | — |
| 描述 | In this task constraints for software components are defined. These constraints can on the one hand describe which SW-Cs should be mapped together to a single ECU, and which must be mapped to separate ECUs, without regard to any particular ECU or topology. This can be done by using the meta-model ComponentClustering and ComponentSeparation constraint. In fact, before the mapping process begins, it can be useful to impose the allocation of a predefined set of SW components onto the same ECU, especially if such a set is tightly linked from a functional point of view. In the same way, two critical SW components, performing some kind of redundancy, may be not suitable to run both on the same ECU. Thus, we call these two kinds of mapping constraints, respectively, ComponentClustering and ComponentSeparation. The Component Clustering constraint (also, clustering) is to be used for expressing that a certain set of SW components (atomic or not) shall be mapped (allocated) onto the same ECU. This is some kind of "execute together on same ECU" constraint. The ComponentSeparation constraint (also, separation) is to be used for expressing that two SWcomponents (atomic or not) shall not be mapped (allocated) onto the same ECU. This is some kind of "do not execute together on same ECU" constraint. | — |
| 执行者 | Software Component Designer | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | VFB Atomic Software Component | 2..* |
| 消费 | VFB Top Level System Composition | 1 |
| 消费 | VFB Composition Component | 1..* |
| 产出 | VFB Software Component Mapping Constraints | 1..* |

##### 3.2.1.5. 定义 VFB 应用软件组件

表3.35：定义 VFB 应用软件组件（**Define VFB Application Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define an ApplicationSoftwareComponentType on VFB level | — |
| 描述 | Define an ApplicationSwComponentType on VFB level. (i.e. without Internal Behavior and Implementation). | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | VFB Modes | 0..* |
| 产出 | VFB Atomic Application Software Component | 1 |

##### 3.2.1.6. 定义 VFB 传感器或执行器组件

表3.36：定义 VFB 传感器或执行器组件（**Define VFB Sensor or Actuator Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a VFB Sensor or Actuator Comnponent. | — |
| 描述 | Define a SensorActuatorSwComponentType on VFB level. (i.e. without Internal Behavior and Implementation). In addition to defining the ports, references to the required sensor/actuator hardrware shall be specified. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | ECU Resources Description | 0..* |
| 产出 | VFB Sensor Actuator Component | 1 |

##### 3.2.1.7. 定义 VFB 参数组件

表3.37：定义 VFB 参数组件（**Define VFB Parameter Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a VFB Parameter Component. | — |
| 描述 | Define a VFB Parameter Component. | — |
| 执行者 | Calibration Engineer | 1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 产出 | VFB Parameter Component | 1 |

##### 3.2.1.8. 定义 ECU 抽象组件

表3.38：定义 ECU 抽象组件（**Define ECU Abstraction Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define an EcuAbstractionSoftwareComponentType on VFB level. | — |
| 描述 | Define a EcuAbstractionSwComponentType on VFB level. (i.e. without Internal Behavior and Implementation). In addition to the defining the ports, references to required ECU or processor hardware elements shall be specified. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB AUTOSAR Standard Package | 1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | VFB Interfaces | 1 |
| 消费 | VFB Types | 1 |
| 消费 | ECU Resources Description | 0..1 |
| 消费 | VFB Modes | 0..* |
| 产出 | ECU Abstraction Software Component | 1 |

##### 3.2.1.9. 定义复杂驱动程序组件

表3.39：定义复杂驱动程序组件（**Define Complex Driver Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a ComplexDeviceDriverSwComponentType on VFB level. | — |
| 描述 | Define a ComplexDeviceDriverSwComponentType on VFB level. (i.e. without Internal Behavior and Implementation). In addition to the defining the ports, references to the required ECU or processor hardware elements shall be specified. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | ECU Resources Description | 0..* |
| 消费 | VFB Modes | 0..* |
| 产出 | Complex Driver Component | 1 |

##### 3.2.1.10. 定义 VFB NvBlock 软件组件

表3.40：定义 VFB NvBlock 软件组件（**Define VFB NvBlock Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define an NvBlockSwComponentType on VFB level. The NvBlockSwComponentType defines non volatile data which can be shared between SwComponentPrototypes. The non volatile data of the NvBlockSwComponentType are accessible via provided and required ports. | — |
| 执行者 | Basic Software Designer | 0..1 |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | Software Component Designer | 0..1 |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 |
| 消费 | Software Component Internal Behavior | 0..* This input is required to collect the requirements for the NvBlockNeeds from the using application software. |
| 消费 | VFB Modes | 0..* |
| 产出 | VFB NvBlock Software Component | 1 |

##### 3.2.1.11. 定义用于集成遗留软件的包装组件

表3.41：定义用于集成遗留软件的包装组件（**Define Wrapper Components to Integrate Legacy Software**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a wrapper component used to represent legacy software that is integrated into an AUTOSAR system. | — |
| 描述 | Define a wrapper component used to represent legacy software that is integrated into an AUTOSAR system. For the VFB system, this mainly means to define the corresponding port interfaces and data elements. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use port blueprints in order to create ports with standardized application interfaces. |
| 消费 | VFB Interfaces | 0..* |
| 消费 | VFB Modes | 0..* |
| 消费 | VFB Types | 0..* |
| 产出 | VFB Non AUTOSAR Component | 1 |

##### 3.2.1.12. 定义 VFB 接口

表3.42：定义 VFB 接口（**Define VFB Interfaces**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a set of Port Interface required by a system. | — |
| 描述 | Define a set of Port Interfaces required by a VFB system, to describe the communication of data via SWC ports. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Types | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use standardized Port Interfaces as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| 产出 | VFB Interfaces | 1..* |

##### 3.2.1.13. 定义 VFB 类型

表3.43：定义 VFB 类型（**Define VFB Types**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define a set of data types required by a system, but not already defined by AUTOSAR. | — |
| 描述 | Define a set of Autosar Data Types and related elements as far as visible on the VFB. Standardized types can be used as input in order to copy and refine them. The VFB Types will be used for specifying types of DataElements in Sender-Receiver PortInterfaces and argument/return values of Client-Server PortInterfaces. This task inludes (optionally) also the creation of a VFB Data Type mapping Set between application and implementation data types. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use standardized elements (e.g. Data Types, Compu Methods) as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| 产出 | VFB Types | 1..* |
| 产出 | VFB Data Type Mapping Set | 0..* |
| 聚合 | Define Local Calibration Parameters | 1 Define VFB types for Local Calibration: Use this task to define VFB types for Local Calibration. |

##### 3.2.1.14. 定义 VFB 模式

表3.44：定义 VFB 模式（**Define VFB Modes**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define modes that are used by the VFB components. | — |
| 描述 | Define modes (mode groups and the modes they contain) that are used by the VFB components. | — |
| 执行者 | Software Component Designer | 1 |
| 产出 | VFB Modes | 1..* |

##### 3.2.1.15. 定义 VFB 常量

表3.45：定义 VFB 常量（**Define VFB Constants**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define one or more VFB Constants. | — |
| 描述 | Define one or more VFB Constants as standalone artifact. Such constants can be referred in the specification of inital values at several places in the VFB descrption, such as port interfaces or declaration of local parameters or variables. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | Calibration Engineer | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | VFB Data Type Mapping Set | 0..* |
| 消费 | VFB Types | 0..* |
| 产出 | VFB Constants | 1..* |

##### 3.2.1.16. 定义 VFB 时序

表3.46：定义 VFB 时序（**Define VFB Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define VFB Timing (TimingDescription and TimingConstraints) for an Atomic Software Component or a Composition Component | — |
| 描述 | Define VFB Timing (TimingDescription and TimingConstraints) for an Atomic Software Component or a Composition Component | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Composition Component | 1..* |
| 消费 | VFB Interfaces | 1..* |
| 消费 | VFB AUTOSAR Standard Package | 0..1 |
| 消费 | VFB Atomic Software Component | 0..* |
| 消费 | VFB Non AUTOSAR Component | 0..* |
| 消费 | VFB Parameter Component | 0..* |
| 产出 | VFB Timing | 1 |

##### 3.2.1.17. 定义 VFB 变体

表3.47：定义 VFB 变体（**Define VFB Variants**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define variants for the artifacts of a VFB system. | — |
| 描述 | Define one or more variants for the artifacts of a VFB system. Defining one variant means creating a Predefined Variant related to the settings used by the VFB elements in scope. To do so, this task can make use of existing System Constant Value Sets and/or Postbuid Variant Sets or define new ones. Several Predefined Variants can be combined to one Evaluated Variant Set. | — |
| 执行者 | Software Component Designer | 1 |
| 消费 | VFB Top Level System Composition | 1 |
| 消费 | VFB Composition Component | 1..* |
| 消费 | VFB Timing | 0..1 |
| 消费 | VFB Atomic Software Component | 0..* |
| 消费 | VFB Interfaces | 0..* |
| 消费 | VFB Non AUTOSAR Component | 0..* |
|  | VFB Parameter Component | 0..* |
| 输入/输出 | Postbuild Variant Set | 0..* |
|  | System Constant Value Set | 0..* |
|  | Evaluated Variant Set | 0..* |
|  | Predefined Variant | 0..* |

##### 3.2.1.18. 定义 VFB 集成连接器

表3.48：定义 VFB 集成连接器（**Define VFB Integration Connector**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Define how the non-AUTOSAR system shall be connected to the AUTOSAR system. | — |
| 描述 | The VFB Integration Connector is used to represent the connection of the non-AUTOSAR system and the AUTOSAR system. Its contents and format depend on the way in which the non-AUTOSAR system is defined. To define the VFB Integration Connector the requirements on the connection are brought into the format of the Integration Connector. When the requirements are defined in a proprietary format the have to be translated to the format of the Integration Connector. When they are only informally defined or are even more tangible the format of the Integration Connector can be used to elicit, formalize, and analyze the connection requirements. | — |
| 执行者 | Non-AUTOSAR System Integrator | 1 |
| 消费 | Description of a Non-AUTO SAR System | 1 |
| 消费 | VFB System | 1 |
| 产出 | Integration Connector | 1 |
| 前驱 | Translate Non-Autosar Description to Autosar Description | 1 |

##### 3.2.1.19. 将非 AUTOSAR 描述转换为 AUTOSAR 描述


表3.49：Translate Non-Autosar Description to Autosar Description（**Translate Non-Autosar Description to Autosar Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Tasks | — |
| 简要描述 | Translate the description of the non-AUTOSAR system into a semantically equivalent AUTOSAR description (template). | — |
| 描述 | In order to incorporate the development of the non-AUTOSAR system into the AUTOSAR process the Description of the non-AUTOSAR system must be translated into an AUTOSAR format. Typically this will be achieved by a translation tool, although in principle it might also be done manually. | — |
| 执行者 | Non-AUTOSAR System Integrator | 1 |
| 消费 | Description of a Non-AUTO SAR System | 1 |
| 消费 | Integration Connector | 1 |
| 消费 | VFB System | 1 Initial VFB System: |
| 产出 | VFB System | 1 Integrated VFB System: |

#### 3.2.2. 工作产品

##### 3.2.2.1. VFB 系统



| Deliverable | VFB System |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products |  |  |
| Brief Description | Complete VFB view of a concrete system. |  |  |
| Description | Delivery of a VFB view of a concrete system. i.e. the top level composition and all nested compositions and components. This element is the basis for several extensions according to the scope of the VFB which can be an Overall System, a System Extract or an ECU Extract. This deliverable may contain variation points in its XML artifacts which need to be bound in later steps of the methodology. If such variation points are present, the delivered VFB system may optionally include PredefinedVariants in order to predefine variants for later selection and an Evaluated Variant Set. |  |  |
| Kind | Delivered |  |  |
| Extended By | ECU Extract of VFB System, Overall VFB System, VFB System Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Consistency Needs | 1 | Correlation between a group of RunnableEntitys and a group of DataPrototypes. |
| Aggregates | VFB Top Level System Composition | 1 |  |
| Deliverable | VFB System |  |  |
| Aggregates | Complex Driver Component | 0..* |  |
| Aggregates | ECU Abstraction Software Component | 0..* |  |
| Aggregates | Evaluated Variant Set | 0..* |  |
| Aggregates | Postbuild Variant Set | 0..* |  |
| Aggregates | Predefined Variant | 0..* |  |
| Aggregates | System Constant Value Set | 0..* |  |
| Aggregates | VFB Atomic Application Software Component | 0..* |  |
| Aggregates | VFB Data Type Mapping Set | 0..* |  |
| Aggregates | VFB Interfaces | 0..* |  |
| Aggregates | VFB Modes | 0..* |  |
| Aggregates | VFB Non AUTOSAR Component | 0..* |  |
| Aggregates | VFB NvBlock Software Component | 0..* |  |
| Aggregates | VFB Parameter Component | 0..* |  |
| Aggregates | VFB Sensor Actuator Component | 0..* |  |
| Aggregates | VFB Software Component Mapping Constraints | 0..* |  |
| Aggregates | VFB Types | 0..* |  |
| Produced by | Extend Composition | 1 | extended system: |
| Produced by | Translate Non-Autosar Description to Autosar Description | 1 | Integrated VFB System: |
| Consumed by | Define Partial Flat Map | 1 | Various parts of a given VFB system will be used as input: • Refer to parameters and variables in port interfaces and their data types. • In order to define unique names, also other the component definitions not in the scope of the partial flat map might be checked. • Set a link to the context of the Flat Map, e.g. a VFB |
| Consumed by | Define VFB Integration Connector | 1 |  |
| Consumed by | Define VFB Safety Information | 1 |  |
| Consumed by | Extend Composition | 1 | initial system: |
| Consumed by | Extract the ECU Communication | 1 | Need as input in order to set up the Data Mapping. |
| Consumed by | Generate or Adjust System Flat Map | 1 |  |
| Consumed by | Translate Non-Autosar Description to Autosar Description | 1 | Initial VFB System: |

##### 3.2.2.2. 整体 VFB 系统

| Deliverable | Overall VFB System |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products |  |  |
| Brief Description |  |  |  |
| Description | Deliverable containing an overall VFB description. It must contain the VFB Top Level System Composition of the complete system. |  |  |
| Kind | Delivered |  |  |
| Extends | VFB System |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregated by | Abstract System Description | 1 |  |
| Aggregated by | System Configuration Description | 1 |  |
| Aggregated by | System Constraint Description | 0..1 |  |
| Aggregates | System View Mapping | 0..1 | The Overall VFB System aggregates a potential mapping to the abstract or functional view of the system. |
| Aggregates | VFB Composition Component | 0..* | Further compositions below the top level composition. |
| Produced by | Develop a VFB System Description | 1 |  |
| Consumed by | Define Software Component Safety Information | 1 |  |
| Consumed by | Develop Application Software | 1 | The application software needs to refer to the relevant elements of the overall VFB system such as Software Component Types, Port Interfaces and Data Types. |
| Consumed by | Develop System | 0..1 | Usually the System refers to elements of an overall VFB descriptions. But for the description of a legacy system, this input might be empty. |
| Consumed by | Flatten Software Composition | 0..1 | Read relevant elements starting from VFB Top Level System Composition in case transformation starts with the full system. |
| Consumed by | Generate or Adjust ECU Flat Map | 0..1 | Used to set the upstream references in case one starts from a complete system. |

##### 3.2.2.3. VFB 系统提取

| Deliverable | VFB System Extract |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products |  |  |
| Brief Description | The VFB description for the partial system. |  |  |
| Description | The VFB description for a sub-system. It contains only those software components which belong to this sub-system. It should contain a VFB Top Level System Composition which has unconnected ports reflecting the connection points to the outer system. |  |  |
| Kind | Delivered |  |  |
| Extends | VFB System |  |  |
| Deliverable | VFB System Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregated by | System Extract | 1 |  |
| Aggregates | System View Mapping | 0..1 | The VFB System Extract aggregates a potential mapping to the abstract or functional view of the system. |
| Aggregates | VFB Composition Component | 0..* | Further compositions below the top level composition. |
| Consumed by | Flatten Software Composition | 0..1 | Read relevant elements starting from VFB Top Level System Composition in case transformation starts from the system extract. |
| Consumed by | Generate or Adjust ECU Flat Map | 0..1 | Used to set the upstream references in case one starts from a system extract. |

##### 3.2.2.4. VFB 顶层系统组合

表3.50：VFB 顶层系统组合（**VFB Top Level System Composition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Highest Level Composition consisting of all components that make up the Virtual Functional Bus. | — |
| 描述 | Highest Level Composition consisting of all components and their connectors that make up the VFB System Deliverable. This composition is not allowed to have ports if it represents the top level composition of an Overall VFB System, but it may have unconnected ports (and port groups) if it is at the top of a System Extract or ECU Extract. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | VFB System | 1 |
| 产出者 | Define VFB Top Level | 1 |
| 消费者 | Assign Top Level Composition | 1 |
| 消费者 | Define VFB Component Constraints | 1 |
| 消费者 | Define VFB Variants | 1 |
| 消费者 | Deploy Software Component | 1 |
| 使用的元模型元素 | CompositionSwComponent Type 1 | — |

##### 3.2.2.5. VFB 组合组件

表3.51：VFB 组合组件（**VFB Composition Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Describes a set of VFB CompositionTypes. | — |
| 描述 | Describes a set of CompositionComponentTypes, which may be nested. A VFB composition aggregates component types to encapsulate and abstract subsystem functionality. Compositions contain instances of components (other compositions and atomic components), as well as the connectors between them. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* In case the delivered atomic components make up one or more VFB Compositions, the composition description(s) shall be included in the delivery. |
| 聚合于 | Overall VFB System | 0..* Further compositions below the top level composition. |
| 聚合于 | VFB System Extract | 0..* Further compositions below the top level composition. |
| 产出者 | Define VFB Composition Component | 1 |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Set System Root | 1 Only the reference to the artifact is needed |
| 消费者 | Define VFB Component Constraints | 1..* |
| 消费者 | Define VFB Timing | 1..* |
| 消费者 | Define VFB Variants | 1..* |
| 消费者 | Define VFB Composition Component | 0..* |
| 消费者 | Define VFB Top Level | 0..* |
| 使用的元模型元素 | CompositionSwComponent Type 1 | — |
| 使用的元模型元素 | SwComponentType 1 | — |

##### 3.2.2.6. VFB AUTOSAR 标准包


| Deliverable | VFB AUTOSAR Standard Package |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products |  |  |
| Brief Description | Package with standardized AUTOSAR DataTypes, PortInterfaces, ComponentTypes (may include compositions), etc. on VFB level. |  |  |
| Description | Contains the standardized AUTOSAR blueprints needed on VFB level. This deliverable is released by AUTOSAR and is read only within the methodology. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | AUTOSAR Platform Types and Blueprints | 1 |  |
| Aggregates | AUTOSAR Specification of Application Interfaces | 1 |  |
| Aggregates | AUTOSAR Standard Types and Blueprints | 1 |  |
| Consumed by | Define ECU Abstraction Component | 1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Develop a VFB System Description | 1..* |  |
| Consumed by | Develop an Abstract System Description | 1..* |  |
| Consumed by | Define Atomic Software Component Internal Behavior | 0..1 | Use standardized elements (e.g. Data Types) as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| Consumed by | Define Complex Driver Component | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Define VFB Application Software Component | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Define VFB Composition Component | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Deliverable | VFB AUTOSAR Standard Package |  |  |
| Consumed by | Define VFB Interfaces | 0..1 | Use standardized Port Interfaces as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| Consumed by | Define VFB NvBlock Software Component | 0..1 |  |
| Consumed by | Define VFB Parameter Component | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Define VFB Sensor or Actuator Component | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Define VFB Timing | 0..1 |  |
| Consumed by | Define VFB Types | 0..1 | Use standardized elements (e.g. Data Types, Compu Methods) as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| Consumed by | Define Wrapper Components to Integrate Legacy Software | 0..1 | Use port blueprints in order to create ports with standardized application interfaces. |
| Consumed by | Generate Atomic Software Component Contract Header Files | 0..1 |  |
| Consumed by | Generate Component Header File in Vendor Mode | 0..1 |  |
| Consumed by | Generate Component Prebuild Data Set | 0..1 |  |

##### 3.2.2.7. AUTOSAR 应用接口规范

表3.52：AUTOSAR 应用接口规范（**AUTOSAR Specification of Application Interfaces**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Definitions of the AUTOSAR standard appliction interfaces. | — |
| 描述 | This includes standardized data types, port interfaces, units, port blueprints and example component types (including compositions) for the design of Application Software Components. Note that most of the content is not meant as direct input for defining a VFB system but as so-called blueprints: Blueprints need to be completed with company or project specific elements (e.g. a component type defined as blueprint may need additional ports or a data type defined as blueprint may need additional properties). | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | VFB AUTOSAR Standard Package | 1 |
| 使用的元模型元素 | AutosarDataType 1 | — |
| 使用的元模型元素 | CompuMethod 1 | — |
| 使用的元模型元素 | DataConstr 1 | — |
| 使用的元模型元素 | PortInterface 1 | — |
| 使用的元模型元素 | PortPrototypeBlueprint 1 | — |
| 使用的元模型元素 | SwComponentType 1 | — |

##### 3.2.2.8. VFB 原子软件组件

表3.53：VFB 原子软件组件（**VFB Atomic Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Description of an Atomic VFB Component. | — |
| 描述 | The description of an Atomic Software Component Type without Internal Behavior. Note that there are more specific artifacts extending this one. This artifact is used to describe general use cases which are valid for all kind of Atomic Software Components. | — |
| 种类 | AUTOSAR XML | — |
| 被扩展 | Complex Driver Component, ECU Abstraction Software Component, VFB Atomic Application Software Component, VFB Sensor Actuator Component | — |
| 聚合于 | Delivered Atomic Software Components | 1..* |
| 产出者 | Define SymbolProps for Types | 0..* symbolProps: The symbolProps attribute redefines the software component type name used in the code of the RTE. This resolves name clashes among different software component types designed accidentally with the same shortName. Note that this output is a splitable element, so it can be added later without changing the VFB model. |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define VFB Component Constraints | 2..* |
| 消费者 | Define Atomic Software Component Internal Behavior | 1 |
| 消费者 | Generate Atomic Software Component Contract Header Files | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Select Software Component Implementation | 1..* |
| 消费者 | Define Consistency Needs | 0..* The description of an AtomicSoftwareComponentType without InternalBehavior. |
| 消费者 | Define VFB Composition Component | 0..* |
| 消费者 | Define VFB Timing | 0..* |
| 消费者 | Define VFB Top Level | 0..* |
| 消费者 | Define VFB Variants | 0..* |
| 使用的元模型元素 | AtomicSwComponentType 1 | — |
| 使用的元模型元素 | SwComponentType 1 | — |

##### 3.2.2.9. VFB 原子应用软件组件

表3.54：VFB 原子应用软件组件（**VFB Atomic Application Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Description of an Atomic VFB Component. | — |
| 描述 | The description of an Application Software Component Type. It is used to represent the ECU-independent application software. | — |
| 种类 | AUTOSAR XML | — |
| 扩展 | VFB Atomic Software Component | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Application Software Component | 1 |
| 使用的元模型元素 | ApplicationSwComponent Type 1 | — |

##### 3.2.2.10. 复杂驱动程序组件

表3.55：复杂驱动程序组件（**Complex Driver Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | VFB Description of a Complex Driver Component. | — |
| 描述 | The Complex Driver Component is a special VFB Atomic Software Component that has direct access to hardware on an ECU and which is therefore linked to a specific ECU or specific hardware. It uses the meta-model element ComplexDeviceDriverSwComponentType which introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template. It provides (non-standardized) AUTOSAR Interfaces via ports on VFB level. | — |
| 种类 | AUTOSAR XML | — |
| 扩展 | VFB Atomic Software Component | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define Complex Driver Component | 1 |
| 消费者 | Map Software Component to BSW | 0..1 |
| 使用的元模型元素 | ComplexDeviceDriverSw ComponentType 1 | — |

##### 3.2.2.11. ECU 抽象软件组件

表3.56：ECU 抽象软件组件（**ECU Abstraction Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | VFB Description of an ECU Abstraction Software Component. | — |
| 描述 | The ECU Abstraction Software Component is a special Atomic Software Component that sits between a component that wants to access ECU periphery (typically a Sensor Actuator Component) and the Microcontroller Abstraction. It provides (non-standardized) AUTOSAR Interfaces via ports which represent the ECU periphery. The EcuAbstractionSwComponentType introduces the possibility to link from the software representation to its hardware description provided by the ECU Resource Template. During integration, an ECU Abstraction Software Component will be mapped to a BSW module which implements it and which will directly (without RTE) be connected to the Microcontroller Abstraction. | — |
| 种类 | AUTOSAR XML | — |
| 扩展 | VFB Atomic Software Component | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define ECU Abstraction Component | 1 |
| 消费者 | Map Software Component to BSW | 0..1 |
| 使用的元模型元素 | EcuAbstractionSw ComponentType 1 | — |

##### 3.2.2.12. VFB 参数组件

表3.57：VFB 参数组件（**VFB Parameter Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | A ParameterComponentType defines parameters and characteristic values accessible via provided Ports. | — |
| 描述 | A ParameterSwComponentType defines parameters and characteristic values accessible via Provide Ports. The provided values are the same for all connected Component Prototypes. This is as opposed to private parameters which are only available within the scope of an Atomic Software Component | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Parameter Component | 1 |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define VFB Composition Component | 0..* |
| 消费者 | Define VFB Timing | 0..* |
| 消费者 | Define VFB Top Level | 0..* |
| 消费者 | Define VFB Variants | 0..* |
| 使用的元模型元素 | ParameterSwComponent Type 1 | — |

##### 3.2.2.13. VFB 传感器执行器组件

表3.58：VFB 传感器执行器组件（**VFB Sensor Actuator Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Describes a sensor or actuator component that exist at the VFB Level and represents the physical interface of an actual sensor or actuator hardware element. | — |
| 描述 | A Sensor Actuator Software Component is an Atomic Software Component that makes the functionality of a sensor or actuator usable for other software components. That means that the Sensor Actuator Software Component provides to the application software components an interface for the physical values of the sensors and actuators. It is written for a concrete sensor or actuator and uses the ECU Abstraction interface. It references the description of the associated hardware elements. | — |
| 种类 | AUTOSAR XML | — |
| 扩展 | VFB Atomic Software Component | — |
| 聚合于 | Complete ECU Description | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Sensor or Actuator Component | 1 |
| 使用的元模型元素 | SensorActuatorSw ComponentType 1 | — |

##### 3.2.2.14. VFB NvBlock 软件组件

表3.59：VFB NvBlock 软件组件（**VFB NvBlock Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 |  | — |
| 描述 | The VFB NvBlock Software Component defines non volatile data which can be shared between Sw ComponentPrototypes. The non volatile data of the VFB NvBlock Software Component are accessible via provided and required ports. | — |
| 种类 |  | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB NvBlock Software Component | 1 |
| 使用的元模型元素 | NvBlockSwComponentType 1 | — |

##### 3.2.2.15. VFB 非 AUTOSAR 组件

表3.60：VFB 非 AUTOSAR 组件（**VFB Non AUTOSAR Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | A Component used to describe the non-autosar entities that exist at the VFB level. | — |
| 描述 | A Component used to describe the non-AUTOSAR entities that exist at the VFB level. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define Wrapper Components to Integrate Legacy Software | 1 |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define VFB Composition Component | 0..* |
| 消费者 | Define VFB Timing | 0..* |
| 消费者 | Define VFB Top Level | 0..* |
| 消费者 | Define VFB Variants | 0..* |
| 使用的元模型元素 | SwComponentType 1 | — |

##### 3.2.2.16. VFB 接口

表3.61：VFB 接口（**VFB Interfaces**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Interfaces and related elements that form part of the VFB, but are not standardized by AUTOSAR. | — |
| 描述 | Interfaces and related elements that form part of the VFB, but are not standardized by AUTOSAR. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Interfaces | 1..* |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define ECU Abstraction Component | 1 |
| 消费者 | Define Complex Driver Component | 1..* |
| 消费者 | Define VFB Application Software Component | 1..* |
| 消费者 | Define VFB Composition Component | 1..* |
| 消费者 | Define VFB NvBlock Software Component | 1..* |
| 消费者 | Define VFB Parameter Component | 1..* |

##### 3.2.2.17. VFB 类型

表3.62：VFB 类型（**VFB Types**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Data types and related elements that form part of the VFB, but are not standardized by AUTOSAR. | — |
| 描述 | Description of AutosarDataTypes and related elements (e.g. units, computation methods, etc.) that form part of the VFB, but are not standardized by AUTOSAR. This may also include copies of standardized elements which have been completed with project specific information (e.g. with calibration access information or computation methods). A VFB system can contain several different instances of this artifact, which may fulfill different roles. AutosarDataTypes can come as so-called ApplicationDatatypes or ImplementationDataTypes. This package can contain both kinds but they can also be split into separate artifacts. However, since it is also possible to generate ImplementationDataTypes from ApplicationDataTypes, a VFB system can be completely defined with ApplicationDatatypes only. Note that this work product is meant for use cases, in which a set of data types is maintained as a separate artifact. It is also possible to define particular AutosarDataTypes as part of another artifact, e.g. of VFB Interfaces if the types are closely related to certain port interfaces. In the methodology this artifact stands not only for data type definitions, but also for related elements like addressing methods, units, computation methods, constraints. etc. This is done for simplicity, because these elements are often consumed by the same tasks. Of course these can be treated as separate artifacts in real projects. | — |
| 种类 | AUTOSAR XML | — |
| 消费者 | Define VFB Sensor or Actuator Component | 1..* |
| 消费者 | Define VFB Timing | 1..* |
| 消费者 | Define VFB Top Level | 1..* |
| 消费者 | Define Consistency Needs | 0..* Interfaces which are relevant for the consistency definition. |
| 消费者 | Define VFB Variants | 0..* |
| 消费者 | Define Wrapper Components to Integrate Legacy Software | 0..* |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 0..* Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | AutosarDataType 1 | — |
| 使用的元模型元素 | ModeDeclarationGroup 1 | — |
| 使用的元模型元素 | PortInterface 1 | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Types | 1..* |
| 产出者 | Define SymbolProps for Types | 0..* symbolProps: The symbolProps attribute redefines the implementation data type name used in the code of the RTE and/or the component. This resolves name clashes among different implementation data types designed accidentally with the same shortName. Note that this output is a splitable element, so it can be added later without changing the VFB model. |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define ECU Abstraction Component | 1 |
| 消费者 | Define Complex Driver Component | 1..* |
| 消费者 | Define VFB Application Software Component | 1..* |
| 消费者 | Define VFB Composition Component | 1..* |
| 消费者 | Define VFB Interfaces | 1..* |
| 消费者 | Define VFB NvBlock Software Component | 1..* |
| 消费者 | Define VFB Parameter Component | 1..* |
| 消费者 | Define VFB Sensor or Actuator Component | 1..* |
| 消费者 | Define VFB Top Level | 1..* |
| 消费者 | Generate BSW Memory Mapping Header | 1..* SwAddrMethod: Referred SwAddrMethods Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate SWC Memory Mapping Header | 1..* SwAddrMethod: Referred SwAddrMethods Meth.bindingTime = SystemDesignTime |
| 消费者 | Configure Memmap Allocation | 0..* SwAddrMethods: SwAddrMethods used for the generic mapping. Note that one SwAddrmethod can represent several memory sections. |
| 消费者 | Define Consistency Needs | 0..* Data types which are relevant for the consistency definition. |
| 消费者 | Define VFB Constants | 0..* |
| 消费者 | Define Wrapper Components to Integrate Legacy Software | 0..* |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 0..* Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | ApplicationDataType 1 | — |
| 使用的元模型元素 | AutosarDataType 1 | — |
| 使用的元模型元素 | CompuMethod 1 | — |
| Use meta element | DataConstr | 1 |
| 使用的元模型元素 | ImplementationDataType 1 | — |
| Use meta element | PhysicalDimension | 1 |
| Use meta element | SwAddrMethod | 1 |
| 使用的元模型元素 | Unit 1 | — |

##### 3.2.2.18. VFB 数据类型映射集合

表3.63：VFB 数据类型映射集合（**VFB Data Type Mapping Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Mapping Set between Application and Implementation Data Types. | — |
| 描述 | Mapping Set between Application and Implementation Data Types. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Types | 0..* |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 0..1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Define VFB Constants | 0..* |
| 使用的元模型元素 | DataTypeMappingSet 1 | — |

##### 3.2.2.19. VFB 模式

表3.64：VFB 模式（**VFB Modes**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Modes declared here are non-AUTOSAR standard. They are modes that are managed by a software component acting as a application mode manager. | — |
| 描述 | Desclaration of mode groups and of the modes they contain. Modes declared here are non-AUTOSAR standard. They are modes that are managed by an application software component acting as a mode manager. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Modes | 1..* |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Define Complex Driver Component | 0..* |
| 消费者 | Define ECU Abstraction Component | 0..* |
| 消费者 | Define VFB Application Software Component | 0..* |
| 消费者 | Define VFB Composition Component | 0..* |
| 消费者 | Define VFB NvBlock Software Component | 0..* |
| 消费者 | Define VFB Top Level | 0..* |
| 消费者 | Define Wrapper Components to Integrate Legacy Software | 0..* |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 0..* Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | ModeDeclarationGroup 1 | — |

##### 3.2.2.20. VFB 常量

表3.65：VFB 常量（**VFB Constants**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Specification of constant data for usage as initial values by other artifacts. | — |
| 描述 | Specification of constant data for usage as initial values by other artifacts, e.g. initial values for calibration parameters or variable data elements provided in ports. By using the ConstantSpecification meta-class, such data can be standalone artifacts and thus maintained independently of the components or interfaces to which they apply. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Define VFB Constants | 1..* |
| 使用的元模型元素 | ConstantSpecification 1 | — |

##### 3.2.2.21. VFB 软件组件映射约束

表3.66：VFB 软件组件映射约束（**VFB Software Component Mapping Constraints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | A defined constraint on how certain components must be mapped (clustered or separated) to ECUs. | — |
| 描述 | These MappingConstraints define constraints describing which components need to be mapped to a single ECU, and which must be mapped to separate ECUs, without regard to any particular ECU or topology. The ComponentClustering constraint (also, clustering) is to be used for expressing that a certain set of SW components (atomic or not) shall be mapped (allocated) onto the same ECU. This is some kind of "execute together on same ECU" constraint. The semantic of the clustering constraint is straightforward if all concerned SW components are atomic. Otherwise, it shall be interpreted as follows: all of the atomic SW components making up the composition shall be mapped together onto the same ECU together with all other SW components (atomic or not) affected by the constraint. This also means that a clustering constraint can also refer to only a single composition. The ComponentSeparation constraint (also, separation) is to be used for expressing that two SW components (atomic or not) shall not be mapped (allocated) onto the same ECU. This is some kind of "do not execute together on same ECU" constraint. The semantic of the separation constraint is straightforward if one or both SW components are atomic. Otherwise, it shall be interpreted as follows: any of the atomic SW components making up the first composition, shall not be mapped onto the same ECU with any atomic SW component from the second composition. As a consequence, and to preserve consistency, an atomic SW component instance cannot be part of two compositions concerned by the same separation constraint, i.e. the two compositions have to be disjoint with regards to component instances. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | VFB System | 0..* |
| 产出者 | Define VFB Component Constraints | 1..* |
| 产出者 | Extend Composition | 0..* |
| 消费者 | Deploy Software Component | 0..1 |
| 使用的元模型元素 | MappingConstraint 1 | — |
| 使用的元模型元素 | SystemMapping 1 The splitable element SystemMapping is the root for this artifact. | — |

##### 3.2.2.22. VFB 时序

表3.67：VFB 时序（**VFB Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Atomic Software Component or Composition Component TimingDescription and TimingConstraints | — |
| 描述 | TimingDescription and TimingConstraints defined for an Atomic Software Component or a Composition Component | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Define VFB Timing | 1 |
| 消费者 | Define Software Component Timing | 0..1 |
| 消费者 | Define System Timing | 0..1 |
| 消费者 | Define VFB Variants | 0..1 |
| 使用的元模型元素 | VfbTiming 1 | — |

##### 3.2.2.23. 非 AUTOSAR 系统的描述

表3.68：非 AUTOSAR 系统的描述（**Description of a Non-AUTOSAR System**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | View of the non-AUTOSAR system that contains the relevant information for its integration with the AUTOSAR system at VFB level | — |
| 描述 | This artifact describes the elements of the non-AUTOSAR system that are relevant for its integration with an AUTOSAR system at the VFB level. The format of the description depends on the methodology or platform that is employed for the development of the non-AUTOSAR system. It may not be assumed that the description of the non-AUTOSAR system comes in an AUTOSAR format. Also the contents of the description may differ both in its scope and in its details from an AUTOSAR description that also addresses the VFB level, i.e. a SwComponent Description. The interfaces of infotainment system components developed on the basis of the GENIVI platform for instance are specified with the Franca Interface Definition Language. A Franca IDL description contains interfaces that define data types, methods, attributes, and broadcasts. It does neither define the components that implement these interfaces nor their connections. In addition, the granularity of the data type description is much coarser than a data type description with the Sw Component Template. | — |
| 种类 | Custom | — |
| 消费者 | Define VFB Integration Connector | 1 |
| 消费者 | Translate Non-Autosar Description to Autosar Description | 1 |

##### 3.2.2.24. 集成连接器

表3.69：集成连接器（**Integration Connector**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::VFB::Work Products | — |
| 简要描述 | Specification of the connections of the elements of the non-AUTOSAR system with the elements of the AUTOSAR system | — |
| 描述 | This artifact specifies which elements of the non-AUTOSAR system are to be connected with which elements of the AUTOSAR system. If for instance the Description of the non-AUTOSAR system contains elements corresponding to port instances, the integration connector would define how these ports are connected with the port instances contained in the AUTOSAR SwComponent Description. In addition, the Integration Connector may specify information that is necessary for the integration but not yet contained in the Description of the non-AUTOSAR system. If for instance the Description of the non-AUTOSAR system contains only very coarse grained data type descriptions the Integration Connector will be used to add sufficient information such that the compatibility of the data types with the ones defined in the AUTOSAR SwComponent Description can be checked. | — |
| 种类 | Custom | — |
| 产出者 | Define VFB Integration Connector | 1 |
| 消费者 | Translate Non-Autosar Description to Autosar Description | 1 |

### 3.3. 系统

本章包含用于开发系统和子系统 的工作产品和任务 的定义。相关元模型元素的定义参见 [\[8, CP TPS System Template\]](#ref-8) 和 [\[19, CP TPS ECU Resource Template\]](#ref-19)。

#### 3.3.1. 任务

##### 3.3.1.1. 设置系统根

表3.70：设置系统根（**Set System Root**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 |  | — |
| 描述 | Set up the root element of a system description. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Communication Layers | 1 Only the reference to the artifact is needed |
| 消费 | Mapping of Software Components to ECUs | 1 Only the reference to the artifact is needed |
| 消费 | Signal Path Constraints | 1 Only the reference to the artifact is needed |
| 消费 | Topology | 1 Only the reference to the artifact is needed |
| 消费 | VFB Composition Component | 1 Only the reference to the artifact is needed |
| 消费 | Data Mapping | 1..* Only the reference to the artifact is needed |
| 产出 | System Description Root Element | 1 Set up the root element, and the links to other artifacts |

##### 3.3.1.2. 指派顶层组合

表3.71：指派顶层组合（**Assign Top Level Composition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 |  | — |
| 描述 | Assign a VFB Top Level Composition to the System Root | — |
| 执行者 | System Engineer | 1 |
| 消费 | VFB Top Level System Composition | 1 |
| 产出 | System Description Root Element | 1 |

##### 3.3.1.3. 定义 ECU 描述

表3.72：定义 ECU 描述（**Define ECU Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Define a particular ECU's resources. | — |
| 描述 | Define a particular ECU's resources by describing Hardware Elements, pins, connections.The HW Elements are the main describing elements of an ECU,e.g processing units, memory, peripherals, sensors and actuators. HW Elements have a unique name and can be identified within the ECU description. HW Elements do not necessarily have to be described on the level of an ECU. It is possible to describe HW Elements as parts of other HW Elements. By this means, a hierarchical description of HW Elements can be created. HW Elements provide HW PinGroups and HW Pins for being interconnected among each others. HW PinGroups allow a rough description of how certain groups of HWPins are arranged. The detailed description can be done using the HW Pins.HW Connections are used to describe connection on several levels:connections between HW Elements, connections between HW PinGroups, connections between HW Pins. | — |
| 执行者 | System Engineer | 1 |
| 产出 | ECU Resources Description | 1..* Decription of the ECU |

##### 3.3.1.4. 定义系统拓扑

表3.73：定义系统拓扑（**Define System Topology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Select the ECUs and how the they are interconnected by networks. | — |
| 描述 | Define how the ECUs of a system are interconnected by networks. | — |
| 执行者 | System Engineer | 1 |
| 消费 | ECU Resources Description | 1..* |
| 产出 | Topology | 1 |

##### 3.3.1.5. 部署软件组件


表3.74：部署软件组件（**Deploy Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Deploy VFB Software Components to an ECU | — |
| 描述 | Deploy each VFB Software Component to an ECU that will execute the component. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Topology | 1 |
| 消费 | VFB Top Level System Composition | 1 |
| 消费 | System Timing | 0..1 |
| 消费 | VFB Software Component Mapping Constraints | 0..1 |
| 产出 | Mapping of Software Components to ECUs | 1 |

##### 3.3.1.6. 生成或调整系统 Flat Map


表3.75：生成或调整系统 Flat Map（**Generate or Adjust System Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Generates and/or adjust the unique names of component prototypes and MCD display data in the scope of system. | — |
| 描述 | Generates and/or adjust the unique names of component prototypes and MCD display data in the scope of a System or System Extract. | — |
| 执行者 | System Engineer | 1 |
| 消费 | System Description Root Element | 1 |
| 消费 | VFB System | 1 |
| 消费 | Partial Flat Map | 0..* If Partial Flat Maps were delivered along with software components, they must be integrated into the System Flat Map: • The instance refs used in a partial flat map must be taken over and adjusted to the context of the System or System Extract. • Name conflicts have to be resolved if several partial flat maps are merged. |
| 输入/输出 | System Flat Map | 1 |

##### 3.3.1.7. 派生通信需求

表3.76：派生通信需求（**Derive Communication Needs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Define the signals used to exchange data & operations needed by software components over a network. | — |
| 描述 | Define the signals used to exchange data & operations needed by software components over a network. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 产出 | Data Mapping | 1..* |
| 产出 | System Signal | 1..* |
| 产出 | System Signal Group | 0..* |

##### 3.3.1.8. 定义信号路径约束

表3.77：定义信号路径约束（**Define Signal Path Constraints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Additional guidelines for the System Generator, which specific way a signal between two Software Components should take in the network without defining in which frame and with which timing it is transmitted. | — |
| 描述 | Define additional guidelines for the System Generator, which specific way a signal between two Software Components should take in the network without defining in which frame and with which timing it is transmitted. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | Topology | 1 |
| 产出 | Signal Path Constraints | 1 |

##### 3.3.1.9. 定义系统变体


表3.78：定义系统变体（**Define System Variants**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Define variants for the artifacts of a System Description. | — |
| 描述 | Define variants for the artifacts of a System Description. Definition of a variant means in general to define its conditions and its latest binding time. Therefore one has to create a PredefinedVariant referring to the settings which are used by the system elements in scope. To do so, this task can make use of existing System Constant Value Set s and/or Postbuid Variant Set s or define new ones. Several PredefinedVariant s can be combined to one Evaluated Variant Set . This task can also be applied when designing a subsystem, therefore the System Extract is an optional input. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | Mapping of Software Components to Implementations | 1 |
| 消费 | System Description Root Element | 1 |
| 消费 | System Signal | 1 |
| 消费 | System Signal Group | 1 |
| 消费 | System Timing | 1 |
| 消费 |  | 1 Topology |
| 消费 | Complete ECU Description | 1..* |
| 消费 | System Description | 0..* |
| 输入/输出 | Postbuild Variant Set | 1 |
| 输入/输出 | System Constant Value Set | 1 |
| 产出 | Evaluated Variant Set | 1 |
| 产出 | Predefined Variant | 1 |

##### 3.3.1.10. 定义系统时序

表3.79：定义系统时序（**Define System Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Define SystemTiming for a concrete system taking the mapping of software components to ECUs and their implementation into account | — |
| 描述 | Define SystemTiming (TimingDescription and TimingConstraints) for a concrete system taking the mapping of software components to ECUs and their implementation into account. This means that the resulting Communication Matrix (and its implication to the communication stack) can also be referenced by the timing specification to refine remote communication timing behavior. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Communication Layers | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | Topology | 1 |
| 消费 | Mapping of Software Components to Implementations | 0..1 |
| 消费 | Software Component Timing | 0..1 |
| 消费 | VFB Timing | 0..1 |
| 产出 | System Timing | 1 |

##### 3.3.1.11. 扩展拓扑


表3.80：扩展拓扑（**Extend Topology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Extend the existing System Topology | — |
| 描述 | Extend the existing System Topology by describing how new ECUs will be connected to the existing one through the current network | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | ECU Resources Description | 0..1 |
| 输入/输出 | Topology | 1 |

##### 3.3.1.12. 选择软件组件实现

表3.81：选择软件组件实现（**Select Software Component Implementation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Select implementation for an Atomic Software Component. | — |
| 描述 | The system engineer selects an Atomic Software Component Implementation for each defined VFB Atomic Software Component. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Atomic Software Component Implementation | 1..* |
| 消费 | Software Component Internal Behavior | 1..* |
| 消费 | VFB Atomic Software Component | 1..* |
| 产出 | Mapping of Software Components to Implementations | 1 |

##### 3.3.1.13. 选择设计期变体

表3.82：选择设计期变体（**Select Design Time Variant**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Select a system variant at system design time. | — |
| 描述 | Select a system variant at system design time. This could be done in different ways: • Replace a model, which contains the variation points contributing to this particular variant and all the possible settings/elements, by a model, which does no more contain these variation points and which contains only the particular settings/elements selected for this variant. • In order to document the selection for further process steps, it is also possible to keep the information about the selected variant and the variation points in the model by introducing a PredefinedVariant along with appropriate fixed settings of system constant values. In constrast to variant selection in later process steps, no code generation or compilation is involved at system design time, thus this task is just a transformation of one XML model into another one. This task can be applied to a complete system description, represented by a System Extract. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | System Engineer | 1 |
| 消费 | Complete ECU Description | 1 |
| 输入/输出 | System Description | 1 |

##### 3.3.1.14. 定义系统视图映射

任务 定义系统视图映射（见图 3.59）在两个系统描述之间创建系统视图映射。可以区分不同的情况：

- 不同整体 VFB 系统的映射——抽象系统描述与系统配置描述。

- 不同结构的系统提取的映射，例如主组织交付的系统提取与次组织的不同结构（ECU 系统描述）（见 2.5.4、2.5.5）。

表3.83：定义系统视图映射（**Define System View Mapping**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 | Map elements from different views on the system. | — |
| 描述 | This task creates the System View Mapping between two System Descriptions (Mapping of different structured system descriptions, e.g. system extract delivered by a primary organization and the different structure of the secondary organisation). | — |
| 执行者 | System Engineer | 1 |
| 消费 | System Description | 2 |
| 产出 | System View Mapping | 1 |

##### 3.3.1.15. 创建转换器规范

表3.84：创建转换器规范（**Create Transformer Specification**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 |  | — |
| 描述 | In this task the specification of a transformer module is created. Since the specification is created as a part of the communication design, the System Engineer has to perform this task. Optionally a Basic Software Designer can support the creation of the specification. | — |
| 执行者 | System Engineer | 1 |
| 执行者 | Basic Software Designer | 0..1 |
| 产出 | Custom Transformer Specification | 1 |

##### 3.3.1.16. 定义快速原型场景


表3.85：定义快速原型场景（**Define Rapid Prototyping Scenario**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Tasks | — |
| 简要描述 |  | — |
| 描述 | Defines the rapid prototyping scenario. | — |
| 执行者 | Rapid Prototyping Engineer | 1 |
| 消费 | System Description Root Element | 1 |
| 消费 | Software Component Internal Behavior | 1..* |
| 产出 | Rapid Prototyping Scenario | 1 |

#### 3.3.2. 工作产品

##### 3.3.2.1. 系统描述


| Deliverable | System Description |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description | Partial Extract of a System |  |  |
| Description | Generic deliverable for defining In each role, this deliverable may contain variation points in its ARXML artifacts which need to be bound in later steps, e.g. when defining a subsystem from a complete system or later for the single ECUs. If such variation points are present, the System Description may optionally include PredefinedVariants in order to predefine variants for later selection and an Evaluated Variant Set. Please note that this generic deliverable does not correspond to the system description with the system category "SYSTEM_DESCRIPTION" (see [TPS_SYST_01003]). The system description with the category "SYSTEM_DESCRIPTION" is represented by the deliverable "System Configuration Description". This deliverable is equivalent to a description of a system with any category. In the System Template Specification "system description" is the most frequently used term for this kind of artifact. Delivered Abstract System Description, System Configuration Description, System Constraint Description, | a System. | It is used in different roles within the methodology. |
| Kind |  |  |  |
| Extended By | System Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | System Description Root Element | 1 |  |
| Aggregates | Communication Layers | 0..1 |  |
| Aggregates | Mapping of Software Components to ECUs | 0..1 |  |
| Aggregates | Mapping of Software Components to Implementations | 0..1 |  |
| Aggregates | Rapid Prototyping Scenario | 0..1 |  |
| Aggregates | Topology | 0..1 |  |
| Aggregates | Alias Name Set | 0..* |  |
| Aggregates | Communication Matrix | 0..* |  |
| Aggregates | Data Mapping | 0..* |  |
| Aggregates | Evaluated Variant Set | 0..* |  |
| Aggregates | Postbuild Variant Set | 0..* |  |
| Aggregates | Predefined Variant | 0..* |  |
| Aggregates | System Constant Value Set | 0..* |  |
| Aggregates | System Signal | 0..* |  |
| Aggregates | System Signal Group | 0..* |  |
| Aggregates | System Timing | 0..* |  |
| In/out | Select Design Time Variant | 1 |  |
| Consumed by | Define System View Mapping | 2 |  |
| Consumed by | Define System Safety Information | 1 |  |
| Consumed by | Define Alias Names | 0..1 | Needed for definition of alias names with system, system extract or ECU scope, depending of the role of the System Description. |
| Consumed by | Define System Variants | 0..* |  |
| Deliverable | System Constraint Description |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description |  |  |  |
| Description | Contains the artifacts that describe System Constraints. It serves as an input for setting up the complete Abstract System Description and/or System Configuration Description. This deliverable corresponds to the system description with the system category "SYSTEM_ CONSTRAINTS" (see [TPS_SYST_01003]). |  |  |
| Kind | Delivered |  |  |
| Extends | System Description |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Overall VFB System | 0..1 |  |
| Aggregates | System Flat Map | 0..1 |  |
| Consumed by | Develop System | 0..1 |  |
| Consumed by | Develop an Abstract System Description | 0..1 | In the context of the "Develop an Abstract System Description" activity, the constraints for the abstract or functional view on the system can be provided by the "System Constraint Description". |
| Deliverable | System Configuration Description |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description |  |  |  |
| Description | Contains the artifacts that describe a complete AUTOSAR System. It is the basis for extracting descriptions for sub-systems or ECUs. Note that System Extracts may be refined by details which are not present in the System Configuration. This deliverable corresponds to the system description with the system category "SYSTEM_ DESCRIPTION" (see [TPS_SYST_01003]). |  |  |
| Kind | Delivered |  |  |
| Extends | System Description |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Overall VFB System | 1 |  |
| Aggregates | System Flat Map | 0..1 |  |
| Produced by | Develop System | 1..* |  |
| Consumed by | Generate System Extract | 1 |  |
| Consumed by | Generate ECU Extract | 0..1 |  |
| Deliverable | System Extract |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description |  |  |  |
| Description | Contains the artifacts that describe a subsystem specific view on the complete System Description. Initially, the System Extract is not fully decomposed and still contains compositions. It is the basis for designing subsystems, e.g. by adding further ECUs within the given constraints. This deliverable corresponds to the system description with the system category "SYSTEM_ EXTRACT" (see [TPS_SYST_01003]). |  |  |
| Kind | Delivered |  |  |
| Extended By | ECU System Description |  |  |
| Deliverable | System Extract |  |  |
| Extends | System Description |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | VFB System Extract | 1 |  |
| Aggregates | System Flat Map | 0..1 |  |
| Produced by | Develop System | 0..* |  |
| Produced by | Generate System Extract | 0..* |  |
| Consumed by | Create ECU System Description | 1 |  |
| Consumed by | Develop Sub-System | 1 |  |
| Consumed by | Generate ECU Extract | 0..1 |  |
| Deliverable | ECU System Description |  |  |
| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description |  |  |  |
| Description | This System Description is used to describe the closed view on one EcuInstance (note that an ECUInstance represents a single instantiation of a Classic Platform stack that may run directly on the physical ECU, or under a hypervisor). It can be derived from a System Extract or it can be designed independently and mapped to a System Extract. The ECU System Description is not fully decomposed and still may contain compositions. It is refined during the activity Design Sub-System. This deliverable corresponds to the system description with the system category "ECU_SYSTEM_ DESCRIPTION" (see [TPS_SYST_01003]). |  |  |
| Kind |  |  |  |
| Extends | System Extract |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Design Sub-System | 1 | System Extract refined during design of the corresponding sub-system with elements needed to generate ECU Extract(s). |
| Produced by | Create ECU System Description | 1..* |  |
| Consumed by | Design Sub-System | 1 | System Extract as generated from the outer system. |
| Consumed by | Configure Mode Management | 0..1 | Input in case ECU Extract is not available (atomic software components not available) |
| Consumed by | Generate ECU Extract | 0..1 |  |

##### 3.3.2.2. 抽象系统描述

| Deliverable | Abstract System Description |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description | Provides an abstract or functional view on the system |  |  |
| Description | The Abstract System Description extends the general System Description and provides an abstract or functional view on the system to be developed. This deliverable corresponds to the system description with the system category "ABSTRACT_ SYSTEM_DESCRIPTION" (see [TPS_SYST_01003]). |  |  |
| Kind | Delivered |  |  |
| Extends | System Description |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Overall VFB System | 1 |  |
| Produced by | Develop an Abstract System Description | 1..* |  |
| Consumed by | Develop System | 0..* | The abstract System Description is an optional input for the activity "Develop System". Please note, that in this step the Abstract System Description is refined to a System Description. |
| Consumed by | Develop a VFB System Description | 0..* | The abstract System Description is an optional input for the activity "Develop a VFB System Description". The VFB-related part of the Abstract System Description can be than refined to the concrete "Overall VFB System". Additionally, a mapping between those two views can be established. |

##### 3.3.2.3. 完整 ECU 描述

| Deliverable | Complete ECU Description |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description | An ECU Description includes the resources it has available along with its corresponding ECU-specific software components. |  |  |
| Description | An ECU Description includes the resources it has available along with its corresponding ECU-specific software components. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | ECU Resources Description | 1 |  |
| Aggregates | VFB Sensor Actuator Component | 0..* |  |
| Consumed by | Select Design Time Variant | 1 |  |
| Consumed by | Define System Variants | 1..* |  |

##### 3.3.2.4. 系统描述根元素

表3.86：系统描述根元素（**System Description Root Element**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | A System Description root element. | — |
| 描述 | The System description defines the following major elements: • Topology : description of the Topology of the System. • Software : description of the root software composition containing all software components in the System in a hierarchical structure. • Communication : description of all Communication elements used in the System. • Mapping and Mapping Constraints : description of all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints). The root element can be the basis for a System extract as well as for the whole System depending on which elements are aggregated. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 1 |
| 产出者 | Assign Top Level Composition | 1 |
| 产出者 | Set System Root | 1 Set up the root element, and the links to other artifacts |
| 消费者 | Define Rapid Prototyping Scenario | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Flatten Software Composition | 1 find the top level composition |
| 消费者 | Generate or Adjust System Flat Map | 1 |
| 使用的元模型元素 | System 1 | — |

##### 3.3.2.5. 系统映射概览

有各种工件对应于元模型元素 SystemMapping 下收集的映射。图 3.64 给出概览。细节将在以下子章中说明。

##### 3.3.2.6. 数据映射

表3.87：数据映射（**Data Mapping**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 |  | — |
| 描述 | Mapping of data prototypes from the VFB description to System signals. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..* |
| 产出者 | Derive Communication Needs | 1..* |
| 消费者 | Define Signal PDUs | 1 |
| 消费者 | Flatten Software Composition | 1..* |
| 消费者 | Set System Root | 1..* Only the reference to the artifact is needed |
| 使用的元模型元素 | DataMapping 1 | — |
| 使用的元模型元素 | SystemMapping 1 The splitable element SystemMapping is the root for this artifact. | — |

##### 3.3.2.7. 软件组件到 ECU 的映射

表3.88：软件组件到 ECU 的映射（**Mapping of Software Components to ECUs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Describes the mapping of Software Components to the ECUs that are defined in the VFB context. | — |
| 描述 | The VFB shows all software components independently of their deployment on individual ECUs. This work product defines for each software component the corresponding ECU on which the software component will be deployed and executed. This artifact may contain a mapping of software components to application partitions by a SwcTo ApplicationPartitionMapping. With an ApplicationPartitionToEcuPartitionMapping the application partitions are assigned to ECU partitions. This can substitute the direct mapping of software components to ECUs via SwcToEcuMapping.ecuInstance. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..1 |
| 产出者 | Deploy Software Component | 1 |
| 消费者 | Define Signal PDUs | 1 |
| 消费者 | Define Signal Path Constraints | 1 |
| 消费者 | Define System Timing | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Derive Communication Needs | 1 |
| 消费者 | Extract the ECU Communication | 1 |
| 消费者 | Flatten Software Composition | 1 |
| 消费者 | Set System Root | 1 Only the reference to the artifact is needed |
| 使用的元模型元素 | ApplicationPartitionToEcu PartitionMapping 1 | — |
| 使用的元模型元素 | SwcToApplicationPartition Mapping 1 | — |
| 使用的元模型元素 | SwcToEcuMapping 1 | — |
| 使用的元模型元素 | SystemMapping 1 The splitable element SystemMapping is the root for this artifact. | — |

##### 3.3.2.8. 软件组件到实现的映射

表3.89：软件组件到实现的映射（**Mapping of Software Components to Implementations**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 |  | — |
| 描述 | Specifies the selection of software implementations for the atomic component prototypes. Because component prototypes can be located on different ECUs, it is possible to have different Implementations of two prototypes of the same AtomicComponentType in the system. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..1 |
| 产出者 | Select Software Component Implementation | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Define System Timing | 0..1 |
| 使用的元模型元素 | SwcToImplMapping 1 | — |
| 使用的元模型元素 | SystemMapping 1 The splitable element SystemMapping is the root for this artifact.. | — |

##### 3.3.2.9. 信号路径约束

表3.90：信号路径约束（**Signal Path Constraints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Constraints on the Path that should be used or not by Signals | — |
| 描述 | One of the tasks of the System Generator is actually to calculate automatically the communication (signals) between the RTEs and define the needed frames for that communication. These definitions of the frames include implicitly the definition of the paths the AUTOSAR-Signals are transmitted through the system. Thereby the System Generator often has the choice between alternative ways through the system. There exist four different constraints for signals regarding the signal path: • The CommonSignalPath describes that two signals must take the same way (Signal Path) in the topology. • 'The ForbiddenSignalPath describes the way (Signal Path) that a signal must not take in the topology, e.g. in case of safety critical transmission. • The PermissibleSignalPath describes the way (Signal Path) a signal can take in the topology. If more than one PermissibleSignalPath is defined for the same signal/operation attributes, any of them can be chosen. • The SeparateSignalPath describes that two or more signals must not take the same way (Signal Path) in the topology e.g. in case of redundant transmission. It is also possible that the same | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Define Signal Path Constraints | 1 |
| 消费者 | Set System Root | 1 Only the reference to the artifact is needed |
| 使用的元模型元素 | SignalPathConstraint 1 | — |
| 使用的元模型元素 | SystemMapping 1 The splitable element SystemMapping is the root for this artifact. | — |

##### 3.3.2.10. 拓扑

表3.91：拓扑（**Topology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | The system topology, which may be reused in different systems. | — |
| 描述 | Describes the topology of the system : A topology is formed by a number of EcuInstances that are interconnected to each other in order to form ensembles of ECUs and CommunicationClusters. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..1 |
| 产出者 | Define System Topology | 1 |
| 输入/输出 | Extend Topology | 1 |
| 消费者 | Define Communication Matrix | 1 |
| 消费者 | Define Network Management | 1 |
| 消费者 | Define Signal PDUs | 1 |
| 消费者 | Define Signal Path Constraints | 1 |
| 消费者 | Define System Timing | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Define TP | 1 |
| 消费者 | Deploy Software Component | 1 |
| 消费者 | Extract ECU Topology | 1 |
| 消费者 | Set System Root | 1 Only the reference to the artifact is needed |
| 消费者 | Define Secured PDUs | 0..1 |
| 使用的元模型元素 | CommunicationCluster 1 | — |
| 使用的元模型元素 | EcuInstance 1 | — |

##### 3.3.2.11. ECU 资源描述

表3.92：ECU Resources Description（**ECU Resources Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Definition of the resources available on an ECU. | — |
| 描述 | Definition of the resources available on an ECU. It mainly contains a description of hardware elements (like physical memory sections or peripherals, pins, hardware connections) which need to be referred by a software component or a basic software description. The focus is to describe an already engineered piece of hardware, its content and structure. It is not in the focus of the ECU Resource Description to support the design of electronics hardware itself. In the XML it is represented as a set of HwDescriptionEntity -s | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Complete ECU Description | 1 |
| 产出者 | Define ECU Description | 1..* Decription of the ECU |
| 消费者 | Define System Topology | 1..* |
| 消费者 | Define BSW Interfaces | 0..1 |
| 消费者 | Define ECU Abstraction Component | 0..1 |
| 消费者 | Extend Topology | 0..1 |
| 消费者 | Generate ECU Executable | 0..1 may be used to set up build environment Meth.bindingTime = CompileTime |
| 消费者 | Implement a BSW Module | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Measure Component Resources | 0..1 |
| 消费者 | Measure Resources | 0..1 |
| 消费者 | Define Complex Driver Component | 0..* |
| 消费者 | Define VFB Sensor or Actuator Component | 0..* |
| 使用的元模型元素 | HwElement 1 | — |

##### 3.3.2.12. 系统信号

表3.93：系统信号（**System Signal**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 |  | — |
| 描述 | The system signals allow to represent this communication view in a flattened structure, with (at least) one system signal defined for each data element sent or received by a SW component instance. If data has to be sent over gateways, there is still only one system signal representing this data. The representation of the data on the individual communication systems is done by the cluster signals. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..* |
| 产出者 | Derive Communication Needs | 1..* |
| 消费者 | Define Signal PDUs | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Define RTE Fan-out | 1..* |
| 消费者 | Extract the ECU Communication | 0..* |
| 使用的元模型元素 | SystemSignal 1 | — |

##### 3.3.2.13. 系统信号组

表3.94：系统信号组（**System Signal Group**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | A signal group refers to a set of signals that must always be kept together. A signal group is used to guarantee the atomic transfer of AUTOSAR composite data types. | — |
| 描述 | The System Signal Group is representing a set of Signals that must be kept together. A signal group is to guarantee the transfer of AUTOSAR composite data types for sender receiver communication.The RTE is required to treat AUTOSAR signals transmitted using sender-receiver communication atomically. To achieve this, the "signal group" mechanisms shall be utilized.It is not possible to map a Variable Data Prototype with a composite datatype directly to a System Signal . The complex data type must be decomposed into single signals. As this set of single signals has to be treated as atomic, it is placed in a "signal group". It is also used in client server communication when the RTE maps a response to a corresponding operation request. The arguments, application errors, client identifier and sequence counter of an operation are mapped to System Signal of two dedicated SystemSignalGroup elements;one for the request and one for the response. The RTE Client Server Protocol is used to provide a specific semantics to each of these SystemSignalGroups and System Signal , also those which are introduced only to support the protocol. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..* |
| 产出者 | Derive Communication Needs | 0..* |
| 消费者 | Define System Variants | 1 |
| 消费者 | Extract the ECU Communication | 0..* |
| 使用的元模型元素 | SystemSignalGroup 1 | — |

##### 3.3.2.14. 系统 Flat Map

表3.95：系统 Flat Map（**System Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Mapping of instance names to nested model elements. Use cases: Resolve name conflicts when flattening VFB software compositions; provide unique names and unique model references for measurement and calibration data. | — |
| 描述 | The flat map is a list of elements, each element represents exactly one node (e.g. a component instance or data element) of the instance tree of a software system. The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name to it. The name will be unique in the scope to which this Flat Map belongs (which could be a whole System or a System Extract). Use case: The System Flat Map is defined in the context of a System or System Extract. It serves as a basis for generating an ECU Flat Map (or a Flat Map of a "child" System Extract). In the ECU Flat Map, the names will be used as display names for MCD tools or as names for component prototypes in a flattened software composition. For further information refer to the description of artifact ECU Flat Map. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Configuration Description | 0..1 |
| 聚合于 | System Constraint Description | 0..1 |
| 聚合于 | System Extract | 0..1 |

##### 3.3.2.15. 系统时序

表3.96：系统时序（**System Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Concrete system's TimingDescription and TimingConstraints | — |
| 描述 | TimingDescription and TimingConstraints defined for a concrete system taking the mapping of software components to ECUs and their implementation into account. This means that the resulting Communication Matrix (and its implication to the communication stack) can also be referenced by the timing specification to refine remote communication timing behavior. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..* |
| 产出者 | Define System Timing | 1 |
| 消费者 | Define System Variants | 1 |
| 消费者 | Extract ECU System Timing | 1 |
| 消费者 | Deploy Software Component | 0..1 |
| 使用的元模型元素 | SystemTiming 1 | — |

##### 3.3.2.16. 系统视图映射

表3.97：系统视图映射（**System View Mapping**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work | — |
| 简要描述 | The System View Mapping provide an mapping between different views on the system. | — |
| 描述 | This artifact contains a set of system view mappings and provides an mapping between different views on the system, e.g. different overall VFB systems (e.g. abstract system description with system configuration description), or the overall VFB system with the VFB System Extract description. | — |
| 种类 | AUTOSAR XML | — |
| 输入/输出 | Generate or Adjust System Flat Map | 1 |
| 消费者 | Add Documentation to the Software Component | 0..1 Optional input in order to refer to unique names defined in system context. |
| 消费者 | Generate or Adjust ECU Flat Map | 0..1 Take over definitions of unique names from system level to ECU level. |
| 使用的元模型元素 | FlatMap 1 | — |
| 聚合于 | Overall VFB System | 0..1 The Overall VFB System aggregates a potential mapping to the abstract or functional view of the system. |
| 聚合于 | VFB System Extract | 0..1 The VFB System Extract aggregates a potential mapping to the abstract or functional view of the system. |
| 产出者 | Define System View Mapping | 1 |
| 使用的元模型元素 | ViewMapSet 1 | — |

##### 3.3.2.17. 转换器设计包

| Deliverable | Transformer Design Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products |  |  |
| Brief Description |  |  |  |
| Description | This deliverable contains a specification of the transformer technology to be implemented by the BSWM developer. Furthermore it contains the Vendor specific parameter definition for the corresponding transformer. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Custom Transformer Specification | 1 |  |
| Aggregates | BSW Module Vendor- Specific Configuration Parameter Definition | 0..1 |  |
| Produced by | Design Custom Transformer | 1 |  |
| Produced by | Develop System | 0..* |  |
| Consumed by | Develop Basic Software | 0..* |  |

##### 3.3.2.18. 定制转换器规范

表3.98：定制转换器规范（**Custom Transformer Specification**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 |  | — |
| 描述 | This artifact represents the functional specification of the Transformer to be implemented. The AUTOSAR methodology does not prescribe the format of this artifact. | — |
| 种类 | Custom | — |
| 聚合于 | Transformer Design Bundle | 1 |
| 产出者 | Create Transformer Specification | 1 |

##### 3.3.2.19. 快速原型场景

表3.99：快速原型场景（**Rapid Prototyping Scenario**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Description of the (required) bypass points and the hooks in the system. | — |
| 描述 | Description of the (required) bypass points and the in the system and the corresponding hooks. This artifact contains the RptContainers with bypass points referencing things like parameterAccess (dataWriteAccess, dataReadAccess, dataSendPoint, dataReceivePointByValue, dataReceivePoint ByArgument, writtenLocalVariable, readLocalVariable, etc.) The hooks describe the link between the bypass points and the rapid prototyping algorithm. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..1 |
| 产出者 | Define Rapid Prototyping Scenario | 1 |
| 消费者 | Extract ECU Rapid Prototyping Scenario | 1 |
| 使用的元模型元素 | RapidPrototypingScenario 1 | — |

#### 3.3.3. 通信矩阵和通信层

本节包含作为系统描述一部分、用于建立通信矩阵和通信层的任务和工作产品。

##### 3.3.3.1. 任务

###### 3.3.3.1.1. 定义通信矩阵

表3.100：定义通信矩阵（**Define Communication Matrix**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | The communication matrix contents are created or extended by adding communication definitions. | — |
| 描述 | Define or extend Communication Matrix. Define the triggering of the Physical Channels and the mapping to the communication connector ports. In case of extension the original communication matrix contents (which were delivered as part of a system extract) are extended by adding communication definitions. The main use case is the extension of the communication matrix when refining a sub-system. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Topology | 1 |
| 产出 | Communication Matrix | 1 |

###### 3.3.3.1.2. 定义帧

表3.101：定义帧（**Define Frames**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define Data Link Layer | — |
| 描述 | Define the Frame and assign it to a physical channel of a communication cluster. Determine the number, the type, the length and the timing of Frames that are sent or received by the ECUs. Describe the mapping of Pdus (I-Pdus, N-Pdus or NmPdus) into the frame. Define the triggering and the identification of a frame on the physical channel, on which it is sent. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Interaction Layer | 0..1 |
| 消费 | Network Layer | 0..1 |
| 产出 | Data Link Layer | 1 |

###### 3.3.3.1.3. 定义信号 PDU

表3.102：定义信号 PDU（**Define Signal PDUs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define the I-PDU and their ISignals | — |
| 描述 | Define the Signal Pdu that is handled by AUTOSAR COM and assign it to a physical channel of a communication cluster. Determine the length and the timing and describe the mapping of Signals into the Signal Pdu.. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Data Mapping | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | System Signal | 1 |
| 消费 | Topology | 1 |
| 产出 | Interaction Layer | 1 ISignals |

###### 3.3.3.1.4. 定义受保护的 PDU

表3.103：定义受保护的 PDU（**Define Secured PDUs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define Secured PDUs | — |
| 描述 | If a secured communication of a PDU over network is required, SecuredIPDUs are defined. A secured communication can be established for IPDUs from the Interaction Layer. In addition to the SecuredPDUs corresponding SecureCommunicationProperties are specified that describe how the PDU is secured (e.g. authentication algorithm). | — |
| 执行者 | System Engineer | 1 |
| 消费 | Interaction Layer | 1 I-PDUs: Authentic IPdu that will be secured against manipulation and replay attacks. |
| 消费 | Topology | 0..1 |
| 产出 | Interaction Layer | 1 Secured PDUs: Secured IPdu that contains payload of an Authentic IPdu supplemented by additional Authentication Information. |

###### 3.3.3.1.5. 定义 TP

表3.104：定义 TP（**Define TP**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define the Network management and the N-PDUs | — |
| 描述 | Define the N-PDU - Network Layer Protocol Data Unit (assembled and disassembled in a Transport Protocol module). If an I-PDU does not fit into one frame, a segmentation is needed and will be done through several N-PDUs by the Transport Protocol module. If large COM PDUs are transported by TP, the Interaction Layer should be the Input to the Define TP task. If Diagnostic is used then the Diagnostics Interaction Layer should be an output of Task Define TP. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Topology | 1 |
| 消费 | Interaction Layer | 0..1 |
| 产出 | Network Layer | 1 |
| 产出 | Diagnostics Interaction Layer | 0..1 |

###### 3.3.3.1.6. 定义网络管理

表3.105：定义网络管理（**Define Network Management**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define the Network Management that is responsible for the communication cluster wide coordinated switching of ECUs between operational modes (Network Mode, Bus-sleep Mode). Describe the Nm Pdus and configure the Nm Coordinator, the Nm Clusters and Nm Nodes. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Topology | 1 |
| 消费 | Interaction Layer | 0..1 |
| 产出 | Network Layer | 1 |

###### 3.3.3.1.7. 定义 PDU 网关

表3.106：定义 PDU 网关（**Define PDU Gateway**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define the gateway for IPDUs | — |
| 描述 | Define the gateways that are transferring the I-Pdus from one channel to the other in pairs. Each pair consists of a source and a target referencing to a IPduTriggering. In the case that a Pdu is being gatewayed to more than one channel of the same communication cluster, all of this gateway relationships shall be specified. Therefore, all affected IpduTriggerings must be described as gateway mappings. | — |
| 执行者 | System Engineer | 1 |
| 输入/输出 | Interaction Layer | 1 |

###### 3.3.3.1.8. 定义信号网关

表3.107：定义信号网关（**Define Signal Gateway**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define the Signal Gateway to describe the routing of signals and signal groups from one Physical Channel to another Physical Channel. | — |
| 执行者 | System Engineer | 1 |
| 输入/输出 | Interaction Layer | 1 |

###### 3.3.3.1.9. 定义 RTE 扇出

表3.108：定义 RTE 扇出（**Define RTE Fan-out**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define RTE fan-out which are the relation between ISignals and System Signal | — |
| 描述 | The RTE supports a "signal fan-out" where the same signal (System Signal) is sent in different IPdus to multiple receivers. The Pdu Router supports the "PDU fan-out" where the same IPdu is sent to multiple destinations. | — |
| 执行者 | System Engineer | 1 |
| 消费 | System Signal | 1..* |
| 产出 | Interaction Layer | 1 Link of ISignals to System Signals |

###### 3.3.3.1.10. 定义转换技术

表3.109：定义转换技术（**Define Transformation Technology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define the transformer for serialization. | — |
| 描述 | This task defines the transformer for serialization. In general, there are two possibilities: serialization based on network representation and serialization based on Implementation data types. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Interaction Layer | 1 ISignals: |
| 产出 | Serializer Transformer | 1 SerializerTransformerTechnology: |

###### 3.3.3.1.11. 定义 E2E 转换器技术

**见图 2.64 任务 定义 E2E 转换器技术**

表3.110：定义 E2E 转换器技术（**Define E2E Transformer Technology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Define the E2E transformer technology. | — |
| 描述 | This task defines the E2E transformer technology. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Interaction Layer | 1 ISignals: |
| 产出 | E2E Transformer | 1 E2ETransformerTechnology: |

###### 3.3.3.1.12. 定义转换链

表3.111：定义转换链（**Define Transformation Chain**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Tasks | — |
| 简要描述 | Concatenate several transformers to a transformer chain. | — |
| 描述 | In this task the several Transformers are concatenated to a Transformer chain producing a set of DataTransformationSets. | — |
| 执行者 | System Engineer | 1 |
| 消费 | Serializer Transformer | 1 |
| 消费 | Custom Transformer | 0..1 |
| 消费 | E2E Transformer | 0..1 |
| 产出 | Interaction Layer | 1 TransformationChain: |

##### 3.3.3.2. 工作产品

###### 3.3.3.2.1. 通信层

| Deliverable | Communication Layers |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products |  |  |
| Brief Description | Communication Matrix |  |  |
| Description | It's a container for the description elements of the communication layers |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregated by | System Description | 0..1 |  |
| Aggregates | Data Link Layer | 1 |  |
| Aggregates | Interaction Layer | 1 |  |
| Aggregates | Diagnostics Interaction Layer | 0..1 |  |
| Aggregates | Network Layer | 0..1 |  |
| Consumed by | Define System Timing | 1 |  |
| Consumed by | Extract the ECU Communication | 1 |  |
| Consumed by | Set System Root | 1 | Only the reference to the artifact is needed |

###### 3.3.3.2.2. 通信矩阵

表3.112：通信矩阵（**Communication Matrix**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 |  | — |
| 描述 | Define the mapping of the triggering elements within the Physical Channels to the communication connector ports for the individual ECUs. Because the triggering elements are aggregated as splitable elements within the Physical Channels it is possible to define them in an artifact separated from the Topology. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | System Description | 0..* |
| 产出者 | Define Communication Matrix | 1 |
| 使用的元模型元素 | FrameTriggering 1 | — |
| 使用的元模型元素 | ISignalTriggering 1 | — |
| 使用的元模型元素 | PduTriggering 1 | — |

###### 3.3.3.2.3. 数据链路层

表3.113：数据链路层（**Data Link Layer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 | Describes the frames that are used in the Data Link Layer | — |
| 描述 | Describes the layout of frames to be sent over communication channels. This definition belongs to the Data Link Layer. The Data Link Layer provides the functional and procedural means to transfer data between network entities. This layer is used to transmit data passed by an upper layer (PduR, Tp) between adjacent network nodes. In AUTOSAR the Drivers (FrDrv, CanDrv, LinDrv) and Interfaces (FrIf, CanIf, LinIf) belong to the Data Link Layer. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Communication Layers | 1 |
| 产出者 | Define Frames | 1 |
| 使用的元模型元素 | Frame 1 | — |

###### 3.3.3.2.4. 交互层

表3.114：交互层（**Interaction Layer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 | Describes the Signals of the Interaction Layer. | — |
| 描述 | Describes the Signals of the Interaction Layer covering the COM Signals. The Interaction Layer packs one or more signals into assigned COM I-Pdus and passes them to the underlying layer for transfer between nodes in a network. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Communication Layers | 1 |
| 产出者 | Define RTE Fan-out | 1 Link of ISignals to System Signals |
| 产出者 | Define Secured PDUs | 1 Secured PDUs: Secured IPdu that contains payload of an Authentic IPdu supplemented by additional Authentication Information. |
| 产出者 | Define Signal PDUs | 1 ISignals |
| 产出者 | Define Transformation Chain | 1 TransformationChain: |
| 输入/输出 | Define PDU Gateway | 1 |
| 输入/输出 | Define Signal Gateway | 1 |
| 消费者 | Define E2E Transformer Technology | 1 ISignals: |
| 消费者 | Define Secured PDUs | 1 I-PDUs: Authentic IPdu that will be secured against manipulation and replay attacks. |
| 消费者 | Define Transformation Technology | 1 ISignals: |
| 消费者 | Define Frames | 0..1 |
| 消费者 | Define Network Management | 0..1 |
| 消费者 | Define TP | 0..1 |
| 使用的元模型元素 | DataTransformationSet 1 | — |
| 使用的元模型元素 | IPdu 1 | — |
| Use meta element | ISignal | 1 |

###### 3.3.3.2.5. 诊断交互层

表3.115：诊断交互层（**Diagnostics Interaction Layer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 |  | — |
| 描述 | Collection of DCM IPDUs. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Communication Layers | 0..1 |
| 产出者 | Define TP | 0..1 |
| 使用的元模型元素 | DcmIPdu 1 | — |

###### 3.3.3.2.6. 网络层

表3.116：网络层（**Network Layer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 | Describes the PDUs of the Network Layer. | — |
| 描述 | Describes the PDUs of the Network Layer (N-PDUs and NM-PDUs). The Network Layer's main purposes are : • the segmentation and reassembly of I-PDUs and DCM I-PDUs that do not fit in one of the assigned N-PDUs • the definition of NM-PDUs | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Communication Layers | 0..1 |
| 产出者 | Define Network Management | 1 |
| 产出者 | Define TP | 1 |
| 消费者 | Define Frames | 0..1 |
| 使用的元模型元素 | NPdu 1 | — |

###### 3.3.3.2.7. 序列化转换器

表3.117：序列化转换器（**Serializer Transformer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 | Serialization of the input data | — |
| 描述 | This transformer performs the serialization of the input data. It is the first transformer in the transformer chain. | — |
| 种类 |  | — |
| 产出者 | Define Transformation Technology | 1 SerializerTransformerTechnology: |
| 消费者 | Define Transformation Chain | 1 |

###### 3.3.3.2.8. E2E 转换器

表3.118：E2E 转换器（**E2E Transformer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Communication Matrix::Work products | — |
| 简要描述 | E2E protection transformation | — |
| 描述 | This transformer adds E2E protection related information to the data stream. | — |
| 种类 |  | — |
| 产出者 | Define E2E Transformer Technology | 1 E2ETransformerTechnology: |
| 消费者 | Define Transformation Chain | 0..1 |

#### 3.3.4. ECU 提取

##### 3.3.4.1. 任务

###### 3.3.4.1.1. 提取 ECU 拓扑

表3.119：提取 ECU 拓扑（**Extract ECU Topology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 | Extract the topology for a single ECU from the System Topology | — |
| 描述 | From the System or System Extract Topology, extract the topology for a single ECU. | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | Topology | 1 |
| 产出 | ECU Extract of Topology | 1..* |

###### 3.3.4.1.2. 生成或调整 ECU Flat Map

表3.120：生成或调整 ECU Flat Map（**Generate or Adjust ECU Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 | Generates and/or adjust the unique names of component prototypes and MCD display data in the scope of a single ECU. | — |
| 描述 | Generates and/or adjust the unique names of component prototypes and MCD display data in the scope of a single ECU. This information is kept in the so-called ECU Flat Map. The names can be generated according to some rules (e.g. from model elements of the VFB system), taken over from the System Flat Map, from partial Flat Maps, or be manually defined. The task shall always result in an ECU Flat Map with unique names. | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | Overall VFB System | 0..1 Used to set the upstream references in case one starts from a complete system. |
| 消费 | System Flat Map | 0..1 Take over definitions of unique names from system level to ECU level. |
| 消费 | VFB System Extract | 0..1 Used to set the upstream references in case one starts from a system extract. |
| 消费 | Partial Flat Map | 0..* If Partial Flat Maps were delivered along with software components referring only to ECU internal information, they may be integrated into the ECU Flat Map directly, i.e. without needing the System Flat Map. • The instance refs used in a partial flat map must be taken over and adjusted to the context ECU Extract. • Name conflicts have to be resolved if several partial flat maps are merged. |
| 输入/输出 | ECU Flat Map | 1 |

###### 3.3.4.1.3. 拍平软件组合

表3.121：拍平软件组合（**Flatten Software Composition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 | Extract and flatten the ECU Software Composition. | — |
| 描述 | Generate the complete software composition in an ECU by copying ComponentPrototypes from the VFB description into a flat representation (still without service components). Flat representation means, that all compositions are removed and a "flat" set of Componet Prototypes is generated. Due to the replication of ComponentPrototypes new names have to be generated for those. These can be predefined in the FlatMap which is an input to this task. The ECU Extract of Data Mapping is also created by this task, as the references to the Data Prototypes need to be created with respect to the new component structure. | — |
| 执行者 | System Engineer | 1 |
| 执行者 | ECU Integrator | 0..1 |
| 消费 | ECU Flat Map | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | System Description Root Element | 1 find the top level composition |
| 消费 | Data Mapping | 1..* |
| 消费 | Overall VFB System | 0..1 Read relevant elements starting from VFB Top Level System Composition in case transformation starts with the full system. |
| 消费 | VFB System Extract | 0..1 Read relevant elements starting from VFB Top Level System Composition in case transformation starts from the system extract. |
| 产出 | ECU Extract of Data Mapping | 1 |
| 产出 | ECU Extract of VFB System | 1 |

###### 3.3.4.1.4. 提取 ECU 通信

表3.122：提取 ECU 通信（**Extract the ECU Communication**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 | The limited-scope communication matrices for an ECU to communicate on all networks on which it is directly connected. | — |
| 描述 | The limited-scope communication matrices for an ECU to communicate on all networks on which it is directly connected. | — |
| 执行者 | ECU Integrator | 1 |
| 执行者 | System Engineer | 1 |
| 消费 | Communication Layers | 1 |
| 消费 | Mapping of Software Components to ECUs | 1 |
| 消费 | VFB System | 1 Need as input in order to set up the Data Mapping. |
| 消费 | System Signal | 0..* |
| 消费 | System Signal Group | 0..* |
| 产出 | ECU Extract for Communication | 1..* |

###### 3.3.4.1.5. 提取 ECU 时序模型


表3.123：Extract ECU System Timing（**Extract ECU System Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 |  | — |
| 描述 | Extract the System Timing Model for a particular ECU from the model for a complete system or system extract. | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | System Timing | 1 |
| 产出 | ECU Extract of System Timing | 1 |

###### 3.3.4.1.6. 提取 ECU 系统变体模型


表3.124：Extract ECU System Variant Model（**Extract ECU System Variant Model**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 |  | — |
| 描述 | Extract the global model elements (ARElements) that are used to describe variants from system or system extract scope to a particular ECU scope. This applies to: • System Constant Value Set • Postbuild Variant Set • Predefined Variant • Evaluated Variant Set They are transformed as far as they are needed into the ECU Extract. | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | Evaluated Variant Set | 0..* |
| 消费 | Postbuild Variant Set | 0..* |
| 消费 | Predefined Variant | 0..* |
| 消费 | System Constant Value Set | 0..* |
| 产出 | ECU Extract of System Variant Model | 1 |

###### 3.3.4.1.7. 提取 ECU 快速原型场景


表3.125：提取 ECU 快速原型场景（**Extract ECU Rapid Prototyping Scenario**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Tasks | — |
| 简要描述 | Extracts the ECU Rapid Prototyping Scenario | — |
| 描述 | From the System Rapid Prototyping Scenario extract the entities relevant for the single ECU. | — |
| 执行者 | ECU Integrator | 0..1 |
| 执行者 | System Engineer | 0..1 |
| 消费 | Rapid Prototyping Scenario | 1 |
| 产出 | ECU Extract of Rapid Prototyping Scenario | 1 |

##### 3.3.4.2. 工作产品

###### 3.3.4.2.1. ECU 提取

| Deliverable | ECU Extract |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products |  |  |
| Brief Description | A version of the System Description, with information pertaining to a single ECU. |  |  |
| Description | A deliverable used to describe the ECU specific view on the System Description. The ECU Extract is fully decomposed and contains only Atomic Software Components.It is the basis for setting up the ECU Configuration. A timing model is optionally included. This deliverable may contain variation points in its XML artifacts which need to be bound for the ECU. If such variation points are present, the ECU extract may optionally include Predefined Variants in order to predefine variants for later selection and an Evaluated Variant Set (this is expressed by artifact ECU Extract of System Variant Model). This deliverable corresponds to the system description with the system category "ECU_EXTRACT" (see [TPS_SYST_01003]). |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | ECU Extract Root Element | 1 |  |
| Aggregates | ECU Extract for Communication | 1 |  |
| Aggregates | ECU Extract of Data Mapping | 1 |  |
| Aggregates | ECU Extract of Topology | 1 |  |
| Deliverable | ECU Extract |  |  |
| Aggregates | ECU Extract of VFB System | 1 |  |
| Aggregates | ECU Flat Map | 1 |  |
| Aggregates | ECU Extract of Rapid Prototyping Scenario | 0..1 |  |
| Aggregates | ECU Extract of System Timing | 0..1 |  |
| Aggregates | ECU Extract of System Variant Model | 0..1 |  |
| Produced by | Generate ECU Extract | 1 |  |
| Produced by | Develop Sub-System | 1..* |  |
| Produced by | Develop System | 1..* |  |
| Consumed by | Configure Com | 1 |  |
| Consumed by | Configure Diagnostics | 1 | Application software requirements for diagnostics, especially SwcServiceDependency and ServiceNeeds. |
| Consumed by | Configure ECUC | 1 |  |
| Consumed by | Configure NvM | 1 | Application software requirements for NvM, especially SwcServiceDependency and ServiceNeeds. |
| Consumed by | Configure RTE | 1 | Elements of the System Description and VFB Description are referred by the RTE configuration. Optional Input: ECU Extract of System Timing, e.g. execution order constraints. |
| Consumed by | Configure Watchdog Manager | 1 | Application software requirements for WdgM, especially SwcServiceDependency and ServiceNeeds. |
| Consumed by | Connect Service Component | 1 | Find the ports on the application side to be connected to the Service Component. |
| Consumed by | Define Integration Variant | 1 |  |
| Consumed by | Generate Base Ecu Configuration | 1 |  |
| Consumed by | Generate RTE | 1 | Find the VFB description of all Atomic Software Components on this ECU and the relevant parts of the system description. The ECU Flat Map is also an input. Meth.bindingTime = SystemDesignTime |
| Consumed by | Generate RTE Postbuild Dataset | 1 | Meth.bindingTime = LinkTime |
| Consumed by | Generate RTE Prebuild Dataset | 1 | Meth.bindingTime = CodeGenerationTime |
| Consumed by | Generate Updated ECU Configuration | 1 |  |
| Consumed by | Integrate Software for ECU | 1 |  |
| Consumed by | Prepare ECU Configuration | 1 |  |
| Consumed by | Update ECU Configuration | 1 |  |
| Consumed by | Configure Mode Management | 0..1 | Application software requirements for NvM, especially SwcServiceDependency and ServiceNeeds. Input in case atomic software components are available. |
| Consumed by | Create MC Function Model | 0..1 | The ECU Flat Map can be used to define references to variables and parameters which are later visible in A2L. Furthermore, the ECU Extract can be used to find the relevant software components. |
| Consumed by | Create Service Component | 0..1 | Input information about the Service Ports and Service Dependencies of the software components. |
| Deliverable | ECU Extract |  |  |
| Consumed by | Define ECU Timing | 0..1 | Needed to set up links to the elements of the ECU extract. |
|  | Configure Transformer | 1 |  |

###### 3.3.4.2.2. ECU 提取根元素

表3.126：ECU 提取根元素（**ECU Extract Root Element**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 |  | — |
| 描述 | Extract of the System root element for a specific ECU. | — |
| 种类 | AUTOSAR XML | — |
| 扩展 | System | — |
| 聚合于 | ECU Extract | 1 |
| 消费者 | Generate Rapid Prototyping Wrapper | 1 |
| 使用的元模型元素 | System 1 | — |

###### 3.3.4.2.3. VFB 系统的 ECU 提取

| Deliverable | ECU Extract of VFB System |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products |  |  |
| Brief Description | Contains the complete software composition in an ECU, copied from the VFB description into a flat representation, it is still without service components. |  |  |
| Description | Contains the complete software composition in an ECU, copied from the VFB description into a flat representation, that means it is still without service components. Flat representation means, that all compositions have been removed and a "flat" set of ComponentPrototypes was generated (including their connectors) which are put into the top level composition of the ECU. |  |  |
| Kind | Delivered |  |  |
| Extends | VFB System |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregated by | ECU Extract | 1 |  |
| Produced by | Flatten Software Composition | 1 |  |
| Consumed by | Generate Rapid Prototyping Wrapper | 1 |  |
| Use meta model element | RootSwComposition Prototype | 1 |  |

###### 3.3.4.2.4. 数据映射的 ECU 提取

表3.127：数据映射的 ECU 提取（**ECU Extract of Data Mapping**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 |  | — |
| 描述 | ECU extract of the mapping of data prototypes from the (flattened) VFB description to System Signals. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 1 |
| 产出者 | Flatten Software Composition | 1 |
| 使用的元模型元素 | DataMapping 1 | — |

###### 3.3.4.2.5. 拓扑的 ECU 提取

表3.128：拓扑的 ECU 提取（**ECU Extract of Topology**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 | A view of the topology centered around a single ECU. | — |
| 描述 | A view of the topology centered around a single ECU. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 1 |
| 产出者 | Extract ECU Topology | 1..* |
| 使用的元模型元素 | CommunicationCluster 1 | — |
| 使用的元模型元素 | EcuInstance 1 | — |

###### 3.3.4.2.6. 用于通信的 ECU 提取

表3.129：用于通信的 ECU 提取（**ECU Extract for Communication**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 | A version of the System Communication Matrix work product, with information pertaining to a single ECU. | — |
| 描述 | This artifact represents an extract of the System Description elements for communication with respect to a single ECU. It provides all information needed to let the ECU communicate on all networks on which it is directly connected. It is extracted from these system artifacts: • Communication Matrix • Communication Layers • System Signal(s) • System Signal Group(s) | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 1 |
| 产出者 | Extract the ECU Communication | 1..* |
| 使用的元模型元素 | FibexElement 1 | — |

###### 3.3.4.2.7. 系统时序的 ECU 提取

表3.130：系统时序的 ECU 提取（**ECU Extract of System Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 |  | — |
| 描述 | The extract of the System Timing for a particular ECU. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 0..1 |
| 产出者 | Extract ECU System Timing | 1 |
| 消费者 | Define ECU Timing | 0..1 |
| 使用的元模型元素 | SystemTiming 1 | — |

###### 3.3.4.2.8. 系统变体模型的 ECU 提取

| Deliverable | ECU Extract of System Variant Model |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products |  |  |
| Brief Description |  |  |  |
| Description | An extract of the System artifacts • System Constant Value Set • Postbuld Variant Set • Predefined Variant • Evaluated Variant Set It contains only the elements relevant for a particular ECU. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregated by | ECU Extract | 0..1 |  |
| Aggregates | Evaluated Variant Set | 0..* |  |
| Aggregates | Postbuild Variant Set | 0..* |  |
| Aggregates | Predefined Variant | 0..* |  |
| Aggregates | System Constant Value Set | 0..* |  |
| Produced by | Extract ECU System Variant Model | 1 |  |
| Consumed by | Generate Rapid Prototyping Wrapper | 0..1 |  |

###### 3.3.4.2.9. ECU Flat Map

表3.131：ECU Flat Map（**ECU Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 | Mapping of instance names to nested model elements. Use cases: Resolve name conflicts when flattening VFB software compositions; provide unique names for measurement and calibration data. | — |
| 描述 | The flat map is a list of elements, each element represents exactly one node (e.g. a component instance or data element) of the instance tree of a software system. The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name to it. The name will be unique in the scope of a single ECU. (Note that additional alias names can be defined via artifact Alias Name Set.) Use cases: • Specify the display name of a data object for measurement and calibration. This serves as an input for the calibration support which is produced by the RTE generator. The RTE generator needs to find the attributes assigned to these data via the attached references. • Specify a unique name for an instance of a component prototype in the ECU extract of the system description. This information is needed to set up the ECU extract. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 1 |
| 输入/输出 | Generate or Adjust ECU Flat Map | 1 |
| 消费者 | Flatten Software Composition | 1 |
| 消费者 | Generate Local MC Data Support | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Rapid Prototyping Wrapper | 1 |
| 消费者 | Provide RTE Calibration Dataset | 1 |
| 消费者 | Generate A2L | 0..1 The ECU Flat Map is needed in case the A2L generator has to process an MC Function Model that relates to data in the ECU Flat Map. |
| 使用的元模型元素 | FlatInstanceDescriptor 1 | — |

###### 3.3.4.2.10. 快速原型场景的 ECU 提取

表3.132：快速原型场景的 ECU 提取（**ECU Extract of Rapid Prototyping Scenario**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::ECU Extract::Work products | — |
| 简要描述 | Description of the (required) bypass points in the ECU. | — |
| 描述 | Description of the (required) bypass points in the ECU. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | ECU Extract | 0..1 |
| 产出者 | Extract ECU Rapid Prototyping Scenario | 1 |
| 输入/输出 | Refine Rapid Prototyping Scenario | 1 |
| 消费者 | Generate Rapid Prototyping Wrapper | 1 |

### 3.4. 软件组件

本章包含针对给定 VFB 描述开发单个软件组件所用的工作产品和任务 的定义。相关元模型元素的定义参见 [\[7, CP TPS Software Component Template\]](#ref-7)。

#### 3.4.1. 任务

##### 3.4.1.1. 定义软件组件内部行为

表3.133：Define Atomic Software Component Internal Behavior（**Define Atomic Software Component Internal Behavior**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Define the InternalBehavior in relation to a given AtomicSoftwareComponentType | — |
| 描述 | Define the InternalBehavior in relation to a given AtomicSoftwareComponentType so that an RTE API can be generated. This includes the definition of Runnables, RTE Events, Inter-Runnable variables, etc. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | VFB Atomic Software Component | 1 |
| 消费 | VFB AUTOSAR Standard Package | 0..1 Use standardized elements (e.g. Data Types) as blueprints (as far as applicable) to create the corresponding elements of the actual project. |
| 产出 | Software Component Internal Behavior | 1 |

##### 3.4.1.2. 定义部分 Flat Map


表3.134：定义部分 Flat Map（**Define Partial Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define a Partial Flat Map for an intended delivery of Atomic Software Components. | — |
| 执行者 | Software Component Designer | 0..1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | VFB System | 1 Various parts of a given VFB system will be used as input: • Refer to parameters and variables in port interfaces and their data types. • In order to define unique names, also other the component definitions not in the scope of the partial flat map might be checked. • Set a link to the context of the Flat Map, e.g. a VFB Composition. |
| 消费 | Software Component Internal Behavior | 0..* Refer to parameter and variables defined in the Internal Behavior of one or more Atomic Software Components. |
| 产出 | Partial Flat Map | 1 |

##### 3.4.1.3. 定义软件组件时序

表3.135：定义软件组件时序（**Define Software Component Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Define SWCTiming (TimingDescription and TimingConstraints) for the Internal Behavior (Runnable Entities) of a Software Component | — |
| 描述 | Define SWCTiming (TimingDescription and TimingConstraints) of a software component. A software component can either be of type AtomicSWComponentType or CompositionSWComponentType. In the former case, the task allows to describe timing description and constraints for the Internal Behavior of the AtomicSWComponentType. In the latter case, timing descriptions and constraints can be defined for all Atomic Software Components in the CompositionSWComponentType. | — |
| 执行者 | Software Component Developer | 1 |
| 消费 | Software Component Internal Behavior | 1 |
| 消费 | VFB Timing | 0..1 |
| 产出 | Software Component Timing | 1 |

##### 3.4.1.4. 为类型定义 SymbolProps

表3.136：为类型定义 SymbolProps（**Define SymbolProps for Types**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Define SymbolProps for types in order to resolve name conflicts in the code. | — |
| 描述 | Redefines the symbols used by the RTE contract for the names of software component types and/or implementation data types (in the code as well as in certain header file names). This task is used to resolve name conflicts between different software components without changing the VFB model. | — |
| 执行者 | Software Component Developer | 1 |
| 产出 | VFB Atomic Software Component | 0..* symbolProps: The symbolProps attribute redefines the software component type name used in the code of the RTE. This resolves name clashes among different software component types designed accidentally with the same shortName. Note that this output is a splitable element, so it can be added later without changing the VFB model. |
| 产出 | VFB Types | 0..* symbolProps: The symbolProps attribute redefines the implementation data type name used in the code of the RTE and/or the component. This resolves name clashes among different implementation data types designed accidentally with the same shortName. Note that this output is a splitable element, so it can be added later without changing the VFB model. |

##### 3.4.1.5. 为软件组件添加文档

表3.137：为软件组件添加文档（**Add Documentation to the Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Add documentation to the Software Component | — |
| 描述 | Add documentation to the Software Component describing the functionality, how to test it, the calibration uses, the maintenance and diagnosis issues. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | Partial Flat Map | 0..1 Optional input in order to refer to unique names defined in component or composition context. |
| 消费 | System Flat Map | 0..1 Optional input in order to refer to unique names defined in system context. |
| 消费 | Alias Name Set | 0..* Optional input in order to refer to unique names defined in an Alias Name Set (e.g. System Constants). |
| 输入/输出 | Software Component Documentation | 1 |

##### 3.4.1.6. 生成原子软件组件合同头文件

表3.138：生成原子软件组件合同头文件（**Generate Atomic Software Component Contract Header Files**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Generate the component contract header files. | — |
| 描述 | Generate the component header files as part of the so-called "contract phase". These headers will allow to link the component lateron with the RTE. The header can still contain variants with later binding time, therefore the information about these variants is contained in the input to this task. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | Software Component Developer | 1 |
| 消费 | Software Component Internal Behavior | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Atomic Software Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Postbuild Variant Set | 0..1 |
| 消费 | Predefined Variant | 0..1 |
| 消费 | Software Component to BS WMapping | 0..1 If a Software Component is mapped to a BSW module description, this input is optionally needed already in the contract phase in order to ensure that the generated prototypes for runnables are consistent with the definitions in Software Component and BSW. Meth.bindingTime = SystemDesignTime |
| 消费 | System Constant Value Set | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB AUTOSAR Standard Package | 0..1 |
| 消费 | VFB Data Type Mapping Set | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Interfaces | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Modes | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Types | 0..* Meth.bindingTime = SystemDesignTime |
| 产出 | Application Header File | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Software Component Data Types Header | 1 Meth.bindingTime = CodeGenerationTime |
| 使用的工具 | Component API Generator Tool | 1 |

##### 3.4.1.7. 以供应商模式生成组件头文件

表3.139：以供应商模式生成组件头文件（**Generate Component Header File in Vendor Mode**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Generate an optimized component header file. This is achieved by using the RTE's vendor mode. | — |
| 描述 | Generate an optimized component header file. This is achieved by using the RTE's vendor mode. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | Software Component Developer | 1 |
| 执行者 | ECU Integrator | 0..1 |
| 消费 | Atomic Software Component Implementation | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component Internal Behavior | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Atomic Software Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB AUTOSAR Standard Package | 0..1 |
| 消费 | VFB Data Type Mapping Set | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Interfaces | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Modes | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | VFB Types | 0..* Meth.bindingTime = SystemDesignTime |
| 产出 | Optimized Application Header File | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Software Component Data Types Header | 1 Meth.bindingTime = CodeGenerationTime |
| 使用的工具 | Component API Generator Tool | 1 |

##### 3.4.1.8. 生成组件预构建数据集

表3.140：生成组件预构建数据集（**Generate Component Prebuild Data Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Prebuild Data Set Generation Phase for a software component: It binds all variations which need to be set after generation of the RTE contract header but before compilation of the component. | — |
| 描述 | Prebuild Data Set Generation Phase for a software component: It binds all variations which need to be set after generation of the RTE contract header but before compilation of the component. The output is a configuration header which is used when compiling the component and the RTE as well. Meth.bindingTime = PreCompileTime | — |
| 执行者 | Software Component Developer | 1 |
| 消费 | Software Component Internal Behavior | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | VFB Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | System Constant Value Set | 1..* Meth.bindingTime = CodeGenerationTime |
| 消费 | VFB AUTOSAR Standard Package | 0..1 |
| 消费 | VFB Data Type Mapping Set | 0..1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Predefined Variant | 0..* |
| 消费 | VFB Interfaces | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | VFB Modes | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | VFB Types | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | Component RTE Prebuild Configuration Header | 1 Meth.bindingTime = PreCompileTime |
| 使用的工具 | Component API Generator Tool | 1 |

##### 3.4.1.9. 实现原子软件组件

表3.141：实现原子软件组件（**Implement Atomic Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Implement the code of the AtomicSoftwareComponent and decribe the Implementation. | — |
| 描述 | Implement the code of the AtomicSoftwareComponent against the generated component contract header. Document the basic information in the Implementation Description. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | Software Component Developer | 1 |
| 消费 | Application Header File | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component Data Types Header | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component Internal Behavior | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component Timing | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | Standard Header Files | 0..1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Library Description | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Library Header Files | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | Atomic Software Component Implementation | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Atomic Software Component Source Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.4.1.10. 编译原子软件组件

表3.142：编译原子软件组件（**Compile Atomic Software Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Compile the AtomicSoftwareComponent independently of an ECU. | — |
| 描述 | Compile the Atomic Software Component independently of an ECU. In the context of Rapid Prototyping Wrapper compilation the task is performed by the Rapid Prototyping Engineer. Meth.bindingTime = CompileTime | — |
| 执行者 | Rapid Prototyping Engineer | 0..1 |
| 执行者 | Software Component Developer | 0..1 |
| 消费 | Application Header File | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Atomic Software Component Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Software Component Data Types Header | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Standard Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Component RTE Prebuild Configuration Header | 0..1 Meth.bindingTime = PreCompileTime |
| 消费 | Rapid Prototyping Wrapper Header File | 0..1 |
| 消费 | Rapid Prototyping Wrapper Source Code | 0..1 |
| 消费 | Library Header Files | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | Atomic Software Component Object Code | 1 The object file should include both code of the SWC and the E2E Protection Wrapper code (if present as an input). Meth.bindingTime = CompileTime |
| 使用的工具 | Compiler | 1 |

##### 3.4.1.11. 将软件组件映射到 BSW

表3.143：将软件组件映射到 BSW（**Map Software Component to BSW**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Define the mapping between a Software Component and a BSW Module. | — |
| 描述 | Define the mapping between a Software Component and a BSW Module. Required only for Complex Drivers and ECU Abstraction Components. Note that for Service Components, this mapping will be generated in the ECU integration phase, so the latter is not considered as a task in the responsibility of the BSW developer. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | ECU Integrator | 0..1 |
| 消费 | Basic Software Module Internal Behavior | 1 |
| 消费 | Software Component Internal Behavior | 1 |
| 消费 | Complex Driver Component | 0..1 |
| 消费 | ECU Abstraction Software Component | 0..1 |
| 产出 | Software Component to BS WMapping | 1 |

##### 3.4.1.12. 测量组件资源

表3.144：测量组件资源（**Measure Component Resources**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Measure the resource consumption of an Atomic Software Component | — |
| 描述 | Determine the resource consumption (memory, execution time) for a specific implementation of an Atomic Software Component in a certain context (ECU or test environment) and document the results in the Implementation description targeted at this specific platform. The ECU Resources Description is an optional input, because some results should be documented in relation to the hardware elements. | — |
| 执行者 | Software Component Developer | 1 |
| 执行者 | Basic Software Module Developer | 0..1 |
| 执行者 | ECU Integrator | 0..1 |
| 消费 | Atomic Software Component Object Code | 1 |
| 消费 | ECU Resources Description | 0..1 |
| 消费 | Software Component Timing | 0..1 |
| 输入/输出 | Atomic Software Component Implementation | 1 |

##### 3.4.1.13. 在 ECU 上下文中重新编译组件

表3.145：Re-compile Component in ECU context（**Re-compile Component in ECU context**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Re-compile Component with ECU-Configuration specific optimizations. | — |
| 描述 | Re-compile Component with optimizations made by the RTE in the context of an ECU (so-called RTE implementation phase). Meth.bindingTime = CompileTime | — |
| 执行者 | Software Component Developer | 1 |
| 消费 | Atomic Software Component Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Optimized Application Header File | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Standard Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Library Header Files | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | Optimized Software Component Object Code | 1 Meth.bindingTime = CompileTime |
| 使用的工具 | Compiler | 1 |

##### 3.4.1.14. 定义一致性需求

表3.146：定义一致性需求（**Define Consistency Needs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 |  | — |
| 描述 | Defines the consistency relations between a group of RunnableEntitys and a group of Data Prototypes. The consistency relations can be defined first time at the design of an Atomic Software Component but can be added as well if Compositions are created. | — |
| 执行者 | Software Component Designer | 1 |
| 执行者 | Software Component Developer | 1 |
| 消费 | Software Component Internal Behavior | 1..* Runnables the consistency is defined for. |
| 消费 | VFB Atomic Software Component | 0..* The description of an AtomicSoftwareComponentType without InternalBehavior. |
| 消费 | VFB Interfaces | 0..* Interfaces which are relevant for the consistency definition. |
| 消费 | VFB Types | 0..* Data types which are relevant for the consistency definition. |
| 输入/输出 | Consistency Needs | 1 The description of the correlation between a group of RunnableEntitys and a group of DataPrototypes. In order to allow incremental development and refinement the Consistency Needs artifact is also used as an input. |

##### 3.4.1.15. 生成快速原型包装器

表3.147：生成快速原型包装器（**Generate Rapid Prototyping Wrapper**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Tasks | — |
| 简要描述 | Generate Rapid Prototyping Wrapper code. | — |
| 描述 | Generate Rapid Prototyping Wrapper code. The header and source code are generated based on the Rapid Prototyping Scenario describing the bypass points and the RPT hooks. | — |
| 执行者 | Rapid Prototyping Engineer | 1 |
| 消费 | ECU Extract Root Element | 1 |
| 消费 | ECU Extract of Rapid Prototyping Scenario | 1 |
| 消费 | ECU Extract of VFB System | 1 |
| 消费 | ECU Flat Map | 1 |
| 消费 | Software Component Internal Behavior | 1 |
| 消费 | ECU Extract of System Variant Model | 0..1 |
| 产出 | Rapid Prototyping Wrapper Header File | 1 |
| 产出 | Rapid Prototyping Wrapper Source Code | 1 |

#### 3.4.2. 工作产品

##### 3.4.2.1. 交付的原子软件组件


| Deliverable | Delivered Atomic Software Components |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products |  |  |
| Brief Description | Delivery of a set of AtomicSoftwareComponents including their Implementation. |  |  |
| Description | Complete description of a set of AtomicSoftwareComponents including Implementation (still standalone, not yet mapped to a specific ECU). The source or object code files are referred by the Implementation Description. The Atomic Software Components that make up the delivery may or may not form a composition (in the sense of the VFB). Note that the VFB descriptions of the components, compositions and the used interfaces are part of the deliverable too in order to describe the delivered components completely. However, depending on the use case, these parts could have been predefined and were treated as "readonly" during the component development. The same holds (optionally) for the Internal Behavior(s). In case of RTE generation a mapping set between Application and Implementation Data Types shall be included if Application Data Types are used. A Timing Model is included optionally. The delivery can optionally also contain variants (an Evaluated Variant Set and the related artifacts). Delivered |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Application Header File | 1..* |  |
| Aggregates | Software Component Data Types Header | 1..* |  |
| Aggregates | VFB Atomic Software Component | 1..* |  |
| Aggregates | Alias Name Set | 0..1 | Alias names valid in the context of the delivered components. |
| Aggregates | Evaluated Variant Set | 0..1 |  |
| Aggregates | Partial Flat Map | 0..1 |  |
| Aggregates | Postbuild Variant Set | 0..1 |  |
| Aggregates | Atomic Software Component Implementation | 0..* | If the delivery contains only VFB NvBlock Software Components, no implementation is contained as the code is generated as part of the RTE. |
| Aggregates | Atomic Software Component Object Code | 0..* |  |
| Aggregates | Atomic Software Component Source Code | 0..* |  |
| Aggregates | Component RTE Prebuild Configuration Header | 0..* |  |
| Aggregates | Consistency Needs | 0..* | Correlation between a group of RunnableEntitys and a group of DataPrototypes. |
| Aggregates | Library Object Code | 0..* |  |
| Aggregates | Predefined Variant | 0..* |  |
| Aggregates | Software Component Documentation | 0..* |  |
| Aggregates | Software Component Internal Behavior | 0..* | If the delivery contains only VFB NvBlock Software Components, the Internal Behavior is optional since it is needed only in special cases. |
| Aggregates | Software Component Timing | 0..* |  |
| Aggregates | Software Component to BS WMapping | 0..* |  |
| Aggregates | System Constant Value Set | 0..* |  |
| Aggregates | VFB Composition Component | 0..* | In case the delivered atomic components make up one or more VFB Compositions, the composition description(s) shall be included in the delivery. |
| Deliverable | Delivered Atomic Software Components |  |  |
| Aggregates | VFB Data Type Mapping Set | 0..* |  |
| Aggregates | VFB Interfaces | 0..* |  |
| Aggregates | VFB Modes | 0..* |  |
| Aggregates | VFB Types | 0..* |  |
| Produced by | Develop Application Software | 1..* | Complete description of a set of AtomicSoftware Components including implementation (incl. source or object code files) |
| Consumed by | Configure RTE | 1..* | Required input: • References to all component implementation descriptions on this ECU • SwcInternalBehavior (for example to map the runnables to tasks) which was used in the contract phase of the software components on this ECU |
| Consumed by | Generate RTE | 1..* | Required input: • References to all component implementation descriptions on this ECU • SwcInternalBehavior which was used in the contract phase of the software components on this ECU • (optional) Software Component to BSW Mapping Meth.bindingTime = SystemDesignTime |
| Consumed by | Integrate Software for ECU | 1..* |  |
| Consumed by | Define Alias Names | 0..1 | Needed for definition of alias names in the scope of delivered software components. |
| Consumed by | Create MC Function Model | 0..* | The component model may be used to derive an MC Function Model. |

##### 3.4.2.2. 软件组件内部行为

表3.148：软件组件内部行为（**Software Component Internal Behavior**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Description of the InternalBehavor: It describes the RTE relevant aspects of a component, for example the runnable entities and the events they respond to. | — |
| 描述 | Description of the Internal Behavor. The Internal Behavior of an Atomic Software Component describes the RTE relevant aspects of a component, i.e. the runnable entities and the events they respond to. It is used to generate the RTE but also as input for parts of the basic software generation (AUTOSAR Services). The Internal Behavior (i.e. the XML description) can only be used together with an Atomic Software Component Type to which it is related. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* If the delivery contains only VFB NvBlock Software Components, the Internal Behavior is optional since it is needed only in special cases. |
| 产出者 | Define Atomic Software Component Internal Behavior | 1 |
| 消费者 | Define Software Component Safety Information | 1 |
| 消费者 | Define Software Component Timing | 1 |
| 消费者 | Generate Atomic Software Component Contract Header Files | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Header File in Vendor Mode | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Component Prebuild Data Set | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate Rapid Prototyping Wrapper | 1 |
| 消费者 | Implement Atomic Software Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Map Software Component to BSW | 1 |
| 消费者 | Refine Rapid Prototyping Scenario | 1 |
| 消费者 | Define Consistency Needs | 1..* Runnables the consistency is defined for. |
| 消费者 | Define Rapid Prototyping Scenario | 1..* |
| 消费者 | Select Software Component Implementation | 1..* |
| 消费者 | Generate Local MC Data Support | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Define Partial Flat Map | 0..* Refer to parameter and variables defined in the Internal Behavior of one or more Atomic Software Components. |
| 消费者 | Define VFB NvBlock Software Component | 0..* This input is required to collect the requirements for the NvBlockNeeds from the using application software. |
| 使用的元模型元素 | SwcInternalBehavior 1 | — |

##### 3.4.2.3. 原子软件组件实现

表3.149：原子软件组件实现（**Atomic Software Component Implementation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Description of an implementation for a single Atomic Software Component. | — |
| 描述 | Description of an implementation for a single Atomic Software Component. It is possible to have several different implementations for the same Software Component Internal Behavior, but only one implementation can be mapped to a particular ECU. In general, this XML artifact relates to one particular version of the code. It contains the version information as defined by the vendor. An implementation description may depend on several non-AUTOSAR artifacts, especially its own code files (source or object) but also required libraries, generator tools etc. These dependencies are not described by direct references to files (because this might be ambiguous), but by referring entries in the container catalog of the General Deliverable which contains the implementation artifacts. Such a reference is described via the metamodel element AutosarEngineeringObject (refer to document ID 202 FO_TPS_GenericStructureTemplate for further description). This allows among other things to refer to a particular version of an artifact. For more information on the content of the implmementation description refer to document ID 89 | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* If the delivery contains only VFB NvBlock Software Components, no implementation is contained as the code is generated as part of the RTE. |
| 产出者 | Create Service Component | 1 In order to generate the RTE, one needs to create a kind of dummy Implementation element for the Service Component, however this should not be filled with descriptive elements, e.g. resource consumption, as these are already defined by the Basic Software Module Implementation Description. Meth.bindingTime = SystemDesignTime |
| 产出者 | Implement Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Measure Resources | 0..* Add extensions to the Implementation Description. Meth.bindingTime = PostBuild |
| 输入/输出 | Measure Component Resources | 1 |
| 消费者 | Generate Component Header File in Vendor Mode | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate SWC Memory Mapping Header | 1 MemorySections: MemorySections defined for an Atomic Software Component. Meth.bindingTime = SystemDesignTime |
| 消费者 | Select Software Component Implementation | 1..* |
| 消费者 | Configure Memmap Allocation | 0..* MemorySections: |
| 使用的元模型元素 | Implementation 1 | — |

##### 3.4.2.4. 软件组件文档

表3.150：软件组件文档（**Software Component Documentation**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Documentation dedicated to a Software Component. | — |
| 描述 | Documentation of a dedicated Software Component. This documentation is following the ASAM FSX standard. In this documentation, you will find the SW Feature definition and description which define the physical functionality of the Swc, the SW test description which will contains suggestions and hints for the test of the software functionality of the Swc, the SW calibration notes which will give calibration instructions and hints for a calibration engineer, some maintenance, diagnosis and CARB notes which will bring general information, on the maintenance diagnosis and CARB issues on the Swc. For other description not listed previously, some notes (chapters) are left free for that. This artifact may also contain standalone documentation (meta-class Documentation) not aggregeted by a specific software component. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 输入/输出 | Add Documentation to the Software Component | 1 |
| 使用的元模型元素 | Documentation 1 | — |
| 使用的元模型元素 | SwComponent Documentation 1 | — |

##### 3.4.2.5. 软件组件时序

表3.151：软件组件时序（**Software Component Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Software Component's TimingDescription and TimingConstraints | — |
| 描述 | TimingDescription and TimingConstraints of a software component. A software component can either be of type AtomicSWComponentType or CompositionSWComponentType. In the former case, the SwcTiming allows to describe timing description and constraints for the InternalBehavior of the AtomicSWComponentType. In the latter case, timing descriptions and constraints can be defined for all Atomic Software Components in the CompositionSWComponentType. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Define Software Component Timing | 1 |
| 消费者 | Define System Timing | 0..1 |
| 消费者 | Implement Atomic Software Component | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Measure Component Resources | 0..1 |
| 使用的元模型元素 | SwcTiming 1 | — |

##### 3.4.2.6. 软件组件到 BSW 的映射

表3.152：软件组件到 BSW 的映射（**Software Component to BSW Mapping**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Desribes how to map a software component to basic software elements (required in special cases only). | — |
| 描述 | Maps an SwcInternalBehavior to an BswInternalBehavior. This is required to coordinate the API generation and the scheduling for AUTOSAR Service Components, ECU Abstraction Components and Complex Driver Components by the RTE and the BSW scheduling mechanisms. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Map Software Component to BSW | 1 |
| 产出者 | Create Service Component | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Atomic Software Component Contract Header Files | 0..1 If a Software Component is mapped to a BSW module description, this input is optionally needed already in the contract phase in order to ensure that the generated prototypes for runnables are consistent with the definitions in Software Component and BSW. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate RTE | 0..* This input is explicitly stated because the mapping may be created during ECU integration and thus is not necessarily part of the Delivered Atomic Software Components. Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | SwcBswMapping 1 | — |

##### 3.4.2.7. 部分 Flat Map

表3.153：部分 Flat Map（**Partial Flat Map**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 |  | — |
| 描述 | The Partial Flat Map pre-defines Flat Map entries in the context of delivered software components. This allows the component developer to specify names of data instances for measurement and calibration. It has to be integrated into the System Flat Map. For more information on the Flat Map concept refer to artifact System Flat Map in the system domain. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Delivered Atomic Software Components | 0..1 |
| 产出者 | Define Partial Flat Map | 1 |
| 消费者 | Add Documentation to the Software Component | 0..1 Optional input in order to refer to unique names defined in component or composition context. |
| 消费者 | Generate or Adjust ECU Flat Map | 0..* If Partial Flat Maps were delivered along with software components referring only to ECU internal information, they may be integrated into the ECU Flat Map directly, i.e. without needing the System Flat Map. • The instance refs used in a partial flat map must be taken over and adjusted to the context ECU Extract. • Name conflicts have to be resolved if several partial flat maps are merged. |
| 消费者 | Generate or Adjust System Flat Map | 0..* If Partial Flat Maps were delivered along with software components, they must be integrated into the System Flat Map: • The instance refs used in a partial flat map must be taken over and adjusted to the context of the System or System Extract. • Name conflicts have to be resolved if several partial flat maps are merged. |
| 使用的元模型元素 | FlatMap 1 | — |

##### 3.4.2.8. 应用头文件

表3.154：应用头文件（**Application Header File**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Header generated for an AtomicSoftwareComponentType in the RTE contract phase. | — |
| 描述 | Header generated for an AtomicSoftwareComponentType in the RTE contract phase. It represents the complete source-code interface between the component code and RTE (calls into the RTE as well as prototypes called by the RTE). All communication of the component code with other components is routed through this header. | — |
| 种类 | Source Code | — |
| 聚合于 | Delivered Atomic Software Components | 1..* |
| 产出者 | Generate Atomic Software Component Contract Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement Atomic Software Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Compile ECU Source Code | 1..* Meth.bindingTime = CodeGenerationTime |

##### 3.4.2.9. 软件组件数据类型头文件

表3.155：软件组件数据类型头文件（**Software Component Data Types Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Software Component Data Types Header provided by the RTE in the contract phase. | — |
| 描述 | Software Component Data Types Header provided by the RTE in the contract phase. This includes data types, which were declared as part of the SWC description but not used in any ports or data elements. | — |
| 种类 | Source Code | — |
| 聚合于 | Delivered Atomic Software Components | 1..* |
| 产出者 | Generate Atomic Software Component Contract Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Generate Component Header File in Vendor Mode | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement Atomic Software Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.4.2.10. 组件 RTE 预构建配置头文件

表3.156：组件 RTE 预构建配置头文件（**Component RTE Prebuild Configuration Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Generated header file used to resolve the prebuild variants in the prebuild RTE contract phase for an SWC. | — |
| 描述 | Generated header file used to resolve the prebuild variants of a software component in the prebuild RTE contract phase. Contains macros which resolve the variants when compiled with the module and the generated RTE. | — |
| 种类 | Bound Source Code | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Generate Component Prebuild Data Set | 1 Meth.bindingTime = PreCompileTime |
| 消费者 | Compile Atomic Software Component | 0..1 Meth.bindingTime = PreCompileTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.4.2.11. 原子软件组件源代码

表3.157：原子软件组件源代码（**Atomic Software Component Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Source code implementing an Atomic Software Component Type | — |
| 描述 | Source code implementing an Atomic Software Component Type. In general it is independent from an ECU. | — |
| 种类 | Source Code | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Implement Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Atomic Software Component | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Re-compile Component in ECU context | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.4.2.12. 原子软件组件目标代码

表3.158：原子软件组件目标代码（**Atomic Software Component Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 |  | — |
| 描述 | Object Code of an Atomic Software Component. | — |
| 种类 | Object Code | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Compile Atomic Software Component | 1 The object file should include both code of the SWC and the E2E Protection Wrapper code (if present as an input). Meth.bindingTime = CompileTime |
| 消费者 | Measure Component Resources | 1 |
| 消费者 | Generate ECU Executable | 0..* Meth.bindingTime = CompileTime |

##### 3.4.2.13. 优化的应用头文件

表3.159：优化的应用头文件（**Optimized Application Header File**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | Optimized application header file for a software component. | — |
| 描述 | Application header file for a software component optimized by the RTE in vendor mode. | — |
| 种类 | Source Code | — |
| 产出者 | Generate Component Header File in Vendor Mode | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Re-compile Component in ECU context | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.4.2.14. 优化的软件组件目标代码

表3.160：优化的软件组件目标代码（**Optimized Software Component Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 | The object code of a software component compiled with ECU specific optimizations. | — |
| 描述 | The object code of a software component compiled with ECU specific optimizations. | — |
| 种类 | Object Code | — |
| 产出者 | Re-compile Component in ECU context | 1 Meth.bindingTime = CompileTime |

##### 3.4.2.15. 一致性需求

表3.161：一致性需求（**Consistency Needs**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work | — |
| 简要描述 |  | — |
| 描述 | A ConsistencyNeed describes the correlation between a group of RunnableEntitys and a group of DataPrototypes with the intended purpose to describe the need for • Stable data during the execution of a group of RunnableEntitys. • Coherent data consumption and propagation for a group of DataPrototypes. The information can be defined first time at the design of an Atomic Software Component but can be added as well if Compositions are created. In order to allow incremental development the groups of Runnables and DataPrototypes can be distributed over several artifacts. | — |
| 种类 |  | — |
| 聚合于 | VFB System | 1 Correlation between a group of RunnableEntitys and a group of DataPrototypes. |
| 聚合于 | Delivered Atomic Software Components | 0..* Correlation between a group of RunnableEntitys and a group of DataPrototypes. |
| 输入/输出 | Define Consistency Needs | 1 The description of the correlation between a group of RunnableEntitys and a group of DataPrototypes. In order to allow incremental development and refinement the Consistency Needs artifact is also used as an input. |
| 使用的元模型元素 | ConsistencyNeeds 1 | — |

##### 3.4.2.16. 快速原型包装器头文件

表3.162：快速原型包装器头文件（**Rapid Prototyping Wrapper Header File**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work | — |
| 简要描述 |  | — |
| 描述 | This header replaces the RTE API in order to allow to read and modify inputs and outputs of the original SWC as well as to control execution of the original (and prototype) runnable. | — |
| 种类 | Source Code | — |
| 产出者 | Generate Rapid Prototyping Wrapper | 1 |
| 消费者 | Compile Atomic Software Component | 0..1 |

##### 3.4.2.17. 快速原型包装器源代码

表3.163：快速原型包装器源代码（**Rapid Prototyping Wrapper Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Work Products | — |
| 简要描述 |  | — |
| 描述 | A piece of code that is placed between software components and the RTE in order to provide rapid prototyping functionality. This code allows to encapsulate the SWC to bypass into the rapid prototyping component and may be implemented ad as a complex device driver and/or integration code. | — |
| 种类 | Source Code | — |
| 产出者 | Generate Rapid Prototyping Wrapper | 1 |
| 消费者 | Compile Atomic Software Component | 0..1 |

#### 3.4.3. 工具

##### 3.4.3.1. 组件 API 生成工具

| Tool | Component API Generator Tool |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Component::Guidance |  |  |
| Brief Description | Generates the software component contract header used to connect the software component to the RTE layer. |  |  |
| Description | This guidance represents the so-called contract phase of the RTE generation process. • SWC Contract phase - a limited set of information about a component, principally the AUTOSAR Interface definitions and the internal behavior, is used to create an application header file for a component type. The application header file defines the "contract" between component and RTE. • BSW Contract phase - a similar use case for a BSW module in order to generate the module interlink header files, which are used to interface between the module and the BSW Scheduler. • Additional phases - for SWS and BSW as well - are used to bind pre-build variants in the contract headers of a single Software Component or BSW module. |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Generate Atomic Software Component Contract Header Files | 1 |  |
| Used | Generate BSW Module Prebuild Data Set | 1 |  |
| Used | Generate BSWM Contract Header Files | 1 |  |
| Used | Generate Component Header File in Vendor Mode | 1 |  |
| Used | Generate Component Prebuild Data Set | 1 |  |

### 3.5. 基础软件

本章包含用于开发基础软件模块的工作产品和任务 的定义。相关元模型元素的定义参见 [\[11, CP TPS BSW Module Description Template\]](#ref-11)。

#### 3.5.1. 任务

##### 3.5.1.1. 定义 BSW 类型

表3.164：定义 BSW 类型（**Define BSW Types**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Define data types for usage within the Basic Software. | — |
| 描述 | A data type is typically based on elements standardized by AUTOSAR, therefore BSW Standard Package appears as a mandatory input. | — |
| 执行者 | Basic Software Designer | 1 |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | BSW Standard Package | 0..1 |
| 输入/输出 | BSW Types | 1 |

##### 3.5.1.2. 定义 BSW 入口

表3.165：定义 BSW 入口（**Define BSW Entries**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Define BswEntries (= function signatures) for usage within the Basic Software. | — |
| 描述 |  | — |
| 执行者 | Basic Software Designer | 1 |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | BSW Types | 1 |
| 消费 | BSW Standard Package | 0..1 |
| 产出 | Basic Software Entries | 1 |

##### 3.5.1.3. 定义 BSW 接口

表3.166：定义 BSW 接口（**Define BSW Interfaces**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Define the interfaces for a single BSW Module. | — |
| 描述 | Define the interfaces for a particular BSW Module or BSW cluster as part of the BSW Module Description. This includes an abstraction of the required and provided C-functions, as well as triggers and modes. Note that this task also exists for modules standardized by AUTOSAR, as it may be required to decide on optional or alternative elements and to add allowed project specific extensions. | — |
| 执行者 | Basic Software Designer | 1 |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | BSW Types | 1 |
| 消费 | Basic Software Entries | 1 |
| 消费 | BSW Standard Package | 0..1 |
| 消费 | ECU Resources Description | 0..1 |
| 产出 | Basic Software Module Description | 1 |

##### 3.5.1.4. 定义供应商特定模块定义

表3.167：定义供应商特定模块定义（**Define Vendor Specific Module Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 |  | — |
| 描述 | Define the Vendor Specific Module Definition (=Configuration Parameters). | — |
| 执行者 | Basic Software Designer | 0..1 |
| 执行者 | Basic Software Module Developer | 0..1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 1 |
| 产出 | BSW Module Vendor- Specific Configuration Parameter Definition | 1 |

##### 3.5.1.5. 定义 BSW 行为

表3.168：定义 BSW 行为（**Define BSW Behavior**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Define the BSW Behavior related to a BSW Module Description. | — |
| 描述 | Define the BSW Behavior related to a BSW Module Description. This task is required during BSW module development in order to be able to generate the API to the BSW Scheduler. In addition, local data (variables or parameters) may be defined during this task in order to use the AUTOSAR data type system for module local data and to generate measurement & calibration support. | — |
| 执行者 | Basic Software Designer | 1 |
| 消费 | Basic Software Module Description | 1 |
| 消费 | BSW Standard Package | 0..1 |
| 产出 | Basic Software Module Internal Behavior | 1 |

##### 3.5.1.6. 定义 BSW 模块时序

表3.169：定义 BSW 模块时序（**Define BSW Module Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Define BSWModuleTiming (TimingDescription and TimingConstraints) for the Internal Behavior (BSWModuleEntities) of a BSW module | — |
| 描述 | Define BSWModuleTiming (TimingDescription and TimingConstraints) for the Internal Behavior (BSWModuleEntities) of a BSW module | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | Basic Software Module Internal Behavior | 1 |
| 产出 | Basic Software Module Timing | 1 |

##### 3.5.1.7. 生成 BSW 合同头文件

表3.170：Generate BSWM Contract Header Files（**Generate BSWM Contract Header Files**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Generate Basic Softwaree Module Contract Header Files | — |
| 描述 | Generate the header files needed for a BSW module as part of the so-called "contract phase". These headers will allow to link the module lateron with the RTE (namely the BSW Scheduler). Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | Basic Software Module Description | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Implementation Description | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Internal Behavior | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Standard Package | 0..1 |
| 产出 | Basic Software Interlink Types Header | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Interlink Header | 1 Meth.bindingTime = CodeGenerationTime |
| 使用的工具 | Component API Generator Tool | 1 |

##### 3.5.1.8. 实现 BSW 模块

表3.171：实现 BSW 模块（**Implement a BSW Module**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Implement the source code of a BSW module. | — |
| 描述 | Implement the source code of a BSW module. This task is not described by AUTOSAR completely, but included for completeness of the AUTOSAR use cases. Note that specification of an AUTOSAR standard module imposes several requirements, e.g. the inclusion of certain header files, onto this task. In addition to the code, this task also produces the necessary XML descriptions. Optionally, a build action manifest may be created or modified in order to be used for code generation or further processing of the code. | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | Basic Software Interlink Types Header | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Description | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Interlink Header | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Internal Behavior | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Standard Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | BSW Standard Package | 0..1 |
| 消费 | Basic Software Module Timing | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Resources Description | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | Library Header Files | 0..1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Core Header | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Implementation Description | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Core Source Code | 0..1 The creation of source code is optional, since it might be generated completely in a later step based on the Build Action Manifest. Meth.bindingTime = CodeGenerationTime |
| 产出 | Build Action Manifest | 0..1 |
| 产出 | Custom Transformer | 0..1 |

##### 3.5.1.9. 开发 BSW 模块生成器

表3.172：开发 BSW 模块生成器（**Develop BSW Module Generator**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 |  | — |
| 描述 | Develop a generator for one or more BSW modules. | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | BSW Standard Package | 1 |
| 消费 | BSW Module Vendor- Specific Configuration Parameter Definition | 0..* |
| 产出 | BSW Module Generator | 1 |

##### 3.5.1.10. 创建库

表3.173：创建库（**Create Library**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Create a library to be used within an EcuInstance. | — |
| 描述 | Create a non-standardized library to be used within an EcuInstance. The task is the same for the basic software and application level, but it is considered as a basic software task because no VFB resp. RTE abstraction is used. The output includes source code, header file and XML descriptions of the interfaces and of the implementation. A "dummy" BSW Behavior must be created too in order to be able to link the other two XML artifacts. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | Basic Software Module Developer | 1 |
| 执行者 | ECU Integrator | 1 |
| 消费 | BSW Standard Package | 1 Used for standard types and specifications. |
| 产出 | Basic Software Module Implementation Description | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Internal Behavior | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Library Description | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Library Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Library Object Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.5.1.11. 编译 BSW 核心代码

表3.174：编译 BSW 核心代码（**Compile BSW Core Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Compile the source code of a BSW modue without ECU specific configurations. | — |
| 描述 | Compile the source code of a BSW modue without ECU specific configurations. This task is mainly used to describe the use cases of BSW development for object code delivery. The output will only represent the "core code". During ECU integration, additional generated code may be added per module in response to ECU configuration. Meth.bindingTime = CompileTime | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | BSW RTE Prebuild Configuration Header | 1 Meth.bindingTime = PreCompileTime |
| 消费 | BSW Types | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Interlink Types Header | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Core Header | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Core Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Interlink Header | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Standard Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Build Action Manifest | 0..1 The compilation can optionally be controlled by a Build Action Manifest. |
| 消费 | Library Header Files | 0..1 Meth.bindingTime = CodeGenerationTime |
| 产出 | Basic Software Module Object Code | 1 Meth.bindingTime = CompileTime |
| 使用的工具 | Compiler | 1 |

##### 3.5.1.12. 生成 BSW 模块预构建数据集

表3.175：Generate BSW Module Prebuild Data Set（**Generate BSW Module Prebuild Data Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Tasks | — |
| 简要描述 | Prebuild Data Set Generation Phase for a BSW module: It binds all variations which need to be set after generation of the RTE contract header but before compilation of the module. | — |
| 描述 | Prebuild Data Set Generation Phase for a basic software module: It binds all variations which need to be set after generation of the RTE contract header but before compilation of the module. The variant settings must be defined by the PredefinedVariant given as input. The output is a BSW Module RTE Prebuild Configuration Header which is included by the corresponding BSW Module Interlink Header, thereby resolving the variation points when compiled. Note that link time variants are not allowed here. Meth.bindingTime = PreCompileTime | — |
| 执行者 | Basic Software Module Developer | 1 |
| 消费 | Basic Software Module Description | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Implementation Description | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Internal Behavior | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Predefined Variant | 1 |
| 消费 | System Constant Value Set | 1 |
| 消费 | BSW Standard Package | 0..1 |
| 产出 | BSW RTE Prebuild Configuration Header | 1 Meth.bindingTime = PreCompileTime |
| 使用的工具 | Component API Generator Tool | 1 |

#### 3.5.2. 工作产品

##### 3.5.2.1. BSW 标准包

| Deliverable | BSW Standard Package |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products |  |  |
| Brief Description | Package containing standard artifacts for BSW. |  |  |
| Description | Contains the standard specifications and standardized AUTOSAR blueprints for the artefacts to be used within the AUTOSAR basic software and for the generation of the RTE. This deliverable is released by AUTOSAR and is read only within the methodology. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | AUTOSAR Platform Types and Blueprints | 1 |  |
| Aggregates | AUTOSAR Standard Types and Blueprints | 1 |  |
| Aggregates | AUTOSAR Standardized E CU Configuration Parameter Definition | 1 |  |
| Aggregates | AUTOSAR Software Module Specification | 0..* |  |
| Consumed by | Create Library | 1 | Used for standard types and specifications. |
| Consumed by | Design Basic Software | 1 |  |
| Consumed by | Develop BSW Module | 1 |  |
| Consumed by | Develop BSW Module Generator | 1 |  |
| Consumed by | Develop Basic Software | 1 |  |
| Consumed by | Define BSW Behavior | 0..1 |  |
| Consumed by | Define BSW Entries | 0..1 |  |
| Consumed by | Define BSW Interfaces | 0..1 |  |
| Consumed by | Define BSW Types | 0..1 |  |
| Consumed by | Generate BSW Module Prebuild Data Set | 0..1 |  |
| Consumed by | Generate BSWM Contract Header Files | 0..1 |  |
| Consumed by | Implement a BSW Module | 0..1 |  |

##### 3.5.2.2. BSW 模块包

| Deliverable | BSW Module Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products |  |  |
| Brief Description |  |  |  |
| Description | Generic deliverable representing a bundle of one or more BSW modules. It is used as a basis for extended deliverables. The deliverable aggregates the ARXML definitions on the interface level including vendor specific configuration parameter definition. According to the role of the extended deliverable, these elements maybe blueprints completely or partially. . |  |  |
| Kind | Delivered |  |  |
| Extended By | BSW Design Bundle, BSW Module Delivered Bundle, BSW Module ICS Bundle |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Basic Software Module Description | 1..* |  |
| Aggregates | Basic Software Entries | 0..1 |  |
| Aggregates | Basic Software Module Timing | 0..1 |  |
| Aggregates | BSW Module Vendor- Specific Configuration Parameter Definition | 0..* | The configuration parameter definitions of the modules under test - needed for static check against the standardized configuration parameters. |
| Aggregates | BSW Types | 0..* |  |

##### 3.5.2.3. BSW 设计包

| Deliverable | BSW Design Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products |  |  |
| Brief Description |  |  |  |
| Description | A bundle of one or more BSW modules used in the design phase. It contains only definitions on the interface level. These elements maybe blueprints completely or partially. |  |  |
| Kind | Delivered |  |  |
| Extends | BSW Module Bundle |  |  |
| Relation Type | Related Element | Mult. | Note |
| Produced by | Design Basic Software | 1..* |  |
| Consumed by | Develop BSW Module | 1..* |  |

##### 3.5.2.4. BSW 模块 ICS 包

| Deliverable | BSW Module ICS Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products |  |  |
| Brief Description |  |  |  |
| Description | Deliverable containing the Implementation Conformance Statement (ICS) for one or more BSW modules. |  |  |
| Deliverable | BSW Module ICS Bundle |  |  |
| Kind | Delivered |  |  |
| Extends | BSW Module Bundle |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Basic Software Module Implementation Description | 1 | The administrative elements (e.g. version info) of the Implementation model needed for the conformance test. |
| Aggregates | Basic Software Module Object Code | 1..* |  |
| Aggregates | BSW Module Preconfigured Configuration | 0..* | The predefined configurations implemented by the modules under test. The modules under test are completely configured. |

##### 3.5.2.5. BSW 模块交付包

| Deliverable | BSW Module Delivered Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products |  |  |
| Brief Description |  |  |  |
| Description | Deliverable containing one or more BSW modules delivered for integration (code and ARXML descriptions). It can still contain blueprints for some of the elements which need to be extended during ECU integration. |  |  |
| Kind | Delivered |  |  |
| Extended By | BSW Module Integration Bundle |  |  |
| Extends | BSW Module Bundle |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | Basic Software Module Core Header | 1..* |  |
| Aggregates | Basic Software Module Implementation Description | 1..* |  |
| Aggregates | Basic Software Module Interlink Header | 1..* |  |
| Aggregates | Basic Software Module Internal Behavior | 1..* |  |
| Aggregates | Build Action Manifest | 0..1 | The build action manifest to be used for the delivered basic software. |
| Aggregates | BSW Module Generator | 0..* |  |
| Aggregates | BSW Module Preconfigured Configuration | 0..* |  |
| Aggregates | BSW Module Recommended Configuration | 0..* |  |
| Aggregates | BSW RTE Prebuild Configuration Header | 0..* |  |
| Aggregates | Basic Software Interlink Types Header | 0..* |  |
| Aggregates | Basic Software Module Core Source Code | 0..* |  |
| Aggregates | Basic Software Module Object Code | 0..* |  |
| Produced by | Develop BSW Module | 1 |  |
| Produced by | Develop Basic Software | 1..* |  |
| Consumed by | Define Integration Variant | 1..* |  |
| Consumed by | Generate Base Ecu Configuration | 1..* | Need vendor specific configuration parameters and their recommended or pre-configured values. |
| Consumed by | Generate Updated ECU Configuration | 1..* |  |
| Consumed by | Integrate Software for ECU | 1..* |  |
| Consumed by | Prepare ECU Configuration | 1..* |  |
| Consumed by | Configure Com | 0..1 |  |
| Consumed by | Configure Diagnostics | 0..1 | Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| Consumed by | Configure MCAL | 0..1 |  |
| Consumed by | Configure Mode Management | 0..1 | Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| Deliverable | BSW Module Delivered Bundle |  |  |
| Consumed by | Configure NvM | 0..1 | Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| Consumed by | Configure Watchdog Manager | 0..1 | Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| Consumed by | Create Service Component | 0..1 | Required in order to define a mapping between SWC and BSW. In addition, the Build Action Manifest may be used. |
| Consumed by | Configure ECUC | 0..* |  |
| Consumed by | Configure IO Hardware abstraction | 0..* |  |
| Consumed by | Configure OS | 0..* | OS Resources required by Basic Software. Optional Input: Basic Software Module Timing, e.g. execution order constraints. |
| Consumed by | Configure RTE | 0..* | Input from the BSW Module Description is needed related to Scheduling, Exclusive Areas, Triggers and Modes. Optional Input: Basic Software Module Timing, e.g. execution order constraints. |
|  | Configure Transformer | 0..1 |  |

##### 3.5.2.6. AUTOSAR 软件模块规范

表3.176：AUTOSAR 软件模块规范（**AUTOSAR Software Module Specification**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | The standard sofware module specification. | — |
| 描述 | Specification of a standardized Basic Software Module (SWS). It is published as a textual specification, but can be seen as a Basic Software Design bundle in the methodology, consisting mainly of blueprints. It may be published as ARXML in future releases of AUTOSAR. | — |
| 种类 | Text | — |
| 聚合于 | BSW Standard Package | 0..* |

##### 3.5.2.7. AUTOSAR 标准类型和蓝图

表3.177：AUTOSAR 标准类型和蓝图（**AUTOSAR Standard Types and Blueprints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | AUTOSAR Standard Types and Blueprints | — |
| 描述 | Model elements provided by AUTOSAR are mainly provided as blueprints: MethodologyAndTemplates/AUTOSAR_MOD_GeneralDefinitions.zip contains blueprints for standard implementation data types (in AUTOSAR_MOD_CommonDataTypes_Blueprint.arxml, package /AUTOSAR/Std). The concrete artefacts used in projects need to be derived from these blueprints. See also document id 578 CP_SWS_BSWGeneral and 49 CP_SWS_StandardTypes. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Standard Package | 1 |
| 聚合于 | VFB AUTOSAR Standard Package | 1 |
| 使用的元模型元素 | ImplementationDataType 1 | — |

##### 3.5.2.8. AUTOSAR 平台类型和蓝图

表3.178：AUTOSAR 平台类型和蓝图（**AUTOSAR Platform Types and Blueprints**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | AUTOSAR Platform Types and Blueprints | — |
| 描述 | Model elements provided by AUTOSAR are mainly provided as blueprints: MethodologyAndTemplates/AUTOSAR_MOD_GeneralDefinitions.zip contains • blueprints for base types, implementation data types, computation methods (in AUTOSAR_MOD_ CommonDataTypes_Blueprint.arxml, package /AUTOSAR/Platform), • physical dimensions (in AUTOSAR_MOD_PhysicalDimensions_Blueprint.arxml), • units (in AUTOSAR_MOD_Units_Blueprint.arxml) • and others. The concrete artefacts used in projects need to be derived from these blueprints. See also document id 578 CP_SWS_BSWGeneral and 49 CP_SWS_StandardTypes. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Standard Package | 1 |
| 聚合于 | VFB AUTOSAR Standard Package | 1 |
| 使用的元模型元素 | ImplementationDataType 1 | — |
| 使用的元模型元素 | SwBaseType 1 | — |

##### 3.5.2.9. BSW 模块生成器

表3.179：BSW 模块生成器（**BSW Module Generator**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 |  | — |
| 描述 | A generator that comes as part of one or more delivered BSW modules. It can be put into a framework to let it generate a module's configuration code. | — |
| 种类 | Custom | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 产出者 | Develop BSW Module Generator | 1 |
| 消费者 | Generate BSW Configuration Code | 0..1 This is an input in case a generator framework is used which has to run some module specific generator code. |

##### 3.5.2.10. AUTOSAR 标准化 ECU 配置参数定义

表3.180：AUTOSAR 标准化 ECU 配置参数定义（**AUTOSAR Standardized ECU Configuration Parameter Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Contains all the standardized module definition parameters. | — |
| 描述 | Contains all the standardized module definition parameters. These parameters must be referred by the vendor specific configuration of a specific module. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Standard Package | 1 |
| 消费者 | Define Vendor Specific Module Definition | 1 |
| 消费者 | Configure Com | 0..1 |
| 消费者 | Configure Diagnostics | 0..1 |
| 消费者 | Configure ECUC | 0..1 |
| 消费者 | Configure IO Hardware abstraction | 0..1 |
| 消费者 | Configure MCAL | 0..1 |
| 消费者 | Configure Mode Management | 0..1 |
| 消费者 | Configure NvM | 0..1 |
| 消费者 | Configure OS | 0..1 |
| 使用的元模型元素 | EcucModuleDef 1 | — |
|  | Configure Transformer | 0..1 |

##### 3.5.2.11. BSW 模块预配置

表3.181：BSW 模块预配置（**BSW Module Preconfigured Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Configuration parameter values that are fixed to the object code and cannot be changed without recompilation. | — |
| 描述 | Configuration parameter values that are pre-configured in the delivered code. They cannot be changed during the ECU integration of the code. Pre-configuration is possible for object and source code as well. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 聚合于 | BSW Module ICS Bundle | 0..* The predefined configurations implemented by the modules under test. The modules under test are completely configured. |
| 产出者 | Define Memory Addressing Modes | 1..* MemMapAddressingModeSet: Meth.bindingTime = SystemDesignTime |
| 消费者 | Configure Memmap Allocation | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation and addressing modes. |
| 消费者 | Generate BSW Memory Mapping Header | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate SWC Memory Mapping Header | 1..* MemMapAddressingModeSet: Collection of compiler specific configuration elements for memory allocation. Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | EcucModuleConfiguration Values 1 | — |

##### 3.5.2.12. BSW 模块推荐配置

表3.182：BSW 模块推荐配置（**BSW Module Recommended Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Recommended "default" configuration parameter values. | — |
| 描述 | Set of configuration parameter values, which are recommended by the module vendor as a default, but are not mandatory for the integration. There can be more than one such set in order to allow for variable usage of the module. This artifact does not include values of so-called published parameters. These must always be given as Basic Software Module Preconfigured Configuration. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 使用的元模型元素 | EcucModuleConfiguration Values 1 | — |

##### 3.5.2.13. BSW 模块供应商特定配置参数定义

表3.183：BSW Module Vendor- Specific Configuration Parameter Definition（**BSW Module Vendor- Specific Configuration Parameter Definition**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Vendor specific parameter definition for a module. This defines the format of the parameters, not its values. | — |
| 描述 | Vendor specific parameter definition for a module. This defines the format of the parameters, not its values. In case of a standardized module, it redefines the existing standardized configuration parameter format (ModuleDef). | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | Transformer Design Bundle | 0..1 |
| 聚合于 | BSW Module Bundle | 0..* The configuration parameter definitions of the modules under test - needed for static check against the standardized configuration parameters. |
| 产出者 | Define Vendor Specific Module Definition | 1 |
| 消费者 | Configure RTE | 1 The definitions for the module RTE |
| 消费者 | Develop BSW Module Generator | 0..* |
| 消费者 | Generate BSW Configuration Code | 0..* |
| 使用的元模型元素 | EcucModuleDef 1 | — |

##### 3.5.2.14. BSW 类型

表3.184：BSW 类型（**BSW Types**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Set of data types for usage within the Basic Software. | — |
| 描述 | Set of data types (arxml descriptions) for usage by Basic Software Modules. They will be referred by the Basic Software Module Description | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Bundle | 0..* |
| 输入/输出 | Define BSW Types | 1 |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Define BSW Entries | 1 |
| 消费者 | Define BSW Interfaces | 1 |
| 使用的元模型元素 | AutosarDataType 1 | — |

##### 3.5.2.15. 基础软件入口

表3.185：基础软件入口（**Basic Software Entries**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Set of signatures for calls between BSW modules. | — |
| 描述 | Set of signatures for calls between BSW modules. Defining such a set as a separate artifact allows for a better reuse by several BSW modules.They are decribed in terms of the meta-model element BswModuleEntry which represents a C-function signature and associated properties. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Bundle | 0..1 |
| 产出者 | Define BSW Entries | 1 |
| 消费者 | Define BSW Interfaces | 1 |
| 使用的元模型元素 | BswModuleEntry 1 | — |

##### 3.5.2.16. 基础软件模块描述

表3.186：基础软件模块描述（**Basic Software Module Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Description of a single BSW module or a module cluster in terms of its interfaces, dependencies and module Id. | — |
| 描述 | Description of all interfaces (ingoing and outgoing C-function calls, triggers and modes) and other dependencies of a single BSW module or a BSW module cluster. In addition, this artifacts defines the so-called module Id, which indicates the role of the module within the architecture (only mandatory for standardized modules). Note that the description of the function signatures (so-called BswModuleEntry and their ImplementationDataType can be factored out into separate artifacts BSW Entries and BSW Types in order to improve their reuse. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Bundle | 1..* |
| 产出者 | Define BSW Interfaces | 1 |
| 消费者 | Define BSW Behavior | 1 |
| 消费者 | Generate BSW Module Prebuild Data Set | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate BSWM Contract Header Files | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Implement a BSW Module | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate BSW Memory Mapping Header | 0..1 shortName: The BSW module's shortName is used as the first part of the generated file name, in case the default rule applies. Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | BswModuleDescription 1 | — |

##### 3.5.2.17. 基础软件模块内部行为

表3.187：基础软件模块内部行为（**Basic Software Module Internal Behavior**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Specifies the InternalBehavior of a BSW module or a BSW cluster, especially the scheduling aspect. | — |
| 描述 | Specifies the behavior of a BSW module or a BSW cluster w.r.t. the code entities visible by the BSW Scheduler. It is possible to have several different BswInternalBehaviors referring to the same Bsw ModuleDescription, but only one of them can be integrated on one CPU. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Delivered Bundle | 1..* |
| 产出者 | Create Library | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Define BSW Behavior | 1 |
| 消费者 | Define BSW Module Timing | 1 |
| 消费者 | Generate BSW Module Prebuild Data Set | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate BSWM Contract Header Files | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Implement a BSW Module | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Map Software Component to BSW | 1 |
| 消费者 | Generate Local MC Data Support | 0..1 Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | BswInternalBehavior 1 | — |

##### 3.5.2.18. 基础软件模块实现描述

表3.188：基础软件模块实现描述（**Basic Software Module Implementation Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Contains the implementation specific information of a module. | — |
| 描述 | Contains the implementation specific information of a module in addition to the generic specification given in Basic Software Module Description and Basic Software Module Internal Behavior. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module ICS Bundle | 1 The administrative elements (e.g. version info) of the Implementation model needed for the conformance test. |
| 聚合于 | BSW Module Delivered Bundle | 1..* |
| 产出者 | Create Library | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Implement a BSW Module | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate BSW Memory Mapping Header | 1 DependencyOnArtifact: Can be used to override the default name of the memory mapping header file. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate BSW Memory Mapping Header | 1 MemorySections: MemorySections defined for a BSW module. This input includes optional prefixes for memory sections overriding the default rule. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate BSW Memory Mapping Header | 1 infixes: Optional infixes (denoting instance and vendor ID) to be used within the created header file name. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate BSW Module Prebuild Data Set | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate BSWM Contract Header Files | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Configure Memmap Allocation | 0..* MemorySections: |
| 使用的元模型元素 | BswImplementation 1 | — |

##### 3.5.2.19. 构建动作清单

表3.189：构建动作清单（**Build Action Manifest**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Describes the actions used to build certain artifacts from other artifacts. | — |
| 描述 | Describes the actions used to build certain artifacts from other artifacts (generate, compile, link...). Note: A build action manifest can include the actions for processing of basic software as well as of application software artifacts. The manifest itself is however considered as a product of basic software development. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Delivered Bundle | 0..1 The build action manifest to be used for the delivered basic software. |
| 产出者 | Implement a BSW Module | 0..1 |
| 消费者 | Compile BSW Core Code | 0..1 The compilation can optionally be controlled by a Build Action Manifest. |
| 消费者 | Compile ECU Source Code | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Connect Service Component | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate A2L | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate BSW Configuration Code | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate ECU Executable | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate OS | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate RTE Postbuild Dataset | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费者 | Generate RTE Prebuild Dataset | 0..1 The task may be controlled by a Build Action Manifest. |
| 使用的元模型元素 | BuildActionManifest 1 | — |

##### 3.5.2.20. 基础软件模块时序

表3.190：基础软件模块时序（**Basic Software Module Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | BSW module's TimingDescription and TimingConstraints | — |
| 描述 | TimingDescription and TimingConstraints defined for the Internal Behavior of a BSW module (BSWModuleEntities) | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Bundle | 0..1 |
| 产出者 | Define BSW Module Timing | 1 |
| 消费者 | Define ECU Timing | 0..1 |
| 消费者 | Implement a BSW Module | 0..1 Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | BswModuleTiming 1 | — |

##### 3.5.2.21. 基础软件模块核心头文件

表3.191：基础软件模块核心头文件（**Basic Software Module Core Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | C-header files delivered with a BSW module. | — |
| 描述 | C-header file delivered with a BSW module. It may have to be included by other modules. | — |
| 种类 | Source Code | — |
| 聚合于 | BSW Module Delivered Bundle | 1..* |
| 产出者 | Implement a BSW Module | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Configuration Data | 1 |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Configured BSW | 1 |
| 消费者 | Compile Unconfigured BSW | 1 |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.5.2.22. 基础软件模块核心源代码

表3.192：基础软件模块核心源代码（**Basic Software Module Core Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | The core source code of a module provided by the vendor. | — |
| 描述 | The core source code of a module provided by the vendor. "Core" means, that it does not include addtional source code, which may be generated during the configuration process. | — |
| 种类 | Source Code | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 产出者 | Implement a BSW Module | 0..1 The creation of source code is optional, since it might be generated completely in a later step based on the Build Action Manifest. Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Configured BSW | 1 |
| 消费者 | Compile Unconfigured BSW | 1 |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.5.2.23. 基础软件互连头文件

表3.193：Basic Software Module Interlink Header（**Basic Software Module Interlink Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Generated Header file used to link a BSW module with the BSW Scheduler. | — |
| 描述 | Generated Header file used to link a BSW module with the BSW Scheduler during Contract phase. | — |
| 种类 | Source Code | — |
| 聚合于 | BSW Module Delivered Bundle | 1..* |
| 产出者 | Generate BSWM Contract Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement a BSW Module | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Compile ECU Source Code | 1..* Meth.bindingTime = CodeGenerationTime |

##### 3.5.2.24. 基础软件互连类型头文件

表3.194：基础软件互连类型头文件（**Basic Software Interlink Types Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Generated Header file with data types used to link a BSW module with the BSW Scheduler | — |
| 描述 | Generated Header file with data types used to link a BSW module with the BSW Scheduler. | — |
| 种类 | Source Code | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 产出者 | Generate BSWM Contract Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement a BSW Module | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.5.2.25. BSW RTE 预构建配置头文件

表3.195：BSW RTE 预构建配置头文件（**BSW RTE Prebuild Configuration Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Generated header file used to resolve the prebuild variants in the prebuild RTE contract phase for the BSW. | — |
| 描述 | Generated header file used to resolve the prebuild variants of a basic software module in the prebuild RTE contract phase. Contains macros which resolve the variants when compiled with the module. | — |
| 种类 | Bound Source Code | — |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 产出者 | Generate BSW Module Prebuild Data Set | 1 Meth.bindingTime = PreCompileTime |
| 消费者 | Compile BSW Core Code | 1 Meth.bindingTime = PreCompileTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = PreCompileTime |

##### 3.5.2.26. 基础软件模块目标代码

表3.196：基础软件模块目标代码（**Basic Software Module Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Object code of a BSW module. | — |
| 描述 | Object code of a BSW module. | — |
| 种类 | Object Code | — |
| 聚合于 | BSW Module ICS Bundle | 1..* |
| 聚合于 | BSW Module Delivered Bundle | 0..* |
| 产出者 | Compile BSW Core Code | 1 Meth.bindingTime = CompileTime |
| 产出者 | Compile Configured BSW | 1 |
| 产出者 | Compile Generated BSW | 1 |
| 产出者 | Compile Unconfigured BSW | 1 |
| 消费者 | Link ECU Code after Precompile Configuration | 1..* |
| 消费者 | Link ECU Code during Link Time Configuration | 1..* |
| 消费者 | Generate ECU Executable | 0..* for object code delivery Meth.bindingTime = CompileTime |

##### 3.5.2.27. 库描述

表3.197：库描述（**Library Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | Description of a library in Autosar XML. | — |
| 描述 | Description of a library in Autosar XML. This uses the same template as for describing Basic Software Modules, but with restricted content. Main purpose is to describe the C-interfaces of the library. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Create Library | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement Atomic Software Component | 0..* Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | BswModuleDescription 1 | — |

##### 3.5.2.28. 库头文件

表3.198：库头文件（**Library Header Files**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | These additional headers are typically needed for libraries that a component uses. | — |
| 描述 | These additional headers are typically needed for libraries that a component or a module uses (e.g. a "math-libary"). | — |
| 种类 | Source Code | — |
| 产出者 | Create Library | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile BSW Core Code | 0..1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement a BSW Module | 0..1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile Atomic Software Component | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费者 | Implement Atomic Software Component | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费者 | Re-compile Component in ECU context | 0..* Meth.bindingTime = CodeGenerationTime |

##### 3.5.2.29. 库目标代码

表3.199：库目标代码（**Library Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Bsw::Work products | — |
| 简要描述 | The object code of a lbrary. | — |
| 描述 | The object code of a library, to be linked with other object code during a build of the ECU executable. | — |
| 种类 | Object Code | — |
| 聚合于 | Delivered Atomic Software Components | 0..* |
| 产出者 | Create Library | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate ECU Executable | 0..* for object code delivery Meth.bindingTime = CompileTime |

##### 3.5.2.30. 定制转换器

表3.200：定制转换器（**Custom Transformer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::System::Work products | — |
| 简要描述 | Custom transformation | — |
| 描述 | This is a user defined transformer that is not standardized in AUTOSAR. | — |
| 种类 |  | — |
| 产出者 | Implement a BSW Module | 0..1 |
| 消费者 | Define Transformation Chain | 0..1 |

### 3.6. ECU 集成和配置

本章包含用于在 ECU 上集成和配置 AUTOSAR 软件 的工作产品和任务 的定义。相关元模型元素的定义参见 [\[12, CP TPS ECU Configuration\]](#ref-12)。

#### 3.6.1. 任务

##### 3.6.1.1. 提供 RTE 标定数据集

表3.201：提供 RTE 标定数据集（**Provide RTE Calibration Dataset**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Provide a data set defining initial values for calibration parameters in the RTE code. | — |
| 描述 | Since a model of the "downstream" calibration process of an ECU is not part of the AUTOSAR methodology, the input data are only shown as a General Non AUTOSAR Artifact. The output of this task is a set of calibration values in AUTOSAR format, which can be further processed within AUTOSAR, namely by the RTE generator. The calibration values have to be associated to the corresponding parameter specification via a reference to the ECU Flat Map. | — |
| 执行者 | ECU Integrator | 1 |
| 执行者 | Calibration Engineer | 0..1 |
| 消费 | ECU Flat Map | 1 |
| 消费 | General Non Autosar Artifact | 1..* input from calibration process |
| 产出 | Calibration Parameter Value Set | 1 |

##### 3.6.1.2. 定义集成变体

表3.202：定义集成变体（**Define Integration Variant**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Define a variant for the artifacts integrated on an ECU. | — |
| 描述 | Define a variant for the artifacts integrated on an ECU, this means adding a PredefinedVariant related to the ECU extract and the BSW modules in scope. To do so, this task can make use of existing System Constant Value Set and/or Postbuid Variant Sets or define new ones. Several PredefinedVariants can be combined to one Evaluated Variant Set. It is up to particular process definition to decide, which variants are allowed to be set at integration time. Technically, since this task is part of ECU integration, it can only resolve variation points which have not yet been resolved in the delivered ECU extract or BSW modules. Especially, variation points which have to be bound at system design time, should have been already resolved before. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 |
| 消费 | BSW Module Delivered Bundle | 1..* |
| 输入/输出 | Postbuild Variant Set | 0..* |
| 输入/输出 | System Constant Value Set | 0..* |
| 产出 | Predefined Variant | 1 Meth.bindingTime = SystemDesignTime |
| 产出 | Evaluated Variant Set | 0..1 Meth.bindingTime = SystemDesignTime |

##### 3.6.1.3. 生成基础 ECU 配置

表3.203：Generate Base Ecu Configuration（**Generate Base Ecu Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate an initial set of ECU configuration values based on the delivered ECU extract. | — |
| 描述 | Create the ECU configuration module structure including an initial set of ECU configuration values. This is based on the delivered ECU extract and on the vendor specific configuration parameters and their recommended or pre-configured values provided with the delivered BSW modules. Furthermore the diagnostic extract is used to create the initial configuration for diagnostic related modules, such as DCM and DEM. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 |
| 消费 | BSW Module Delivered Bundle | 1..* Need vendor specific configuration parameters and their recommended or pre-configured values. |
| 消费 | Diagnostic ECU Extract | 0..1 |
| 产出 | ECU Configuration Values | 1 Meth.bindingTime = SystemDesignTime |

##### 3.6.1.4. 生成更新的 ECU 配置

表3.204：生成更新的 ECU 配置（**Generate Updated ECU Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generates the updated ECU configuration. | — |
| 描述 | This task generates the updated ECU configuration based on the initial ECU configuration, the updated ECU Extract and optionally the Diagnostic Extract. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 |
| 消费 | BSW Module Delivered Bundle | 1..* |
| 消费 | Diagnostic ECU Extract | 0..1 |
| 输入/输出 | ECU Configuration Values | 1 The task "Generate Updated ECU Configuration" consumes the initial ECU configuration values and produces the updated ECU configuration values. |

##### 3.6.1.5. 定义 ECU 时序

表3.205：定义 ECU 时序（**Define ECU Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Define ECUTiming (TimingDescription and TimingConstraints) for a concrete ECU taking the ECU configuration and the ECU Software Composition (including their implementation) into account. | — |
| 描述 | Define ECUTiming (TimingDescription and TimingConstraints) for a concrete ECU taking the ECU configuration and the ECU Software Composition (including their implementation) into account. Meth.bindingTime = SystemDesignTime | — |

##### 3.6.1.6. 配置 EcuC

表3.206：Configure ECUC（**Configure ECUC**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 |
| 消费 | ECU Service Connectors | 1..* |
| 消费 | Basic Software Module Timing | 0..1 |
| 消费 | ECU Extract | 0..1 Needed to set up links to the elements of the ECU extract. |
| 消费 | ECU Extract of System Timing | 0..1 |
| 产出 | ECU Timing | 1 Meth.bindingTime = SystemDesignTime |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Set the general ECU configuration values. | — |
| 描述 | Set the general ECU configuration values, the so-called EcuC parameters. These are the configuration parameters which are not related to a particular module, but are relevant for the ECU in general. The EcuC parameters consist of the following parts: • Collection of all Pdu objects flowing through the Com-Stack. • Definition of partitions for the ECU (One partition will be implemented using one OS application). The memory partitions have to be known before doing the OS configuration. • Collection of PredefinedVariant elements which shall be applied when resolving the variability during ECU Configuration. • Collection of mappings between ECU hardware memory segments (defined in ECU Resources Description) and SwAddrMethod elements (defined in VFB Types). The name of each such Ecuc MemoryMappingElement could be used as to predefine the logical memory segment for the linker configuration. Note: The usage of EcucMemoryMappingElement is deprecated in R4.0 rev.2, because the configuration of the "MemMap" module has been added which allows a more fined grained memory mapping than SwAddrmethod. A relatonship to hardware elements from this fine grained mapping is currently not provided. See task definition Configure Memmap Allocation. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..* |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.7. 配置 OS

表3.207：配置 OS（**Configure OS**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the OS by creating the Tasks, events, alarms, etc. | — |
| 描述 | The OS configuration process may be highly iterative between RTE and OS, e.g. RTE needs some OsTasks or OsScheduleTables to map Runnables into them. To finalize a ECU Configuration the OS is the last BSW module to configure. To use multi-core ECUs the EcuC Configuration needs to be provided beforehand to the OS Configuration to map the cores. There cannot be specified a precedence which configuration parameter values should be set first for OsAlarm, OsApplication, Os Counter, OsIsr, OsOs, OsResource, OsScheduleTable, OsSpinlock, OsTask. This is dependent on the development and configuration process. Application + Basic Software requirements and fulfill those with OS artifacts. Mandatory Inputs: • RTE part of the ECU Configuration • EcuC part of the ECU Configuration Outputs: • OS part of the ECU Configuration • RTE part of the ECU Configuration The following steps are needed to perform the task : • Map OS Configuration to Cores only in the case of multiple core ECU. • Define the OSTasks and OSSchedule : Tables based on the events/runnables of the application & bsw components, create the OSTasks that will invoke them. • Map Runnables into OSTasks and OSSchedule Tables : Assign all the runnables to the OSTasks • Steps for "OsAlarm, OsApplication, OsCounter, OsIsr, OsOs, OsResource, OsScheduleTable, Os Spinlock, OsTask." | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | ECU Timing | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..* OS Resources required by Basic Software. Optional Input: Basic Software Module Timing, e.g. execution order constraints. |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.8. 配置 RTE

表3.208：配置 RTE（**Configure RTE**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Describes the steps required to successfully configure the AUTOSAR RTE. | — |
| 描述 | Configure the RTE to correctly interact with AUTOSAR COM and the OS. The specification of the OS objects used by the generated RTE are configured in this task. In addition, configuration includes setting RTE specific options and the handling of measurement and calibration data. Post-build variants which shall be supported by the RTE code must be referenced by the configuration. The following steps are usualy done to configure the RTE : 1. Setup RTE General Configuration 2. Select Software Component Implementations 3. Select BSW Module Implementations 4. Each Runnable needs to be assigned to an Operating System Task in order to be invoked. 5. Map BSW Executables to tasks 6. Resolve Exclusive Areas 7. Select Implicit Communication behavior 8. Select Calibration Support 9. Configure Non Volatile Memory Block Component (only needed if decisions on the configuration have to be taken during ECU Configuration) 10. Select the supported post-build variants Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | BSW Module Vendor- Specific Configuration Parameter Definition | 1 The definitions for the module RTE |
| 消费 | ECU Extract | 1 Elements of the System Description and VFB Description are referred by the RTE configuration. Optional Input: ECU Extract of System Timing, e.g. execution order constraints. |
| 消费 | Delivered Atomic Software Components | 1..* Required input: • References to all component implementation descriptions on this ECU • SwcInternalBehavior (for example to map the runnables to tasks) which was used in the contract phase of the software components on this ECU |
| 消费 | ECU Timing | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..* Input from the BSW Module Description is needed related to Scheduling, Exclusive Areas, Triggers and Modes. Optional Input: Basic Software Module Timing, e.g. execution order constraints. |
| 消费 | Service Component Description | 0..* The Internal Behavior of Service Components contributes to the RTE configuration. |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.9. 配置看门狗管理器

表3.209：配置看门狗管理器（**Configure Watchdog Manager**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Describes the steps required to succesfully configure the Watchdog Manager | — |
| 描述 | Configured Top-Down. Service needs determine what kind of watchdog manager you need. For each service need there is one interface. You can connect several of these interfaces to one watchdog manager Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 Application software requirements for WdgM, especially SwcServiceDependency and ServiceNeeds. |
| 消费 | BSW Module Delivered Bundle | 0..1 Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| 消费 | ECU Timing | 0..1 |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.10. 配置模式管理

表3.210：配置模式管理（**Configure Mode Management**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the Mode Managers in the Basic Software for this ECU. | — |
| 描述 | Configure the Mode Managers in the Basic Software for this ECU. In the methodology library this is modeled as a single task (for simplicity) though in practice it may consist of several single tasks. In general, there are two approaches that are supported by AUTOSAR: • Top-down approach: the software components are available and the mode management can be configured using the data elements, i.e. mode requests, inside a port of a software component. • Bottom-up approach: the software components are not available and the mode management can be configured using a reference to a data element (stating the mode requests) in an interface, that is not yet used by a port of a software component. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..1 Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| 消费 | ECU Extract | 0..1 Application software requirements for NvM, especially SwcServiceDependency and ServiceNeeds. Input in case atomic software components are available. |
| 消费 | ECU System Description | 0..1 Input in case ECU Extract is not available (atomic software components not available) |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.11. 配置 NvM

表3.211：配置 NvM（**Configure NvM**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the NvM stack for this ECU. | — |
| 描述 | Configure the NvM stack for this ECU. In the methodology library this is modeled as a single task (for simplicity) though in practice it may consist of several single tasks. Requirements for the configuration of NvM can be collected • from the upstream information about ServiceDependencies and ServiceNeeds in the ECU Extract and BSW Modules • from existing ECU configuration values • from Service Component Descriptions created for other Services (e.g. DEM) Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 Application software requirements for NvM, especially SwcServiceDependency and ServiceNeeds. |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..1 Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| 消费 | Service Component Description | 0..* The configuration of diagnostics, especially of the DEM, typically leads to the definition of additional data to be stored in NvM. One possibility to handle this is to create ServiceNeeds on the level ServiceComponentType which is then taken into account for the configuration of the NvM. |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.12. 配置诊断

表3.212：配置诊断（**Configure Diagnostics**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the diagnostic modules for this ECU | — |
| 描述 | Configure the diagnostic modules for this ECU. In the methodology library this is modeled as a single task (for simplicity) though in practice it may consist of several single tasks. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 Application software requirements for diagnostics, especially SwcServiceDependency and ServiceNeeds. |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..1 Predefined or recommended configuration values, vendor specific parameters, ServiceNeeds defined by BSW. |
| 输入/输出 | ECU Configuration Values | 1 Configuration Values for DEM, DCM, DLT, FIM. |

##### 3.6.1.13. 创建服务组件

表3.213：创建服务组件（**Create Service Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Create an instances for all required Service Components, configure them, create necessary ports and connectors to the respective application software components. This completes the ECU Software Composition. | — |
| 描述 | Create Service Component The ECU Extract contains all information about which components are mapped to a specific ECU. In a new "flat" Software Composition (meta-class RootSwCompositionPrototype) all other compositions have been removed. This has to be extended by an aggregation of the SwComponent Prototypes which describe the Services required by all application components on the ECU: • For each mapped SwComponentPrototype of type AtomicSwComponentType, the PortPrototypes requiring a particular Service and the asscociated SwcServiceDependency-s and ServiceNeeds are collected. Based on this information, a ServiceSwComponentType and its prototype is created exactly once per service with the corresponding number of PortPrototypes, thus that all service-type PortPrototypes of the Application Components have their PortPrototype counterpart on the ServiceSwComponentType. • RTE generation requires that an InternalBehavior and Implementation is created for each Service SwComponentType. In particular, the port defined argument values required for the usage of some service interfaces are configured, and the required RunnableEntities and RTEEvents are set up. It is also required to define a mapping between elements of the generated SWC and existing or generated elements of the BSW module description. • The evaluation of the input might result in further ServiceNeeds to be added to the generated InternalBehavior - for example a ServiceSwComponentType created for the DEM might include ServiceNeeds for NVRAM blocks. It is assumed, that such interdependencies are incrementally resolved within this task for all involved Service Components such that the outputs are consistent. Note that this is just one possibility to handle the situation - another option is to resolve the interdependencies only within the ECU configuration tasks (Configure Diagnostics, Configure Nv M) without creating additional ServiceNeeds. Depending on the details of the configuration process for the particular module (namely which parts are generated or manually created), the steps described above can be done before, in parallel or after setting up the ECU configuration of the involved BSW modules. Likewise, the information used to create the ServiceSwComponentType(s) can come directly as input from the ECU Extract, or via the ECU Configuration. Therefore both artifacts are shown as optional input. The ECU Configuration is also an output, because a reference to the created SwComponentPrototype(s) must be entered here. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | BSW Module Delivered Bundle | 0..1 Required in order to define a mapping between SWC and BSW. In addition, the Build Action Manifest may be used. |
| 消费 | ECU Configuration Values | 0..1 The creation of Service Component details may depend on ECU configuration values, especially for the DCM. |
| 消费 | ECU Extract | 0..1 Input information about the Service Ports and Service Dependencies of the software components. |
| 消费 | ECU Timing | 0..1 Additional information for fine tuning configuration decisions. |
| 产出 | Atomic Software Component Implementation | 1 In order to generate the RTE, one needs to create a kind of dummy Implementation element for the Service Component, however this should not be filled with descriptive elements, e.g. resource consumption, as these are already defined by the Basic Software Module Implementation Description. Meth.bindingTime = SystemDesignTime |
| 产出 | ECU Configuration Values | 1 Enter links to the created SwComponentPrototypes. Meth.bindingTime = SystemDesignTime |
| 产出 | Service Component Description | 1 Meth.bindingTime = SystemDesignTime |
| 产出 | Software Component to BS WMapping | 0..1 Meth.bindingTime = SystemDesignTime |

##### 3.6.1.14. 连接服务组件


表3.214：连接服务组件（**Connect Service Component**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 |  | — |
| 描述 | In order to connect the "isService"-ports of the application components to a particular ServiceSw ComponentType, AssemblyConnectorPrototypes are generated. The ECU Extract with its RootSwCompositionPrototype, extended by the Service Components and their connectors, finally serves as input for generating the RTE. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 Find the ports on the application side to be connected to the Service Component. |
| 消费 | Service Component Description | 1 Required in order to define the connector links to the ports on the BSW side. |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 产出 | ECU Service Connectors | 1..* Meth.bindingTime = SystemDesignTime |

##### 3.6.1.15. 配置 COM

表3.215：Configure Com（**Configure Com**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the COM stack modules within an ECU | — |
| 描述 | The ECU Extract of the System Configuration contains the major part of information that is needed to configure the COM Stack modules. Many parameter values of the ECU configuration can be derived from the ECU extract.The missing ECU specific configuration parameters that can not be derived from the System Description need to be set in this phase, e.g. Vendor-Specific Configuration Parameters. The following steps will be needed to perform the task : 1. Derive configuration parameter values from ECU extract : The System Template Specification describes rules on how the individual ECU configuration parameters shall be derived from the Upstream Templates (SWC Template, System Template, ECU Resource Template). This rules shall be followed. 2. Derive global PDUs from ECU extract : A global PDU has to be configured for each I-PDU flow and is added to the PDU collection of the module EcuC. Derived from the ECU Extract all PDUs that traverse through the COM Stack have to be created. 3. Create PDU References from the BSW Module PDUs to the global PDUs in the module EcuC:As soon as these global PDUs are created the references from the local module PDUs to the appropriate global PDUs need to be configured. 4. Set Missing and Vendor-Specific Parameter Values:Missing and Vendor-Specific Parameter Values need to be set 5. Set BSW Module specific PDU handle IDs:The last step is the assignment of the actual values for the Handle IDs. This can be achieved by an automatic tool which might be run directly before the generation of the module. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Extract | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..1 |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.16. 配置 IO 硬件抽象

表3.216：Configure IO Hardware abstraction（**Configure IO Hardware abstraction**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure I/O Hardware Abstraction | — |
| 描述 | Configure the I/O Hardware Abstraction modules. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..* |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.17. 配置 MCAL

表3.217：配置 MCAL（**Configure MCAL**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Configure the Microcontroller Abstraction Layer for this ECU. | — |
| 描述 | Configure the Microcontroller Abstraction Layer for this ECU. Meth.bindingTime = SystemDesignTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
| 消费 | BSW Module Delivered Bundle | 0..1 |
| 输入/输出 | ECU Configuration Values | 1 |

##### 3.6.1.18. 配置转换器

表3.218：配置转换器（**Configure Transformer**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 |  | — |
| 描述 | Configure the Transformer modules for this ECU. | — |
| 执行者 | ECU Integrator | 1 |
| 输入/输出 | ECU Configuration Values | 1 |
|  | ECU Extract | 1 |
|  | AUTOSAR Standardized E CU Configuration Parameter Definition | 0..1 |
|  | BSW Module Delivered Bundle | 0..1 |

##### 3.6.1.19. 生成 BSW 配置代码和模型扩展

表3.219：生成 BSW 配置代码（**Generate BSW Configuration Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Generate source code which implements configuration data for link- or compile-time configuration. | — |
| 描述 | A generator reads the relevant parameters from the ECU Configuration Description and creates a separate code file that implements the specified configuration. This task is used for link-time configuration, i.e. the configuration code can be produced at link-time of the core code or for compile-time configuration, if the configuration code cannot be put into a header file (e.g. for tables), even if the core code and the configuration code shall be compiled at the same time. A header file may be produced in addition, to declare the data. Furthermore the generator may produce extensions of the BSW module description artifacts as a result of configuration parameter values which are set at integration time. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 |
| 消费 | BSW Module Generator | 0..1 This is an input in case a generator framework is used which has to run some module specific generator code. |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | BSW Module Vendor- Specific Configuration Parameter Definition | 0..* |
| 产出 | BSW Module Configuration Data Source Code | 1 |
| 产出 | BSW Module Configuration Header File | 1 |
| 产出 | BSW Module Behavior Extension | 0..1 |
| 产出 | BSW Module Implementation Extension | 0..1 |
| 产出 | BSW Module Interface Extension | 0..1 |
| 使用的工具 | BSW Generator Framework | 1 |

##### 3.6.1.20. 生成本地 MC 数据支持

表3.220：生成本地 MC 数据支持（**Generate Local MC Data Support**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate Local MC Support Data | — |
| 描述 | Generate the support data needed for measurement and calibration of those parameters and variables (roles constantMemory and staticMemory), which are owned locally by the code of a module or component (in contrast to those, which are owned by the RTE). The declaration of local variables/parameters is read from the Internal Behavior of either a BSW module or an Atomic Software Component, therefore these can be considered as alternative inputs.The ECU Flat Map is needed as input in order to resolve possible name conflicts. This task can be combined with RTE generation for practical reasons, but it is considered as an independent task. Note that calibration data that need software emulation support by the RTE cannot be handled by this task; they need to be processed by the task Generate RTE. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Flat Map | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Module Behavior Extension | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | Basic Software Module Internal Behavior | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component Internal Behavior | 0..1 Meth.bindingTime = SystemDesignTime |
| 产出 | Local Measurement and Calibration Support Data | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.1.21. 创建 MC 功能模型

表3.221：创建 MC 功能模型（**Create MC Function Model**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Define a model of McFunctions. | — |
| 描述 | Create (manually or by generator) a functional model of measurement and calibration data on an ECU. Such a model may be derived from the logical structure of software components, ports etc. but the rules for this transformation are not standardized. This task may be performed before the RTE code is generated. Then the model will be based on the data defined in the ECU Flat Map. The task may also be performed at the same time as or after the generation of Measurement and Calibration Support Data. In this case it is possible (but not mandatory) to base the model on these support data only. | — |
| 执行者 | Calibration Engineer | 0..1 |
| 执行者 | ECU Integrator | 0..1 |
| 消费 | ECU Extract | 0..1 The ECU Flat Map can be used to define references to variables and parameters which are later visible in A2L. Furthermore, the ECU Extract can be used to find the relevant software components. |
| 消费 | RTE Measurement and Calibration Support Data | 0..1 Used if the MC Function Model shall refer to McData Instances allocated by the RTE. |
| 消费 | Delivered Atomic Software Components | 0..* The component model may be used to derive an MC Function Model. |
| 消费 | Local Measurement and Calibration Support Data | 0..* Used if the MC Function Model shall refer to McData Instances allocated by BSW modules without RTE support. |
| 产出 | MC Function Model | 1 |

##### 3.6.1.22. 生成 RTE

表3.222：生成 RTE（**Generate RTE**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate the RTE and several further artifacts. | — |
| 描述 | Generate the RTE and several further artifacts from the input XML descriptions in the scope of a given ECU: • RTE Core Source Code • BSW Scheduler Code • RTE Implementation Description • RTE Measurement and Calibration Support Data In an optional mode, this task can also write into the ECU configuration, especially for the configuration of the OS. This mode is used to pre-configure parts of the ECU configuration. It shall support the integrator in setting up the configuration in an iterative way. In the so-called strict mode, the ECU configuration is not changed but assumed to be complete. This mode shall be used before the final build. A PredefinedVariant in the input data (referred in the EcuC configuration, see task Configure EcuC) can be used to bind variation points at code generation time. For variation points with latest binding time "code generation time" this is mandatory. Unbound variation points can still be present in the generated code. Meth.bindingTime = CodeGenerationTime Related Element Mult. Note | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Extract | 1 Find the VFB description of all Atomic Software Components on this ECU and the relevant parts of the system description. The ECU Flat Map is also an input. Meth.bindingTime = SystemDesignTime |
| 消费 | Delivered Atomic Software Components | 1..* Required input: • References to all component implementation descriptions on this ECU • SwcInternalBehavior which was used in the contract phase of the software components on this ECU • (optional) Software Component to BSW Mapping Meth.bindingTime = SystemDesignTime |
| 消费 | Calibration Parameter Value Set | 0..1 Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Module Integration Bundle | 0..* Input for BSW scheduling, BSW mode and trigger declaration, BSW exclusive areas, BSW calibration parameters that need RTE support (for software emulation). Optionally, a Build Action Manifest maybe be used to control the generator steps. Meth.bindingTime = SystemDesignTime |
| 消费 | ECU Service Connectors | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | Service Component Description | 0..* Meth.bindingTime = SystemDesignTime |
| 消费 | Software Component to BS WMapping | 0..* This input is explicitly stated because the mapping may be created during ECU integration and thus is not necessarily part of the Delivered Atomic Software Components. Meth.bindingTime = SystemDesignTime |
| 产出 | BSW Scheduler Code | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Implementation Description | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | ECU Configuration Values | 0..1 Optional output for the configuration of the OS. Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Measurement and Calibration Support Data | 0..1 Meth.bindingTime = CodeGenerationTime |
| 使用的工具 | RTE Generator | 1 |

##### 3.6.1.23. 生成调度器

表3.223：生成调度器（**Generate Scheduler**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate the BSW Scheduler | — |
| 描述 | Optional task of the RTE generator which only produces the code of the BSW Scheduler and related artifacts. Meth.bindingTime = CodeGenerationTime | — |
| 执行者 | ECU Integrator | 1 |

##### 3.6.1.24. 生成 OS

表3.224：生成 OS（**Generate OS**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate the OS Generated Code files | — |
| 描述 | Generate the OS Generated Code files using the OS configuration values from the ECU Configuration . Meth.bindingTime = CodeGenerationTime | — |
| 消费 | ECU Configuration Values | 1 Configuration values for the BSW Scheduler (subset of RTE configuration). Meth.bindingTime = SystemDesignTime |
| 消费 | BSW Module Integration Bundle | 1..* Input for BSW scheduling, BSW mode and trigger declaration, BSW exclusive areas, BSW calibration parameters that need support for software emulation. Optionally, a Build Action Manifest maybe be used to control the generator steps. Meth.bindingTime = SystemDesignTime |
| 产出 | BSW Scheduler Code | 1 Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Implementation Description | 0..1 Creates a subset of the RTE implementation description that contains only the description of data owned by the BSW Scheduler. Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Measurement and Calibration Support Data | 0..1 Creates a subset of the measurement & calibration support data related only to the data owned by the BSW Scheduler. Meth.bindingTime = CodeGenerationTime |
| 使用的工具 | RTE Generator | 1 |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 Meth.bindingTime = SystemDesignTime |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 产出 | OS Generated Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.1.25. 生成 RTE 预构建数据集

表3.225：生成 RTE 预构建数据集（**Generate RTE Prebuild Dataset**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Prebuild Data Set Generation Phase for the RTE: It binds all variations which are later than code generation time | — |
| 描述 | Prebuild Data Set Generation Phase for the RTE: It binds all variations which are later than code generation time but before build time. The output is a configuration header which is used for the build. The actually supported variant are defined by the PredefinedVariant referred in the EcuC configuration (see task Configure EcuC). Meth.bindingTime = PreCompileTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 find the Predefiined Variant to be used Meth.bindingTime = CodeGenerationTime |
| 消费 | ECU Extract | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Predefined Variant | 1 |
| 消费 | System Constant Value Set | 1 |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | Postbuild Variant Set | 0..1 |
| 消费 | Service Component Description | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | RTE Prebuild Configuration Header | 1 Meth.bindingTime = PreCompileTime |
| 使用的工具 | RTE Generator | 1 |

##### 3.6.1.26. 编译 ECU 源代码

表3.226：编译 ECU 源代码（**Compile ECU Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Compile Source Code for an ECU | — |
| 描述 | Compile all the source code required for ECU integration, i.e. all source code except the code which is delivered as object code. Meth.bindingTime = CompileTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | BSW Scheduler Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | OS Generated Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | RTE Source Code | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Standard Header Files | 1 Meth.bindingTime = CodeGenerationTime |
| 消费 | Application Header File | 1..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Interlink Header | 1..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | RTE Prebuild Configuration Header | 0..1 Meth.bindingTime = PreCompileTime |
| 消费 | Atomic Software Component Source Code | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | BSW Module Configuration Data Source Code | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | BSW Module Configuration Header File | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | BSW RTE Prebuild Configuration Header | 0..* Meth.bindingTime = PreCompileTime |
| 消费 | Basic Software Interlink Types Header | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Core Header | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Basic Software Module Core Source Code | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Component RTE Prebuild Configuration Header | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Library Header Files | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Optimized Application Header File | 0..* Meth.bindingTime = CodeGenerationTime |
| 消费 | Software Component Data Types Header | 0..* Meth.bindingTime = CodeGenerationTime |
| 产出 | ECU Object Code | 1..* Meth.bindingTime = CompileTime |
| 使用的工具 | Compiler | 1 |

##### 3.6.1.27. 生成 ECU 可执行文件

表3.227：生成 ECU 可执行文件（**Generate ECU Executable**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate the executable code of the ECU out of the object files and linker configuration. | — |
| 描述 | The steps to generate the code for an ECU resemble today's development practice. However, it is important to note that this activity is more than a simple linker step. Information from the ECU Configuration Description might be used to generate specially configured executable software. The ECU Configuration Description is needed as input to the Generate Executable activity, because it contains the information which BSW modules and SWC implementations are used to create the executable and further information about the memory mapping. The output of this activity is the ECU Executable and the Map of Executable (which is typically the log file from linking the ECU Executable). The detailed input and output formats of this task are not standardized by AUTOSAR, therefore this task is only included for informative purposes. Note that ECU Configuration is shown as an input to get the overall picture, however in practice more specific artifacts (e.g. linker settings, make file etc.) will have to be generated out of the ECU configuration before the actual software build can be started. Especially, the information about the mapping of the physical memory sections to the memory section used in the software, which is described in the so-called EcuC parameter values, is needed in order to generate the linker settings. Meth.bindingTime = LinkTime | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Object Code | 1..* from generated or delivered source code Meth.bindingTime = CompileTime |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | ECU Configuration Values | 0..1 may be used to set up build environment Meth.bindingTime = CompileTime |
| 消费 | ECU Resources Description | 0..1 may be used to set up build environment Meth.bindingTime = CompileTime |
| 消费 | Atomic Software Component Object Code | 0..* Meth.bindingTime = CompileTime |
| 消费 | Basic Software Module Object Code | 0..* for object code delivery Meth.bindingTime = CompileTime |
| 消费 | Library Object Code | 0..* for object code delivery Meth.bindingTime = CompileTime |
| 产出 | ECU Executable | 1 Meth.bindingTime = LinkTime |
| 产出 | Map of the ECU Executable | 1 Meth.bindingTime = LinkTime |
| 使用的工具 | Linker | 1 |
| 前驱 | Encapsulate SW-C | 1 |
| 前驱 | Generate BSW and RTE | 1 |

##### 3.6.1.28. 生成 RTE 后构建数据集


表3.228：生成 RTE 后构建数据集（**Generate RTE Postbuild Dataset**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Postbuild Data Set Generation Phase for the RTE: It binds all variations which are for postbuild time. | — |
| 描述 | Data Set Generation Phase for the RTE: It binds all variations which are for postbuild time. The output is a data set which can be used to build an image separately from the main code. The supported post-build variants are defined by the PredefinedVariants referred in the post-build section of the RTE configuration. At runtime, only one of those variants can be active. This selection is done via the initialization structure for the BSW Scheduler. The actual value for this iniialization structure used for runtime initialization is defined by the configuration of the ECU State Manager. Meth.bindingTime = PostBuild | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Configuration Values | 1 Meth.bindingTime = LinkTime |
| 消费 | ECU Extract | 1 Meth.bindingTime = LinkTime |
| 消费 | Postbuild Variant Set | 1 |
| 消费 | Predefined Variant | 1 |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | Service Component Description | 0..* Meth.bindingTime = LinkTime |
| 产出 | RTE Postbuild Variants Dataset | 1 Meth.bindingTime = PostBuild |
| 使用的工具 | RTE Generator | 1 |

##### 3.6.1.29. 生成 A2L

表3.229：生成 A2L（**Generate A2L**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Generate the A2L File for an ECU. | — |
| 描述 | The A2L File created by this task is the final representation of the data given by RTE Measurement and Calibration Support Data and Local Measurement and Calibration Support Data. The main purpose of this task is to replace all symbolic information on data location found in these input data by actual addresses. Optionally, it replaces identifiers by alias names given in Alias Name Set(s). Finally is completes the A2L file with configuration from ECU driver software (MC Driver Support Data) and configuration not determined by AUTOSAR artifacts (MC Additional Configuration). This task is not part of AUTOSAR, it is only included for completeness of the use cases. The Map of the ECU Executable (linker map file) is shown as input in order to illustrate the principle use case only. Note that one needs additional information, like the .ELF or .COFF file, to resolve addresses of elements of composite C-variables. | — |
| 执行者 | Calibration Engineer | 1 |
| 消费 | Map of the ECU Executable | 1 |
| 消费 | RTE Measurement and Calibration Support Data | 1 |
| 消费 | Build Action Manifest | 0..1 The task may be controlled by a Build Action Manifest. |
| 消费 | ECU Flat Map | 0..1 The ECU Flat Map is needed in case the A2L generator has to process an MC Function Model that relates to data in the ECU Flat Map. |
| 消费 | MC Additional Config | 0..1 |
| 消费 | MC Function Model | 0..1 This input is needed if the keyword FUNCTION shall be supported in the generated A2L. |
| 消费 | Alias Name Set | 0..* |
| 消费 | Local Measurement and Calibration Support Data | 0..* |
| 消费 | MC Driver Support Data | 0..* |
| 产出 | A2L File | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.1.30. 测量资源

表3.230：测量资源（**Measure Resources**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 | Measure the resource consumption and update the implementation section of the Application SWC and BSW Module Descriptions. | — |
| 描述 | Measure the resource consumption and update the implementation section of the Application SWC and BSW Module Descriptions. | — |
| 执行者 | ECU Integrator | 1 |
| 消费 | ECU Executable | 1 |
| 消费 | ECU Resources Description | 0..1 |
| 消费 | Map of the ECU Executable | 0..1 |
| 产出 | Atomic Software Component Implementation | 0..* Add extensions to the Implementation Description. Meth.bindingTime = PostBuild |
| 产出 | BSW Module Implementation Extension | 0..* Meth.bindingTime = PostBuild |

##### 3.6.1.31. 细化快速原型场景

表3.231：细化快速原型场景（**Refine Rapid Prototyping Scenario**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Tasks | — |
| 简要描述 |  | — |
| 描述 | Add missing ECU specific information in the Rapid Prototyping Scenario, e.g. missing RptHooks or hook implementation decisions. | — |
| 执行者 | Rapid Prototyping Engineer | 1 |
| 消费 | Software Component Internal Behavior | 1 |
| 输入/输出 | ECU Extract of Rapid Prototyping Scenario | 1 |
| 前驱 | Generate ECU Extract | 1 |

#### 3.6.2. 工作产品

##### 3.6.2.1. BSW 模块集成包

| Deliverable | BSW Module Integration Bundle |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products |  |  |
| Brief Description |  |  |  |
| Description | Contains the BSW artifacts for one or more BSW modules completed during integration. |  |  |
| Kind | Delivered |  |  |
| Extends | BSW Module Delivered Bundle |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | BSW Module Behavior Extension | 0..* |  |
| Aggregates | BSW Module Implementation Extension | 0..* |  |
| Aggregates | BSW Module Interface Extension | 0..* |  |
| Aggregates | Local Measurement and Calibration Support Data | 0..* |  |
| Consumed by | Generate Scheduler | 1..* | Input for BSW scheduling, BSW mode and trigger declaration, BSW exclusive areas, BSW calibration parameters that need support for software emulation. Optionally, a Build Action Manifest maybe be used to control the generator steps. Meth.bindingTime = SystemDesignTime |
| Deliverable | BSW Module Integration Bundle |  |  |
| Consumed by | Generate RTE | 0..* | Input for BSW scheduling, BSW mode and trigger declaration, BSW exclusive areas, BSW calibration parameters that need RTE support (for software emulation). Optionally, a Build Action Manifest maybe be used to control the generator steps. Meth.bindingTime = SystemDesignTime |

##### 3.6.2.2. 交付的 ECU 软件

| Deliverable | ECU Software Delivered |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products |  |  |
| Brief Description | All the work products that form the deliverable of an ECUInstance. |  |  |
| Description | All the work products that form the deliverable of an ECUInstance software build. ECU in this context means ECUInstance. One electronic control unit can consist of several ECUInstances (for example if it consists of several processors). In such a case, one "ECU Software Delivered" will be needed for each ECUInstance. Note that the detailed format for all parts of this deliverable is not defined by AUTOSAR. |  |  |
| Kind | Delivered |  |  |
| Relation Type | Related Element | Mult. | Note |
| Aggregates | ECU Executable | 1..* |  |
| Aggregates | A2L File | 0..* |  |
| Aggregates | BSW Module Configuration Data Loadable to ECU Memory | 0..* |  |
| Produced by | Integrate Software for ECU | 1 |  |

##### 3.6.2.3. 服务组件描述

表3.232：服务组件描述（**Service Component Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Describes the RTE relevant part of an AUTOSAR Service on a given ECU in form of a Servcie ComponentType with all its ports and an internal behavior. | — |
| 描述 | Describes the RTE relevant part of an AUTOSAR Service on a given ECU in form of a Service ComponentType with all its ports and an internal behavior. This artifact must be generated during the ECU configuration process, latest before the RTE is generated. It depends on the needs of the software components for this AUTOSAR Service. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Create Service Component | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Connect Service Component | 1 Required in order to define the connector links to the ports on the BSW side. |
| 消费者 | Configure NvM | 0..* The configuration of diagnostics, especially of the DEM, typically leads to the definition of additional data to be stored in NvM. One possibility to handle this is to create ServiceNeeds on the level ServiceComponentType which is then taken into account for the configuration of the NvM. |
| 消费者 | Configure RTE | 0..* The Internal Behavior of Service Components contributes to the RTE configuration. |
| 消费者 | Generate RTE | 0..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate RTE Postbuild Dataset | 0..* Meth.bindingTime = LinkTime |
| 消费者 | Generate RTE Prebuild Dataset | 0..* Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | ServiceSwComponentType 1 | — |
| 使用的元模型元素 | SwcInternalBehavior 1 | — |

##### 3.6.2.4. ECU 服务连接器

表3.233：ECU 服务连接器（**ECU Service Connectors**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | The conectors to the Service Components which complete the complete Software Composition predefined in the ECU extract. | — |
| 描述 | The assembly connectors to the Service Components which complete the Software Composition predefined in the ECU extract. These connectores are added during ECU integration as a separate artifact to the already defined composition of Atomic Software Components. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Connect Service Component | 1..* Meth.bindingTime = SystemDesignTime |
| 消费者 | Define ECU Timing | 1..* |
| 消费者 | Generate RTE | 0..* Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | AssemblySwConnector 1 | — |

##### 3.6.2.5. ECU 时序

表3.234：ECU 时序（**ECU Timing**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | TimingDescription and TimingConstraints for a concrete ECU | — |
| 描述 | TimingDescription and TimingConstraints defined for a concrete ECU taking the ECU configuration and the ECU Software Composition (including their implementation) into account. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Define ECU Timing | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Configure OS | 0..1 |
| 消费者 | Configure RTE | 0..1 |
| 消费者 | Configure Watchdog Manager | 0..1 |
| 消费者 | Create Service Component | 0..1 Additional information for fine tuning configuration decisions. |
| 使用的元模型元素 | EcuTiming 1 | — |

##### 3.6.2.6. BSW 模块接口扩展

表3.235：BSW 模块接口扩展（**BSW Module Interface Extension**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 |  | — |
| 描述 | Additions to the BSW Module on the interface level during integration. It is used for example to add Basic Software Module Entries in response to the ECU configuration, for example callback declarations. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Integration Bundle | 0..* |
| 产出者 | Generate BSW Configuration Code | 0..1 |
| 使用的元模型元素 | BswModuleDescription 1 | — |
| 使用的元模型元素 | BswModuleEntry 1 | — |

##### 3.6.2.7. BSW 模块行为扩展

表3.236：BSW 模块行为扩展（**BSW Module Behavior Extension**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 |  | — |
| 描述 | Additions to the BSW Module on the behavior level during integration. It can for example be used to add local data declaration (constantMemory, staticMemory, perInstanceMemory) for calibration purposes in response to configuration parameters. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Integration Bundle | 0..* |
| 产出者 | Generate BSW Configuration Code | 0..1 |
| 消费者 | Generate Local MC Data Support | 0..1 Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | BswInternalBehavior 1 | — |

##### 3.6.2.8. BSW 模块实现扩展

表3.237：BSW 模块实现扩展（**BSW Module Implementation Extension**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 |  | — |
| 描述 | Additions to the BSW Module on the implementation level during integration. It is used for example to add information on resource consumption. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Integration Bundle | 0..* |
| 产出者 | Generate BSW Configuration Code | 0..1 |
| 产出者 | Measure Resources | 0..* Meth.bindingTime = PostBuild |
| 使用的元模型元素 | BswImplementation 1 | — |

##### 3.6.2.9. ECU 配置值

表3.238：ECU 配置值（**ECU Configuration Values**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | The collection of all configuration values for an ECU. | — |
| 描述 | First of all, the ECU Configuration Values contain a link to the System element which comes with the ECU Extract thus it can be used as a root element for integration on this ECU. Furtheron, it contains a collection of all configuration values for an ECU, which is gradually filled. Starting with the root element EcucValueCollection it contains the actual configuration settings Ecuc ModuleConfigurationValues for each module including the RTE. Note that due to their strong interrelation, these parts are not considered as separate artifacts in the use cases for ECU integration. A special set of configuration values is the so-called EcuC-configuration: It contains the configuration values which are relevant for the whole ECU. Tools that interpret the configuration values need to know the underlying parameter definition. Therefore, in addition to the configuration values, each EcucValueCollection contains a link and the version of the parameter definition to which it adheres. This parameter definition is either part of the AUTOSAR Standardized ECU Configuration Parameter Definition or, in case of vendor specific extensions, is given by the artifact Basic Software Module Vendor-Specific Configuration Parameter Definition. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Configure Memmap Allocation | 1 MemMapAllocation: Meth.bindingTime = SystemDesignTime |
| 产出者 | Create Service Component | 1 Enter links to the created SwComponentPrototypes. Meth.bindingTime = SystemDesignTime |
| 产出者 | Generate Base Ecu Configuration | 1 Meth.bindingTime = SystemDesignTime |
| 产出者 | Prepare ECU Configuration | 1 |
| 产出者 | Generate RTE | 0..1 Optional output for the configuration of the OS. Meth.bindingTime = CodeGenerationTime |
| 输入/输出 | Configure BSW and RTE | 1 |
| 输入/输出 | Configure Com | 1 |
| 输入/输出 | Configure Diagnostics | 1 Configuration Values for DEM, DCM, DLT, FIM. |
| 输入/输出 | Configure ECUC | 1 |
| 输入/输出 | Configure IO Hardware abstraction | 1 |
| 输入/输出 | Configure MCAL | 1 |
| 输入/输出 | Configure Mode Management | 1 |
| 输入/输出 | Configure NvM | 1 |
| 输入/输出 | Configure OS | 1 |
| 输入/输出 | Configure RTE | 1 |
| 输入/输出 | Configure Transformer | 1 |
| 输入/输出 | Configure Watchdog Manager | 1 |
| 输入/输出 | Generate Updated ECU Configuration | 1 The task "Generate Updated ECU Configuration" consumes the initial ECU configuration values and produces the updated ECU configuration values. |
| 消费者 | Define ECU Timing | 1 |
| 消费者 | Generate BSW Configuration Code | 1 |
| 消费者 | Generate BSW Memory Mapping Header | 1 MemMapAllocation: Mapping of the abstract sections (SwAddressMethods for generic mapping resp. Memory Section Elements for specific mapping) to the compiler specific MemMapAddressingModes. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate BSW Postbuild Configuration Code | 1 |
| 消费者 | Generate BSW Precompile Configuration Header | 1 |
| 消费者 | Generate BSW Source Code | 1 |
| 消费者 | Generate BSW and RTE | 1 |
| 消费者 | Generate OS | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate RTE | 1 Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate RTE Postbuild Dataset | 1 Meth.bindingTime = LinkTime |
| 消费者 | Generate RTE Prebuild Dataset | 1 find the Predefiined Variant to be used Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate SWC Memory Mapping Header | 1 MemMapAllocation: Mapipng of the abstract sections (SwAddressMethods for generic mapping resp. Memory Section Elements for specific mapping) to the compiler specific MemMapAddressingModes. Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate Scheduler | 1 Configuration values for the BSW Scheduler (subset of RTE configuration). Meth.bindingTime = SystemDesignTime |
| 消费者 | Create Service Component | 0..1 The creation of Service Component details may depend on ECU configuration values, especially for the DCM. |
| 消费者 | Generate BSW Memory Mapping Header | 0..1 moduleDescription: List of used BSW modules (Ecuc ValueCollection.ecucValue.moduleDescription) Meth.bindingTime = SystemDesignTime |
| 消费者 | Generate ECU Executable | 0..1 may be used to set up build environment Meth.bindingTime = CompileTime |
| 消费者 | Generate SWC Memory Mapping Header | 0..1 RteImplementationRef: Existence of SWCs could be identified by usage of the RTE ECU Configuration "Rte SwComponentType.RteImplementationRef" Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | EcucModuleConfiguration Values 1 | — |
| 使用的元模型元素 | EcucValueCollection 1 | — |

##### 3.6.2.10. RTE 实现描述

表3.239：RTE 实现描述（**RTE Implementation Description**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Implementation Description for the RTE, generated by the RTE generator. | — |
| 描述 | Implementation Description for the RTE, generated by the RTE generator. Uses the format of Bsw Implementation. This artifact is required to provide information for other generators and the build process, namely memory section. It aggregates also the support data for measurement and calibration, which is considered as a separate artifact. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Generate RTE | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Generate Scheduler | 0..1 Creates a subset of the RTE implementation description that contains only the description of data owned by the BSW Scheduler. Meth.bindingTime = CodeGenerationTime |
| 使用的元模型元素 | BswImplementation 1 | — |

##### 3.6.2.11. RTE 预构建配置头文件

表3.240：RTE 预构建配置头文件（**RTE Prebuild Configuration Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | RTE Prebuild Configuration Header File. It defines all variants for the RTE code which have to be bound later than code generation time but before build time. | — |
| 描述 | RTE Prebuild Configuration Header File. It defines the setting of all variants for the RTE code (via macro code) which have to be bound later than code generation time but before build time. | — |
| 种类 | Bound Source Code | — |
| 产出者 | Generate RTE Prebuild Dataset | 1 Meth.bindingTime = PreCompileTime |
| 消费者 | Compile ECU Source Code | 0..1 Meth.bindingTime = PreCompileTime |

##### 3.6.2.12. 标定参数值集合

表3.241：标定参数值集合（**Calibration Parameter Value Set**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Calibration Parameter Value Setting | — |
| 描述 | A set of calibration parameter values used to initialize the memory objects which implement calibration parameters. The values are specific for the software component instances in ECU scope. They will override any initial values defined for those parameters within the ECU Extract. The parameter values can be defined as ApplicationDataTypes or as ImplementationDataTypes which has several use cases. These two use cases are supported by the RTE generation phase: • Parameter values defined as ImplementationDataTypes can be used as instance specific initialization for calibration parameters within components as soon as the respective ImplementationDataTypes are available (which must be the case for RTE generation anyhow). • Parameter values defined as ApplicationDataTypes can be used as instance specific initialization for calibration parameters which are only defined with ApplicationDataTypes. The next case is not modelled within AUTOSAR in detail: • Parameter values defined as ApplicationDataTypes can be used to exchange initial values with the component vendor not publishing the transformation algorithm between ApplicationDataTypes and ImplementationDataTypes | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Provide RTE Calibration Dataset | 1 |
| 消费者 | Generate RTE | 0..1 Meth.bindingTime = SystemDesignTime |
| 使用的元模型元素 | CalibrationParameterValue Set 1 | — |

##### 3.6.2.13. MC 功能模型

表3.242：MC 功能模型（**MC Function Model**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | A functional model to be used for A2L generation. | — |
| 描述 | As set of nested McFunction elements to be used as input to generate A2L. Its purpose is to • assign calibration parameters to a logical function • assign measurement variables to a logical function • structure functions hierarchically It shall support the generation of the FUNCTION keyword and related elements defined in ASAM MCD-2 MC. An MC Function Model refers to the data descriptions in other AUTOSAR XML artifacts either via entries in the ECU Flat Map or via McDataInstances being part of Measurement and Calibration Support Data. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Create MC Function Model | 1 |
| 消费者 | Generate A2L | 0..1 This input is needed if the keyword FUNCTION shall be supported in the generated A2L. |
| 使用的元模型元素 | McFunction 1 | — |

##### 3.6.2.14. 本地测量和标定支持数据

表3.243：本地测量和标定支持数据（**Local Measurement and Calibration Support Data**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Generated artifact, which supports the later generation of "A2L"-files for measurement and calibration data which are owned locally by a component or module. | — |
| 描述 | Generated artifact which is used as an input for the later generation of "A2L"-files for measurement and calibration. It relates the measurment and calibration data listed in the ECU FlatMap to the C-variables used locally within a component or module (this is relevant only valid for those parameters and variables, which are not implemented by the RTE) . In addition, it contains all configuration data which are relevant for the A2L generator (e.g. the access method to calibration data whithin a Complex Driver). This XML-artifact is linked via a (splitable) aggregation to the Implementation Description of the component or module, but it is considered as a separate artifact. | — |
| 种类 | AUTOSAR XML | — |
| 聚合于 | BSW Module Integration Bundle | 0..* |
| 产出者 | Generate Local MC Data Support | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Create MC Function Model | 0..* Used if the MC Function Model shall refer to McData Instances allocated by BSW modules without RTE support. |
| 消费者 | Generate A2L | 0..* |
| 使用的元模型元素 | McSupportData 1 | — |

##### 3.6.2.15. RTE 测量和标定支持数据

表3.244：RTE 测量和标定支持数据（**RTE Measurement and Calibration Support Data**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | RTE generator output, which supports the later generation of "A2L"-files for the measurement and calibration data which are owned by the RTE. | — |
| 种类 | AUTOSAR XML | — |
| 产出者 | Generate RTE | 0..1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Generate Scheduler | 0..1 Creates a subset of the measurement & calibration support data related only to the data owned by the BSW Scheduler. Meth.bindingTime = CodeGenerationTime |
| 消费者 | Generate A2L | 1 |
| 消费者 | Create MC Function Model | 0..1 Used if the MC Function Model shall refer to McData Instances allocated by the RTE. |
| 使用的元模型元素 | McSupportData 1 | — |

##### 3.6.2.16. RTE 源代码

表3.245：RTE 源代码（**RTE Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Source code implementiing the RTE on a CPU. | — |
| 描述 | Source code implementing the RTE on a CPU. The output of an RTE generator can consist of both generated code and configuration for "library" code that may be supplied as either object code or source code. Both configured and generated code reference standard definitions that are defined in one of two standardized header files: The RTE Header File and the Lifecycle Header File. These header files are not explicitly shown in the methodology, as in all tasks they appear with the RTE source code. For details refer to document ID 84 CP_SWS_RTE. Apart from this, the file structure is not standardized, and therefore represented as one single artifact in the methodology. In general, the RTE code can be partitioned in several files. The partitioning depends on the RTE vendor's software design and generation strategy. Nevertheless it shall be possible to clearly identify code and header files which are part of the RTE module. | — |
| 种类 | Source Code | — |
| 产出者 | Generate BSW and RTE | 1 |
| 产出者 | Generate RTE | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.2.17. BSW 调度器代码

表3.246：BSW 调度器代码（**BSW Scheduler Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Generated Code implementing the BSW Scheduler. | — |
| 描述 | Generated Code implementing the BSW Scheduler. It can be source or macro code. | — |
| 种类 | Source Code | — |
| 产出者 | Generate RTE | 1 Meth.bindingTime = CodeGenerationTime |
| 产出者 | Generate Scheduler | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.2.18. OS 生成的代码

表3.247：OS 生成的代码（**OS Generated Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | OS configuration generated code | — |
| 描述 | OS configuration generated code. OS configuration code are composed of header and C files. These will be compiled with the source code in the build process (see Compile Source Code). | — |
| 种类 | Source Code | — |
| 产出者 | Generate OS | 1 Meth.bindingTime = CodeGenerationTime |
| 消费者 | Compile ECU Source Code | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.2.19. RTE 后构建变体数据集

表3.248：RTE 后构建变体数据集（**RTE Postbuild Variants Dataset**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Generated code used to resolve postbuild variants in the RTE. | — |
| 描述 | Generated code used to resolve postbuild variants in the RTE. It consists of a c-file and a header file: • The RTE generator must generate a Rte_PBCfg.c file containing the declarations and initializations of one or more RTE post build variants. Only one of these variants can be active at runtime. • The RTE generator shall generate in the Rte_PBCfg.h file the SchM_ConfigType type declaration of the predefined post build variants data structure. This header file must be used by other RTE modules to resolve their runtime variabilities. | — |
| 种类 | Bound Source Code | — |
| 产出者 | Generate RTE Postbuild Dataset | 1 Meth.bindingTime = PostBuild |

##### 3.6.2.20. ECU 目标代码

表3.249：ECU 目标代码（**ECU Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 |  | — |
| 描述 | Object code file produced by compilation during ECU integration. To be distinguished from code files which are already delivered as object code for integration (see Basic Software Module Object Code or Atomic Software Component Object Code). | — |
| 种类 | Object Code | — |
| 产出者 | Compile ECU Source Code | 1..* Meth.bindingTime = CompileTime |
| 消费者 | Generate ECU Executable | 1..* from generated or delivered source code Meth.bindingTime = CompileTime |
| 消费者 | Link ECU Code during Link Time Configuration | 1..* |

##### 3.6.2.21. ECU 可执行文件

表3.250：ECU 可执行文件（**ECU Executable**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | The executable image containing all the fully integrated software ready to download to an ECU. | — |
| 描述 | The executable image containing all the fully integrated software ready to download to an ECU. This work product and its format is not defined by AUTOSAR, it is only included for completeness of the use cases. | — |
| 种类 | Executable | — |
| 聚合于 | ECU Software Delivered | 1..* |
| 产出者 | Generate ECU Executable | 1 Meth.bindingTime = LinkTime |
| 产出者 | Link ECU Code after Precompile Configuration | 1 |
| 产出者 | Link ECU Code during Link Time Configuration | 1 |
| 消费者 | Measure Resources | 1 |

##### 3.6.2.22. ECU 可执行文件的映射

表3.251：ECU 可执行文件的映射（**Map of the ECU Executable**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Linker map file of the excecutable. | — |
| 描述 | Linker map file of the excecutable. This work product and its format is not defined by AUTOSAR, it is only included for completeness of the use cases. | — |
| 种类 | Text | — |
| 产出者 | Generate ECU Executable | 1 Meth.bindingTime = LinkTime |
| 消费者 | Generate A2L | 1 |
| 消费者 | Measure Resources | 0..1 |

##### 3.6.2.23. A2L 文件

表3.252：A2L 文件（**A2L File**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Input file for measurment and calibration tools. | — |
| 描述 | Input file for measurement and calibration tools related to one ECU. This format is not in the scope of AUTOSAR, it is defined by the ASAM organization. The work product is only included for completeness of the use cases. | — |
| 种类 | Text | — |
| 聚合于 | ECU Software Delivered | 0..* |
| 产出者 | Generate A2L | 1 Meth.bindingTime = CodeGenerationTime |

##### 3.6.2.24. MC 驱动支持数据

表3.253：MC 驱动支持数据（**MC Driver Support Data**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | Support data describing the specific access of a driver (e.g. XCP) for exchange of data for measurement and calibration. | — |
| 描述 | Support data describing the specific access method of a driver (e.g. XCP) in order to exchange data for measurement and calibration. These are the so-called IF-DATA needed in the A2L files. This artifact shall be generated by a driver( e.g. XCP) specific generator out of its ECU configuration. This format is not defined by AUTOSAR. The work product is only included for completeness of the use cases. | — |
| 种类 | Custom | — |
| 消费者 | Generate A2L | 0..* |

##### 3.6.2.25. MC 附加配置

表3.254：MC 附加配置（**MC Additional Config**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Work Products | — |
| 简要描述 | External configuration data nedded to generate the A2L file. | — |
| 描述 | Additional configuration data needed to generate the A2L file. This format is not defined by AUTOSAR. The work product is only included for completeness of the use cases. | — |
| 种类 | Custom | — |
| 消费者 | Generate A2L | 0..1 |

#### 3.6.3. 工具

##### 3.6.3.1. RTE 生成器

| Tool | RTE Generator |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Guidance |  |  |
| Brief Description |  |  |  |
| Description | RTE Generator used for several tasks during ECU integration. |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Generate RTE | 1 |  |
| Used | Generate RTE Postbuild Dataset | 1 |  |
| Used | Generate RTE Prebuild Dataset | 1 |  |
| Used | Generate Scheduler | 1 |  |

##### 3.6.3.2. BSW 生成器框架

| Tool | BSW Generator Framework |  |

| Package | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::Guidance |  |  |
| Brief Description |  |  |  |
| Description | Framework that uses BSW generators that are being delivered as part of individual modules. |  |  |
| Kind |  |  |  |
| Relation Type | Related Element | Mult. | Note |
| Used | Generate BSW Configuration Code | 1 |  |

#### 3.6.4. ECU 配置类

##### 3.6.4.1. 任务

###### 3.6.4.1.1. 编译未配置的 BSW

表3.255：Compile Unconfigured BSW（**Compile Unconfigured BSW**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Compile unconfigured BSW to get a BSW Module Object Code. | — |
| 描述 | Compile Unconfigured BSW is the usual step to compile files without any configuration data when no configuration is needed. This can be use either in the pre-compile, link or post-build time. | — |
| 消费 | Basic Software Module Core Header | 1 |
| 消费 | Basic Software Module Core Source Code | 1 |
| 产出 | Basic Software Module Object Code | 1 |
| 使用的工具 | Compiler | 1 |

###### 3.6.4.1.2. 编译已配置的 BSW


表3.256：Compile Configured BSW（**Compile Configured BSW**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Compile Configured BSW to get a BSW Module Object Code | — |
| 描述 | Compile Configured BSW to get a Basic Software Module Object Code used in the link steps. This Configured BSW is representing C files that have already included all needed configured data. This is done in the pre-compile time. | — |
| 消费 | BSW Module Configuration Header File | 1 |
| 消费 | Basic Software Module Core Header | 1 |
| 消费 | Basic Software Module Core Source Code | 1 |
| 产出 | Basic Software Module Object Code | 1 |
| 使用的工具 | Compiler | 1 |

###### 3.6.4.1.3. 编译 BSW 配置数据

表3.257：编译 BSW 配置数据（**Compile BSW Configuration Data**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Compile BSW Configuration Data during link time | — |
| 描述 | Compile BSW Configuration Data during link-time- or post-build configuration to get the Basic Software Module Configuration Data Object Code used in the link steps. | — |
| 消费 | BSW Module Configuration Data Source Code | 1 |
| 消费 | BSW Module Configuration Header File | 1 |
| 消费 | Basic Software Module Core Header | 1 |
| 产出 | BSW Module Configuration Data Object Code | 1 |
| 使用的工具 | Compiler | 1 |

###### 3.6.4.1.4. 编译生成的 BSW

表3.258：编译生成的 BSW（**Compile Generated BSW**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Compile generated BSW in the pre-compile time: | — |
| 描述 | Compile generated BSW in the pre-compile time: this generated BSW has been generated with a BSW Configuration generator which generates the complete configuration-specific code. | — |
| 消费 | BSW Module Completely Generated Source Code | 1 |
| 消费 | BSW Module Configuration Header File | 1 |
| 产出 | Basic Software Module Object Code | 1 |
| 使用的工具 | Compiler | 1 |

###### 3.6.4.1.5. 生成 BSW 预编译配置头文件

表3.259：生成 BSW 预编译配置头文件（**Generate BSW Precompile Configuration Header**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Generate BSW Precompile Configuration Header | — |
| 描述 | Generate BSW Pre-compile Configuration Header. The header is used for definition or declaration (in case source code is needed) of the pre-compile configuration data code. | — |
| 消费 | ECU Configuration Values | 1 |
| 产出 | BSW Module Configuration Header File | 1 |

###### 3.6.4.1.6. 生成 BSW 源代码


表3.260：生成 BSW 源代码（**Generate BSW Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Generate the source code of a module completely from its precompile configuration. | — |
| 描述 | Generate the source code of a BSW module completely from its pre-compile configuration. A header file may be produced in addition, if required. | — |
| 消费 | ECU Configuration Values | 1 |
| 产出 | BSW Module Completely Generated Source Code | 1 |
| 产出 | BSW Module Configuration Header File | 1 |

###### 3.6.4.1.7. 生成 BSW 配置代码

另见 生成 BSW 配置代码。

###### 3.6.4.1.8. 生成 BSW 后构建配置代码

表3.261：生成 BSW 后构建配置代码（**Generate BSW Postbuild Configuration Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Generate the code for data structures that can be used for postbuild configuration. | — |
| 描述 | Generate the source code and associated header for data structures that can be used for postbuild configuration. | — |
| 消费 | ECU Configuration Values | 1 |
| 产出 | BSW Module Configuration Data Source Code | 1 |
| 产出 | BSW Module Configuration Header File | 1 |

###### 3.6.4.1.9. 在预编译配置后链接 ECU

表3.262：Link ECU Code after Precompile Configuration（**Link ECU Code after Precompile Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Link the ECU code in the pre-compile time Configuration Class | — |
| 描述 | Link the different BSW modules object code in the pre-compile Configuration Class. All parameters values for configurable elements have been already fixed and are effective after compilation time. | — |
| 消费 | Basic Software Module Object Code | 1..* |
| 产出 | ECU Executable | 1 |
| 使用的工具 | Linker | 1 |

###### 3.6.4.1.10. 在链接期配置期间链接 ECU 代码

表3.263：Link ECU Code during Link Time Configuration（**Link ECU Code during Link Time Configuration**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Link ECU Code during Link Time | — |
| 描述 | Link ECU Code during Link Time | — |
| 消费 | BSW Module Configuration Data Object Code | 1..* |
| 消费 | Basic Software Module Object Code | 1..* |
| 消费 | ECU Object Code | 1..* |
| 产出 | ECU Executable | 1 |
| 使用的工具 | Linker | 1 |

###### 3.6.4.1.11. 在后构建期链接 ECU 代码

表3.264：Link ECU Code during Post-Build Time（**Link ECU Code during Post-Build Time**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Tasks | — |
| 简要描述 | Link ECU Code during post-build time loadable . | — |
| 描述 | Link ECU Code during post-build time. The objects used for this link are coming from configuration data file that contain all configured parameters. The result of the link is a hex file that will be loadable in the ECU memory. | — |
| 消费 | BSW Module Configuration Data Object Code | 1..* |
| 产出 | BSW Module Configuration Data Loadable to ECU Memory | 1 |
| 使用的工具 | Linker | 1 |

##### 3.6.4.2. 工作产品

###### 3.6.4.2.1. BSW 模块配置头文件

表3.265：BSW 模块配置头文件（**BSW Module Configuration Header File**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Work | — |
| 简要描述 | C-header file generated from the configuration data of a BSW module. | — |
| 描述 | C-header file generated from the configuration data of a BSW module, defining the data (only possible for pre-compile configuration) or containing additional declarations (needed by generated configuration code only). | — |
| 种类 | Bound Source Code | — |
| 产出者 | Generate BSW Configuration Code | 1 |
| 产出者 | Generate BSW Postbuild Configuration Code | 1 |
| 产出者 | Generate BSW Precompile Configuration Header | 1 |
| 产出者 | Generate BSW Source Code | 1 |
| 产出者 | Generate BSW and RTE | 1 |
| 消费者 | Compile BSW Configuration Data | 1 |
| 消费者 | Compile Configured BSW | 1 |
| 消费者 | Compile Generated BSW | 1 |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

###### 3.6.4.2.2. BSW 模块完全生成的源代码

表3.266：BSW 模块完全生成的源代码（**BSW Module Completely Generated Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Work Products | — |
| 简要描述 | Generated BSW source code implementing the complete module after inclusion of pre-compilation configuration data. | — |
| 描述 | Generated BSW source code implementing the complete module after inclusion of pre-compilation configuration data. In this case, no core code is delivered by the module vendor. | — |
| 种类 | Source Code | — |
| 产出者 | Generate BSW Source Code | 1 |
| 消费者 | Compile Generated BSW | 1 |

###### 3.6.4.2.3. BSW 模块配置数据源代码

表3.267：BSW 模块配置数据源代码（**BSW Module Configuration Data Source Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Work Products | — |
| 简要描述 | BSW source code generated from configuration data, implementing only the data. | — |
| 描述 | BSW source code generated from configuration data, implementing only the data. | — |
| 种类 | Bound Source Code | — |
| 产出者 | Generate BSW Configuration Code | 1 |
| 产出者 | Generate BSW Postbuild Configuration Code | 1 |
| 产出者 | Generate BSW and RTE | 1 |
| 消费者 | Compile BSW Configuration Data | 1 |
| 消费者 | Compile ECU Source Code | 0..* Meth.bindingTime = CodeGenerationTime |

###### 3.6.4.2.4. BSW 模块配置数据目标代码

表3.268：BSW 模块配置数据目标代码（**BSW Module Configuration Data Object Code**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Work Products | — |
| 简要描述 | Generated data for link-time or postbuild configuration of a BSW module. | — |
| 描述 | Generated & compiled configuration data for link-time or postbuild configuration of a BSW module. | — |
| 种类 | Object Code | — |
| 产出者 | Compile BSW Configuration Data | 1 |
| 消费者 | Link ECU Code during Link Time Configuration | 1..* |
| 消费者 | Link ECU Code during Post-Build Time | 1..* |

###### 3.6.4.2.5. 可加载到 ECU 内存的 BSW 模块配置数据

表3.269：可加载到 ECU 内存的 BSW 模块配置数据（**BSW Module Configuration Data Loadable to ECU Memory**）

| 属性 | 值 | 多重性 |
| --- | --- | --- |
| 包 | AUTOSAR Root::M2::Methodology::Methodology Library::Ecu::ECU Config Classes::Work Products | — |
| 简要描述 | Generated loadable configuration data for post-build configuration of a BSW module. | — |
| 描述 | Generated loadable configuration data for post-build configuration of a BSW module. | — |
| 种类 | Configuration Data Set | — |
| 聚合于 | ECU Software Delivered | 0..* |
| 产出者 | Link ECU Code during Post-Build Time | 1 |

## A. 本文档提及的类表（**Mentioned Class Tables**）

为完整起见，本章收录一组类表，表示本文档上下文中提及、但不直接属于描述特定元模型语义范围的元类。属性级备注（Note 列）保留英文原文（量大，待批量门评审决定是否全译）。

表A.1：ARElement（**ARElement**）

| 包 | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage |
| 说明 | An element that can be defined stand-alone, i.e. without being part of another element (except for packages of course). |
| 基类 | ARObject , CollectableElement , Identifiable , MultilanguageReferrable , PackageableElement , Referrable |
| 子类 | AclObjectSet, AclOperation, AclPermission, AclRole, AliasNameSet, ApplicabilityInfoSet, Application Partition, AutosarDataType , BaseType , BlueprintMappingSet, BswEntryRelationshipSet, BswModule Description, BswModuleEntry, BuildActionManifest, CalibrationParameterValueSet, ClientIdDefinitionSet, ClientServerInterfaceToBswModuleEntryBlueprintMapping, Collection, CompuMethod, Consistency NeedsBlueprintSet, ConstantSpecification, ConstantSpecificationMappingSet, CpSoftwareCluster, Cp SoftwareClusterBinaryManifestDescriptor, CpSoftwareClusterMappingSet, CpSoftwareClusterResource Pool, CryptoEllipticCurveProps, CryptoServiceCertificate, CryptoServiceKey, CryptoServicePrimitive, CryptoServiceQueue, CryptoSignatureScheme, DataConstr, DataExchangePoint, DataTransformation Set, DataTypeMappingSet, DdsCpConfig, DiagnosticCommonElement , DiagnosticConnection, DiagnosticContributionSet, DltContext, DltEcu, Documentation, E2EProfileCompatibilityProps, Ecuc DefinitionCollection, EcucDestinationUriDefSet, EcucModuleConfigurationValues, EcucModuleDef, Ecuc ValueCollection, EndToEndProtectionSet, EthIpProps, EthTcpIpIcmpProps, EthTcpIpProps, Evaluated VariantSet, FMFeature, FMFeatureMap, FMFeatureModel, FMFeatureSelectionSet, FirewallRule, Flat Map, GeneralPurposeConnection, HwCategory, HwElement, HwType, IEEE1722TpConnection , IPSec ConfigProps, IPv6ExtHeaderFilterSet, IdsCommonElement , IdsDesign, Implementation , ImpositionTime DefinitionGroup, InterpolationRoutineMappingSet, J1939ControllerApplication, KeywordSet, LifeCycle InfoSet, LifeCycleStateDefinitionGroup, LogAndTraceMessageCollectionSet, MacSecGlobalKayProps, MacSecParticipantSet, McFunction, McGroup, ModeDeclarationGroup, ModeDeclarationMappingSet, Os TaskProxy, PhysicalDimension, PhysicalDimensionMappingSet, PortInterface , PortInterfaceMappingSet, PortPrototypeBlueprint, PostBuildVariantCriterion, PostBuildVariantCriterionValueSet, PredefinedVariant, RapidPrototypingScenario, SdgDef, SignalServiceTranslationPropsSet, SomeipSdClientEventGroup TimingConfig, SomeipSdClientServiceInstanceConfig, SomeipSdServerEventGroupTimingConfig, SomeipSdServerServiceInstanceConfig, SwAddrMethod, SwAxisType, SwComponentMapping Constraints, SwComponentType , SwRecordLayout, SwSystemconst, SwSystemconstantValueSet, Swc BswMapping, System, SystemSignal, SystemSignalGroup, TDCpSoftwareClusterMappingSet, Tcp OptionFilterSet, TimingExtension , TlsConnectionGroup, TlvDataIdDefinitionSet, TransformationProps |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage |
| 说明 | AUTOSAR package, allowing to create top level packages to structure the contained ARElements. ARPackages are open sets. This means that in a file based description system multiple files can be used to partially describe the contents of a package. This is an extended version of MSR's SW-SYSTEM. |
| 基类 | ARObject , AtpBlueprint , AtpBlueprintable , CollectableElement , Identifiable , MultilanguageReferrable Referrable |
| 聚合于 | ARPackage.arPackage, AUTOSAR.arPackage |
| 包 | M2::AUTOSARTemplates::CommonStructure::FlatMap |
| 说明 | This meta-class represents a set of AliasNames. The AliasNameSet can for example be an input to the A2L-Generator. Tags: atp.recommendedPackage=AliasNameSets |
| 基类 | ARElement , ARObject , AtpBlueprint , AtpBlueprintable , CollectableElement , Identifiable , Multilanguage Referrable , PackageableElement , Referrable |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::Components |
| 说明 | An atomic software component is atomic in the sense that it cannot be further decomposed and distributed across multiple ECUs. |
| 基类 | ARElement , ARObject , AtpBlueprint , AtpBlueprintable , AtpClassifier , AtpType , CollectableElement , Identifiable , MultilanguageReferrable , PackageableElement , Referrable , SwComponentType |
| 子类 | ApplicationSwComponentType, ComplexDeviceDriverSwComponentType, EcuAbstractionSwComponent Type, NvBlockSwComponentType, SensorActuatorSwComponentType, ServiceProxySwComponent Type, ServiceSwComponentType |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::GenericStructure::VariantHandling |
| 说明 | This class represents a condition which is computed based on system constants according to the specified expression. The expected result is considered as boolean value. The result of the expression is interpreted as a condition. • "0" represents "false"; • a value other than zero is considered "true" |
| 基类 | ARObject , FormulaExpression , SwSystemconstDependentFormula |
| 聚合于 | VariationPoint.swSyscond, VariationPointProxy.conditionAccess |
| 包 | M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology |
| 说明 | ECUInstances are used to define the ECUs used in the topology. The type of the ECU is defined by reference to an ECU specified with the ECU resource description. Tags: atp.recommendedPackage=EcuInstances |
| 基类 | ARObject , CollectableElement , FibexElement , Identifiable , MultilanguageReferrable , Packageable Element , Referrable |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::GenericStructure::VariantHandling |
| 说明 | This meta class represents the ability to express if a set of ARElements is able to support one or more particular variants. In other words, for a given set of evaluatedElements this meta class represents a table of evaluated variants, where each PredefinedVariant represents one column. In this column each descendant sw SystemconstantValue resp. postbuildVariantCriterionValue represents one entry. In a graphical representation each swSystemconstantValueSet / postBuildVariantCriterionValueSet could be used as an intermediate headline in the table column. If the approvalStatus is "APPROVED" it expresses that the collection of CollectableElements is known be valid for the given evaluatedVariants. Note that the EvaluatedVariantSet is a CollectableElement. This allows to establish a hierarchy of EvaluatedVariantSets. Tags: atp.recommendedPackage=EvaluatedVariantSets |
| 基类 | ARElement , ARObject , CollectableElement , Identifiable , MultilanguageReferrable , Packageable Element , Referrable |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::CommonStructure::FlatMap |
| 说明 | Contains a flat list of references to software objects. This list is used to identify instances and to resolve name conflicts. The scope is given by the RootSwCompositionPrototype for which it is used, i.e. it can be applied to a system, system extract or ECU-extract. An instance of FlatMap may also be used in a preliminary context, e.g. in the scope of a software component before integration into a system. In this case it is not referred by a RootSwComposition Prototype. Tags: atp.recommendedPackage=FlatMaps |
| 基类 | ARElement , ARObject , AtpBlueprint , AtpBlueprintable , CollectableElement , Identifiable , Multilanguage Referrable , PackageableElement , Referrable |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes |
| 说明 | Describes a reusable data type on the implementation level. This will typically correspond to a typedef in C-code. Tags: atp.recommendedPackage=ImplementationDataTypes |
| 基类 | ARElement , ARObject , AbstractImplementationDataType , AtpBlueprint , AtpBlueprintable , AtpClassifier , AtpType , AutosarDataType , CollectableElement , Identifiable , MultilanguageReferrable , Packageable Element , Referrable |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::IncludedDataTypes |
| 说明 | An includedDataTypeSet declares that a set of AutosarDataType is used by a basic software module or a software component for its implementation and the AutosarDataType becomes part of the contract. This information is required if the AutosarDataType is not used for any DataPrototype owned by this software component or if the enumeration literals, lowerLimit and upperLimit constants shall be generated with a literalPrefix. The optional literalPrefix is used to add a common prefix on enumeration literals, lowerLimit and upper Limit constants created by the RTE. |
| 基类 | ARObject |
| 聚合于 | BswInternalBehavior.includedDataTypeSet, SwcInternalBehavior.includedDataTypeSet |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::PortInterface |
| 说明 | Abstract base class for an interface that is either provided or required by a port of a software component. |
| 基类 | ARElement , ARObject , AtpBlueprint , AtpBlueprintable , AtpClassifier , AtpType , CollectableElement , Identifiable , MultilanguageReferrable , PackageableElement , Referrable |
| 子类 | ClientServerInterface, DataInterface , ModeSwitchInterface, TriggerInterface |
| 聚合于 | ARPackage.element |
| 包 | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable |
| 说明 | Instances of this class can be referred to by their identifier (while adhering to namespace borders). |
| 基类 | ARObject |
| 子类 | AtpDefinition , BswDistinguishedPartition, BswModuleCallPoint , BswModuleClientServerEntry, Bsw VariableAccess, CouplingPortTrafficClassAssignment, DiagnosticEnvModeElement , EthernetPriority Regeneration, ExclusiveAreaNestingOrder, HwDescriptionEntity , ImplementationProps , LinSlaveConfig Ident, ModeTransition, MultilanguageReferrable , PncMappingIdent, SingleLanguageReferrable , SoConI PduIdentifier, SocketConnectionBundle, TimeSyncServerConfiguration, TpConnectionIdent |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior |
| 说明 | A RunnableEntity represents the smallest code-fragment that is provided by an AtomicSwComponent Type and are executed under control of the RTE. RunnableEntities are for instance set up to respond to data reception or operation invocation on a server. |
| 基类 | ARObject , AtpClassifier , AtpFeature , AtpStructureElement , ExecutableEntity , Identifiable , Multilanguage Referrable , Referrable |
| 聚合于 | AtpClassifier .atpFeature, SwcInternalBehavior.runnable |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior |
| 说明 | The SwcInternalBehavior of an AtomicSwComponentType describes the relevant aspects of the software-component with respect to the RTE, i.e. the RunnableEntities and the RTEEvents they respond to. |
| 基类 | ARObject , AtpClassifier , AtpFeature , AtpStructureElement , Identifiable , InternalBehavior , Multilanguage Referrable , Referrable |
| 聚合于 | AtomicSwComponentType .internalBehavior, AtpClassifier .atpFeature |
| 包 | M2::AUTOSARTemplates::SWComponentTemplate::Components |
| 说明 | This meta-class represents the ability to attach with the symbol attribute a symbolic name that is conform to C language requirements to another meta-class, e.g. AtomicSwComponentType, that is a potential subject to a name clash on the level of RTE source code. |
| 基类 | ARObject , ImplementationProps , Referrable |
| 聚合于 | Allocator.namespace, ApApplicationErrorDomain.namespace, AtomicSwComponentType .symbolProps, CppImplementationDataType .namespace, ImplementationDataType.symbolProps, PortInterface . namespace, SecurityEventDefinition.eventSymbolName |
| 包 | M2::AUTOSARTemplates::GenericStructure::VariantHandling |
| 说明 | This meta-class represents the ability to express a "structural variation point". The container of the variation point is part of the selected variant if swSyscond evaluates to true and each postBuildVariant Criterion is fulfilled. |
| 基类 | ARObject |

| 属性 | 类型 | 多重性 | 种类 | 备注 |
| --- | --- | --- | --- | --- |
| Class | ARPackage |  |  |  |
| Class | ARPackage |  |  |  |
| arPackage | ARPackage | * | aggr | This represents a sub package within an ARPackage, thus allowing for an unlimited package hierarchy. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arPackage.shortName, arPackage.variation Point.shortLabel vh.latestBindingTime=blueprintDerivationTime xml.sequenceOffset=30 |
| element | PackageableElement | * | aggr | Elements that are part of this package Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=element.shortName, element.variation Point.shortLabel vh.latestBindingTime=systemDesignTime xml.sequenceOffset=20 |
| referenceBase | ReferenceBase | * | aggr | This denotes the reference bases for the package. This is the basis for all relative references within the package. The base needs to be selected according to the base attribute within the references. Stereotypes: atpSplitable Tags: atp.Splitkey=referenceBase.shortLabel xml.sequenceOffset=10 |
| Class | AliasNameSet |  |  |  |
| aliasName | AliasNameAssignment | * | aggr | AliasNames contained in the AliasNameSet. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=aliasName.shortLabel, aliasName.variation Point.shortLabel vh.latestBindingTime=preCompileTime |
| Class | AtomicSwComponentType (abstract) |  |  |  |
| Class | AtomicSwComponentType (abstract) |  |  |  |
| internalBehavior | SwcInternalBehavior | 0..1 | aggr | The SwcInternalBehaviors owned by an AtomicSw ComponentType can be located in a different physical file. Therefore the aggregation is <<atpSplitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=internalBehavior.shortName, internal Behavior.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| symbolProps | SymbolProps | 0..1 | aggr | This represents the SymbolProps for the AtomicSw ComponentType. Stereotypes: atpSplitable Tags: atp.Splitkey=symbolProps.shortName |
| Class | <<atpMixedString>> ConditionByFormula |  |  |  |
| bindingTime | BindingTimeEnum | 1 | attr | This attribute specifies the point in time when condition may be evaluated at earliest. At this point in time all referenced system constants shall have a value. Tags: xml.attribute=true |
| Class | EcuInstance |  |  |  |
| Class | EcuInstance |  |  |  |
| associatedCom IPduGroup | ISignalIPduGroup | * | ref | With this reference it is possible to identify which ISignal IPduGroups are applicable for which Communication Connector/ ECU. Only top level ISignalIPduGroups shall be referenced by an EcuInstance. If an ISignalIPduGroup contains other ISignalIPduGroups than these contained ISignalIPdu Groups shall not be referenced by the EcuInstance. Contained ISignalIPduGroups are associated to an Ecu Instance via the top level ISignalIPduGroup. |
| associated Consumed Provided ServiceInstance Group | ConsumedProvided ServiceInstanceGroup | * | ref | With this reference it is possible to identify which ConsumedProvidedServiceInstanceGroups are applicable for which ECUInstance. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=associatedConsumedProvidedService InstanceGroup.consumedProvidedServiceInstanceGroup, associatedConsumedProvidedServiceInstance Group.variationPoint.shortLabel vh.latestBindingTime=postBuild |
| associatedPdur IPduGroup | PdurIPduGroup | * | ref | With this reference it is possible to identify which PduR IPdu Groups are applicable for which Communication Connector/ ECU. |
| channel Synchronous Wakeup | Boolean | 0..1 | attr | If this parameter is available and set to true, then all available channels will be woken up as soon as at least one channel wakeup occurs. If PNCs are configured, then all PNCs will be requested upon a channel wakeup. |
| clientIdRange | ClientIdRange | 0..1 | aggr | Restriction of the Client Identifier for this Ecu to an allowed range of numerical values. The Client Identifier of the transaction handle is generated by the client RTE for inter-Ecu Client/Server communication. |
| com Configuration GwTimeBase | TimeValue | 0..1 | attr | The period between successive calls to Com_Main FunctionRouteSignals of the AUTOSAR COM module in seconds. |
| com ConfigurationRx TimeBase | TimeValue | 0..1 | attr | The period between successive calls to Com_Main FunctionRx of the AUTOSAR COM module in seconds. |
| com ConfigurationTx TimeBase | TimeValue | 0..1 | attr | The period between successive calls to Com_Main FunctionTx of the AUTOSAR COM module in seconds. |
| comEnable MDTForCyclic Transmission | Boolean | 0..1 | attr | Enables for the Com module of this EcuInstance the minimum delay time monitoring for cyclic and repeated transmissions (TransmissionModeTiming has cyclic Timing assigned or eventControlledTiming with numberOf Repetitions > 0). |
| commController | Communication Controller | * | aggr | CommunicationControllers of the ECU. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=commController.shortName, comm Controller.variationPoint.shortLabel vh.latestBindingTime=postBuild |
| connector | Communication Connector | * | aggr | All channels controlled by a single controller. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=connector.shortName, connector.variation Point.shortLabel vh.latestBindingTime=postBuild |
| dltConfig | DltConfig | 0..1 | aggr | Describes the Dlt configuration on this EcuInstance. |
| Class | EcuInstance |  |  |  |
| doIpConfig | DoIpConfig | 0..1 | aggr | DoIp configuration on this EcuInstance. Tags: atp.Status=draft |
| ecuTaskProxy | OsTaskProxy | * | ref | Reference to OsTaskProxies assigned to the Ecu Instance. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuTaskProxy |
| ethSwitchPort Group Derivation | Boolean | 0..1 | attr | Defines whether the derivation of SwitchPortGroups based on VLAN and/or CouplingPort.pncMapping shall be performed for this EcuInstance. If not defined the derivation shall not be done. |
| firewallRule | StateDependentFirewall | * | ref | Firewall rules defined in the context of an EcuInstance. Tags: atp.Status=candidate |
| partition | EcuPartition | * | aggr | Optional definition of Partitions within an Ecu. |
| pncNmRequest | Boolean | 0..1 | attr | Defines if this EcuInstance shall request Nm on all its PhysicalChannels which have Nm variant set to FULL each time a PNC is requested. |
| pncPrepare SleepTimer | TimeValue | 0..1 | attr | Time in seconds the PNC state machine shall wait in PNC_PREPARE_SLEEP. |
| pnc Synchronous Wakeup | Boolean | 0..1 | attr | If this parameter is available and set to true then all available PNCs will be woken up as soon as a channel wakeup occurs. This is ensured by adding all PNCs to all channel wakeup sources during upstream mapping. |
| pnResetTime | TimeValue | 0..1 | attr | Specifies the runtime of the reset timer in seconds. This reset time is valid for the reset of PN requests in the EIRA and in the ERA. |
| sleepMode Supported | Boolean | 0..1 | attr | Specifies whether the ECU instance may be put to a "low power mode" • true: sleep mode is supported • false: sleep mode is not supported Note: This flag may only be set to "true" if the feature is supported by both hardware and basic software. |
| tcpIpIcmpProps | EthTcpIpIcmpProps | 0..1 | ref | EcuInstance specific ICMP (Internet Control Message Protocol) attributes |
| tcpIpProps | EthTcpIpProps | 0..1 | ref | EcuInstance specific TcpIp Stack attributes. |
| v2xSupported | V2xSupportEnum | 0..1 | attr | This attribute is used to control the existence of the V2X stack on the given EcuInstance. |
| wakeUpOver BusSupported | Boolean | 0..1 | attr | Driver support for wakeup over Bus. |
| Class | EvaluatedVariantSet |  |  |  |
| approvalStatus | NameToken | 1 | attr | Defines the approval status of a predefined variant. Two values are predefined: "APPROVED" and "REJECTED": • Approved variants are known to work. • Rejected variants are known NOT to work. Further values can be approved on a per-company basis; within AUTOSAR only "APPROVED" and "REJECTED" should be recognized. |
| evaluated Element | CollectableElement | * | ref | This represents a particular element which is evaluated in context of the EvaluatedVariants. The approvalStatus applies to this element (and all of its descendants). In other words, the referenced elements are those that were considered when the predefined variant was evaluated. |
| evaluated Variant | PredefinedVariant | * | ref | This metaclass represents one particular variant which was evaluated. LowerMultiplicity is set to 0 to support a stepwise approach. |
| Class | FlatMap |  |  |  |
| Class | FlatMap |  |  |  |
| instance | FlatInstanceDescriptor | * | aggr | A descriptor instance aggregated in the flat map. The variation point accounts for the fact, that the system in scope can be subject to variability, and thus the existence of some instances is variable. The aggregation has been made splitable because the content might be contributed by different stakeholders at different times in the workflow. Plus, the overall size might be so big that eventually it becomes more manageable if it is distributed over several files. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instance.shortName, instance.variation Point.shortLabel vh.latestBindingTime=postBuild |
| Class | ImplementationDataType |  |  |  |
| dynamicArray SizeProfile | String | 0..1 | attr | Specifies the profile which the array will follow in case this data type is a variable size array. |
| isStructWith Optional Element | Boolean | 0..1 | attr | This attribute is only valid if the attribute category is set to STRUCTURE. If set to true, this attribute indicates that the ImplementationDataType has been created with the intention to define at least one element of the structure as optional. |
| subElement (ordered) | ImplementationData TypeElement | * | aggr | Specifies an element of an array, struct, or union data type. The aggregation of ImplementionDataTypeElement is subject to variability with the purpose to support the conditional existence of elements inside a Implementation DataType representing a structure. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=subElement.shortName, sub Element.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| symbolProps | SymbolProps | 0..1 | aggr | This represents the SymbolProps for the Implementation DataType. Stereotypes: atpSplitable Tags: atp.Splitkey=symbolProps.shortName |
| typeEmitter | NameToken | 0..1 | attr | This attribute is used to control which part of the AUTOSAR toolchain is supposed to trigger data type definitions. |
| Class | IncludedDataTypeSet |  |  |  |
| dataType | AutosarDataType | * | ref | AutosarDataType belonging to the includedDataTypeSet |
| literalPrefix | Identifier | 0..1 | attr | LiteralPrefix defines a common prefix for all AutosarData Types of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE. |
| Class | PortInterface (abstract) |  |  |  |
| isService | Boolean | 0..1 | attr | This flag is set if the PortInterface is to be used for communication between an • ApplicationSwComponentType or • ServiceProxySwComponentType or • SensorActuatorSwComponentType or • ComplexDeviceDriverSwComponentType • ServiceSwComponentType • EcuAbstractionSwComponentType and a ServiceSwComponentType (namely an AUTOSAR Service) located on the same ECU. Otherwise the flag is not set. Stereotypes: atpVariation Tags: vh.latestBindingTime=blueprintDerivationTime |
| serviceKind | ServiceProviderEnum | 0..1 | attr | This attribute provides further details about the nature of the applied service. |
| Class | Referrable (abstract) |  |  |  |
| Class | Referrable (abstract) |  |  |  |
| shortName | Identifier | 1 | attr | This specifies an identifying shortName for the object. It needs to be unique within its context and is intended for humans but even more for technical reference. Stereotypes: atpIdentityContributor Tags: xml.enforceMinMultiplicity=true xml.sequenceOffset=-100 |
| shortName Fragment | ShortNameFragment | * | aggr | This specifies how the Referrable.shortName is composed of several shortNameFragments. Tags: xml.sequenceOffset=-90 |
| Class | RunnableEntity |  |  |  |
| argument (ordered) | RunnableEntity Argument | * | aggr | This represents the formal definition of a an argument to a RunnableEntity. |
| asynchronous ServerCall ResultPoint | AsynchronousServer CallResultPoint | * | aggr | The server call result point admits a runnable to fetch the result of an asynchronous server call. The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=asynchronousServerCallResultPoint.short Name, asynchronousServerCallResultPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime |
| canBeInvoked Concurrently | Boolean | 0..1 | attr | If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponent Type). This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency. |
| Class | RunnableEntity |  |  |  |
| dataRead Access | VariableAccess | * | aggr | RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReadAccess.shortName, dataRead Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| dataReceive PointBy Argument | VariableAccess | * | aggr | RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of an argument in the function signature. The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByArgument.shortName, dataReceivePointByArgument.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| dataReceive PointByValue | VariableAccess | * | aggr | RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of the return value. The aggregation of dataReceivePointBy Value is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByValue.shortName, data ReceivePointByValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| dataSendPoint | VariableAccess | * | aggr | RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel |
| Class | RunnableEntity |  |  |  |
| dataWrite Access | VariableAccess | * | aggr | RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataWriteAccess.shortName, dataWrite Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| external TriggeringPoint | ExternalTriggeringPoint | * | aggr | The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=externalTriggeringPoint.ident.shortName, externalTriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| internal TriggeringPoint | InternalTriggeringPoint | * | aggr | The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=internalTriggeringPoint.shortName, internal TriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| modeAccess Point | ModeAccessPoint | * | aggr | The runnable has a mode access point. The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeAccessPoint.ident.shortName, mode AccessPoint.variationPoint.shortLabel |
| modeSwitch Point | ModeSwitchPoint | * | aggr | The runnable has a mode switch point. The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchPoint.shortName, modeSwitch Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| Class | RunnableEntity |  |  |  |
| parameter Access | ParameterAccess | * | aggr | The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a Parameter DataPrototype which may either be local or within a Port Prototype. The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of Parameter Access (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=parameterAccess.shortName, parameter Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| readLocal Variable | VariableAccess | * | aggr | The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of read LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=readLocalVariable.shortName, readLocal Variable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| serverCallPoint | ServerCallPoint | * | aggr | The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| symbol | CIdentifier | 0..1 | attr | The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase. |
| waitPoint | WaitPoint | * | aggr | The WaitPoint associated with the RunnableEntity. |
| writtenLocal Variable | VariableAccess | * | aggr | The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of written LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=writtenLocalVariable.shortName, written LocalVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| Class | SwcInternalBehavior |  |  |  |
| arTypedPer Instance Memory | VariableDataPrototype | * | aggr | Defines an AUTOSAR typed memory-block that needs to be available for each instance of the SW-component. This is typically only useful if supportsMultipleInstantiation is set to "true" or if the component defines NVRAM access via permanent blocks. The aggregation of arTypedPerInstanceMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arTypedPerInstanceMemory.shortName, ar TypedPerInstanceMemory.variationPoint.shortLabel |
| event | RTEEvent | * | aggr | This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime |
| exclusiveArea Policy | SwcExclusiveArea Policy | * | aggr | Options how to generate the ExclusiveArea related APIs. When no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values apply. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaPolicy, exclusiveArea Policy.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| explicitInter Runnable Variable | VariableDataPrototype | * | aggr | Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| Class | SwcInternalBehavior |  |  |  |
| implicitInter Runnable Variable | VariableDataPrototype | * | aggr | Implement state message semantics for establishing communication among runnables of the same component. The aggregation of implicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=implicitInterRunnableVariable.shortName, implicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| includedData TypeSet | IncludedDataTypeSet | * | aggr | The includedDataTypeSet is used by a software component for its implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=includedDataTypeSet |
| includedMode Declaration GroupSet | IncludedMode DeclarationGroupSet | * | aggr | This aggregation represents the included Mode DeclarationGroups Stereotypes: atpSplitable Tags: atp.Splitkey=includedModeDeclarationGroupSet |
| instantiation DataDefProps | InstantiationDataDef Props | * | aggr | The purpose of this is that within the context of a given SwComponentType some data def properties of individual instantiations can be modified. The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of Port Prototypes and component local memories like "per InstanceParameter" or "arTypedPerInstanceMemory". Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=instantiationDataDefProps, instantiationData DefProps.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| perInstance Memory | PerInstanceMemory | * | aggr | Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| Class | SwcInternalBehavior |  |  |  |
| perInstance Parameter | ParameterData Prototype | * | aggr | Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| portAPIOption | PortAPIOption | * | aggr | Options for generating the signature of port-related calls from a runnable to the RTE and vice versa. The aggregation of PortPrototypes is subject to variability with the purpose to support the conditional existence of ports. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portAPIOption, portAPIOption.variation Point.shortLabel vh.latestBindingTime=preCompileTime |
| runnable | RunnableEntity | * | aggr | This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime |
| service Dependency | SwcService Dependency | * | aggr | Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| Class | SwcInternalBehavior |  |  |  |
| shared Parameter | ParameterData Prototype | * | aggr | Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime |
| supports Multiple Instantiation | Boolean | 0..1 | attr | Indicate whether the corresponding software-component can be multiply instantiated on one ECU. In this case the attribute will result in an appropriate component API on programming language level (with or without instance handle). |
| variationPoint Proxy | VariationPointProxy | * | aggr | Proxy of a variation points in the C/C++ implementation. Stereotypes: atpSplitable Tags: atp.Splitkey=variationPointProxy.shortName |
| Class | SymbolProps |  |  |  |
| Class | VariationPoint |  |  |  |
| blueprint Condition | DocumentationBlock | 0..1 | aggr | This represents a description that documents how the variation point shall be resolved when deriving objects from the blueprint. Note that variationPoints are not allowed within a blueprintCondition. Tags: xml.sequenceOffset=28 |
| Class | VariationPoint |  |  |  |
| desc | MultiLanguageOverview Paragraph | 0..1 | aggr | This allows to describe shortly the purpose of the variation point. Tags: xml.sequenceOffset=20 |
| formalBlueprint Generator | BlueprintGenerator | 0..1 | aggr | This represents a description that documents how the variation point shall be resolved when deriving objects from the blueprint by using ARMQL. Note that variationPoints are not allowed within a formal BlueprintGenerator. Tags: atp.Status=draft xml.sequenceOffset=30 |
| postBuildVariant Condition | PostBuildVariant Condition | * | aggr | This is the set of post build variant conditions which all shall be fulfilled in order to (postbuild) bind the variation point. Tags: xml.sequenceOffset=40 |
| sdg | Sdg | 0..1 | aggr | An optional special data group is attached to every variation point. These data can be used by external software systems to attach application specific data. For example, a variant management system might add an identifier, an URL or a specific classifier. Tags: xml.sequenceOffset=50 |
| shortLabel | Identifier | 0..1 | attr | This provides a name to the particular variation point to support the RTE generator. It is necessary for supporting splitable aggregations and if binding time is later than codeGenerationTime, as well as some RTE conditions. It needs to be unique with in the enclosing Identifiables with the same ShortName. Stereotypes: atpIdentityContributor Tags: xml.sequenceOffset=10 |
| swSyscond | ConditionByFormula | 0..1 | aggr | This condition acts as Binding Function for the Variation Point. Note that the multiplicity is 0..1 in order to support pure postBuild variants. Tags: xml.sequenceOffset=30 |

## B. 变更历史（**Change History**）

**注意：** 依照 TPS_APSD 附录先例，以下变更历史表仅保留标题列（Number 列按批项决策丢弃）。

请注意，本章中的清单还包括在后续版本中已从规范中移除的规范项。这些规范项在文档中不再作为超链接出现。

### B.1. 本文档 R4.1.1 版本的变更历史

#### B.1.1. 4.1.1 中新增的规范项

表B.1：Added Specification Items in 4.1.1（**Added Specification Items in 4.1.1**）

| 标题 |
| --- |
| Definition of Binding Time for Tasks |
| Definition of Binding Time for Artifacts |
| Definition of Binding Time for Artifacts in the context of particular tasks |
| Domains of the AUTOSAR methodology |
| AUTOSAR methodology assets |
| AUTOSAR methodology use cases |
| Scope of the AUTOSAR methodology |
| Support for various stakeholders by the AUTOSAR methodology |
| Restrictions of AUTOSAR methodology |
| General AUTOSAR methodology concepts |
| Method Library |
| Method Library Element |
| Relation of Method Library and Method Library Element to theSPEM meta model |
| Overview of Method Library Elements |
| Task Definition |
| Task semantics |
| Task usage |
| Work Product Definition |
| Relationship between Roles and Work Products |
| Artifact Definition |
| Kinds of Artifacts |
| Properties of Artifacts |
| Relationship between Artifacts and meta model elements |
| Deliverable Definition |
| Aggregation of Work Products |
| Role Definition |
| Role assignment |
| Tool Definition |
| Guidance definition |
| Guidance kinds |
| Usage of tables |
| Capability Patterns definition |
| Composition of Capability Patterns |
| Adaptability of the AUTOSAR methodology |
| Use case elements |
| Definition of Activities |
| Composition of Activities |
| Definition of Processes |
| Description of overall Use Cases |
| Precise description of Use Cases |
| Detailed description of the work flow |
| AUTOSAR System development overview |
| Support of different system views |
| Abstract system |
| Overall technical system |
| Sub-System |
| Development of a functional view on the system |
| Development of the Overall VFB System |
| Development of the system |
| Two phase development approach |
| The overall system |
| Interaction between organizations |
| Abstract System Description activity |
| Creation of an overall abstract system |
| Definition of a constraints in the context of an abstract system |
| Definition of a System Description in the context of an abstract system |
| Virtual Functional Bus |
| Data Model Development activity |
| Definition of the VFB |
| Top-Down approach |
| Bottom-Up approach |
| Kinds of VFB Atomic Software Component s |
| Develop an Atomic Software Component activity |
| Develop Application Software activity |
| Develop System and Develop Sub-System activities |
| Creation of a System Extract and a ECU Extract |
| Abstract System Description deliverable |
| Inputs and Output of the Design System activity |
| Deployment of AUTOSAR Software Components |
| Description of network signals |
| Description of design constraints |
| Design Sub-System activity |
| Design Sub-System activity |
| Transformation changes during the Mapping of different views |
| Use Case: Substitution of existing components |
| Use Case: Mapping of requirements to the solution |
| Use Case: Reorganization of the software structure versions |
| Use Case: Description of changes between different of System De- scription s |
| Design Basic Software activity |
| Separation of design and development of basic software |
| Develop BSW Module activity |
| Integrate Software for ECU activity |
| Scope of Integrate Software for ECU activity |
| activity |
| Configure BSW and RTE task |
| Configure Debug task |
| Generating BSW modules, RTE, and OS source files |
| Building ECU Executable |
| Configuration Class: Pre-compile Time |
| Generating header files only |
| Generating header and source files |
| Configuration Class: Link Time |
| Generation and compilation of BSW Configuration Code |
| Definition of configuration data |
| Separate compilation of module source and configuration file |
| Linking process |
| Re-generation in case of configuration value changes |
| Configuration Class: Post-build Time |
| Generate BSW Postbuild Configuration Code |
| Generate BSW Configuration Data Loadable |
| Configuration Class: Post-build Time Selectable |
| Generating multiple post-build configuration variants |
| Producing ECU-specific deliverables |
| Development of Software Components |
| Development of Basic Software modules |
| Integration of AUTOSAR ECUs |
| Usage of hyperlinks |
| Definition of Consistency Needs |
| Building the AUTOSAR methodology document |
| Relations between AUTOSAR Work Products |
| Traceability to external artifacts |
| Documentation of Work Products Use of AUTOSAR Services |
| Define Cross-component Calibration Parameters activity |
| Define Local Calibration Parameters activity |
| Provide Unique Parameter Names activity |
| Re-generate RTE and Calibration Support activity |
| Memory sections for data and code |
| E2E Protection Define E2E Protection Set activity |
| Regenerate E2E Protection Wrapper activity |
| Variation points in Variant Handling |
| Predefined Variants in Variant Handling |
| Types of binding times |
| Definition of a binding time |
| Latest Binding Time |
| Actual Binding Time |
| Definition of variants |
| Evaluated Variant Set |
| Use of Predefined Variant |
| Choosing variants |
| Definition of latest Binding Time for a variation point in the meta-model |
| Name spaces via s |
| ARPackage Reasons for name conflicts in 'downstream' artifacts |
| Conflict solution at system design time Conflict solution at coding time |
| Conflict solution at ECU integration time |
| Conflict solution via literal prefixes |
| Conflict solution in names of runnable entities |
| Conflict solution via FlatMap |
| Conflict solution via AliasNameSet |
| Conflict solution via API Infixes |

#### B.1.2. 4.1.1 中变更的规范项

无

#### B.1.3. 4.1.1 中删除的规范项

无

### B.2. 本文档 R4.1.2 版本的变更历史

#### B.2.1. 4.1.2 中新增的规范项

表B.2：Added Specification Items in 4.1.2（**Added Specification Items in 4.1.2**）

| 标题 |
| --- |
| Input sources for ECU Configuration |
| A mix of parameters with different configuration classes within a BSW module is allowed |
| ECU Configuration Value description contains the configuration of all BSW modules in a single ECU |
| BSW implementation shall be chosen for each BSW module that is present in the ECU |

#### B.2.2. 4.1.2 中变更的规范项

无

#### B.2.3. 4.1.2 中删除的规范项

无

### B.3. 本文档 R4.1.3 版本的变更历史

#### B.3.1. 4.1.3 中新增的规范项

表B.3：Added Specification Items in 4.1.3（**Added Specification Items in 4.1.3**）

| 标题 |
| --- |
| Create ECU System Description activity |
| Using the System Extract as the structural basis for the ECU development |
| Creating a new structure for the ECU development |

#### B.3.2. 4.1.3 中变更的规范项

表B.4：Changed Specification Items in 4.1.3（**Changed Specification Items in 4.1.3**）

| 标题 |
| --- |
| Interaction between organizations |
| Creation of a System Extract and an ECU Extract |
| Design Sub-System activity |
| Collaboration between different organizations |

#### B.3.3. 4.1.3 中删除的规范项

无

### B.4. 本文档 R4.2.1 版本的变更历史

#### B.4.1. 4.2.1 中新增的规范项

表B.5：Added Specification Items in 4.2.1（**Added Specification Items in 4.2.1**）

| 标题 |
| --- |
| Integration of Non AUTOSAR Systems in the context of an abstract system |
| Integrate Non AUTOSAR System at VFB level activity |
| Design Transformer activity |
| Output of Design Transformer activity |
| Definition of a Rapid Prototyping Scenario |
| Content of Rapid Prototyping Scenario artifact |
| Component wrapper method |
| Direct buffer access method |
| Content of Diagnostic Extract |
| Diagnostic Extract category |
| Decentralized configuration |
| Roles |
| Develop Diagnostic Abstract System Description activity |
| Development of diagnostic requirements |
| Diagnostic information in the context of SW-C development |
| Integration of diagnostic information |
| Activity Define Safety Information |
| Creation of Safety Requirement s |
| Allocation of Safety Requirement s |
| Decomposition of Safety Requirement s |
| Definition of Safety Measure s |
| Definition of VFB relevant safety information |
| Including different post-build variants |
| Update ECU Configuration activity |
| Configuration and Generation of the E2E Transformer |
| Define E2E Transformer Technology Task |

#### B.4.2. 4.2.1 中变更的规范项

表B.6：Changed Specification Items in 4.2.1（**Changed Specification Items in 4.2.1**）

| 标题 |
| --- |
| Kinds of VFB Atomic Software Component s |
| Development of the system |
| Develop System and Develop Sub-System activities |
| Develop an Atomic Software Component activity |
| Develop System and Develop Sub-System activities |
| Configuration Class: Post-build Time |
| Generate BSW Postbuild Configuration Code |
| Generating multiple post-build configuration variants |
| E2E Protection |

#### B.4.3. 4.2.1 中删除的规范项

表B.7：Deleted Specification Items in 4.2.1（**Deleted Specification Items in 4.2.1**）

| 标题 |
| --- |
| Generate BSW Configuration Data Loadable |
| Configuration Class: Post-build Time Selectable |
| Define E2E Protection Set activity |
| Regenerate E2E Protection Wrapper activity |

### B.5. 本文档 R4.2.2 版本的变更历史

#### B.5.1. 4.2.2 中新增的规范项

无

#### B.5.2. 4.2.2 中变更的规范项

无

#### B.5.3. 4.2.2 中删除的规范项

无

### B.6. 本文档 R4.3.0 版本的变更历史

#### B.6.1. 4.3.0 中新增的规范项

表B.8：Added Specification Items in 4.3.0（**Added Specification Items in 4.3.0**）

| 标题 |
| --- |
| Definition of serialization |
| Use case: Serialization based on network representation |
| Use case: Serialization based on implementation data types |
| Create a Profile of Data Exchange Point |
| Agreement on a profile for data exchange points |
| Validation based on an Agreed Profile of Data Exchange Point |

#### B.6.2. 4.3.0 中变更的规范项

表B.9：Changed Specification Items in 4.3.0（**Changed Specification Items in 4.3.0**）

| 标题 |
| --- |
| General AUTOSAR methodology concepts |
| Task usage |
| Use case elements |
| Description of overall Use Cases |
| Precise description of Use Cases |
| Domains of the AUTOSAR methodology |
| Virtual Functional Bus View |
| Support of different system views |
| Development of a functional view on the system |
| Development of the Overall VFB System |
| Development of the system |
| Two phase development approach |
| Interaction between organizations |
| Producing ECU-specific deliverables |
| Development of Software Components |
| Integration of AUTOSAR ECUs |
| Building ECU Executable |
| Description of design constraints |
| Design Custom Transformer activity |
| Output of Design Custom Transformer activity |

#### B.6.3. 4.3.0 中删除的规范项

无

### B.7. 本文档 R4.3.1 版本的变更历史


无

#### B.7.2. 4.3.1 中变更的规范项

表B.10：Changed Specification Items in 4.3.1（**Changed Specification Items in 4.3.1**）

| 标题 |
| --- |
| Work Product Definition |


无

### B.8. 本文档 R4.4.0 版本的变更历史

#### B.8.1. 4.4.0 中新增的规范项

无

#### B.8.2. 4.4.0 中变更的规范项

表B.11：Changed Specification Items in 4.4.0（**Changed Specification Items in 4.4.0**）

| 标题 |
| --- |
| AUTOSAR methodology assets |
| AUTOSAR methodology use cases |
| Support for various stakeholders by the AUTOSAR methodology |
| Restrictions of AUTOSAR methodology |
| General AUTOSAR methodology concepts |
| Heading |
| Methodology Library |
| Methodology Library Element |
| Relation of Methodology Library and Methodology Library Ele- ment to the SPEM meta model |
| Overview of Methodology Library Elements |
| Task Definition |
| Task semantics |
| Task usage |
| Work Product Definition |
| Relationship between Roles and Work Products |
| Artifact Definition |
| Kinds of Artifacts |
| Properties of Artifacts |
| Relationship between Artifacts and meta-model elements |
| Deliverable Definition |
| Aggregation of Work Products |
| Role Definition |
| Role assignment |
| Guidance definition |
| Guidance kinds |
| Usage of tables |
| Definition of Activities |
| Composition of Activities |
| Development of a functional view on the system |
| Development of the system |
| Two phase development approach |
| The overall system |
| Abstract System Description activity |
| Creation of an overall abstract system |
| Definition of a constraints in the context of an abstract system |
| Definition of a System Description in the context of an abstract system |
| Virtual Functional Bus |
| Data Model Development activity |
| Definition of the VFB |
| Top-Down approach |
| Bottom-Up approach |
| Kinds of VFB Atomic Software Component s |
| Develop an Atomic Software Component activity |
| Develop Application Software activity |
| Heading |
| Develop System and Develop Sub-System activities |
| Creation of a System Extract and an ECU Extract |
| Abstract System Description deliverable |
| Inputs and Output of the Design System activity |
| Description of network signals |
| Description of design constraints |
| Design Sub-System activity |
| Collaboration between different organizations |
| Transformation changes during the Design Sub-System activity |
| Mapping of different views |
| Use Case: Substitution of existing components |
| Use Case: Mapping of requirements to the solution |
| Use Case: Reorganization of the software structure |
| Use Case: Description of changes between different versions of System Description s |
| Design Basic Software activity |
| Separation of design and development of basic software |
| Develop BSW Module activity |
| Integrate Software for ECU activity |
| Scope of Integrate Software for ECU activity |
| Prepare ECU Configuration activity |
| Configure BSW and RTE activity |
| Configure RTE task |
| Generating BSW modules, RTE, and OS source files |
| Building ECU Executable |
| Configuration Class: Pre-compile Time |
| Configuration Class: Link Time |
| Re-generation in case of configuration value changes |
| Configuration Class: Post-build Time |
| Producing ECU-specific deliverables |
| Development of Software Components |
| Development of Basic Software modules |
| Integration of AUTOSAR ECUs |
| Usage of hyperlinks |
| Input sources for ECU Configuration |
| A mix of parameters with different configuration classes within a BSWmodule is allowed |
| ECU Configuration Value description contains the configuration of all BSW modules in a single ECU |
| Heading |
| BSW implementation shall be chosen for each BSW module that is present in the ECU |
| Building the AUTOSAR methodology document |
| Relations between AUTOSAR Work Products |
| Traceability to external artifacts |
| Create ECU System Description activity |
| Using the System Extract as the structural basis for the ECUdevelopment |
| Creating a new structure for the ECU development |
| Design Custom Transformer activity |
| Definition of a Rapid Prototyping Scenario |
| Content of Rapid Prototyping Scenario artifact |
| Content of Diagnostic Extract |
| Diagnostic Extract category |
| Decentralized configuration |
| Roles |
| Develop Diagnostic Abstract System Description activity |
| Development of diagnostic requirements |
| Diagnostic information in the context of SW-C development |
| Integration of diagnostic information |
| Activity Define Safety Information |
| Creation of Safety Requirement s |
| Allocation of Safety Requirement s |
| Decomposition of Safety Requirement s |
| Definition of Safety Measure s |
| Definition of VFB relevant safety information |
| Update ECU Configuration activity |
| Configuration and Generation of the E2E Transformer |
| Define E2E Transformer Technology Task |
| Definition of serialization |
| Use case: Serialization based on network representation |
| Use case: Serialization based on implementation data types |
| Use of AUTOSAR Services |
| Define Cross-component Calibration Parameters activity |
| Define Local Calibration Parameters activity |
| Provide Unique Parameter Names activity |
| Memory sections for data and code |
| E2E Protection |
| Definition of variants |
| Evaluated Variant Set |
| Heading |
| Use of Predefined Variant |
| Choosing variants |
| Name spaces via ARPackage s |
| Reasons for name conflicts in 'downstream' artifacts |
| Conflict solution via SymbolProps |
| Conflict solution via literal prefixes |
| Conflict solution in names of runnable entities |
| Conflict solution via FlatMap |
| Conflict solution via API Infixes |

#### B.8.3. 4.4.0 中删除的规范项

表B.12：Deleted Specification Items in 4.4.0（**Deleted Specification Items in 4.4.0**）

| 标题 |
| --- |
| Configure Debug task |

### B.9. 本文档 R19-11 版本的变更历史

#### B.9.1. 19-11 中新增的规范项

无

#### B.9.2. 19-11 中变更的规范项

表B.13：Changed Specification Items in 19-11（**Changed Specification Items in 19-11**）

| 标题 |
| --- |
| Domains of the AUTOSAR methodology |
| AUTOSAR methodology assets |
| AUTOSAR methodology use cases |
| Scope of the AUTOSAR methodology |
| Restrictions of AUTOSAR methodology |
| General AUTOSAR methodology concepts |
| Heading |
| Methodology Library |
| Methodology Library Element |
| Relation of Methodology Library and Methodology Library Ele- ment to the SPEM meta model |
| Overview of Methodology Library Element s |
| Task Definition |
| Task usage |
| Work Product Definition |
| Relationship between Role s and Work Product s |
| Artifact Definition |
| Kinds of Artifacts |
| Deliverable Definition |
| Aggregation of Work Product s |
| Role Definition |
| Role assignment |
| Tool Definition |
| Guidance definition |
| Use case elements |
| Composition of Activities |
| Description of overall Use Cases |
| Precise description of Use Cases |
| Detailed description of the work flow |
| Development of a functional view on the system |
| Development of the Overall VFB System |
| Development of the system |
| Interaction between organizations |
| Data Model Development activity |
| Definition of the VFB |
| Develop an Atomic Software Component activity |
| Develop System and Develop Sub-System activities |
| Creation of a System Extract and an ECU Extract |
| Producing ECU-specific deliverables |
| Development of Software Components |
| Development of Basic Software modules |
| Integration of AUTOSAR ECUs |
| Usage of hyperlinks |
| Definition of Consistency Needs |
| Building the AUTOSAR methodology document |
| Traceability to external artifacts |
| Heading |
| Roles |
| Activity Define Safety Information |
| Definition of VFB relevant safety information |
| Including different post-build variants |

#### B.9.3. 19-11 中删除的规范项

无

### B.10. 本文档 R20-11 版本的变更历史

#### B.10.1. R20-11 中新增的规范项

无


无

#### B.10.3. R20-11 中删除的规范项

无

### B.11. 本文档 R21-11 版本的变更历史

#### B.11.1. R21-11 中新增的规范项

无

#### B.11.2. R21-11 中变更的规范项

无

#### B.11.3. R21-11 中删除的规范项

无

### B.12. 本文档 R22-11 版本的变更历史

#### B.12.1. R22-11 中新增的规范项

无

#### B.12.2. R22-11 中变更的规范项

表B.14：Changed Specification Items in R22-11（**Changed Specification Items in R22-11**）

| 标题 |
| --- |
| Scope of Integrate Software for ECU activity |
| Integration of EcuInstance s |
| Memory sections for data and code |
| Conflict solution via SymbolProps |

#### B.12.3. R22-11 中删除的规范项

无

### B.13. 本文档 R23-11 版本的变更历史

#### B.13.1. R23-11 中新增的规范项

无

#### B.13.2. R23-11 中变更的规范项

无

#### B.13.3. R23-11 中删除的规范项

无


