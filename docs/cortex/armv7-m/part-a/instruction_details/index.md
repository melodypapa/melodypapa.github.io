---
title: "指令详情（Instruction Details）"
---

本文译自 Part A《应用程序级架构》（Application level architecture） Chapter A7《指令详情》（Instruction Details）。

本章按字母顺序给出 **Armv7-M** Thumb 指令集中每条指令的详细说明，包括编码、汇编语法、操作伪代码与异常信息。本章不含插图；指令编码以位域表给出，位段编号与源文一致（**16 位编码**为单个半字，**32 位编码**为高低两个半字，分别对应指令位 `[15:0]` 与 `[31:16]`）。

## 1. 指令描述格式

第 7 节按字母顺序排列的指令列表中，每条指令的说明通常采用以下格式：

* 指令小节标题。
* 指令简介。
* 指令编码，以及架构信息。
* 汇编语法。
* 描述指令如何操作的伪代码。
* 异常信息。
* 注释（适用时）。

以下小节逐一详细说明这些条目。

少数指令说明描述的是其他指令的替代助记符，并采用该格式的简化修改版本。

### 1.1. 指令小节标题

指令小节标题给出本节所描述指令的基本助记符。当一个助记符有多种形式、且分别在不同小节描述时，标题后会用括号给出该形式的简短说明。最常见的用法是区分操作数为立即数的形式与操作数为寄存器的形式。

在某个助记符被新汇编语法中的另一助记符完全取代时，括号中的文字也用于记录它原来的助记符。

### 1.2. 指令简介

指令小节标题之后是简要描述该指令主要特征的文字。这段描述不一定完整，也不具有定义性。如果它与后文更详细的信息冲突，以后者为准。

### 1.3. 指令编码

编码小节包含一条或多条指令编码。为便于引用，每个 Thumb 指令编码都有一个编号标签，如 T1、T2。

每条指令编码的描述由以下内容组成：

* 关于哪些架构变体包含该指令特定编码的信息。自 Armv4T 起就存在的 Thumb 指令标注为 Thumb 指令集的所有版本，否则：
  * **Armv5T\*** 表示 Arm 架构版本 5 中所有包含 Thumb 指令支持的变体。
  * **Armv6-M** 表示 Arm 架构微控制器配置文件（microcontroller profile）中仅支持 Thumb 的变体，它与引入 Thumb-2 技术之前的 Armv6 Thumb 支持兼容。
  * **Armv7-M** 表示 Arm 架构微控制器配置文件中仅支持 Thumb 的变体，它通过 Thumb-2 技术以及故障处理支持等附加系统特性，在 Armv6-M 的基础上提供更高的性能与功能。

**注意：** 本手册不提供 Armv6 与 Armv7 非 M 配置文件的架构变体信息。此类信息参见《Arm Architecture Reference Manual, Armv7-A and Armv7-R edition》。

* 一种汇编语法，确保汇编器优先选用该编码而不是其他任何编码。某些情况下会给出多种语法。有时通过语法的注释（如 **Inside IT block**、**Outside IT block**）指出应使用哪一种。另一些情况下，可以通过阅读汇编语法描述、并用它判断被反汇编的指令对应哪种语法来确定。
  通常存在不止一种能保证重新汇编到某一特定编码的语法，而能够做到这一点的语法集合通常取决于寄存器编号、立即数常量以及指令的其他操作数。例如在汇编到 Thumb 指令集时，语法 `AND R0, R0, R8` 保证选择 32 位编码，而 `AND R0, R0, R1` 选择 16 位编码。
  为某个编码记录的汇编语法，是在该编码所支持的所有操作数组合下都能确保选中该编码的最简语法。这往往意味着它包含只对一小部分操作数组合才必要的元素。例如 32 位 Thumb `AND (register)` 编码记录的汇编语法包含 `.W` 限定符，以便即使在一小部分同时存在 16 位编码的操作数组合下也能选中 32 位编码。
  因此，为某个编码给出的汇编语法适合反汇编器将该编码反汇编成它；不过反汇编器在适合当前操作数组合时，可以使用更简单的语法，以产生可读性更好的反汇编代码。

* 编码图。16 位 Thumb 编码为半宽，32 位 Thumb 编码为全宽。Thumb 编码按两个半字的字节序处理，而不是按字的字节序，参见第 A3-68 页的「指令对齐与字节序」。

* 编码专用伪代码。它把编码专用的指令字段转换为后续 Operation 小节中与编码无关的伪代码的输入，并挑出编码中的特殊情况。关于所用伪代码的详细描述，以及编码图、编码专用伪代码与编码无关伪代码之间的关系，参见附录 D6《伪代码定义》。

### 1.4. 汇编语法

汇编语法小节描述该指令的标准 UAL 语法。

每条语法描述由以下元素组成：

* 一行或多行以打字机字体书写的语法原型行，遵循第 A7-174 页「汇编语法原型行约定」中描述的约定。每个原型行描述一整行汇编代码中的助记符与（适用时的）操作数部分。当存在多行时，每一行都被标注，以指出编码专用伪代码所要求的输出结果。对每一种指令编码，都可以用这些信息判断在汇编该语法时是否有匹配该编码的指令可用，以及具体是哪些。

* `where:` 行，其后是原型语法行中所有可变或可选字段的描述。有些语法字段在所有或大多数指令中都是标准化的。这些字段在第 A7-177 页的「标准汇编语法字段」中描述。

默认情况下，指定寄存器的语法字段（如 `&lt;Rd&gt;`、`&lt;Rn&gt;` 或 `&lt;Rt&gt;`）允许是 R0-R12 或 Thumb 指令中的 LR。这要求编码专用伪代码把相应的整数变量（如 `d`、`n` 或 `t`）设为对应的寄存器编号（R0-R12 为 0-12，LR 为 14）。通常可以通过把指令中的相应位域（如 `Rd`、`Rn` 或 `Rt`）设为该编号的二进制编码来实现。对 16 位 Thumb 编码，该位域通常为 3 位，因此只有在汇编语法中指定 R0-R7 之一时该编码才可用。这类编码也常使用 `Rdn` 这样的位域名，表示只有当 `&lt;Rd&gt;` 与 `&lt;Rn&gt;` 指定同一寄存器时该编码才可用，且该寄存器的编号编码在该位域中。

指定寄存器的语法字段的描述，有时会扩展或限制允许的寄存器范围，或记录与其他默认规则的不同之处。典型的扩展是允许使用 SP 与 PC 之一或两者，分别使用寄存器编号 13 与 15。

**注意：** pre-UAL Thumb 汇编语法与 UAL 不兼容，因此不在指令小节中记录。

#### 汇编语法原型行约定

汇编语法原型行及其子字段使用以下约定：

`&lt; &gt;`
> 任何用 `&lt;` 与 `&gt;` 括起来的条目，都是对该位置应由用户提供的值类型的简短描述。后续文字通常给出该条目的更详细描述。这类条目常对应指令编码图中同名的字段。当这种对应只是简单地把整数值或寄存器编号的二进制编码代入指令编码时，不做显式描述。例如，Thumb 指令的汇编语法包含条目 `&lt;Rn&gt;`、指令编码图包含 4 位字段 `Rn` 时，汇编语法中指定的寄存器编号就以二进制编码在该指令字段中。
>
> 如果汇编语法条目与指令编码之间的对应关系比简单的整数或寄存器编号二进制编码更复杂，条目描述会指出它如何编码。这常通过指定编码专用伪代码所要求的输出（如 `add = TRUE`）来完成；汇编器只能使用产生该输出的编码。

`{ }`
> 任何用 `{` 与 `}` 括起来的条目都是可选的。后续文字通常给出该条目的描述，以及它的存在或缺失在指令中如何编码。
>
> 许多指令有可选的目的寄存器。除非另有说明，如果省略这样的目的寄存器，则它与指令语法中紧随其后的源寄存器相同。

空格
> 用单个空格分隔条目，以求清晰。当汇编语法中空格是必需的时候，使用两个或更多连续空格。

`+/-`
> 表示可选的 `+` 或 `-` 号。如果都不写，则假定为 `+`。

其他所有字符都必须严格按汇编语法中的样子编码。除 `{` 与 `}` 外，上述特殊字符不出现在本手册所记录汇编指令的基本形式中。少数地方需要把 `{` 与 `}` 字符作为可变条目的一部分编码，此时可变条目的描述会说明它们必须如何使用。

### 1.5. 描述指令操作的伪代码

Operation 小节包含描述指令主要操作的与编码无关的伪代码。关于所用伪代码的详细描述，以及编码图、编码专用伪代码与编码无关伪代码之间的关系，参见附录 D6《伪代码定义》。

### 1.6. 异常信息

Exceptions 小节列出执行该指令可能引起的异常条件。

处理器异常按如下方式列出：

* 复位与中断（包括 NMI、PendSV 与 SysTick）不列出。它们可以在任何指令执行之前或之后发生，某些情况下也可以在指令执行期间发生，但一般不是由相关指令引起的。
* 所有执行显式数据存储器访问的指令都会列出 MemManage 与 BusFault 异常。所有指令取指都可能引起 MemManage 与 BusFault 异常，但它们不是由该指令的执行引起的，因此不列出。
* UsageFault 异常可能因多种原因发生，并按适用情况列在相应指令下。伪代码指出指令为 UNDEFINED 时也会发生 UsageFault 异常，这些 UsageFault 不列出。
* `SVC` 指令列出 SVCall 异常。
* `BKPT` 指令列出 DebugMonitor 异常。
* HardFault 异常可能来自指令所列故障的升级，但它本身不列出。

**注意：** 关于 MemManage、BusFault 与 UsageFault 各类异常的汇总，参见第 B1-551 页的「故障行为」。

### 1.7. 注释

适用时，关于指令的附加注释出现在进一步的子标题下。

## 2. 标准汇编语法字段

以下汇编语法字段在所有或大多数指令中都是标准的：

**&lt;c&gt;**
> 可选字段。它指定指令执行的条件。如果省略 `&lt;c&gt;`，则默认为 always（AL）。详情参见第 A4-104 页的「条件指令」。

**&lt;q&gt;**
> 指定指令上的可选汇编限定符。定义了以下限定符：
>
> * `.N`：含义为 narrow（窄），指定汇编器必须为该指令选择 16 位编码。如果不可能，则产生汇编器错误。
> * `.W`：含义为 wide（宽），指定汇编器必须为该指令选择 32 位编码。如果不可能，则产生汇编器错误。
>
> 如果 `.W` 与 `.N` 都未指定，汇编器可以选择 16 位或 32 位编码。如果两者都可用，必须选择 16 位编码。少数情况下，同一长度的多种编码对一条指令都可用。这些编码之间的选择规则是特定于指令的，属于指令描述的一部分。

## 3. 条件执行

**Armv7-M** 中的大多数 Thumb 指令都可以根据 APSR 条件标志的值条件执行。可用的条件列于表 A7-1。

在 Thumb 指令中，条件（如果不是 AL）通常编码在前置的 `IT` 指令中，详情参见第 A4-104 页的「条件指令」、第 A7-179 页的「ITSTATE」与第 A7-236 页的「IT」。某些条件分支指令不需要前置 `IT` 指令，其编码中直接包含条件码。

### 3.1. 条件执行的伪代码细节

`CurrentCond()` 伪代码函数的原型为：

```arm
bits(4) CurrentCond()
```

它返回一个 4 位条件说明符，规则如下：

* 对第 A7-205 页「B」中所示 Branch 指令的 T1 与 T3 编码，返回编码中的 4 位 `cond` 字段。
* 对其他所有 Thumb 指令：
  * 如果 `ITSTATE.IT<3:0> != '0000'`，返回 `ITSTATE.IT<7:4>`。
  * 如果 `ITSTATE.IT<7:0> == '00000000'`，返回 `'1110'`。
  * 否则，该指令的执行是 UNPREDICTABLE。

更多信息参见「ITSTATE」。

表 A7-1 条件码

| cond | 助记符扩展 | 含义（整数运算） | 含义（浮点运算）^a^ | 条件标志 |
| --- | --- | --- | --- | --- |
| 0000 | EQ | 相等（Equal） | 相等 | Z == 1 |
| 0001 | NE | 不相等（Not equal） | 不相等，或无序（unordered） | Z == 0 |
| 0010 | CS ^b^ | 进位置位（Carry set） | 大于、相等或无序 | C == 1 |
| 0011 | CC ^c^ | 进位清零（Carry clear） | 小于 | C == 0 |
| 0100 | MI | 负（Minus, negative） | 小于 | N == 1 |
| 0101 | PL | 正或零（Plus, positive or zero） | 大于、相等或无序 | N == 0 |
| 0110 | VS | 溢出（Overflow） | 无序 | V == 1 |
| 0111 | VC | 无溢出（No overflow） | 非无序 | V == 0 |
| 1000 | HI | 无符号高于（Unsigned higher） | 大于，或无序 | C == 1 and Z == 0 |
| 1001 | LS | 无符号低于或相同（Unsigned lower or same） | 小于或等于 | C == 0 or Z == 1 |
| 1010 | GE | 有符号大于或等于（Signed greater than or equal） | 大于或等于 | N == V |
| 1011 | LT | 有符号小于（Signed less than） | 小于，或无序 | N != V |
| 1100 | GT | 有符号大于（Signed greater than） | 大于 | Z == 0 and N == V |
| 1101 | LE | 有符号小于或等于（Signed less than or equal） | 小于、相等或无序 | Z == 1 or N != V |
| 1110 | 无（AL）^d^ | 始终（无条件） | 始终（无条件） | 任意 |

a. 无序（unordered）表示至少有一个 NaN 操作数。

b. HS（unsigned higher or same，无符号高于或相同）是 CS 的同义词。

c. LO（unsigned lower，无符号低于）是 CC 的同义词。

d. 除 `IT` 指令外，AL 是 always 的可选助记符扩展。详情参见第 A7-236 页的「IT」。

`ConditionPassed()` 函数使用该条件说明符与 APSR 条件标志，判断指令是否必须执行：

```arm
// ConditionPassed()
// =================
boolean ConditionPassed()
    cond = CurrentCond();

    // Evaluate base condition.
    case cond<3:1> of
        when '000'  result = (APSR.Z == '1');                        // EQ or NE
        when '001'  result = (APSR.C == '1');                        // CS or CC
        when '010'  result = (APSR.N == '1');                        // MI or PL
        when '011'  result = (APSR.V == '1');                        // VS or VC
        when '100'  result = (APSR.C == '1') && (APSR.Z == '0');     // HI or LS
        when '101'  result = (APSR.N == APSR.V);                     // GE or LT
        when '110'  result = (APSR.N == APSR.V) && (APSR.Z == '0');  // GT or LE
        when '111'  result = TRUE;                                   // AL

    // Condition flag values in the set '111x' indicate the instruction is always executed.
    // Otherwise, invert condition if necessary.
    if cond<0> == '1' && cond != '1111' then
        result = !result;

    return result;
```

### 3.2. 未定义指令的条件执行

在 **Armv7-M** 中，如果未定义指令的条件检查失败，该指令的行为是 NOP，且不引起异常。

**注意：** 条件字段为 `'1110'` 的 Branch（B）指令是 UNDEFINED，会引起异常，除非因 `IT` 指令的条件检查失败而被限定。

### 3.3. ITSTATE

ITSTATE 寄存器的位分配如下：

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IT[7] | IT[6] | IT[5] | IT[4] | IT[3] | IT[2] | IT[1] | IT[0] |

该寄存器保存 Thumb `IT` 指令的 If-Then 执行状态位。关于 `IT` 指令与相关 IT 块的描述，参见第 A7-236 页的「IT」。

ITSTATE 分为两个子字段：

**IT[7:5]**
> 保存当前 IT 块的基本条件。基本条件是 `IT` 指令所指定条件的高 3 位。
>
> 没有活动 IT 块时，该子字段为 `0b000`。

**IT[4:0]**
> 编码：
>
> * IT 块的大小，即要条件执行的指令条数。块的大小由该字段中最低有效 1 的位置隐含，如表 A7-2 所示。
> * 块中每条指令条件码最低有效位的值。把条件码最低有效位从 0 改为 1 的效果是反转条件码。
>
> 没有活动 IT 块时，该子字段为 `0b00000`。

执行 `IT` 指令时，这些位根据指令中的条件以及指令中的 Then 与 Else（T 与 E）参数设置，详情参见第 A7-236 页的「IT」。

IT 块中的指令是条件指令，参见第 A4-104 页的「条件指令」。所用条件是 IT[7:4] 的当前值。IT 块中的指令正常完成执行后，ITSTATE 推进到表 A7-2 的下一行。

这类指令发生异常时的情况，参见第 B1-531 页的「异常进入行为」。

**注意：** 通过分支正常完成执行的指令，只允许作为 IT 块的最后一条指令，因此总是使 ITSTATE 推进到正常执行。

**ITSTATE 操作的伪代码细节**

IT 块指令正常执行后 ITSTATE 推进，由 `ITAdvance()` 伪代码函数描述：

```arm
// ITAdvance()
// ===========
ITAdvance()
    if ITSTATE<2:0> == '000' then
        ITSTATE.IT = '00000000';
    else
        ITSTATE.IT<4:0> = LSL(ITSTATE.IT<4:0>, 1);
```

以下函数测试当前指令是否在 IT 块中，以及它是否为 IT 块的最后一条指令：

```arm
// InITBlock()
// ===========
boolean InITBlock()
    return (ITSTATE.IT<3:0> != '0000');

// LastInITBlock()
// ===============
boolean LastInITBlock()
    return (ITSTATE.IT<3:0> == '1000');
```

表 A7-2 IT 执行状态位的作用

| IT[7:5] | IT[4] | IT[3] | IT[2] | IT[1] | IT[0] | 含义 |
| --- | --- | --- | --- | --- | --- | --- |
| cond_base | P1 | P2 | P3 | P4 | 1 | 4 条指令 IT 块的进入点 |
| cond_base | P1 | P2 | P3 | 1 | 0 | 3 条指令 IT 块的进入点 |
| cond_base | P1 | P2 | 1 | 0 | 0 | 2 条指令 IT 块的进入点 |
| cond_base | P1 | 1 | 0 | 0 | 0 | 1 条指令 IT 块的进入点 |
| 000 | 0 | 0 | 0 | 0 | 0 | 正常执行，不在 IT 块中 |

a. 表中未显示的 IT 位组合为保留。

## 4. 施加于寄存器的移位

Thumb 数据处理指令可以对第二个操作数寄存器施加一系列常量移位。参见「常量移位」。

### 4.1. 常量移位

`<shift>` 是要施加于 `&lt;Rm&gt;` 的可选移位，可以是以下之一：

（省略）
> 等价于 `LSL #0`。

`LSL #&lt;n&gt;`
> 逻辑左移 `&lt;n&gt;` 位，`0 <= &lt;n&gt; <= 31`。

`LSR #&lt;n&gt;`
> 逻辑右移 `&lt;n&gt;` 位，`1 <= &lt;n&gt; <= 32`。

`ASR #&lt;n&gt;`
> 算术右移 `&lt;n&gt;` 位，`1 <= &lt;n&gt; <= 32`。

`ROR #&lt;n&gt;`
> 循环右移 `&lt;n&gt;` 位，`1 <= &lt;n&gt; <= 31`。

`RRX`
> 带扩展的一位循环右移：位 [0] 写入 `shifter_carry_out`，位 [31:1] 右移一位，进位标志移入位 [31]。

**编码**

汇编器把 `<shift>` 编码为两个类型位与五个立即数位，规则如下：

（省略）
> `type = 0b00`，`immediate = 0`。

`LSL #&lt;n&gt;`
> `type = 0b00`，`immediate = &lt;n&gt;`。

`LSR #&lt;n&gt;`
> `type = 0b01`。如果 `<n> &lt; 32`，`immediate = &lt;n&gt;`；如果 `<n> == 32`，`immediate = 0`。

`ASR #&lt;n&gt;`
> `type = 0b10`。如果 `<n> &lt; 32`，`immediate = &lt;n&gt;`；如果 `<n> == 32`，`immediate = 0`。

`ROR #&lt;n&gt;`
> `type = 0b11`，`immediate = &lt;n&gt;`。

`RRX`
> `type = 0b11`，`immediate = 0`。

### 4.2. 移位操作

```arm
// DecodeImmShift()
// ================

(SRType, integer) DecodeImmShift(bits(2) type, bits(5) imm5)

    case type of
        when '00'
            shift_t = SRType_LSL;  shift_n = UInt(imm5);
        when '01'
            shift_t = SRType_LSR;  shift_n = if imm5 == '00000' then 32 else UInt(imm5);
        when '10'
            shift_t = SRType_ASR;  shift_n = if imm5 == '00000' then 32 else UInt(imm5);
        when '11'
            if imm5 == '00000' then
                shift_t = SRType_RRX;  shift_n = 1;
            else
                shift_t = SRType_ROR;  shift_n = UInt(imm5);

    return (shift_t, shift_n);

// Shift()
// =======

bits(N) Shift(bits(N) value, SRType type, integer amount, bit carry_in)
    (result, -) = Shift_C(value, type, amount, carry_in);
    return result;

// Shift_C()
// =========

(bits(N), bit) Shift_C(bits(N) value, SRType type, integer amount, bit carry_in)
    assert !(type == SRType_RRX && amount != 1);
    if amount == 0 then
        (result, carry_out) = (value, carry_in);
    else
        case type of
            when SRType_LSL
                (result, carry_out) = LSL_C(value, amount);
            when SRType_LSR
                (result, carry_out) = LSR_C(value, amount);
            when SRType_ASR
                (result, carry_out) = ASR_C(value, amount);
            when SRType_ROR
                (result, carry_out) = ROR_C(value, amount);
            when SRType_RRX
                (result, carry_out) = RRX_C(value, carry_in);

    return (result, carry_out);
```

## 5. 存储器访问

存储器访问指令通常允许以下寻址模式：

**偏移寻址（Offset addressing）**
> 偏移值加到一个由基址寄存器得到的地址上，或从该地址中减去。结果用作存储器访问的地址。基址寄存器不变。
>
> 该模式的汇编语法为：
>
> ```arm
> [<Rn>,<offset>]
> ```

**前索引寻址（Pre-indexed addressing）**
> 偏移值施加到由基址寄存器得到的地址上。结果用作存储器访问的地址，并写回基址寄存器。
>
> 该模式的汇编语法为：
>
> ```arm
> [<Rn>,<offset>]!
> ```

**后索引寻址（Post-indexed addressing）**
> 由基址寄存器得到的地址原样用作存储器访问的地址。偏移值施加到该地址上，并写回基址寄存器。
>
> 该模式的汇编语法为：
>
> ```arm
> [<Rn>],<offset>
> ```

每种情况下 `&lt;Rn&gt;` 都是基址寄存器。`&lt;offset&gt;` 可以是：

* 一个立即数常量，如 `&lt;imm8&gt;` 或 `&lt;imm12&gt;`。
* 一个索引寄存器 `&lt;Rm&gt;`。
* 一个移位后的索引寄存器，如 `&lt;Rm&gt;, LSL #&lt;shift&gt;`。

关于非对齐访问、字节序与独占访问的信息，参见：

* 第 A3-65 页的「对齐支持」。
* 第 A3-67 页的「字节序支持」。
* 第 A3-70 页的「同步与信号量」。

## 6. 提示指令

Thumb 指令集包含以下提示指令类别：

* 存储器提示。
* 与 NOP 兼容的提示。

### 6.1. 存储器提示

某些 `Rt == 0b1111` 的加载指令是存储器提示。存储器提示使你能够向存储器系统提供关于未来存储器访问的预先信息，而不实际加载或存储任何数据。

`PLD` 与 `PLI` 是目前唯一已定义的存储器提示指令，参见第 A5-148 页的「加载字节、存储器提示」。指令详情参见：

* 第 A7-313 页的「PLD (immediate)」。
* 第 A7-314 页的「PLD (literal)」。
* 第 A7-315 页的「PLD (register)」。
* 第 A7-316 页的「PLI (immediate, literal)」。
* 第 A7-318 页的「PLI (register)」。

其他存储器提示目前尚未分配，参见第 A5-147 页的「加载半字、存储器提示」。存储器提示指令的效果由实现定义（IMPLEMENTATION DEFINED）。未分配的存储器提示必须实现为 NOP，软件不得使用它们。

### 6.2. 与 NOP 兼容的提示

与存储器访问无关的提示指令属于另一类提示指令，称为与 NOP 兼容的提示。与 NOP 兼容的提示提供由实现定义的行为，或充当 NOP。16 位与 32 位编码均为保留：

* 关于 16 位编码的信息，参见第 A5-135 页的「If-Then 与提示」。
* 关于 32 位编码的信息，参见第 A5-143 页的「提示指令」。

## 7. Armv7-M Thumb 指令按字母顺序列表

本小节列出所有 **Armv7-M** Thumb 指令。所用格式的详情参见第 A7-172 页的「指令描述格式」。

### 7.1. ADC (immediate)：立即数带进位加

立即数带进位加（Add with Carry (immediate)）。`ADC (immediate)` 把一个立即数与进位标志值加到一个寄存器值上，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`ADC{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 0 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ADC{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<const>`：指定要加到由 `<Rn>` 得到的值上的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `ADC<c>S` 等价于 `ADCS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], imm32, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.2. ADC (register)：寄存器带进位加

寄存器带进位加（Add with Carry (register)）。`ADC (register)` 把一个寄存器值、进位标志值以及一个可选移位的寄存器值相加，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADCS <Rdn>,<Rm>`（IT 块外）、`ADC<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`ADC{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ADC{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

特殊情况：如果写成 `ADC<c> <Rd>,<Rn>,<Rd>` 且 `<Rd>` 与 `<Rn>` 都在 R0-R7 范围内，汇编结果使用编码 T2，如同写的是 `ADC<c> <Rd>,<Rn>`。要避免这种情况，使用 `.W` 限定符。

pre-UAL 语法 `ADC<c>S` 等价于 `ADCS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], shifted, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.3. ADD (immediate)：立即数加法

立即数加法（Add (immediate)）。该指令把一个立即数加到一个寄存器值上，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = !InITBlock();  imm32 = ZeroExtend(imm3, 32);
d = UInt(Rdn);  n = UInt(Rdn);  setflags = !InITBlock();  imm32 = ZeroExtend(imm8, 32);
if Rd == '1111' && S == '1' then SEE CMN (immediate);
if Rn == '1101' then SEE ADD (SP plus immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d == 13 || (d == 15 && S == '0') || n == 15 then UNPREDICTABLE;
if Rn == '1111' then SEE ADR;
if Rn == '1101' then SEE ADD (SP plus immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = FALSE;  imm32 = ZeroExtend(i:imm3:imm8, 32);
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADDS <Rd>,<Rn>,#<imm3>`（IT 块外）、`ADD<c> <Rd>,<Rn>,#<imm3>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 1 | 1 | 1 | 0 | imm3 | imm3 | imm3 | Rn | Rn | Rn | Rd | Rd | Rd |

**编码 T2**（Thumb 指令集的所有版本）：`ADDS <Rdn>,#<imm8>`（IT 块外）、`ADD<c> <Rdn>,#<imm8>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 1 | 1 | 0 | Rdn | Rdn | Rdn | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`ADD{S}<c>.W <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 0 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T4**（Armv7-M）：`ADDW<c> <Rd>,<Rn>,#<imm12>`（`Rn` 必须为 SP）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ADD{S}<c><q>
  {<Rd>,} <Rn>, #<const>       // 允许所有编码
ADDW<c><q>
  {<Rd>,} <Rn>, #<const>       // 只允许编码 T4
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。如果为 `<Rn>` 指定 SP，参见第 A7-194 页的「ADD (SP plus immediate)」；如果为 `<Rn>` 指定 PC，参见第 A7-198 页的「ADR」。
* `<const>`：指定要加到由 `<Rn>` 得到的值上的立即数。允许的取值范围为：编码 T1 为 0-7，编码 T2 为 0-255，编码 T4 为 0-4095；编码 T3 的允许取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

当同一长度的多种编码可用时，编码 T3 优先于编码 T4（如需编码 T4，使用 `ADDW` 语法）。如果指定了 `<Rd>`，编码 T1 优先于编码 T2；如果省略 `<Rd>`，编码 T2 优先于编码 T1。

pre-UAL 语法 `ADD<c>S` 等价于 `ADDS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], imm32, '0');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.4. ADD (register)：寄存器加法

寄存器加法（Add (register)）。`ADD (register)` 把一个寄存器值与一个可选移位的寄存器值相加，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);
if (DN:Rdn) == '1101' || Rm == '1101' then SEE ADD (SP plus register);

d = UInt(DN:Rdn);  n = UInt(DN:Rdn);  m = UInt(Rm);  setflags = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);
if d == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
if d == 15 && m == 15 then UNPREDICTABLE;
if Rd == '1111' && S == '1' then SEE CMN (register);
if Rn == '1101' then SEE ADD (SP plus register);

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 || (d == 15 && S == '0') || n == 15 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADDS <Rd>,<Rn>,<Rm>`（IT 块外）、`ADD<c> <Rd>,<Rn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 1 | 1 | 0 | 0 | Rm | Rm | Rm | Rn | Rn | Rn | Rd | Rd | Rd |

**编码 T2**（Thumb 指令集的所有版本）：`ADD<c> <Rdn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | DN | Rm | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T3**（Armv7-M）：`ADD{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ADD{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同；如果两种编码都可用，编码 T2 优先于编码 T1（这只可能发生在 IT 块内）。如果指定了 `<Rd>`，编码 T1 优先于编码 T2。如果 `<Rm>` 不是 PC，编码 T2 中可以使用 PC。
* `<Rn>`：指定包含第一个操作数的寄存器。如果为 `<Rn>` 指定 SP，参见第 A7-196 页的「ADD (SP plus register)」。如果 `<Rm>` 不是 PC，编码 T2 中可以使用 PC。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。编码 T2 中可以使用 PC。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且所有编码都允许；如果指定 `<shift>`，只允许编码 T3。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

在 IT 块内，如果 `ADD<c> <Rd>,<Rn>,<Rd>` 无法用编码 T1 汇编，则使用编码 T2 汇编，如同写的是 `ADD<c> <Rd>,<Rn>`。要避免这种情况，使用 `.W` 限定符。

pre-UAL 语法 `ADD<c>S` 等价于 `ADDS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], shifted, '0');
    if d == 15 then
        ALUWritePC(result);  // setflags is always FALSE here
    else
        R[d] = result;
        if setflags then
            APSR.N = result<31>;
            APSR.Z = IsZeroBit(result);
            APSR.C = carry;
            APSR.V = overflow;
```

**异常**：无。

### 7.5. ADD (SP plus immediate)：SP 加立即数

SP 加立即数（Add (SP plus immediate)）。该指令把一个立即数加到 SP 值上，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  setflags = FALSE;  imm32 = ZeroExtend(imm8:'00', 32);
d = 13;  setflags = FALSE;  imm32 = ZeroExtend(imm7:'00', 32);
if Rd == '1111' && S == '1' then SEE CMN (immediate);
d = UInt(Rd);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d == 15 && S == '0' then UNPREDICTABLE;
d = UInt(Rd);  setflags = FALSE;  imm32 = ZeroExtend(i:imm3:imm8, 32);
if d == 15 then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADD<c> <Rd>,SP,#<imm8>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 0 | 1 | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Thumb 指令集的所有版本）：`ADD<c> SP,SP,#<imm7>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | imm7 | imm7 | imm7 | imm7 | imm7 | imm7 | imm7 |

**编码 T3**（Armv7-M）：`ADD{S}<c>.W <Rd>,SP,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 0 | 0 | 0 | S | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T4**（Armv7-M）：`ADDW<c> <Rd>,SP,#<imm12>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ADD{S}<c><q>
  {<Rd>,} SP, #<const>        // 允许所有编码
ADDW<c><q>
  {<Rd>,} SP, #<const>        // 只允许编码 T4
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器为 SP。
* `<const>`：指定要加到由 `<Rn>` 得到的值上的立即数。允许的取值为：编码 T1 为 0-1020 范围内 4 的倍数，编码 T2 为 0-508 范围内 4 的倍数，编码 T4 为 0-4095 范围内的任意值；编码 T3 的允许取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

当两个 32 位编码都可用时，编码 T3 优先于编码 T4（如需编码 T4，使用 `ADDW` 语法）。

pre-UAL 语法 `ADD<c>S` 等价于 `ADDS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(SP, imm32, '0');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.6. ADD (SP plus register)：SP 加寄存器

SP 加寄存器（Add (SP plus register)）。该指令把一个可选移位的寄存器值加到 SP 值上，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(DM:Rdm);  m = UInt(DM:Rdm);  setflags = FALSE;
if d == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
(shift_t, shift_n) = (SRType_LSL, 0);
if Rm == '1101' then SEE encoding T1;

d = 13;  m = UInt(Rm);  setflags = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);
if Rd == '1111' && S == '1' then SEE CMN (register);

d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 && (shift_t != SRType_LSL || shift_n > 3) then UNPREDICTABLE;
if (d == 15 && S == '0') || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADD<c> <Rdm>, SP, <Rdm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | DM | 1 | 1 | 0 | 1 | Rdm | Rdm | Rdm |

**编码 T2**（Thumb 指令集的所有版本）：`ADD<c> SP,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm | 1 | 0 | 1 |

**编码 T3**（Armv7-M）：`ADD{S}<c>.W <Rd>,SP,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | S | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ADD{S}<c><q>
  {<Rd>,} SP, <Rm>{, <shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器为 SP。在编码 T1 中使用 PC 作为 `<Rd>` 已被弃用。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。在编码 T1 中使用 SP 作为 `<Rm>` 已被弃用。在编码 T1 与编码 T2 中使用 PC 作为 `<Rm>` 已被弃用。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且所有编码都允许；如果指定 `<shift>`，只允许编码 T3。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。如果 `<Rd>` 为 SP 或被省略，`<shift>` 只允许为 `LSL #0`、`LSL #1`、`LSL #2` 或 `LSL #3`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(SP, shifted, '0');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.7. ADR：地址到寄存器

地址到寄存器（Address to Register）。`ADR` 把一个立即数加到 PC 值上，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  imm32 = ZeroExtend(imm8:'00', 32);  add = TRUE;

d = UInt(Rd);  imm32 = ZeroExtend(i:imm3:imm8, 32);  add = FALSE;
if d IN {13,15} then UNPREDICTABLE;

d = UInt(Rd);  imm32 = ZeroExtend(i:imm3:imm8, 32);  add = TRUE;
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ADR<c> <Rd>,<label>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 0 | 0 | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`ADR<c>.W <Rd>,<label>`，`<label>` 在当前指令之前

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`ADR<c>.W <Rd>,<label>`，`<label>` 在当前指令之后

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ADR<c><q>
  <Rd>, <label>                // 常规语法
ADD<c><q>
  <Rd>, PC, #<const>           // 编码 T1、T3 的替代形式
SUB<c><q>
  <Rd>, PC, #<const>           // 编码 T2 的替代形式
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<label>`：指定要加载其地址到 `<Rd>` 的指令或文字数据项的标签。汇编器从 `ADR` 指令的 `Align(PC,4)` 值到该标签计算所需偏移量。
  如果偏移为正，允许编码 T1 与编码 T3，且 `imm32` 等于该偏移。允许的偏移值为：编码 T1 为 0 到 1020 范围内 4 的倍数，编码 T3 为 0 到 4095 范围内的任意值。
  如果偏移为负，允许编码 T2，且 `imm32` 等于偏移的相反数。允许的偏移值为 -4095 到 -1。
  在替代语法形式中：
* `<const>`：对 `ADD` 形式指定偏移值，对 `SUB` 形式指定偏移值的相反数。允许的取值为：编码 T1 为 0 到 1020 范围内 4 的倍数，编码 T2 与编码 T3 为 0 到 4095 范围内的任意值。

**注意：** 建议尽可能避免使用替代语法形式。不过编码 T2 在所有立即数位都为零时，唯一可能的语法是 `SUB<c><q> <Rd>,PC,#0`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = if add then (Align(PC,4) + imm32) else (Align(PC,4) - imm32);
    R[d] = result;
```

**异常**：无。

### 7.8. AND (immediate)：立即数与

立即数与（AND (immediate)）。该指令把一个寄存器值与一个立即数按位与，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if Rd == '1111' && S == '1' then SEE TST (immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d == 13 || (d == 15 && S == '0') || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`AND{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
AND{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<const>`：指定要与由 `<Rn>` 得到的值进行按位与的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `AND<c>S` 等价于 `ANDS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] AND imm32;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.9. AND (register)：寄存器与

寄存器与（AND (register)）。`AND (register)` 把一个寄存器值与一个可选移位的寄存器值按位与，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);
if Rd == '1111' && S == '1' then SEE TST (register);

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 || (d == 15 && S == '0') || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ANDS <Rdn>,<Rm>`（IT 块外）、`AND<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`AND{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
AND{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `AND<c>S` 等价于 `ANDS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    result = R[n] AND shifted;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;   // carry is unchanged
        // APSR.V unchanged
```

**异常**：无。

### 7.10. ASR (immediate)：立即数算术右移

立即数算术右移（Arithmetic Shift Right (immediate)）。该指令把一个寄存器值右移一个立即数位数，移入其符号位的副本，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  setflags = !InITBlock();
(-, shift_n) = DecodeImmShift('10', imm5);

d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(-, shift_n) = DecodeImmShift('10', imm3:imm2);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ASRS <Rd>,<Rm>,#<imm5>`（IT 块外）、`ASR<c> <Rd>,<Rm>,#<imm5>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 1 | 0 | imm5 | imm5 | imm5 | imm5 | imm5 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`ASR{S}<c>.W <Rd>,<Rm>,#<imm5>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ASR{S}<c><q>
  <Rd>, <Rm>, #<imm5>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含第一个操作数的寄存器。
* `<imm5>`：指定移位量，取值范围为 1 到 32。参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `ASR<c>S` 等价于 `ASRS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry) = Shift_C(R[m], SRType_ASR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.11. ASR (register)：寄存器算术右移

寄存器算术右移（Arithmetic Shift Right (register)）。该指令把一个寄存器值右移一个可变位数，移入其符号位的副本，并把结果写入目的寄存器。该可变位数由另一寄存器的最低字节读出。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ASRS <Rdn>,<Rm>`（IT 块外）、`ASR<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`ASR{S}<c>.W <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ASR{S}<c><q>
  <Rd>, <Rn>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定其最低字节包含移位量的寄存器。

pre-UAL 语法 `ASR<c>S` 等价于 `ASRS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shift_n = UInt(R[m]<7:0>);
    (result, carry) = Shift_C(R[n], SRType_ASR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.12. B：分支

分支（Branch）。`B` 使控制流分支到目标地址。

**编码专用伪代码**

```arm
if cond == '1110' then SEE UDF;
if cond == '1111' then SEE SVC;
imm32 = SignExtend(imm8:'0', 32);
if InITBlock() then UNPREDICTABLE;

imm32 = SignExtend(imm11:'0', 32);
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;

if cond<3:1> == '111' then SEE "Related encodings";
imm32 = SignExtend(S:J2:J1:imm6:imm11:'0', 32);
if InITBlock() then UNPREDICTABLE;

I1 = NOT(J1 EOR S);  I2 = NOT(J2 EOR S);  imm32 = SignExtend(S:I1:I2:imm10:imm11:'0', 32);
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`B<c> <label>`，不允许在 IT 块内

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | cond | cond | cond | cond | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Thumb 指令集的所有版本）：`B<c> <label>`，在 IT 块外或为 IT 块中最后一条

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 0 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 |

**编码 T3**（Armv7-M）：`B<c>.W <label>`，不允许在 IT 块内

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | S | cond | cond | cond | cond | imm6 | imm6 | imm6 | imm6 | imm6 | imm6 |
| [31:16] | 1 | 0 | J1 | 0 | J2 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 |

**编码 T4**（Armv7-M）：`B<c>.W <label>`，在 IT 块外或为 IT 块中最后一条

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | S | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 |
| [31:16] | 1 | 0 | J1 | 1 | J2 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 |

**汇编语法**

```arm
B<c><q>
  <label>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<label>`：指定要分支到的指令的标签。汇编器从 `B` 指令的 PC 值到该标签计算所需偏移量，然后选择能把 `imm32` 设为该偏移量的编码。
  允许的偏移为偶数值，范围为：编码 T1 为 -256 到 254，编码 T2 为 -2048 到 2046，编码 T3 为 -1048576 到 1048574，编码 T4 为 -16777216 到 16777214。

**注意：** 编码 T1 与编码 T3 本身即为条件的，不需要 `IT` 指令使其条件化。

对编码 T1 与编码 T3，`<c>` 不允许为 AL 或省略。条件的 4 位编码放在指令中而不是前置的 `IT` 指令中，且该指令不允许处于 IT 块内。因此汇编器永远不会同时可用编码 T1 与编码 T2，也永远不会同时可用编码 T3 与编码 T4。

**相关编码**：参见第 A5-142 页的「分支与杂项控制」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    BranchWritePC(PC + imm32);
```

**异常**：无。

### 7.13. BFC：位域清零

位域清零（Bit Field Clear）。`BFC` 清零寄存器中任意位置上的任意数量相邻位，不影响寄存器中的其他位。

**编码专用伪代码**

```arm
d = UInt(Rd);  msbit = UInt(msb);  lsbit = UInt(imm3:imm2);
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`BFC<c> <Rd>,#<lsb>,#<width>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | msb | msb | msb | msb | msb |

**汇编语法**

```arm
BFC<c><q>
  <Rd>, #<lsb>, #<width>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<lsb>`：指定要清零的最低有效位，取值范围为 0 到 31。它决定 `lsbit` 的所需值。
* `<width>`：指定要清零的位数，取值范围为 1 到 32-`<lsb>`。`msbit` 的所需值为 `<lsb>`+`<width>`-1。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if msbit >= lsbit then
        R[d]<msbit:lsbit> = Replicate('0', msbit-lsbit+1);
        // R[d] 的其他位不变
    else
        UNPREDICTABLE;
```

**异常**：无。

### 7.14. BFI：位域插入

位域插入（Bit Field Insert）。`BFI` 把一个寄存器中的若干低位复制到目的寄存器中任意位置上的相同数量相邻位。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE BFC;
d = UInt(Rd);  n = UInt(Rn);  msbit = UInt(msb);  lsbit = UInt(imm3:imm2);
if d IN {13,15} || n == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`BFI<c> <Rd>,<Rn>,#<lsb>,#<width>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 0 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | msb | msb | msb | msb | msb |

**汇编语法**

```arm
BFI<c><q>
  <Rd>, <Rn>, #<lsb>, #<width>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定源寄存器。
* `<lsb>`：指定最低有效目的位，取值范围为 0 到 31。它决定 `lsbit` 的所需值。
* `<width>`：指定要复制的位数，取值范围为 1-32-`<lsb>`。`msbit` 的所需值为 `<lsb>`+`<width>`-1。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if msbit >= lsbit then
        R[d]<msbit:lsbit> = R[n]<(msbit-lsbit):0>;
        // R[d] 的其他位不变
    else
        UNPREDICTABLE;
```

**异常**：无。

### 7.15. BIC (immediate)：立即数位清零

立即数位清零（Bit Clear (immediate)）。该指令把一个寄存器值与一个立即数的按位取反值进行按位与，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`BIC{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 0 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
BIC{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含操作数的寄存器。
* `<const>`：指定其按位取反值要与由 `<Rn>` 得到的值进行按位与的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `BIC<c>S` 等价于 `BICS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] AND NOT(imm32);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.16. BIC (register)：寄存器位清零

寄存器位清零（Bit Clear (register)）。`BIC (register)` 把一个寄存器值与一个可选移位的寄存器值的按位取反值进行按位与，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`BICS <Rdn>,<Rm>`（IT 块外）、`BIC<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`BIC{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
BIC{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `BIC<c>S` 等价于 `BICS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    result = R[n] AND NOT(shifted);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;   // carry is unchanged
        // APSR.V unchanged
```

**异常**：无。

### 7.17. BKPT：断点

断点（Breakpoint）。`BKPT` 根据调试支持的配置引起 DebugMonitor 异常或调试暂停。

**注意：** `BKPT` 是无条件指令，在 IT 块内与块外都按无条件方式执行。

**编码专用伪代码**

```arm
imm32 = ZeroExtend(imm8, 32);
// imm32 仅用于汇编/反汇编，硬件忽略它。
```

**编码 T1**（Armv5T\*、Armv6-M、Armv7-M，M 配置特定行为）：`BKPT #<imm8>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
BKPT<q>#<imm8>
```

where：

* `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<imm8>`：指定存储在指令中的 8 位值。Arm 硬件忽略该值，但调试器可以用它存储关于断点的附加信息。

**操作**

```arm
EncodingSpecificOperations();
BKPTInstrDebugEvent();
```

**异常**：DebugMonitor。

### 7.18. BL：带链接分支

带链接分支（Branch with Link (immediate)）。`BL` 调用位于 PC 相对地址处的子程序。

**编码专用伪代码**

```arm
I1 = NOT(J1 EOR S);  I2 = NOT(J2 EOR S);  imm32 = SignExtend(S:I1:I2:imm10:imm11:'0', 32);
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`BL<c> <label>`，在 IT 块外或为 IT 块中最后一条

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | S | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 | imm10 |
| [31:16] | 1 | 1 | J1 | 1 | J2 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 | imm11 |

**汇编语法**

```arm
BL<c><q>
  <label>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<label>`：指定要分支到的指令的标签。汇编器从 `BL` 指令的 PC 值到该标签计算所需偏移量，然后选择能把 `imm32` 设为该偏移量的编码。允许的偏移为偶数值，范围为 -16777216 到 16777214。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    next_instr_addr = PC;
    LR = next_instr_addr<31:1> : '1';
    BranchWritePC(PC + imm32);
```

**异常**：无。

**注意：** 在 Thumb-2 技术引入之前，编码 T1 与编码 T2 中的 J1 与 J2 都为 1，因此分支范围较小。该指令可以拆成两条独立的 16 位指令执行：第一条指令 `instr1` 把 LR 设为 `PC + SignExtend(instr1<10:0>:'000000000000', 32)`，第二条指令完成操作。在 Armv6-M 与 Armv7-M 中无法把 `BL` 指令拆成两条 16 位指令。

### 7.19. BLX (register)：寄存器带链接与交换分支

寄存器带链接与交换分支（Branch with Link and Exchange）。`BLX (register)` 调用位于寄存器指定地址与指令集处的子程序。**Armv7-M** 仅支持 Thumb 指令集。尝试改变指令执行状态（Execution state）会使处理器在目标地址处的指令上进入异常。

**编码专用伪代码**

```arm
m = UInt(Rm);
if m == 15 then UNPREDICTABLE;
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv5T\*、Armv6-M、Armv7-M）：`BLX<c> <Rm>`，在 IT 块外或为 IT 块中最后一条

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | Rm | Rm | Rm | Rm | (0) | (0) | (0) |

**汇编语法**

```arm
BLX<c><q>
  <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rm>`：指定包含分支目标地址与指令集选择位的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    target = R[m];
    next_instr_addr = PC - 2;
    LR = next_instr_addr<31:1> : '1';
    BLXWritePC(target);
```

**异常**：UsageFault。

### 7.20. BX：分支与交换

分支与交换（Branch and Exchange）。`BX` 分支到寄存器指定的地址与指令集。**Armv7-M** 仅支持 Thumb 指令集。尝试改变指令执行状态会使处理器在目标地址处的指令上进入异常。

`BX` 也可用于异常返回，参见第 B1-539 页的「异常返回行为」。

**编码专用伪代码**

```arm
m = UInt(Rm);
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`BX<c> <Rm>`，在 IT 块外或为 IT 块中最后一条

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | Rm | Rm | Rm | Rm | (0) | (0) | (0) |

**汇编语法**

```arm
BX<c><q>
  <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rm>`：指定包含分支目标地址与指令集选择位的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    BXWritePC(R[m]);
```

**异常**：UsageFault。

### 7.21. CBNZ、CBZ：非零比较并分支、零比较并分支

非零比较并分支与零比较并分支（Compare and Branch on Non-Zero and Compare and Branch on Zero）。这两条指令把一个寄存器中的值与零比较，并条件性地向前分支一个常量值。它们不影响条件标志。

**编码专用伪代码**

```arm
n = UInt(Rn);  imm32 = ZeroExtend(i:imm5:'0', 32);  nonzero = (op == '1');
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`CB{N}Z <Rn>,<label>`，不允许在 IT 块内

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | op | 0 | i | 1 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn |

**汇编语法**

```arm
CB{N}Z<q>
  <Rn>, <label>
```

where：

* `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定第一个操作数寄存器。
* `<label>`：指定要分支到的指令的标签。汇编器从 `CB{N}Z` 指令的 PC 值到该标签计算所需偏移量，然后选择能把 `imm32` 设为该偏移量的编码。允许的偏移为偶数值，范围为 0-126。

**操作**

```arm
EncodingSpecificOperations();
if nonzero != IsZero(R[n]) then
    BranchWritePC(PC + imm32);
```

**异常**：无。

### 7.22. CDP、CDP2：协处理器数据处理

协处理器数据处理（Coprocessor Data Processing）。这两条指令告诉协处理器执行一个与 Arm 寄存器及存储器无关的操作。

如果没有协处理器能执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
cp = UInt(coproc);
cp = UInt(coproc);
```

**编码 T1**（Armv7-M）：`CDP<c> <coproc>,<opc1>,<CRd>,<CRn>,<CRm>,<opc2>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | opc1 | CRn | CRn | CRn | CRn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 0 | CRm | CRm | CRm | CRm |

**编码 T2**（Armv7-M）：`CDP2<c> <coproc>,<opc1>,<CRd>,<CRn>,<CRm>,<opc2>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | opc1 | CRn | CRn | CRn | CRn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 0 | CRm | CRm | CRm | CRm |

**汇编语法**

```arm
CDP{2}<c><q>
  <coproc>, #<opc1>, <CRd>, <CRn>, <CRm> {,#<opc2>}
```

where：

* `2`：如果指定，选择 `opc0 == 1` 形式的编码；如果省略，选择 `opc0 == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器名称，并把对应的协处理器编号放入指令的 `cp_num` 字段。通用协处理器名称为 p0-p15。
* `<opc1>`：协处理器专用操作码，取值范围为 0-15。
* `<CRd>`：指定该指令的目的协处理器寄存器。
* `<CRn>`：指定包含第一个操作数的协处理器寄存器。
* `<CRm>`：指定包含第二个操作数的协处理器寄存器。
* `<opc2>`：协处理器专用操作码，取值范围为 0-7。如果省略 `<opc2>`，则假定为 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        Coproc_InternalOperation(cp, ThisInstr());
```

**异常**：UsageFault。

**注意：协处理器字段**

只有指令的 `bits<31:24>`、`bits<11:8>` 与 `bit<4>` 是架构定义的。其余字段为建议值。

### 7.23. CLREX：清除独占

清除独占（Clear Exclusive）。`CLREX` 清除执行处理器关于某地址曾有独占访问请求的本地记录。

**编码专用伪代码**

```arm
// 无需附加译码
```

**编码 T1**（Armv7-M）：`CLREX<c>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 0 | 1 | 0 | (1) | (1) | (1) | (1) |

**汇编语法**

```arm
CLREX<c><q>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    ClearExclusiveLocal(ProcessorID());
```

**异常**：无。

### 7.24. CLZ：前导零计数

前导零计数（Count Leading Zeros）。`CLZ` 返回一个值中第一个二进制 1 位之前的二进制 0 位数。

**编码专用伪代码**

```arm
if !Consistent(Rm) then UNPREDICTABLE;
d = UInt(Rd);  m = UInt(Rm);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`CLZ<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rm |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
CLZ<c><q>
  <Rd>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。其编号必须在编码 T1 中编码两次，即 `Rm` 与 `Rm2` 两个字段。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = CountLeadingZeroBits(R[m]);
    R[d] = result<31:0>;
```

**异常**：无。

### 7.25. CMN (immediate)：立即数比较负数

立即数比较负数（Compare Negative (immediate)）。该指令把一个寄存器值与一个立即数相加。它根据结果更新条件标志，并丢弃结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  imm32 = ThumbExpandImm(i:imm3:imm8);
if n == 15 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`CMN<c> <Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
CMN<c><q>
  <Rn>, #<const>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定包含操作数的寄存器。该寄存器允许为 SP。
* `<const>`：指定要加到由 `<Rn>` 得到的值上的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], imm32, '0');
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    APSR.V = overflow;
```

**异常**：无。

### 7.26. CMN (register)：寄存器比较负数

寄存器比较负数（Compare Negative (register)）。该指令把一个寄存器值与一个可选移位的寄存器值相加。它根据结果更新条件标志，并丢弃结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = (SRType_LSL, 0);

n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if n == 15 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`CMN <Rn>,<Rm>`（IT 块外）、`CMN<c> <Rn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rn | Rn | Rn |

**编码 T2**（Armv7-M）：`CMN<c>.W <Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
CMN<c><q>
  <Rn>, <Rm> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定包含第一个操作数的寄存器。该寄存器允许为 SP。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], shifted, '0');
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    APSR.V = overflow;
```

**异常**：无。

### 7.27. CMP (immediate)：立即数比较

立即数比较（Compare (immediate)）。该指令从一个寄存器值中减去一个立即数。它根据结果更新条件标志，并丢弃结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);

n = UInt(Rn);  imm32 = ThumbExpandImm(i:imm3:imm8);
if n == 15 then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`CMP<c> <Rn>,#<imm8>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`CMP<c>.W <Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 1 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
CMP<c><q>
  <Rn>, #<const>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定包含操作数的寄存器。该寄存器允许为 SP。
* `<const>`：指定要从由 `<Rn>` 得到的值中减去的立即数。编码 T1 允许的取值范围为 0-255；编码 T2 允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], NOT(imm32), '1');
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    APSR.V = overflow;
```

**异常**：无。

### 7.28. CMP (register)：寄存器比较

寄存器比较（Compare (register)）。该指令从一个寄存器值中减去一个可选移位的寄存器值。它根据结果更新条件标志，并丢弃结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = (SRType_LSL, 0);

n = UInt(N:Rn);  m = UInt(Rm);
(shift_t, shift_n) = (SRType_LSL, 0);
if n < 8 && m < 8 then UNPREDICTABLE;
if n == 15 || m == 15 then UNPREDICTABLE;

n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if n == 15 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`CMP <Rn>,<Rm>`（IT 块外）、`CMP<c> <Rn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | Rm | Rm | Rm | Rn | Rn | Rn |

**编码 T2**（Thumb 指令集的所有版本）：`CMP <Rn>,<Rm>`（IT 块外）、`CMP<c> <Rn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | N | Rm | Rm | Rm | Rm | Rn | Rn | Rn |

**编码 T3**（Armv7-M）：`CMP<c>.W <Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
CMP<c><q>
  <Rn>, <Rm> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定包含第一个操作数的寄存器。可以使用 SP。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。可以使用 SP，但使用 SP 已被弃用。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且所有编码都允许；如果指定 `<shift>`，只允许编码 T3。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], NOT(shifted), '1');
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    APSR.V = overflow;
```

**异常**：无。

### 7.29. CPS：改变处理器状态

改变处理器状态（Change Processor State）。该指令修改 PRIMASK 与 FAULTMASK 特殊用途寄存器的值。

**注意：** `CPS` 是一条系统级指令，具有 **Armv7-M** 特定行为。完整的指令定义参见第 B5-673 页的「CPS」。

**编码 T1**（Armv6-M、Armv7-M；在 Armv7-M 中功能增强）：`CPS<effect> <iflags>`，不允许在 IT 块内

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | im | (0) | (0) | I | F |

**汇编语法**

```arm
CPS<effect> <iflags>
```

where：

* `<effect>`：指定是使能（`IE`）还是禁止（`ID`）由 `<iflags>` 指定的中断。
* `<iflags>`：指定要修改的中断标志，由下列字符的任意组合构成：`a`（异步中止）、`i`（IRQ）、`f`（FIQ）。

该指令的完整语义（包括 `im`、`I`、`F` 三个编码位的含义）参见第 B5-673 页的「CPS」。

### 7.30. CPY：复制

复制（Copy）。`CPY` 是 `MOV (register)` 的 pre-UAL 同义词。

**汇编语法**

```arm
CPY
  <Rd>, <Rn>
```

它等价于：

```arm
MOV
  <Rd>, <Rn>
```

**异常**：无。

### 7.31. CSDB：推测数据消费屏障

推测数据消费屏障（Consumption of Speculative Data Barrier）。`CSDB` 是一个内存屏障，用于控制推测执行与数据值预测。

在程序顺序中出现在 `CSDB` 之后的非分支指令、以及写 PC 的指令，不得使用以下任一结果进行推测执行：

* 任何指令的数据值预测。
* 在 `CSDB` 之前按程序顺序出现、且尚未在架构上解析的条件分支指令与写 PC 的条件指令的 `APSR.{N,Z,C,V}` 预测。

`APSR.{N,Z,C,V}` 不被视为数据值。该定义允许：

* 在 `CSDB` 之前与之后进行控制流推测。
* 在 `CSDB` 之后推测执行条件数据处理指令，除非它们使用了在 `CSDB` 之前按程序顺序出现、且尚未在架构上执行的指令的数据值预测或 `APSR.{N,Z,C,V}` 预测结果。

**编码专用伪代码**

```arm
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`CSDB<c>.W`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (0) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |

**汇编语法**

```arm
CSDB{<c>}.W
```

where：

* `<c>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    ConsumptionOfSpeculativeDataBarrier();
```

**异常**：无。

### 7.32. DBG：调试提示

调试提示（Debug Hint）。`DBG` 向调试跟踪支持及相关调试系统提供提示。该指令的实际用途（如果有）参见调试架构文档。

这是与 NOP 兼容的提示。关于一般提示行为的说明参见第 A7-185 页的「与 NOP 兼容的提示」。

**编码专用伪代码**

```arm
// 对 'option' 的任何译码都由调试系统规定
```

**编码 T1**（Armv7-M）：`DBG<c> #<option>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (0) | 0 | 0 | 0 | 1 | 1 | 1 | 1 | option | option | option | option |

**汇编语法**

```arm
DBG<c><q>
  #<option>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<option>`：提供关于该提示的附加信息，取值范围为 0-15。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    Hint_Debug(option);
```

**异常**：无。

### 7.33. DMB：数据内存屏障

数据内存屏障（Data Memory Barrier）。`DMB` 充当内存屏障。它确保按程序顺序出现在 `DMB` 指令之前的所有显式内存访问，都在按程序顺序出现在 `DMB` 指令之后的任何显式内存访问之前被观察到。它不影响处理器上执行的其他指令的顺序。

**编码专用伪代码**

```arm
// 无需附加译码
```

**编码 T1**（Armv6-M、Armv7-M）：`DMB<c> #<option>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 1 | option | option | option | option |

**汇编语法**

```arm
DMB<c><q>
  {<opt>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<opt>`：指定对 `DMB` 操作的可选限制。
  * `SY`：`DMB` 操作确保所有访问的顺序，编码为 `option == '1111'`。可以省略。
  * `option` 的其他所有编码均为保留。相应指令作为系统（SY）`DMB` 操作执行，但软件不得依赖该行为。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    DataMemoryBarrier(option);
```

**异常**：无。

### 7.34. DSB：数据同步屏障

数据同步屏障（Data Synchronization Barrier）。`DSB` 是一种特殊的内存屏障。按程序顺序位于该指令之后的指令，必须等到该指令完成才能执行。该指令仅在以下两个条件都满足时才算完成：

* 在该指令之前进行的所有显式内存访问都已完成。
* 执行改变上下文操作的任何 SCS 访问的副作用都已可见。

**注意：** 关于 SCS 更新同步的更多信息，参见第 A3-96 页的「系统控制空间更新的同步要求」。

**编码专用伪代码**

```arm
// 无需附加译码
```

**编码 T1**（Armv6-M、Armv7-M）：`DSB<c> #<option>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 0 | option | option | option | option |

**汇编语法**

```arm
DSB<c><q>
  {<opt>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<opt>`：指定对 `DSB` 操作的可选限制。取值为：
  * `SY`：`DSB` 操作确保所有访问的完成，编码为 `option == '1111'`。可以省略。
  * `option` 的其他所有编码均为保留。相应指令作为系统（SY）`DSB` 操作执行，但软件不得依赖该行为。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    DataSynchronizationBarrier(option);
```

**异常**：无。

### 7.35. EOR (immediate)：立即数异或

立即数异或（Exclusive OR (immediate)）。该指令把一个寄存器值与一个立即数进行按位异或，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if Rd == '1111' && S == '1' then SEE TEQ (immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d == 13 || (d == 15 && S == '0') || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`EOR{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 1 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
EOR{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含操作数的寄存器。
* `<const>`：指定要与由 `<Rn>` 得到的值进行异或的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `EOR<c>S` 等价于 `EORS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] EOR imm32;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.36. EOR (register)：寄存器异或

寄存器异或（Exclusive OR (register)）。该指令把一个寄存器值与一个可选移位的寄存器值进行按位异或，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);
if Rd == '1111' && S == '1' then SEE TEQ (register);

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 || (d == 15 && S == '0') || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`EORS <Rdn>,<Rm>`（IT 块外）、`EOR<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`EOR{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
EOR{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `EOR<c>S` 等价于 `EORS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = R[n] EOR shifted;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.37. ISB：指令同步屏障

指令同步屏障（Instruction Synchronization Barrier）。`ISB` 冲刷处理器流水线，使 `ISB` 之后的所有指令都在该指令完成后从缓存或存储器取指。它确保在该 `ISB` 指令之前完成的上下文改变操作（如对系统控制空间（SCS）的读写访问所产生的结果）对 `ISB` 之后取指的指令可见。

**注意：** 关于 SCS 更新同步的更多信息，参见第 A3-96 页的「系统控制空间更新的同步要求」。

此外，`ISB` 指令确保按程序顺序位于其后的任何分支都总是以 `ISB` 指令之后可见的上下文写入分支预测逻辑。这是确保指令流正确执行所必需的。

**编码专用伪代码**

```arm
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`ISB<c> {#<option>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 1 | 1 | 0 | option | option | option | option |

**汇编语法**

```arm
ISB<c><q>
  {<opt>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<opt>`：指定对 `ISB` 操作的可选限制。
  * `SY`：`ISB` 操作确保完成所有访问，编码为 `option == '1111'`。可以省略。
  * `option` 的其他所有编码均为保留。相应指令作为系统（SY）`ISB` 操作执行，但软件不得依赖该行为。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    InstructionSynchronizationBarrier(option);
```

**异常**：无。

### 7.38. IT：条件执行

If-Then。`IT` 使随后的最多四条指令（IT 块）成为条件执行的指令。IT 块中各指令的条件可以相同，也可以部分互为反条件。

`IT` 不影响条件标志。除异常返回所执行的分支外，不允许分支到 IT 块中的任何指令。

IT 块中除 `CMP`、`CMN` 与 `TST` 之外的 16 位指令不设置条件标志。可以指定 AL 条件，以便在不进行条件执行的情况下获得这种改变后的行为。

**编码专用伪代码**

```arm
if mask == '0000' then SEE "Related encodings";
if firstcond == '1111' || (firstcond == '1110' && BitCount(mask) != 1) then UNPREDICTABLE;
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`IT{x{y{z}}}<q> <firstcond>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | firstcond | firstcond | firstcond | firstcond | mask | mask | mask | mask |

**汇编语法**

```arm
IT{x{y{z}}}<q>
  <firstcond>
```

where：

* `<x>`：指定 IT 块中第二条指令的条件。
* `<y>`：指定 IT 块中第三条指令的条件。
* `<z>`：指定 IT 块中第四条指令的条件。
* `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<firstcond>`：指定 IT 块中第一条指令的条件。

`<x>`、`<y>`、`<z>` 的取值为 `T`（Then，与第一条指令条件相同）或 `E`（Else，与第一条指令条件相反）；省略时表示 IT 块在该处结束。表 A7-3 给出 `mask` 字段的确定方式。

表 A7-3 `mask` 字段的确定 ^a^

| `<x>` | `<y>` | `<z>` | mask[3] | mask[2] | mask[1] | mask[0] |
| --- | --- | --- | --- | --- | --- | --- |
| 省略 | 省略 | 省略 | 0 | 0 | 0 | 1 |
| T | 省略 | 省略 | 0 | 0 | 1 | firstcond[0] |
| E | 省略 | 省略 | 0 | 0 | 1 | NOT firstcond[0] |
| T | T | 省略 | 0 | 1 | firstcond[0] | firstcond[0] |
| T | E | 省略 | 0 | 1 | firstcond[0] | NOT firstcond[0] |
| E | T | 省略 | 0 | 1 | NOT firstcond[0] | firstcond[0] |
| E | E | 省略 | 0 | 1 | NOT firstcond[0] | NOT firstcond[0] |
| T | T | T | 1 | firstcond[0] | firstcond[0] | firstcond[0] |
| T | T | E | 1 | firstcond[0] | firstcond[0] | NOT firstcond[0] |
| T | E | T | 1 | firstcond[0] | NOT firstcond[0] | firstcond[0] |
| T | E | E | 1 | firstcond[0] | NOT firstcond[0] | NOT firstcond[0] |
| E | T | T | 1 | NOT firstcond[0] | firstcond[0] | firstcond[0] |
| E | T | E | 1 | NOT firstcond[0] | firstcond[0] | NOT firstcond[0] |
| E | E | T | 1 | NOT firstcond[0] | NOT firstcond[0] | firstcond[0] |
| E | E | E | 1 | NOT firstcond[0] | NOT firstcond[0] | NOT firstcond[0] |

a. 任何掩码中至少要有一位为 1。

参见第 A7-179 页的「ITSTATE」。

**操作**

```arm
EncodingSpecificOperations();
ITSTATE.IT<7:0> = firstcond:mask;
```

**异常**：无。

### 7.39. LDC、LDC2 (immediate)：立即数加载协处理器

加载协处理器（Load Coprocessor）。`LDC (immediate)` 把一串连续内存地址上的数据加载到协处理器。如果没有协处理器能执行该指令，则产生 UsageFault 异常。

这是通用协处理器指令。某些字段没有架构定义的功能，可供协处理器指令集设计者自由使用。这些字段是 `D` 位、`CRd` 字段，以及仅在非索引寻址模式下的 `imm8` 字段。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDC (literal);
if P == '0' && U == '0' && D == '0' && W == '0' then UNDEFINED;
if P == '0' && U == '0' && D == '1' && W == '0' then SEE MRRC, MRRC2;
n = UInt(Rn);  cp = UInt(coproc);  imm32 = ZeroExtend(imm8:'00', 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');

if Rn == '1111' then SEE LDC (literal);
if P == '0' && U == '0' && D == '0' && W == '0' then UNDEFINED;
if P == '0' && U == '0' && D == '1' && W == '0' then SEE MRRC, MRRC2;
n = UInt(Rn);  cp = UInt(coproc);  imm32 = ZeroExtend(imm8:'00', 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
```

**编码 T1**（Armv7-M）：`LDC<c> <coproc>,<CRd>,[<Rn>{,#<imm>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 0 | P | U | D | W | 1 | Rn | Rn | Rn | Rn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`LDC2<c> <coproc>,<CRd>,[<Rn>{,#<imm>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | P | U | D | W | 1 | Rn | Rn | Rn | Rn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDC{2}{<c>}{<q>} <coproc>, <CRd>, [<Rn>{, #<imm>}]
LDC{2}{<c>}{<q>} <coproc>, <CRd>, [<Rn>, #<imm>]!
LDC{2}{<c>}{<q>} <coproc>, <CRd>, [<Rn>], #<imm>
LDC{2}{<c>}{<q>} <coproc>, <CRd>, [<Rn>], {#<option>}
```

where：

* `2`：如果指定，选择 `opc0 == 1` 形式的编码；如果省略，选择 `opc0 == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器名称，取值范围为 p0-p15。
* `<CRd>`：指定目的协处理器寄存器。
* `<Rn>`：指定基址寄存器。如果为 `<Rn>` 指定 PC，参见第 A7-248 页的「LDC, LDC2 (literal)」。
* `!`：如果出现，表示回写基址寄存器。
* `<imm>`：施加到 `<Rn>` 值上以形成地址的立即数偏移。允许值为 0-1020 范围内 4 的倍数。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 +0。
* `<option>`：给协处理器的附加指令选项，取值范围为 0-255，用 `{ }` 括起来，编码在 `imm8` 中。

pre-UAL 语法 `LDC<c>L` 等价于 `LDCL<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
        address = if index then offset_addr else R[n];
        repeat
            Coproc_SendLoadedWord(MemA[address,4], cp, ThisInstr());  address = address + 4;
        until Coproc_DoneLoading(cp, ThisInstr());
        if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.40. LDC、LDC2 (literal)：文字加载协处理器

文字加载协处理器（Load Coprocessor (literal)）。该指令把一串连续内存地址上的数据加载到协处理器。如果没有协处理器能执行该指令，则产生 UsageFault 异常。

这是通用协处理器指令。`D` 位与 `CRd` 字段没有架构定义的功能，可供协处理器指令集设计者自由使用。

**编码专用伪代码**

```arm
if P == '0' && U == '0' && D == '0' && W == '0' then UNDEFINED;
if P == '0' && U == '0' && D == '1' && W == '0' then SEE MRRC, MRRC2;
index = (P == '1');     // 在 Thumb 指令集中始终为 TRUE
add = (U == '1');  cp = UInt(coproc);  imm32 = ZeroExtend(imm8:'00', 32);
if W == '1' || P == '0' then UNPREDICTABLE;

if P == '0' && U == '0' && D == '0' && W == '0' then UNDEFINED;
if P == '0' && U == '0' && D == '1' && W == '0' then SEE MRRC, MRRC2;
index = (P == '1');     // 在 Thumb 指令集中始终为 TRUE
add = (U == '1');  cp = UInt(coproc);  imm32 = ZeroExtend(imm8:'00', 32);
if W == '1' || P == '0' then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDC<c> <coproc>,<CRd>,<label>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 0 | P | U | D | W | 1 | 1 | 1 | 1 | 1 |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`LDC2<c> <coproc>,<CRd>,<label>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | P | U | D | W | 1 | 1 | 1 | 1 | 1 |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDC{2}{<c>}{<q>} <coproc>, <CRd>, <label>
```

where：

* `2`：如果指定，选择 `opc0 == 1` 形式的编码；如果省略，选择 `opc0 == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器名称，取值范围为 p0-p15。
* `<CRd>`：指定目的协处理器寄存器。
* `<label>`：指定该指令要加载其地址处的数据项的标签。汇编器从 `Align(PC,4)` 到该标签计算所需偏移量，并选择能把 `imm32` 设为该偏移量的编码。允许的偏移为 0-1020 范围内 4 的倍数。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        offset_addr = if add then (Align(PC,4) + imm32) else (Align(PC,4) - imm32);
        address = if index then offset_addr else Align(PC,4);
        repeat
            Coproc_SendLoadedWord(MemA[address,4], cp, ThisInstr());  address = address + 4;
        until Coproc_DoneLoading(cp, ThisInstr());
```

**异常**：UsageFault、MemManage、BusFault。
