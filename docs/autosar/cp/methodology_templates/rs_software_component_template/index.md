---
title: "Requirements on Software Component Template（软件组件模板需求）"
spec: AUTOSAR_CP_RS_SoftwareComponentTemplate
release: R23-11
---

<!-- 源文档 AUTOSAR_CP_RS_SoftwareComponentTemplate（R23-11），需求规范（RS），不受 Type A 七章骨架约束；章节结构镜像源文档自身编号（参考文献不编号，1–3）。需求项 ID [RS_SWCT_*] 按 2026-11-03 Foundation 批次决议整体省略（标题仅翻译）。§1.4 Requirements Tracing 为纯 ID 追溯表，按 ASWS 先例省略（§1.1–§1.3 编号不变）。封面元数据表、文档变更记录表、免责声明与目录按 EXP 流程省略。源 markdown 中 ch.2 的大部分需求项标题在转换中丢失（仅 §2.3.9 保留），已依据 R23-11 PDF 逐项恢复为「粗体项标题行 + 五字段表」形式；§2.3.4、§2.3.23、§2.3.35、§2.3.39、§2.3.45、§2.3.47 的表格单元格错列也已按 PDF 原文恢复。源文档全部 60 处图片引用均为页面装饰性元素，无内容插图。§2.1/§2.2 的项内容为对主需求/特性定义文档的引用，被引用项 ID 按决议以不带方括号的形式保留。第 3 章为「AUTOSAR 可追溯项变更历史」（编号章节），按附录 B 先例译出（标题仅翻译的标题列）。 -->

## 参考文献

<a id="ref-1"></a>[1] Software Component Template
> AUTOSAR_CP_TPS_SoftwareComponentTemplate

<a id="ref-2"></a>[2] Standardization Template
> AUTOSAR_FO_TPS_StandardizationTemplate

<a id="ref-3"></a>[3] Main Requirements
> AUTOSAR_FO_RS_Main

<a id="ref-4"></a>[4] Requirements on AUTOSAR Features
> AUTOSAR_CP_RS_Features

<a id="ref-5"></a>[5] Feature Definition
> AUTOSAR_FeatureDefinition.pdf

<a id="ref-6"></a>[6] Specification of SW-C End-to-End Communication Protection Library
> AUTOSAR_CP_SWS_E2ELibrary

## 1. 简介

### 1.1. 本文档的范围

本文档收集对软件组件模板（**Software Component Template**，**SWC-T**）的需求。

本文档中收集的需求将由软件组件模板规范 [\[1\]](#ref-1) 满足。该文档实现了本文所述的大部分需求。

### 1.2. 文档约定

**AUTOSAR** 文档中需求的表示遵循 TPS\_STDT\_00078 所规定的表格，参见标准模板（**Standardization Template**）的「追溯支持」（**Support for Traceability**）一章（[\[2\]](#ref-2)）。

应使用 TPS\_STDT\_00053 中规定的用于表达义务的助动词形式来表示需求，参见标准模板（**Standardization Template**）的「追溯支持」（**Support for Traceability**）一章（[\[2\]](#ref-2)）。

### 1.3. 指南

应引用既有的规范（以单个需求的形式）。与这些规范的差异作为附加需求加以规定。所有需求应具有以下特性：

- 无冗余（**Redundancy**）

  在单个需求之内或其他需求之中，需求不应重复。

- 清晰性（**Clearness**）

  所有需求应只允许一种解释。所使用的不在术语表中的技术术语必须加以定义。

- 原子性（**Atomicity**）

  每个需求应只包含一个需求。如果一个需求不能再被拆分为更多的需求，则它是原子的。

- 可测试性（**Testability**）

  需求应能通过分析、评审或测试加以验证。

- 可追溯性（**Traceability**）

  需求的来源和状态应始终可见。

## 2. 需求

本章描述驱动软件组件模板规范 [\[1\]](#ref-1) 定义工作的全部需求。这些需求可追溯到主需求（**Main Requirements**） [\[3\]](#ref-3) 和 **AUTOSAR** 特性（**AUTOSAR Features**） [\[4\]](#ref-4)。

### 2.1. 类别：AUTOSAR 主要需求

本节对主需求 [\[3\]](#ref-3) 中定义的相关需求进行重新定义。

#### 2.1.1. 支持 ECU 通信（**Support of ECU-communication**）

| 描述 | 参见需求 RS\_Main\_00050。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00050。 |
| 用例 | 参见需求 RS\_Main\_00050。 |
| 依赖项 | - |
| 支撑材料 | - |

| 描述 | 参见需求 RS\_Main\_00060。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00060。 |
| 用例 | 参见需求 RS\_Main\_00060。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.2. 到应用软件和基础软件模块的接口（**Interfaces to application software and basic software modules**）

| 描述 | 参见需求 Main70。 |
| --- | --- |
| 理由 | 参见需求 Main70。 |
| 用例 | 参见需求 Main70。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.3. 应用软件的抽象与独立性（**Abstraction and Independence of the application software**）

| 描述 | 参见需求 RS\_Main\_00130。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00130。 |
| 用例 | 参见需求 RS\_Main\_00130。 |
| 依赖项 | - |
| 支撑材料 | - |

| 描述 | 参见需求 RS\_Main\_00140。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00140。 |
| 用例 | 参见需求 RS\_Main\_00140。 |
| 依赖项 | - |
| 支撑材料 | - |

| 描述 | 参见需求 RS\_Main\_00141。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00141。 |
| 用例 | 参见需求 RS\_Main\_00141。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.4. 功能接口视图（**Functional interface view**）

| 描述 | 参见需求 RS\_Main\_00160。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00160。 |
| 用例 | 参见需求 RS\_Main\_00160。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.5. 软件的保护/解锁机制（**Protection/unlock mechanisms for software**）

| 描述 | 参见需求 RS\_Main\_00180。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00180。 |
| 用例 | 参见需求 RS\_Main\_00180。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.6. 保护软件组件免受恶意软件组件的侵害（**Protection of SW-Components from malicious SW-Components**）

| 描述 | 参见需求 RS\_Main\_00240。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00240。 |
| 用例 | 参见需求 RS\_Main\_00240。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.7. 可组合性（**Compositionality**）

| 描述 | 参见需求 RS\_Main\_00250。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00250。 |
| 用例 | 参见需求 RS\_Main\_00250。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.8. 运行期间、生产和售后服务用途的诊断（**Diagnostics during runtime, for production and services purposes**）

| 描述 | 参见需求 RS\_Main\_00260。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00260。 |
| 用例 | 参见需求 RS\_Main\_00260。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.9. 层次化设计方法（**Hierarchical design methods**）

| 描述 | 参见需求 RS\_Main\_00310。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00310。 |
| 用例 | 参见需求 RS\_Main\_00310。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.10. 软件组件之间的关系（**Relations between SW components**）

| 描述 | 参见需求 RS\_Main\_00320。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00320。 |
| 用例 | 参见需求 RS\_Main\_00320。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.11. 防止非法访问（**Protection from illegal access**）

| 描述 | 参见需求 RS\_Main\_00330。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00330。 |
| 用例 | 参见需求 RS\_Main\_00330。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.12. 车辆多样性的管理（**Management of vehicle diversity**）

| 描述 | 参见需求 RS\_Main\_00360。 |
| --- | --- |
| 理由 | 参见需求 RS\_Main\_00360。 |
| 用例 | 参见需求 RS\_Main\_00360。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.1.13. 命名约定（**Naming conventions**）

| 描述 | 软件组件模板应提供定义公共符号命名约定的能力。这尤其包括发布版文档中使用的需求 ID、模块缩写、元数据和配置符号。 |
| --- | --- |
| 理由 | 避免规范内部的歧义和命名冲突。向规范的读者提供一致、统一的元数据呈现。允许对规范元素进行自动处理。 |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

软件组件模板并不定义具体的命名约定。此类命名约定实际定义在 **AUTOSAR** AISpecification [\[2\]](#ref-2) 中。

### 2.2. 类别：AUTOSAR 特性定义需求

本节定义来自特性定义（**Feature Definition**） [\[5\]](#ref-5) 第 3.2 章用例的需求。被引用的文档自 **AUTOSAR** 4.0 发布版起已废止，但在之前的发布版中存在。

#### 2.2.1. 自顶向下的层次化设计（**Top-down hierarchical design**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.1 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.1 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.1 章的用例。 |
| 依赖项 | RS\_SWCT\_00190 |
| 支撑材料 | - |

#### 2.2.2. 原子软件组件的接口（**Interfaces of atomic software-components**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.2 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.2 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.2 章的用例。 |
| 依赖项 | RS\_SWCT\_00020 |
| 支撑材料 | - |

#### 2.2.3. 组合类型（CompositionTypes）的自底向上设计（**Bottom-up design of CompositionTypes**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.3 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.3 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.3 章的用例。 |
| 依赖项 | RS\_SWCT\_00160、RS\_SWCT\_00200 |
| 支撑材料 | - |

#### 2.2.4. 通信的规定（**Specification of Communications**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.5 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.5 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.5 章的用例。 |
| 依赖项 | RS\_SWCT\_00010、RS\_SWCT\_00020 |
| 支撑材料 | - |

#### 2.2.5. 与基础软件的交互（**Interaction with basic software**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.9 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.9 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.9 章的用例。 |
| 依赖项 | RS\_SWCT\_00030 |
| 支撑材料 | - |

#### 2.2.6. 传感器执行器组件（**Sensor Actuator Components**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.14 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.14 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.14 章的用例。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.2.7. RunnableEntity 之间通信的数据一致性（**Data-consistency for communication among RunnableEntities**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.20 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.20 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.20 章的用例。 |
| 依赖项 | RS\_SWCT\_00010 |
| 支撑材料 | - |

#### 2.2.8. 物理单位（**Physical units**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.21 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.21 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.21 章的用例。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.2.9. 注释（**Comments**）

| 描述 | 参见 [\[5\]](#ref-5) 第 3.2.22 章的用例。 |
| --- | --- |
| 理由 | 参见 [\[5\]](#ref-5) 第 3.2.22 章的用例。 |
| 用例 | 参见 [\[5\]](#ref-5) 第 3.2.22 章的用例。 |
| 依赖项 | - |
| 支撑材料 | - |

### 2.3. 类别：软件组件模板需求

本节定义来自各个 **AUTOSAR** 工作组（例如方法论与配置工作组等）的需求。

#### 2.3.1. 组合（**Compositions**）

**SW-Component 模板应支持组合（**The SW-Component template shall support compositions**）**

| 描述 | SW-Component 模板必须允许将既有软件组件聚合为一个组件，该组件本身也可以再被聚合。 |
| --- | --- |
| 理由 | - |
| 用例 | - |
| 依赖项 | RS\_SWCT\_02020、RS\_SWCT\_00160 |
| 支撑材料 | - |

#### 2.3.2. 接口（**Interfaces**）

**SW-Component 模板应支持接口（**The SW-Component template shall support interfaces**）**

| 描述 | SW-Component 模板必须允许独立于软件组件规定接口。（即使没有组件使用某个定义，该定义也可以存在。） |
| --- | --- |
| 理由 | - |
| 用例 | - |
| 依赖项 | RS\_SWCT\_02010、RS\_SWCT\_00010、RS\_SWCT\_00020 |
| 支撑材料 | - |

#### 2.3.3. 行为（**Behavior**）

**SW-Component 模板应支持行为的描述（**The SW-Component template shall support description of the behavior**）**

| 描述 | SW-Component 模板必须允许将软件组件与其行为的形式化描述链接起来。 |
| --- | --- |
| 理由 | 「……只要组件实现相同的逻辑并提供相同的公共通信，它们在理论上就是可交换的……」因此，软件组件的功能/逻辑应当是可描述的。 |
| 用例 | 软件组件的交换/兼容性。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.4. RTE 事件（**RTE Events**）

**SW-Component 模板应允许启用 RTE 特性以获取 Runnable Entity 的激活 RTE 事件（**The SW-Component template shall allow enabling of RTE-Feature to get the activating RTE-Event of Runnable Entity**）**

| 描述 | 软件组件模板应提供请求手段：**RTE** 启用将激活的 **RTE** 事件传递给被调用的 Runnable 实体这一特性。该请求应针对每个 Runnable 实体可用。 |
| --- | --- |
| 理由 | 如果 Runnable 实体的代码不需要 **RTE API**，则它不应可用，并且生成的 **RTE** 不应为该 Runnable 实体跟踪激活的 **RTE** 事件。 |
| 用例 | 某个 Runnable 实体被定义为既由「TimingEvent」激活，也由「DataReceivedEvent」激活。在该 Runnable 实体执行期间，代码需要区分实际触发执行的是哪个激活来源。 |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持实例特定的 RTE 事件（**The SW-Component template shall support instance specific RTE-Events**）**

| 描述 | 软件组件模板应提供描述实例特定 **RTE** 事件的方法。 |
| --- | --- |
| 理由 | 见用例。 |
| 用例 | 组件在不同周期中的复用，即时序事件的执行由控制器的时基针对软件组件的每个实例单独确定。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.5. 可调度性（**Schedulability**）

**SW-Component 模板应支持可调度性的定义（**The SW-Component template shall support the definition of schedulability**）**

| 描述 | SW-Component 模板必须包含足够的信息（在组件能够提供的范围内），用于生成运行环境以及将多个软件组件集成到一个 **ECU** 或联网的多个 **ECU** 上。 |
| --- | --- |
| 理由 | 信息必须足以支持组件的调度。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_00090 |
| 支撑材料 | - |

#### 2.3.6. Runnable 实体（**Runnable Entities**）

**SW-Component 模板应支持 RunnableEntity 内独占区使用的可选配置（**The SW-Component template shall support optional configuration of ExclusiveArea usage within RunnableEntities**）**

| 描述 | 软件组件配置应支持为每个实现的 RunnableEntity 规定可选的配置信息，以描述：<br>* 该实体以嵌套方式使用了哪些独占区（**ExclusiveArea**）<br>* 在某个独占区或嵌套独占区内调用了哪些其他 RunnableEntity |
| --- | --- |
| 理由 | 附加的配置信息可以在配置阶段由工具检查。其目标是通过在资源共享于不同 RunnableEntity 之间可能出现冲突时向实现者发出警告来防止死锁。 |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

**软件组件模板应支持隐式通信行为的定义（**The Software Component Template shall support the definition of implicit communication behavior**）**

| 描述 | 软件组件模板应支持交换用于按照软件组件的需求配置 **RTE** 隐式通信行为的支持信息。该信息可以在原子软件组件设计时首次定义，也可以在创建组合时添加。例如，若干原子软件组件的 Runnable 实体通常期望数据稳定（**stable data**）。 |
| --- | --- |
| 理由 | 确保软件组件正确的环境行为。 |
| 用例 | 这在概念上可以归结为两个基本用例：<br>* 一组 Runnable 实体执行期间的数据稳定<br>* 一组数据原型（**Data Prototype**）的一致性数据消费与传播 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.7. 所需和可用的传感器与执行器（**Needed and usable sensors and actuators**）

**SW-Component 模板应支持所需和可用的传感器与执行器的定义（**The SW-Component template shall support the definition of needed and usable sensors and actuators**）**

| 描述 | SW-Component 模板必须允许：<br>* 列出所需的传感器/执行器<br>* 枚举可以使用的传感器/执行器<br>* 为软件组件引用传感器/执行器的外部描述 |
| --- | --- |
| 理由 | - |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.8. 变体（**Variants**）

**SW-Component 模板应支持变体处理（**The SW-Component template shall support variant handling**）**

| 描述 | SW-Component 模板必须允许规定软件组件的不同变体，例如软件配置。 |
| --- | --- |
| 理由 | - |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.9. 模式（**Modes**）

**SW-Component 模板应支持模式（**The SW-Component template shall support modes**）**

| 描述 | SW-Component 模板必须提供一些简单的方法来定义模式。模式的名称是必须提供的最重要属性。 |
| --- | --- |
| 理由 | 从软件组件的角度来看，假设状态管理器（**State Manager**）使用标准化的 **AUTOSAR** 接口来影响软件组件，并向软件组件提供获取请求和确认的接口。 |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持模式声明的映射（**The SW-Component template shall support mapping of mode declarations**）**

| 描述 | 软件组件模板应支持模式声明（**Mode Declaration**）的映射。 |
| --- | --- |
| 理由 | 见用例。 |
| 用例 | 接收软件组件必须连接到一个模式管理器，后者提供的 ModeDeclarationGroup 所包含的 ModeDeclaration 与用户的不同。 |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持对模式的依赖（**The SW-Component template shall support dependency on modes**）**

| 描述 | SW-Component 必须提供一个矩阵，根据来自状态管理器的模式，使 runnable 实体和端口被启用或禁用。 |
| --- | --- |
| 理由 | 软件组件可以因状态管理器提供的不同模式而改变其活动接口。诊断模式下的通信行为可能与正常运行模式下不同。 |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持使软件组件能够请求专用模式（**The SW-Component template shall support enabling SWCs to request dedicated modes**）**

| 描述 | 如果经过配置，在一个 **ECU** 上的一个或多个 **ECU** 上，软件组件可以请求一个模式。模式请求被传播到一个特定的功能，该功能负责根据收到的模式请求控制受影响的 **BSW**。 |
| --- | --- |
| 理由 | 参见「整车与应用模式管理概念（**Vehicle and Application Mode Management Concept**）」。 |
| 用例 | 需要根据模式信息控制基础软件和 runnable 执行的用例。 |
| 依赖项 | RS\_SWCT\_03200 |
| 支撑材料 | - |

**SW-Component 模板应支持模式信息的传播（**The SW-Component template shall support propagation of mode information**）**

| 描述 | 一个模式可以影响位于多个 **ECU** 上的软件组件。因此，必须通过配置将模式信息传播到多个 **ECU**。 |
| --- | --- |
| 理由 | 参见「整车与应用模式管理概念」。 |
| 用例 | 所有需要控制基础软件和 runnable 控制的用例。 |
| 依赖项 | RS\_SWCT\_03200 |
| 支撑材料 | - |

#### 2.3.10. PortInterface 之间的连接（**Connections between PortInterfaces**）

**SW-Component 模板应支持 PortInterface 之间的连接（**The SW-Component template shall support connections between PortInterfaces**）**

| 描述 | 软件组件模板应提供定义兼容 PortInterface 之间连接的方法，而不受 PortInterface 元素名称的影响。 |
| --- | --- |
| 理由 | 支持大型跨公司开发团队之间的协同工作。（短）名称在分布式开发中不一定经过协调定义。但短名称与软件组件的实现相关，不应仅为定义连接而更改。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_00200 |
| 支撑材料 | - |

**SW-Component 模板应支持记录类型的子集化（**The SW-Component template shall support record type subsetting**）**

| 描述 | 软件组件模板应支持这样的端口连接：端口由不同的接口定义类型，提供端口的元素由复合数据类型定义类型，其复合元素映射到需求端口的元素。此时需求端口可以只包含提供端口所包含元素的一个子集。 |
| --- | --- |
| 理由 | 由于以一致的方式处理数据需要使用记录类型，应允许 RecordType 的接收方只接收所发送记录数据元素的一个子集，因为不同的接收方确实需要所提供数据的不同子集。 |
| 用例 | 4 个轮速信号和运动方向信号在一个记录中提供。如果某个接收方只关心运动方向信息，则该记录中的所有其他信息在该特定接收方处都不必被考虑。 |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持带原始类型的记录类型子集化（**The SW-Component template shall support record type subsetting with primitive types**）**

| 描述 | 软件组件模板应支持这样的端口连接：端口由不同的接口定义类型，提供端口的元素由复合数据类型定义类型，而需求端口的元素由原始类型定义类型。 |
| --- | --- |
| 理由 | 见 RS\_SWCT\_03135。 |
| 用例 | 见 RS\_SWCT\_03135。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.11. 变体处理引起的原型条件性存在（**Conditional existence of Prototypes due to variant handling**）

**SW-Component 模板应支持 PortPrototype 的条件性存在（**The SW-Component template shall support conditional existence of PortPrototypes**）**

| 描述 | **AUTOSAR** 元模型应支持条件性存在的 PortPrototype 的描述。 |
| --- | --- |
| 理由 | 条件数据流取决于系统配置。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

**SW-Component 模板应支持接口中数据元素原型、操作原型和参数原型的条件性存在（**The SW-Component template shall support the conditional existence of data element prototypes, operation prototypes and parameter prototypes in interfaces**）**

| 描述 | SWCT 应支持描述接口中数据元素原型、操作原型和参数原型的条件性存在。 |
| --- | --- |
| 理由 | 条件数据、服务和标定特性因系统配置而异。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

**SW-Component 模板应支持 ComponentPrototype 的条件性存在（**The SW-Component template shall support the conditional existence of ComponentPrototypes**）**

| 描述 | SWCT 应支持描述 ComponentPrototype 的条件性存在。 |
| --- | --- |
| 理由 | ComponentPrototype 的条件使用取决于系统配置。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

**SW-Component 模板应支持 ConnectorPrototype 的条件性存在（**The SW-Component template shall support the conditional existence of ConnectorPrototypes**）**

| 描述 | SWCT 应支持描述 ConnectorPrototype 的条件性存在。 |
| --- | --- |
| 理由 | 条件使用取决于系统配置。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.12. 数组大小的可配置性（**Configurable size of Arrays**）

**SW-Component 模板应支持数组大小的可配置性（**The SW-Component template shall support a configurable size of arrays**）**

| 描述 | SWCT 应支持数组大小的可配置性（maxNumberOfElements）。 |
| --- | --- |
| 理由 | 将接口智能化地适配到既有系统部件的数量。 |
| 用例 | 将接口适配到可配置的气缸数量或气缸排数量。 |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.13. 属性 swMinAxisPoints 和 swMaxAxisPoints 应可通过系统常量定义进行调整（**Attributes swMinAxisPoints and swMaxAxisPoints shall be adjustable by an System Constant Definition**）

**属性 swMinAxisPoints 和 swMaxAxisPoints 应可通过系统常量定义进行调整（**Attributes swMinAxisPoints and swMaxAxisPoints shall be adjustable by an System Constant Definition**）**

| 描述 | 属性 swMinAxisPoints 和 swMaxAxisPoints 应可通过系统常量定义（**System Constant Definition**）进行调整。 |
| --- | --- |
| 理由 | 将标定轴适配到可配置的气缸数量或气缸排数量。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.14. RunnableEntity 的条件性存在（**Conditional existence of RunnableEntitys**）

**SW-Component 模板应支持 RunnableEntity 的条件性存在（**The SW-Component template shall support the conditional existence of RunnableEntitys**）**

| 描述 | SWCT 应支持描述 RunnableEntity 的条件性存在。 |
| --- | --- |
| 理由 | 依据系统配置对算法进行适配。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.15. RTEEvent 的条件性存在（**Conditional existence of RTEEvents**）

**SW-Component 模板应支持 RTEEvent 的条件性存在（**The SW-Component template shall support the conditional existence of RTEEvents**）**

| 描述 | SWCT 应支持描述 RTEEvent 的条件性存在。 |
| --- | --- |
| 理由 | 依据系统配置对算法进行适配。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.16. InterRunnableVariable 的条件性存在（**Conditional existence of InterRunnableVariables**）

**SW-Component 模板应支持 InterRunnableVariable 的条件性存在（**The SW-Component template shall support the conditional existence of InterRunnableVariables**）**

| 描述 | SWCT 应支持描述条件性存在的 InterRunnableVariable。 |
| --- | --- |
| 理由 | 依据系统配置对算法进行适配。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.17. 测量的条件性可访问性（**Conditional accessibility for measurement**）

**SW-Component 模板应支持测量的条件性可访问性（**The SW-Component template shall support the conditional accessibility for measurement**）**

| 描述 | SWCT 应支持描述对外部测量工具的条件性可访问性。 |
| --- | --- |
| 理由 | 在后续开发步骤中关闭元素的可测量性能力，以优化资源。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.18. 参数原型的条件性存在（**Conditional existence of parameter prototypes**）

**SW-Component 模板应支持参数原型的条件性存在（**The SW-Component template shall support the conditional existence of parameter prototypes**）**

| 描述 | SWCT 应支持描述条件性存在的参数原型（**parameter prototype**）。 |
| --- | --- |
| 理由 | 依据系统配置对算法进行适配。 |
| 用例 | - |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.19. 支持 SW-C 的条件端口（**Support of conditional ports for SW-C**）

**SW-Component 模板应支持软件组件的条件端口（**The SW-Component template shall support conditional ports for software components**）**

| 描述 | 如果某个特定软件组件可用，则其接口必须实现，即它是一个核心（**core**）接口；这类元素的存在仅取决于车辆配置。<br>* 与软件组件关联的一个端口被称为提供方（**Provider**）条件端口，如果满足某个条件、且该条件证明相应信息需要由该软件组件发送。这类条件可以是车上存在某个特定软件组件、存在的某个软件组件内存在某个特定功能、特定的安全概念等。此时，该条件必须被精确指示。<br>* 与软件组件关联的一个端口被称为接收方（**Receiver**）条件端口，如果满足某个条件、且该条件证明相应信息需要由该软件组件接收。这类条件可以是该软件组件内存在某个特定功能等。此时，该条件必须被精确指示。 |
| --- | --- |
| 理由 | - |
| 用例 | [VH30] 支持连接名称不同的端口；[VH31] 支持 SW-C 的核心端口。 |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.20. 支持不同分辨率的接口（**Support of Interfaces with different resolutions**）

**SW-Component 模板应支持不同分辨率的接口（**The SW-Component template shall support interfaces with different resolutions**）**

| 描述 | 对主表（**MasterTable**）中的某些信号而言，其分辨率显得过高，尤其在这些信号最终会在 2 个 **ECU** 之间交换的情况下，因为这对通信网络总线而言可能非常占尺寸。 |
| --- | --- |
| 理由 | - |
| 用例 | 某些由 10.2 软件组件发送到 10.3 软件组件的扭矩信号为 22 位。这对 10.3 来说太多了，但同时，该信号很可能在 10.2 内部的 2 个软件组件之间使用，这证明了其 22 位定义的合理性。<br>* 某些 10.3 内部信号（仅在底盘域内由 2 个软件组件交换）对高端车而言分辨率很高，而对更「标准」的车辆而言，更低的分辨率（例如 8 字节而非 16 字节）就「足够」了。由于这种高分辨率会带来额外成本，对这些「标准」车辆不能接受使用这种高分辨率。 |
| 依赖项 | RS\_SWCT\_03100 |
| 支撑材料 | - |

#### 2.3.21. 固定数据交换（**Fixed data exchange**）

**SW-Component 模板应支持固定数据交换（**The SW-Component template shall support fixed data exchange**）**

| 描述 | 固定数据（宏）和标定由唯一的参数接口处理。兼容性规则允许将数据、固定数据、常量、标定和 **NV** 数据互连。现状：不经常变化的固定数据实现为宏；可由标定工程师更改的固定数据实现为 const 标定。 |
| --- | --- |
| 理由 | - |
| 用例 | (RS\_BRF\_00157)<br>* UC2：某个软件组件产生一个在软件组件模板中设置的固定数据<br>* UC3：集成者希望最终确定某个标定参数的取值 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.22. 支持 M2 层级的标定数据集定义（**M2 support for definition of calibration datasets**）

**SW-Component 模板应支持标定数据集的定义（**The SW-Component template shall support the definition of calibration datasets**）**

| 描述 | 需要扩充规定初始取值的通用方法。初始取值的规定可能不应局限于标定参数。也可以考虑 DataElementPrototype 的初始取值。 |
| --- | --- |
| 理由 | - |
| 用例 | UC1：为标定参数类型提供初始取值。为标定过程预定义起始取值。<br>* UC2：为标定参数实例提供初始取值。利用标定过程的结果。<br>* UC3：提供多组初始取值。初始取值通常取自先前的项目。<br>* UC4：在多个域（物理域和编码域）中提供初始取值。允许在不同项目之间传输取值。在项目内保持最高精度。<br>* UC5：支持「变体编码（**Variant coding**）」。「变体编码」为某个特定的标定参数提供多个取值。<br>* UC6：提供与 SWCT 名称相关的初始取值。看来存在各种名称域。为支持一套完整的方法论，初始取值应与 SWCT 名称相关。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.23. 支持 SAE J1939 协议特性（**Support of SAE J1939 Protocol Features**）

**SW-Component 模板应支持 SAE J1939 协议特性（**The SW-Component template shall support SAE J1939 Protocol Features**）**

| 描述 | 所选 **SAE** **J1939** 协议特性的子集，以允许与 **SAE** **J1939** 组件进行正确的通信。 |
| --- | --- |
| 理由 | 所请求的 **SAE** **J1939** 功能子集将支持与 **J1939** 控制器应用（**CA**）的集成和通信。许多卡车 **OEM** 需要维护包含 **SAE** **J1939** 在内的多网络系统。 |
| 用例 | 用例 A：现有的 **SAE** **J1939** 现成（**off-the-shelf**）组件可以集成或复用。<br>* 用例 B：**SAE** **J1939** 协议是许多市场的行业标准。因此，对卡车 **OEM** 而言支持 **J1939** 是强制性的。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.24. 需要对最大尺寸内可变元素数量数组的数据类型与访问支持（**Need data type and access support for arrays of variable number of elements within the maximum size**）

**SW-Component 模板应支持最大尺寸内可变元素数量的数组（**The SW-Component template shall support arrays of variable number of elements within the maximum size**）**

| 描述 | 增加对复杂类型数组的支持，其元素数量可变（0 .. maxNumberOfElements）。包含可变数量数据集的数组，用于访问只有前几个信号真正可用的 **COM** 信号组。 |
| --- | --- |
| 理由 | 见「支持 SAE J1939 协议特性」。 |
| 用例 | 用例：**DM1** 中的信号建模。 |
| 依赖项 | RS\_SWCT\_03180 |
| 支撑材料 | - |

#### 2.3.25. 需要对可变元素数量字节数组的数据类型与访问支持（**Need data type and access support for byte arrays of variable number of elements**）

**SW-Component 模板应支持可变元素数量的字节数组（**The SW-Component template shall support byte arrays of variable number of elements**）**

| 描述 | 增加对原始类型字节数组的支持，其大小可变、无终止符或终止符可配置。其处理方式应可与字符串类比，但不带零终止语义。 |
| --- | --- |
| 理由 | 见「支持 SAE J1939 协议特性」。 |
| 用例 | 例如 **ECUID** 中的信号建模。 |
| 依赖项 | RS\_SWCT\_03180 |
| 支撑材料 | - |

#### 2.3.26. 发布/规定软件组件的诊断能力及其资源的能力（**Ability to publish/specify the diagnostic capabilities and its resources of an SWC**）

**SW-Component 模板应支持发布/规定软件组件的诊断能力及其资源的能力（**The SW-Component template shall support the ability to publish/specify the diagnostic capabilities and its resources of an SWC**）**

| 描述 | 软件组件设计者需要能够发布并规定诊断能力及其资源（例如端口、数据元素、服务需求等）的关系。这些诊断能力涵盖以下方面：<br>* 某个信号的当前取值（在 **AUTOSAR** 中表示为 VariableDataPrototype）——诊断测试仪只读访问<br>* 某个 IO 信号的 IO 控制（例如在传感器/执行器软件组件中）——诊断测试仪读取与控制访问<br>* 参数（表示为 ParameterDataPrototype，例如标定参数）——诊断测试仪读写访问<br>* 诊断例程（**DiagnosticRoutine**）——诊断测试仪 RoutineControl 访问<br>* 诊断监视器（表示 **DTC**/事件的检测） |
| --- | --- |
| 理由 | - |
| 用例 | 软件组件设计者应能够发布/规定诊断能力及其资源（例如端口、数据元素、服务需求等）。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.27. 增加对整车与应用模式管理概念的支持（**Add support for Vehicle and Application Mode Management Concept**）

**SW-Component 模板应支持整车与应用模式管理（**The SW-Component template shall support vehicle and application mode management**）**

| 描述 | 软件组件模板受到以下特性的影响：<br>* PortGroup 应表示 **VFB** 中通信管理使用者的概念，并应用于将一个软件组件中被同一功能所需的端口分组。这些端口在逻辑上是一个通信使用者。一个 PortGroup 应作为一个使用者与通信管理（**COMM**）通信。<br>* 使软件组件能够请求专用模式<br>* 模式信息的传播<br>每个特性创建一个子需求。 |
| --- | --- |
| 理由 | 参见「整车与应用模式管理概念」。 |
| 用例 | 参见「整车与应用模式管理概念」。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.28. 增加对端口组的支持（**Add support for Portgroups**）

**SW-Component 模板应支持端口组（**The SW-Component template shall support Portgroups**）**

| 描述 | PortGroup 应表示 **VFB**（内部行为）中通信管理使用者的概念，并应用于将一个软件组件中被同一功能所需的端口分组。这些端口在逻辑上是一个通信使用者。一个 PortGroup 应作为一个使用者与通信管理（**COMM**）通信。 |
| --- | --- |
| 理由 | 参见「整车与应用模式管理概念」。 |
| 用例 | 常见的用例是：软件组件的一些端口必须高度可用，而另一些端口只在某些特殊功能时才需要。这可以通过将这些端口分组为两个端口组来实现。 |
| 依赖项 | RS\_SWCT\_03200 |
| 支撑材料 | - |

#### 2.3.29. 端口处的完整性与分辨率调整（**Integrity and Scaling at Ports**）

**SW-Component 模板应支持端口处的完整性与分辨率调整（**The SW-Component template shall support integrity and scaling at ports**）**

| 描述 | 规定连接接口不兼容的端口的方法，以及为低带宽 **ECU** 间通信使用较低分辨率数据类型的方法。 |
| --- | --- |
| 理由 | 应能够确保软件组件之间的端口接口转换是一致的。 |
| 用例 | 工程师应能够在无需显式规定转换公式的情况下连接接口不兼容的端口。数据的重新缩放（**re-scaling**）应自动完成。当数据经由 **ECU** 间而非 **ECU** 内通信时，工程师应能够选择替代的数据类型。内部数据类型与网络传输数据类型之间的转换应自动完成。保持重新缩放/转换后数据的完整性。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.30. 需要在实现数据类型之上增加应用数据类型（**Need to add application data type on top of implementation data type**）

**SW-Component 模板应定义在实现数据类型之上增加应用数据类型的需求（**The SW-Component template shall define the need to add application data type on top of implementation data type**）**

| 描述 | 定义两种不同类型的 **AUTOSAR** 数据类型：ApplicationDataType 和 ImplementationDataType。 |
| --- | --- |
| 理由 | 需要重新定义 **AUTOSAR** 中的数据类型概念，以支持在「物理/应用层级」上使用类型，与在「实现层级」上使用类型相区分。 |
| 用例 | 只要涉及「物理」层面，就应使用 ApplicationDataType。ApplicationDataType 不限于物理属性，没有位大小、字节序等。<br>* ImplementationDataType 将数据类型的实现方面（例如指针）形式化。例如调试概念需要它。也可以用于规定数据映射。软件组件在适用时可以混合使用 ApplicationDataType 和 ImplementationDataType。 |
| 依赖项 | RS\_SWCT\_00070、RS\_SWCT\_00080 |
| 支撑材料 | - |

#### 2.3.31. 应用数据类型（**Application data type**）

**SW-Component 模板应支持应用数据类型（**The SW-Component template shall support application data type**）**

| 描述 | 应可以完全用应用类型对一个（不带服务的）**VFB** 系统建模。<br>* 应用类型用于检查接口兼容性。<br>* 应用类型用于从应用角度描述语义（单位、compuMethod、名称）以及数据结构。 |
| --- | --- |
| 理由 | 见 RS\_SWCT\_03215。 |
| 用例 | 见 RS\_SWCT\_03215。 |
| 依赖项 | RS\_SWCT\_03215 |
| 支撑材料 | 见 RS\_SWCT\_03215。 |

#### 2.3.32. 实现数据类型（**Implementation data type**）

**SW-Component 模板应支持实现数据类型（**The SW-Component template shall support implementation data type**）**

| 描述 | 实现类型表示软件组件与 **RTE** 之间通信的数据类型。<br>* 应可以仅用实现类型对所有服务接口（**Service Interface**）建模。<br>* 应可以用实现类型对 **AR** 调试变量建模。<br>* 应可以在端口接口中使用实现类型而无需应用类型。<br>* 应可以用实现类型对所有 **BSW** 接口建模。<br>* 一个实现类型可以独立于任何应用类型加以规定。 |
| --- | --- |
| 理由 | 见 RS\_SWCT\_03215。 |
| 用例 | 见 RS\_SWCT\_03215。 |
| 依赖项 | RS\_SWCT\_03215 |
| 支撑材料 | 见 RS\_SWCT\_03215。 |

#### 2.3.33. 用于原始数据映射的数据类型（**Data Types for Primitive Data Mapping**）

**SW-Component 模板应支持用于原始数据映射的数据类型（**The SW-Component template shall support data types for primitive data mapping**）**

| 描述 | 软件组件模板应提供定义「可用于原始数据映射（**Primitive Data Mapping**）的数据类型」之判据的方法。该判据应为 ApplicationDataType 和 ImplementationDataType 定义。 |
| --- | --- |
| 理由 | 系统模板允许对满足 **UINT8** 数组判据的数组进行原始数据映射。遗憾的是，目前没有定义哪些判据使应用数据类型或实现数据类型与 **UINT8** 数组兼容。 |
| 用例 | 见理由。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.34. 允许组合上的通信属性（**Allow Communication Attributes on Compositions**）

**SW-Component 模板应允许组合上的通信属性（**The SW-Component template shall allow communication attributes on compositions**）**

| 描述 | 规定连接接口不兼容的端口的方法，以及为低带宽 **ECU** 间通信使用较低分辨率数据类型的方法。 |
| --- | --- |
| 理由 | 允许交换包含空组合、但仍描述通信属性的软件组件描述。 |
| 用例 | 今天（**AR** rel. 3.1）禁止将 ComSpec 附加到属于 CompositionType 的 PortPrototype。在并非要交换系统完整信息的用例中（例如 **OEM** 提供软件部分——尤其是通信相关部分——的描述，而供应商在 **OEM** 提供的预定义容器中引入其原子软件组件），这是一个很强的限制。即使尚无 AtomicSoftwareComponentType，也应能够传输对 ComSpec 的需求。当实际的 AtomicSoftwareComponentType 被添加时，ComSpec 应被（手动或由工具支持地）附加到该 AtomicSoftwareComponentType 的 PortPrototype 上。**RTE** 生成应只考虑 AtomicSoftwareComponentType 的 PortPrototype 上的 ComSpec。 |
| 依赖项 | RS\_SWCT\_00160 |
| 支撑材料 | - |

#### 2.3.35. 允许端口特定的数据转换属性配置（**Allow Port Specific Configuration of Data Transformation Properties**）

**SW-Component 模板应允许端口特定的数据转换属性配置（**The SW-Component template shall allow port specific configuration of data transformation properties**）**

| 描述 | SW-Component 模板应允许端口特定的数据转换属性配置，这些属性规定用于 **ECU** 间通信的转换器（**transformer**）的属性。 |
| --- | --- |
| 理由 | 用于 **ECU** 间通信的转换器的某些属性不是信号特定而是端口特定的。 |
| 用例 | 同一安全相关信号被一个 **ECU** 内的两个软件组件接收。这两个软件组件具有不同的安全需求和不同的验收判据。该信号对一个软件组件可能不安全，但对另一个软件组件仍然安全。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.36. 数据转换的错误通知（**Error notification of data transformation**）

**SW-Component 模板应支持转换后数据通信的错误通知（**The SW-Component template shall support error notification for transformed data communication**）**

| 描述 | 软件组件模板应提供配置数据转换错误通知的方法。 |
| --- | --- |
| 理由 | 软件组件可能希望对转换错误做出反应。 |
| 用例 | 安全相关软件组件对转换中安全检查期间的错误做出反应。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.37. 增强非易失性（NV）存储器接口（**Enhancing the Non-Volatile (NV) memory interface**）

**SW-Component 模板应支持增强的非易失性（NV）存储器接口（**The SW-Component template shall support an enhanced non-volatile (NV) memory interface**）**

| 描述 | 规定定义和配置一个 NvBlockComponent 的方法，使一个 **ECU** 中的所有软件组件都能用它访问 **NvData**。 |
| --- | --- |
| 理由 | 通过定义一个带有发送者-接收者接口、并提供给各软件组件的 NvBlockComponent 来确保数据一致性。通过使用一个公共的 NvBlockComponent，每个软件组件中保存 **NvData** **RAM** 副本所需的 **RAM** 量得以减少。 |
| 用例 | **Nv** 存储器情形涉及提供一个可被许多软件组件用作 **Nv** 存储器接口的 NvBlockComponent。这个公共的 **Nv** 存储器接口可以确保 **ECU**。 |
| 依赖项 | RS\_SWCT\_00030、RS\_SWCT\_00070 |
| 支撑材料 | - |

#### 2.3.38. M1 产物的文档化（**Documentation of M1 artifacts**）

**SW-Component 模板应支持 M1 产物的文档化（**The SW-Component template shall support documentation of M1 artifacts**）**

| 描述 | 规定能够为 **M1** 产物提供文档的方法，该文档支持：<br>* 结构化（例如段落、列表、交叉引用）<br>* 内容聚焦<br>* 文档部分的验证与识别 |
| --- | --- |
| 理由 | 增加这一能力将带来：<br>* 利益相关方之间更高效的文档信息交换<br>* 对 **M1** 产物更精确、更清晰的文档<br>* 新团队成员更容易、更快速地融入产物工作<br>* 对 **M1** 产物文档更高效的维护 |
| 用例 | **OEM** 或供应商需要能够为 **M1** 产物提供更高效、更精确、更清晰的文档。 |
| 依赖项 | RS\_SWCT\_02110、RS\_SWCT\_02060 |
| 支撑材料 | - |

#### 2.3.39. 支持端到端通信保护（**Support end-to-end communication protection**）

**SW-Component 模板应支持端到端通信保护（**The SW-Component template shall support end-to-end communication protection**）**

| 描述 | 应可以为特定的通信路径（在 **ECU** 的上下文中）分配唯一的数据 ID，并且还应支持选择 **E2E** 配置文件 ID（**E2E Profile ID**）。 |
| --- | --- |
| 理由 | 增加这些属性将支持软件组件之间受保护的端到端通信。 |
| 用例 | **OEM** 或供应商需要能够规定软件组件之间受保护的端到端通信。 |
| 依赖项 | RS\_SWCT\_00010 |
| 支撑材料 | **AUTOSAR** 中端到端保护的细节在 [\[6\]](#ref-6) 中描述。 |

#### 2.3.40. 局部网络（**Partial Networking**）

**SW-Component 模板应支持局部网络（**The SW-Component template shall support partial networking**）**

| 描述 | 软件组件模板应支持虚拟功能簇（**Virtual Function Cluster**，**VFC**）的定义。 |
| --- | --- |
| 理由 | 局部网络通过 **VFB** 层级上的虚拟功能簇（**VFC**）得到支持。 |
| 用例 | 一个 **VFC** 定义参与局部网络通信的所有端口。某些端口控制 **VFC** 行为，其他端口读取 **VFC** 当前状态并做出反应。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.41. 双向通信（**Bidirectional communication**）

**SW-Component 模板应支持双向通信（**The SW-Component template shall support bidirectional communication**）**

| 描述 | 软件组件模板应支持表达需求端口与提供端口组合语义的端口。这类端口应支持本软件组件：<br>* 可以对同一数据元素进行读写访问<br>* 可以调用自身的服务器 runnable<br>* 可以在模式切换时触发自身 runnable<br>* 可以触发自身 runnable<br>此外，如果这类「需求并提供」端口连接到具有提供、需求或「需求并提供」语义的其他端口，则双向数据流应成为可能。 |
| --- | --- |
| 理由 | 既需要产生的数据又需要输入的软件算法。NvBlockComponent 通常提供对同一数据的读写访问。 |
| 用例 | 某个软件组件产生一个数据，而该数据同时也是自身算法下一次迭代的输入。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.42. 数据的初始化（**Initialization of Data**）

**SW-Component 模板应支持基于规则的数组初始化（**The SW-Component template shall support rule-based initialization of arrays**）**

| 描述 | 软件组件模板应提供为数组性质数据类型的 DataPrototype 定义基于规则的初始化的方法。 |
| --- | --- |
| 理由 | DataPrototype 可能需要大量的初始化数据（以 **AUTOSAR** XML 计）。通过基于规则的数组初始化可以改善这一点。 |
| 用例 | 例如，一个具有 100 个元素的 ApplicationArrayDataType 需要初始化，使得每个元素都有专门的初始取值。在最常见的情况下，这些元素中的大多数以相同的取值（例如 0）初始化，只有前几个元素在初始取值上不同。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.43. 实例特定的时序（**Instance specific timing**）

**SW-Component 模板应支持在实例层级覆盖激活周期时间（**The SW-Component template shall support overriding the activation period time on instance level**）**

| 描述 | 软件组件模板应支持为软件组件的特定实例覆盖时间周期性 runnable 实体激活的适用周期。 |
| --- | --- |
| 理由 | 支持具有不同时基的闭环控制器。 |
| 用例 | 组件在不同时间栅格中的复用。例如，可能存在一个提供闭环控制器的组件。该组件可以应用于慢速和快速控制路径。由于控制器的时基源自调度，应当可以在实例层级上规定它。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.44. 快速原型支持（**Rapid Prototyping support**）

**SW-Component 模板应支持旁路点和旁路场景的描述（**The SW-Component template shall support the description of bypass points and bypass scenarios**）**

| 描述 | 软件组件模板应支持在软件组件层级描述旁路点（**bypass point**）和旁路场景（**bypass scenario**）。旁路包括为测试或快速原型目的读取/修改/写入数据。旁路点是逻辑数据流中可以实现旁路的位置。旁路场景由旁路点组成，表示旁路点之间的旁路数据流。 |
| --- | --- |
| 理由 | 支持 **OEM** 与 **ECU** 供应商之间旁路需求的交换。支持旁路配置在不同项目以及不同旁路工具之间的复用。 |
| 用例 | **OEM** 向 **ECU** 供应商提供该 **ECU** 应支持的旁路点的描述。**ECU** 供应商配置 **ECU** 以支持这些旁路点，并向 **OEM** 交付 **ECU** 和一个旁路工具。**OEM** 基于 **ECU** 中可用的旁路点向旁路工具提供旁路场景的描述。旁路工具与 **ECU** 交互以实现旁路场景。 |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持用于快速原型的 post-build 挂钩工具（**The SW-Component template shall support post-build hooking tools for rapid prototyping**）**

| 描述 | 软件组件模板应通过规定所需的快速原型存储器接口，支持用于快速原型的 post-build 挂钩工具。快速原型存储器接口强制一种代码生成策略，该策略包含一个写-读周期，为快速原型工具提供一个无歧义的、可以在其中修改后续使用取值的位置。 |
| --- | --- |
| 理由 | 为支持 post-build 挂钩的使用，软件组件必须包含对快速原型存储器接口的使用。 |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

**SW-Component 模板应支持服务点和快速原型场景的描述（**The SW-Component template shall support the description of service points and rapid prototyping scenarios**）**

| 描述 | 软件组件模板应支持在软件组件内 **RTE** 事件层级描述服务点（**service point**）及相关联的快速原型场景。服务点是调用一个或多个由快速原型服务组件提供的快速原型服务函数的位置。快速原型服务函数是对快速原型服务组件所提供函数的调用，其中数据被采样和/或激励。快速原型服务组件是提供快速原型服务的 **AUTOSAR** 或供应商特定 **BSW** 模块。快速原型场景由服务点组成，表示服务点之间的数据流。 |
| --- | --- |
| 理由 | 为支持基于服务的旁路的使用，软件组件必须包含手动分配的服务点，这些服务点必须在 **SWCT** 中记录。 |
| 用例 | **OEM** 向 **ECU** 供应商提供该 **ECU** 应为某个软件组件支持的服务点的描述。**ECU** 供应商配置 **ECU** 以支持这些服务点，并向 **OEM** 交付 **ECU** 和一个服务组件。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.45. Runnable 的初始化（**Initialization of Runnables**）

**SW-Component 模板应支持在不使用模式管理的情况下初始化 runnable（**The SW-Component template shall support the initialization of runnables without usage of mode management**）**

| 描述 | 软件组件模板应提供定义一种不使用 **AUTOSAR** 模式管理特性的 runnable 初始化机制的方法。 |
| --- | --- |
| 理由 | 该需求已由工具供应商实现，而未经 **AUTOSAR** 标准化。 |
| 用例 | 函数开发者交付一组 runnable，其中一些是为初始化目的而创建的。这应在不使用 **AUTOSAR** 模式管理特性的情况下描述，因为那会为这种简单的情形引入新的复杂度层级。 |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.46. 基于 IP 的诊断（**Diagnostics over IP**）

**SW-Component 模板应支持基于 IP 的诊断（**The SW-Component template shall support Diagnostics over IP**）**

| 描述 | 软件组件模板应提供为基于 **IP** 的诊断定义服务需求（**service need**）的方法。 |
| --- | --- |
| 理由 | - |
| 用例 | - |
| 依赖项 | - |
| 支撑材料 | - |

#### 2.3.47. 可选元素（**Optional Elements**）

**SW-Component 模板应支持通信的可选元素的定义（**The SW-Component template shall support the definition of optional elements for communication**）**

| 描述 | 软件组件模板应提供在用于 **VFB** 上通信的数据结构中定义可选元素的方法。 |
| --- | --- |
| 理由 | 复合数据结构中可选元素的存在，在语义上不同于「接收方在收到的信息不包含复合数据结构的相应子元素时简单地采用初始值」。接收方应主动确认某些信息缺失这一事实，并仍能有意义地处理这种情况。 |
| 用例 | 定义一个复合数据结构并将其用于 **VFB** 上的通信。该数据结构的设计已经预见了这样的可能性：在任何给定时刻，该数据结构可能只被有意义的信息部分填充。 |
| 依赖项 | - |
| 支撑材料 | - |

## 3. 可追溯项变更历史

### 3.1. 本文档按 AUTOSAR 发布版 R4.0.1 的可追溯项历史

#### 3.1.1. 新增的规范项

表3.1：R4.0.1 中新增的规范项

| 标题 |
| --- |
| AUTOSAR 应支持高可靠性的 ECU 间与 ECU 内通信机制 |
| AUTOSAR 应为 ECU 内和 ECU 间通信提供开放且标准化的软件接口 |
| AUTOSAR 应向应用软件和基础软件模块提供完整的接口 |
| AUTOSAR 应便于软件及其概念与实现的复用 |
| AUTOSAR 应提供适用于不同功能域的软件架构 |
| AUTOSAR 应提供应用软件对硬件的抽象 |
| AUTOSAR 应提供应用软件对车载通信技术的独立性 |
| AUTOSAR 应提供应用软件对操作系统的独立性 |
| AUTOSAR 应提供整个系统的功能接口视图 |
| AUTOSAR 应通过基础设施中的适当服务提供软件的保护/解锁机制 |
| AUTOSAR 应提供与传统软件的互操作性 |
| AUTOSAR 应提供保护软件组件免受恶意软件组件侵害的方法 |
| AUTOSAR 应提供实现可组合性的方法 |
| AUTOSAR 应提供运行期间、生产和售后服务用途的诊断手段 |
| AUTOSAR 应支持层次化设计方法 |
| 软件组件之间的关系定义是穷尽且形式化的 |
| 软件组件受到保护、免遭非法访问 |
| AUTOSAR 支持车辆多样性的管理 |
| 自顶向下的层次化设计 |
| 原子软件组件的接口 |
| 组合类型（CompositionTypes）的自底向上设计 |
| 通信的规定 |
| 软件组件描述的时序资源的规定 |
| 考虑与基础软件的交互 |
| 设计传感器执行器组件 |
| RunnableEntity 之间通信的数据一致性 |
| 物理单位的定义 |
| 注释的定义 |
| PortInterface 之间的连接 |
| PortPrototype 的条件性存在 |
| 接口中数据元素原型、操作原型、参数原型的条件性存在 |
| ComponentPrototype 的条件性存在 |
| ConnectorPrototype 的条件性存在 |
| 数组大小的可配置性 |
| 描述软件组件类型的系统常量取值的受支持组合 |
| 描述内部行为（InternalBehavior）的系统常量取值的受支持组合 |
| 描述实现（Implementation）的系统常量取值的受支持组合 |
| 属性 swMinAxisPoints 和 swMaxAxisPoints 应可通过系统常量定义进行调整 |
| RunnableEntity 的条件性存在 |
| RTEEvent 的条件性存在 |
| InterRunnableVariable 的条件性存在 |
| 测量的条件性可访问性 |
| 参数原型的条件性存在 |
| 支持 SW-C 的条件端口 |
| 支持不同分辨率的接口 |
| 固定数据交换 |
| 支持 M2 层级的标定数据集定义 |
| 支持 SAE J1939 协议特性 |
| 需要对最大尺寸内可变元素数量数组的数据类型与访问支持 |
| 需要对可变元素数量字节数组的数据类型与访问支持 |
| 发布/规定软件组件的诊断能力及其资源的能力 |
| 增加对整车与应用模式管理概念的支持 |
| 增加对端口组的支持 |
| 使软件组件能够请求专用模式 |
| 模式信息的传播 |
| 端口处的完整性与分辨率调整 |
| 需要在实现数据类型之上增加应用数据类型 |
| 应用数据类型 |
| 实现数据类型 |
| 允许组合上的通信属性 |
| 增强非易失性（NV）存储器接口 |
| M1 产物的文档化 |
| 支持端到端通信保护 |

#### 3.1.2. 变更的规范项

无

#### 3.1.3. 删除的规范项

无

### 3.2. 本文档按 AUTOSAR 发布版 R4.0.2 的可追溯项历史

#### 3.2.1. 新增的规范项

无

#### 3.2.2. 变更的规范项

无

#### 3.2.3. 删除的规范项

无

### 3.3. 本文档按 AUTOSAR 发布版 R4.0.3 的可追溯项历史

#### 3.3.1. 新增的规范项

表3.2：R4.0.3 中新增的规范项

| 标题 |
| --- |
| 记录类型的子集化 |
| 带原始类型的记录类型子集化 |
| 支持局部网络 |

#### 3.3.2. 变更的规范项

无

#### 3.3.3. 删除的规范项

无

### 3.4. 本文档按 AUTOSAR 发布版 R4.1.1 的可追溯项历史

#### 3.4.1. 新增的规范项

表3.3：R4.1.1 中新增的规范项

| 标题 |
| --- |
| SW-Component 模板应允许启用 RTE 特性以获取 Runnable Entity 的激活 RTE 事件 |
| SW-Component 模板应支持实例特定的 RTE 事件 |
| SW-Component 模板应支持 RunnableEntity 内独占区使用的可选配置 |
| SW-Component 模板应支持隐式通信行为的定义 |
| SW-Component 模板应支持模式声明的映射 |
| SW-Component 模板应支持用于原始数据映射的数据类型 |
| SW-Component 模板应支持双向通信 |
| SW-Component 模板应支持基于规则的数组初始化 |
| SW-Component 模板应支持在实例层级覆盖激活周期时间 |
| SW-Component 模板应支持旁路点和旁路场景的描述 |
| SW-Component 模板应支持在不使用模式管理的情况下初始化 runnable |
| SW-Component 模板应支持基于 IP 的诊断 |

#### 3.4.2. 变更的规范项

无

#### 3.4.3. 删除的规范项

表3.4：R4.1.1 中删除的规范项

| 标题 |
| --- |
| AUTOSAR 应便于软件及其概念与实现的复用 |
| AUTOSAR 应提供适用于不同功能域的软件架构 |
| AUTOSAR 应提供与传统软件的互操作性 |
| 软件组件描述的时序资源的规定 |
| 库 |
| 目标码层级的集成 |
| runnable 实体的执行顺序 |
| 软件组件所需的资源 |
| 软件组件的时序需求 |
| 描述软件组件类型的系统常量取值的受支持组合 |
| 描述内部行为（InternalBehavior）的系统常量取值的受支持组合 |
| 描述实现（Implementation）的系统常量取值的受支持组合 |

### 3.5. 本文档按 AUTOSAR 发布版 R4.1.2 的可追溯项历史

#### 3.5.1. 新增的规范项

无

#### 3.5.2. 变更的规范项

无

#### 3.5.3. 删除的规范项

无

### 3.6. 本文档按 AUTOSAR 发布版 R4.2.1 的可追溯项历史

#### 3.6.1. 新增的规范项

表3.5：R4.2.1 中新增的规范项

| 标题 |
| --- |
| 软件组件模板应提供定义公共符号命名约定的能力 |
| SW-Component 模板应允许端口特定的数据转换属性配置 |
| SW-Component 模板应支持转换后数据通信的错误通知 |

#### 3.6.2. 变更的规范项

无

#### 3.6.3. 删除的规范项

无

### 3.7. 本文档按 AUTOSAR 发布版 R4.2.2 的可追溯项历史

无

### 3.8. 本文档按 AUTOSAR 发布版 R4.3.0 的可追溯项历史

#### 3.8.1. 新增的规范项

表3.6：R4.3.0 中新增的规范项

| 标题 |
| --- |
| SW-Component 模板应支持用于快速原型的 post-build 挂钩工具 |
| SW-Component 模板应支持服务点和快速原型场景的描述 |

#### 3.8.2. 变更的规范项

无

#### 3.8.3. 删除的规范项

无

### 3.9. 本文档按 AUTOSAR 发布版 R4.3.1 的可追溯项历史

#### 3.9.1. 新增的规范项

无

#### 3.9.2. 变更的规范项

无

#### 3.9.3. 删除的规范项

无

### 3.10. 本文档按 AUTOSAR 发布版 R4.4.0 的可追溯项历史

#### 3.10.1. 新增的规范项

表3.7：R4.4.0 中新增的规范项

| 标题 |
| --- |
| SW-Component 模板应支持通信的可选元素的定义 |

#### 3.10.2. 变更的规范项

无

#### 3.10.3. 删除的规范项

无

### 3.11. 本文档按 AUTOSAR 发布版 R19-11 的可追溯项历史

#### 3.11.1. 新增的规范项

无

#### 3.11.2. 变更的规范项

表3.8：R19-11 中变更的规范项

| 标题 |
| --- |
| SW-Component 模板应支持通信的可选元素的定义 |

#### 3.11.3. 删除的规范项

无

### 3.12. 本文档按 AUTOSAR 发布版 R20-11 的可追溯项历史

#### 3.12.1. R20-11 中新增的需求

无

#### 3.12.2. R20-11 中变更的需求

无

#### 3.12.3. R20-11 中删除的需求

无

### 3.13. 本文档按 AUTOSAR 发布版 R21-11 的可追溯项历史

#### 3.13.1. R21-11 中新增的需求

无

#### 3.13.2. R21-11 中变更的需求

表3.9：R21-11 中变更的需求

| 标题 |
| --- |
| AUTOSAR 应支持高可靠性的 ECU 间与 ECU 内通信机制 |
| SW-Component 模板应支持隐式通信行为的定义 |

#### 3.13.3. R21-11 中删除的需求

无

### 3.14. 本文档按 AUTOSAR 发布版 R22-11 的可追溯项历史

#### 3.14.1. R22-11 中新增的需求

无

#### 3.14.2. R22-11 中变更的需求

表3.10：R22-11 中变更的需求

| 标题 |
| --- |
| 软件组件模板应支持高可靠性的 ECU 间与 ECU 内通信机制 |
| 软件组件模板应为 ECU 内和 ECU 间通信提供开放且标准化的软件接口 |
| 软件组件模板应向应用软件和基础软件模块提供完整的接口 |
| 软件组件模板应提供应用软件对硬件的抽象 |
| 软件组件模板应提供应用软件对车载通信技术的独立性 |
| 软件组件模板应提供应用软件对操作系统的独立性 |
| 软件组件模板应提供整个系统的功能接口视图 |
| 软件组件模板应通过基础设施中的适当服务提供软件的保护/解锁机制 |
| 软件组件模板应提供保护软件组件免受恶意软件组件侵害的方法 |
| 软件组件模板应提供实现可组合性的方法 |
| 软件组件模板应提供运行期间、生产和售后服务用途的诊断手段 |
| 软件组件模板应支持层次化设计方法 |
| 软件组件模板应支持车辆多样性的管理 |
| 软件组件模板应支持自顶向下的层次化设计 |
| 软件组件模板应支持隐式通信行为的定义 |

#### 3.14.3. R22-11 中删除的需求

无

### 3.15. 本文档按 AUTOSAR 发布版 R23-11 的可追溯项历史

#### 3.15.1. R23-11 中新增的需求

无

#### 3.15.2. R23-11 中变更的需求

无

#### 3.15.3. R23-11 中删除的需求

无
