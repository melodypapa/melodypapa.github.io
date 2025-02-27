<section id="title">复位（**Reset**）</section>

# 1. 介绍

本章描述了芯片的复位顺序和行为。

复位序列由具有固定序列的定义入口点组成，在完成后导致芯片的已知和确定状态。芯片上的一个或多个模块触发复位事件，这些复位事件决定了复位序列的入口点。

本章讨论以下细节：

* 芯片的全局复位行为
* 各种复位源
* 可能的复位序列及其阶段
* 软件可复位域，可以在不影响其他模块功能的情况下独立复位
* 模块在复位过程中的状态
* 低功耗（待机）模式进入和退出期间芯片的复位行为

下表显示了可导致其各自复位序列的复位事件类型。

| 复位事件       | 说明                                                                      |
| -------------- | ------------------------------------------------------------------------- |
| 功能性复位     | 芯片操作仍然可靠，**SRAM** 内存内容可以保留。导致无法保证功能的模块重置。 |
| 破坏性复位     | 除少数选定模块外，重置大部分芯片。在此复位事件后，内存内容被视为丢失。    |
| 上电复位 (POR) | 整个芯片被复位。                                                          |

# 复位 功能

该芯片的复位架构具有以下特点：

* 具有三个入口点的复位 序列控制：
   * 上电复位
   * 破坏性复位
   * 功能性复位 
* 破坏性和功能性复位事件的状态报告
* 功能复位升级为破坏性复位
* 破坏性复位升级以保持复位状态直到下一次 POR
* **SRAM** 内容保护免受任何功能复位事件的损坏
* 软件可复位域管理
* 芯片退出待机模式后复位管理
* 通过保险丝配置芯片



