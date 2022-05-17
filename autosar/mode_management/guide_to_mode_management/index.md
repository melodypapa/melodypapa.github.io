<section id="title">模式管理指南（Guide to Mode Management）</section>

# 1. 介绍

本文档主要是针对**AUTOSAR 4.0.3**及以后版本的模式管理的通用介绍。主要目的是为**AUTOSAR**的用户和开发人员提供基于示例的**AUTOSAR**模式管理不同方面的详细概述。概述会和相关示例相结合的一起解释。本文档中的代码清单可以被视为**ECU**配置的相关示例。

在第**2**章节会解释了基础的模式管理概念，例如：模式概述，模式切换的实现，模式管理器和模式用户的这些角色等。其次介绍了应用程序模式管理（**Application Mode management**）与基础软件模式管理（**Basic Software Mode management**）密切相关的依赖关系。

**BswM**是**AUTOSAR R4.0**中的中央模式管理模块（**central mode management module**），它是高度可配置的。如何实现这种配置是第3章节的主题。

由于本主题的复杂性和广泛范围，仍有一些用例尚未在此处详细描述。

* **ECU**作为网关
* **FlexRay**的通信管理（**Communication management for FlexRay**）
* 以太网通信管理（**Communication management for Ethernet**）
* Lin的通信管理（包括调度表切换）
* DCM路由路径组
* 多核ECU的**BswM**的配置

# 2. 总体机制和概念

本章节概述了模式的概念已经**AUTOSAR**中有关状态的简短定义。术语模式和状态的定义可以在第**5.1**章节中找到。模式可以看作是已一个分区（**Partition**）为范围的当前状态。它是一个全局变量，由**RTE**的调度管理器分别维护。可能的模式在**ModeDeclarationGroups**中定义。具体语法的定义可参考AUTOSAR软件组件模板[1]中定义。

模式可以用于不同的目的：

1. 首先，模式用于软件组件和基础软件模块的同步，通过模式可以启用和禁用指定的触发器，于是可执行实体（**ExecutableEntity**）的激活可以被阻止。当然可执行实体（**ExecutableEntity**）也可以在模式切换（**Mode Switch**）期间被显式触发。
2. 另一方面，模式切换可以在从一种模式转换到另一种模式期间显式触发可执行实体。例如，RTE 可以激活 OnEntry ExecutableEntity 以在进入特定模式之前初始化特定资源。在这种模式下，这个 ExecutableEntity 的触发器被激活。如果离开该模式，则调用 OnExit ExecutableEntity，它可以执行一些清理代码并且触发器将被停用。