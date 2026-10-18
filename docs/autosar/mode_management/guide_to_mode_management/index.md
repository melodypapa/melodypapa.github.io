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