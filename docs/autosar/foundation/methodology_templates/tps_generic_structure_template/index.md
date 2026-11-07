---
title: "Generic Structure Template（通用结构模板）"
spec: AUTOSAR_FO_TPS_GenericStructureTemplate
release: R23-11
---

<!-- 源文档 AUTOSAR_FO_TPS_GenericStructureTemplate（R23-11），模板规范（TPS），不受 Type A 七章骨架约束；章节编号镜像源文档 References + ch.1–ch.14 + 附录 A–G。
     文档框架信息（封面/状态/变更历史表、Contents、Disclaimer）不译；附录 B（Reference Material）仅含需求可追溯性内容 → 按需求可追溯性可省略集合（STANDARD.md §1，用户决定 2026-10-25）省略（与 tps_standardization_template 附录 A 同型）。
     条目标题中的 [TPS_GST_xxxxx] 编号按批项决策（2026-11-03）丢弃、标题翻译为粗体段；源文自身点名的 ID 保留（正文相互引用的 [TPS_GST_*]、[TPS_STDT_*] 等）；条目 {DRAFT} 生命周期标记以 &#123;DRAFT&#125; 实体呈现以通过 hygiene grep。
     663 个图引用 = 内容图（>30KB 唯一哈希，逐章嵌入为 Figure<N>-<k>.png）+ 页面装饰图（7.9KB 循环条 ×255 等哈希）丢弃。
     源 markdown 转换把类表示例/清单正文以图片或排版文本给出，处理方式逐处注记；分页切断的条目闭合行按上下文合并。 -->

## 参考文献

- <a id="ref-1"></a>[\[1\]](#ref-1) Meta Model — AUTOSAR\_FO\_MMOD\_MetaModel
- <a id="ref-2"></a>[\[2\]](#ref-2) Standardization Template — AUTOSAR\_FO\_TPS\_StandardizationTemplate
- <a id="ref-3"></a>[\[3\]](#ref-3) AUTOSAR XML Schema Production Rules — AUTOSAR\_FO\_TPS\_XMLSchemaProductionRules
- <a id="ref-4"></a>[\[4\]](#ref-4) Specification of ECU Resource Template — AUTOSAR\_CP\_TPS\_ECUResourceTemplate
- <a id="ref-5"></a>[\[5\]](#ref-5) System Template — AUTOSAR\_CP\_TPS\_SystemTemplate
- <a id="ref-6"></a>[\[6\]](#ref-6) Specification of Manifest — AUTOSAR\_AP\_TPS\_ManifestSpecification
- <a id="ref-7"></a>[\[7\]](#ref-7) Standardized M1 Models used for the Definition of AUTOSAR — AUTOSAR\_FO\_MOD\_GeneralDefinitions
- <a id="ref-8"></a>[\[8\]](#ref-8) Predefined Names in AUTOSAR — AUTOSAR\_FO\_TR\_PredefinedNames
- <a id="ref-9"></a>[\[9\]](#ref-9) List of Basic Software Modules — AUTOSAR\_CP\_TR\_BSWModuleList
- <a id="ref-10"></a>[\[10\]](#ref-10) Basic Software Module Description Template — AUTOSAR\_CP\_TPS\_BSWModuleDescriptionTemplate
- <a id="ref-11"></a>[\[11\]](#ref-11) XML Schema 1.0 — <http://www.w3.org/TR/xmlschema-1>
- <a id="ref-12"></a>[\[12\]](#ref-12) ANTLR parser generator V3
- <a id="ref-13"></a>[\[13\]](#ref-13) C++ Operator Precedence — <http://www.cppreference.com/wiki/operator_precedence>
- <a id="ref-14"></a>[\[14\]](#ref-14) Collection of blueprints for AUTOSAR M1 models — AUTOSAR\_FO\_MOD\_GeneralBlueprints
- <a id="ref-15"></a>[\[15\]](#ref-15) Issue Exchange Format V3.0.0 — <http://www.asam.net>
- <a id="ref-16"></a>[\[16\]](#ref-16) Container Catalog XML Model Specification — <http://www.asam.net>
- <a id="ref-17"></a>[\[17\]](#ref-17) ASAM MCD-2 MC (ASAP2 / A2L) — <http://www.asam.net> ASAM\_AE\_MCD-2\_MC\_BS\_V1-7-1.pdf
- <a id="ref-18"></a>[\[18\]](#ref-18) Methodology for Classic Platform — AUTOSAR\_CP\_TR\_Methodology
- <a id="ref-19"></a>[\[19\]](#ref-19) Specification of RTE Software — AUTOSAR\_CP\_SWS\_RTE
- <a id="ref-20"></a>[\[20\]](#ref-20) Software Component Template — AUTOSAR\_CP\_TPS\_SoftwareComponentTemplate
- <a id="ref-21"></a>[\[21\]](#ref-21) Unified Modeling Language:Superstructure, Version 2.0, OMG Available Specification, ptc/05-07-04 — <http://www.omg.org/cgi-bin/apps/doc?formal/05-07-04>
- <a id="ref-22"></a>[\[22\]](#ref-22) ASAM AE Functional Specification Exchange Format V1.0.0 — <http://www.asam.net> AE-FSX\_V1.0.0.pdf
- <a id="ref-23"></a>[\[23\]](#ref-23) OASIS open exchange table model — <http://www.oasis-open.org/specs/tm9901.html>
- <a id="ref-24"></a>[\[24\]](#ref-24) Software Process Engineering Meta-Model Specification — <http://www.omg.org/spec/SPEM/2.0/>

## 1. 简介

本文档给出 AUTOSAR 通用结构模板（**Generic Structure Template**）的规范。实际上，它是 AUTOSAR 元模型 [\[1\]](#ref-1) 所提供形式化定义的补充。换言之，本文档在形式化规范之外，还对 AUTOSAR 元模型中与几乎所有 AUTOSAR 模板相关的部分提供了介绍性描述与设计动机。

尽管如此，本规范的核心部分仍直接基于 AUTOSAR 元模型的内容。因此，本文档包含对 AUTOSAR 元模型主要概念的总结，参见第 1.3 章与第 1.4 章。

本文档提供参考信息，并不要求按顺序阅读。其主要内容如下：

1. 第 3 章解释所有 AUTOSAR 模板共有的顶层结构。
2. 用于设计 AUTOSAR 模板的机制：
   1. 第 2 章描述 AUTOSAR 模板 UML 构造型（profile）中理解各 AUTOSAR 模板文档所必需的关键方面。
   2. 第 4 章描述通用模板类，这些类以类似编译器标准库的方式汇集在一起。
   3. 第 5 章解释带抽象关系的抽象类。这些结构实现了适用于所有 AUTOSAR 模板的特定概念；这些概念通过特化这些抽象类、尤其是特化抽象关系来应用。
   4. 第 6 章总体解释通过模型转换应用的方法论（例如变体处理中所采用的方式）。
3. 设计机制在元模型中的一些具体应用：
   1. 第 7 章描述基于元建模模式（如第 6 章所述）在 AUTOSAR 模板中实现变体处理的方式。
   2. 第 8 章描述可拆分元素（**Splitable** elements）在 AUTOSAR M2 模型中的实现；相应的 AUTOSAR M1 模型视图在 F.2 章中说明。
   3. 第 9 章描述文档支持。

### 1.1. 范围

本文档的范围涵盖理解 AUTOSAR 模板以及定义这些模板所用核心机制所需的信息。

执行模板建模任务所需的 UML 建模方面的内容不在本文档范围之内。

### 1.2. 文档约定

技术术语以等宽字体排版，例如 `PortPrototype`。一般规则是，技术术语的复数形式在单数形式后加 “s”，例如 `PortPrototypes`。借此，本文档的术语风格与 AUTOSAR XML Schema 保持一致。

本文档包含文本形式的约束（**constraint**），它们通过唯一的数值约束 ID、一个标题行以及以约束定界符开始、以结束定界符结束的约束正文与文本其余部分相区分。

这些约束的目的是对 AUTOSAR 元模型的解释作出字面限定，使得在元模型实例（即 M1 层）上检测违反标准化行为的情况成为可能。

鼓励 AUTOSAR 工具的制作者在工具发出的诊断消息中附上与 M1 建模问题相对应的约束数值 ID。

本文档所引入类的属性以类表（**class table**）形式列出，其形式如顶层元素 `AUTOSAR` 的示例所示：

请注意，约束并不要求在 AUTOSAR 工作流的任意时刻都被强制执行。在模型开发过程中，约束可以被合理地违反，因为不完整的模型显然会表现出不一致。

然而，在工作流的特定时点上，约束应当被强制执行，以防止错误配置。约束应当被强制执行的工作流时点（有时也称为约束的“施加时间”（**binding time**））对每个模型类别各不相同——例如在经典平台上，为软件组件定义的约束通常在 RTE 生成之前强制执行，而针对 ECU 抽取定义的约束则在创建 Com 栈的 ECU 配置时应用。

每份文档都定义了约束可能的施加时间，并且施加时间通常在约束自身中注明，以便为 AUTOSAR 编写工具的实现者提供明确的方向。

以 `AUTOSAR` 作为一个典型类表的示例。表中前几行的含义如下：

**类（Class）**：UML 模型中定义的类的名称。

**包（Package）**：定义该类的 UML 包。列出此项只是为了帮助在整体元模型中定位该类。

**注意（Note）**：建模者针对该类给出的注释（类注释）。类的构型和 UML 标签也在此注明。

**基类（Base Classes）**：如适用，为直接基类的列表。

表中各列表头的含义如下：

**属性（Attribute）**：类属性或类所拥有的关联端（AUTOSAR 不区分二者）。

**类型（Type）**：该属性的类型。

**多重性（Mul.）**：该属性被赋予的多重性，即有多少个给定数据类型的实例与该属性相关联。

**类别（Kind）**：说明该属性是被类聚合（`aggr` 聚合）、是类中的 UML 属性（`attr` 原始属性），还是仅被类引用（`ref` 引用）。实例引用也在此字段中标识（`iref` 实例引用）。

**注意（Note）**：建模者针对该类属性给出的注释（角色注释）。构造型和 UML 标签也在此注明。

请注意，以字母而非数字编号开始的章节代表文档的附录。附录的目的是支撑文档某些方面的解释，不代表标准的有约束力的约定。

[TPS\_STDT\_00053] 所规定的表达义务的言语形式（verbal forms）应当用于表达需求，参见标准化模板（**Standardization Template**）的可追溯性支持章（[\[2\]](#ref-2)）。

AUTOSAR 文档中需求的表示遵循 [TPS\_STDT\_00078] 所规定的表，参见标准化模板（**Standardization Template**）的可追溯性支持章（[\[2\]](#ref-2)）。

### 1.3. 定义形式化模板的方法论

图 1.1 以系统模板（**System Template**）为例，说明了定义形式化模板所采用的总体方法论。关于需要捕获到 AUTOSAR XML 文件中的信息，[\[1\]](#ref-1) 提供了精确而简洁的模型。

![图 1.1：AUTOSAR 中定义模板的方法论（以 SystemTemplate 为例）](Figure1-1.png)

以下文档描述该方法论的各个方面：

1. 模板文档（本例中为系统模板）描述模板中可以捕获的信息，与该模型到 XML 技术的映射无关。它包含对 AUTOSAR 元模型相关部分中可捕获的全部信息的语义（精确含义）的详尽描述。
2. AUTOSAR 元模型 [\[1\]](#ref-1) 中称为 **M2 Templates** 的模型包含以 UML 建模的 AUTOSAR 模板结构。该模型以注释（notes）标注，这些注释在模板文档中同样以类表的形式呈现。
3. 称为通用结构模板（**Generic Structure Template**，即本文档）的文档体现为元模型中的预定义类等，这些内容被并入生成的 schema。
4. 模板 UML 构型与建模指南（**Template UML Profile and Modeling Guide**）描述创建元模型内容时所应用的基本概念。这些信息在第 2 章中呈现。
5. 称为 XML Schema 生成规则（**XML Schema Production Rules**）的文档 [\[3\]](#ref-3) 描述如何使用 XML，以及“软件组件模板”中设计的元模型应如何由“Schema 生成器”（MDS）翻译为 XML Schema（XSD）“数据交换格式”。

这一“形式化策略”应当用于元模型中形式化描述的所有数据。特别地，为理解元模型与基于 XML 的 AUTOSAR 模板之间的映射，值得阅读本文档。

6. 数据交换格式（**Data Exchange Format**）体现为一个 XML schema，它依据 XML Schema 生成规则中定义的方法与模式从 AUTOSAR 元模型自动生成。该 schema 通常用作 AUTOSAR 工具的输入。
7. M1 层描述（在图 1.1 中表现为“System configuration description”与“System Constraint Description”）是可以对照该 XML schema 校验的 XML 文件，随后遵循相关“模板文档”中的规范。换言之，这些 XML 文件是定义模板的 XML 表示的 schema 的实例。

### 1.4. 元模型的组织

图 1.2 勾勒了元模型的总体结构，该元模型形式化地定义了描述 AUTOSAR 软件组件所需的词汇。如图所示，其他模板规范（例如 ECU 资源模板 [\[4\]](#ref-4) 与系统模板 [\[5\]](#ref-5)）也采用相同的建模方法，以便定义一个整体一致的 AUTOSAR 软件描述模型。

图中的虚线箭头表示元模型内部各包之间依赖关系（即导入关系）。例如，包 `SWComponentTemplate` 导入了包 `GenericStructure`（本文档所描述）与 `ECUResourceTemplate` [\[4\]](#ref-4) 中定义的元类。

![图 1.2：元模型的结构](Figure1-2.png)

为澄清起见，请注意包 `GenericStructure` 包含一些基础性的基础设施元类与通用模式。由于它们被所有其他模板规范使用，为清晰起见，图中未描绘指向它的依赖关联。

## 2. AUTOSAR 模板中 UML 的使用

AUTOSAR 元模型以 UML 模型定义。因此，理解各 AUTOSAR 模板文档需要具备 UML 的基础知识。

### 2.1. UML 图

AUTOSAR 模板文档中的图与 UML 2.0 一致。底层模型（AUTOSAR 元模型）被假定为完整的，即使为了便于理解，某个特定的图中可能未展示某些元素。尽管如此，类表会给出全部相关信息。

图中的着色通常在周围的文字中解释。但总体而言，浅绿色的元类取自 ASAM/MSR。

实例引用（**instance ref**）的表示如图 5.9 所示（参见 [TPS\_GST\_00044]）。

### 2.2. AUTOSAR 元模型层次

AUTOSAR 模板的完整元模型层次如图 2.1 所示。与 OMG 使用的经典四层架构不同，图中展示了五个元层次。从最低、最具体的元层次开始，它们分别是：

#### M0：AUTOSAR 对象

这是运行中的 AUTOSAR 系统的实现：例如真实的 ECU 在执行包含风窗刮水器控制软件的软件映像。

#### M1：AUTOSAR 模型

这一元层次上的模型由 AUTOSAR 开发者构建。他们可以定义一个名为“风窗刮水器”的软件组件，它带有一组确定的端口并与另一个软件组件相连，等等。在这一层次上，描述 AUTOSAR 系统所需的全部制品都被细化，包括可复用的类型以及这些类型的特定实例。

AUTOSAR 软件被装载到单个车辆的各个 ECU 中。这种装载意味着 M1 模型被实例化。

请注意，这样的 AUTOSAR 模型可以用多种格式表示，从 XML 到 C 乃至 PDF。

#### M2：AUTOSAR 元模型

这一元层次上定义了 AUTOSAR 模板的词汇。这一词汇随后可供基于 AUTOSAR 的 ECU 系统的开发者使用。

例如，在 M2 上定义了 AUTOSAR 中存在一个称为“软件组件”的实体，它聚合一个称为“端口”的实体，等等。这一

![图 2.1：元模型层次（Meta Model Hierarchy）](Figure2-1.png)

定义保证了 AUTOSAR 软件组件的开发者能够描述其特定的组件及其端口。这一描述称为 AUTOSAR 模型，位于 M1 层。

#### M3：AUTOSAR 模板的 UML 构型（profile）

M2 层上的 AUTOSAR 模板按照 M3 层定义的元模型构建。如前所述，这是 UML 加上一个为更好地支持模板建模工作而设的特定 UML 构型（profile）。

形式上，M2 层的模板仍然是 UML 的实例，但同时应用了模板构型，即还需要遵守构型中各构型（stereotype）所设定的规则。该构型的相关细节在第 2.3 章和第 2.4 章中规定。

请注意，AUTOSAR 模型可以用多种格式表示，从 XML 到 C 乃至 PDF。这些格式之间的转换称为“转换”（**transformation**），而 AUTOSAR 模型遵循 AUTOSAR 元模型这一事实称为“实例化”（**instantiation**）。因此，AUTOSAR 模型（M1）被称为 AUTOSAR 元模型（M2）的实例。

### 2.3. 构型（Stereotypes）

AUTOSAR 模板构型（Template Profile）使用以下构型<sup>1</sup>：

- **&lt;atpAbstract&gt;** — 适用于关系（关联、聚合）：这表示该关系是抽象的。每个具体子类中都需要有一个特化的关系来重定义该抽象关系。设置这一构型是为了在图中提供更好的可视化。关系是抽象的这一事实通过在模型中将该角色定义为“派生（derived）”来建模；在图中也通过角色名前的“/”来指示。
- **&lt;atpDerived&gt;** — 适用于关系（关联、聚合）：这表示该关系通过继承存在于子类中。它还进一步表明，在 M1 模型中该关系是由其他信息计算（派生）得出的。

  计算分为两类：

  - **general** — 表示该值由抽象关系注释中所描述的方法计算。例如 `atpBase` 被计算为第一个 `atpContextElement` 的容器。
  - **derived union** — 表示它被派生为所有具体关系的并集。

  例如，从 `AtpClassifier` 到 `AtpFeature`、角色为 `atpFeature` 的聚合是 **&lt;atpDerived&gt;** 的：`SwComponentType` 在 `component`、`port` 等之外还拥有一个 `atpFeature` 关联。该 `atpFeature` 被计算为各具体 feature 的并集。

  derived union 意味着：对于一个给定的组件类型，其 `atpFeature` 属性持有它的端口**以及**它所包含的组件原型**以及**它所包含的连接器。这使得能够在抽象层次上定义实例引用。

  更多细节参见第 5 章。

- **&lt;atpMixed&gt;** — 适用于类：仅应用于元类，表示一个不含交杂文本的混合内容模型。

  更多细节参见第 2.3.1 章。

- **&lt;atpMixedString&gt;** — 适用于类：这是一个含交杂文本的混合内容模型。仅应用于元类。

  更多细节参见第 2.3.1 章。

- **&lt;atpObject&gt;** — 适用于类：这是一个隐式基类。它只能提供带有 `xml.attribute=true` 标签的属性。

  更多细节参见第 6.3.3 章。

- **&lt;atpSplitable&gt;** — 适用于关系：通过使用构型 **&lt;atpSplitable&gt;**，元模型可以显式地定义元模型的实例如何分布到多个文件中。默认情况下所有数据存储在单个文件中。若应用了 **&lt;atpSplitable&gt;**，则关联或聚合的信息可以存储在不同的文件中。

  关于可拆分元素和 splitkey 的更多信息参见第 8 章。

- **&lt;atpIdentityContributor&gt;** — 适用于聚合、关联和原始属性：这一构型应用于对 M1 元素的标识（identity）有贡献的聚合、关联和原始属性，例如 `shortName` 属性。带有 **&lt;atpIdentityContributor&gt;** 构型的属性参与 splitkey 的构成，splitkey 控制来自部分模型（partial models）的可拆分元素的合并。

  关于可拆分元素和 splitkey 的更多信息参见第 8 章。

- **&lt;atpVariation&gt;** — 适用于类和关系：这表示变体处理。它既应用于元类，也应用于关联或聚合。

  更多细节参见第 7 章。

- **&lt;atpUriDef&gt;** — 适用于关联：这表示本质信息只是引用目标的全限定名（full qualified name）。它随后被整体用作特定用途的标识符。该关联充当 AUTOSAR 模型中一种“通用资源标识符”（**Universal Resource Identifier**）的定义。

  请注意，在这种情况下只有全限定 shortName 路径是重要的，目标本身的 shortName 乃至目标本身都不重要。其具体语义以及后续处理取决于各个用例。

  因此，并不总是需要真正地追随 **&lt;atpUriDef&gt;** 构型所修饰的引用。除非用户或特定用例明确要求，工具不应当对该构型的悬挂引用（dangling references）发出警告。

  例如 `EcucReferenceDef.destination`：该引用表明 `EcucReferenceValue` 的有效目标应当是其 definition 派生自 `EcucReferenceDef.destination` 目标的 `EcucContainerValue`。即使目标 `EcucReferenceDef.destination` 并不真实可用，这一点也可以得到校验。

- **&lt;instanceRef&gt;** — 适用于依赖：用于在图中提供实例引用的简化表示。
- **&lt;instanceRef&gt;** 与 **&lt;atpUriDef&gt;** 组合：如果构型 **&lt;instanceRef&gt;** 和 **&lt;atpUriDef&gt;** 同时应用于一个依赖，则 [TPS\_GST\_00029] 中定义的 **&lt;atpUriDef&gt;** 语义应当应用于该实例引用的所有子引用。

  关于实例引用的更多细节参见第 5.1.3 章。

- **&lt;isOfType&gt;** — 适用于关联：用于强调原型（`AtpPrototype` 的子类）与类型（`AtpType` 的子类）之间的具体关系。

  这一构型影响按照第 6.3.2 章进行的关联生成<sup>3</sup>。

> **1** 这些构型的名称以 atp 开头，它是“AUTOSAR Template Profile”的缩写。
>
> **2** 作为这种重定义的结果，XSD 生成器会忽略此类抽象关系。
>
> **3** 注意，这一构型对于“此类关联需要直接或间接地重定义角色 `atpType`”这一事实而言是冗余的。

**约束：以构型 &lt;isOfType&gt; 修饰的引用必须存在**

如果 `AtpPrototype` 的一个子类定义了一个以构型 **&lt;isOfType&gt;** 修饰的、指向 `AtpType` 某个子类的引用，则该引用必须始终存在。

### 2.3.1. 混合内容（&lt;atpMixed&gt;、&lt;atpMixedString&gt;）

如果一个元类拥有多个属性（其中可以包括聚合或引用），在某些情况下，M1 模型中的“序列化”表示（如 XML）会为属性实例的实际顺序和出现次数添加语义。也可能出现如下要求：同一属性以多个实例（在 M1 中）出现，并且与其他属性的实例相互交杂。这种情况无法用 UML 简单地表达。

此外，如果模型需要描述类似文档的信息，它往往需要把形式化内容与文本混合在一起。这类模型的一个例子是 HTML 中的嵌入式链接：形式化信息片段的标记混入普通文本之中，如下例所示：

```
[...]meet <a href="/wiki/Runtime" title="Runtime">runtime</a> requirements of automotive devices[...]
```

该示例说明，“混合内容”特性在 XML 领域早已广为人知，在那里它被称为 mixed content<sup>4</sup>。

**混合内容的基本特性**

下表从建模的角度列出了混合内容的特性。在一个混合内容实例中：

- 一组形式化定义的模型元素可以以任意顺序、任意次数出现；
- 但实际出现的顺序就整体对象的语义而言是相关的；并且
- 在 **&lt;atpMixedString&gt;** 的情况下，非限定文本（unqualified text）可以交杂在任何形式化定义的元素之间。

AUTOSAR 通过以下构型支持这一机制：

- **&lt;atpMixedString&gt;**（[TPS\_GST\_00025]）——允许在数据元素之间出现文本；
- **&lt;atpMixed&gt;**（[TPS\_GST\_00024]）——允许该类的各属性以任意顺序任意混合。

后一种构型不允许混入文本，但在语法和语义上保留了顺序的定义。

**混合内容中的多重性上限**

混合内容类会在模板模型中聚合或引用若干其他类。这些关系的目标多重性通常为 1，因为按照 [TPS\_GST\_00032] 给出的定义，整体出现次数本来就是任意的。

但如果多重性不等于 1，则规定了所需成组（grouping）的大小。

例如，若目标多重性为 2，则总是必须将这样的一对对象（而不只是单个对象）放入混合内容中，依此类推。

图 2.2 展示了它的工作方式。M1 模型以 XML 表示。请注意：

1. `MixedContent` 可以是 `a b c d e` 的任意混合、任意顺序。顺序在语义上是重要的。这与在 UML 中把一个多重性上限 &gt; 1 的聚合标注为 {ordered} 的意义相同<sup>5</sup>。
2. `c` 的多重性上限 &gt; 1，因此存在针对多重性的包装元素。
3. `e` 合法地缺失，因为按照定义整体出现次数是任意的。

![图 2.2：混合内容（Mixed content）](Figure2-2.png)

**混合内容中继承的属性**

- 被继承的混合属性属于混合内容的一部分，可以与自有混合属性自由混合。
- 来自本身不是 **&lt;atpMixed&gt;** 的类的被继承属性，不属于混合内容。
- 属性（`xml.attribute` 置为 `true` 的）和被继承的属性不属于混合内容。

进一步注意，在 **&lt;atpMixedString&gt;** 中，除 `xml.attribute` 置为 `true` 的属性外没有其他被继承的属性。

> **4** <http://www.w3schools.com/schema/schema_complex_mixed.asp>
>
> **5** 在 UML 中无法为类标注这一注解。

### 2.3.2. StructuredComment 元素（&lt;atpStructuredComment&gt;）

AUTOSAR 支持 StructuredComment，以提供旨在形成注释的辅助信息。

**&lt;atpStructuredComment&gt;**

标记为 **&lt;atpStructuredComment&gt;** 的元素所包含的信息在模型中没有语义，在模型层次上可以被忽略。

**&lt;atpStructuredComment&gt; 与 &lt;atpSplitable&gt; 的相互作用**

在按照可拆分元素合并多个物理文件时，所有标记为 **&lt;atpStructuredComment&gt;** 的元素及其全部子元素都可以被忽略。

清单 2.1 通过提供关于生成工具及其版本的信息，展示了 **&lt;atpStructuredComment&gt;** 的用法。

清单2.1：ARXML 文件中的 FileInfoComment

```xml
<AUTOSAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://autosar.org/schema/r4.0"
         xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
  <FILE-INFO-COMMENT>
    <SDGS>
      <SDG GID="GENERATION-INFO">
        <SD GID="TOOL-VERSION">ToolA.1.2.3</SD>
        <SD/>
      </SDG>
    </SDGS>
  </FILE-INFO-COMMENT>
  <ADMIN-DATA>
```

表2.1：FileInfoComment

| 类         | FileInfoComment                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------------|
| 包         | M2::AUTOSARTemplates::AutosarTopLevelStructure                                                            |
| 注意       | 该类支持 StructuredComment，以提供旨在形成注释的辅助信息。                                                   |
| 基类       | ARObject                                                                                                  |
| 聚合于     | AUTOSAR.fileInfoComment                                                                                   |

| 属性 | 类型 | 多重性 | 类别 | 注意 |
|------|------|--------|------|------|
| sdg  | Sdg  | *      | aggr | 该属性允许保留标准模型未表示的特殊数据。它可用于保存例如工具特定的数据。 |

### 2.4. UML 标签

AUTOSAR 模板构型使用以下 UML 标签。注意，这里只列出直接影响元模型语义内容的标签。

**UML 标签在适合时附着于关系的目标端**

除非特定 UML 标签另行规定，UML 标签附着于关系（关联、聚合）的目标端。对于依赖（Dependency）和泛化（Generalization），UML 标签与连接符本身相关联（以克服 AUTOSAR 所用 UML 工具（EA）的限制）。

- **atp.recommendedPackage**：该标签为给定元类的对象提供一个推荐的包名，从而为 {kind} 提供取值。通常它就是该标签所附着元类的名称。请注意：

  - 该标签会传播到子类；
  - 该标签只应用于 `PackageableElement` 的子类。

  可能的取值是 [\[6\]](#ref-6) 中定义的各种 manifest，例如 Machine Manifest、Execution Manifest、Service Instance Manifest。{kind} 的取值在第 3.1 章中描述。

- **atp.Splitkey**：规定 **&lt;atpSplitable&gt;** 关系的标识键。该标签规定一个以逗号分隔的列表，其元素是 [TPS\_GST\_00416] 中定义的属性。这些属性是按照 [TPS\_GST\_00047] 在部分模型中构造 M1 元素标识的基础。

  更多细节参见第 8 章。

### 2.4.1. 生命周期标签

**表示生命周期信息的标签**

AUTOSAR 通过名为 `atp.Status*` 和 `map.Status` 的标签，在 UML 模型的实体上标注其相对于生命周期的状态。

- **atp.Status**：该标签允许规定元模型实体相对于其生命周期的当前状态。它适用于类、聚合、关联和属性。支持以下取值：

  - **VALID** — 表示相关实体是文档的有效部分。
  - **DRAFT** — 表示相关实体是元模型中新增的、仍处于试验状态的实体。该信息已发布，但可在不受向后兼容性管理约束的情况下变更。
  - **CANDIDATE** — 用于尚未成为有效（valid）但仍应被 AUTOSAR BWC 检查器（针对 XML schema）识别的相关实体。相关实体的任何 BWC 不兼容变更都应由 BWC 检查器报告。
  - **OBSOLETE** — 表示相关实体已废弃，出于兼容性原因保留在元模型中。若设置了该标签，注释（note）应当表述推荐的替代方案。
  - **REMOVED** — 表示相关实体仍因某种原因（例如在 lifeCycles 的上下文中）留在元模型中。它不得再被使用，甚至不应再出现在文档中。AUTOSAR 发布版不包含这样的元素。它面向 AUTOSAR 内部开发。在 M1 用例中，这类被移除的元素不会包含在 .arxml 交付物中，但可以通过 `Referrable` 类型的 **&lt;atpUriDef&gt;** 属性在 LifeCycleInfoSet 中被引用：`lcObject`，相应地还有 `useInstead`。

  类与聚合/引用中 LifeCycleState 的允许组合见表 [TPS\_GST\_00440] 和表 [TPS\_GST\_00441]。若未规定该标签，则相关实体是当前元模型的有效（VALID）部分。该标签应当应用于关联的目标端。

  若希望在图的注释中显示该标签，也可以将其应用于关联本身。

  未验证的新引入元素通常以 `LifeCycleState = DRAFT` 创建，与假定的置信水平无关。在后续发布版中，它们可以以对 AUTOSAR schema 不兼容的方式变更。

  为缓解这种情况，由概念（concept）引入的元模型元素以 `LifeCycleState = CANDIDATE` 呈现。具有该 LifeCycleState 的模型元素成为（BWC）兼容性检查器的检查对象，这避免了此类模型元素以不兼容方式被意外变更而未被察觉的情况。

  `LifeCycleState = CANDIDATE` 只适用于元模型元素，不适用于规范项（specification items）的 LifeCycleState。

  请注意，[TPS\_GST\_00051] 关注的是 M2 实体（元模型），而 [TPS\_STDT\_00064] 针对 M1 实体（模型）表达了同样的内容。

  请注意，清单 12.1 以 AUTOSAR arxml 文件的形式提供了这些取值。

- **atp.Status 的默认值**

  元模型的 `atp.Status` 默认值为 “valid”；关联从其源端继承该值；聚合和属性从其父元素继承该值。

- **atp.StatusRevisionBegin**：该标签指示从哪个 AUTOSAR 发布版起 `atp.Status` 所标注的状态有效。它对应于 [TPS\_GST\_00244] 规定的 periodBegin。
- **atp.StatusRevisionEnd**：该标签指示从哪个 AUTOSAR 发布版起 `atp.Status` 所标注的状态有效。它对应于 [TPS\_GST\_00244] 规定的 periodEnd。
- **atp.StatusComment**：这是按照 [TPS\_GST\_00051] 对当前状态的一段简短说明。它主要应用于 “valid” 以外的状态取值。
- **map.Status**：该标签允许为上游映射定义生命周期。该标签的取值与 `atp.status` [TPS\_GST\_00051] 的取值相关联。

元类/枚举的成员所允许的 LifeCycleState 定义于 [TPS\_GST\_00440]。元类成员的目标/类型所允许的 LifeCycleState 定义于 [TPS\_GST\_00441]。两表表示直接子元素，不考虑继承。

**元模型（聚合/引用/属性/枚举字面量）允许的 LifeCycleState**

表2.2：图例：1=允许的组合

| 类/枚举（父/源）的 LifeCycleState | DRAFT | CANDIDATE | VALID | OBSOLETE | REMOVED |
|-----------------------------------|-------|-----------|-------|----------|---------|
| DRAFT                             | 1     |           |       | 1        | 1       |
| CANDIDATE                         |       | 1         |       | 1        | 1       |
| VALID                             | 1     | 1         | 1     | 1        | 1       |
| OBSOLETE                          |       |           |       | 1        | 1       |
| REMOVED                           |       |           |       |          | 1       |

**元模型元类允许的 LifeCycleState**

表2.3：图例：1=允许的组合

| （聚合/引用/属性）的 LifeCycleState | DRAFT | CANDIDATE | VALID | OBSOLETE | REMOVED |
|-------------------------------------|-------|-----------|-------|----------|---------|
| DRAFT                               | 1     |           | 1     |          |         |
| CANDIDATE                           |       | 1         | 1     |          |         |
| VALID                               |       |           | 1     |          |         |
| OBSOLETE                            | 1     | 1         | 1     | 1        |         |
| REMOVED                             | 1     | 1         | 1     | 1        | 1       |

表 [TPS\_GST\_00440] 与表 [TPS\_GST\_00441] 的适用范围如图 2.3 所示。

![图 2.3：状态值组合（Status value combinations）](Figure2-3.png)

图 2.4 展示了几种无效的情况：

- `ClassA` 的 `LifeCycleState = OBSOLETE` 却拥有 `LifeCycleState = VALID` 的成员（聚合与引用）。这违反表 [TPS\_GST\_00440]。
- 图中所示 `LifeCycleState = VALID` 的聚合与引用以 `LifeCycleState = OBSOLETE` 的 `ClassB` 为目标。这违反表 [TPS\_GST\_00441]。

![图 2.4：LifeCycleState 的无效组合（Invalid combination of LifeCycleStates）](Figure2-4.png)

**atp.EnumerationLiteralIndex**

该标签允许为特定的枚举字面量定义一个索引。该索引允许把某个枚举字面量规定为数值函数（尤其是公式表达式的结果）的结果。该索引在一个特定的 Enumeration 元类内是唯一的。

清单2.2：枚举属性值变体点示例

```xml
<DIAGNOSTIC-CONTRIBUTION-SET>
  <SHORT-NAME>DiagSet1</SHORT-NAME>
  <COMMON-PROPERTIES>
    <DIAGNOSTIC-COMMON-PROPS-VARIANTS>
      <DIAGNOSTIC-COMMON-PROPS-CONDITIONAL>
        <DEBOUNCE-ALGORITHM-PROPSS>
          <DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>
            <SHORT-NAME>DiagDebounce</SHORT-NAME>
            <DEBOUNCE-BEHAVIOR BASE="DefaultEnumMappingTables"
                               ENUM-TABLE="DiagnosticDebounceBehaviorEnum">
              <SYSC-REF DEST="SW-SYSTEMCONST">processor</SYSC-REF> == 42 ? 0 : 1
            </DEBOUNCE-BEHAVIOR>
          </DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>
        </DEBOUNCE-ALGORITHM-PROPSS>
      </DIAGNOSTIC-COMMON-PROPS-CONDITIONAL>
    </DIAGNOSTIC-COMMON-PROPS-VARIANTS>
  </COMMON-PROPERTIES>
</DIAGNOSTIC-CONTRIBUTION-SET>
```

在清单 2.2 中，`DiagnosticDebounceAlgorithmProps` 的行为由一个形式化表达式计算。若该形式化表达式的结果为 42，则得到 “0”。该 numericalValue 在 M2 层上标记一个索引，并映射到 `DiagnosticDebounceBehaviorEnum` 的枚举字面量 `FREEZE`。若计算结果不是 42，则得到 “1”，并落到 `DiagnosticDebounceBehaviorEnum` 的枚举字面量 `RESET`。这些映射基于 **&lt;mmt.EnumerationLiteralIndex&gt;** 定义的数值“等价物”。参见 [\[7\]](#ref-7) 中的 EnumerationMappingTable。numericalValue 不用于 CCode，也不在运行时使用。

### 2.4.2. 文档生产控制标签

AUTOSAR 规定了一种手段，用于控制平台特定内容在规范文档中的呈现。这些限制的语义进一步解释如下：

- 在文档层次上：[TPS\_GST\_00428]；
- 在建模层次上：[TPS\_GST\_00431]。

该手段是元模型制品（artifact）特定的，进一步解释如下：

- 元模型类、连接符和属性：[TPS\_GST\_00372]；
- 元模型图：[TPS\_GST\_00429]；
- 元模型描述：[TPS\_GST\_00430]。

**文档层次上的标准限制**

标准限制（standards restriction）的使用控制模型元素在所提及标准范围内生成的文档制品中的呈现。若一个标准限制应用于某个模型元素，则该模型元素应当只出现在由该限制的取值所标识的标准的生成制品中。

**标准限制在建模层次上的影响**

由于 [TPS\_GST\_00372] 而对相应平台不可见的模型元素，即使在模型中可见地存在，也被隐式地排除在模型中的任何进一步语义之外。

若没有 [TPS\_GST\_00431]，就必须在 [TPS\_GST\_00372] 的限制之外再编写形式化的 AUTOSAR 约束，以进一步限制模型中这些被排除制品的任何使用或关联。这会显著增加约束的数量。一个明显的例子是：某个模型中被限制的制品可以存在，但一旦考虑标准限制，它们就不具有任何文档语义。

**控制规范文档生产的标签**

名为 `mmt.*` 的 UML 标签控制规范文档的生产。

- **mmt.RestrictToStandards**：该标签的使用控制元类、连接符和属性等模型元素在生成制品中相对于所提及标准的呈现。若 `mmt.RestrictToStandards` 应用于某个模型元素，则该模型元素应当只出现在由 `mmt.RestrictToStandards` 取值所标识的标准的生成制品中。`mmt.RestrictToStandards` 的取值是一个以逗号分隔的列表，包含一个或多个下列值：“CP”、“AP”、“FO”、“TC”、“TA”。列表中值周围的空白没有意义。

  示例：`Tags:mmt.RestrictToStandards = "CP , AP"`

  若未应用标准限制标签，或值部分的列表为空，则假定不施加限制，制品为所有标准生成。

  AUTOSAR 为所有平台定义了一个统一的元模型。这允许复用既有元类。某些元类会拥有对各标准相互排斥的属性、聚合或引用——例如与经典平台相关的属性应当只出现在为经典平台生成的制品中。

- **mmt.templateTable**：

  该标签用于将模板与给定的变体点（variation point）相关联。取值是一个以空白分隔的模板列表，模板名称遵循 [TR\_PDN\_00003]；具体而言，它是 [\[8\]](#ref-8) 中集合 “DocumentAbbreviations” 里分类为 DocumentAbbreviation 的 Keyword 所定义的 abbrName（例如 `SWCT`）。

  `mmt.templateTable` 标签应用于任何含有对元模型有贡献的对象的包。

  `mmt.templateTable` 传递地应用于定义所在包的所有子包。尽管如此，子包可以覆盖祖先包上 `mmt.templateTable` 提供的值。

**元模型图的标准限制应用**

元模型图的标准限制应用是一个图注（Diagram Note），其取值为 JSON 格式的键/值，其中键为 `mmt.RestrictToStandards`，值为一个字符串，包含一个或多个下列以逗号分隔的值：“CP”、“AP”、“FO”。列表中值周围的空白没有意义。

示例：`{'mmt.RestrictToStandards' : 'CP , AP'}`

若未应用标准限制，或值部分的列表为空，则假定不施加限制，制品为上述所有标准生成。

**元模型描述字段的标准限制应用**

对应当出现在生成文档中的元类或连接符描述（角色注释）应用标准限制的方式，是在描述字段中使用一个嵌入式解析器令牌（parser token）将文本块指派给各个平台，由 AUTOSAR 文档工具套件处理。

示例：

```
@RESTRICT_TO_STANDARD:CP:AP! Classic and Adaptive text. @RESTRICT_TO_STANDARD:FO! Foundation text. @END_RESTRICT_TO_STANDARD!
```

若未应用标准限制，或值部分的列表为空，则假定不施加限制，制品为上述所有标准生成。

### 2.4.3. 变体处理标签

**表示变体处理属性的标签**

名为 `vh.*` 的 UML 标签与变体处理相关。

- **vh.latestBindingTime**：该标签控制变体处理的施加时间（binding time）。更多细节参见第 7.6 章 [TPS\_GST\_00182]。
- **vh.variationPointApplicable**：将该标签设置为 “false” 即标识出“幽灵变体点”（**Ghost Variation Points**）。关于“幽灵变体点”的更多信息，参见第 7.1.3 章 [TPS\_GST\_00185]。

### 2.4.4. Schema 生产配置标签

**用于配置 XML schema 生产的 UML 标签**

名为 `xml.*` 的 UML 标签与 AUTOSAR 模型的 XML 序列化相关。它们基本上不影响 M1 模型的语义，但保证 XML 序列化可以由元模型控制。

它们还提供了对 schema 进行微调的手段，使得在元模型演化的同时能够保证 schema 的向后兼容性。

关于如何应用这些标签及其影响的更多细节，参见 [\[3\]](#ref-3) 中的“4 Configuration of XML schema production”章。

- **xml.xsd.\* 等**：这些标签允许使用 XSD 限制来定义原始类型（primitive types）的细节。即使它是借助一种技术特定的定义规定的，它也独立于存储技术而适用于元模型。
- **xml.xsd.customType**：该标签适用于 **&lt;primitive&gt;**。它规定表示该原始类型的 `xsd:simpleType` 的名称。
- **xml.attribute**：规定该 UML 属性是否序列化为一个 XML 属性。该标签允许控制 XML 序列化，与 M1 模型的语义无关。
- **xml.attributeRef**：规定该 UML 属性是否序列化为对一个全局 XML 属性的引用。若置为 `true`，则将该属性序列化为对一个全局属性的引用。仅在 `xml.attribute` 置为 `true` 时适用。

  被引用属性的名称由 `xml.name` 规定。被引用属性的命名空间前缀由 `xml.nsPrefix` 规定。

- **xml.enforceMinMultiplicity**：若为 `true`，强制最小多重性；否则为 “0”。为了允许传输部分信息，标准化 schema 中默认不强制最小多重性。
- **xml.enforceMaxMultiplicity**：若为 `true`，强制最大多重性；否则为 “unbounded”。`xml.enforceMaxMultiplicity` 默认为 `true`。
- **xml.globalElement**：若为 `true`，为被标记的类创建一个全局 `xsd:element`。该 `xsd:element` 可以用作 schema 实例的根元素。该标签需要在 AUTOSAR 元模型中显式定义。通常只有元类 `AUTOSAR` 由一个全局定义的 XML 元素表示。
- **xml.mds.type**：当某原始类型是由元模型工具生成的类型时，该标签规定其数据类型。这类生成类型的主要例子是 `REFERRABLE-SUBTYPES-ENUM`。该标签应当应用于一个 **&lt;primitive&gt;**，后者随后充当 `xml.mds.type` 所指类型的代理（proxy）。
- **xml.name**：提供表示该角色或类的 schema 片段（元素、属性、组等）的名称。

  若未在 AUTOSAR 元模型中显式定义，则该值按照 [\[3\]](#ref-3) 中说明的方式计算。

- **xml.nsPrefix**：该标签可应用于属性，为 `xml.attributeRef` 置为 `true` 的属性确定命名空间前缀；应用于包时，为基于该包的 schema 确定所使用的命名空间前缀。
- **xml.nsUri**：为基于该包的 schema 确定所使用的命名空间 URI。命名空间 URI 的格式定义于 [\[3\]](#ref-3)。若未在 AUTOSAR 元模型中显式定义，则该值按照 [\[3\]](#ref-3) 中说明的方式隐式指定。
- **xml.roleElement、xml.roleWrapperElement、xml.typeElement、xml.typeWrapperElement**：这些标签允许控制 XML 序列化，尤其是 XML 元素的创建，与 M1 模型的语义无关。更多细节参见 [\[3\]](#ref-3)。
- **xml.sequenceOffset**：确定各属性在 XML 中序列化的顺序。若缺少该标签，属性按字母顺序序列化。该顺序只影响 XML 制品的维护便利性，与 M1 模型的语义无关。<sup>6</sup>

> **6** 若顺序是相关的，则在模型中以 {ordered} 多重性表示。

### 2.4.5. 管理 UML 标签

**管理类 UML 标签**

为了元模型的文档管理，名称模式为 `admin.*` 的 UML 标签应用于一个特定的包（例如 `M2::AUTOSARTemplates::ReadMe`）。若该包在“元模型工具”（**Meta-Model Tool**，MMT）的配置文件中被引用，则这些取值会被传递到生成的制品（例如 `MMOD_XMLSchema` 或 `MOD_ECUConfigurationParameters`）。

除 UML 标签外，生成制品的免责声明（disclaimer）也取自该包的包注释。

适用的 UML 标签如下：

- **admin.documentClassification**：表示元模型的分类（Standard 或 Auxiliary）。
- **admin.documentIdentificationNo**：表示 AUTOSAR 文档编号。
- **admin.documentOwner**：表示元模型的维护者。
- **admin.documentResponsibility**：表示元模型的责任机构。
- **admin.documentStatus**：表示元模型的状态。
- **admin.documentTitle**：表示指派给元模型的标题。
- **admin.documentVersion**：表示元模型的正式版本。注意，文档版本与 `admin.partOfRelease` 无关，因此像 3.1.12 这样的版本号不一定指 AUTOSAR 的 R3.1 分支。

AUTOSAR 区分外部与内部 AUTOSAR 发布版编号：

- 外部 AUTOSAR 发布版编号采用 R&lt;yy&gt;.&lt;mm&gt; 格式（例如 R20-11），标识面向外部社区的某次 AUTOSAR 发布，参见 [TPS\_GST\_00074]。
- 内部 AUTOSAR 发布版编号采用 RevisionLabelString 定义的格式（例如 4.6.0），用于 AUTOSAR 发布版的内部标识与引用。内部发布版编号用于例如 BSW 模块、XML schema 和 ARXML 文件中，参见 [TPS\_GST\_00076]。

- **admin.partOfRelease**：表示元模型发布所在的外部 AUTOSAR 发布版（例如 R20-11）。注意，该标签是必需的，因为工具链要用它来控制各类生成器的细节，例如：

  - 为早于 4.0 的 AUTOSAR 发布版插入硬编码的名为 `REF` 的 `xsd:simpleType`；
  - 按照各自的实现处理原始类型；
  - 各 AUTOSAR 发布版之间制品（例如类表）的结构差异。

  原始类型实现的细节在第 6.3.1 章中描述。

- **admin.releaseDate**：表示元模型发布所在的 AUTOSAR 发布版的日期。
- **admin.revision**：表示元模型发布所在的内部 AUTOSAR 发布版的特定修订（revision）。

### 2.4.6. 上游映射规范标签

**规定上游映射的标签**

名为 `map.*` 的 UML 标签与上游映射的描述相关。上游映射描述方法论中较晚创建的 M1 实体（下游）如何与较早创建的实体（上游）相关联（映射）。

- **map.template**：

  - 表示适用的上游 M2“模板”的列表，映射将在其中列出。
  - 格式为一个以逗号分隔的列表，包含一个或多个“模板”。列表中值（“模板”）周围的空白没有意义。
  - 每个“模板”遵循 [TR\_PDN\_00003]；具体而言，它是 [\[8\]](#ref-8) 中集合 “DocumentAbbreviations” 里分类为 DocumentAbbreviation 的 Keyword 所定义的 abbrName（例如 `SWCT`）。

  ```
  示例：map.template=TPS_SWCT,TPS_DEXT
  ```

- **map.param**：

  - 表示适用的上游 M2 元素的列表，M1 参数应当映射到这些元素。
  - 格式为一个以逗号分隔的列表，包含一个或多个“节点路径”。列表中值（“节点路径”）周围的空白没有意义。
  - 每个“节点路径”是到相应 M2 元素的全限定元模型节点路径。

  ```
  示例：map.param=SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanFrameTriggering.canAddressingMode, SystemTemplate::Fibex::Fibex4Can::CanCommunication::CanFrameTriggering.canFrameRxBehavior
  ```

- **map.rule**：

  - 表示如何转换数据的自由文本描述。

  ```
  示例：map.rule=1:1 mapping
  ```

- **map.type**：

  - 表示映射质量。适用以下取值：**local** — 无需映射，因为参数是 BSW 本地的；**partial** — 部分数据可以自动映射，但不是全部；**full** — 全部数据都可以自动映射。

  ```
  示例：map.type=full
  ```

## 3. AUTOSAR 顶层结构

AUTOSAR 为所有 AUTOSAR 模板使用一个公共的顶层结构。这一做法为在 AUTOSAR 方法论中设计各制品保留了最大的灵活性。图 3.1 展示了 AUTOSAR 的顶层结构。

![图 3.1：AUTOSAR 模板的顶层结构（Top level structure of AUTOSAR templates）](Figure3-1.png)

**AUTOSAR 模型的顶层结构**

元类 `AUTOSAR` 是所有模板的根。`AUTOSAR` 以 `arPackage` 的形式包含多个 `ARPackage`。

由于元类 `AUTOSAR` 作为所有模板（进而也是相应 XML 文档）的根，`AUTOSAR` 的这一唯一角色还通过赋予 `xml.globalElement` 标签来体现，另参见 [TPS\_GST\_00059]。

`ARPackage` 可以任意嵌套。这些包包含 `PackageableElement`，它们代表 AUTOSAR 模板中特定的自治实体。其中最突出的特化是 `ARElement`（参见第 4.2 章）。

请注意，所有 AUTOSAR 元类都继承自 `ARObject`（参见第 4.1 章）。<sup>1</sup>

**AUTOSAR 顶层的 AdminData**

顶层结构还包含 AdminData，它规定了 AUTOSAR 制品的两个主要方面：

- 以 `DocRevision` 规定的变更管理信息；
- 文档的语言状态。

更多细节参见第 4.5 章。

聚合的 introduction 刻意不带有 **&lt;atpSplitable&gt;** 构型。它由类 `DocumentationBlock` 表示，后者带有指示混合内容模型的 **&lt;atpMixed&gt;** 构型，参见 [TPS\_GST\_00024]。

**制品的语言状态**

制品的语言状态规定：

1. 文档的“主”语言，规定于顶层 AdminData 中的属性 `language`。
2. 文档中存在的其他语言。这规定为 `usedLanguages`，它是一个 `MultiLanguagePlainText`，充当文档所用语言的列表。

关于多语言方法的更多细节参见第 9.6 章。以下示例展示了一个 ARXML 文件的顶层结构。该文件同时以英语和德语维护，英语是主语言。

清单3.1：ARXML 文件的顶层结构

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://autosar.org/schema/r4.0"
         xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
  <ADMIN-DATA>
    <LANGUAGE>EN</LANGUAGE>
    <USED-LANGUAGES>
      <L-10 L="EN" xml:space="default">English</L-10>
      <L-10 L="DE" xml:space="default">German</L-10>
    </USED-LANGUAGES>
  </ADMIN-DATA>
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>demo</SHORT-NAME>
      <ELEMENTS>
        <!--autosar elements here-->
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
```

另参见 AUTOSAR。

一个 AUTOSAR 制品按 `ARPackage` 组织，`ARPackage` 包含所谓的 `PackageableElement` 元素。这些元素按其自身的性质定义，彼此独立存在，并通过关联被使用。例如，一个计算方法（computation method）独立定义自身，并通过引用被数据定义所使用。

关于 `ARPackage` 的更多细节请参见第 4.2 章。

为了在顶层提供模型中没有语义的辅助信息，AUTOSAR 支持 **&lt;atpStructuredComment&gt;**，参见 [TPS\_GST\_00381]。

> **1** 显然 `ARObject` 不继承自其自身。

### 3.1. 标识包中的 M1 元素

包用于组织 AUTOSAR M1 模型。AUTOSAR GBR 本身将 M1 模型作为已发布标准的一部分发布。为了清晰地标识这些模型元素，适用以下规则：

**AUTOSAR 交付模型的包结构**

由 AUTOSAR 标准化并以 ARXML 交付的模型元素位于 shortName 为 `AUTOSAR` 的顶层包中。

这意味着由 OEM 或供应商定义的数据元素不应当位于名为 `AUTOSAR` 的顶层包中。

**AUTOSAR 交付模型的结构模式**

AUTOSAR 交付模型的包结构遵循以下模式：

```
/AUTOSAR
  /{module}                       --标识规范
    /{kind}s[_Blueprint | _Example] --标识对象的类别
```

请注意，AUTOSAR 通常交付 Blueprint。更多细节参见 [TPS\_STDT\_00067]。

一个示例结构为：

| /AUTOSAR                            |              |
|-------------------------------------|--------------|
| /ComM                               |              |
| /ApplicationDataTypes_Blueprint     | [BLUEPRINT]  |
| /BswModuleEntrys_Blueprint          | [BLUEPRINT]  |
| /CompuMethods_Blueprint             | [BLUEPRINT]  |
| /DataConstrs_Blueprint              | [BLUEPRINT]  |
| /DataTypeMappingSets_Blueprint      | [BLUEPRINT]  |
| /Documentations                     | [STANDARD]   |
| /ImplementationDataTypes_Blueprint  | [BLUEPRINT]  |
| /ImplementationDataTypes            | [STANDARD]   |
| /ModeDeclarationGroups_Blueprint    | [BLUEPRINT]  |
| /SwcBswMappings_Blueprint           | [BLUEPRINT]  |
| /SwComponentTypes_Blueprint         | [BLUEPRINT]  |
| /BswModuleDescriptions_Blueprint    | [BLUEPRINT]  |

在此示例中，既有实现数据类型的 blueprint 包，也有最终实现为 STANDARD 的实现数据类型的包。

另一个示例为：

| /AUTOSAR                            |              |
|-------------------------------------|--------------|
| /AISpecification                    |              |
| /DataConstrs                        | [STANDARD]   |
| /PhysicalDimensions                 | [STANDARD]   |
| /Units                              | [STANDARD]   |
| /ApplicationDataTypes_Blueprint     | [BLUEPRINT]  |
| /CompuMethods_Blueprint             | [BLUEPRINT]  |
| /PortInterfaces_Blueprint           | [BLUEPRINT]  |
| /PortPrototypeBlueprints_Blueprint  | [BLUEPRINT]  |
| /ApplicationDataTypes_Example       | [EXAMPLE]    |
| /BlueprintMappingSets_Example       | [EXAMPLE]    |
| /CompuMethods_Example               | [EXAMPLE]    |
| /PortInterfaces_Example             | [EXAMPLE]    |
| /SwComponentTypes_Example           | [EXAMPLE]    |

此示例展示了一个同时提供 STANDARD、BLUEPRINT 和 EXAMPLE 的用例。

**ECUC 参数定义的包结构**

请注意，出于兼容性原因，ECUC 包结构在 AUTOSAR 4.0 中保持为：

```
/AUTOSAR
  /EcucDefs
```

**AUTOSAR 定义模型元素的结构模式**

AUTOSAR 规范已经为其定义了标准化名称（例如平台类型）的模型元素，应当位于遵循以下模式的包路径中：

```
/AUTOSAR_{module}[_{postfix}]/{kind}s
```

在这些模式中，适用以下占位符：

- **{module}** 表示一个模块标志符（**Module Designator**）。模块标志符是以下之一：

  - 模块、库等（作为按照 [\[9\]](#ref-9) 的 API 服务前缀，例如 `CanIf`、`Ifx`、`Compiler`）；
  - [\[8\]](#ref-8) 中集合 “VirtualModules” 里分类为 ModuleDesignator 的 Keyword 所定义的 abbrName（例如 `AISpecification`）。

- **{postfix}** 表示特定的实现：当且仅当同一系统中出现同一 BSW 模块的多个实现时，才在包结构中附加一个后缀。
- **{kind}** 表示元素的类别：取值是 `ARElement` 某个子类的名称加复数后缀 “s”。各 `ARElement` 特定的包名通过 UML 标签 `atp.recommendedPackage` 规定（参见 [TPS\_GST\_00049]），并照此显示在类表中（例如由 `BswModuleDescription` 派生的 `BswModuleDescriptions`）。

**ARPackage 的类别**

`ARPackage` 的 `category` 属性取值可以作为该 `ARPackage` 内容性质的一个指示。`category` 属性的某些取值由 AUTOSAR 标准化：`STANDARD`、`BLUEPRINT`、`EXAMPLE`、`ICS`。`category` 属性自定义取值的定义适用 [TPS\_GST\_00016]。

- **BLUEPRINT**：此类包中的元素充当真实对象的一种“蓝图”。

  这特别适用于诸如 `PortInterface` 这类对象——它们并非特意被建模为“蓝图”，但仍是 `AtpBlueprint` 或 `AtpBlueprintable` 的特化。

  例如，编写工具会把这类预定义的 `PortInterface` 作为一种工具箱提供，从中可以把定义复制到真实的项目中。

  这类包中的模型元素可以只定义一部分。因此可能适用特定的语义约束。更多细节参见 [\[2\]](#ref-2) 中的 [TPS\_STDT\_00002]。

  **约束：不支持蓝图的蓝图**

  请注意，特意建模为“蓝图”的对象（例如 `PortPrototypeBlueprint`）同样位于类别为 BLUEPRINT 的包中。严格说来，这意味着它们可以成为“蓝图的蓝图”。这种间接层次并非本意，不受支持。

- **STANDARD**：由相关顶层包的提交方标准化、可以直接按原样用于处理（例如 ECU 参数定义）的元素。

  请注意，这也允许表示利益相关方特定的标准元素，因为 STANDARD 不限于 AUTOSAR 内部应用。

- **ICS**：构成实现一致性声明（**Implementation Conformance Statement**）的元素。

  **约束：ICS 不得包含蓝图**

  由于实现一致性声明始终描述一组一个或多个完整配置的软件模块，类别为 ICS 的包不允许在任何层次上包含类别为 BLUEPRINT 的子包。

  **约束：ICS 不得引用示例**

  ICS 如同生产模型，因此不得引用 EXAMPLE。这样的引用毫无用处，因为在 ICS 中目标需要被忽略。

  关于实现一致性声明内容的更多细节，参见 [\[10\]](#ref-10)。

- **EXAMPLE**：EXAMPLE 包中的元素展示如何应用（例如）STANDARD 或 BLUEPRINT 包中定义的元素。EXAMPLE 包中的元素应当被生成器等忽略。

**ARPackage 的非标准化类别**

不属于上述任一类别的模型元素应当位于一个类别由利益相关方共同商定的包中。在这种情况下也可以完全不设类别。

**约束：包的类别不得冲突**

**包类别冲突表（父类别 × 子类别，含间接子包）**

| 父类别 \ 子类别（含间接子包） | 空 | BLUEPRINT | STANDARD | EXAMPLE | ICS | custom1 | custom2 |
|-------------------------------|----|-----------|----------|---------|-----|---------|---------|
| 空                            | ok | ok        | ok       | ok      | ok  | ok      | ok      |
| BLUEPRINT                     | ok | ok        | conflict | conflict| conflict | conflict | conflict |
| STANDARD                      | ok | conflict  | ok       | conflict| conflict | conflict | conflict |
| EXAMPLE                       | ok | conflict  | conflict | ok      | conflict | conflict | conflict |
| ICS                           | ok | conflict  | conflict | conflict| ok  | conflict | conflict |
| custom1                       | ok | conflict  | conflict | conflict| conflict | ok   | conflict |
| custom2                       | ok | conflict  | conflict | conflict| conflict | conflict | ok   |

**特定类别包之间引用的规则表（引用源元素所在包的类别 × 目标包的类别）**

| 引用源元素所在包的类别 | 空 | BLUEPRINT | STANDARD | EXAMPLE | ICS | custom1 | custom2 |
|------------------------------------|----|-----------|----------|---------|-----|---------|---------|
| 空                                 | ok | ok        | ok       | ok      | ok  | ok      | ok      |
| BLUEPRINT                          | ok | ok        | ok       | conflict| ok  | conflict | conflict |
| STANDARD                           | ok | conflict  | ok       | conflict| conflict | conflict | conflict |
| EXAMPLE                            | ok | ok        | ok       | ok      | ok  | conflict | conflict |
| ICS                                | ok | conflict  | ok       | conflict<sup>2</sup> | ok | conflict | conflict |
| custom1                            | ok | ok        | ok       | ok      | ok  | ok      | ok      |
| custom2                            | ok | ok        | ok       | ok      | ok  | ok      | ok      |

> **2** 细节参见 [constr\_2573]。（表头注：目标包的类别为空时，应用父包的类别；引用源所在包同理。）

第一张表：若为某个包定义了非空类别，则其所有子包应当具有空类别或相同的类别。

第二张表：此外，“特定类别包中元素之间引用的规则”应当适用。

可以从蓝图维护一个指向由该蓝图派生的“实际”对象的引用。元类 `BlueprintMappingSet` 可用于此目的。可能适用特定的兼容性规则，并在相应的模板中定义。更多细节参见 [\[2\]](#ref-2)。

表3.1：BlueprintMappingSet

| 类         | BlueprintMappingSet                                                                                                                            |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 包         | M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping                                                                |
| 注意       | 这表示“实际”模型元素与创建它们所采用的“蓝图”之间映射的容器。标签：atp.recommendedPackage=BlueprintMappingSets                                    |
| 基类       | ARElement、ARObject、CollectableElement、Identifiable、MultilanguageReferrable、PackageableElement、Referrable                                   |
| 聚合于     | ARPackage.element                                                                                                                               |

| 属性         | 类型                | 多重性 | 类别 | 注意                                       |
|--------------|---------------------|--------|------|--------------------------------------------|
| blueprintMap | AtpBlueprintMapping | *      | aggr | 这表示该集合中一个特定的蓝图映射。           |

### 3.2. ARPackage、ARElement 与 Identifiable 等的角色

AUTOSAR 元模型使用一些抽象类来表示与模型组织相关的各种能力。图 3.2 提供了它们的概览。

![图 3.2：模型组织类概览（Synopsis of model organization classes）](Figure3-2.png)

**关于 Referrable：**

- `Referrable` 是一个抽象元类，拥有充当引用目标的 `shortName`。`Referrable` 主要用于占用空间小的引用目标，例如 `Sdg`。`Referrable` 特化为 `SingleLanguageReferrable` / `MultilanguageReferrable`。
- `SingleLanguageReferrable` 的特化适用于嵌入在已经属于多语言对象的文本中的元素（即第 9.2.8 章所述的内联元素（inline elements））。
- `MultilanguageReferrable` 的特化适用于占用空间相对较小的多语言对象，例如 `DefList`、`Traceable`。

**关于 Describable：**

- `Describable` 是一个抽象元类，表示提供描述但不作为 `Referrable` 或 `Identifiable` 的能力。此处提及仅为完整性。

**关于 Identifiable：**

- `Identifiable` 是继承自 `MultilanguageReferrable` 的抽象类。它用于标识 AUTOSAR 模型中的本质对象。相对于 `Referrable`，它提供了进一步标识元素的手段，例如 `desc`。显然，任何可被标识的东西也应当是可引用的，因此 `Identifiable` 是 `Referrable` 的特化。
- 嵌套的 `Identifiable` 建立了一个层次化的命名空间（**name space**）。

请注意，如果 `Referrable` 还能包含更进一步的 `Referrable`，那么它就不会构成层次化的命名空间，因为命名空间只由 `Identifiable` 建立。<sup>3</sup>

更多细节参见第 4.3.1 章。

- AUTOSAR 中的 `ARPackage` 是 AUTOSAR 模型中最顶层的 `Identifiable`。这个顶层 `ARPackage` 是命名空间层次的根。
- `Identifiable`（更准确地说 `Referrable`）的 `shortName` 在其包含的 `Identifiable` 内应当（不区分大小写地）唯一。例如：

  - `ARElement`（例如 `ApplicationSwComponentType`）的 `shortName` 在 `ARPackage`（它是一个 `Identifiable`）内应当唯一。但在另一个 `ARPackage` 中可能存在 `shortName` 相同的其他 `ApplicationSwComponentType`。
  - `PortPrototype` 的 `shortName` 在一个 `ApplicationSwComponentType`（它是一个 `Identifiable`）内应当唯一。但在其他 `ApplicationSwComponentType` 中可能存在同名的 `PortPrototype`。

**关于 CollectableElement：**

- `CollectableElement` 表示成为集合一部分的能力（尤其是被一个集合引用）。该元类不引入更多属性，也不引入更多可能的聚合。
- 尽管 `CollectableElement` 与 `ARElement` 相似，但两者并不相同，因为它处理的是完全不同的方面。

**关于 ARPackage：**

- `ARPackage` 可以嵌套：`ARPackage` 可以在 `arPackage` 角色中包含 `ARPackage`。
- 由此，`ARPackage` 由嵌套的分支（`ARPackage`）和叶子（`PackageableElement` 的子类，尤其是 `ARElement` 的子类）组成。
- `ARPackage` 是 `Identifiable` 的特化。否则它将无法参与命名空间层次。
- `PackageableElement` 是一个抽象类，表示对象可以被独立定义的能力。这些对象不需要上下文。这样的对象有时被称为“一等公民”（**first class citizens**）。
- `PackageableElement`（`ARElement`、`FibexElement`）不能包含更进一步的 `PackageableElement`（相应地即 `ARElement`、`FibexElement`）。

**关于 ARElement 与 FibexElement：**

- `ARElement` 是一个抽象类，通常对 AUTOSAR 模型有所贡献。
- `FibexElement` 是一个抽象类，表示元素对系统通信与拓扑描述的特定贡献能力。
- `ARElement` 与 `FibexElement` 都是 `Identifiable`。因此派生的元素也拥有 `shortName`。
- `ARElement`、`FibexElement` 可以包含从 `Identifiable` 派生的更多元素。

> **3** 尽管如此，AUTOSAR 元模型中并不出现这样的 `Referrable` 嵌套。
