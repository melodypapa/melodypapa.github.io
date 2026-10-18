---
title: "模式管理指南（Guide to Mode Management）"
---




## 1. 介绍

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

## 2. 总体机制和概念

本章节概述了模式的概念已经**AUTOSAR**中有关状态的简短定义。术语模式和状态的定义可以在第**5.1**章节中找到。模式可以看作是已一个分区（**Partition**）为范围的当前状态。它是一个全局变量，由**RTE**的调度管理器分别维护。可能的模式在**ModeDeclarationGroups**中定义。具体语法的定义可参考AUTOSAR软件组件模板[1]中定义。

模式可以用于不同的目的：

1. 首先，模式用于软件组件和基础软件模块的同步，通过模式可以启用和禁用指定的触发器，于是可执行实体（**ExecutableEntity**）的激活可以被阻止。当然可执行实体（**ExecutableEntity**）也可以在模式切换（**Mode Switch**）期间被显式触发。
2. 另一方面，模式切换可以在从一种模式转换到另一种模式期间显式触发可执行实体。例如，RTE 可以激活 OnEntry ExecutableEntity 以在进入特定模式之前初始化特定资源。在这种模式下，这个 ExecutableEntity 的触发器被激活。如果离开该模式，则调用 OnExit ExecutableEntity，它可以执行一些清理代码并且触发器将被停用。

### 2.1. 声明模式

AUTOSAR软件组件模板[1]定义了一种用于描述**AUTOSAR**中模式的通用机制。模式通过模式声明（**ModeDeclaration**）来定义。一个模式声明表示全局变量当前状态的一种可能取值。例如：在**ECU**状态管理中，可能存在**STARTUP**、**RUN**、**POST_RUN**、**SLEEP**等模式声明。

模式声明组（**ModeDeclarationGroup**）将多个模式声明分组在一起，其方式类似于枚举（**enumeration**）将字面量（**literal**）分组。在上面的示例中，模式声明组可以是**ECUMODE**。对于每个模式声明组，都必须定义一个初始模式（**InitialMode**），该初始模式在启动时被赋值给该变量。图2.1展示了**AUTOSAR**元模型（**Metamodel**）中模式声明、模式声明组和可执行实体之间关系的摘录。

图2.1：有关模式的元模型摘录

### 2.2. 模式管理器和模式用户

在模式管理中涉及两方：模式管理器（**mode manager**）和模式用户（**mode user**）。负责切换模式的是模式管理器，它们是唯一能够改变全局变量值的实例。模式管理器既可以是一个提供模式请求端口（**ModeRequestPort**）的软件组件，也可以是一个基础软件模块——后者在其软件组件描述中提供模式请求端口，或者在其基础软件模块描述中提供一个模式声明组。模式用户通过明确定义的机制获知模式切换，并且可以随时读取当前活动的模式。如果模式用户想切换到另一个模式，它可以向对应的模式管理器请求模式切换。

### 2.3. RTE中的模式

AUTOSAR运行环境（**RTE**）实现了模式的概念。为此，它会为每个原子软件组件（**Atomic Software Component**）的模式声明组原型（**ModeDeclarationGroupPrototype**）创建一个所谓的模式机实例（**ModeMachineInstance**）。模式机实例是一个状态机，其状态由相应模式声明组的模式声明定义。

图2.2描绘了模式声明组原型、模式管理器和模式用户之间的交互。注意，模式用户的模式切换端口并不是直接连接到模式管理器对应的**PPortPrototype**，而是连接到**RTE**的模式机实例。理解**RTE**内部模式切换的机制时，这一点非常重要。

图2.2：RTE为每个ModeDeclarationGroupPrototype实例化一个ModeMachineInstance

以前版本的基础软件模块（特别是**ECU**状态管理器模块）区分了**ECU**状态（**ECU states**）和**ECU**模式（**ECU modes**）。**ECU**模式是持续时间较长、对应用可见的**ECU**操作状态，例如：启动、关闭、休眠和唤醒。而**ECU**管理器状态通常是**ECU**管理器模块操作的连续序列，以等待外部条件满足而结束。例如：**Startup1**包含在**OS**启动之前的所有**BSW**初始化，并在**OS**将控制权交还给**ECU**管理器模块时结束。在灵活的**ECU**管理中，**ECU**状态机是在**BSW**模式管理器模块控制下的通用模式实现的。为了解决这一术语问题，状态仅在内部使用，对应用不可见。在与应用交互时，基础软件必须使用模式。

### 2.4. 基础软件调度器中的模式

基础软件调度器（**BSW Scheduler**）为基础软件模块提供了与**RTE**为软件组件所提供的类似的模式通信机制。如果基础软件模块在其基础软件模块描述中将一个模式声明组原型提供为**providedModeGroup**，则基础软件调度器会实例化一个模式机实例。因此，会为该基础软件模块提供一个**SchM_Switch** **API**，使其能够发起模式切换。模式用户必须将该模式声明组原型引用为**requiredModeGroup**，并将获得一个用于读取当前活动模式的**SchM_Mode** **API**。基础软件模块之间的模式请求可以直接通过函数调用进行通信。

对于作为模式用户的基础软件模块，获知模式切换的另一种可能性是注册一个**BSW**模块条目（**BSW Module Entry**），该条目由模式切换事件（**Mode Switch Event**）触发（另请参阅[3]）。

### 2.5. 模式通信

软件组件模板区分了模式管理器和模式用户之间以下几种不同的模式通信类型：

* **模式切换（Mode Switch）**：模式切换是从一个模式到另一个模式的当前模式转换的通信。模式切换总是由模式管理器发起。
* **模式请求（Mode Request）**：模式请求是模式用户向模式管理器发出的进入某个模式的请求。注意，并不保证模式管理器会进入该模式。此外，模式管理器必须对所有模式用户的请求进行仲裁，并决定进入哪个模式。

此外，还给出了模式代理（**mode proxies**）的概念以及多核**ECU**上模式通信的相关信息。

#### 2.5.1. 模式切换

与软件组件之间或软件组件与基础软件模块之间的所有其他通信一样，模式通过端口原型（**PortPrototype**）进行通信。每个端口原型都必须由端口接口（**PortInterface**）类型化。在模式通信的情况下，存在所谓的模式切换接口（**mode switch interface**），它们是端口接口。如图2.3所示。每个模式切换接口都有且只有一个模式声明组原型，该原型由多个模式声明组成。任何一个模式声明都表示模式声明组中的一个模式，其中之一被定义为初始模式。

图2.3：模式切换接口

之所以需要这些模式切换，是因为软件组件需要能够对模式管理器发起的状态变化做出反应。根据配置，有两种机制可供软件组件对模式变化做出反应：

1. 模式切换事件（**ModeSwitchEvent**）可以触发**OnEntry**、**OnTransition**或**OnExit**可执行实体。
2. **RTE**事件（**RTEEvent**）可以在某个模式下被禁用，从而阻止相应可执行实体的执行。

#### 2.5.2. 模式请求

模式请求在从模式请求者（模式仲裁**SW-C**或通用**SW-C**）到模式管理器的路径上进行分发。然后每个**ECU**上的模式管理器必须做出决定并发起本地的模式切换。因此，仲裁结果仅在每个**ECU**上使用**RTE**的模式切换机制在本地进行通信。

对于模式请求，模式的通信方式与模式切换略有不同：模式请求不使用模式声明组。

模式的请求通过标准的**SenderReceiverInterface**完成。与模式切换接口不同，被请求的模式不是由模式声明组给出的，而是由一个必须包含枚举类型的**VariableDataPrototype**给出的。该枚举由一个集合组成，其中包含可以被请求的模式。

模式请求可以在整个系统中分发。对于应用模式和车辆模式，模式请求者的请求必须分发到所有受影响的**ECU**。这意味着模式请求者与模式管理器之间是1:n的连接。在**AUTOSAR**中，这只能通过发送者-接收者通信（**Sender-Receiver Communication**）实现。模式管理器只需要模式请求者所请求模式的信息，而不需要模式切换。模式管理器为每个模式请求者提供一个发送者-接收者端口。为了实际传输该信号，**COM**应使用带有信号超时通知**RTE**的周期信号。模式管理器将使用数据元素过期事件（**data element outdated event**）来释放模式请求。

#### 2.5.3. 模式切换和模式请求的一致性

如上所述，模式切换接口使用模式声明组工作，而模式请求接口通过包含枚举类型的**VariableDataPrototype**传递参数。

配置工具有责任确保两种表示形式所表示数据的一致性等价。这意味着枚举的元素必须与模式声明组的元素精确匹配。或者换一种说法：其中一个接口中可用的所有模式，在另一个接口中也必须可用。

#### 2.5.4. 模式代理

目前，**AUTOSAR**有一个约束：只有本地软件组件才允许与服务组件（**ServiceComponent**）通信。因此，软件组件无法从远程（例如：基础软件模式管理器）请求模式。为了克服这一限制，**AUTOSAR Release 4.0**引入了所谓的**ServiceProxySwComponentType**。图2.4描绘了这一概念。

对于应用软件和**RTE**而言，**ServiceProxySoftwareComponentType**的行为类似于一个"普通的"**AtomicSwComponentType**，但它实际上是一个**AUTOSAR**服务的代理。这意味着一方面，它必须通过服务端口与它所代表的**ECU**本地的**ServiceSwComponentType**通信；另一方面，它必须向**ApplicationSwComponentType**提供相应的端口原型。在元模型中，除了类不同之外，**ServiceProxySwComponentType**与**ApplicationSwComponentType**没有区别。作为代理满足语义所施加的限制是实现者的责任。**ServiceProxySwComponentType**与**ApplicationSwComponentType**的主要区别在于系统层面：**ServiceProxySwComponentType**的一个原型可以被映射到多个**ECU**，即使它在**VFB**系统中只出现一次，因为这样的原型在每个**ECU**上都是必需的，在那里它需要寻址一个本地的**ServiceSwComponentType**。由此导致的结果是，**ServiceProxySwComponentType**只能通过网络接收信号，而不能发送信号（另请参阅[1]）。

图2.4：通过ServiceProxySwComponent的通信

#### 2.5.5. 多核ECU上的模式通信

**RTE**能够在**ECU**的不同分区之间同步模式机实例。这使得这样的配置成为可能：一个提供端口的模式声明组原型可以连接到来自多个分区的接收端口的模式声明组原型。因此，一个模式声明组原型的模式用户可以分布在多个分区上。

图2.5：示例配置

根据[SWS_Rte_02665]，在一次模式转换期间，模式机实例会执行一个包含10个步骤的序列：

1. 激活模式禁用（**mode disablings**）
2. 等待受下一模式的模式禁用依赖（**ModeDisablingDependency**）影响的可执行实体终止
3. 执行**OnExit**可执行实体
4. 等待所有**OnExit**可执行实体终止
5. 执行**OnTransition**可执行实体
6. 等待所有**OnTransition**可执行实体终止
7. 执行**OnEntry**可执行实体
8. 等待所有**OnEntry**可执行实体终止
9. 停用前一模式的模式禁用，激活当前模式的模式禁用
10. 触发模式切换确认事件（**ModeSwitchAckEvent**）

第1至9步可以在每个**CPU**内核上并行执行，分别针对分布在相应内核上的模式用户。第10步只有在对整个模式机实例完成其他步骤后才会执行。尽管如此，某些应用特定的用例可能要求第1至9步具有更高程度的同步，例如：在**OnTransition**可执行实体之前执行所有**OnExit**可执行实体。因此，**RTE**提供了配置同步点（**synchronization points**）的机会（更多细节请参阅[ECUC_Rte_09127]、[ECUC_Rte_09128]和[ECUC_Rte_09129]）。

对于模式用户分布在不同分区上的模式机实例，在分区重启的情况下无法将其重新初始化为默认模式。这会干扰其他仍在运行的分区。因此，处理分区重启唯一适用的策略是将**modeManagerErrorBehavior.errorReactionPolicy**设置为**lastMode**，它规定模式用户保持其最后已知的模式。

## 3. 基础软件模式管理器的配置

**BSW**模式管理器是实现车辆模式管理和应用模式管理概念中驻留在**BSW**部分的模块。它的职责是基于规则对来自应用层软件组件或其他基础软件模块的模式请求进行仲裁，并根据仲裁结果执行动作。

从功能的角度来看，**BswM**负责使基础软件进入这样一种状态：基础软件能够正常运行并满足功能需求。

**BswM**的配置非常依赖于具体项目和**ECU**。因此**AUTOSAR**无法将其标准化。尽管如此，**BswM**实现在特定情况下应以特定方式行为。本章首先介绍**BswM**的总体概念，它在某种程度上是一个由用户描述的规则的执行环境。随后描述**ECU**生命周期中的典型场景，并给出如何配置**BswM**的示例。

### 3.1. 配置和集成BswM的过程

将**BswM**配置并集成到**ECU**项目中的步骤与其他基础软件模块相同。尽管如此，为了更好地理解后续步骤，此处仍对其进行描述。通常需要执行以下操作：

1. 创建模块的**ECUC**配置。对于**BswM**，该配置包含：
   * 必需的**ModeRequestSources**
   * 提供的**ModeSwitchPorts**
   * 对规则和动作列表的描述
2. 该配置作为模块生成器的输入，生成器会创建：
   * **AUTOSAR**接口的软件组件描述
   * 模块的实现（本文档假定**BswM**的实现会在很大程度上被生成）
3. 最后一步是通过将软件组件的端口与**BswM**对应的端口相连接，将模块集成到**ECU**中。

### 3.2. BswM配置的语义：接口和行为方面

通常，**BswM**可以被看作一个状态机，它由其接口和行为描述定义。该状态机的输入动作是模式请求。每个模式请求在**BswM**的**ECU**配置中被描述为一个**BswMModeRequestSource**。这些模式请求可以是不同的类型（**C** **API**调用、通过**RTE**的模式请求、通过**RTE**的模式通知等），但在内部它们以相同的方式处理。

当一个模式被请求时，该**BswMModeRequestSource**的内部镜像会被更新，并且根据配置会触发一次规则评估，其结果是执行预定义的动作列表。动作列表对动作进行分组。通常，动作是对**RTE**或调度管理器中模式切换的触发，但也存在一些预定义的动作会改变某些基础软件模块的状态。

#### 3.2.1. BswM的接口

接口由**BswMModeRequestSource**和**BswMActionListItem**配置容器定义。

##### 3.2.1.1. 模式请求

**BswMModeRequestSource**是一个选择容器（**ChoiceContainer**），可以是以下几种类型：

1. 在**BswM**规范中定义的**C** **API**。基础软件模块可以直接调用**BswM**的**C** **API**，**BswM**会将其在内部转换为模式请求。例如：对**API**

```c
BswM_CanSM_CurrentState( NetworkHandleType Network, CanSM_BswMCurrentStateType CurrentState )
```

的调用，需要根据标识事件发生通道的参数**Network**映射到不同的模式请求端口。参数**CurrentState**则包含被请求的模式。由**BswM**标准化接口定义的模式请求将在3.2.2.2节中更详细地描述。

2. 由**SenderReceiverInterface**类型化的**RPort**（**BswMSwcModeRequest**）：对于此类型的每个容器，**BswM**必须在其服务组件描述中创建一个对应的**RPort**。
3. 由**ModeSwitchInterface**类型化的**RPort**（**BswMSwcModeNotification**）：对于此类型的每个容器，**BswM**必须在其服务组件描述中创建一个对应的**RPort**。由于它由**ModeSwitchInterface**类型化，**BswM**作为该模式机实例的模式用户，会在模式管理器执行**rte_switch**时获得通知。
4. 模式声明组原型（**BswMBswModeNotification**）：对于此类型的每个容器，**BswM**必须在其基础软件模块描述中以**ModeDeclarationGroupPrototype**的角色创建一个对应的模式声明组原型。在这种情况下，**BswM**同样作为模式用户，但模式机实例由调度管理器维护。因此，当模式管理器（例如：另一个基础软件模块）执行**SchM_Switch**调用时，**BswM**会获得通知。

##### 3.2.1.2. 可用动作

**BswMActionListItem**可以是以下几种类型：

1. 来自其他**BswM**模块的**C** **API**，它们在动作列表执行期间被直接调用：
   * BswMComMAllowCom
   * BswMComMModeLimitation
   * BswMComMModeSwitch
   * BswMDeadlineMonitoringControl
   * BswMEcuMGoDown
   * BswMEcuMSelectShutdownTarget
   * BswMEcuMStateSwitch
   * BswMJ1939Rm
   * BswMLinScheduleSwitch
   * BswMNMControl
   * BswMPduGroupSwitch
   * BswMPduRouterControl
   * BswMRteSwitch
   * BswMSchMSwitch
   * BswMSwitchIPduMode
   * BswMTriggerIPduSend
   * BswMUserCallout
2. 由**ModeSwitchInterface**类型化的**PPort**（**BswMSwitchPort**）：对于此类型的每个容器，如果满足某个配置条件（参见**BswM SWS**），**BswM**必须在其服务组件描述中创建一个对应的**PPort**。
3. 模式声明组原型（**SwitchPort**）：对于此类型的每个容器，如果满足某个配置条件（参见**BswM SWS**），**BswM**必须在其基础软件模块描述中以**providedModeGroup**的角色创建一个对应的模式声明组原型。在这种情况下，**BswM**同样作为模式管理器，但模式机实例由调度管理器维护。

#### 3.2.2. 用伪代码定义的接口

以下各小节用伪代码定义**BswM**的接口。

##### 3.2.2.1. 模式切换和模式请求接口

清单3.1展示了**BswM**配置中模式切换接口的一个示例。其中创建了一个模式声明组和一个模式切换接口。该模式切换接口使用已定义的模式声明组作为原型，其中**exampleModes**是该模式切换接口的短名称。

```
modeGroup MDG_ApplicationModes { APP_ACTIVE, APP_STARTING, APP_INACTIVE }
interface modeSwitch MSIF_ApplicationModes { mode MDG_ApplicationModes appMode }
```

清单3.1：ECU整体模式的模式切换接口

清单3.2以示例的形式展示了与清单3.1的模式切换接口相对应的模式请求接口的配置。基于此**BswM**配置，将创建一个包含模式声明和接口的**Arxml**描述。该**arxml**的摘录如清单3.3所示。

```
enum ENUM_ApplicationModes{ ModeA, ModeB, ModeC }
interface senderReceiver exampleModeRequestPort { data ENUM_ApplicationsModes exampleModeRequest }
```

清单3.2：模式请求接口的声明

```
<SENDER-RECEIVER-INTERFACE>
  <SHORT-NAME> exampleModeRequestPort </SHORT-NAME>
  <IS-SERVICE> false </IS-SERVICE>
  <DATA-ELEMENTS>
    <VARIABLE-DATA-PROTOTYPE>
      <SHORT-NAME> exampleModeRequest </SHORT-NAME>
      <!--...-->
      <TYPE-TREF DEST= "APPLICATION-PRIMITIVE-DATA-TYPE" > ENUM_ApplicationModes </TYPE-TREF>
    </VARIABLE-DATA-PROTOTYPE>
  </DATA-ELEMENTS>
</SENDER-RECEIVER-INTERFACE>
<!--...-->
<APPLICATION-PRIMITIVE-DATA-TYPE>
  <SHORT-NAME> ENUM_ApplicationModes </SHORT-NAME>
  <CATEGORY> VALUE </CATEGORY>
  <SW-DATA-DEF-PROPS>
    <SW-DATA-DEF-PROPS-VARIANTS>
      <SW-DATA-DEF-PROPS-CONDITIONAL>
        <COMPU-METHOD-REF DEST= "COMPU-METHOD" > ENUM_ApplicationModes_def </COMPU-METHOD-REF>
      </SW-DATA-DEF-PROPS-CONDITIONAL>
    </SW-DATA-DEF-PROPS-VARIANTS>
  </SW-DATA-DEF-PROPS>
</APPLICATION-PRIMITIVE-DATA-TYPE>
<!--...-->
<COMPU-METHOD>
  <SHORT-NAME> ENUM_ApplicationModes_def </SHORT-NAME>
  <CATEGORY> TEXTTABLE </CATEGORY>
  <COMPU-INTERNAL-TO-PHYS>
    <COMPU-SCALES>
      <COMPU-SCALE>
        <LOWER-LIMIT INTERVAL-TYPE= "CLOSED" > 0 </LOWER-LIMIT>
        <UPPER-LIMIT INTERVAL-TYPE= "CLOSED" > 0 </UPPER-LIMIT>
        <COMPU-CONST> <VT> ModeA </VT> </COMPU-CONST>
      </COMPU-SCALE>
      <COMPU-SCALE>
        <LOWER-LIMIT INTERVAL-TYPE= "CLOSED" > 1 </LOWER-LIMIT>
        <UPPER-LIMIT INTERVAL-TYPE= "CLOSED" > 1 </UPPER-LIMIT>
        <COMPU-CONST> <VT> ModeB </VT> </COMPU-CONST>
      </COMPU-SCALE>
      <COMPU-SCALE>
        <LOWER-LIMIT INTERVAL-TYPE= "CLOSED" > 2 </LOWER-LIMIT>
        <UPPER-LIMIT INTERVAL-TYPE= "CLOSED" > 2 </UPPER-LIMIT>
        <COMPU-CONST> <VT> ModeC </VT> </COMPU-CONST>
      </COMPU-SCALE>
    </COMPU-SCALES>
  </COMPU-INTERNAL-TO-PHYS>
</COMPU-METHOD>
```

清单3.3：模式请求接口ARXML描述的摘录

每一个发向**BswM**的模式请求都必须被映射到一个受限的取值集合上，这使得集成者可以据此定义仲裁规则。

**ECU**模式可以由**BswM**通过**EcuM_SetState** **API**来设置。

目的：通过此接口，**BswM**设置**EcuM**的当前状态。

```
Signature: EcuM_SetState(EcuM_StateType State)

Modes:
modeGroup EcuM_StateType { ECUM_STATE_STARTUP, ECUM_STATE_APP_RUN,
ECUM_STATE_APP_POST_RUN, ECUM_STATE_SHUTDOWN, ECUM_STATE_SLEEP }
```

##### 3.2.2.2. 由BswM标准化接口定义的模式请求端口

在**BswM**配置中，必须定义模式请求源。以下的模式请求端口是由**BswM**的**API**隐式定义的。本小节对这些端口接口进行汇总。

下面的模式声明组在**AUTOSAR**规范的相应**SWS**文档中以**C**枚举（**C-Enum**）的形式定义。尽管如此，此处仍以**BswM**配置的形式引用它们，它们作为本文档其余部分的基础。有关模式的定义，请参阅**SWS**文档中对**C**枚举的定义。

###### 3.2.2.2.1. BswMComMIndication

目的：由**ComM**调用的函数，用于指示其当前状态。

```
Signature: void BswM_ComM_CurrentMode( NetworkHandleType Network, ComM_ModeType RequestedMode )
Modes:     modeGroup ComM_ModeType
Example:   request ComMIndication ComM_Mode_Channel1 {
             processing IMMEDIATE
             initialValue COMM_NO_COM_NO_PENDING_REQUEST
             source MyComM.ComMChannel1
           }
```

**注意：** 对于由**Network**参数标识的每个**ComM**通道，都必须创建一次此模式请求源。

###### 3.2.2.2.2. BswMComMPncRequest

目的：由**ComM**调用的函数，用于指示部分网络（**partial network**）的当前状态。

```
Signature: void BswM_ComM_CurrentPNCMode( PNCHandleType PNC, ComM_PncModeType CurrentPncMode )
Modes:     modeGroup ComM_PncModeType
Example:   request ComMPncRequest PNC1 {
             processing IMMEDIATE
             initialValue PNC_NO_COMMUNICATION
             source MyComM.ComMPnc1
           }
           request ComMPncRequest PNC2 {
             processing IMMEDIATE
             initialValue PNC_NO_COMMUNICATION
             source MyComM.ComMPnc2
           }
           request ComMPncRequest PNC3 {
             processing IMMEDIATE
             initialValue PNC_NO_COMMUNICATION
             source MyComM.ComMPnc3
           }
```

**注意：** 对于每个部分网络，都必须创建一次此模式请求源。

###### 3.2.2.2.3. BswMDcmComModeRequest

目的：由**DCM**调用的函数，用于指示**CommunicationControl**的当前状态。

```
Signature: void BswM_Dcm_CommunicationMode_CurrentState( NetworkHandleType Network, Dcm_CommunicationModeType RequestedMode )
Modes:     modeGroup Dcm_CommunicationModeType
Example:   request DcmComModeRequest BswM_Dcm_CommunicationMode_CurrentState {
             processing IMMEDIATE
             initialValue DCM_ENABLE_RX_TX_NORM
             network "network1"
           }
```

###### 3.2.2.2.4. BswMCanSMIndication

目的：由**CanSM**调用的函数，用于指示其当前状态。

```
Signature: void BswM_CanSM_CurrentState( NetworkHandleType Network, CanSM_BswMCurrentStateType CurrentState )
Modes:     modeGroup CanSM_BswMCurrentStateType
Example:   request CanSMIndication CanSM_Can1 {
             processing IMMEDIATE
             initialValue CANSM_BSWM_NO_COMMUNICATION
             source MyComM.CanNet1
           }
           request CanSMIndication CanSM_Can2 {
             processing IMMEDIATE
             initialValue CANSM_BSWM_NO_COMMUNICATION
             source MyComM.CanNet2
           }
```

**注意：** 对于每个**CAN**通道，都必须创建一次此模式请求源。

###### 3.2.2.2.5. BswMEthSMIndication

目的：由**EthSM**调用的函数，用于指示其当前状态。

```
Signature: void BswM_EthSM_CurrentState( NetworkHandleType Network, EthSM_NetworkModeStateType CurrentState )
Modes:     modeGroup EthSM_NetworkModeStateType
Example:   request EthSMIndication EthSM_Network1 {
             processing IMMEDIATE
             initialValue ETHSM_NO_COMMUNICATION
             source MyComM.EthSmNetwork
           }
```

**注意：** 对于每个以太网通道，都必须创建一次此模式请求源。

###### 3.2.2.2.6. BswMFrSMIndication

目的：由**FrSM**调用的函数，用于指示其当前状态。

```
Signature: void BswM_FrSM_CurrentState( NetworkHandleType Network, FrSM_BswM_StateType CurrentState )
Modes:     modeGroup FrSM_BswM_StateType
Example:   request FrSMIndication FrSM_BswM_StateType {
             processing IMMEDIATE
             initialValue FRSM_BSWM_READY
             source MyComM.EthSmNetwork
           }
```

**注意：** 对于每个**FlexRay**集群（**cluster**），都必须创建一次此模式请求源。

###### 3.2.2.2.7. BswMLinSMIndication

目的：由**LinSM**调用的函数，用于指示其当前状态。

```
Signature: void BswM_LinSM_CurrentState( NetworkHandleType Network, LinSM_ModeType CurrentState )
Modes:     modeGroup LinSM_ModeType
Example:   request LinSMIndication LinSM_CurrentState {
             processing IMMEDIATE
             initialValue LINSM_NO_COM
             source MyComM.LinSMChannel
           }
```

**注意：** 对于每个**LIN**通道，都必须创建一次此模式请求源。

###### 3.2.2.2.8. BswMEcuMRequestedState

目的：**EcuM**通过此接口基于**RUN**请求协议的结果向**BswM**请求一个状态。

```
Signature:  BswM_EcuM_RequestState( EcuM_StateType State, EcuM_RunStatusType CurrentStatus)
Modes:      modeGroup EcuM_StateType { ECUM_STATE_APP_RUN, ECUM_STATE_APP_POST_RUN }
Parameter:  EcuM_RunStatusType { ECUM_RUNSTATUS_UNKNOWN, ECUM_RUNSTATUS_REQUESTED,
            ECUM_RUNSTATUS_RELEASED }
```

###### 3.2.2.2.9. BswMEcuMCurrentState

```
Signature: BswM_EcuM_CurrentState(EcuM_StateType CurrentState)
```

###### 3.2.2.2.10. BswMEcuMWakeupSource

目的：由**EcuM**调用的函数，用于指示唤醒源的当前状态。

```
Signature: void BswM_EcuM_CurrentWakeup( EcuM_WakeupSourceType source, EcuM_WakeupStatusType state )
Modes:     modeGroup EcuM_WakeupStatusType
Example:   request EcuMWakeupSource EcuM_WakeupSource {
             processing IMMEDIATE
             initialValue ECUM_WKSTATUS_NONE
             source MyEcuM.EcuMWakeupSource1
           }
```

**注意：** 对于每个唤醒源，都必须创建一次此模式请求源。

###### 3.2.2.2.11. BswMLinScheduleIndication

目的：由**LinSM**调用的函数，用于指示特定**LIN**通道当前活动的调度表。

```
Signature: void BswM_LinSM_CurrentSchedule( NetworkHandleType Network, LinIf_SchHandleType CurrentSchedule )
```

所报告的模式取决于**LIN**状态管理器中配置的调度表。

```
Example: request LinScheduleIndication LinSM1_CurrentSchedule {
           processing IMMEDIATE
           initialValue TBD
           source MyLinSM.LinSMChannel
         }
```

###### 3.2.2.2.12. BswMLinTpModeRequest

目的：由**LinTP**调用的函数，用于为相应的**LIN**通道请求模式。**LinTp_Mode**主要与应当使用的**LIN**调度表相关。

```
Signature: void BswM_LinTp_RequestMode( NetworkHandleType Network, LinTp_Mode LinTpRequestedMode )
Modes:     modeGroup LinTp_Mode
Example:   request LinTpModeRequest LinTp_Mode {
             processing IMMEDIATE
             initialValue LINTP_APPLICATIVE_SCHEDULE
             source MyLinIF.config0.LinIFChannel
           }
```

###### 3.2.2.2.13. BswMNvMJobModeIndication

目的：指示多块作业（**multiblock job**）的当前状态。该作业通过**BswMNvmService**标识，例如：**0x0c**表示**NvmReadAll**，**0x0d**表示**NvmWriteAll**。

```
Signature: void BswM_NvM_CurrentJobMode( uint8 ServiceId, NvM_RequestResultType CurrentJobMode )
Modes:     modeGroup NvM_RequestResultType
Example:   request NvMJobModeIndication NvMWriteAllJobMode {
             service WriteAll
             initialValue NVM_BLK_NOT_OK
             processing IMMEDIATE
           }
           request NvMJobModeIndication NvMReadAllJobMode {
             service ReadAll
             initialValue NVM_BLK_NOT_OK
             processing IMMEDIATE
           }
```

###### 3.2.2.2.14. BswMNvMRequest

目的：通过此模式请求源，**NvM**指示指定数据块的当前状态。

```
Signature: void BswM_NvM_CurrentBlockMode( NvM_BlockIdType Block, NvM_RequestResultType CurrentBlockMode )
Modes:     modeGroup NvM_RequestResultType
```

###### 3.2.2.2.15. BswMJ1939NmIndication

```
Signature: void BswM_J1939Nm_StateChangeNotification( NetworkHandleType nmNetworkHandle, uint8 Node, Nm_StateType nmCurrentState )
Modes:     modeGroup Nm_StateType
Example:   request BswMJ1939NmIndication J1939NmState {
             network "Channel1"
             node "Node1"
             initialValue NM_STATE_UNINIT
             processing IMMEDIATE
           }
```

**注意：** 对于由**J1939**网络管理所管理的每个通道，都必须配置此模式请求源。目前**ARText**不支持这种类型的模式请求源。

###### 3.2.2.2.16. BswMWdgMRequestPartitionReset

```
Signature: void BswM_WdgM_RequestPartitionReset( ApplicationType Application )
Modes:     modeGroup WdgM_PartitionResetType
Example:   request WdgMRequestPartitionReset WdgM_RequestResetPart1 {
             processing IMMEDIATE
             initialValue WDGM_PARTITION_RESET_NOTREQUESTED
             source MyEcuC.eCucPartition
           }
```

**注意：** 对于每个可由看门狗管理器模块请求重置的分区，都必须创建一次此模式请求源。

###### 3.2.2.2.17. BswMJ1939DcmBroadcastStatus

```
Signature: void BswM_J1939DcmBroadcastStatus( uint16 networkMask )
Modes:     modeGroup J1939DcmBroadcastStatusType
Example:   request BswMJ1939DcmBroadcastStatus J1939BroadcastStatusChannel1 {
             processing IMMEDIATE
             initialValue NETWORK_DISABLED
             source MyComM.CanNet1
           }
```

**注意：** 这是对每个网络所期望的广播状态的通知，由**DM13**触发。

##### 3.2.2.3. 可配置的模式请求端口

除了由**BswM**标准化接口所定义的接口之外，还可以通过配置参数定义额外的模式请求端口。

例如：对于与应用程序的交互，应用软件组件至少需要将其当前状态通知**BswM**。这可以通过定义一个模式请求端口来实现，如清单3.4所示。随后**BswM**会创建一个由**SenderReceiverInterface**类型化的对应**RPort**。

```
request SwcModeRequest App1ModeRequest {
  source MSIF_ApplicationModes.appMode
  processing IMMEDIATE
  initialValue ModeA
}
```

清单3.4：应用模式请求端口

注意，对模式声明组原型的引用可能具有误导性。其含义是：**BswM**会创建一个包含**VariableDataPrototype**的**SenderReceiverInterface**。该**VariableDataPrototype**的**SwDataDefProps**引用一个**CompuMethod**，该**CompuMethod**定义了一个与所引用模式声明组原型相对应的枚举。

```
request SwcModeNotification App1ModeNotification {
  source MSIF_ApplicationModes.appMode
  processing IMMEDIATE
  initialValue ModeA
}
```

清单3.5：应用模式通知

清单3.5展示了模式通知端口的声明。注意，与清单3.4相反，在这种情况下**BswM**将生成一个由**ModeSwitchInterface**类型化的**RPort**。当模式管理器发起模式切换时，**BswM**会通过模式切换通知获得通知。

```
request BswModeNotification EcuMode {
  source MSIF_EcuMode.ecuMode
  processing IMMEDIATE
  initialValue ECU_STARTUP_ONE
}
```

清单3.6：基础软件模式通知

清单3.6展示了一个模式通知端口的声明。如果配置了这样的端口，**BswM**配置工具将创建一个**requiredModeGroup**模式声明组原型，这样当相应的模式管理器通过调用**SchM_Switch** **API**发起模式切换时，**BswM**就会通过调度管理器获得模式切换的通知。

##### 3.2.2.4. 可配置的模式切换端口

**BswM**可以通过配置的**BswMSwitchPort**发送模式切换。对于一个已配置的**BswMSwitchPort**，根据配置（参见**BswM SWS**），**BswM**可以生成**PPortPrototype**、**providedModeGroups**模式声明组原型，或者两者同时生成。清单3.7展示了一个**BswMSwitchPort**的示例。

```
switchport EcuMode { modeSwitchinterface MSIF_EcuMode }
```

清单3.7：可配置模式切换端口的示例

#### 3.2.3. BswM行为的配置

**BswM**的行为通过规则和动作列表来指定。规则是一个逻辑表达式，它组合各**ModeRequestTypeMap**的当前值。每条规则的评估结果会导致执行其**true**或**false**动作列表。

**ModeControl**容器包含这些动作列表。一个动作列表可以由一组原子动作、其他"嵌套的"动作列表组成，也可以引用（嵌套的）规则，这些规则会在该动作列表的上下文中被评估。

下面的示例展示了一个简单的规则，它激活专用**CAN**通道的**I-PDU**组。根据此规则，**BswM**必须提供一个名为**Can1_Indication**的**CanSMIndication**类型的模式请求端口。这是一个来自基础软件模块的模式请求，在此例中来自**CAN**状态管理器。在代码中，此模式请求端口对应于[4]中[SWS_BswM_00049]所描述的**API BswM_CanSM_CurrentState**。**source**参数标识此模式请求源端口所属的网络。由**BswM**的配置工具负责为所引用的**ECUC**容器分配**API**所需的正确参数。

该模式请求源端口的初始值为**CAN_SM_BswM_NO_COMMUNICATION**。

**processing immediate**意味着每一条引用此模式请求源端口的规则评估都会被立即处理。每个立即模式请求都会触发引用它的规则的评估。如果此参数在模式请求的情况下配置为**deferred**，那么规则的评估将被推迟到**BswM**主函数的下一次运行。**BswM**不支持对延迟模式请求的排队评估。因此，延迟模式请求具有"最后者最优"（**last-is-best**）语义：只有**BswM**主函数执行之前发出的最后一个模式请求会被使用。

下面的示例展示了一条名为**canIPDUActivation**的仲裁规则。其总体内容不言自明。**initial**参数指定规则评估的初始结果为**false**。

```
rule checkApp1Request initially false {
  if ( App1ModeRequest == MDG_ApplicationModes.ModeA
       && EcuMode == MDG_EcuMode.ECU_RUN)
  {
    actionlist checkApp1RequestTrueActions
  }
}
actions checkApp1RequestTrueActions on condition {
  ComMAllowCom MyComM.CanNet1 true
  SchMSwitch EcuMode : ECU_RUN
}
```

清单3.8：规则示例

在事件发生后，规则在哪个时间点被执行取决于参数**BswMActionListExecution**。要么每次规则被评估且具有相应结果时都执行，要么仅当评估结果与上一次评估相比发生变化时才执行。这分别称为触发执行（**triggered**）和条件执行（**conditional**）。

表3.1概述了在哪些情况下动作列表会被执行或不被执行。触发型动作列表在规则评估结果发生变化时被执行（触发）；条件型动作列表仅取决于评估的当前结果（条件），而不论其是否发生了变化。

表3.1：动作列表的执行取决于参数BswMActionListExecution

| 评估结果（旧）→（新） | true → true | true → false | false → false | false → true |
| --- | --- | --- | --- | --- |
| TrueActionList | CONDITION | - | - | TRIGGERED/CONDITION |
| FalseActionList | - | TRIGGERED/CONDITION | CONDITION | - |

### 3.3. ECU状态管理

在启动和关闭期间，**BswM**的任务是以与旧版**AUTOSAR**版本中**ECU**管理器（**ECUM**）类似的方式初始化所有基础软件模块。为此，需要定义下面的模式声明组，它向应用软件组件指示**ECU**的整体状态，并用于内部规则仲裁。

```
modeGroup MDG_EcuMode { ECU_RUN, ECU_APP_RUN, ECU_APP_POST_RUN, ECU_GO_SLEEP,
                        ECU_GO_OFF_ONE, ECU_SLEEP, ECU_GO_OFF_TWO, ECU_STARTUP_ONE,
                        ECU_STARTUP_TWO, ECU_RESET_READY }
interface modeSwitch MSIF_EcuMode { mode MDG_EcuMode ecuMode }
```

清单3.9：用于ECU整体状态管理的模式声明组

该模式声明组的初始模式为**ECU_STARTUP_ONE**。

#### 3.3.1. ECU模式处理

**ECU**模式处理是在**AUTOSAR 4.2.1**中随"具有灵活状态机的**ECU**状态管理器"和**BSW**模式管理器这两个**BSW**模块引入的。**ECU**状态管理器为**SW-C**提供了一个公共接口，用于请求和释放**RUN**与**POST_RUN**模式。

**ECU**状态管理器（**EcuM**）不包含自己的状态机。它应接收来自**BswM**的状态通知，并将其传播给**RTE**。

**ECU**模式处理提供了以下**API**：

目的：通过此接口，**EcuM**将**ECU**模式的当前模式通知**BswM**。

```
Signature: BswM_EcuM_CurrentState( EcuM_StateType CurrentState )
Modes:     modeGroup EcuM_StateType { ECUM_STATE_STARTUP, ECUM_STATE_APP_RUN,
           ECUM_STATE_APP_POST_RUN, ECUM_STATE_SHUTDOWN, ECUM_STATE_SLEEP }
```

* **EcuM_CurrentState**：由**EcuM**通过接口**BswM_EcuM_CurrentState()**设置。当**RTE**给出其反馈后，**EcuM**会设置该状态。
* **RUNRequested**：由**EcuM**根据**RUN**请求协议的结果，通过接口**BswM_EcuM_RequestedState()**设置。
* **POSTRUNRequested**：由**EcuM**根据**RUN**请求协议的结果，通过接口**BswM_EcuM_RequestedState()**设置。

下面的**BswM**规则展示了**ECU**模式处理中**EcuM**与**BswM**之间交互的一个示例。注意，这些**BswM**规则不足以构成一个完整的系统。还需要更多的**BswM**规则来覆盖例如**NvM**、唤醒处理和诊断等方面。完整示例请参阅3.3.2节。

##### 3.3.1.1. 启动（Startup）

**STARTUP**模式在**RTE**启动期间使用。所有驱动程序初始化完成后，设置**RUN**模式：

```
rule SwitchToStartup initially false {
  if (EcuMode == ECUM_STARTUP) {
    actionlist SwitchToStartup
  }
}
actions SwitchToStartup on condition {
  custom "EcuM_DriverInitListTwo()"
  custom "Rte_Start()"
  custom "EcuM_DriverInitListThree()"
  custom "ComM_CommunicationAllowed(TRUE)"
  custom "EcuM_SetState(ECUM_STATE_APP_RUN)"
}
```

##### 3.3.1.2. 运行（Running）

当所有**EcuM**用户都释放了**RUN**模式后，**EcuM**将**RUNRequested**模式设置为**RELEASED**。

```
Rule SwitchToPostRun initially false {
  if (EcuM_CurrentState==RUN && RUNRequested == RELEASED) {
    actionlist SwitchToPostRun
  }
}
actions SwitchToPostRun on condition {
  custom "CommunicationAllowed(FALSE)"
  custom "EcuM_SetState(ECUM_STATE_APP_POST_RUN)"
}
```

**SWC**可以在**POST_RUN**期间请求**RUN**模式。下面的**BswM**规则在至少一个**EcuM**用户请求了**RUN**模式时切换回**RUN**模式。

```
rule SwitchBackToRunMode initially false {
  if (EcuM_CurrentState==POST_RUN && RUNRequested == REQUESTED
      && POSTRUNRequested == RELEASED)
  {
    actionlist SwitchBackToRunMode
  }
}
actions SwitchBackToRunMode on condition {
  custom "ComM_CommunicationAllowed(TRUE)"
  custom "EcuM_SetState(ECUM_STATE_APP_RUN)"
}
```

##### 3.3.1.3. 关机和睡眠（Shutdown and Sleep）

下面的**BswM**规则仅演示了到**SLEEP**模式的切换。

```
rule SwitchToShutdownMode initially false {
  if (EcuM_CurrentState==POST_RUN && RUNRequested == RELEASED
      && POSTRUNRequested == RELEASED)
  {
    actionlist SwitchToShutdownMode
  }
}
actions SwitchToShutdownMode on condition {
  custom "EcuM_SetState(ECUM_STATE_SLEEP)"
}
```

注意，对于一个完整运行的系统，还需要更多的**BswM**规则。

#### 3.3.2. ECU模式处理的默认状态

本章描述了一种使用软件组件的方案，这些软件组件的设计目标是与"具有固定状态机的**ECU**状态管理器（**EcuM**）"协同工作——该管理器已不再是当前**AUTOSAR**规范的一部分。尽管如此，这种方法仍被广泛使用，并且受益于标准接口（例如：**RUN**请求协议）。这意味着，这里描述的是一个基于"具有灵活状态机的**EcuM**与**BswM**"的方案，由它实现固定状态机**EcuM**的行为。

图3.1展示了该架构方案的概览。为了使用设计为与"具有固定状态机的**ECU**状态管理器"协同工作的软件组件，必须激活"**ECU**模式处理"选项。实现这种行为不需要所谓的兼容性**SWC**（**Compatibility SWC**）。

图3.1：EcuM Flex中的默认状态使旧SWC得以复用

图3.2描绘了该方案的行为方面。小方框表示固定**EcuM**的状态，绿色方框标出灵活**EcuM**的各个阶段。应用软件只会在**UP**阶段期间察觉到变化。

图3.2：固定EcuM的阶段到灵活EcuM的映射

其结果是，固定**EcuM**在**UP**阶段中的所有状态都必须使用**BswM**以及为此场景引入的软件组件来模拟。该软件组件必须将**BswM**报告的模式映射到固定状态机**EcuM**接口中定义的模式。

##### 3.3.2.1. BswM配置示例

系统设计者必须确保在设置**ECU**状态管理器的状态时，所有前置和后置条件都得到满足。由于**EcuM**应保持灵活，**BswM**切换状态的序列不会进行校验。如果状态切换的序列需要与**EcuMFixed**的序列兼容，系统设计者必须通过**BswM**规则来实现这种行为。

###### 3.3.2.1.1. 启动

在启动阶段，应当初始化与固定**EcuM**相同的**BSW**模块。这通过**BswM**规则实现，这些规则在**EcuM**初始化之后执行并初始化这些模块。已经由灵活**EcuM**初始化的模块由**BswM**跳过。

更改后的**BswM**规则见清单3.10。

```
rule InitBlockII initially false {
  if ( EcuMode == MDG_EcuMode.ECU_STARTUP_ONE ) {
    actionlist InitBlockIITrueActions
  }
}
actions InitBlockIITrueActions on condition {
  custom "Port_Init(null)"
  custom "Dio_Init(null)"
  custom "Adc_Init(null)"
  custom "Spi_Init(null)"
  custom "Eep_Init(null)"
  custom "Fls_Init(null)"
  custom "NvM_Init(null)"
  custom "EcuM_SetState(ECU_STARTUP_TWO)"
  custom "NvM_ReadAll()"
}

rule NvMReadAllFinished initially false {
  if ( NvMReadAllJobMode != NVM_REQ_PENDING
       && EcuMode == MDG_EcuMode.ECU_STARTUP_TWO)
  {
    actionlist NvMReadAllFinishedTrueActions
  }
}
actions NvMReadAllFinishedTrueActions on condition {
  custom "CanTrcv_Init(null)"
  custom "Can_Init(null)"
  custom "CanIf_Init(null)"
  custom "CanSM_Init(null)"
  custom "CanTp_Init(null)"
  custom "Lin_Init(null)"
  custom "LinIf_Init(null)"
  custom "LinSM_Init(null)"
  custom "LinTp_Init(null)"
  custom "FrTrcv_Init(null)"
  custom "Fr_Init(null)"
  custom "FrIf_Init(null)"
  custom "FrSM_Init(null)"
  custom "FrTp_Init(null)"
  custom "PduR_Init(null)"
  custom "CANNM_Init(null)"
  custom "FrNM_Init(null)"
  custom "NmIf_Init(null)"
  custom "IpduM_Init(null)"
  custom "COM_Init(null)"
  custom "DCM_Init(null)"
  custom "StartRte()"
  custom "ComM_Init(null)"
  custom "DEM_Init(null)"
  custom "FIM_Init(null)"
  custom "EcuM_SetState(ECU_RUN)"
}
```

清单3.10：与固定EcuM兼容的启动BswM配置

###### 3.3.2.1.2. 关机

关机机制由清单3.11中的**BswM**配置负责。所列出的规则协调post-run阶段、反初始化各模块，并使**ECU**进入关机或睡眠状态。这些规则执行的**Callout**与固定**EcuM**情况下执行的**EcuM_On\<Mode\>()**相同。

```
rule checkEcuMCompatibilityModeRequest initially false {
  if ( EcuMode == MDG_EcuMode.ECU_APP_RUN) {
    actionlist checkEcuMCompatibilityModeRequestActions
  }
}
actions checkEcuMCompatibilityModeRequestActions on condition {
  ComMAllowCom MyComM.CanNet1 false
  custom "EcuM_SetState(ECU_APP_POST_RUN)"
}

rule GoBackToRun initially false {
  if ( EcuMode == MDG_EcuMode.ECU_APP_POST_RUN) {
    actionlist GoBackToRunActions
  }
}
actions GoBackToRunActions on condition {
  custom "EcuM_SetState(ECU_APP_RUN)"
}

rule PrepShutdown initially false {
  if ( ComM_Mode_Channel1 == COMM_NO_COM_REQUEST_PENDING
       && EcuMode == MDG_EcuMode.ECU_APP_POST_RUN)
  {
    actionlist PrepShutdownActions
  }
}
actions PrepShutdownActions on condition {
  custom "Dem_Shutdown(null)"
  custom "EcuM_SetState(ECU_GO_SLEEP)"
  custom "EcuM_SetState(ECU_GO_OFF_ONE)"
}

rule GoSleep initially false {
  if ( ComM_Mode_Channel1 == COMM_NO_COM_REQUEST_PENDING
       && EcuMode == MDG_EcuMode.ECU_GO_SLEEP)
  {
    actionlist GoSleepActions
  }
}
actions GoSleepActions on condition {
  custom "EcuM_SetState(ECU_STARTUP_TWO)"
  custom "NvM_WriteAll()"
}

rule GoOff initially false {
  if ( ComM_Mode_Channel1 == COMM_NO_COM_REQUEST_PENDING
       && EcuMode == MDG_EcuMode.ECU_GO_OFF_ONE)
  {
    actionlist GoOffActions
  }
}
actions GoOffActions on condition {
  custom "Rte_stop(null)"
  custom "ComM_DeInit(null)"
  custom "EcuM_SetState(ECU_GO_OFF_TWO)"
  custom "NvM_WriteAll()"
}

rule GoSleepNvMWriteAllFinished initially false {
  if ( NvMWriteAllJobMode != NVM_REQ_PENDING
       && EcuMode == MDG_EcuMode.ECU_SLEEP)
  {
    actionlist GoSleepNvMWriteAllFinishedActions
  }
}
actions GoSleepNvMWriteAllFinishedActions on condition {
  custom "EcuM_GoHalt()"
}

rule GoOff2 initially false {
  if ( NvMWriteAllJobMode == NVM_BLK_OK
       && EcuMode == MDG_EcuMode.ECU_GO_OFF_TWO)
  {
    actionlist GoOff2Actions
  }
}
actions GoOff2Actions on condition {
  custom "EcuM_GoDown()"
}
```

清单3.11：与固定EcuM兼容的关机BswM配置

###### 3.3.2.1.3. 唤醒

从睡眠模式正确唤醒的功能必须在**BswM**中完整配置。但由于它不需要为向后兼容做任何调整，因此无需进行修改。

#### 3.3.3. 启动（Startup）

**ECUM**启动操作系统，随后其**OS**后序列启动调度管理器（**SchM_Start()**），初始化**BswM**（**BswM_Init()**），然后完成**SchM**的初始化（**SchM_Init()**和**SchM_StartTiming()**）。**BswM**在初始化之后必须注意：所有基础软件模块必需的初始化例程都被调用，并且**RTE**被启动（先**Rte_Start()**，再**Rte_Init()**，最后**Rte_StartTiming()**）。

在此场景中，期望**BswM**具有下面的模式声明组。这个**modeGroup**的用途类似于以前**AUTOSAR**版本中**ECU**状态管理器的状态，用于跟踪**ECU**的当前状态/模式。

规则**InitBlockII**指定了用于访问**NVRAM**的基础驱动程序的初始化，并启动**NvM_ReadAll**。由于**EcuMode**源的**processing**属性设置为**DEFERRED**，每次调用**BswM**主函数时都会评估该规则。第一次运行后，它将**EcuMode**设置为**ECU_STARTUP_TWO**，从而该动作列表永远不会再次被调用。

如果**NvMReadAll**作业完成，将触发**NvMReadAllFinished**规则，该规则启动剩余的初始化，并将**EcuMode**切换为**ECU_RUN**。

```
rule InitBlockII initially false {
  if ( EcuMode == MDG_EcuMode.ECU_STARTUP_ONE ) {
    actionlist InitBlockIIActions
  }
}
actions InitBlockIIActions on condition {
  custom "Spi_Init(null)"
  custom "Eep_Init(null)"
  custom "Fls_Init(null)"
  custom "NvM_Init(null)"
  SchMSwitch EcuMode : ECU_STARTUP_TWO
  custom "NvM_ReadAll()"
}

rule NvMReadAllFinished initially false {
  if ( NvMReadAllJobMode == NVM_REQ_OK
       && EcuMode == MDG_EcuMode.ECU_STARTUP_TWO)
  {
    actionlist NvMReadAllFinishedActions
  }
}
actions NvMReadAllFinishedActions on condition {
  custom "Can_Init(null)"
  custom "CanIf_Init(null)"
  custom "CanSM_Init(null)"
  custom "CanTp_Init(null)"
  custom "Lin_Init(null)"
  custom "LinIf_Init(null)"
  custom "LinSM_Init(null)"
  custom "LinTp_Init(null)"
  custom "Fr_Init(null)"
  custom "FrIf_Init(null)"
  custom "FrSM_Init(null)"
  custom "FrTp_Init(null)"
  custom "PduR_Init(null)"
  custom "CANNM_Init(null)"
  custom "FrNM_Init(null)"
  custom "NmIf_Init(null)"
  custom "IpduM_Init(null)"
  custom "COM_Init(null)"
  custom "DCM_Init(null)"
  custom "ComM_Init(null)"
  custom "DEM_Init(null)"
  custom "StartRte()"
  SchMSwitch EcuMode : ECU_RUN
}
```

清单3.12：用于启动的规则和动作列表

为了确保服务模块中的可运行实体在调用**RTE** **API**函数之前**RTE**已被正确初始化，可以通过模式禁用依赖（**mode disabling dependency**）将这些可运行实体禁用——即在**EcuM**模式**RUN**以外的所有模式下停用这些可运行实体。对于服务器可运行实体（**server runnable**）——它们无法被禁用——在**RTE**未初始化时，**RTE**会忽略传入的客户端-服务器请求。

**RTE**启动后，可运行实体将被启动。此时，保持**ECU**继续运行就是应用的责任了。为此，**BswM**可以例如提供一个如示例3.4所描绘的模式请求端口。在后续阅读中，假定应用软件向**BswM**请求模式**APP1_ACTIVE**。如果该模式被请求，**BswM**就不应关闭**ECU**。

```
rule checkApp1Request initially false {
  if ( App1ModeRequest == MDG_ApplicationModes.ModeA
       && EcuMode == MDG_EcuMode.ECU_RUN)
  {
    actionlist checkApp1RequestTrueActions
  }
}
actions checkApp1RequestTrueActions on condition {
  ComMAllowCom MyComM.CanNet1 true
  SchMSwitch EcuMode : ECU_RUN
}
```

清单3.13：应用运行，使能通信

#### 3.3.4. 运行（Run）

由于**BswM**是一个高度灵活的模块，如何判定**ECU**是否应当关闭在很大程度上取决于集成者。可以设想许多不同的方案。本文档提出一种与**AUTOSAR R3.1**中**ECUM**概念相当类似的方法。其总体概念是：只要至少有一个应用软件组件请求运行状态，**ECU**就保持运行。

应用在某个模式下是否可以被关闭的信息，必须由软件组件的开发者提供。示例3.14展示了一个针对只有单个软件组件的**ECU**的简化规则。如果该软件组件将其模式切换为**INACTIVE**，**BswM**就发起关机序列。

```
rule checkApp1Request initially false {
  if ( App1ModeRequest == MDG_ApplicationModes.APP_INACTIVE
       && EcuMode == MDG_EcuMode.ECU_RUN)
  {
    actionlist checkApp1RequestActions
  }
}
actions checkApp1RequestActions on condition {
  ComMAllowCom ArMmExample.EcuC.MyComM.ComMChannel1 false
  SchMSwitch EcuMode : ECU_APP_POST_RUN
}
```

清单3.14：如果没有应用再想运行，则发起关机

#### 3.3.5. 关机（Shutdown）

在**ECU_APP_POST_RUN**状态中，**BswM**等待所有通道报告不再有待处理的请求。清单3.14中的规则会在**ComM**通道的模式每次发生变化时被触发。如果存在多个**ComM**通道，必须将它们组合成单一表达式。

```
rule InitiateShutdown initially false {
  if ( ComM_Mode_Channel1 == COMM_NO_COM_REQUEST_PENDING
       && EcuMode == MDG_EcuMode.ECU_APP_POST_RUN)
  {
    actionlist InitiateShutdownActions
  }
}
actions InitiateShutdownActions on condition {
  custom "Dem_Shutdown(null)"
  custom "Rte_Stop()"
  custom "ComM_DeInit()"
  SchMSwitch EcuMode : ECU_GO_OFF_ONE
  custom "NvM_WriteAll()"
}

rule NvMWriteAllFinished initially false {
  if ( NvMWriteAllJobMode == NVM_BLK_OK
       && EcuMode == MDG_EcuMode.ECU_GO_OFF_ONE)
  {
    actionlist NvMWriteAllFinishedTrueActions
  }
}
actions NvMWriteAllFinishedTrueActions on condition {
  custom "EcuM_SelectShutdownCause(ECUM_CAUSE_ECU_STATE)"
  custom "EcuM_GoDown(MODULE_ID)"
}
```

清单3.15：关机序列

注意，在**ECUM**的配置中，必须将**BswM**的模块**ID**作为有效用户添加到**EcuMFlexUserConfig**中。

#### 3.3.6. 睡眠（Sleep）

进入睡眠状态与关机序列3.14类似，只是调用的是**EcuM_GoHalt**或**EcuM_GoPoll**，而不是**EcuM_GoDown**。

#### 3.3.7. 唤醒（Wakeup）

示例3.16展示了一条规则：只有在由**EcuM_WakeupSource**标识的特定唤醒事件已发生时才启动**ECU**；否则**ECU**将立即关闭。

```
rule InitBlockII initially false {
  if ( EcuMode == MDG_EcuMode.ECU_STARTUP_ONE
       && EcuM_WakeupSource == ECUM_WKSTATUS_VALIDATED)
  {
    actionlist InitBlockIITrueActions
  }
  else {
    actionlist InitBlockIIFalseActions
  }
}
actions InitBlockIITrueActions on condition {
  custom "Spi_Init(null)"
  custom "Eep_Init(null)"
  custom "Fls_Init(null)"
  custom "NvM_Init(null)"
  SchMSwitch EcuMode : ECU_STARTUP_TWO
  custom "NvM_ReadAll()"
}

actions InitBlockIIFalseActions on condition {
  custom "EcuM_GoDown(MODULE_ID)"
}
```

清单3.16：带唤醒检查的启动序列

#### 3.3.8. 分区复位

在某个特定分区发生错误并需要重启的情况下，分区到该分区的基础软件模块必须被重新初始化。为了确定哪个分区已被重启，可以利用模式请求源**BswMPartitionRestarted**。

```
rule InitBlockII initially false {
  if ( EcuMode == MDG_EcuMode.ECU_STARTUP_ONE ) {
    actionlist InitBlockIIActions
  }
}
actions InitBlockIIActions on condition {
  custom "Spi_Init(null)"
  custom "Eep_Init(null)"
  custom "Fls_Init(null)"
  custom "NvM_Init(null)"
  custom "EcuM_SetState(ECU_STARTUP_TWO)"
  custom "NvM_ReadAll()"
}

rule NvMReadAllFinished initially false {
  if ( NvMReadAllJobMode == NVM_REQ_OK
       && EcuMode == MDG_EcuMode.ECU_STARTUP_TWO
       && BSWM_BSW_MODE_REQUEST_API_CALLED(BswMPartitionRestarted) )
  {
    actionlist NvMReadAllFinished4PartitionActions
  }
}
actions NvMReadAllFinished4PartitionActions on condition {
  // 只初始化分区到相应内核的模块，例如：
  custom "Can_Init(null)"
  custom "CanIf_Init(null)"
  custom "CanSM_Init(null)"
  custom "CanTp_Init(null)"
  ...
}
```

清单3.17：分区复位序列

### 3.4. 通信管理

除了**ECU**状态管理的部分内容之外，**BswM**还负责通信管理的部分内容。本节描述**BswM**中与**AUTOSAR**通信栈相关的功能，涵盖但不限于以下用例：

* 一般情况下**I-PDU**组的启动和停止
* 部分网络（**Partial Networking**）
* 影响**ECU**通信的诊断用例，例如：当应用发出请求时，可能需要通过**FrSm_SetEcuPassive()**将**FlexRay**状态管理器设置为被动模式
* 面向应用**SWC**的服务发现控制

为了实现所请求的功能，**BswM**具有指向以下模块的模式请求源：

* 通信管理器（**Communication Manager**）
* 各总线状态管理器
* **AUTOSAR COM**
* 服务发现（**Service Discovery**）

#### 3.4.1. 启动和关闭

除了通信栈的初始化之外，还可以将**BswM**配置为：根据**ECU**的需要初始化其他模块或执行自定义动作。由于**BswM**的灵活性，也可以实现在唤醒事件之后只启动通信栈的一部分。

与启动类似，也可以配置在关机时执行的额外动作。

#### 3.4.2. 部分网络集群

部分网络集群（**Partial Network Cluster，PNC**）是一个（逻辑上的）**ECU**组，这些**ECU**必须同时处于活动状态才能实现某些分布式功能。一个**PNC**可以分配给一个或多个用户（在**ComM**中配置），特定的软件组件可以通过请求映射到该**PNC**的用户的通信模式，来请求或释放该**PNC**的通信。**ComM**为每个部分网络集群实现一个状态机，每个**PNC**都有自己的状态。为了简单映射，**PNC**状态的定义与**ComM**的状态相关。

系统通道上各节点所有**PNC**的状态通过所谓的**PNC**位向量（**PNC bit vector**）在网络管理报文（**NM**报文）中交换。

每个**PNC**在通过**CAN**、**FlexRay**和以太网的**NM**报文传输的位向量（**PNC**位向量）中使用一个专用的位位置。如果节点上的本地**ComM**用户请求了某个**PNC**，该节点就将**PNC**位向量中相应的**PNC**位设置为1；如果该**PNC**不再被请求，则将相应的**PNC**位设置为0。（请注意：如果使用了可选特性"同步**PNC**关闭"并且需要发送**PN**关闭报文，则被释放的**PNC**的位被设置为1，其余**PNC**位被设置为0）。**\<Bus\>Nm**从接收到的**NM-PDU**中提取**PNC**位向量，并将其转发给**NM**接口。**Nm**接口模块收集并聚合**PNC**请求。

每个**PNC**在**NM**报文中的**PNC**位向量里，在每条系统通道上都使用相同的位位置。**ComM**使用三种类型的**PNC**位向量与**NM**接口和**\<Bus\>Nm**交换**PNC**状态信息，分别是外部和内部请求数组（**E**xternal and **I**nternal **R**equest **A**rray，**EIRA**）、外部请求数组（**E**xternal **R**equest **A**rray，**ERA**）和内部请求数组（**I**nternal **R**equest **A**rray，**IRA**）。

**CAN**、**FlexRay**和以太网总线类型支持部分网络。**CAN**、**FlexRay**和以太网节点上**PNC**的**I-PDU**组的激活和停用是必需的，以便结合**PNC**的当前状态控制通信能力，并避免系统中的虚假超时。**COM**中**I-PDU**组的启动和停止由**BswM**处理。如果相应的**PNC**被内部或外部请求，则应启动其**I-PDU**组；一旦某个**PNC**既没有被内部请求也没有被外部请求，就应停止相应的**I-PDU**组。内部**PNC**请求表示**ECU**本地的通信需求，也称为"主动**PNC**请求"（**active PNC request**）；外部**PNC**请求表示网络中远程**ECU**的通信需求，也称为"被动**PNC**请求"（**passive PNC request**）。控制**I-PDU**组的逻辑作为**ComM**与**BswM**之间的交互来处理。**ComM**向**BswM**指示特定**PNC**状态机的当前状态，**BswM**通过模式仲裁和模式控制来控制相应的**I-PDU**组。请注意，无法停用单个**FlexRay** **ECU**。

**PNC**网关（**PNC Gateway**）特性用于将（逻辑上的）部分网络集群跨越总线/通信通道边界，把**PNC**请求从一个总线/网络"网关"到其他总线/网络。**PNC**网关从其所有活动的通道（称为活动，是因为需要时它会主动保持它们唤醒）收集**PNC**请求并进行聚合。**PNC**网关将聚合后的**PNC**状态在网络中发送到其所有活动通道，这使得所有节点对全局**PNC**请求状态具有与网关相同的视图。如果**PNC**网关不是网络层次结构中最顶层的**PNC**网关，它还会将所有下级节点的聚合**PNC**请求状态以及自身的内部请求状态，发送给通过所谓"被动"（**passive**）连接器类型连接的上级**PNC**协调器。上级**PNC**协调器会聚合下级协调器的**PNC**请求状态，因此顶层协调器会知道网络中所有活动的**PNC**请求，并将该信息发送给下级节点。

##### 3.4.2.1. 内部和外部部分网络集群的聚合

每个作为部分网络集群成员的**ECU**都会使用此特性。主动**PNC**请求由**ComM**通过**Nm**转发给**\<Bus\>Nm**；被动**PNC**请求由**\<Bus\>Nm**接收并转发给**Nm**。**Nm**根据所谓的**PN**过滤掩码（**PN filter mask**）处理接收到的**PNC**请求。**PN**过滤掩码定义了哪些接收到的**PNC**请求是相关的。**Nm**收集并维护内部和外部**PNC**请求。内部和外部被请求**PNC**的聚合称为"外部内部请求数组（**EIRA**）"。**EIRA**的变化由**Nm**转发给**ComM**。**ComM**需要该信息来处理相应**PNC**状态机中的变化。

在（几乎）同一时刻向每个**ECU**上的**ComM**提供请求变化的信息（**PNC**请求从请求变为释放，或反之），会使所有直接相连的**ECU**同步地切换**I-PDU**组。因此，**Nm**为**EIRA**中的每个**PNC**请求维护定时器（所谓的**PNC**复位定时器）。每当在接收到的**PNC**位向量中请求了相应的**PNC**时，以及每当发送相应的**PNC**请求时，该**PNC**复位定时器都会重启。

##### 3.4.2.2. 外部部分网络集群的聚合

启用了**PNC**网关功能的**ECU**使用此特性按通道收集外部**PNC**请求。外部**PNC**请求必须在所有受影响的通道之间协调。**PNC**协调的逻辑由**ComM**提供，其中为每个通道配置了它是主动协调还是被动协调。在主动协调的通道上，外部**PNC**请求会被镜像回接收到该请求的通道，并且还会被转发到分配了该**PNC**的所有其他协调通道（无论被动还是主动协调）。在被动协调的通道上，外部**PNC**请求会被转发到分配了该**PNC**的其他主动协调通道，而不会镜像回接收到该外部**PNC**请求的通道。这避免了当两个**ECU**都启用了**PNC**网关功能并连接到同一通道时，部分网络集群请求的无休止镜像。**Nm**模块向**ComM**提供**PNC**是否被外部请求或释放的信息，并为每个相关的**PNC**按通道管理**PNC**定时器处理。外部被请求**PNC**的聚合状态称为"外部请求数组（**ERA**）"。

##### 3.4.2.3. 同步PNC关闭

为了避免应用层的超时失败，**PNC**应以同步的方式关闭（**PNC**中的所有节点在同一时间点关闭）。同步**PNC**关闭是**ComM**、**Nm**和**\<Bus\>Nm**协作的功能，用于确保在整个**PN**拓扑中几乎在同一时间点同步关闭**PNC**。如果启用了**PNC**网关，同步**PNC**关闭由处于顶层**PNC**协调器或中间**PNC**协调器角色的**ECU**处理。当处于顶层**PNC**协调器角色的**ECU**的**ComM**检测到某个**PNC**被释放（该**PNC**不再被内部或外部请求）时，该**ComM**会请求一次同步**PNC**关闭。**Nm**模块存储所有请求，并在**Nm_MainFunction**的上下文中处理它们。**Nm**模块就已激活的**PNC**关闭过程向受影响的**\<Bus\>Nm**发出指示。**\<Bus\>Nm**调用**Nm**模块，以按给定的**NM**通道获取用于同步**PNC**关闭的聚合请求（作为**PNC**位向量）。**\<Bus\>Nm**使用所提供的**PNC**位向量组装一个作为**PN**关闭报文的**NM-PDU**，并在相应的**NM**通道上发送该报文。如果处于中间**PNC**协调器角色的**ECU**接收到一个**PN**关闭报文，**\<Bus\>Nm**会从接收到的**PN**关闭报文中提取**PNC**位向量，并通过调用回调函数**Nm_ForwardSynchronizedPncShutdown**转发该信息。该回调函数会立即通过调用**ComM_Nm_ForwardSynchronizedPncShutdown**将该指示转发给**ComM**。**ComM**将立即请求所有主动**PNC**协调（由**PNC**网关协调）的**ComM**通道的同步**PNC**关闭。同步**PNC**关闭的请求按**NM**通道转发给**Nm**模块，并按照上一节所述的相同方式处理。如果**PNC**叶节点接收到**PN**关闭报文，它会将该报文作为普通**NM**报文处理（更新本地**PN**信息并复位**PN**复位定时器）。

#### 3.4.3. 主函数的调度

由于通信通道或**PNC**的状态变化通常在主处理函数的上下文中处理，因此必须恰当考虑通信和网络管理所涉及模块（**ComM**、**Nm**、**\<Bus\>Nm**）的主处理函数的调度和执行顺序。**ComM**通常结合系统中的事件来协调各项活动，并通过调用相关**API**触发下层所需的动作。系统中需要**ComM**触发特定动作的事件可以是用户的内部请求（对通道或**PNC**的内部请求）、对通道或**PNC**的被动/外部请求，或者在总线上接收到的同步**PNC**关闭报文。外部事件可能由唤醒事件、周期**NM**报文的接收或同步关闭报文引起。**ComM**接收并处理所有内部和外部请求，并触发所需的动作，这些动作将导致通信和网络管理模块状态机的状态变化，进而导致周期**NM**报文或同步关闭报文在总线上的传输。在集成这些模块时，必须考虑到：特定请求的处理在基础软件中是异步完成的（例如：传输请求、来自应用的某些请求），并且特定动作可能在所涉及模块的主处理周期上下文中被解耦处理（例如：**\<Bus\>Nm**中的传输、定时器的处理、状态变化以及向上层的通知）。

#### 3.4.4. I-PDU组切换

对于**I-PDU**组切换，预期**COM**中为每个通道或部分网络存在专用于发出和接收**I-PDU**的**I-PDU**组。**AUTOSAR COM**确保只要包含某个**I-PDU**的至少一个**I-PDU**组处于活动（启动）状态，该**I-PDU**就是活动的。

请注意，**I-PDU**组的处理高度依赖具体项目，某些用例必须在项目范围内加以考虑（例如：使用**\<Bus\>Sm**状态而不是**ComM**模式，或者同时使用**\<Bus\>Sm**状态和**ComM**模式）。

为了说明如何管理一个**ECU**的**I-PDU**，创建以下简化场景来描述其处理方式。示例**ECU**具有两个**CAN**通道和三个部分网络。通道的模式请求端口命名为**ComM_Mode_Channel1**和**ComM_Mode_Channel2**，部分网络的请求源命名为**PNC1**、**PNC2**和**PNC3**。**PNC1**的**I-PDU**仅通过**Channel1**通信；**PNC2**的**I-PDU**通过**Channel1**和**Channel2**通信；**PNC3**的**I-PDU**仅通过**Channel2**通信。本示例中使用的**I-PDU**组在下表中定义。

表3.2：PNC处理的I-PDU组

| I-PDU组 | PNC | 方向 | 通道 |
| --- | --- | --- | --- |
| PNC1PDUS_TX | PNC1 | TX | Channel1 |
| PNC1PDUS_RX | PNC1 | RX | Channel1 |
| PNC2PDUS_CH1_TX | PNC2 | TX | Channel1 |
| PNC2PDUS_CH1_RX | PNC2 | RX | Channel1 |
| PNC2PDUS_CH2_TX | PNC2 | TX | Channel2 |
| PNC2PDUS_CH2_RX | PNC2 | RX | Channel2 |
| PNC3PDUS_TX | PNC3 | TX | Channel2 |
| PNC3PDUS_RX | PNC3 | RX | Channel2 |

表3.3：由通道处理控制的I-PDU组

| I-PDU组 | PNC | 方向 | 通道 |
| --- | --- | --- | --- |
| CAN1IPDUS_TX | n/a | TX | Channel1 |
| CAN1IPDUS_RX | n/a | RX | Channel1 |
| CAN2IPDUS_TX | n/a | TX | Channel2 |
| CAN2IPDUS_RX | n/a | RX | Channel2 |

##### 3.4.4.1. 通道相关的I-PDU组处理

如果一个通信通道被请求，则应启动相应的**I-PDU**组。

```
rule channel1requested initially false {
  if ( ComM_Mode_Channel1 == COMM_FULL_COMMUNICATION ) {
    actionlist channel1requestedActions
  }
}
actions channel1requestedActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.CAN1IPDUS_TX, ArMmExample.EcuC.MyCom.CAN1IPDUS_RX
  }
}

rule channel2requested initially false {
  if ( ComM_Mode_Channel2 == COMM_FULL_COMMUNICATION ) {
    actionlist channel2requestedActions
  }
}
actions channel2requestedActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.CAN2IPDUS_TX, ArMmExample.EcuC.MyCom.CAN2IPDUS_RX
  }
}
```

清单3.18：ComM报告FULL_COMMUNICATION

如果一个通信通道被释放，且通道状态机进入**COMM_SILENT_COMMUNICATION**，则应停止相应的**TX** **I-PDU**组。

```
rule channel1silentcom initially false {
  if ( ComM_Mode_Channel1 == COMM_SILENT_COMMUNICATION ) {
    actionlist channel1silentcomActions
  }
}
actions channel1silentcomActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.CAN1IPDUS_TX
  }
}

rule channel2silentcom initially false {
  if ( ComM_Mode_Channel2 == COMM_SILENT_COMMUNICATION ) {
    actionlist channel2silentcomActions
  }
}
actions channel2silentcomActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.CAN2IPDUS_TX
  }
}
```

清单3.19：ComM报告SILENT_COMMUNICATION

如果一个通信通道被释放，且通道状态机进入**COMM_NO_COMMUNICATION**，则应停止相应的**RX** **I-PDU**组。

```
rule channel1nocom initially false {
  if ( ComM_Mode_Channel1 == COMM_NO_COMMUNICATION ) {
    actionlist channel1nocomActions
  }
}
actions channel1nocomActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.CAN1IPDUS_RX
  }
}

rule channel2nocom initially false {
  if ( ComM_Mode_Channel2 == COMM_NO_COMMUNICATION ) {
    actionlist channel2nocomActions
  }
}
actions channel2nocomActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.CAN2IPDUS_RX
  }
}
```

清单3.20：ComM报告NO_COMMUNICATION

##### 3.4.4.2. PNC相关的I-PDU组处理

如果一个部分网络被请求（无论是主动还是被动），则应启动相应的**I-PDU**组。

```
rule pnc1requested initially false {
  if ( PNC1 == PNC_REQUESTED || PNC1 == PNC_READY_SLEEP ) {
    actionlist pnc1requestedActions
  }
}
actions pnc1requestedActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC1IPDUS_TX, ArMmExample.EcuC.MyCom.PNC1IPDUS_RX
  }
}

rule pnc2requested initially false {
  if ( PNC2 == PNC_REQUESTED || PNC2 == PNC_READY_SLEEP ) {
    actionlist pnc2requestedActions
  }
}
actions pnc2requestedActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_RX,
           ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_RX
  }
}

rule pnc3requested initially false {
  if ( PNC3 == PNC_REQUESTED || PNC3 == PNC_READY_SLEEP ) {
    actionlist pnc3requestedActions
  }
}
actions pnc3requestedActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC3IPDUS_TX, ArMmExample.EcuC.MyCom.PNC3IPDUS_RX
  }
}
```

清单3.21：ComM报告PNC_REQUESTED或PNC_READY_SLEEP

如果一个部分网络被释放，且**PNC**状态机进入**PNC_PREPARE_SLEEP**，则应停用相应**PNC**的截止期限监视（**deadline monitoring**）。在达到**PNC_NO_COMMUNICATION**状态之前，**I-PDU**仍会被传输。

```
rule pnc1preparesleep initially false {
  if (PNC1 == PNC_PREPARE_SLEEP) {
    actionlist pnc1preparesleepActions
  }
}
actions pnc1preparesleepActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC1IPDUS_TX, ArMmExample.EcuC.MyCom.PNC1IPDUS_RX
  }
  DeadlineMonitoring {
    disable ArMmExample.EcuC.MyCom.PNC1IPDUS_RX
  }
}

rule pnc2preparesleep initially false {
  if (PNC2 == PNC_PREPARE_SLEEP ) {
    actionlist pnc2preparesleepActions
  }
}
actions pnc2preparesleepActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_RX,
           ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_RX
  }
  DeadlineMonitoring {
    disable ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_RX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_RX
  }
}

rule pnc3preparesleep initially false {
  if (PNC3 == PNC_PREPARE_SLEEP ) {
    actionlist pnc3preparesleepActions
  }
}
actions pnc3preparesleepActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.PNC3IPDUS_TX, ArMmExample.EcuC.MyCom.PNC3IPDUS_RX
  }
  DeadlineMonitoring {
    disable ArMmExample.EcuC.MyCom.PNC3IPDUS_RX
  }
}
```

清单3.22：ComM报告PNC_PREPARE_SLEEP

如果一个部分网络被释放，且**PNC**状态机进入**PNC_NO_COMMUNICATION**，则应停止相应的**I-PDU**组。

```
rule pnc1nocom initially false {
  if ( PNC1 == PNC_NO_COMMUNICATION ) {
    actionlist pnc1nocomTrueActions
  }
}
actions pnc1nocomTrueActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.PNC1IPDUS_TX, ArMmExample.EcuC.MyCom.PNC1IPDUS_RX
  }
}

rule pnc2nocom initially false {
  if ( PNC2 == PNC_NO_COMMUNICATION ) {
    actionlist pnc2nocomTrueActions
  }
}
actions pnc2nocomTrueActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH1_RX,
            ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_TX, ArMmExample.EcuC.MyCom.PNC2IPDUS_CH2_RX
  }
}

rule pnc3nocom initially false {
  if ( PNC3 == PNC_NO_COMMUNICATION ) {
    actionlist pnc3nocomTrueActions
  }
}
actions pnc3nocomTrueActions on condition {
  PduGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyCom.PNC3IPDUS_TX, ArMmExample.EcuC.MyCom.PNC3IPDUS_RX
  }
}
```

清单3.23：ComM报告PNC_NO_COMMUNICATION

#### 3.4.5. J1939网络管理

与当前的**AUTOSAR**网络管理不同，**J1939**网络管理的任务不是处理**ECU**的睡眠和唤醒，而是为**ECU**所表示的每个节点分配唯一的地址。

这是通过在启动时发送**AddressClaimed**（**AC**，0x0EE00）参数组来实现的，该报文宣告所期望的地址。如果另一个节点声明了相同的地址并具有更高的优先级，本节点在发送**CannotClaimAddress**参数组（**SA**为空地址的**AC**）后必须进入静默，或者尝试使用其他地址。

为了支持这一用例，**BswM**被扩展为可以通过**API**函数**BswM_J1939Nm_StateChangeNotification()**接受来自**J1939Nm**的状态变化指示（另请参阅3.2.2.2.15节）。

根据网络管理所指示的状态，**BswM**需要切换**COM**的**ComIPduGroup**、**PduR**的**PduRRoutingPathGroup**，以及**J1939Rm**的通用请求处理。

前两个动作通过**BswMPduGroupSwitch**和**BswMPduRouterControl**动作实现。**J1939**请求管理器应使用**BswMJ1939Rm**动作进行切换。

预期**COM**为每个网络提供包含所有本地接收和发送**I-PDU**的**IPDU**组。**PduR**应以相同的方式配置，为每个通道提供用于所有本地接收和发送**I-PDU**的路由路径组，不包括转发给**J1939Rm**的**Request**报文的接收**I-PDU**。

然后，**BswM**必须配置为根据所报告的**NM**状态切换上述**IPDU**组和**PduRRoutingPathGroup**的开启与关闭，以及**J1939**请求管理器的通用请求处理。下面的规则展示了**BswM**根据**NM**状态所执行的动作。

```
rule J1939_nm_normal_operation initially false {
  if ( J1939NmState == NM_STATE_NORMAL_OPERATION ) {
    actionlist J1939NormalOperationActions
  }
}
actions J1939NormalOperationActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.J1939IPDUS
  }
  PduRoute enable J1939_RoutingPath
  custom "J1939Rm_SetState(J1939RM_STATE_ONLINE)"
  custom "Xcp_SetTransmissionMode(CHANNEL1,XCP_TX_ON)"
}

rule J1939_nm_offline initially false {
  if ( J1939NmState != NM_STATE_NORMAL_OPERATION ) {
    actionlist J1939OfflineActions
  }
}
actions J1939OfflineActions on condition {
  PduGroupSwitch {
    disable ArMmExample.EcuC.MyCom.J1939IPDUS
  }
  PduRoute disable J1939_RoutingPath
  custom "J1939Rm_SetState(J1939RM_STATE_OFFLINE)"
  custom "Xcp_SetTransmissionMode(CHANNEL1,XCP_TX_OFF)"
}
```

清单3.24：实现J1939网络管理的规则

**注意：** 建议使用**BswMJ1939Rm**动作而不是自定义调用。本清单中使用自定义调用只是因为当前**ARText**版本尚不支持该动作。

#### 3.4.6. J1939诊断模式管理

除了地址分配之外，**BswM**还必须监督**J1939**环境中广播报文的发送。每个**IPDU**组代表一个网络的广播报文（具有**PDU2**格式**PGN**或**PDU1**格式**PGN**以及广播目标地址的**J1939 PG**）。

为此，同样预期**COM**为每个通道包含一个**IPDU**组，其中包含该**ECU**的广播报文。

```
rule J1939_broadcast_management initially false {
  if ( BswMJ1939DcmBroadcastStatus == NETWORK_ENABLED) {
    actionlist J1939ActivateBroadcastActions
  }
  else {
    actionlist J1939DeactivateBroadcastActions
  }
}
actions J1939ActivateBroadcastActions on condition {
  PduGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyCom.J1939BroadcastIPDUS
  }
}
actions J1939DeactivateBroadcastActions on condition {
  PduGroupSwitch {
    disable ArMmExample.EcuC.MyCom.J1939BroadcastIPDUS
  }
}
```

清单3.25：实现J1939广播管理的规则

#### 3.4.7. LIN调度表切换

**BswM**能够根据来自应用**SWC**的请求切换**LIN**通道的调度表。

**SWC**以应用模式的形式向**BswM**请求一个**LIN**调度表。切换成功后，**BswM**切换到所请求的模式。

下面展示了这种行为的一个示例。首先，需要一个供应用**SWC**用于请求特定调度表的模式声明组，**LIN**通道将切换到该调度表。

```
modeGroup MDG_LinScheduleTables { Schedule1, Schedule2 }
```

**BswM**与**SWC**之间的**SenderReceiverInterface**需要一个包含相同取值的枚举。

```
enum ENUM_LinScheduleTables { Schedule1, Schedule2 }
```

在**LIN**调度表设置完成后，需要一个模式切换接口来切换应用模式。

```
interface modeSwitch LinScheduleMode { mode MDG_LinScheduleTables LinScheduleMode }
```

还需要一个使用前面定义的枚举的**SenderReceiverInterface**。应用**SWC**可以使用它来请求一个应当引发**LIN**调度表切换的模式。

```
interface senderReceiver LinChannel1ScheduleTableRequestPort {
  data ENUM_LinScheduleTables LinScheduleMode
}
```

当应用**SWC**请求另一个应用模式时，下面的**BswM**规则会切换**LIN**通道的调度表。

```
rule LinChannel1Schedule1Request initially false {
  if (LinChannel1ScheduleTableRequestPort == Schedule1) {
    LinScheduleSwitch(LinSchedule1)
  }
}
```

下面的**BswM**规则将应用模式切换到应用此前请求的模式。当**LinSM**通知**BswM**发生了一次**LIN**调度表切换时，该规则被触发。

```
rule LinChannel1Schedule1Switched initially false {
  if (LinSM_CurrentState == LinSchedule1) {
    RteSwitch(LinScheduleMode, Schedule1)
  }
}
```

最后是**LIN**调度表**LinSchedule2**对应的规则：

```
rule LinChannel1Schedule2Request initially false {
  if (LinChannel1ScheduleTableRequestPort == Schedule2) {
    LinScheduleSwitch(LinSchedule2)
  }
}

rule LinChannel2Schedule1Switched initially false {
  if (LinSM_CurrentState == Schedule2) {
    RteSwitch(LinScheduleMode, LinSchedule2)
  }
}
```

#### 3.4.8. 以太网交换机端口组切换

对于以太网交换机端口切换，预期**EthSwtPort**被组合为**EthIfSwitchPortGroup**。**EthIfSwitchPortGroup**可以从系统描述提取（**SystemDescriptionExtract**）中派生。根据建模，每个**EthSwitchPortGroup**被映射到至少一个**PNC**。**EthIfSwitchPortGroup**的切换通过特定的**BswM**规则实现。因此，**ComM**通过**BswM_ComM_CurrentPNCMode**报告**PNC**的当前模式。**PNC**与**EthSwitchPortGroup**之间的映射为**BswM**所知。于是，**BswM**通过以相应的**EthIfSwitchPortGroup**调用**EthIf_SwitchPortGroupRequestMode**，将所报告的**PNC**当前模式转发给**EthIf**。根据给定的端口模式（**ETH_MODE_DOWN**或**ETH_MODE_ACTIVE**），**EthIf**管理对**EthIfSwitchPortGroup**的请求，并决定关闭或打开**EthSwtPort**。

为了说明如何管理**EthIfSwitchPortGroup**的切换，创建以下场景。示例**ECU**配置了两个部分网络（命名为**PNC1**和**PNC2**）和两个对应的**EthIfSwtPortGroup**（命名为**EthIfSwtPortGroup1**和**EthIfSwtPortGroup2**）：

* 如果**PNC1**被请求，则以**EthSwtPortGroup1**和**ETH_MODE_ACTIVE**调用**EthIf_SwitchPortGroupRequestMode**
* 如果**PNC1**被释放，则以**EthSwtPortGroup1**和**ETH_MODE_DOWN**调用**EthIf_SwitchPortGroupRequestMode**
* 如果**PNC2**被请求，则以**EthSwtPortGroup2**和**ETH_MODE_ACTIVE**调用**EthIf_SwitchPortGroupRequestMode**
* 如果**PNC2**被释放，则以**EthSwtPortGroup2**和**ETH_MODE_DOWN**调用**EthIf_SwitchPortGroupRequestMode**

如果一个部分网络被请求，则打开相应的**EthSwtPortGroup**。

```
rule pnc1requested initially false {
  if ( PNC1 == COMM_PNC_REQUESTED || PNC1 == COMM_PNC_READY_SLEEP
       || PNC1 == COMM_PNC_PREPARE_SLEEP ){
    actionlist pnc1requestedActions
  }
}
actions pnc1requestedActions on condition {
  EthIfSwitchPortGroupRequestMode {
    init false
    enable EthIfSwtPortGroup1
  }
}

rule pnc2requested initially false {
  if ( PNC2 == COMM_PNC_REQUESTED || PNC2 == COMM_PNC_READY_SLEEP
       || PNC2 == COMM_PNC_PREPARE_SLEEP ){
    actionlist pnc2requestedActions
  }
}
actions pnc2requestedActions on condition {
  EthIfSwitchPortGroupRequestMode {
    init false
    enable EthIfSwtPortGroup2
  }
}
```

清单3.26：ComM报告切换到COMM_PNC_FULL_COMMUNICATION

如果一个部分网络被释放，则关闭相应的**EthSwtPortGroup**。

```
rule pnc1released initially false {
  if ( PNC1 == COMM_PNC_NO_COMMUNICATION) {
    actionlist pnc1releasedActions
  }
}
actions pnc1releasedActions on condition {
  EthIfSwitchPortGroupRequestMode {
    init true
    disable EthIfSwtPortGroup1
  }
}

rule pnc2released initially false {
  if ( PNC2 == COMM_PNC_NO_COMMUNICATION) {
    actionlist pnc2releasedActions
  }
}
actions pnc2releasedActions on condition {
  EthIfSwitchPortGroupRequestMode {
    init true
    disable EthIfSwtPortGroup2
  }
}
```

清单3.27：ComM报告COMM_PNC_NO_COMMUNICATION

##### 3.4.8.1. 带唤醒请求的以太网交换机端口组切换

**AUTOSAR**支持对兼容**OA TC10**的以太网硬件通过数据线（**dataline**）进行睡眠/唤醒的处理。结合**PNC**处理和以太网交换机端口组切换，当存在带唤醒请求的活动**PNC**请求时，**ComM**会以**COMM_PNC_REQUESTED_WITH_WAKEUP_REQUEST**向**BswM**发出指示。**BswM**通过以相应的**EthIfSwtPortGroup**和相应的**Eth_ModeType ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**调用**EthIf_SwitchPortGroupRequestMode**，将该活动的**PNC**转发给**EthIf**。基于3.4.8节以太网交换机端口组切换中的示例配置，下面的示例展示了带数据线唤醒请求的以太网交换机端口切换：

* 如果**PNC1**被请求，则以**EthSwtPortGroup1**和**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**调用**EthIf_SwitchPortGroupRequestMode**
* 如果**PNC2**被请求，则以**EthSwtPortGroup2**和**ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**调用**EthIf_SwitchPortGroupRequestMode**

如果一个部分网络被请求，且以太网硬件支持并使用了数据线唤醒，则打开相应的**EthSwtPortGroup**，并通过**Eth_ModeType ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST**报告数据线唤醒请求。

```
rule pnc1requested_with_wakeup_request initially false {
  if ( PNC1 == COMM_PNC_REQUESTED_WITH_WAKEUP_REQUEST){
    actionlist pnc1requested_with_wakeup_request_Actions
  }
}
actions pnc1requested_with_wakeup_request_Actions on condition {
  EthIfSwitchPortGroupRequestMode {
    init false
    enable EthIfSwtPortGroup1
  }
}

rule pnc2requested_with_wakeup_request initially false {
  if ( PNC2 == COMM_PNC_REQUESTED_WITH_WAKEUP_REQUEST){
    actionlist pnc2requested_with_wakeup_request_Actions
  }
}
actions pnc2requested_with_wakeup_request_Actions on condition {
  EthIfSwitchPortGroupRequestMode {
    init false
    enable EthIfSwtPortGroup1
  }
}
```

清单3.28：ComM报告切换到COMM_PNC_FULL_COMMUNICATION并带有数据线唤醒请求

除了管理**EthIfSwitchPortGroup**切换的请求之外，**EthIf**还监督每个**EthSwitchPortGroup**的累积链路状态。如果**EthIf**检测到**EthIfSwitchPortGroup**累积链路状态的意外变化，它会通过调用受影响**EthIfSwitchPortGroup**的**BswM_EthIf_PortGroupLinkStateChg**来指示这一链路状态变化。该指示可以通过模式切换转发给应用，以便对这类通信错误场景做出反应（例如：以太网交换机端口硬件错误、数据线连接松动等）。

#### 3.4.9. PduR路由路径组切换

**PduR**路由路径组切换用于切换未分配给**COM** **I-PDU**组的**I-PDU**的路由路径（参见3.4.4节"I-PDU组切换"），例如：通过**LdCom**传输的**I-PDU**。**LdCom**不具备**Com**所提供的那种控制**I-PDU**组的能力。

因此，可以通过配置**PduR**路由路径组来控制受影响的**PduR**路由路径（类似于**COM**中的**I-PDU**组）。

**PduR**路由路径组通过以下**API**控制：**PduR_EnableRouting(\<routing path group id\>)**和**PduR_DisableRouting(\<routing path group id\>)**。

这些**API**可以由**BswM**基于特定的**BswM**规则调用。这使得**PduR**路由路径组的切换能够与部分网络结合使用，例如：**ComM**向**BswM**指示当前的**PNC**状态，**BswM**评估相应**BswM**规则的触发条件并触发**BswM**动作（控制**PduR**路由路径组）。

**请注意：**

* 如果需要控制**I-PDU**，建议通过**COM** **I-PDU**组控制**COM**的**I-PDU**，并通过切换**PduR**路由路径组控制其余的**I-PDU**。

以下场景说明如何管理一个**ECU**的**PduR**路由路径组。示例**ECU**具有一个带两个**VLAN**的物理以太网通道和三个部分网络集群。

**VLAN**的模式请求端口命名为**EthSM_Vlan1**和**EthSM_Vlan2**，部分网络集群的请求源命名为**PNC1**、**PNC2**和**PNC3**。**PNC1**的**I-PDU**仅通过**Vlan1**通信；**PNC2**的**I-PDU**通过**Vlan1**和**Vlan2**通信；**PNC3**的**I-PDU**仅通过**Vlan2**通信。当总线状态管理器发出指示时，**BswM**应检查哪些部分网络集群被请求。

```
rule activeWakeupVlan1 initially false {
  if ( EthSM_Vlan1 == ETHSM_BSWM_FULL_COMMUNICATION){
    actionlist activeWakeupVlan1Actions
  }
}
actions activeWakeupVlan1Actions on condition{
  rule pnc1requested
  rule pnc2requested
}

rule activeWakeupVlan2 initially false{
  if ( EthSM_Vlan2 == ETHSM_BSWM_FULL_COMMUNICATION
       && PNC2 != PNC_REQUESTED && PNC3 != PNC_REQUESTED )
  {
    actionlist activeWakeupVlan2Actions
  }
}
actions activeWakeupVlan2Actions on condition{
  rule pnc2requested
  rule pnc3requested
}
```

清单3.29：通道上的主动唤醒

如果总线状态管理器报告某个**VLAN**即将离线，**BswM**会禁用相应的**I-PDU**路由路径组。如果该通道是一个部分网络的一部分，则必须禁用整个部分网络。

```
rule offlineVlan1 initially false {
  if (EthSM_Vlan1 == ETHSM_BSWM_NO_COMMUNICATION){
    actionlist offlineVlan1Actions
  }
}
actions offlineVlan1Actions on condition {
  PduRRoutingPathGroupSwitch{
    init true
    disable ArMmExample.EcuC.MyPduR.VLAN1_IPDU_ROUTING_PATHS,
            ArMmExample.EcuC.MyPduR.PNC1_IPDU_ROUTING_PATHS,
            ArMmExample.EcuC.MyPduR.PNC2_IPDU_ROUTING_PATHS
  }
}

rule offlineVlan2 initially false {
  if ( EhtSM_Can2 == CANSM_BSWM_NO_COMMUNICATION ) {
    actionlist offlineVlan2Actions
  }
}
actions offlineVlan2Actions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyPduR.VLAN2_IPDU_ROUTING_PATHS,
            ArMmExample.EcuC.MyPduR.PNC2_IPDU_ROUTING_PATHS,
            ArMmExample.EcuC.MyPduR.PNC3_IPDU_ROUTING_PATHS
  }
}
```

清单3.30：EthSM报告NO_COMMUNICATION

当单个部分网络集群被释放时，代表该网络的**I-PDU**路由路径组必须被禁用。

```
rule pnc1nocom initially false {
  if ( PNC1 == PNC_NO_COMMUNICATION ) {
    actionlist pnc1nocomTrueActions
  }
}
actions pnc1nocomActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyPduR.PNC1_IPDU_ROUTING_PATHS
  }
}

rule pnc2nocom initially false {
  if ( PNC2 == PNC_NO_COMMUNICATION ) {
    actionlist pnc2nocomTrueActions
  }
}
actions pnc2nocomActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyPduR.PNC2_IPDU_ROUTING_PATHS
  }
}

rule pnc3nocom initially false {
  if ( PNC3 == PNC_NO_COMMUNICATION ) {
    actionlist pnc3nocomActions
  }
}
actions pnc3nocomActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    disable ArMmExample.EcuC.MyPduR.PNC3_IPDU_ROUTING_PATHS
  }
}
```

清单3.31：PNC报告NO_COMMUNICATION

如果一个部分网络集群被请求，则使能相应的**I-PDU**路由路径组。

```
rule pnc1requested initially false {
  if ( PNC1 == PNC_REQUESTED || PNC1 == PNC_READY_SLEEP ) {
    actionlist pnc1requestedActions
  }
}
actions pnc1requestedActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyPduR.PNC1_IPDU_ROUTING_PATHS
  }
}

rule pnc2requested initially false {
  if ( PNC2 == PNC_REQUESTED || PNC2 == PNC_READY_SLEEP ) {
    actionlist pnc2requestedActions
  }
}
actions pnc2requestedActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyPduR.PNC2_IPDU_ROUTING_PATHS
  }
}

rule pnc3requested initially false {
  if ( PNC3 == PNC_REQUESTED || PNC3 == PNC_READY_SLEEP ) {
    actionlist pnc3requestedActions
  }
}
actions pnc3requestedActions on condition {
  PduRRoutingPathGroupSwitch {
    init true
    enable ArMmExample.EcuC.MyPduR.PNC2_IPDU_ROUTING_PATHS
  }
}
```

清单3.32：PNC报告PNC_REQUESTED或PNC_READY_SLEEP

#### 3.4.10. 服务发现控制

**AUTOSAR**提供了一种由应用软件组件控制面向服务通信的标准方式。它利用**BswM**进行模式管理的通用手段。

为了实现标准的接口和行为，模式请求端口和模式切换接口与**BswM**的配置描述一起被标准化（参见[4]《基础软件模式管理器规范》第7.8章）。这样，不仅接口得到了很好的定义，期望的行为也得到了很好的定义。

配置描述旨在供工具链使用，生成一组相互匹配的规则和动作列表，以提供对服务发现的实际控制。

自动提供/自动订阅（**auto-offer/auto-subscribe**）与项目自定义的方法可以并行使用。唯一的例外是：如果使用了自动提供/自动订阅，则同一**ECU**上的同一服务实例不能再进行应用层控制。

图3.3展示了标准化服务发现控制所涉及实体的概览。

图3.3：服务发现控制流概览

为了能够使用服务发现控制的标准手段，在设计应用**SWC**时就必须将其纳入考虑。

虽然必须在设计时就知道需要哪些用例，但实际的接口对它们将应用于哪种**SOA**技术完全无关。

图3.4：BswM交互中涉及端口连接的示例

对于一个需要请求订阅一个或多个事件的**SWC**，需要一个对应的**S/R**端口。

该端口将用于与服务发现交互这一事实，通过将**ServiceNeedsKind**设置为**BswMgrNeeds**来表达。

交互的类型由**RoleBasedDataAssignment**决定，它可以是一下几种之一：

* **ClientEventSubscription**
* **ClientEventSubscriptionStatus**
* **ServerServiceOffer**
* **ServerEventSubscriptionStatus**

到实际载荷端口（即：事件/方法）的映射，通过在**RepresentedPortGroup**中引用与此请求/通知相关的所有事件/方法端口来提供。

图3.5：模式请求端口与对应事件/方法（载荷数据）之间的映射

该映射在设计时完成。映射的粒度可以选择为1:1、为整个服务实例使用一个请求端口，或介于两者之间的任何形式。在使用**Some-IP**服务发现的情况下，例如：可以将其设定为与事件到事件组的映射相匹配。因此，**BswM**规则会据此处理，当一个**SWC**端口映射到多于一个事件/方法时，相应的规则和动作列表将实现"最高者胜出"（**highest wins**，针对请求）和"最低者胜出"（**lowest wins**，针对返回的指示）。

由于构建这些**BswM**规则所需的全部信息都可以通过**EcuExtract**和**EcuC**获得，配置工具可以生成完整的**BswM**配置，构建相应的请求和通知行为。更多细节请参阅[4]《基础软件模式管理器规范》。必要规则和动作列表的生成在[4]的第7.8.2–7.8.5章中描述。

图3.6展示了生成的配置可能的样子的一个示例。所有白色的框都预期由配置工具生成。

图3.6：生成的BswM配置示例