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

### 7.41. LDM、LDMIA、LDMFD：多寄存器加载

多寄存器加载（Load Multiple）使用基址寄存器中的地址，从连续的内存位置加载多个寄存器。连续的存储位置从该地址开始，并可选择把最后一个位置之后的地址写回基址寄存器。

被加载的寄存器可以包含 PC。若包含，则为 PC 加载的字被当作分支地址或异常返回值。位[0]遵循 Arm 架构对分支到 Thumb 状态执行的互工作规则，必须为 1。如果位[0]为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
n = UInt(Rn);  registers = '00000000':register_list;  wback = (registers<n> == '0');
if BitCount(registers) < 1 then UNPREDICTABLE;
if W == '1' && Rn == '1101' then SEE POP (Thumb);

n = UInt(Rn);  registers = P:M:'0':register_list;  wback = (W == '1');
if n == 15 || BitCount(registers) < 2 || (P == '1' && M == '1') then UNPREDICTABLE;
if registers<15> == '1' && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
if wback && registers<n> == '1' then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDM<c> <Rn>!,<registers>`（`<Rn>` 不在 `<registers>` 中）、`LDM<c> <Rn>,<registers>`（`<Rn>` 在 `<registers>` 中）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T2**（Armv7-M）：`LDM<c>.W <Rn>{!},<registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | W | 1 | Rn | Rn | Rn | Rn |
| [31:16] | P | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**汇编语法**

```arm
LDM<c><q>
  <Rn>{!}, <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。如果它是 SP 且指定了 `!`，该指令按第 A7-319 页的「POP」中所述处理。
* `!`：使指令把修改后的值写回 `<Rn>`。如果省略 `!`，指令不会以这种方式改变 `<Rn>`。
* `<registers>`：要加载的一个或多个寄存器列表，用逗号分隔并用 `{` 与 `}` 包围。编号最小的寄存器从最低的内存地址加载，直到编号最大的寄存器从最高的内存地址加载。如果寄存器列表中指定了 PC，该指令分支到加载进 PC 的地址（数据）。
  * 编码 T2 不支持只含一个寄存器的列表。如果只有一个寄存器 `<Rt>` 的 `LDMIA` 指令汇编为 Thumb，且编码 T1 不可用，则汇编为等价的 `LDR<c><q> <Rt>,[<Rn>]{,#4}` 指令。
  * SP 不能在列表中。
  * 如果列表中包含 PC，则 LR 不能在列表中，且该指令必须位于 IT 块之外，或是 IT 块中的最后一条指令。

`LDMIA` 与 `LDMFD` 是 `LDM` 的伪指令。`LDMFD` 指其用于从满递减栈（Full Descending stack）弹出数据的用法。

pre-UAL 语法 `LDM<c>IA` 与 `LDM<c>FD` 等价于 `LDM<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];
    for i = 0 to 14
        if registers<i> == '1' then
            R[i] = MemA[address,4];  address = address + 4;
    if registers<15> == '1' then
        LoadWritePC(MemA[address,4]);
    if wback && registers<n> == '0' then R[n] = R[n] + 4*BitCount(registers);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.42. LDMDB、LDMEA：递减前多寄存器加载

递减前多寄存器加载（Load Multiple Decrement Before）——又称空递增栈多寄存器加载（Load Multiple Empty Ascending）——使用基址寄存器中的地址，从连续的内存位置加载多个寄存器。连续的存储位置结束于该地址正下方，并可选择把第一个位置的地址写回基址寄存器。

被加载的寄存器可以包含 PC。若包含，则为 PC 加载的字被当作分支地址或异常返回值。位<0>遵循 Arm 架构对分支到 Thumb 状态执行的互工作规则，必须为 1。如果位<0>为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
n = UInt(Rn);  registers = P:M:'0':register_list;  wback = (W == '1');
if n == 15 || BitCount(registers) < 2 || (P == '1' && M == '1') then UNPREDICTABLE;
if registers<15> == '1' && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
if wback && registers<n> == '1' then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDMDB<c> <Rn>{!},<registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | W | 1 | Rn | Rn | Rn | Rn |
| [31:16] | P | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**汇编语法**

```arm
LDMDB<c><q>
  <Rn>{!}, <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。可以使用 SP。
* `!`：使指令把修改后的值写回 `<Rn>`，编码为 `W = 1`。如果省略 `!`，指令不会以这种方式改变 `<Rn>`，编码为 `W = 0`。
* `<registers>`：一个或多个寄存器的列表，用逗号分隔并用 `{` 与 `}` 包围。它指定要加载的寄存器集合。编号最小的寄存器从最低的内存地址加载，直到编号最大的寄存器从最高的内存地址加载。如果寄存器列表中指定了 PC，该指令分支到加载进 PC 的地址（数据）。
  * 编码 T1 不支持只含一个寄存器的列表。如果只有一个寄存器 `<Rt>` 的 `LDMDB` 指令汇编为 Thumb，则汇编为等价的 `LDR<c><q> <Rt>,[<Rn>,#-4]{!}` 指令。
  * SP 不能在列表中。
  * 如果列表中包含 PC，则 LR 不能在列表中，且该指令必须位于 IT 块之外，或是 IT 块中的最后一条指令。

`LDMEA` 是 `LDMDB` 的伪指令，指其用于从空递增栈（Empty Ascending stack）弹出数据的用法。

pre-UAL 语法 `LDM<c>DB` 与 `LDM<c>EA` 等价于 `LDMDB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] - 4*BitCount(registers);
    for i = 0 to 14
        if registers<i> == '1' then
            R[i] = MemA[address,4];  address = address + 4;
    if registers<15> == '1' then
        LoadWritePC(MemA[address,4]);
    if wback && registers<n> == '0' then R[n] = R[n] - 4*BitCount(registers);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.43. LDR (immediate)：立即数加载寄存器

立即数加载寄存器（Load Register (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字并写入寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

被加载的寄存器可以是 PC。若是，则为 PC 加载的字被当作分支地址或异常返回值。位<0>遵循 Arm 架构对分支到 Thumb 状态执行的互工作规则，必须为 1。如果位<0>为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5:'00', 32);
index = TRUE;  add = TRUE;  wback = FALSE;

t = UInt(Rt);  n = 13;  imm32 = ZeroExtend(imm8:'00', 32);
index = TRUE;  add = TRUE;  wback = FALSE;

if Rn == '1111' then SEE LDR (literal);
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);  index = TRUE;  add = TRUE;
wback = FALSE;
if t == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;

if Rn == '1111' then SEE LDR (literal);
if P == '1' && U == '1' && W == '0' then SEE LDRT;
if Rn == '1101' && P == '0' && U == '1' && W == '1' && imm8 == '00000100' then SEE POP;
if P == '0' && W == '0' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);
imm32 = ZeroExtend(imm8, 32);  index = (P == '1');  add = (U == '1');  wback = (W == '1');
if (wback && n == t) || (t == 15 && InITBlock() && !LastInITBlock()) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDR<c> <Rt>, [<Rn>{,#<imm5>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 1 | 0 | 1 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Thumb 指令集的所有版本）：`LDR<c> <Rt>,[SP{,#<imm8>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 0 | 1 | 1 | Rt | Rt | Rt | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`LDR<c>.W <Rt>,[<Rn>{,#<imm12>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T4**（Armv7-M）：`LDR<c> <Rt>,[<Rn>,#-<imm8>]`、`LDR<c> <Rt>,[<Rn>],#+/-<imm8>`、`LDR<c> <Rt>,[<Rn>,#+/-<imm8>]!`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDR<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
LDR<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
LDR<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。该寄存器允许是 SP；也允许是 PC，前提是指令位于 IT 块之外或是 IT 块的最后一条指令。如果是 PC，则分支到加载进 PC 的地址（数据）。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。如果该寄存器是 PC，参见第 A7-248 页的「LDR (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。编码 T1 允许 0-124 范围内 4 的倍数，编码 T2 允许 0-1020 范围内 4 的倍数，编码 T3 允许 0-4095 范围内的任意值，编码 T4 允许 0-255 范围内的任意值。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

三种寻址形式：

* 偏移（Offset）：`index==TRUE`、`wback==FALSE`。
* 前索引（Pre-indexed）：`index==TRUE`、`wback==TRUE`。
* 后索引（Post-indexed）：`index==FALSE`、`wback==TRUE`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    data = MemU[address,4];
    if wback then R[n] = offset_addr;
    if t == 15 then
        if address<1:0> == '00' then LoadWritePC(data);  else UNPREDICTABLE;
    else
        R[t] = data;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.44. LDR (literal)：文字加载寄存器

文字加载寄存器（Load Register (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载一个字并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

被加载的寄存器可以是 PC。若是，则为 PC 加载的字被当作分支地址或异常返回值。位[0]遵循 Arm 架构对分支到 Thumb 状态执行的互工作规则，必须为 1。如果位[0]为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  imm32 = ZeroExtend(imm8:'00', 32);  add = TRUE;

t = UInt(Rt);  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
if t == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDR<c> <Rt>,<label>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 1 | Rt | Rt | Rt | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`LDR<c>.W <Rt>,<label>`（普通形式）、`LDR<c>.W <Rt>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | U | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
LDR<c><q>
  <Rt>, <label>
LDR<c><q>
  <Rt>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。可以使用 SP。可以使用 PC，前提是指令位于 IT 块之外或是 IT 块的最后一条指令。如果使用 PC，指令分支到加载进 PC 的地址（数据）。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从该指令的 PC 值到该标签所需的偏移值。允许的偏移值为：
  * 编码 T1：0 到 1020 范围内 4 的倍数。
  * 编码 T2：-4095 到 4095 范围内的任意值。
  如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。编码 T1 不支持负偏移。

**注意：** 在本手册的代码示例中，语法 `=<value>` 用于内容为常量且等于 `<value>` 的内存字的标签。这类标签的实际语法取决于汇编器。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = Align(PC,4);
    address = if add then (base + imm32) else (base - imm32);
    data = MemU[address,4];
    if t == 15 then
        if address<1:0> == '00' then LoadWritePC(data);  else UNPREDICTABLE;
    else
        R[t] = data;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.45. LDR (register)：寄存器加载寄存器

寄存器加载寄存器（Load Register (register)）由基址寄存器值与偏移寄存器值计算出地址，从存储器加载一个字并写入寄存器。偏移寄存器值可以左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

被加载的寄存器可以是 PC。若是，则为 PC 加载的字被当作分支地址或异常返回值。位[0]遵循 Arm 架构对分支到 Thumb 状态执行的互工作规则，必须为 1。如果位[0]为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);

if Rn == '1111' then SEE LDR (literal);
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if m IN {13,15} then UNPREDICTABLE;
if t == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDR<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDR<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LDR<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。该寄存器允许是 SP；也允许是 PC，前提是指令位于 IT 块之外或是 IT 块的最后一条指令。如果是 PC，则分支到加载进 PC 的地址（数据）。
* `<Rn>`：包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含左移后加到 `<Rn>` 值以形成地址的偏移。
* `<shift>`：`<Rm>` 值左移的位数，范围为 0-3。如果省略该选项，假定移位 0 且两种编码都允许；如果指定该选项，只允许编码 T2。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    offset_addr = if add then (R[n] + offset) else (R[n] - offset);
    address = if index then offset_addr else R[n];
    data = MemU[address,4];
    if wback then R[n] = offset_addr;
    if t == 15 then
        if address<1:0> == '00' then LoadWritePC(data);  else UNPREDICTABLE;
    else
        R[t] = data;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.46. LDRB (immediate)：立即数加载寄存器字节

立即数加载寄存器字节（Load Register Byte (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字节，将其零扩展为 32 位字后写入寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5, 32);
index = TRUE;  add = TRUE;  wback = FALSE;

if Rt == '1111' then SEE PLD;
if Rn == '1111' then SEE LDRB (literal);
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t == 13 then UNPREDICTABLE;

if Rt == '1111' && P == '1' && U == '0' && W == '0' then SEE PLD (immediate);
if Rn == '1111' then SEE LDRB (literal);
if P == '1' && U == '1' && W == '0' then SEE LDRBT;
if P == '0' && W == '0' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t == 13 || (wback && n == t) then UNPREDICTABLE;
if t == 15 && (P == '0' || U == '1' || W == '1') then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRB<c> <Rt>,[<Rn>{,#<imm5>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 1 | 1 | 1 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRB<c>.W <Rt>,[<Rn>{,#<imm12>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T3**（Armv7-M）：`LDRB<c> <Rt>,[<Rn>,#-<imm8>]`、`LDRB<c> <Rt>,[<Rn>],#+/-<imm8>`、`LDRB<c> <Rt>,[<Rn>,#+/-<imm8>]!`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRB<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
LDRB<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
LDRB<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。如果该寄存器是 PC，参见第 A7-254 页的「LDRB (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围：编码 T1 为 0-31，编码 T2 为 0-4095，编码 T3 为 0-255。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>B` 等价于 `LDRB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    R[t] = ZeroExtend(MemU[address,1], 32);
    if wback then R[n] = offset_addr;
```

**异常**：MemManage、BusFault。

### 7.47. LDRB (literal)：文字加载字节

文字加载字节（Load Register Byte (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载一个字节，将其零扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rt == '1111' then SEE PLD;
t = UInt(Rt);  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
if t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRB<c> <Rt>,<label>`（普通形式）、`LDRB<c> <Rt>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | U | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
LDRB<c><q>
  <Rt>, <label>
LDRB<c><q>
  <Rt>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从该指令的 PC 值到该标签所需的偏移值。允许的偏移值为 -4095 到 4095。如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

pre-UAL 语法 `LDR<c>B` 等价于 `LDRB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = Align(PC,4);
    address = if add then (base + imm32) else (base - imm32);
    R[t] = ZeroExtend(MemU[address,1], 32);
```

**异常**：MemManage、BusFault。

### 7.48. LDRB (register)：寄存器加载字节

寄存器加载字节（Load Register Byte (register)）由基址寄存器值与偏移寄存器值计算出地址，从存储器加载一个字节，将其零扩展形成 32 位字，并写入寄存器。偏移寄存器值可以左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);

if Rt == '1111' then SEE PLD;
if Rn == '1111' then SEE LDRB (literal);
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRB<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRB<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LDRB<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含左移后加到 `<Rn>` 值以形成地址的偏移。
* `<shift>`：`<Rm>` 值左移的位数，范围为 0-3。如果省略该选项，假定移位 0 且两种编码都允许；如果指定该选项，只允许编码 T2。

pre-UAL 语法 `LDR<c>B` 等价于 `LDRB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    offset_addr = if add then (R[n] + offset) else (R[n] - offset);
    address = if index then offset_addr else R[n];
    R[t] = ZeroExtend(MemU[address,1],32);
```

**异常**：MemManage、BusFault。

### 7.49. LDRBT：非特权加载字节

非特权加载字节（Load Register Byte Unprivileged）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字节，将其零扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `LDRBT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另参见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDRB (literal);
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRBT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRBT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围：0-255。`<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>BT` 等价于 `LDRBT<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    R[t] = ZeroExtend(MemU_unpriv[address,1],32);
```

**异常**：MemManage、BusFault。

### 7.50. LDRD (immediate)：立即数加载双字

立即数加载双字（Load Register Dual (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载两个字，并写入两个寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if P == '0' && W == '0' then SEE "Related encodings";
if Rn == '1111' then SEE LDRD (literal);
t = UInt(Rt);  t2 = UInt(Rt2);  n = UInt(Rn);  imm32 = ZeroExtend(imm8:'00', 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if wback && (n == t || n == t2) then UNPREDICTABLE;
if t IN {13,15} || t2 IN {13,15} || t == t2 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRD<c> <Rt>,<Rt2>,[<Rn>{,#+/-<imm8>}]`（偏移：`index == TRUE`、`wback == FALSE`）、`LDRD<c> <Rt>,<Rt2>,[<Rn>,#+/-<imm8>]!`（前索引：`index == TRUE`、`wback == TRUE`）、`LDRD<c> <Rt>,<Rt2>,[<Rn>],#+/-<imm8>`（后索引：`index == FALSE`、`wback == TRUE`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | P | U | 1 | W | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | Rt2 | Rt2 | Rt2 | Rt2 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRD<c><q>
  <Rt>, <Rt2>, [<Rn> {, #+/-<imm>}]
LDRD<c><q>
  <Rt>, <Rt2>, [<Rn>, #+/-<imm>]!
LDRD<c><q>
  <Rt>, <Rt2>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：第一个目的寄存器。
* `<Rt2>`：第二个目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。在语法的偏移寻址形式中，该寄存器也允许是 PC。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围为 0-1020 范围内 4 的倍数。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>D` 等价于 `LDRD<c>`。

**相关编码**：参见第 A5-145 页的「加载/存储双字或独占、表分支」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    R[t] = MemA[address,4];
    R[t2] = MemA[address+4,4];
    if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.51. LDRD (literal)：文字加载双字

文字加载双字（Load Register Dual (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载两个字，并写入两个寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**注意：** 对于 M 配置文件，PC 值必须按字对齐，否则该指令的行为是 UNPREDICTABLE。

**编码专用伪代码**

```arm
if P == '0' && W == '0' then SEE "Related encodings";
t = UInt(Rt);  t2 = UInt(Rt2);
imm32 = ZeroExtend(imm8:'00', 32);  add = (U == '1');
if t IN {13,15} || t2 IN {13,15} || t == t2 then UNPREDICTABLE;
if W == '1' then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRD<c> <Rt>,<Rt2>,<label>`（普通形式）、`LDRD<c> <Rt>,<Rt2>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | P | U | 1 | W | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | Rt2 | Rt2 | Rt2 | Rt2 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRD<c><q>
  <Rt>, <Rt2>, <label>
LDRD<c><q>
  <Rt>, <Rt2>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：第一个目的寄存器。
* `<Rt2>`：第二个目的寄存器。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从该指令的 PC 值到该标签所需的偏移值。允许的偏移值为 -1020 到 1020 范围内 4 的倍数。如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

pre-UAL 语法 `LDR<c>D` 等价于 `LDRD<c>`。

**相关编码**：参见第 A5-145 页的「加载/存储双字或独占、表分支」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if PC<1:0> != '00' then UNPREDICTABLE;
    address = if add then (PC + imm32) else (PC - imm32);
    R[t] = MemA[address,4];
    R[t2] = MemA[address+4,4];
```

**异常**：MemManage、BusFault。

### 7.52. LDREX：独占加载寄存器

独占加载寄存器（Load Register Exclusive）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字，写入寄存器，并且：

* 如果该地址具有可共享（shareable）的存储器属性，则在全局监视器中将该物理地址标记为执行处理器的独占访问。
* 使执行处理器在本地监视器中指示存在活动的独占访问。

关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8:'00', 32);
if t IN {13,15} || n == 15 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDREX<c> <Rt>,[<Rn>{,#<imm8>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | (1) | (1) | (1) | (1) | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDREX<c><q>
  <Rt>, [<Rn> {,#<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围为 0-1020 范围内 4 的倍数。`<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    SetExclusiveMonitors(address,4);
    R[t] = MemA[address,4];
```

**异常**：UsageFault、MemManage、BusFault。

### 7.53. LDREXB：独占加载字节

独占加载字节（Load Register Exclusive Byte）由基址寄存器值导出地址，从存储器加载一个字节，将其零扩展形成 32 位字，写入寄存器，并且：

* 如果该地址具有可共享（shareable）的存储器属性，则在全局监视器中将该物理地址标记为执行处理器的独占访问。
* 使执行处理器在本地监视器中指示存在活动的独占访问。

关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);
if t IN {13,15} || n == 15 then UNPREDICTABLE;
```

**编码 T1**（Armv7）：`LDREXB<c> <Rt>, [<Rn>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 0 | (1) | (1) | (1) | (1) |

**汇编语法**

```arm
LDREXB<c><q>
  <Rt>, [<Rn>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];
    SetExclusiveMonitors(address,1);
    R[t] = ZeroExtend(MemA[address,1], 32);
```

**异常**：MemManage、BusFault。

### 7.54. LDREXH：独占加载半字

独占加载半字（Load Register Exclusive Halfword）由基址寄存器值导出地址，从存储器加载一个半字，将其零扩展形成 32 位字，写入寄存器，并且：

* 如果该地址具有可共享（shareable）的存储器属性，则在全局监视器中将该物理地址标记为执行处理器的独占访问。
* 使执行处理器在本地监视器中指示存在活动的独占访问。

关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);
if t IN {13,15} || n == 15 then UNPREDICTABLE;
```

**编码 T1**（Armv7）：`LDREXH<c> <Rt>, [<Rn>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 1 | (1) | (1) | (1) | (1) |

**汇编语法**

```arm
LDREXH<c><q>
  <Rt>, [<Rn>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];
    SetExclusiveMonitors(address,2);
    R[t] = ZeroExtend(MemA[address,2], 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.55. LDRH (immediate)：立即数加载半字

立即数加载半字（Load Register Halfword (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个半字，将其零扩展形成 32 位字，并写入寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5:'0', 32);
index = TRUE;  add = TRUE;  wback = FALSE;

if Rt == '1111' then SEE PLD (immediate);
if Rn == '1111' then SEE LDRH (literal);
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t == 13 then UNPREDICTABLE;

if Rn == '1111' then SEE LDRH (literal);
if Rt == '1111' && P == '1' && U == '0' && W == '0' then SEE PLD;
if P == '1' && U == '1' && W == '0' then SEE LDRHT;
if P == '0' && W == '0' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t == 13 || (t == 15 && W == '1') || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRH<c> <Rt>,[<Rn>{,#<imm5>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 1 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRH<c>.W <Rt>,[<Rn>{,#<imm12>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T3**（Armv7-M）：`LDRH<c> <Rt>,[<Rn>,#-<imm8>]`、`LDRH<c> <Rt>,[<Rn>],#+/-<imm8>`、`LDRH<c> <Rt>,[<Rn>,#+/-<imm8>]!`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRH<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
LDRH<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
LDRH<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。如果该寄存器是 PC，参见第 A7-266 页的「LDRH (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围：编码 T1 为 0-62 范围内 2 的倍数，编码 T2 为 0-4095 范围内的任意值，编码 T3 为 0-255 范围内的任意值。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>H` 等价于 `LDRH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    data = MemU[address,2];
    if wback then R[n] = offset_addr;
    R[t] = ZeroExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

**未分配存储器提示**

如果编码 T2 中的 `Rt` 字段为 `'1111'`，或者编码 T3 中的 `Rt` 字段与 P、U、W 位分别为 `'1111'`、`'1'`、`'0'`、`'0'`，则该指令是未分配存储器提示（unallocated memory hint）。

未分配存储器提示必须实现为 NOP。软件不得使用它们，因此它们没有 UAL 汇编语法。

### 7.56. LDRH (literal)：文字加载半字

文字加载半字（Load Register Halfword (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载一个半字，将其零扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rt == '1111' then SEE PLD (literal);
t = UInt(Rt);  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
if t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRH<c> <Rt>,<label>`（普通形式）、`LDRH<c> <Rt>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | U | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
LDRH<c><q>
  <Rt>, <label>
LDRH<c><q>
  <Rt>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从 `ADR` 指令的 PC 值到该标签所需的偏移值。允许的偏移值为 -4095-4095。如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

pre-UAL 语法 `LDR<c>H` 等价于 `LDRH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = Align(PC,4);
    address = if add then (base + imm32) else (base - imm32);
    data = MemU[address,2];
    R[t] = ZeroExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.57. LDRH (register)：寄存器加载半字

寄存器加载半字（Load Register Halfword (register)）由基址寄存器值与偏移寄存器值计算出地址，从存储器加载一个半字，将其零扩展形成 32 位字，并写入寄存器。偏移寄存器值可以左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);

if Rn == '1111' then SEE LDRH (literal);
if Rt == '1111' then SEE "Related instructions";
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRH<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRH<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LDRH<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含左移后加到 `<Rn>` 值以形成地址的偏移。
* `<shift>`：`<Rm>` 值左移的位数，范围为 0-3。如果省略该选项，假定移位 0 且两种编码都允许；如果指定该选项，只允许编码 T2。

pre-UAL 语法 `LDR<c>H` 等价于 `LDRH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    offset_addr = if add then (R[n] + offset) else (R[n] - offset);
    address = if index then offset_addr else R[n];
    data = MemU[address,2];
    if wback then R[n] = offset_addr;
    R[t] = ZeroExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.58. LDRHT：非特权加载半字

非特权加载半字（Load Register Halfword Unprivileged）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个半字，将其零扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `LDRHT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另参见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDRH (literal);
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRHT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRHT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围：0-255。`<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    data = MemU_unpriv[address,2];
    R[t] = ZeroExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.59. LDRSB (immediate)：立即数加载有符号字节

立即数加载有符号字节（Load Register Signed Byte (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字节，将其符号扩展形成 32 位字，并写入寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rt == '1111' then SEE PLI;
if Rn == '1111' then SEE LDRSB (literal);
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t == 13 then UNPREDICTABLE;

if Rt == '1111' && P == '1' && U == '0' && W == '0' then SEE PLI;
if Rn == '1111' then SEE LDRSB (literal);
if P == '1' && U == '1' && W == '0' then SEE LDRSBT;
if P == '0' && W == '0' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t == 13 || (t == 15 && W == '1') || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSB<c> <Rt>,[<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T2**（Armv7-M）：`LDRSB<c> <Rt>,[<Rn>,#-<imm8>]`、`LDRSB<c> <Rt>,[<Rn>],#+/-<imm8>`、`LDRSB<c> <Rt>,[<Rn>,#+/-<imm8>]!`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRSB<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
LDRSB<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
LDRSB<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。如果该寄存器是 PC，参见第 A7-272 页的「LDRSB (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围：编码 T1 为 0-4095，编码 T2 为 0-255。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>SB` 等价于 `LDRSB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    R[t] = SignExtend(MemU[address,1], 32);
    if wback then R[n] = offset_addr;
```

**异常**：MemManage、BusFault。

### 7.60. LDRSB (literal)：文字加载有符号字节

文字加载有符号字节（Load Register Signed Byte (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载一个字节，将其符号扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rt == '1111' then SEE PLI;
t = UInt(Rt);  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
if t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSB<c> <Rt>,<label>`（普通形式）、`LDRSB<c> <Rt>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | U | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
LDRSB<c><q>
  <Rt>, <label>
LDRSB<c><q>
  <Rt>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从 `ADR` 指令的 PC 值到该标签所需的偏移值。允许的偏移值为 -4095-4095。如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

pre-UAL 语法 `LDR<c>SB` 等价于 `LDRSB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = Align(PC,4);
    address = if add then (base + imm32) else (base - imm32);
    R[t] = SignExtend(MemU[address,1], 32);
```

**异常**：MemManage、BusFault。

### 7.61. LDRSB (register)：寄存器加载有符号字节

寄存器加载有符号字节（Load Register Signed Byte (register)）由基址寄存器值与偏移寄存器值计算出地址，从存储器加载一个字节，将其符号扩展形成 32 位字，并写入寄存器。偏移寄存器值可以左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);

if Rt == '1111' then SEE PLI;
if Rn == '1111' then SEE LDRSB (literal);
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRSB<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRSB<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LDRSB<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含左移后加到 `<Rn>` 值以形成地址的偏移。
* `<shift>`：`<Rm>` 值左移的位数，范围为 0-3。如果省略该选项，假定移位 0 且两种编码都允许；如果指定该选项，只允许编码 T2。

pre-UAL 语法 `LDR<c>SB` 等价于 `LDRSB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    offset_addr = if add then (R[n] + offset) else (R[n] - offset);
    address = if index then offset_addr else R[n];
    R[t] = SignExtend(MemU[address,1], 32);
```

**异常**：MemManage、BusFault。

### 7.62. LDRSBT：非特权加载有符号字节

非特权加载有符号字节（Load Register Signed Byte Unprivileged）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字节，将其符号扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `LDRSBT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另参见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDRSB (literal);
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSBT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRSBT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围：0-255。`<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    R[t] = SignExtend(MemU_unpriv[address,1], 32);
```

**异常**：MemManage、BusFault。

### 7.63. LDRSH (immediate)：立即数加载有符号半字

立即数加载有符号半字（Load Register Signed Halfword (immediate)）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个半字，将其符号扩展形成 32 位字，并写入寄存器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDRSH (literal);
if Rt == '1111' then SEE "Related instructions";
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t == 13 then UNPREDICTABLE;

if Rn == '1111' then SEE LDRSH (literal);
if Rt == '1111' && P == '1' && U == '0' && W == '0' then SEE "Related instructions";
if P == '1' && U == '1' && W == '0' then SEE LDRSHT;
if P == '0' && W == '0' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t == 13 || (t == 15 && W == '1') || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSH<c> <Rt>,[<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T2**（Armv7-M）：`LDRSH<c> <Rt>,[<Rn>,#-<imm8>]`、`LDRSH<c> <Rt>,[<Rn>],#+/-<imm8>`、`LDRSH<c> <Rt>,[<Rn>,#+/-<imm8>]!`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRSH<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
LDRSH<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
LDRSH<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。如果该寄存器是 PC，参见第 A7-277 页的「LDRSH (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围：编码 T1 为 0-4095，编码 T2 为 0-255。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>SH` 等价于 `LDRSH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    data = MemU[address,2];
    if wback then R[n] = offset_addr;
    R[t] = SignExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.64. LDRSH (literal)：文字加载有符号半字

文字加载有符号半字（Load Register Signed Halfword (literal)）由 PC 值与立即数偏移计算出地址，从存储器加载一个半字，将其符号扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if Rt == '1111' then SEE "Related instructions";
t = UInt(Rt);  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
if t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSH<c> <Rt>,<label>`（普通形式）、`LDRSH<c> <Rt>,[PC,#-0]`（特殊情况）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | U | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
LDRSH<c><q>
  <Rt>, <label>
LDRSH<c><q>
  <Rt>, [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<label>`：要加载进 `<Rt>` 的文字数据项的标签。汇编器计算从 `ADR` 指令的 PC 值到该标签所需的偏移值。允许的偏移值为 -4095-4095。如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

pre-UAL 语法 `LDR<c>SH` 等价于 `LDRSH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = Align(PC,4);
    address = if add then (base + imm32) else (base - imm32);
    data = MemU[address,2];
    R[t] = SignExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

**未分配存储器提示**

如果编码 T1 中的 `Rt` 字段为 `'1111'`，则该指令是未分配存储器提示（unallocated memory hint）。

未分配存储器提示必须实现为 NOP。软件不得使用它们，因此它们没有 UAL 汇编语法。

### 7.65. LDRSH (register)：寄存器加载有符号半字

寄存器加载有符号半字（Load Register Signed Halfword (register)）由基址寄存器值与偏移寄存器值计算出地址，从存储器加载一个半字，将其符号扩展形成 32 位字，并写入寄存器。偏移寄存器值可以左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);

if Rn == '1111' then SEE LDRSH (literal);
if Rt == '1111' then SEE "Related instructions";
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LDRSH<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 1 | 1 | 1 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`LDRSH<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LDRSH<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含左移后加到 `<Rn>` 值以形成地址的偏移。
* `<shift>`：`<Rm>` 值左移的位数，范围为 0-3。如果省略该选项，假定移位 0 且两种编码都允许；如果指定该选项，只允许编码 T2。

pre-UAL 语法 `LDR<c>SH` 等价于 `LDRSH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    offset_addr = if add then (R[n] + offset) else (R[n] - offset);
    address = if index then offset_addr else R[n];
    data = MemU[address,2];
    if wback then R[n] = offset_addr;
    R[t] = SignExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.66. LDRSHT：非特权加载有符号半字

非特权加载有符号半字（Load Register Signed Halfword Unprivileged）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个半字，将其符号扩展形成 32 位字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `LDRSHT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另参见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDRSH (literal);
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRSHT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRSHT<c><q>
  <Rt>, [<Rn>, {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rm>` 值上以形成地址的立即数偏移。允许范围：0-255。`<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>SH` 等价于 `LDRSH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    data = MemU_unpriv[address,2];
    R[t] = SignExtend(data, 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.67. LDRT：非特权加载寄存器

非特权加载寄存器（Load Register Unprivileged）由基址寄存器值与立即数偏移计算出地址，从存储器加载一个字，并写入寄存器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `LDRT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另参见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE LDR (literal);
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`LDRT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
LDRT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：目的寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围：0-255。`<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `LDR<c>T` 等价于 `LDRT<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    data = MemU_unpriv[address,4];
    R[t] = data;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.68. LSL (immediate)：立即数逻辑左移

立即数逻辑左移（Logical Shift Left (immediate)）把一个寄存器值左移一个立即数位数，移入零，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if imm5 == '00000' then SEE MOV (register);
d = UInt(Rd);  m = UInt(Rm);  setflags = !InITBlock();
(-, shift_n) = DecodeImmShift('00', imm5);

if (imm3:imm2) == '00000' then SEE MOV (register);
d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(-, shift_n) = DecodeImmShift('00', imm3:imm2);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LSLS <Rd>,<Rm>,#<imm5>`（IT 块外）、`LSL<c> <Rd>,<Rm>,#<imm5>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 0 | 0 | imm5 | imm5 | imm5 | imm5 | imm5 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`LSL{S}<c>.W <Rd>,<Rm>,#<imm5>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LSL{S}<c><q>
  <Rd>, <Rm>, #<imm5>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含第一个操作数的寄存器。
* `<imm5>`：指定移位量，取值范围为 0 到 31。参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry) = Shift_C(R[m], SRType_LSL, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.69. LSL (register)：寄存器逻辑左移

寄存器逻辑左移（Logical Shift Left (register)）把一个寄存器值左移一个可变位数，移入零，并把结果写入目的寄存器。该可变位数取自另一个寄存器的低字节。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LSLS <Rdn>,<Rm>`（IT 块外）、`LSL<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`LSL{S}<c>.W <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LSL{S}<c><q>
  <Rd>, <Rn>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定其低字节包含移位量的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shift_n = UInt(R[m]<7:0>);
    (result, carry) = Shift_C(R[n], SRType_LSL, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.70. LSR (immediate)：立即数逻辑右移

立即数逻辑右移（Logical Shift Right (immediate)）把一个寄存器值右移一个立即数位数，移入零，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  setflags = !InITBlock();
(-, shift_n) = DecodeImmShift('01', imm5);

d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(-, shift_n) = DecodeImmShift('01', imm3:imm2);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LSRS <Rd>,<Rm>,#<imm5>`（IT 块外）、`LSR<c> <Rd>,<Rm>,#<imm5>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 0 | 1 | imm5 | imm5 | imm5 | imm5 | imm5 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`LSR{S}<c>.W <Rd>,<Rm>,#<imm5>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LSR{S}<c><q>
  <Rd>, <Rm>, #<imm5>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含第一个操作数的寄存器。
* `<imm5>`：指定移位量，取值范围为 1 到 32。参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry) = Shift_C(R[m], SRType_LSR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.71. LSR (register)：寄存器逻辑右移

寄存器逻辑右移（Logical Shift Right (register)）把一个寄存器值右移一个可变位数，移入零，并把结果写入目的寄存器。该可变位数取自另一个寄存器的低字节。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`LSRS <Rdn>,<Rm>`（IT 块外）、`LSR<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`LSR{S}<c>.W <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
LSR{S}<c><q>
  <Rd>, <Rn>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定其低字节包含移位量的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shift_n = UInt(R[m]<7:0>);
    (result, carry) = Shift_C(R[n], SRType_LSR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.72. MCR、MCR2：Arm 寄存器移到协处理器

从 Arm 寄存器移到协处理器（Move to Coprocessor from Arm Register）把某个 Arm 寄存器的值传给协处理器。

如果没有协处理器可以执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  cp = UInt(coproc);
if t == 15 || t == 13 then UNPREDICTABLE;

t = UInt(Rt);  cp = UInt(coproc);
if t == 15 || t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MCR<c> <coproc>,<opc1>,<Rt>,<CRn>,<CRm>{,<opc2>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | 0 | CRn | CRn | CRn | CRn |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 1 | CRm | CRm | CRm | CRm |

**编码 T2**（Armv7-M）：`MCR2<c> <coproc>,<opc1>,<Rt>,<CRn>,<CRm>{,<opc2>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | 0 | CRn | CRn | CRn | CRn |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 1 | CRm | CRm | CRm | CRm |

**注意：**

**协处理器字段**：只有指令位[31:24]、位[20]、位[15:8]与位[4]由 Arm 架构定义。其余字段属于建议。

**汇编语法**

```arm
MCR{2}<c><q>
  <coproc>, #<opc1>, <Rt>, <CRn>, <CRm>{, #<opc2>}
```

where：

* `2`：如果指定，选择 `C == 1` 形式的编码；如果省略，选择 `C == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器的名称。标准的通用协处理器名为 `p0`-`p15`。
* `<opc1>`：是协处理器专用的操作码，范围为 0-7。
* `<Rt>`：是值被传送给协处理器的 Arm 寄存器。
* `<CRn>`：是目的协处理器寄存器。
* `<CRm>`：是附加的目的协处理器寄存器。
* `<opc2>`：是协处理器专用的操作码，范围为 0-7。如果省略，假定 `<opc2>` 为 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        Coproc_SendOneWord(R[t], cp, ThisInstr());
```

**异常**：UsageFault。

### 7.73. MCRR、MCRR2：两个 Arm 寄存器移到协处理器

从两个 Arm 寄存器移到协处理器（Move to Coprocessor from two Arm Registers）把两个 Arm 寄存器的值传给协处理器。

如果没有协处理器可以执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  t2 = UInt(Rt2);  cp = UInt(coproc);
if t == 15 || t2 == 15 then UNPREDICTABLE;
if t == 13 || t2 == 13 then UNPREDICTABLE;

t = UInt(Rt);  t2 = UInt(Rt2);  cp = UInt(coproc);
if t == 15 || t2 == 15 then UNPREDICTABLE;
if t == 13 || t2 == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MCRR<c> <coproc>,<opc1>,<Rt>,<Rt2>,<CRm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | Rt2 | Rt2 | Rt2 | Rt2 |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc1 | opc1 | opc1 | opc1 | CRm | CRm | CRm | CRm |

**编码 T2**（Armv7-M）：`MCRR2<c> <coproc>,<opc1>,<Rt>,<Rt2>,<CRm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | Rt2 | Rt2 | Rt2 | Rt2 |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc1 | opc1 | opc1 | opc1 | CRm | CRm | CRm | CRm |

**汇编语法**

```arm
MCRR{2}<c><q>
  <coproc>, #<opc1>, <Rt>, <Rt2>, <CRm>
```

where：

* `2`：如果指定，选择 `C == 1` 形式的编码；如果省略，选择 `C == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器的名称。标准的通用协处理器名为 `p0`-`p15`。
* `<opc1>`：是协处理器专用的操作码，范围为 0-15。
* `<Rt>`：是值被传送给协处理器的第一个 Arm 寄存器。
* `<Rt2>`：是值被传送给协处理器的第二个 Arm 寄存器。
* `<CRm>`：是目的协处理器寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        Coproc_SendTwoWords(R[t2], R[t], cp, ThisInstr());
```

**异常**：UsageFault。

### 7.74. MLA：乘加

乘加（Multiply Accumulate）把两个寄存器值相乘，再加上第三个寄存器值。结果的低 32 位写入目的寄存器。这些 32 位与执行的是有符号还是无符号计算无关。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE MUL;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);  setflags = FALSE;
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MLA<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
MLA<c><q>
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定包含第二个操作数的寄存器。
* `<Ra>`：指定包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = SInt(R[n]);  // operand1 = UInt(R[n]) produces the same final results
    operand2 = SInt(R[m]);  // operand2 = UInt(R[m]) produces the same final results
    addend   = SInt(R[a]);  // addend   = UInt(R[a]) produces the same final results
    result = operand1 * operand2 + addend;
    R[d] = result<31:0>;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result<31:0>);
        // APSR.C unchanged
        // APSR.V unchanged
```

**异常**：无。

### 7.75. MLS：乘减

乘减（Multiply and Subtract）把两个寄存器值相乘，再以第三个寄存器值减去该结果的低 32 位。这些 32 位与执行的是有符号还是无符号计算无关。结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MLS<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
MLS<c><q>
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定包含第二个操作数的寄存器。
* `<Ra>`：指定包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = SInt(R[n]);  // operand1 = UInt(R[n]) produces the same final results
    operand2 = SInt(R[m]);  // operand2 = UInt(R[m]) produces the same final results
    addend   = SInt(R[a]);  // addend   = UInt(R[a]) produces the same final results
    result = addend - operand1 * operand2;
    R[d] = result<31:0>;
```

**异常**：无。

### 7.76. MOV (immediate)：立即数搬移

立即数搬移（Move (immediate)）把立即数值写入目的寄存器。它可以选择根据该值更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  setflags = !InITBlock();  imm32 = ZeroExtend(imm8, 32);  carry = APSR.C;

d = UInt(Rd);  setflags = (S == '1');  (imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d IN {13,15} then UNPREDICTABLE;

d = UInt(Rd);  setflags = FALSE;  imm32 = ZeroExtend(imm4:i:imm3:imm8, 32);
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`MOVS <Rd>,#<imm8>`（IT 块外）、`MOV<c> <Rd>,#<imm8>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 1 | 0 | 0 | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`MOV{S}<c>.W <Rd>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`MOVW<c> <Rd>,#<imm16>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 0 | 1 | 0 | 0 | imm4 | imm4 | imm4 | imm4 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
MOV{S}<c><q>
  <Rd>, #<const>
```
（允许所有编码）

```arm
MOVW<c><q>
  <Rd>, #<const>
```
（只允许编码 T3）

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<const>`：指定要放入 `<Rd>` 的立即数值。允许范围：编码 T1 为 0-255，编码 T3 为 0-65535。编码 T2 的允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

当一条指令同时有两种 32 位编码可用时，编码 T2 优先于编码 T3（如果需要编码 T3，使用 `MOVW` 语法）。

pre-UAL 语法 `MOV<c>S` 等价于 `MOVS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = imm32;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.77. MOV (register)：寄存器搬移

寄存器搬移（Move (register)）把一个值从寄存器复制到目的寄存器。它可以选择根据该值更新条件标志。

**编码专用伪代码**

```arm
d = UInt(D:Rd);  m = UInt(Rm);  setflags = FALSE;
if d == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;

d = UInt(Rd);  m = UInt(Rm);  setflags = TRUE;
if InITBlock() then UNPREDICTABLE;

d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
if setflags && (d IN {13,15} || m IN {13,15}) then UNPREDICTABLE;
if !setflags && (d == 15 || m == 15 || (d == 13 && m == 13)) then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M；如果 `<Rd>` 与 `<Rm>` 都在 R0-R7 内，则为 Thumb 指令集的所有版本）：`MOV<c> <Rd>,<Rm>`（如果 `<Rd>` 是 PC，则必须位于 IT 块外或是 IT 块的最后一条）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | D | Rm | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Thumb 指令集的所有版本）：`MOVS <Rd>,<Rm>`（不允许在 IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T3**（Armv7-M）：`MOV{S}<c>.W <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | 0 | 0 | 0 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
MOV{S}<c><q>
  <Rd>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。只要未指定 `S`，该寄存器可以是 SP 或 PC。如果 `<Rd>` 是 PC，则只允许编码 T1，且该指令分支到搬移到 PC 的地址。该指令必须位于 IT 块外，或是 IT 块的最后一条指令。
* `<Rm>`：源寄存器。该寄存器可以是 SP 或 PC。如果 `<Rm>` 是 SP 或 PC，则该指令不得指定 `S`。

如果出现下列任一情况，则不允许编码 T3：

* `<Rd>` 或 `<Rm>` 是 PC。
* `<Rd>` 与 `<Rm>` 都是 SP。

**注意：** Arm 不推荐使用下列 `MOV (register)` 指令：

* `<Rd>` 是 SP 或 PC 且 `<Rm>` 也是 SP 或 PC 的指令已废弃。
* 指定了 `S` 且 `<Rm>` 是 SP，或 `<Rm>` 是 PC 的指令已废弃。

pre-UAL 语法 `MOV<c>S` 等价于 `MOVS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[m];
    if d == 15 then
        ALUWritePC(result);  // setflags is always FALSE here
    else
        R[d] = result;
        if setflags then
            APSR.N = result<31>;
            APSR.Z = IsZeroBit(result);
            // APSR.C unchanged
            // APSR.V unchanged
```

**异常**：无。

### 7.78. MOV (shifted register)：移位寄存器搬移

移位寄存器搬移（Move (shifted register)）是 `ASR`、`LSL`、`LSR`、`ROR` 与 `RRX` 的同义词。

详细信息参见以下各节：

* 第 A7-203 页的「ASR (immediate)」。
* 第 A7-204 页的「ASR (register)」。
* 第 A7-282 页的「LSL (immediate)」。
* 第 A7-283 页的「LSL (register)」。
* 第 A7-284 页的「LSR (immediate)」。
* 第 A7-285 页的「LSR (register)」。
* 第 A7-338 页的「ROR (immediate)」。
* 第 A7-339 页的「ROR (register)」。
* 第 A7-340 页的「RRX」。

**汇编语法**

表 A7-4 给出 `MOV (shifted register)` 与其他指令之间的等价关系。

| MOV 指令 | 规范形式 |
| --- | --- |
| `MOV{S} <Rd>,<Rm>,ASR #<n>` | `ASR{S} <Rd>,<Rm>,#<n>` |
| `MOV{S} <Rd>,<Rm>,LSL #<n>` | `LSL{S} <Rd>,<Rm>,#<n>` |
| `MOV{S} <Rd>,<Rm>,LSR #<n>` | `LSR{S} <Rd>,<Rm>,#<n>` |
| `MOV{S} <Rd>,<Rm>,ROR #<n>` | `ROR{S} <Rd>,<Rm>,#<n>` |
| `MOV{S} <Rd>,<Rm>,ASR <Rs>` | `ASR{S} <Rd>,<Rm>,<Rs>` |
| `MOV{S} <Rd>,<Rm>,LSL <Rs>` | `LSL{S} <Rd>,<Rm>,<Rs>` |
| `MOV{S} <Rd>,<Rm>,LSR <Rs>` | `LSR{S} <Rd>,<Rm>,<Rs>` |
| `MOV{S} <Rd>,<Rm>,ROR <Rs>` | `ROR{S} <Rd>,<Rm>,<Rs>` |
| `MOV{S} <Rd>,<Rm>,RRX` | `RRX{S} <Rd>,<Rm>` |

反汇编时产生该指令的规范形式。

**异常**：无。

### 7.79. MOVT：搬移高半字

搬移高半字（Move Top）把立即数值写入目的寄存器的高半字。它不影响低半字的内容。

**编码专用伪代码**

```arm
d = UInt(Rd);  imm16 = imm4:i:imm3:imm8;
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MOVT<c> <Rd>,#<imm16>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 1 | 1 | 0 | 0 | imm4 | imm4 | imm4 | imm4 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
MOVT<c><q>
  <Rd>, #<imm16>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<imm16>`：指定要写入 `<Rd>` 的立即数值。该值必须在 0-65535 范围内。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    R[d]<31:16> = imm16;
    // R[d]<15:0> unchanged
```

**异常**：无。

### 7.80. MRC、MRC2：协处理器移到 Arm 寄存器

从协处理器移到 Arm 寄存器（Move to Arm Register from Coprocessor）使协处理器把一个值传送到 Arm 寄存器或条件标志。

如果没有协处理器可以执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  cp = UInt(coproc);
if t == 13 then UNPREDICTABLE;

t = UInt(Rt);  cp = UInt(coproc);
if t == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MRC<c> <coproc>,<opc1>,<Rt>,<CRn>,<CRm>{,<opc2>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | 1 | CRn | CRn | CRn | CRn |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 1 | CRm | CRm | CRm | CRm |

**编码 T2**（Armv7-M）：`MRC2<c> <coproc>,<opc1>,<Rt>,<CRn>,<CRm>{,<opc2>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | opc1 | opc1 | opc1 | 1 | CRn | CRn | CRn | CRn |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc2 | opc2 | opc2 | 1 | CRm | CRm | CRm | CRm |

**汇编语法**

```arm
MRC{2}<c><q>
  <coproc>, #<opc1>, <Rt>, <CRn>, <CRm>{, #<opc2>}
```

where：

* `2`：如果指定，选择 `C == 1` 形式的编码；如果省略，选择 `C == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器的名称。标准的通用协处理器名为 `p0`-`p15`。
* `<opc1>`：是协处理器专用的操作码，范围为 0-7。
* `<Rt>`：是目的 Arm 寄存器。该寄存器允许为 R0-R14 或 `APSR_nzcv`。后一种形式把传送值的位[31:28] 写入 N、Z、C 与 V 条件标志，其指定方式是把编码中的 `Rt` 字段置为 `0b1111`。在 pre-UAL 汇编语法中，该形式用 PC 而不是 `APSR_nzcv` 书写。
* `<CRn>`：是包含第一个操作数的协处理器寄存器。
* `<CRm>`：是附加的源或目的协处理器寄存器。
* `<opc2>`：是协处理器专用的操作码，范围为 0-7。如果省略，假定 `<opc2>` 为 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        value = Coproc_GetOneWord(cp, ThisInstr());
        if t != 15 then
            R[t] = value;
        else
            APSR.N = value<31>;
            APSR.Z = value<30>;
            APSR.C = value<29>;
            APSR.V = value<28>;
            // value<27:0> are not used.
```

**异常**：UsageFault。

### 7.81. MRRC、MRRC2：协处理器移到两个 Arm 寄存器

从协处理器移到两个 Arm 寄存器（Move to two Arm Registers from Coprocessor）使协处理器把值传送到两个 Arm 寄存器。

如果没有协处理器可以执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
t = UInt(Rt);  t2 = UInt(Rt2);  cp = UInt(coproc);
if t == 15 || t2 == 15 || t == t2 then UNPREDICTABLE;
if t == 13 || t2 == 13 then UNPREDICTABLE;

t = UInt(Rt);  t2 = UInt(Rt2);  cp = UInt(coproc);
if t == 15 || t2 == 15 || t == t2 then UNPREDICTABLE;
if t == 13 || t2 == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MRRC<c> <coproc>,<opc>,<Rt>,<Rt2>,<CRm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | Rt2 | Rt2 | Rt2 | Rt2 |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc1 | opc1 | opc1 | opc1 | CRm | CRm | CRm | CRm |

**编码 T2**（Armv7-M）：`MRRC2<c> <coproc>,<opc>,<Rt>,<Rt2>,<CRm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | Rt2 | Rt2 | Rt2 | Rt2 |
| [31:16] | Rt | Rt | Rt | Rt | coproc | coproc | coproc | coproc | opc1 | opc1 | opc1 | opc1 | CRm | CRm | CRm | CRm |

**汇编语法**

```arm
MRRC{2}<c><q>
  <coproc>, #<opc1>, <Rt>, <Rt2>, <CRm>
```

where：

* `2`：如果指定，选择 `C == 1` 形式的编码；如果省略，选择 `C == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器的名称。标准的通用协处理器名为 `p0`-`p15`。
* `<opc1>`：是协处理器专用的操作码，范围为 0-15。
* `<Rt>`：是第一个目的 Arm 寄存器。
* `<Rt2>`：是第二个目的 Arm 寄存器。
* `<CRm>`：是提供要传送数据的协处理器寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if !Coproc_Accepted(cp, ThisInstr()) then
        GenerateCoprocessorException();
    else
        (R[t2], R[t]) = Coproc_GetTwoWords(cp, ThisInstr());
```

**异常**：UsageFault。

### 7.82. MRS：从特殊寄存器移到寄存器

从特殊寄存器移到寄存器（Move to Register from Special register）把选定的专用寄存器的值移入通用 Arm 寄存器。

除访问 APSR 或 CONTROL 寄存器之外，`MRS` 是系统级指令。该指令的完整描述（包括其应用级用法）参见第 B5-675 页的「MRS」。

**编码 T1**（Armv6-M、Armv7-M；Armv7-M 中功能增强）：`MRS<c> <Rd>,<spec_reg>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | (0) | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | Rd | Rd | Rd | Rd | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm |

### 7.83. MSR：从寄存器移到特殊寄存器

从寄存器移到特殊寄存器（Move to Special Register from Arm Register）把通用 Arm 寄存器的值移到指定的专用寄存器。

除访问 APSR 之外，`MSR` 是系统级指令。该指令的完整描述（包括其应用级用法）参见第 B5-677 页的「MSR」。

**编码 T1**（Armv6-M、Armv7-M；Armv7-M 中功能增强）：`MSR<c> <spec_reg>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | (0) | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 0 | (0) | 0 | mask | mask | (0) | (0) | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm | SYSm |

### 7.84. MUL：乘法

乘法（Multiply）把两个寄存器值相乘。结果的低 32 位写入目的寄存器。这些 32 位与执行的是有符号还是无符号计算无关。

它可以选择根据结果更新条件标志。该选项在 Thumb 指令集中仅限于少数几种指令形式，并且在许多处理器实现上使用它会损害性能。

**编码专用伪代码**

```arm
d = UInt(Rdm);  n = UInt(Rn);  m = UInt(Rdm);  setflags = !InITBlock();

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = FALSE;
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`MULS <Rdm>,<Rn>,<Rdm>`（IT 块外）、`MUL<c> <Rdm>,<Rn>,<Rdm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rdm | Rdm | Rdm |

**编码 T2**（Armv7-M）：`MUL<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
MUL{S}<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定包含第二个操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = SInt(R[n]);  // operand1 = UInt(R[n]) produces the same final results
    operand2 = SInt(R[m]);  // operand2 = UInt(R[m]) produces the same final results
    result = operand1 * operand2;
    R[d] = result<31:0>;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result<31:0>);
        // APSR.C unchanged
        // APSR.V unchanged
```

**异常**：无。

### 7.85. MVN (immediate)：立即数按位取反

立即数按位取反（Bitwise NOT (immediate)）把立即数值的按位取反结果写入目的寄存器。它可以选择根据该值更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`MVN{S}<c> <Rd>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 1 | 1 | S | 1 | 1 | 1 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
MVN{S}<c><q>
  <Rd>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<const>`：指定加到从 `<Rn>` 得到的值上的立即数值。允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `MVN<c>S` 等价于 `MVNS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = NOT(imm32);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.86. MVN (register)：寄存器按位取反

寄存器按位取反（Bitwise NOT (register)）把寄存器值的按位取反结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);

d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`MVNS <Rd>,<Rm>`（IT 块外）、`MVN<c> <Rd>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`MVN{S}<c>.W <Rd>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
MVN{S}<c><q>
  <Rd>, <Rm> {, <shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定可选地移位并用作源寄存器的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读出的值的移位。如果省略 `<shift>`，不施加移位且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `MVN<c>S` 等价于 `MVNS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = NOT(shifted);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.87. NEG：取负

取负（Negate）是立即数为 0 的 `RSB (immediate)` 的 pre-UAL 同义词。详细信息参见第 A7-341 页的「RSB (immediate)」。

**汇编语法**

```arm
NEG<c><q>
  {<Rd>,} <Rm>
```

这等价于：

```arm
RSBS<c><q>
  {<Rd>,} <Rm>, #0
```

**异常**：无。

### 7.88. NOP：空操作

空操作（No Operation）不做任何事。

这是 NOP 兼容提示（NOP-compatible hint），即架构规定的 NOP，参见第 A7-185 页的「NOP 兼容提示」。

**编码专用伪代码**

```arm
// No additional decoding required

// No additional decoding required
```

**编码 T1**（Armv7-M）：`NOP<c>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**编码 T2**（Armv7-M）：`NOP<c>.W`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**汇编语法**

```arm
NOP<c><q>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    // Do nothing
```

**异常**：无。

### 7.89. ORN (immediate)：立即数逻辑或非

立即数逻辑或非（Logical OR NOT (immediate)）对一个寄存器值与一个立即数值的补码执行按位（包含）或，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE MVN (immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d IN {13,15} || n == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`ORN{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 1 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ORN{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含操作数的寄存器。
* `<const>`：指定加到从 `<Rn>` 得到的值上的立即数值。允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] OR NOT(imm32);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.90. ORN (register)：寄存器逻辑或非

寄存器逻辑或非（Logical OR NOT (register)）对一个寄存器值与一个可选移位的寄存器值的补码执行按位（包含）或，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE MVN (register);
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`ORN{S}<c> <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | S | Rn | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ORN{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选地移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读出的值的移位。如果省略 `<shift>`，不施加移位。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = R[n] OR NOT(shifted);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.91. ORR (immediate)：立即数逻辑或

立即数逻辑或（Logical OR (immediate)）对一个寄存器值与一个立即数值执行按位（包含）或，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE MOV (immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if d IN {13,15} || n == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`ORR{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
ORR{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含操作数的寄存器。
* `<const>`：指定加到从 `<Rn>` 得到的值上的立即数值。允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `ORR<c>S` 等价于 `ORRS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] OR imm32;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.92. ORR (register)：寄存器逻辑或

寄存器逻辑或（Logical OR (register)）对一个寄存器值与一个可选移位的寄存器值执行按位（包含）或，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);

if Rn == '1111' then SEE "Related encodings";
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`ORRS <Rdn>,<Rm>`（IT 块外）、`ORR<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`ORR{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | Rn | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ORR{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选地移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读出的值的移位。如果省略 `<shift>`，不施加移位且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

一种特殊情况：如果写的是 `ORR<c> <Rd>,<Rn>,<Rd>`，且 `<Rd>` 与 `<Rn>` 都在 R0-R7 范围内，则它会像写的是 `ORR<c> <Rd>,<Rn>` 一样用编码 T2 汇编。要避免这种情况，使用 `.W` 限定符。

pre-UAL 语法 `ORR<c>S` 等价于 `ORRS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = R[n] OR shifted;
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.93. PKHBT、PKHTB：半字打包

打包半字（Pack Halfword）指令把一个操作数的一个半字与另一个经过移位的操作数的另一个半字组合起来。

**编码专用伪代码**

```arm
if S == '1' || T == '1' then UNDEFINED;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  tbform = (tb == '1');
(shift_t, shift_n) = DecodeImmShift(tb:'0', imm3:imm2);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`PKHBT<c> <Rd>,<Rn>,<Rm>{,LSL #<imm>}`（`tb == 0`）、`PKHTB<c> <Rd>,<Rn>,<Rm>{,ASR #<imm>}`（`tb == 1`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | tb | T | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
PKHBT{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm> {, LSL #<imm>}
PKHTB{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm> {, ASR #<imm>}
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：可选地移位并用作第二个操作数的寄存器。
* `<imm>`：施加于从 `<Rm>` 读出的值的移位，编码在 `imm3:imm2` 中。

对 `PKHBT`，取值是：

* 省略：不移位，编码为 `0b00000`。
* 1-31：左移指定位数，编码为二进制数。

对 `PKHTB`，取值是：

* 省略：该指令是伪指令，汇编时如同写的是 `PKHBT{<c>}{<q>} <Rd>,<Rm>,<Rn>`。
* 1-32：算术右移指定位数。移 32 位编码为 `0b00000`。其他移位量编码为二进制数。

**注意：** 汇编器可以允许 `<imm> = 0` 表示与省略移位相同的含义，但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = Shift(R[m], shift_t, shift_n, APSR.C);  // APSR.C ignored
    R[d]<15:0>  = if tbform then operand2<15:0> else R[n]<15:0>;
    R[d]<31:16> = if tbform then R[n]<31:16>    else operand2<31:16>;
```

**异常**：无。

### 7.94. PLD (immediate)：立即数预加载数据

预加载数据（Preload Data）向存储器系统指示：来自指定地址的数据存储器访问很可能在不久的将来发生。存储器系统可以作出响应，采取措施以加快这些访问真正发生时的速度，例如把包含指定地址的缓存行预加载到数据缓存中。更多信息参见第 A3-99 页的「预加载缓存」与第 A7-185 页的「存储器提示」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE PLD (literal);
n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);  add = TRUE;

if Rn == '1111' then SEE PLD (literal);
n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);  add = FALSE;
```

**编码 T1**（Armv7-M）：`PLD<c> [<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T2**（Armv7-M）：`PLD<c> [<Rn>,#-<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
PLD<c><q>
  [<Rn> {, #+/-<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。关于 `PLD` 指令中 PC 的用法，参见第 A7-314 页的「PLD (literal)」。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：用于形成地址的立即数偏移。该偏移可以省略，表示偏移 0。取值是：
  * 编码 T1：0-4095 范围内的任意值。
  * 编码 T2：0-255 范围内的任意值。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = if add then (R[n] + imm32) else (R[n] - imm32);
    Hint_PreloadData(address);
```

**异常**：无。

### 7.95. PLD (literal)：文字预加载数据

预加载数据（Preload Data）向存储器系统指示：来自指定地址的数据存储器访问很可能在不久的将来发生。存储器系统可以作出响应，采取措施以加快这些访问真正发生时的速度，例如把包含指定地址的缓存行预加载到数据缓存中。更多信息参见第 A3-99 页的「预加载缓存」与第 A7-185 页的「存储器提示」。

**编码专用伪代码**

```arm
imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
```

**编码 T1**（Armv7-M）：`PLD<c> <label>`（普通形式）、`PLD<c><q> [PC, #+/-<imm>]`（替代形式）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | U | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
PLD<c><q>
  <label>
PLD<c><q>
  [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<label>`：很可能在不久的将来被访问的文字数据项的标签。汇编器计算从该指令的 PC 值到该标签所需的偏移值。该偏移必须在 -4095 到 4095 范围内。
  * 如果偏移为零或正数，`imm32` 等于该偏移且 `add == TRUE`。
  * 如果偏移为负数，`imm32` 等于该偏移的相反数且 `add == FALSE`。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：用于形成地址的立即数偏移。取值在 0-4095 范围内。

替代语法允许分别指定偏移的加与减以及立即数偏移，包括允许指定无法用普通语法表达的减去 0。更多信息参见第 A4-104 页的「在 UAL 指令语法中使用标签」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = if add then (Align(PC,4) + imm32) else (Align(PC,4) - imm32);
    Hint_PreloadData(address);
```

**异常**：无。

### 7.96. PLD (register)：寄存器预加载数据

预加载数据（Preload Data）是存储器提示指令，可以向存储器系统指示：来自指定地址的数据存储器访问很可能在不久的将来发生。存储器系统可以作出响应，采取措施以加快这些访问真正发生时的速度，例如把包含指定地址的缓存行预加载到数据缓存中。更多信息参见第 A3-99 页的「预加载缓存」与第 A7-185 页的「存储器提示」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE PLD (literal);
n = UInt(Rn);  m = UInt(Rm);  add = TRUE;
(shift_t, shift_n) = (SRType_LSL, UInt(shift));
if m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`PLD<c> [<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
PLD<c><q>
  [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<Rm>`：可选移位的偏移寄存器。
* `<shift>`：施加于从 `<Rm>` 读出的值的移位，范围为 0-3。如果省略该选项，假定移位 0。`<shift>` 编码在 `<imm2>` 中。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    address = if add then (R[n] + offset) else (R[n] - offset);
    Hint_PreloadData(address);
```

**异常**：无。

### 7.97. PLI (immediate, literal)：立即数与文字预加载指令

预加载指令（Preload Instruction）是存储器提示指令，可以向存储器系统指示：来自指定地址的指令存储器访问很可能在不久的将来发生。存储器系统可以作出响应，采取措施以加快这些访问真正发生时的速度，例如把包含指定地址的缓存行预加载到指令缓存中。更多信息参见第 A3-99 页的「预加载缓存」与第 A7-185 页的「存储器提示」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE encoding T3;
n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);  add = TRUE;

if Rn == '1111' then SEE encoding T3;
n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);  add = FALSE;

n = 15;  imm32 = ZeroExtend(imm12, 32);  add = (U == '1');
```

**编码 T1**（Armv7）：`PLI<c> [<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T2**（Armv7）：`PLI<c> [<Rn>,#-<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7）：`PLI<c> <label>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | U | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
PLI<c><q>
  [<Rn>, #+/-<imm>]
PLI<c><q>
  [PC, #+/-<imm>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：指定相对基址寄存器的偏移。该值必须在下列范围内：
  * 如果基址寄存器是 PC，则为 -4095-4095。
  * 否则为 -255-4095。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    base = if n == 15 then Align(PC,4) else R[n];
    address = if add then (base + imm32) else (base - imm32);
    Hint_PreloadInstr(address);
```

**异常**：无。

### 7.98. PLI (register)：寄存器预加载指令

预加载指令（Preload Instruction）是存储器提示指令，可以向存储器系统指示：来自指定地址的指令存储器访问很可能在不久的将来发生。存储器系统可以作出响应，采取措施以加快这些访问真正发生时的速度，例如把包含指定地址的缓存行预加载到指令缓存中。更多信息参见第 A3-99 页的「预加载缓存」与第 A7-185 页的「存储器提示」。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE PLI (immediate, literal);
n = UInt(Rn);  m = UInt(Rm);  add = TRUE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7）：`PLI<c> [<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
PLI<c><q>
  [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<Rm>`：可选移位的偏移寄存器。
* `<shift>`：施加于从 `<Rm>` 读出的值的移位，范围为 0-3。如果省略该选项，假定移位 0。`<shift>` 编码在 `<imm2>` 中。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    address = if add then (R[n] + offset) else (R[n] - offset);
    Hint_PreloadInstr(address);
```

**异常**：无。

### 7.99. POP：弹出多个寄存器

弹出多个寄存器（Pop Multiple Registers）从堆栈加载通用寄存器 R0-R12 的一个子集（也可能是全部）以及 PC 或 LR。

如果被加载的寄存器包含 PC，则加载到 PC 的字被视作分支地址或异常返回值。位[0] 遵循 Arm 架构关于分支到 Thumb 状态执行的互操作规则，必须为 1。如果位[0] 为 0，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
registers = P:'0000000':register_list;   UnalignedAllowed = FALSE;
if BitCount(registers) < 1 then UNPREDICTABLE;
if registers<15> == '1' && InITBlock() && !LastInITBlock() then UNPREDICTABLE;

registers = P:M:'0':register_list;  UnalignedAllowed = FALSE;
if BitCount(registers) < 2 || (P == '1' && M == '1') then UNPREDICTABLE;
if registers<15> == '1' && InITBlock() && !LastInITBlock() then UNPREDICTABLE;

t = UInt(Rt);  registers = Zeros(16);  registers<t> = '1';  UnalignedAllowed = TRUE;
if t == 13 || (t == 15 && InITBlock() && !LastInITBlock()) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`POP<c> <registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 1 | 0 | P | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T2**（Armv7-M）：`POP<c>.W <registers>`（`<registers>` 含多个寄存器）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 |
| [31:16] | P | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T3**（Armv7-M）：`POP<c>.W <registers>`（`<registers>` 只含一个寄存器 `<Rt>`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

**汇编语法**

```arm
POP<c><q>
  <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<registers>`：由一个或多个寄存器组成的列表，寄存器之间用逗号分隔并用 `{` 与 `}` 包围。它指定要加载的寄存器集合。寄存器按顺序加载：编号最低的寄存器从最低的存储器地址加载，直到编号最高的寄存器从最高的存储器地址加载。如果寄存器列表中指定了 PC，则该指令分支到加载进 PC 的地址（数据）。

  如果列表包含不止一个寄存器，该指令汇编为编码 T1 或 T2。如果列表恰好包含一个寄存器，该指令汇编为编码 T1 或 T3。

  SP 不能在列表中。

  如果列表中有 PC，则列表中不得有 LR。

**等效 LDM 语法**

```arm
LDMIA<c><q>
  SP!, <registers>
```

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = SP;
    SP = SP + 4*BitCount(registers);
    for i = 0 to 14
        if registers<i> == '1' then
            R[i] = MemA[address,4];  address = address + 4;
    if registers<15> == '1' then
        LoadWritePC(MemA[address,4]);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.100. PSSBB：物理推测旁路屏障

物理推测旁路屏障（Physical Speculative Bypass Barrier）是一种存储器屏障，它阻止推测性加载绕过对同一物理地址的更早存储。物理推测旁路屏障的语义是：

* 当对某位置的加载在程序顺序上出现在 `PSSBB` 之后时，该加载不会推测性地读取该位置一致性顺序中早于满足下列全部条件的最新存储所生成的条目的条目：
  * 该存储与加载访问同一位置。
  * 该存储在程序顺序上出现在 `PSSBB` 之前。
* 当对某位置的加载在程序顺序上出现在 `PSSBB` 之前时，该加载不会推测性地从任何满足下列全部条件的存储读取数据：
  * 该存储与加载访问同一位置。
  * 该存储在程序顺序上出现在 `PSSBB` 之后。

**编码专用伪代码**

```arm
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`PSSBB{<q>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

**汇编语法**

```arm
PSSBB{<q>}
```

where：

* `<q>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    SpecualtiveSynchronizationBarrierToPA();
```

**异常**：无。

### 7.101. PUSH：压入多个寄存器

压入多个寄存器（Push Multiple Registers）把通用寄存器 R0-R12 的一个子集（也可能是全部）以及 LR 存储到堆栈。

**编码专用伪代码**

```arm
registers = '0':M:'000000':register_list;  UnalignedAllowed = FALSE;
if BitCount(registers) < 1 then UNPREDICTABLE;

registers = '0':M:'0':register_list;  UnalignedAllowed = FALSE;
if BitCount(registers) < 2 then UNPREDICTABLE;

t = UInt(Rt);  registers = Zeros(16);  registers<t> = '1';  UnalignedAllowed = TRUE;
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`PUSH<c> <registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 1 | 0 | M | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T2**（Armv7-M）：`PUSH<c>.W <registers>`（`<registers>` 含多个寄存器）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| [31:16] | (0) | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T3**（Armv7-M）：`PUSH<c>.W <registers>`（`<registers>` 只含一个寄存器 `<Rt>`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

**汇编语法**

```arm
PUSH<c><q>
  <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<registers>`：由一个或多个寄存器组成的列表，寄存器之间用逗号分隔并用 `{` 与 `}` 包围。它指定要存储的寄存器集合。寄存器按顺序存储：编号最低的寄存器存到最低的存储器地址，直到编号最高的寄存器存到最高的存储器地址。

  如果列表包含不止一个寄存器，该指令汇编为编码 T1 或 T2。如果列表恰好包含一个寄存器，该指令汇编为编码 T1 或 T3。

  SP 与 PC 不能在列表中。

**等效 STM 语法**

```arm
STMDB<c><q>
  SP!, <registers>
```

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = SP - 4*BitCount(registers);
    for i = 0 to 14
        if registers<i> == '1' then
            MemA[address,4] = R[i];
            address = address + 4;
    SP = SP - 4*BitCount(registers);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.102. QADD：饱和加

饱和加（Saturating Add）把两个寄存器值相加，把结果饱和到 32 位有符号整数范围 –2^31 ≤ x ≤ 2^31 – 1，并把结果写入目的寄存器。如果发生饱和，它置位 APSR 中的 Q 标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QADD<c> <Rd>,<Rm>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QADD{<c>}{<q>}
  {<Rd>,} <Rm>, <Rn>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：第一个操作数寄存器。
* `<Rn>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (R[d], sat) = SignedSatQ(SInt(R[m]) + SInt(R[n]), 32);
    if sat then
        APSR.Q = '1';
```

**异常**：无。

### 7.103. QADD16：16 位饱和加

16 位饱和加（Saturating Add 16）执行两个 16 位整数加法，把结果饱和到 16 位有符号整数范围 –2^15 ≤ x ≤ 2^15 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QADD16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<15:0>) + SInt(R[m]<15:0>);
    sum2 = SInt(R[n]<31:16>) + SInt(R[m]<31:16>);
    R[d]<15:0>  = SignedSat(sum1, 16);
    R[d]<31:16> = SignedSat(sum2, 16);
```

**异常**：无。

### 7.104. QADD8：8 位饱和加

8 位饱和加（Saturating Add 8）执行四个 8 位整数加法，把结果饱和到 8 位有符号整数范围 –2^7 ≤ x ≤ 2^7 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QADD8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<7:0>) + SInt(R[m]<7:0>);
    sum2 = SInt(R[n]<15:8>) + SInt(R[m]<15:8>);
    sum3 = SInt(R[n]<23:16>) + SInt(R[m]<23:16>);
    sum4 = SInt(R[n]<31:24>) + SInt(R[m]<31:24>);
    R[d]<7:0>   = SignedSat(sum1, 8);
    R[d]<15:8>  = SignedSat(sum2, 8);
    R[d]<23:16> = SignedSat(sum3, 8);
    R[d]<31:24> = SignedSat(sum4, 8);
```

**异常**：无。

### 7.105. QASX：交换操作数的饱和加与减

交换操作数的饱和加与减（Saturating Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个 16 位整数加法与一个 16 位减法，把结果饱和到 16 位有符号整数范围 –2^15 ≤ x ≤ 2^15 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QASX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `QADDSUBX<c>` 等价于 `QASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = SInt(R[n]<15:0>) - SInt(R[m]<31:16>);
    sum  = SInt(R[n]<31:16>) + SInt(R[m]<15:0>);
    R[d]<15:0>  = SignedSat(diff, 16);
    R[d]<31:16> = SignedSat(sum, 16);
```

**异常**：无。

### 7.106. QDADD：饱和双倍加

饱和双倍加（Saturating Double and Add）把一个寄存器的双倍值加到另一个寄存器值上，并把结果写入目的寄存器。双倍运算与加法运算的结果都饱和到 32 位有符号整数范围 –2^31 ≤ x ≤ 2^31 – 1。如果任一运算发生饱和，它置位 APSR 中的 Q 标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QDADD<c> <Rd>,<Rm>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QDADD{<c>}{<q>}
  {<Rd>,} <Rm>, <Rn>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：第一个操作数寄存器。
* `<Rn>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (doubled, sat1) = SignedSatQ(2 * SInt(R[n]), 32);
    (R[d], sat2)  = SignedSatQ(SInt(R[m]) + SInt(doubled), 32);
    if sat1 || sat2 then
        APSR.Q = '1';
```

**异常**：无。

### 7.107. QDSUB：饱和双倍减

饱和双倍减（Saturating Double and Subtract）从另一个寄存器值中减去一个寄存器的双倍值，并把结果写入目的寄存器。双倍运算与减法运算的结果都饱和到 32 位有符号整数范围 –2^31 ≤ x ≤ 2^31 – 1。如果任一运算发生饱和，它置位 APSR 中的 Q 标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QDSUB<c> <Rd>,<Rm>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QDSUB{<c>}{<q>}
  {<Rd>,} <Rm>, <Rn>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：第一个操作数寄存器。
* `<Rn>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (doubled, sat1) = SignedSatQ(2 * SInt(R[n]), 32);
    (R[d], sat2)  = SignedSatQ(SInt(R[m]) - SInt(doubled), 32);
    if sat1 || sat2 then
        APSR.Q = '1';
```

**异常**：无。

### 7.108. QSAX：交换操作数的饱和减与加

交换操作数的饱和减与加（Saturating Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一个 16 位整数减法与一个 16 位加法，把结果饱和到 16 位有符号整数范围 –2^15 ≤ x ≤ 2^15 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QSAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QSAX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `QSUBADDX<c>` 等价于 `QSAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = SInt(R[n]<15:0>) + SInt(R[m]<31:16>);
    diff = SInt(R[n]<31:16>) - SInt(R[m]<15:0>);
    R[d]<15:0>  = SignedSat(sum, 16);
    R[d]<31:16> = SignedSat(diff, 16);
```

**异常**：无。

### 7.109. QSUB：饱和减

饱和减（Saturating Subtract）从一个寄存器值中减去另一个寄存器值，把结果饱和到 32 位有符号整数范围 –2^31 ≤ x ≤ 2^31 – 1，并把结果写入目的寄存器。如果发生饱和，它置位 APSR 中的 Q 标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QSUB<c> <Rd>,<Rm>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QSUB{<c>}{<q>}
  {<Rd>,} <Rm>, <Rn>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：第一个操作数寄存器。
* `<Rn>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (R[d], sat) = SignedSatQ(SInt(R[m]) - SInt(R[n]), 32);
    if sat then
        APSR.Q = '1';
```

**异常**：无。

### 7.110. QSUB16：16 位饱和减

16 位饱和减（Saturating Subtract 16）执行两个 16 位整数减法，把结果饱和到 16 位有符号整数范围 –2^15 ≤ x ≤ 2^15 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QSUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QSUB16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<15:0>) - SInt(R[m]<15:0>);
    diff2 = SInt(R[n]<31:16>) - SInt(R[m]<31:16>);
    R[d]<15:0>  = SignedSat(diff1, 16);
    R[d]<31:16> = SignedSat(diff2, 16);
```

**异常**：无。

### 7.111. QSUB8：8 位饱和减

8 位饱和减（Saturating Subtract 8）执行四个 8 位整数减法，把结果饱和到 8 位有符号整数范围 –2^7 ≤ x ≤ 2^7 – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`QSUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
QSUB8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<7:0>) - SInt(R[m]<7:0>);
    diff2 = SInt(R[n]<15:8>) - SInt(R[m]<15:8>);
    diff3 = SInt(R[n]<23:16>) - SInt(R[m]<23:16>);
    diff4 = SInt(R[n]<31:24>) - SInt(R[m]<31:24>);
    R[d]<7:0>   = SignedSat(diff1, 8);
    R[d]<15:8>  = SignedSat(diff2, 8);
    R[d]<23:16> = SignedSat(diff3, 8);
    R[d]<31:24> = SignedSat(diff4, 8);
```

**异常**：无。

### 7.112. RBIT：位反转

位反转（Reverse Bits）反转 32 位寄存器中的位序。

**编码专用伪代码**

```arm
if !Consistent(Rm) then UNPREDICTABLE;
d = UInt(Rd);  m = UInt(Rm);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`RBIT<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
RBIT<c><q>
  <Rd>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。其编号必须在编码 T1 中编码两次，分别位于 `Rm` 与 `Rm2` 字段。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    bits(32) result;
    for i = 0 to 31
        result<31-i> = R[m]<i>;
    R[d] = result;
```

**异常**：无。

### 7.113. REV：字节反转字

字节反转字（Byte-Reverse Word）反转 32 位寄存器中的字节顺序。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);
if !Consistent(Rm) then UNPREDICTABLE;

d = UInt(Rd);  m = UInt(Rm);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`REV<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`REV<c>.W <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
REV<c><q>
  <Rd>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。其编号必须在编码 T2 中编码两次，分别位于 `Rm` 与 `Rm2` 字段。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    bits(32) result;
    result<31:24> = R[m]<7:0>;
    result<23:16> = R[m]<15:8>;
    result<15:8>  = R[m]<23:16>;
    result<7:0>   = R[m]<31:24>;
    R[d] = result;
```

**异常**：无。

### 7.114. REV16：反转打包半字的字节

反转打包半字的字节（Byte-Reverse Packed Halfword）反转 32 位寄存器中每个 16 位半字的字节顺序。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);
if !Consistent(Rm) then UNPREDICTABLE;

d = UInt(Rd);  m = UInt(Rm);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`REV16<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`REV16<c>.W <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
REV16<c><q>
  <Rd>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。其编号必须在编码 T2 中编码两次，分别位于 `Rm` 与 `Rm2` 字段。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    bits(32) result;
    result<31:24> = R[m]<23:16>;
    result<23:16> = R[m]<31:24>;
    result<15:8>  = R[m]<7:0>;
    result<7:0>   = R[m]<15:8>;
    R[d] = result;
```

**异常**：无。

### 7.115. REVSH：反转有符号半字的字节

反转有符号半字的字节（Byte-Reverse Signed Halfword）反转 32 位寄存器低 16 位半字的字节顺序，并把结果符号扩展为 32 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);
if !Consistent(Rm) then UNPREDICTABLE;

d = UInt(Rd);  m = UInt(Rm);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`REVSH<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`REVSH<c>.W <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rm |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
REVSH<c><q>
  <Rd>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。其编号必须在编码 T2 中编码两次，分别位于 `Rm` 与 `Rm2` 字段。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    bits(32) result;
    result<31:8>  = SignExtend(R[m]<7:0>, 24);
    result<7:0>   = R[m]<15:8>;
    R[d] = result;
```

**异常**：无。

### 7.116. ROR (immediate)：立即数循环右移

立即数循环右移（Rotate Right (immediate)）给出寄存器内容按常量值循环右移后的值。从右端移出的位被插入到左侧空出的位。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
if (imm3:imm2) == '00000' then SEE RRX;
d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(-, shift_n) = DecodeImmShift('11', imm3:imm2);
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`ROR{S}<c> <Rd>,<Rm>,#<imm5>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ROR{S}<c><q>
  <Rd>, <Rm>, #<imm5>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含第一个操作数的寄存器。
* `<imm5>`：指定移位量，取值范围为 1-31。参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry) = Shift_C(R[m], SRType_ROR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.117. ROR (register)：寄存器循环右移

寄存器循环右移（Rotate Right (register)）给出寄存器内容按可变位数循环右移后的值。从右端移出的位被插入到左侧空出的位。该可变位数取自另一个寄存器的低字节。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();

d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`RORS <Rdn>,<Rm>`（IT 块外）、`ROR<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`ROR{S}<c>.W <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
ROR{S}<c><q>
  <Rd>, <Rn>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定其低字节包含循环移位量的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shift_n = UInt(R[m]<7:0>);
    (result, carry) = Shift_C(R[n], SRType_ROR, shift_n, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.118. RRX：带扩展循环右移

带扩展循环右移（Rotate Right with Extend）给出寄存器内容右移一位、并把进位标志移入位[31] 后的值。

`RRX` 可以选择根据结果更新条件标志。在这种情况下，位[0] 被移入进位标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`RRX{S}<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | S | 1 | 1 | 1 | 1 |
| [31:16] | (0) | 0 | 0 | 0 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
RRX{S}<c><q>
  <Rd>, <Rm>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rm>`：指定包含操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry) = Shift_C(R[m], SRType_RRX, 1, APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        // APSR.V unchanged
```

**异常**：无。

### 7.119. RSB (immediate)：立即数反向减

立即数反向减（Reverse Subtract (immediate)）从一个立即数值中减去一个寄存器值，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = !InITBlock();  imm32 = Zeros(32); // immediate = #0

d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`RSBS <Rd>,<Rn>,#0`（IT 块外）、`RSB<c> <Rd>,<Rn>,#0`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`RSB{S}<c>.W <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 1 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
RSB{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<const>`：指定加到从 `<Rn>` 得到的值上的立即数值。编码 T1 只允许取值 0。编码 T2 的允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `RSB<c>S` 等价于 `RSBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(NOT(R[n]), imm32, '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.120. RSB (register)：寄存器反向减

寄存器反向减（Reverse Subtract (register)）从一个可选移位的寄存器值中减去一个寄存器值，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`RSB{S}<c> <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
RSB{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选地移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读出的值的移位。如果省略 `<shift>`，不施加移位。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `RSB<c>S` 等价于 `RSBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(NOT(R[n]), shifted, '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.121. SADD16：有符号 16 位加

有符号 16 位加（Signed Add 16）执行两个 16 位有符号整数加法，并把结果写入目的寄存器。它根据加法的结果置位 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SADD16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<15:0>) + SInt(R[m]<15:0>);
    sum2 = SInt(R[n]<31:16>) + SInt(R[m]<31:16>);
    R[d]<15:0>  = sum1<15:0>;
    R[d]<31:16> = sum2<15:0>;
    APSR.GE<1:0> = if sum1 >= 0 then '11' else '00';
    APSR.GE<3:2> = if sum2 >= 0 then '11' else '00';
```

**异常**：无。

### 7.122. SADD8：有符号 8 位加

有符号 8 位加（Signed Add 8）执行四个 8 位有符号整数加法，并把结果写入目的寄存器。它根据加法的结果置位 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SADD8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<7:0>) + SInt(R[m]<7:0>);
    sum2 = SInt(R[n]<15:8>) + SInt(R[m]<15:8>);
    sum3 = SInt(R[n]<23:16>) + SInt(R[m]<23:16>);
    sum4 = SInt(R[n]<31:24>) + SInt(R[m]<31:24>);
    R[d]<7:0>   = sum1<7:0>;
    R[d]<15:8>  = sum2<7:0>;
    R[d]<23:16> = sum3<7:0>;
    R[d]<31:24> = sum4<7:0>;
    APSR.GE<0>  = if sum1 >= 0 then '1' else '0';
    APSR.GE<1>  = if sum2 >= 0 then '1' else '0';
    APSR.GE<2>  = if sum3 >= 0 then '1' else '0';
    APSR.GE<3>  = if sum4 >= 0 then '1' else '0';
```

**异常**：无。

### 7.123. SASX：交换操作数的有符号加与减

交换操作数的有符号加与减（Signed Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个 16 位整数加法与一个 16 位减法，并把结果写入目的寄存器。它根据结果置位 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SASX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `SADDSUBX<c>` 等价于 `SASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = SInt(R[n]<15:0>) - SInt(R[m]<31:16>);
    sum  = SInt(R[n]<31:16>) + SInt(R[m]<15:0>);
    R[d]<15:0>  = diff<15:0>;
    R[d]<31:16> = sum<15:0>;
    APSR.GE<1:0> = if diff >= 0 then '11' else '00';
    APSR.GE<3:2> = if sum  >= 0 then '11' else '00';
```

**异常**：无。

### 7.124. SBC (immediate)：立即数带进位减

立即数带进位减（Subtract with Carry (immediate)）从一个寄存器值中减去一个立即数值与 NOT(进位标志) 的值，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SBC{S}<c> <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
SBC{S}<c><q>
  {<Rd>,} <Rn>, #<const>
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<const>`：指定加到从 `<Rn>` 得到的值上的立即数值。允许值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

pre-UAL 语法 `SBC<c>S` 等价于 `SBCS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], NOT(imm32), APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.125. SBC (register)：寄存器带进位减

寄存器带进位减（Subtract with Carry (register)）从一个寄存器值中减去一个可选移位的寄存器值与 NOT(进位标志) 的值，并把结果写入目的寄存器。它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rdn);  n = UInt(Rdn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`SBCS <Rdn>,<Rm>`（IT 块外）、`SBC<c> <Rdn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rdn | Rdn | Rdn |

**编码 T2**（Armv7-M）：`SBC{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SBC{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定可选地移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读出的值的移位。如果省略 `<shift>`，不施加移位且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `SBC<c>S` 等价于 `SBCS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], NOT(shifted), APSR.C);
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.126. SBFX：有符号位段提取

有符号位段提取（Signed Bit Field Extract）从某个寄存器中提取任意位置的任意数量相邻位，把它们符号扩展为 32 位，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);
lsbit = UInt(imm3:imm2);  widthminus1 = UInt(widthm1);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SBFX<c> <Rd>,<Rn>,#<lsb>,#<width>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | widthm1 | widthm1 | widthm1 | widthm1 | widthm1 |

**汇编语法**

```arm
SBFX<c><q>
  <Rd>, <Rn>, #<lsb>, #<width>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<lsb>`：位段中最低有效位的位编号，范围为 0-31。这决定 `lsbit` 所需的取值。
* `<width>`：位段的宽度，范围为 1-32-`<lsb>`。`widthminus1` 所需的取值为 `<width>`-1。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    msbit = lsbit + widthminus1;
    if msbit <= 31 then
        R[d] = SignExtend(R[n]<msbit:lsbit>, 32);
    else
        UNPREDICTABLE;
```

**异常**：无。

### 7.127. SDIV：有符号除法

有符号除法（Signed Divide）用一个 32 位有符号整数寄存器值除以另一个 32 位有符号整数寄存器值，并把结果写入目的寄存器。条件标志不受影响。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SDIV<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (1) | (1) | (1) | (1) | Rd | Rd | Rd | Rd | 1 | 1 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SDIV<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含被除数的寄存器。
* `<Rm>`：指定包含除数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if SInt(R[m]) == 0 then
        if IntegerZeroDivideTrappingEnabled() then
            GenerateIntegerZeroDivide();
        else
            result = 0;
    else
        result = RoundTowardsZero(SInt(R[n]) / SInt(R[m]));
    R[d] = result<31:0>;
```

**异常**：UsageFault。

**注意：溢出**

如果执行的是有符号整数除法 0x80000000 / 0xFFFFFFFF，伪代码会产生中间整数结果 +2^31，这超出了 32 位有符号整数范围。不产生任何该溢出情况的指示，而写入 R[d] 的 32 位结果要求是 +2^31 的二进制表示的低 32 位。因此该除法的结果是 0x80000000。

### 7.128. SEL：按字节选择

按字节选择（Select Bytes）根据 GE 标志的取值，从第一个操作数或第二个操作数中选择结果的每个字节。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SEL<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SEL{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    R[d]<7:0>   = if APSR.GE<0> == '1' then R[n]<7:0>   else R[m]<7:0>;
    R[d]<15:8>  = if APSR.GE<1> == '1' then R[n]<15:8>  else R[m]<15:8>;
    R[d]<23:16> = if APSR.GE<2> == '1' then R[n]<23:16> else R[m]<23:16>;
    R[d]<31:24> = if APSR.GE<3> == '1' then R[n]<31:24> else R[m]<31:24>;
```

**异常**：无。

### 7.129. SEV：发送事件

发送事件（Send Event）是提示指令。它向多处理器系统中的所有 CPU 发出事件信号。更多细节参见第 B1-560 页的「等待事件与发送事件」。

这是 NOP 兼容提示，参见第 A7-185 页的「NOP 兼容提示」。

**编码专用伪代码**

```arm
// No additional decoding required

// No additional decoding required
```

**编码 T1**（Armv6-M、Armv7-M）：`SEV<c>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

**编码 T2**（Armv7-M）：`SEV<c>.W`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

**汇编语法**

```arm
SEV<c><q>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    Hint_SendEvent();
```

**异常**：无。

### 7.130. SHADD16：有符号 16 位折半加

有符号 16 位折半加（Signed Halving Add 16）执行两个 16 位有符号整数加法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHADD16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<15:0>) + SInt(R[m]<15:0>);
    sum2 = SInt(R[n]<31:16>) + SInt(R[m]<31:16>);
    R[d]<15:0>  = sum1<16:1>;
    R[d]<31:16> = sum2<16:1>;
```

**异常**：无。

### 7.131. SHADD8：有符号 8 位折半加

有符号 8 位折半加（Signed Halving Add 8）执行四个 8 位有符号整数加法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHADD8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = SInt(R[n]<7:0>) + SInt(R[m]<7:0>);
    sum2 = SInt(R[n]<15:8>) + SInt(R[m]<15:8>);
    sum3 = SInt(R[n]<23:16>) + SInt(R[m]<23:16>);
    sum4 = SInt(R[n]<31:24>) + SInt(R[m]<31:24>);
    R[d]<7:0>   = sum1<8:1>;
    R[d]<15:8>  = sum2<8:1>;
    R[d]<23:16> = sum3<8:1>;
    R[d]<31:24> = sum4<8:1>;
```

**异常**：无。

### 7.132. SHASX：交换操作数的有符号折半加与减

交换操作数的有符号折半加与减（Signed Halving Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个有符号 16 位整数加法与一个有符号 16 位减法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHASX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `SHADDSUBX<c>` 等价于 `SHASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = SInt(R[n]<15:0>) - SInt(R[m]<31:16>);
    sum  = SInt(R[n]<31:16>) + SInt(R[m]<15:0>);
    R[d]<15:0>  = diff<16:1>;
    R[d]<31:16> = sum<16:1>;
```

**异常**：无。

### 7.133. SHSAX：交换操作数的有符号折半减与加

交换操作数的有符号折半减与加（Signed Halving Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一个有符号 16 位整数减法与一个有符号 16 位加法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHSAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHSAX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `SHSUBADDX<c>` 等价于 `SHSAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = SInt(R[n]<15:0>) + SInt(R[m]<31:16>);
    diff = SInt(R[n]<31:16>) - SInt(R[m]<15:0>);
    R[d]<15:0>  = sum<16:1>;
    R[d]<31:16> = diff<16:1>;
```

**异常**：无。

### 7.134. SHSUB16：有符号 16 位折半减

有符号 16 位折半减（Signed Halving Subtract 16）执行两个有符号 16 位整数减法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHSUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHSUB16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<15:0>) - SInt(R[m]<15:0>);
    diff2 = SInt(R[n]<31:16>) - SInt(R[m]<31:16>);
    R[d]<15:0>  = diff1<16:1>;
    R[d]<31:16> = diff2<16:1>;
```

**异常**：无。

### 7.135. SHSUB8：有符号 8 位折半减

有符号 8 位折半减（Signed Halving Subtract 8）执行四个有符号 8 位整数减法，把结果折半，并写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SHSUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SHSUB8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<7:0>) - SInt(R[m]<7:0>);
    diff2 = SInt(R[n]<15:8>) - SInt(R[m]<15:8>);
    diff3 = SInt(R[n]<23:16>) - SInt(R[m]<23:16>);
    diff4 = SInt(R[n]<31:24>) - SInt(R[m]<31:24>);
    R[d]<7:0>   = diff1<8:1>;
    R[d]<15:8>  = diff2<8:1>;
    R[d]<23:16> = diff3<8:1>;
    R[d]<31:24> = diff4<8:1>;
```

**异常**：无。

### 7.136. SMLABB、SMLABT、SMLATB、SMLATT：有符号半字乘加

有符号半字乘加（Signed Multiply Accumulate (halfwords)）执行有符号乘加运算。乘法作用于两个有符号 16 位量，它们分别取自各自源寄存器的低半字或高半字。这些源寄存器的另一半被忽略。32 位乘积与 32 位累加值相加，结果写入目的寄存器。

如果在累加值相加过程中发生溢出，该指令置位 APSR 中的 Q 标志。乘法过程中不可能发生溢出。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE SMULBB, SMULBT, SMULTB, SMULTT;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);
n_high = (N == '1');  m_high = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLA<x><y><c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | N | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLA<x><y>{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `<x>`：指定源寄存器 `<Rn>` 的哪一半用作第一个乘数操作数。如果 `<x>` 为 `B`，则使用 `<Rn>` 的低半字（位[15:0]）。如果 `<x>` 为 `T`，则使用 `<Rn>` 的高半字（位[31:16]）。
* `<y>`：指定源寄存器 `<Rm>` 的哪一半用作第二个乘数操作数。如果 `<y>` 为 `B`，则使用 `<Rm>` 的低半字（位[15:0]）。如果 `<y>` 为 `T`，则使用 `<Rm>` 的高半字（位[31:16]）。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：其低半字或高半字（由 `<x>` 选择）作为第一个乘数操作数的源寄存器。
* `<Rm>`：其低半字或高半字（由 `<y>` 选择）作为第二个乘数操作数的源寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = if n_high then R[n]<31:16> else R[n]<15:0>;
    operand2 = if m_high then R[m]<31:16> else R[m]<15:0>;
    result = SInt(operand1) * SInt(operand2) + SInt(R[a]);
    R[d] = result<31:0>;
    if result != SInt(result<31:0>) then  // Signed overflow
        APSR.Q = '1';
```

**异常**：无。

### 7.137. SMLAD、SMLADX：有符号双乘加

有符号双乘加（Signed Multiply Accumulate Dual）执行两次有符号 16 × 16 位乘法。它把乘积加到一个 32 位累加操作数上。

可以选择在执行运算之前交换第二个操作数的两个半字。这产生高 × 低与低 × 高的乘法。

如果累加运算溢出，该指令置位 Q 标志。乘法过程中不可能发生溢出。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE SMUAD;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);
m_swap = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLAD{X}<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLAD{X}{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `X`：如果出现 `X`（编码为 `M == 1`），乘法为低 × 高与高 × 低。如果省略 `X`（编码为 `M == 0`），乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 + product2 + SInt(R[a]);
    R[d] = result<31:0>;
    if result != SInt(result<31:0>) then  // Signed overflow
        APSR.Q = '1';
```

**异常**：无。

### 7.138. SMLAL：有符号长乘加

有符号长乘加（Signed Multiply Accumulate Long）把两个有符号 32 位值相乘得到 64 位值，并与一个 64 位值累加。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  setflags = FALSE;
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SMLAL<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLAL<c><q>
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供累加值的低 32 位，并且是结果低 32 位的目的寄存器。
* `<RdHi>`：提供累加值的高 32 位，并且是结果高 32 位的目的寄存器。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定包含第二个操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = SInt(R[n]) * SInt(R[m]) + SInt(R[dHi]:R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.139. SMLALBB、SMLALBT、SMLALTB、SMLALTT：有符号半字长乘加

有符号半字长乘加（Signed Multiply Accumulate Long (halfwords)）把两个有符号 16 位值相乘得到 32 位值，并与一个 64 位值累加。乘法作用于两个有符号 16 位量，它们分别取自各自源寄存器的低半字或高半字。这些源寄存器的另一半被忽略。32 位乘积被符号扩展，并与 64 位累加值相加。

该指令过程中可能发生溢出，但只是作为 64 位加法的结果。如果发生这种溢出，则不被检测，结果改为按模 2^64 回绕。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);
n_high = (N == '1');  m_high = (M == '1');
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLAL<x><y><c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 1 | 0 | N | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLAL<x><y>{<c>}{<q>}
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<x>`：指定源寄存器 `<Rn>` 的哪一半用作第一个乘数操作数。如果 `<x>` 为 `B`，则使用 `<Rn>` 的低半字（位[15:0]）。如果 `<x>` 为 `T`，则使用 `<Rn>` 的高半字（位[31:16]）。
* `<y>`：指定源寄存器 `<Rm>` 的哪一半用作第二个乘数操作数。如果 `<y>` 为 `B`，则使用 `<Rm>` 的低半字（位[15:0]）。如果 `<y>` 为 `T`，则使用 `<Rm>` 的高半字（位[31:16]）。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供累加值的低 32 位，并且是结果低 32 位的目的寄存器。
* `<RdHi>`：提供累加值的高 32 位，并且是结果高 32 位的目的寄存器。
* `<Rn>`：其低半字或高半字（由 `<x>` 选择）作为第一个乘数操作数的源寄存器。
* `<Rm>`：其低半字或高半字（由 `<y>` 选择）作为第二个乘数操作数的源寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = if n_high then R[n]<31:16> else R[n]<15:0>;
    operand2 = if m_high then R[m]<31:16> else R[m]<15:0>;
    result = SInt(operand1) * SInt(operand2) + SInt(R[dHi]:R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.140. SMLALD、SMLALDX：有符号双半字长乘加

有符号双半字长乘加（Signed Multiply Accumulate Long Dual）执行两次有符号 16 × 16 位乘法。它把乘积与一个 64 位累加操作数相加。

可选地，可以在执行算术运算前交换第二个操作数的半字。这样产生高 × 低与低 × 高的乘法。

该指令过程中可能发生溢出，但只是作为 64 位加法的结果。如果发生这种溢出，则不被检测，结果改为按模 2^64 回绕。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  m_swap = (M == '1');
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLALD{X}<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 1 | 1 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLALD{X}{<c>}{<q>}
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `X`：如果存在 `X`，则乘法为低 × 高与高 × 低。如果省略 `X`，则乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供累加值的低 32 位，并且是结果低 32 位的目的寄存器。
* `<RdHi>`：提供累加值的高 32 位，并且是结果高 32 位的目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 + product2 + SInt(R[dHi]:R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.141. SMLAWB、SMLAWT：有符号字乘半字加

有符号字乘半字加（Signed Multiply Accumulate (word by halfword)）执行一次有符号乘加运算。乘法作用于一个有符号 32 位量与一个有符号 16 位量。该有符号 16 位量取自其源寄存器的低半字或高半字。第二个源寄存器的另一半被忽略。48 位乘积的高 32 位与一个 32 位累加值相加，结果写入目的寄存器。48 位乘积的低 16 位被忽略。

如果在累加值相加过程中发生溢出，该指令置位 APSR 中的 Q 标志。乘法过程中不会发生溢出。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE SMULWB, SMULWT;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);  m_high = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLAW<y><c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLAW<y>{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `<y>`：指定源寄存器 `<Rm>` 的哪一半用作第二个乘数操作数。如果 `<y>` 为 `B`，则使用 `<Rm>` 的低半字（位[15:0]）。如果 `<y>` 为 `T`，则使用 `<Rm>` 的高半字（位[31:16]）。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：其低半字或高半字（由 `<y>` 选择）作为第二个乘数操作数的源寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_high then R[m]<31:16> else R[m]<15:0>;
    result = SInt(R[n]) * SInt(operand2) + (SInt(R[a]) << 16);
    R[d] = result<47:16>;
    if (result >> 16) != SInt(R[d]) then  // Signed overflow
        APSR.Q = '1';
```

**异常**：无。

### 7.142. SMLSD、SMLSDX：有符号双半字乘减

有符号双半字乘减（Signed Multiply Subtract Dual）执行两次有符号 16 × 16 位乘法。它把乘积之差与一个 32 位累加操作数相加。

可选地，可以在执行算术运算前交换第二个操作数的半字。这样产生高 × 低与低 × 高的乘法。

如果累加运算溢出，该指令置位 Q 标志。乘法或减法过程中不会发生溢出。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE SMUSD;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);  m_swap = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLSD{X}<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLSD{X}{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `X`：如果存在 `X`，则乘法为低 × 高与高 × 低。如果省略 `X`，则乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 - product2 + SInt(R[a]);
    R[d] = result<31:0>;
    if result != SInt(result<31:0>) then  // Signed overflow
        APSR.Q = '1';
```

**异常**：无。

### 7.143. SMLSLD、SMLSLDX：有符号双半字长乘减

有符号双半字长乘减（Signed Multiply Subtract Long Dual）执行两次有符号 16 × 16 位乘法。它把乘积之差与一个 64 位累加操作数相加。

可选地，可以在执行算术运算前交换第二个操作数的半字。这样产生高 × 低与低 × 高的乘法。

该指令过程中可能发生溢出，但只是作为 64 位加法的结果。如果发生这种溢出，则不被检测，结果改为按模 2^64 回绕。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  m_swap = (M == '1');
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMLSLD{X}<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 1 | 1 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMLSLD{X}{<c>}{<q>}
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `X`：如果存在 `X`，则乘法为低 × 高与高 × 低。如果省略 `X`，则乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供累加值的低 32 位，并且是结果低 32 位的目的寄存器。
* `<RdHi>`：提供累加值的高 32 位，并且是结果高 32 位的目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 - product2 + SInt(R[dHi]:R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.144. SMMLA、SMMLAR：有符号最高有效字乘加

有符号最高有效字乘加（Signed Most Significant Word Multiply Accumulate）把两个有符号 32 位值相乘，取出结果的高 32 位（最高有效字），并与一个累加值相加。

可选地，可以指定对结果取整而不是截断。此时，在取出高字之前先把常量 `0x80000000` 加到乘积上。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE SMMUL;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);  round = (R == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMMLA{R}<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | R | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMMLA{R}{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `R`：如果存在 `R`，则乘法取整。如果省略 `R`，则乘法截断。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：包含第一个乘数操作数的寄存器。
* `<Rm>`：包含第二个乘数操作数的寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = (SInt(R[a]) << 32) + SInt(R[n]) * SInt(R[m]);
    if round then result = result + 0x80000000;
    R[d] = result<63:32>;
```

**异常**：无。

### 7.145. SMMLS、SMMLSR：有符号最高有效字乘减

有符号最高有效字乘减（Signed Most Significant Word Multiply Subtract）把两个有符号 32 位值相乘，从被左移 32 位的 32 位累加值中减去该乘积，并取出该减法结果的高 32 位。

可选地，可以指定对指令结果取整而不是截断。此时，在取出高字之前先把常量 `0x80000000` 加到减法结果上。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);  round = (R == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMMLS{R}<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | R | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMMLS{R}{<c>}{<q>}
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `R`：如果存在 `R`，则乘法取整。如果省略 `R`，则乘法截断。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：包含第一个乘数操作数的寄存器。
* `<Rm>`：包含第二个乘数操作数的寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = (SInt(R[a]) << 32) - SInt(R[n]) * SInt(R[m]);
    if round then result = result + 0x80000000;
    R[d] = result<63:32>;
```

**异常**：无。

### 7.146. SMMUL、SMMULR：有符号最高有效字乘

有符号最高有效字乘（Signed Most Significant Word Multiply）把两个有符号 32 位值相乘，取出结果的高 32 位，并把这些位写入目的寄存器。

可选地，可以指定对结果取整而不是截断。此时，在取出高字之前先把常量 `0x80000000` 加到乘积上。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  round = (R == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMMUL{R}<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | R | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMMUL{R}{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `R`：如果存在 `R`，则乘法取整。如果省略 `R`，则乘法截断。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = SInt(R[n]) * SInt(R[m]);
    if round then result = result + 0x80000000;
    R[d] = result<63:32>;
```

**异常**：无。

### 7.147. SMUAD、SMUADX：有符号双乘加

有符号双乘加（Signed Dual Multiply Add）执行两次有符号 16 × 16 位乘法。它把乘积相加，并把结果写入目的寄存器。

可选地，可以在执行算术运算前交换第二个操作数的半字。这样产生高 × 低与低 × 高的乘法。

如果加法溢出，该指令置位 Q 标志。乘法本身不会溢出。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  m_swap = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMUAD{X}<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMUAD{x}{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `X`：如果存在 `X`，则乘法为低 × 高与高 × 低。如果省略 `X`，则乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 + product2;
    R[d] = result<31:0>;
    if result != SInt(result<31:0>) then  // Signed overflow
        APSR.Q = '1';
```

**异常**：无。

### 7.148. SMULBB、SMULBT、SMULTB、SMULTT：有符号半字乘

有符号半字乘（Signed Multiply (halfwords)）把两个有符号 16 位量相乘，它们分别取自各自源寄存器的低半字或高半字。这些源寄存器的另一半被忽略。32 位乘积被写入目的寄存器。该指令过程中不会发生溢出。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
n_high = (N == '1');  m_high = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMUL<x><y><c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | N | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMUL<x><y>{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<x>`：指定源寄存器 `<Rn>` 的哪一半用作第一个乘数操作数。如果 `<x>` 为 `B`，则使用 `<Rn>` 的低半字（位[15:0]）。如果 `<x>` 为 `T`，则使用 `<Rn>` 的高半字（位[31:16]）。
* `<y>`：指定源寄存器 `<Rm>` 的哪一半用作第二个乘数操作数。如果 `<y>` 为 `B`，则使用 `<Rm>` 的低半字（位[15:0]）。如果 `<y>` 为 `T`，则使用 `<Rm>` 的高半字（位[31:16]）。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：其低半字或高半字（由 `<x>` 选择）作为第一个乘数操作数的源寄存器。
* `<Rm>`：其低半字或高半字（由 `<y>` 选择）作为第二个乘数操作数的源寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand1 = if n_high then R[n]<31:16> else R[n]<15:0>;
    operand2 = if m_high then R[m]<31:16> else R[m]<15:0>;
    result = SInt(operand1) * SInt(operand2);
    R[d] = result<31:0>;
    // Signed overflow cannot occur
```

**异常**：无。

### 7.149. SMULL：有符号长乘

有符号长乘（Signed Multiply Long）把两个 32 位有符号值相乘，产生 64 位结果。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  setflags = FALSE;
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SMULL<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMULL<c><q>
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：保存结果的低 32 位。
* `<RdHi>`：保存结果的高 32 位。
* `<Rn>`：指定包含第一个操作数的寄存器。
* `<Rm>`：指定包含第二个操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = SInt(R[n]) * SInt(R[m]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.150. SMULWB、SMULWT：有符号字乘半字

有符号字乘半字（Signed Multiply (word by halfword)）把一个有符号 32 位量与一个有符号 16 位量相乘。该有符号 16 位量取自其源寄存器的低半字或高半字。第二个源寄存器的另一半被忽略。48 位乘积的高 32 位被写入目的寄存器。48 位乘积的低 16 位被忽略。该指令过程中不会发生溢出。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  m_high = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMULW<y><c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMULW<y>{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<y>`：指定源寄存器 `<Rm>` 的哪一半用作第二个乘数操作数。如果 `<y>` 为 `B`，则使用 `<Rm>` 的低半字（位[15:0]）。如果 `<y>` 为 `T`，则使用 `<Rm>` 的高半字（位[31:16]）。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：其低半字或高半字（由 `<y>` 选择）作为第二个乘数操作数的源寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_high then R[m]<31:16> else R[m]<15:0>;
    product = SInt(R[n]) * SInt(operand2);
    R[d] = product<47:16>;
    // Signed overflow cannot occur
```

**异常**：无。

### 7.151. SMUSD、SMUSDX：有符号双半字乘减

有符号双半字乘减（Signed Dual Multiply Subtract）执行两次有符号 16 × 16 位乘法。它把其中一个乘积从另一个中减去，并把结果写入目的寄存器。

可选地，可以在执行算术运算前交换第二个操作数的半字。这样产生高 × 低与低 × 高的乘法。

不会发生溢出。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  m_swap = (M == '1');
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SMUSD{X}<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | M | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SMUSD{X}{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `X`：如果存在 `X`，则乘法为低 × 高与高 × 低。如果省略 `X`，则乘法为低 × 低与高 × 高。
* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand2 = if m_swap then ROR(R[m],16) else R[m];
    product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>);
    product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>);
    result = product1 - product2;
    R[d] = result<31:0>;
    // Signed overflow cannot occur
```

**异常**：无。

### 7.152. SSAT：有符号饱和

有符号饱和（Signed Saturate）把可选移位的带符号值饱和到一个可选的带符号范围。

如果该运算发生饱和，Q 标志被置为 1。

**编码专用伪代码**

```arm
if sh == '1' && (imm3:imm2) == '00000' then
    if HaveDSPExt() then
        SEE SSAT16;
    else
        UNDEFINED;
d = UInt(Rd);  n = UInt(Rn);  saturate_to = UInt(sat_imm)+1;
(shift_t, shift_n) = DecodeImmShift(sh:'0', imm3:imm2);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SSAT<c> <Rd>,#<imm5>,<Rn>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 0 | 0 | sh | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | sat_imm | sat_imm | sat_imm | sat_imm | sat_imm |

**汇编语法**

```arm
SSAT<c><q>
  <Rd>, #<imm>, <Rn> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。
* `<imm>`：指定用于饱和的位位置，范围为 1-32。
* `<Rn>`：指定包含待饱和值的寄存器。
* `<shift>`：指定可选移位。如果省略 `<shift>`，则使用 `LSL #0`。如果存在，它必须是以下之一：
  * `LSL #N`：`N` 必须在 0-31 范围内。
  * `ASR #N`：`N` 必须在 1-31 范围内。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand = Shift(R[n], shift_t, shift_n, APSR.C);  // APSR.C ignored
    (result, sat) = SignedSatQ(SInt(operand), saturate_to);
    R[d] = SignExtend(result, 32);
    if sat then
        APSR.Q = '1';
```

**异常**：无。

### 7.153. SSAT16：有符号 16 饱和

有符号 16 饱和（Signed Saturate 16）把两个有符号 16 位值饱和到一个选定的带符号范围。

如果该运算发生饱和，Q 标志被置为 1。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  saturate_to = UInt(sat_imm)+1;
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SSAT16<c> <Rd>,#<imm>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | 0 | 0 | 0 | Rd | Rd | Rd | Rd | 0 | 0 | (0) | (0) | sat_imm | sat_imm | sat_imm | sat_imm |

**汇编语法**

```arm
SSAT16{<c>}{<q>}
  <Rd>, #<imm>, <Rn>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<imm>`：用于饱和的位位置，范围为 1-16。
* `<Rn>`：包含待饱和值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result1, sat1) = SignedSatQ(SInt(R[n]<15:0>), saturate_to);
    (result2, sat2) = SignedSatQ(SInt(R[n]<31:16>), saturate_to);
    R[d]<15:0> = SignExtend(result1, 16);
    R[d]<31:16> = SignExtend(result2, 16);
    if sat1 || sat2 then
        APSR.Q = '1';
```

**异常**：无。

### 7.154. SSAX：有符号交换加减

有符号交换加减（Signed Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一次 16 位整数减法与一次 16 位加法，并把结果写入目的寄存器。它根据结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SSAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SSAX{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `SSUBADDX<c>` 等价于 `SSAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = SInt(R[n]<15:0>) + SInt(R[m]<31:16>);
    diff = SInt(R[n]<31:16>) - SInt(R[m]<15:0>);
    R[d]<15:0>  = sum<15:0>;
    R[d]<31:16> = diff<15:0>;
    APSR.GE<1:0> = if sum  >= 0 then '11' else '00';
    APSR.GE<3:2> = if diff >= 0 then '11' else '00';
```

**异常**：无。

### 7.155. SSBB：推测存储绕过屏障

推测存储绕过屏障（Speculative Store Bypass Barrier）是一种内存屏障，它在特定条件下阻止推测性加载绕过对同一虚拟地址的更早存储。推测存储绕过屏障的语义如下：

* 当对某个位置的加载在程序顺序上位于 `SSBB` 之后时，该加载不会推测性地读取该位置一致性顺序中、早于满足以下所有条件的最新存储所生成的条目的条目：
  * 该存储与加载访问同一位置。
  * 该存储使用与加载相同的虚拟地址。
  * 该存储在程序顺序上位于 `SSBB` 之前。
* 当对某个位置的加载在程序顺序上位于 `SSBB` 之前时，该加载不会推测性地读取来自满足以下所有条件的任何存储的数据：
  * 该存储与加载访问同一位置。
  * 该存储使用与加载相同的虚拟地址。
  * 该存储在程序顺序上位于 `SSBB` 之后。

**编码专用伪代码**

```arm
if InITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SSBB<q>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | (1) | (1) | (1) | (1) |
| [31:16] | 1 | 0 | (0) | 0 | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

**汇编语法**

```arm
SSBB{<q>}
```

where：

* `<q>`：参见第 A7-177 页的「标准汇编语法字段」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    SpeculativeSynchronizationBarrierToVA();
```

**异常**：无。

### 7.156. SSUB16：有符号 16 位减

有符号 16 位减（Signed Subtract 16）执行两次 16 位有符号整数减法，并把结果写入目的寄存器。它根据减法结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SSUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SSUB16{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<15:0>) - SInt(R[m]<15:0>);
    diff2 = SInt(R[n]<31:16>) - SInt(R[m]<31:16>);
    R[d]<15:0>  = diff1<15:0>;
    R[d]<31:16> = diff2<15:0>;
    APSR.GE<1:0> = if diff1 >= 0 then '11' else '00';
    APSR.GE<3:2> = if diff2 >= 0 then '11' else '00';
```

**异常**：无。

### 7.157. SSUB8：有符号 8 位减

有符号 8 位减（Signed Subtract 8）执行四次 8 位有符号整数减法，并把结果写入目的寄存器。它根据减法结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SSUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SSUB8{<c>}{<q>}
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c>`, `<q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = SInt(R[n]<7:0>) - SInt(R[m]<7:0>);
    diff2 = SInt(R[n]<15:8>) - SInt(R[m]<15:8>);
    diff3 = SInt(R[n]<23:16>) - SInt(R[m]<23:16>);
    diff4 = SInt(R[n]<31:24>) - SInt(R[m]<31:24>);
    R[d]<7:0>   = diff1<7:0>;
    R[d]<15:8>  = diff2<7:0>;
    R[d]<23:16> = diff3<7:0>;
    R[d]<31:24> = diff4<7:0>;
    APSR.GE<0>  = if diff1 >= 0 then '1' else '0';
    APSR.GE<1>  = if diff2 >= 0 then '1' else '0';
    APSR.GE<2>  = if diff3 >= 0 then '1' else '0';
    APSR.GE<3>  = if diff4 >= 0 then '1' else '0';
```

**异常**：无。

### 7.158. STC、STC2：存储协处理器

存储协处理器（Store Coprocessor）把数据从协处理器存储到一系列连续的内存地址。

如果没有协处理器能执行该指令，则产生 UsageFault 异常。

**编码专用伪代码**

```arm
if P == '0' && U == '0' && N == '0' && W == '0' then UNDEFINED;
if P == '0' && U == '0' && N == '1' && W == '0' then SEE MCRR, MCRR2;
n = UInt(Rn);  cp = UInt(coproc);  imm32 = ZeroExtend(imm8:'00', 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if n == 15 then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STC{L}<c> <coproc>,<CRd>,[<Rn>{,#+/-<imm8>}]`（偏移：`P = 1`、`W = 0`）、`STC{L}<c> <coproc>,<CRd>,[<Rn>,#+/-<imm8>]!`（前索引：`P = 1`、`W = 1`）、`STC{L}<c> <coproc>,<CRd>,[<Rn>],#+/-<imm8>`（后索引：`P = 0`、`W = 1`）、`STC{L}<c> <coproc>,<CRd>,[<Rn>],<option>`（无索引：`P = 0`、`W = 0`、`U = 1`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 0 | P | U | N | W | 0 | Rn | Rn | Rn | Rn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`STC2{L}<c> <coproc>,<CRd>,[<Rn>{,#+/-<imm8>}]`（偏移：`P = 1`、`W = 0`）、`STC2{L}<c> <coproc>,<CRd>,[<Rn>,#+/-<imm8>]!`（前索引：`P = 1`、`W = 1`）、`STC2{L}<c> <coproc>,<CRd>,[<Rn>],#+/-<imm8>`（后索引：`P = 0`、`W = 1`）、`STC2{L}<c> <coproc>,<CRd>,[<Rn>],<option>`（无索引：`P = 0`、`W = 0`、`U = 1`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 1 | 0 | P | U | N | W | 0 | Rn | Rn | Rn | Rn |
| [31:16] | CRd | CRd | CRd | CRd | coproc | coproc | coproc | coproc | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STC{2}{L}<c><q>
  <coproc>,<CRd>,[<Rn>{,#+/-<imm>}]
STC{2}{L}<c><q>
  <coproc>,<CRd>,[<Rn>,#+/-<imm>]!
STC{2}{L}<c><q>
  <coproc>,<CRd>,[<Rn>],#+/-<imm>
STC{2}{L}<c><q>
  <coproc>,<CRd>,[<Rn>],<option>
```

where：

* `2`：如果指定，则选择编码 T2。如果省略，则选择编码 T1。
* `L`：如果指定，则选择编码的 `N == 1` 形式。如果省略，则选择 `N == 0` 形式。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<coproc>`：指定协处理器的名称。标准的通用协处理器名称为 `p0` - `p15`。
* `<CRd>`：指定协处理器源寄存器。
* `<Rn>`：指定基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许值为 0-1020 范围内 4 的倍数。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。
* `<option>`：以 `{` 与 `}` 括起的整数指定附加的指令选项，范围为 0-255。该整数编码在指令的 `imm8` 字段中。

pre-UAL 语法 `STC<c>L` 等价于 `STCL<c>`。

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
            MemA[address,4] = Coproc_GetWordToStore(cp, ThisInstr());  address = address + 4;
        until Coproc_DoneStoring(cp, ThisInstr());
        if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.159. STM、STMIA、STMEA：存储多个寄存器

存储多个寄存器（Store Multiple）使用基址寄存器中的地址，把多个寄存器存储到连续的内存位置。连续的内存位置从该地址开始，这些位置中最后一个地址之上的地址可以选择写回基址寄存器。

**编码专用伪代码**

```arm
n = UInt(Rn);  registers = '00000000':register_list;  wback = TRUE;
if BitCount(registers) < 1 then UNPREDICTABLE;

n = UInt(Rn);  registers = '0':M:'0':register_list;  wback = (W == '1');
if n == 15 || BitCount(registers) < 2 then UNPREDICTABLE;
if wback && registers<n> == '1' then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STM<c> <Rn>!,<registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**编码 T2**（Armv7-M）：`STM<c>.W <Rn>{!},<registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | W | 0 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**汇编语法**

```arm
STM<c><q>
  <Rn>{!}, <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。可以使用 SP。
* `!`：使指令把修改后的值写回 `<Rn>`。如果省略 `!`，指令不改变 `<Rn>`。
* `<registers>`：一个或多个待存储寄存器的列表，以逗号分隔并用 `{` 与 `}` 括起。编号最低的寄存器存储到最低的内存地址，依此类推到编号最高的寄存器存储到最高的内存地址。

编码 T2 不支持只含一个寄存器的列表。如果带单个寄存器 `<Rt>` 的 `STM` 指令汇编到 Thumb 且编码 T1 不可用，则汇编为等价的 `STR<c><q> <Rt>,[<Rn>]{,#4}` 指令。

SP 与 PC 不能出现在列表中。

对于基址寄存器在列表中且指定了 `!` 的指令，编码 T2 不可用，且此类指令的使用已废弃。如果基址寄存器不是列表中编号最低的寄存器，此类指令会为该基址寄存器存储一个 UNKNOWN 值。

`STMEA` 与 `STMIA` 是 `STM` 的伪指令，其中 `STMEA` 指其用于把数据压入空递增（Empty Ascending）栈的用法。

pre-UAL 语法 `STM<c>IA` 与 `STM<c>EA` 等价于 `STM<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];

    for i = 0 to 14
        if registers<i> == '1' then
            if i == n && wback && i != LowestSetBit(registers) then
                MemA[address,4] = bits(32) UNKNOWN;    // encoding T1 only
            else
                MemA[address,4] = R[i];
            address = address + 4;
    if wback then R[n] = R[n] + 4*BitCount(registers);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.160. STMDB、STMFD：先减后存储多个寄存器

先减后存储多个寄存器（Store Multiple Decrement Before）使用基址寄存器中的地址，把多个寄存器存储到连续的内存位置。连续的内存位置结束于该地址之下，这些位置中第一个的地址可以选择写回基址寄存器。

**编码专用伪代码**

```arm
if W == '1' && Rn == '1101' then SEE PUSH;
n = UInt(Rn);  registers = '0':M:'0':register_list;  wback = (W == '1');
if n == 15 || BitCount(registers) < 2 then UNPREDICTABLE;
if wback && registers<n> == '1' then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STMDB<c> <Rn>{!},<registers>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | W | 0 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | M | (0) | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list | register_list |

**汇编语法**

```arm
STMDB<c><q>
  <Rn>{!}, <registers>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。如果它是 SP 且指定了 `!`，则按第 A7-322 页的「PUSH」中所述处理该指令。
* `!`：使指令把修改后的值写回 `<Rn>`。编码为 `W = 1`。如果省略 `!`，指令不改变 `<Rn>`。编码为 `W = 0`。
* `<registers>`：一个或多个待存储寄存器的列表，以逗号分隔并用 `{` 与 `}` 括起。编号最低的寄存器存储到最低的内存地址，依此类推到编号最高的寄存器存储到最高的内存地址。

编码 T1 不支持只含一个寄存器的列表。如果带单个寄存器 `<Rt>` 的 `STMDB` 指令汇编到 Thumb，则汇编为等价的 `STR<c><q> <Rt>,[<Rn>,#-4]{!}` 指令。

SP 与 PC 不能出现在列表中。

`STMFD` 是 `STMDB` 的同义词，指其用于把数据压入满递减（Full Descending）栈的用法。

pre-UAL 语法 `STM<c>DB` 与 `STM<c>FD` 等价于 `STMDB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] - 4*BitCount(registers);

    for i = 0 to 14
        if registers<i> == '1' then
            MemA[address,4] = R[i];
            address = address + 4;
    if wback then R[n] = R[n] - 4*BitCount(registers);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.161. STR (immediate)：立即数存储寄存器

立即数存储寄存器（Store Register (immediate)）由基址寄存器值与立即数偏移计算出地址，把一个字从寄存器存储到存储器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5:'00', 32);
index = TRUE;  add = TRUE;  wback = FALSE;

t = UInt(Rt);  n = 13;  imm32 = ZeroExtend(imm8:'00', 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t == 15 then UNPREDICTABLE;
if P == '1' && U == '1' && W == '0' then SEE STRT;
if Rn == '1101' && P == '1' && U == '0' && W == '1' && imm8 == '00000100' then SEE PUSH;
if Rn == '1111' || (P == '0' && W == '0') then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t == 15 || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STR<c> <Rt>, [<Rn>{,#<imm5>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 1 | 0 | 0 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Thumb 指令集的所有版本）：`STR<c> <Rt>,[SP,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 0 | 1 | 0 | Rt | Rt | Rt | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`STR<c>.W <Rt>,[<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T4**（Armv7-M）：`STR<c> <Rt>,[<Rn>,#-<imm8>]`（偏移：`index == TRUE`、`wback == FALSE`）、`STR<c> <Rt>,[<Rn>],#+/-<imm8>`（后索引：`index == FALSE`、`wback == TRUE`）、`STR<c> <Rt>,[<Rn>,#+/-<imm8>]!`（前索引：`index == TRUE`、`wback == TRUE`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STR<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
STR<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
STR<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：指定源寄存器。该寄存器允许是 SP。
* `<Rn>`：指定基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。编码 T1 允许 0-124 范围内 4 的倍数，编码 T2 允许 0-1020 范围内 4 的倍数，编码 T3 允许 0-4095 范围内的任意值，编码 T4 允许 0-255 范围内的任意值。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    MemU[address,4] = R[t];
    if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.162. STR (register)：寄存器存储寄存器

寄存器存储寄存器（Store Register (register)）由基址寄存器值与偏移寄存器值计算出地址，把一个字从寄存器存储到存储器。偏移寄存器值可以被左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t == 15 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STR<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`STR<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
STR<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：指定源寄存器。该寄存器允许是 SP。
* `<Rn>`：指定包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含被左移并加到 `<Rn>` 值上以形成地址的偏移。
* `<shift>`：指定 `<Rm>` 值被左移的位数，范围为 0-3。如果省略该选项，则假定移位 0，且两种编码都允许。如果指定该选项，则只允许编码 T2。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    address = R[n] + offset;
    MemU[address,4] = R[t];
```

**异常**：UsageFault、MemManage、BusFault。

### 7.163. STRB (immediate)：立即数存储寄存器字节

立即数存储寄存器字节（Store Register Byte (immediate)）由基址寄存器值与立即数偏移计算出地址，把一个字节从寄存器存储到存储器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t IN {13,15} then UNPREDICTABLE;
if P == '1' && U == '1' && W == '0' then SEE STRBT;
if Rn == '1111' || (P == '0' && W == '0') then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t IN {13,15} || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STRB<c> <Rt>,[<Rn>,#<imm5>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 1 | 1 | 0 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`STRB<c>.W <Rt>,[<Rn>,#<imm12>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T3**（Armv7-M）：`STRB<c> <Rt>,[<Rn>,#-<imm8>]`（偏移：`index == TRUE`、`wback == FALSE`）、`STRB<c> <Rt>,[<Rn>],#+/-<imm8>`（后索引：`index == FALSE`、`wback == TRUE`）、`STRB<c> <Rt>,[<Rn>,#+/-<imm8>]!`（前索引：`index == TRUE`、`wback == TRUE`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRB<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
STRB<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
STRB<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：指定源寄存器。
* `<Rn>`：指定基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许值范围为：编码 T1 为 0-31，编码 T2 为 0-4095，编码 T3 为 0-255。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `STR<c>B` 等价于 `STRB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    MemU[address,1] = R[t]<7:0>;
    if wback then R[n] = offset_addr;
```

**异常**：MemManage、BusFault。

### 7.164. STRB (register)：寄存器存储寄存器字节

寄存器存储寄存器字节（Store Register Byte (register)）由基址寄存器值与偏移寄存器值计算出地址，并把一个字节从寄存器存储到存储器。偏移寄存器值可以被左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STRB<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`STRB<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
STRB<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：指定包含基值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含被左移并加到 `<Rn>` 值上以形成地址的偏移。
* `<shift>`：指定 `<Rm>` 值被左移的位数，范围为 0-3。如果省略该选项，则假定移位 0，且两种编码都允许。如果指定该选项，则只允许编码 T2。

pre-UAL 语法 `STR<c>B` 等价于 `STRB<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    address = R[n] + offset;
    MemU[address,1] = R[t]<7:0>;
```

**异常**：MemManage、BusFault。

### 7.165. STRBT：非特权存储寄存器字节

非特权存储寄存器字节（Store Register Byte Unprivileged）由基址寄存器值与立即数偏移计算出地址，并把一个字节从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。当特权软件使用 `STRBT` 指令时，其存储器访问受到限制，如同该软件是非特权的。另见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STRBT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRBT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：指定源寄存器。
* `<Rn>`：指定基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许值范围为 0-255。`<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `STR<c>BT` 等价于 `STRBT<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    MemU_unpriv[address,1] = R[t]<7:0>;
```

**异常**：MemManage、BusFault。

### 7.166. STRD (immediate)：立即数存储双寄存器

立即数存储双寄存器（Store Register Dual (immediate)）由基址寄存器值与立即数偏移计算出地址，把两个字从两个寄存器存储到存储器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
if P == '0' && W == '0' then SEE "Related encodings";
t = UInt(Rt);  t2 = UInt(Rt2);  n = UInt(Rn);  imm32 = ZeroExtend(imm8:'00', 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if wback && (n == t || n == t2) then UNPREDICTABLE;
if n == 15 || t IN {13,15} || t2 IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STRD<c> <Rt>,<Rt2>,[<Rn>{,#+/-<imm8>}]`（偏移：`index == TRUE`、`wback == FALSE`）、`STRD<c> <Rt>,<Rt2>,[<Rn>,#+/-<imm8>]!`（前索引：`index == TRUE`、`wback == TRUE`）、`STRD<c> <Rt>,<Rt2>,[<Rn>],#+/-<imm8>`（后索引：`index == FALSE`、`wback == TRUE`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | P | U | 1 | W | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | Rt2 | Rt2 | Rt2 | Rt2 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRD<c><q>
  <Rt>, <Rt2>, [<Rn> {, #+/-<imm>}]
STRD<c><q>
  <Rt>, <Rt2>, [<Rn>, #+/-<imm>]!
STRD<c><q>
  <Rt>, <Rt2>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：第一个源寄存器。
* `<Rt2>`：第二个源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。允许范围为 0-1020 范围内 4 的倍数。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `STR<c>D` 等价于 `STRD<c>`。

**相关编码**：参见第 A5-145 页的「加载/存储双字或独占、表分支」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    MemA[address,4] = R[t];
    MemA[address+4,4] = R[t2];
    if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.167. STREX：存储寄存器独占

存储寄存器独占（Store Register Exclusive）由基址寄存器值与立即数偏移计算出地址，若执行处理器对被寻址的存储器具有独占访问权，则把一个字从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
d = UInt(Rd);  t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8:'00', 32);
if d IN {13,15} || t IN {13,15} || n == 15 then UNPREDICTABLE;
if d == n || d == t then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STREX<c> <Rd>,<Rt>,[<Rn>{,#<imm8>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STREX<c><q>
  <Rd>, <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：返回状态值的目的寄存器。返回值为：
  * `0`：如果操作更新了存储器。
  * `1`：如果操作未能更新存储器。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围为 0-1020 范围内 4 的倍数。`<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    if ExclusiveMonitorsPass(address,4) then
        MemA[address,4] = R[t];
        R[d] = ZeroExtend('0', 32);
    else
        R[d] = ZeroExtend('1', 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.168. STREXB：存储寄存器独占字节

存储寄存器独占字节（Store Register Exclusive Byte）由基址寄存器值推导出地址，若执行处理器对被寻址的存储器具有独占访问权，则把一个字节从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
d = UInt(Rd);  t = UInt(Rt);  n = UInt(Rn);
if d IN {13,15} || t IN {13,15} || n == 15 then UNPREDICTABLE;
if d == n || d == t then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STREXB<c> <Rd>,<Rt>,[<Rn>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 0 | Rd | Rd | Rd | Rd |

**汇编语法**

```arm
STREXB<c><q>
  <Rd>, <Rt>, [<Rn>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：返回状态值的目的寄存器。返回值为：
  * `0`：如果操作更新了存储器。
  * `1`：如果操作未能更新存储器。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];
    if ExclusiveMonitorsPass(address,1) then
        MemA[address,1] = R[t]<7:0>;
        R[d] = ZeroExtend('0', 32);
    else
        R[d] = ZeroExtend('1', 32);
```

**异常**：MemManage、BusFault。

### 7.169. STREXH：存储寄存器独占半字

存储寄存器独占半字（Store Register Exclusive Halfword）由基址寄存器值推导出地址，若执行处理器对被寻址的存储器具有独占访问权，则把一个半字从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
d = UInt(Rd);  t = UInt(Rt);  n = UInt(Rn);
if d IN {13,15} || t IN {13,15} || n == 15 then UNPREDICTABLE;
if d == n || d == t then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STREXH<c> <Rd>,<Rt>,[<Rn>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | (1) | (1) | (1) | (1) | 0 | 1 | 0 | 1 | Rd | Rd | Rd | Rd |

**汇编语法**

```arm
STREXH<c><q>
  <Rd>, <Rt>, [<Rn>]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：返回状态值的目的寄存器。返回值为：
  * `0`：如果操作更新了存储器。
  * `1`：如果操作未能更新存储器。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n];
    if ExclusiveMonitorsPass(address,2) then
        MemA[address,2] = R[t]<15:0>;
        R[d] = ZeroExtend('0', 32);
    else
        R[d] = ZeroExtend('1', 32);
```

**异常**：UsageFault、MemManage、BusFault。

### 7.170. STRH (immediate)：立即数存储寄存器半字

立即数存储寄存器半字（Store Register Halfword (immediate)）由基址寄存器值与立即数偏移计算出地址，把一个半字从寄存器存储到存储器。它可以使用偏移、后索引或前索引寻址。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm5:'0', 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm12, 32);
index = TRUE;  add = TRUE;  wback = FALSE;
if t IN {13,15} then UNPREDICTABLE;

if P == '1' && U == '1' && W == '0' then SEE STRHT;
if Rn == '1111' || (P == '0' && W == '0') then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  imm32 = ZeroExtend(imm8, 32);
index = (P == '1');  add = (U == '1');  wback = (W == '1');
if t IN {13,15} || (wback && n == t) then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STRH<c> <Rt>,[<Rn>{,#<imm5>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 0 | 0 | 0 | imm5 | imm5 | imm5 | imm5 | imm5 | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`STRH<c>.W <Rt>,[<Rn>{,#<imm12>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**编码 T3**（Armv7-M）：`STRH<c> <Rt>,[<Rn>,#-<imm8>]`（偏移：`index == TRUE`、`wback == FALSE`）、`STRH<c> <Rt>,[<Rn>],#+/-<imm8>`（后索引：`index == FALSE`、`wback == TRUE`）、`STRH<c> <Rt>,[<Rn>,#+/-<imm8>]!`（前索引：`index == TRUE`、`wback == TRUE`）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | P | U | W | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRH<c><q>
  <Rt>, [<Rn> {, #+/-<imm>}]
STRH<c><q>
  <Rt>, [<Rn>, #+/-<imm>]!
STRH<c><q>
  <Rt>, [<Rn>], #+/-<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `+/-`：`+` 或省略表示立即数偏移加到基址寄存器值上（`add == TRUE`），`-` 表示减去该偏移（`add == FALSE`）。`#0` 与 `#-0` 生成不同的指令。
* `<imm>`：加到 `<Rn>` 值上或从中减去以形成地址的立即数偏移。编码 T1 允许 0-62 范围内 2 的倍数，编码 T2 允许 0-4095 范围内的任意值，编码 T3 允许 0-255 范围内的任意值。在偏移寻址语法中 `<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `STR<c>H` 等价于 `STRH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset_addr = if add then (R[n] + imm32) else (R[n] - imm32);
    address = if index then offset_addr else R[n];
    MemU[address,2] = R[t]<15:0>;
    if wback then R[n] = offset_addr;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.171. STRH (register)：寄存器存储寄存器半字

寄存器存储寄存器半字（Store Register Halfword (register)）由基址寄存器值与偏移寄存器值计算出地址，把一个半字从寄存器存储到存储器。偏移寄存器值可以被左移 0、1、2 或 3 位。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。

**编码专用伪代码**

```arm
t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, 0);
if Rn == '1111' then UNDEFINED;

t = UInt(Rt);  n = UInt(Rn);  m = UInt(Rm);
index = TRUE;  add = TRUE;  wback = FALSE;
(shift_t, shift_n) = (SRType_LSL, UInt(imm2));
if t IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`STRH<c> <Rt>,[<Rn>,<Rm>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rn | Rn | Rn | Rt | Rt | Rt |

**编码 T2**（Armv7-M）：`STRH<c>.W <Rt>,[<Rn>,<Rm>{,LSL #<imm2>}]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 0 | 0 | 0 | 0 | 0 | 0 | imm2 | imm2 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
STRH<c><q>
  <Rt>, [<Rn>, <Rm> {, LSL #<shift>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：源寄存器。
* `<Rn>`：包含基址值的寄存器。该寄存器允许是 SP。
* `<Rm>`：包含偏移的寄存器，该偏移左移后加到 `<Rn>` 值上以形成地址。
* `<shift>`：`<Rm>` 中值左移的位数，范围为 0-3。如果省略该选项，则假定移位 0，且两种编码都允许；如果指定该选项，则只允许编码 T2。

pre-UAL 语法 `STR<c>H` 等价于 `STRH<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    offset = Shift(R[m], shift_t, shift_n, APSR.C);
    address = R[n] + offset;
    MemU[address,2] = R[t]<15:0>;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.172. STRHT：非特权存储寄存器半字

非特权存储寄存器半字（Store Register Halfword Unprivileged）由基址寄存器值与立即数偏移计算出地址，把一个半字从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。特权软件使用 `STRHT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STRHT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRHT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围为 0-255。`<imm>` 可以省略，表示偏移 0。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    MemU_unpriv[address,2] = R[t]<15:0>;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.173. STRT：非特权存储寄存器

非特权存储寄存器（Store Register Unprivileged）由基址寄存器值与立即数偏移计算出地址，把一个字从寄存器存储到存储器。关于存储器访问的信息，参见第 A7-184 页的「存储器访问」。特权软件使用 `STRT` 指令时，存储器访问受到限制，如同该软件是非特权的一样。另见第 B3-637 页的「MPU_CTRL 设置对非特权指令的影响」。

**编码专用伪代码**

```arm
if Rn == '1111' then UNDEFINED;
t = UInt(Rt);  n = UInt(Rn);  postindex = FALSE;  add = TRUE;
register_form = FALSE;  imm32 = ZeroExtend(imm8, 32);
if t IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`STRT<c> <Rt>,[<Rn>,#<imm8>]`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | Rt | Rt | Rt | Rt | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
STRT<c><q>
  <Rt>, [<Rn> {, #<imm>}]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rt>`：源寄存器。
* `<Rn>`：基址寄存器。该寄存器允许是 SP。
* `<imm>`：加到 `<Rn>` 值上以形成地址的立即数偏移。允许范围为 0-255。`<imm>` 可以省略，表示偏移 0。

pre-UAL 语法 `STR<c>T` 等价于 `STRT<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    address = R[n] + imm32;
    data = R[t];
    MemU_unpriv[address,4] = data;
```

**异常**：UsageFault、MemManage、BusFault。

### 7.174. SUB (immediate)：立即数减法

立即数减法（Subtract (immediate)）把一个立即数从一个寄存器值中减去，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  setflags = !InITBlock();  imm32 = ZeroExtend(imm3, 32);
d = UInt(Rdn);  n = UInt(Rdn);  setflags = !InITBlock();  imm32 = ZeroExtend(imm8, 32);
if Rd == '1111' && S == '1' then SEE CMP (immediate);
if Rn == '1101' then SEE SUB (SP minus immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d == 13 || (d == 15 && S == '0') || n == 15 then UNPREDICTABLE;
if Rn == '1111' then SEE ADR;
if Rn == '1101' then SEE SUB (SP minus immediate);
d = UInt(Rd);  n = UInt(Rn);  setflags = FALSE;  imm32 = ZeroExtend(i:imm3:imm8, 32);
if d IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`SUBS <Rd>,<Rn>,#<imm3>`（IT 块外）、`SUB<c> <Rd>,<Rn>,#<imm3>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 1 | 1 | 1 | 1 | imm3 | imm3 | imm3 | Rn | Rn | Rn | Rd | Rd | Rd |

**编码 T2**（Thumb 指令集的所有版本）：`SUBS <Rdn>,#<imm8>`（IT 块外）、`SUB<c> <Rdn>,#<imm8>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 1 | 1 | 1 | Rdn | Rdn | Rdn | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`SUB{S}<c>.W <Rd>,<Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 1 | 0 | 1 | S | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T4**（Armv7-M）：`SUBW<c> <Rd>,<Rn>,#<imm12>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
SUB{S}<c><q>
  {<Rd>,} <Rn>, #<const>       // 允许所有编码
SUBW<c><q>
  {<Rd>,} <Rn>, #<const>       // 只允许编码 T4
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。如果为 `<Rn>` 指定 SP，参见第 A7-406 页的「SUB (SP minus immediate)」；如果为 `<Rn>` 指定 PC，参见第 A7-198 页的「ADR」。
* `<const>`：指定要从由 `<Rn>` 得到的值中减去的立即数。允许的取值范围为：编码 T1 为 0-7，编码 T2 为 0-255，编码 T4 为 0-4095；编码 T3 的允许取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

当同一长度的多种编码可用时，编码 T3 优先于编码 T4（如需编码 T4，使用 `SUBW` 语法）。如果指定了 `<Rd>`，编码 T1 优先于编码 T2；如果省略 `<Rd>`，编码 T2 优先于编码 T1。

pre-UAL 语法 `SUB<c>S` 等价于 `SUBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(R[n], NOT(imm32), '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.175. SUB (register)：寄存器减法

寄存器减法（Subtract (register)）从一个寄存器值中减去一个可选移位的寄存器值，并把结果写入目的寄存器；它可以选择根据结果更新条件标志。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = !InITBlock();
(shift_t, shift_n) = (SRType_LSL, 0);
if Rd == '1111' && S == '1' then SEE CMP (register);
if Rn == '1101' then SEE SUB (SP minus register);
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 || (d == 15 && S == '0') || n == 15 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`SUBS <Rd>,<Rn>,<Rm>`（IT 块外）、`SUB<c> <Rd>,<Rn>,<Rm>`（IT 块内）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rm | Rm | Rm | Rn | Rn | Rn | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`SUB{S}<c>.W <Rd>,<Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | S | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SUB{S}<c><q>
  {<Rd>,} <Rn>, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：指定包含第一个操作数的寄存器。如果为 `<Rn>` 指定 SP，参见第 A7-408 页的「SUB (SP minus register)」。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

pre-UAL 语法 `SUB<c>S` 等价于 `SUBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(R[n], NOT(shifted), '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.176. SUB (SP minus immediate)：SP 减立即数

SP 减立即数（Subtract (SP minus immediate)）从 SP 值中减去一个立即数，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = 13;  setflags = FALSE;  imm32 = ZeroExtend(imm7:'00', 32);
if Rd == '1111' && S == '1' then SEE CMP (immediate);
d = UInt(Rd);  setflags = (S == '1');  imm32 = ThumbExpandImm(i:imm3:imm8);
if d == 15 && S == '0' then UNPREDICTABLE;
d = UInt(Rd);  setflags = FALSE;  imm32 = ZeroExtend(i:imm3:imm8, 32);
if d == 15 then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`SUB<c> SP,SP,#<imm7>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | imm7 | imm7 | imm7 | imm7 | imm7 | imm7 | imm7 |

**编码 T2**（Armv7-M）：`SUB{S}<c>.W <Rd>,SP,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 1 | 1 | 0 | 1 | S | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T3**（Armv7-M）：`SUBW<c> <Rd>,SP,#<imm12>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
SUB{S}<c><q>
  {<Rd>,} SP, #<const>        // 允许所有编码
SUBW<c><q>
  {<Rd>,} SP, #<const>        // 只允许编码 T3
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器为 SP。
* `<const>`：指定要从 SP 值中减去的立即数。允许的取值为：编码 T1 为 0-508 范围内 4 的倍数，编码 T3 为 0-4095 范围内的任意值；编码 T2 的允许取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

当两个 32 位编码都可用时，编码 T2 优先于编码 T3（如需编码 T3，使用 `SUBW` 语法）。

pre-UAL 语法 `SUB<c>S` 等价于 `SUBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result, carry, overflow) = AddWithCarry(SP, NOT(imm32), '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.177. SUB (SP minus register)：SP 减寄存器

SP 减寄存器（Subtract (SP minus register)）从 SP 值中减去一个可选移位的寄存器值，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
if Rd == '1111' && S == '1' then SEE CMP (register);
d = UInt(Rd);  m = UInt(Rm);  setflags = (S == '1');
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if d == 13 && (shift_t != SRType_LSL || shift_n > 3) then UNPREDICTABLE;
if (d == 15 && S == '0') || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`SUB{S}<c> <Rd>,SP,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | S | 1 | 1 | 0 | 1 |
| [31:16] | (0) | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SUB{S}<c><q>
  {<Rd>,} SP, <Rm> {,<shift>}
```

where：

* `S`：如果出现，表示指令更新标志；否则不更新标志。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：指定目的寄存器。如果省略 `<Rd>`，该寄存器为 SP。
* `<Rm>`：指定可选移位并用作第二个操作数的寄存器。
* `<shift>`：指定施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

如果 `<Rd>` 为 SP 或被省略，`<shift>` 只允许为 `LSL #0`、`LSL #1`、`LSL #2` 或 `LSL #3`。

pre-UAL 语法 `SUB<c>S` 等价于 `SUBS<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    shifted = Shift(R[m], shift_t, shift_n, APSR.C);
    (result, carry, overflow) = AddWithCarry(SP, NOT(shifted), '1');
    R[d] = result;
    if setflags then
        APSR.N = result<31>;
        APSR.Z = IsZeroBit(result);
        APSR.C = carry;
        APSR.V = overflow;
```

**异常**：无。

### 7.178. SVC：管理员调用

管理员调用（Supervisor Call）。`SVC` 指令生成对系统管理程序（supervisor）的调用。更多信息参见第 B1-523 页的「Armv7-M 异常模型」。

可用它作为对操作系统的调用，以提供服务。

**注意：** 在较早版本的 Arm 架构中，`SVC` 称为 `SWI`，即软件中断（Software Interrupt）。

**编码专用伪代码**

```arm
imm32 = ZeroExtend(imm8, 32);
// imm32 用于汇编/反汇编。某些系统中的 SVC 处理程序
// 在软件中解释 imm8，例如用于确定所请求的服务。
```

**编码 T1**（Thumb 指令集的所有版本）：`SVC<c> #<imm8>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
SVC<c><q>
  #<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<imm>`：8 位立即数常量。

pre-UAL 语法 `SWI<c>` 等价于 `SVC<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    CallSupervisor();
```

**异常**：SVCall。

### 7.179. SXTAB：有符号扩展并加字节

有符号扩展并加字节（Signed Extend and Add Byte）从一个寄存器中提取一个 8 位值，把它符号扩展到 32 位，将结果加到另一个寄存器中的值上，并把最终结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE SXTB;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SXTAB<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTAB<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = R[n] + SignExtend(rotated<7:0>, 32);
```

**异常**：无。

### 7.180. SXTAB16：有符号扩展并加字节 16

有符号扩展并加字节 16（Signed Extend and Add Byte 16）从一个寄存器中提取两个 8 位值，把它们各自符号扩展到 16 位，将结果加到另一个寄存器的两个 16 位值上，并把最终结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE SXTB16;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SXTAB16<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTAB16<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d]<15:0>  = R[n]<15:0> + SignExtend(rotated<7:0>, 16);
    R[d]<31:16> = R[n]<31:16> + SignExtend(rotated<23:16>, 16);
```

**异常**：无。

### 7.181. SXTAH：有符号扩展并加半字

有符号扩展并加半字（Signed Extend and Add Halfword）从一个寄存器中提取一个 16 位值，把它符号扩展到 32 位，将结果加到另一个寄存器中的值上，并把最终结果写入目的寄存器。在提取 16 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE SXTH;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SXTAH<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTAH<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = R[n] + SignExtend(rotated<15:0>, 32);
```

**异常**：无。

### 7.182. SXTB：有符号扩展字节

有符号扩展字节（Signed Extend Byte）从一个寄存器中提取一个 8 位值，把它符号扩展到 32 位，并把结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = 0;
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`SXTB<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`SXTB<c>.W <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTB<c><q>
  <Rd>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：包含操作数的寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 如果你的汇编器接受移位 `#0` 并将其视为等同于无移位或 `LSL #0`，那么它必须在此处接受 `ROR #0`。它等价于省略 `<rotation>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = SignExtend(rotated<7:0>, 32);
```

**异常**：无。

### 7.183. SXTB16：有符号扩展字节 16

有符号扩展字节 16（Signed Extend Byte 16）从一个寄存器中提取两个 8 位值，把它们各自符号扩展到 16 位，并把结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`SXTB16<c> <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTB16<c><q>
  {<Rd>,} <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：包含操作数的寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d]<15:0>  = SignExtend(rotated<7:0>, 16);
    R[d]<31:16> = SignExtend(rotated<23:16>, 16);
```

**异常**：无。

### 7.184. SXTH：有符号扩展半字

有符号扩展半字（Signed Extend Halfword）从一个寄存器中提取一个 16 位值，把它符号扩展到 32 位，并把结果写入目的寄存器。在提取 16 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = 0;
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`SXTH<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`SXTH<c>.W <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
SXTH<c><q>
  <Rd>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：包含操作数的寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 如果你的汇编器接受移位 `#0` 并将其视为等同于无移位或 `LSL #0`，那么它必须在此处接受 `ROR #0`。它等价于省略 `<rotation>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = SignExtend(rotated<15:0>, 32);
```

**异常**：无。

### 7.185. TBB、TBH：表分支字节、表分支半字

表分支字节（Table Branch Byte）使用一张单字节偏移表实现 PC 相对的前向分支。基址寄存器提供指向该表的指针，第二个寄存器提供表内索引。分支长度为表中返回字节值的两倍。

表分支半字（Table Branch Halfword）使用一张单半字偏移表实现 PC 相对的前向分支。基址寄存器提供指向该表的指针，第二个寄存器提供表内索引。分支长度为表中返回半字值的两倍。

**编码专用伪代码**

```arm
n = UInt(Rn);  m = UInt(Rm);  is_tbh = (H == '1');
if n == 13 || m IN {13,15} then UNPREDICTABLE;
if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`TBB<c> [<Rn>,<Rm>]`（IT 块外或作为 IT 块的最后一条）、`TBH<c> [<Rn>,<Rm>,LSL #1]`（IT 块外或作为 IT 块的最后一条）

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (1) | (1) | (1) | (1) | (0) | (0) | (0) | (0) | 0 | 0 | 0 | H | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
TBB<c><q>
  [<Rn>, <Rm>]
TBH<c><q>
  [<Rn>, <Rm>, LSL #1]
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：基址寄存器。它包含分支长度表的地址。该寄存器可以是 PC；如果为 PC，则表紧接在该指令之后。
* `<Rm>`：索引寄存器。
  * 对于 `TBB`，它包含指向表中单个字节的整数。表内偏移就是该索引的值。
  * 对于 `TBH`，它包含指向表中单个半字的整数。表内偏移是该索引值的两倍。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if is_tbh then
        halfwords = UInt(MemU[R[n]+LSL(R[m],1), 2]);
    else
        halfwords = UInt(MemU[R[n]+R[m], 1]);
    BranchWritePC(PC + 2*halfwords);
```

**异常**：MemManage、BusFault、UsageFault。

### 7.186. TEQ (immediate)：立即数等价测试

立即数等价测试（Test Equivalence (immediate)）对一个寄存器值与一个立即数执行异或运算。它根据结果更新条件标志，并丢弃该结果。

**编码专用伪代码**

```arm
n = UInt(Rn);
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`TEQ<c> <Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
TEQ<c><q>
  <Rn>, #<const>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：包含操作数的寄存器。
* `<const>`：要与由 `<Rn>` 得到的值进行比较的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] EOR imm32;
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    // APSR.V 不变
```

**异常**：无。

### 7.187. TEQ (register)：寄存器等价测试

寄存器等价测试（Test Equivalence (register)）对一个寄存器值与一个可选移位的寄存器值执行异或运算。它根据结果更新条件标志，并丢弃该结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`TEQ<c> <Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
TEQ<c><q>
  <Rn>, <Rm> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：包含第一个操作数的寄存器。
* `<Rm>`：可选移位并用作第二个操作数的寄存器。
* `<shift>`：施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = R[n] EOR shifted;
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    // APSR.V 不变
```

**异常**：无。

### 7.188. TST (immediate)：立即数测试

立即数测试（Test (immediate)）对一个寄存器值与一个立即数执行逻辑与运算。它根据结果更新条件标志，并丢弃该结果。

**编码专用伪代码**

```arm
n = UInt(Rn);
(imm32, carry) = ThumbExpandImm_C(i:imm3:imm8, APSR.C);
if n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`TST<c> <Rn>,#<const>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | i | 0 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**汇编语法**

```arm
TST<c><q>
  <Rn>, #<const>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：包含操作数的寄存器。
* `<const>`：要与由 `<Rn>` 得到的值进行比较的立即数。允许的取值范围参见第 A5-139 页的「Thumb 指令中的修改立即数常量」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = R[n] AND imm32;
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    // APSR.V 不变
```

**异常**：无。

### 7.189. TST (register)：寄存器测试

寄存器测试（Test (register)）对一个寄存器值与一个可选移位的寄存器值执行逻辑与运算。它根据结果更新条件标志，并丢弃该结果。

**编码专用伪代码**

```arm
n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = (SRType_LSL, 0);
n = UInt(Rn);  m = UInt(Rm);
(shift_t, shift_n) = DecodeImmShift(type, imm3:imm2);
if n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Thumb 指令集的所有版本）：`TST<c> <Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | Rm | Rm | Rm | Rn | Rn | Rn |

**编码 T2**（Armv7-M）：`TST<c>.W <Rn>,<Rm>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (0) | imm3 | imm3 | imm3 | 1 | 1 | 1 | 1 | imm2 | imm2 | type | type | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
TST<c><q>
  <Rn>, <Rm> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rn>`：包含第一个操作数的寄存器。
* `<Rm>`：可选移位并用作第二个操作数的寄存器。
* `<shift>`：施加于从 `<Rm>` 读取的值的移位。如果省略 `<shift>`，不施加移位，且两种编码都允许；如果指定 `<shift>`，只允许编码 T2。可能的移位及其编码方式参见第 A7-182 页的「施加于寄存器的移位」。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (shifted, carry) = Shift_C(R[m], shift_t, shift_n, APSR.C);
    result = R[n] AND shifted;
    APSR.N = result<31>;
    APSR.Z = IsZeroBit(result);
    APSR.C = carry;
    // APSR.V 不变
```

**异常**：无。

### 7.190. UADD16：无符号 16 位加法

无符号 16 位加法（Unsigned Add 16）执行两个 16 位无符号整数加法，并把结果写入目的寄存器。它根据加法的结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UADD16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<15:0>) + UInt(R[m]<15:0>);
    sum2 = UInt(R[n]<31:16>) + UInt(R[m]<31:16>);
    R[d]<15:0>  = sum1<15:0>;
    R[d]<31:16> = sum2<15:0>;
    APSR.GE<1:0> = if sum1 >= 0x10000 then '11' else '00';
    APSR.GE<3:2> = if sum2 >= 0x10000 then '11' else '00';
```

**异常**：无。

### 7.191. UADD8：无符号 8 位加法

无符号 8 位加法（Unsigned Add 8）执行四个 8 位无符号整数加法，并把结果写入目的寄存器。它根据加法的结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UADD8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<7:0>) + UInt(R[m]<7:0>);
    sum2 = UInt(R[n]<15:8>) + UInt(R[m]<15:8>);
    sum3 = UInt(R[n]<23:16>) + UInt(R[m]<23:16>);
    sum4 = UInt(R[n]<31:24>) + UInt(R[m]<31:24>);
    R[d]<7:0>   = sum1<7:0>;
    R[d]<15:8>  = sum2<7:0>;
    R[d]<23:16> = sum3<7:0>;
    R[d]<31:24> = sum4<7:0>;
    APSR.GE<0>  = if sum1 >= 0x100 then '1' else '0';
    APSR.GE<1>  = if sum2 >= 0x100 then '1' else '0';
    APSR.GE<2>  = if sum3 >= 0x100 then '1' else '0';
    APSR.GE<3>  = if sum4 >= 0x100 then '1' else '0';
```

**异常**：无。

### 7.192. UASX：无符号带交换的加法与减法

无符号带交换的加法与减法（Unsigned Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数加法和一个 16 位无符号整数减法，并把结果写入目的寄存器。它根据结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UASX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `UADDSUBX<c>` 等价于 `UASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = UInt(R[n]<15:0>) - UInt(R[m]<31:16>);
    sum  = UInt(R[n]<31:16>) + UInt(R[m]<15:0>);
    R[d]<15:0>  = diff<15:0>;
    R[d]<31:16> = sum<15:0>;
    APSR.GE<1:0> = if diff >= 0 then '11' else '00';
    APSR.GE<3:2> = if sum  >= 0x10000 then '11' else '00';
```

**异常**：无。

### 7.193. UBFX：无符号位域提取

无符号位域提取（Unsigned Bit Field Extract）从一个寄存器中提取任意位置的任意数量的相邻位，把它们零扩展到 32 位，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);
lsbit = UInt(imm3:imm2);  widthminus1 = UInt(widthm1);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`UBFX<c> <Rd>,<Rn>,#<lsb>,#<width>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | widthm1 | widthm1 | widthm1 | widthm1 | widthm1 |

**汇编语法**

```arm
UBFX<c><q>
  <Rd>, <Rn>, #<lsb>, #<width>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：包含第一个操作数的寄存器。
* `<lsb>`：位域中最低有效位的位号，范围为 0-31。它决定 `lsbit` 的取值。
* `<width>`：位域的宽度，范围为 1 到 32-`<lsb>`。`widthminus1` 的取值为 `<width>`-1。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    msbit = lsbit + widthminus1;
    if msbit <= 31 then
        R[d] = ZeroExtend(R[n]<msbit:lsbit>, 32);
    else
        UNPREDICTABLE;
```

**异常**：无。

### 7.194. UDF：永久未定义

永久未定义（Permanently Undefined）产生未定义指令异常。

**编码专用伪代码**

```arm
imm32 = ZeroExtend(imm8, 32);
// imm32 仅用于汇编与反汇编，硬件忽略它。
imm32 = ZeroExtend(imm4:imm12, 32);
// imm32 仅用于汇编与反汇编，硬件忽略它。
```

**编码 T1**（Armv7-M）：`UDF<c> #<imm8>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 | imm8 |

**编码 T2**（Armv7-M）：`UDF<c>.W #<imm16>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | imm4 | imm4 | imm4 | imm4 |
| [31:16] | 1 | 0 | 1 | 0 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 | imm12 |

**汇编语法**

```arm
UDF<c><q>
  {#}<imm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<imm>`：立即数常量，编码 T1 中为 8 位，编码 T2 中为 16 位。处理器忽略该常量的值。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    UNDEFINED;
```

**异常**：未定义指令（Undefined Instruction）。

### 7.195. UDIV：无符号除法

无符号除法（Unsigned Divide）把一个 32 位无符号整数寄存器值除以另一个 32 位无符号整数寄存器值，并把结果写入目的寄存器。条件标志不受影响。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`UDIV<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | (1) | (1) | (1) | (1) | Rd | Rd | Rd | Rd | 1 | 1 | 1 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UDIV<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。如果省略 `<Rd>`，该寄存器与 `<Rn>` 相同。
* `<Rn>`：包含被除数的寄存器。
* `<Rm>`：包含除数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    if UInt(R[m]) == 0 then
        if IntegerZeroDivideTrappingEnabled() then
            GenerateIntegerZeroDivide();
        else
            result = 0;
    else
        result = RoundTowardsZero(UInt(R[n]) / UInt(R[m]));
    R[d] = result<31:0>;
```

**异常**：UsageFault。

### 7.196. UHADD16：无符号折半 16 位加法

无符号折半 16 位加法（Unsigned Halving Add 16）执行两个 16 位无符号整数加法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHADD16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<15:0>) + UInt(R[m]<15:0>);
    sum2 = UInt(R[n]<31:16>) + UInt(R[m]<31:16>);
    R[d]<15:0>  = sum1<16:1>;
    R[d]<31:16> = sum2<16:1>;
```

**异常**：无。

### 7.197. UHADD8：无符号折半 8 位加法

无符号折半 8 位加法（Unsigned Halving Add 8）执行四个 8 位无符号整数加法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHADD8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<7:0>) + UInt(R[m]<7:0>);
    sum2 = UInt(R[n]<15:8>) + UInt(R[m]<15:8>);
    sum3 = UInt(R[n]<23:16>) + UInt(R[m]<23:16>);
    sum4 = UInt(R[n]<31:24>) + UInt(R[m]<31:24>);
    R[d]<7:0>   = sum1<8:1>;
    R[d]<15:8>  = sum2<8:1>;
    R[d]<23:16> = sum3<8:1>;
    R[d]<31:24> = sum4<8:1>;
```

**异常**：无。

### 7.198. UHASX：无符号折半带交换的加法与减法

无符号折半带交换的加法与减法（Unsigned Halving Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数加法和一个 16 位无符号整数减法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHASX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `UHADDSUBX<c>` 等价于 `UHASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = UInt(R[n]<15:0>) - UInt(R[m]<31:16>);
    sum  = UInt(R[n]<31:16>) + UInt(R[m]<15:0>);
    R[d]<15:0>  = diff<16:1>;
    R[d]<31:16> = sum<16:1>;
```

**异常**：无。

### 7.199. UHSAX：无符号折半带交换的减法与加法

无符号折半带交换的减法与加法（Unsigned Halving Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数减法和一个 16 位无符号整数加法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHSAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHSAX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `UHSUBADDX<c>` 等价于 `UHSAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = UInt(R[n]<15:0>) + UInt(R[m]<31:16>);
    diff = UInt(R[n]<31:16>) - UInt(R[m]<15:0>);
    R[d]<15:0>  = sum<16:1>;
    R[d]<31:16> = diff<16:1>;
```

**异常**：无。

### 7.200. UHSUB16：无符号折半 16 位减法

无符号折半 16 位减法（Unsigned Halving Subtract 16）执行两个 16 位无符号整数减法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHSUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHSUB16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<15:0>) - UInt(R[m]<15:0>);
    diff2 = UInt(R[n]<31:16>) - UInt(R[m]<31:16>);
    R[d]<15:0>  = diff1<16:1>;
    R[d]<31:16> = diff2<16:1>;
```

**异常**：无。

### 7.201. UHSUB8：无符号折半 8 位减法

无符号折半 8 位减法（Unsigned Halving Subtract 8）执行四个 8 位无符号整数减法，把结果折半后写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UHSUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UHSUB8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<7:0>) - UInt(R[m]<7:0>);
    diff2 = UInt(R[n]<15:8>) - UInt(R[m]<15:8>);
    diff3 = UInt(R[n]<23:16>) - UInt(R[m]<23:16>);
    diff4 = UInt(R[n]<31:24>) - UInt(R[m]<31:24>);
    R[d]<7:0>   = diff1<8:1>;
    R[d]<15:8>  = diff2<8:1>;
    R[d]<23:16> = diff3<8:1>;
    R[d]<31:24> = diff4<8:1>;
```

**异常**：无。

### 7.202. UMAAL：无符号乘法累加累加长

无符号乘法累加累加长（Unsigned Multiply Accumulate Accumulate Long）把两个无符号 32 位值相乘产生一个 64 位值，再加上两个无符号 32 位值，并把 64 位结果写入两个寄存器。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UMAAL<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 0 | 1 | 1 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UMAAL<c><q>
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供待相加的一个 32 位值，并作为结果低 32 位的目的寄存器。
* `<RdHi>`：提供待相加的另一个 32 位值，并作为结果高 32 位的目的寄存器。
* `<Rn>`：包含第一个乘法操作数的寄存器。
* `<Rm>`：包含第二个乘法操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = UInt(R[n]) * UInt(R[m]) + UInt(R[dHi]) + UInt(R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.203. UMLAL：无符号乘法累加长

无符号乘法累加长（Unsigned Multiply Accumulate Long）把两个无符号 32 位值相乘产生一个 64 位值，并把该值与一个 64 位值累加。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  setflags = FALSE;
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`UMLAL<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UMLAL<c><q>
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：提供累加值的低 32 位，并作为结果低 32 位的目的寄存器。
* `<RdHi>`：提供累加值的高 32 位，并作为结果高 32 位的目的寄存器。
* `<Rn>`：包含第一个操作数的寄存器。
* `<Rm>`：包含第二个操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = UInt(R[n]) * UInt(R[m]) + UInt(R[dHi]:R[dLo]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.204. UMULL：无符号乘法长

无符号乘法长（Unsigned Multiply Long）把两个 32 位无符号值相乘，产生一个 64 位结果。

**编码专用伪代码**

```arm
dLo = UInt(RdLo);  dHi = UInt(RdHi);  n = UInt(Rn);  m = UInt(Rm);  setflags = FALSE;
if dLo IN {13,15} || dHi IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
if dHi == dLo then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`UMULL<c> <RdLo>,<RdHi>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | RdLo | RdLo | RdLo | RdLo | RdHi | RdHi | RdHi | RdHi | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UMULL<c><q>
  <RdLo>, <RdHi>, <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<RdLo>`：存放结果的低 32 位。
* `<RdHi>`：存放结果的高 32 位。
* `<Rn>`：包含第一个操作数的寄存器。
* `<Rm>`：包含第二个操作数的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    result = UInt(R[n]) * UInt(R[m]);
    R[dHi] = result<63:32>;
    R[dLo] = result<31:0>;
```

**异常**：无。

### 7.205. UQADD16：无符号饱和 16 位加法

无符号饱和 16 位加法（Unsigned Saturating Add 16）执行两个 16 位无符号整数加法，把结果饱和到 16 位无符号整数范围 0 ≤ x ≤ 2^16^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQADD16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQADD16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<15:0>) + UInt(R[m]<15:0>);
    sum2 = UInt(R[n]<31:16>) + UInt(R[m]<31:16>);
    R[d]<15:0>  = UnsignedSat(sum1, 16);
    R[d]<31:16> = UnsignedSat(sum2, 16);
```

**异常**：无。

### 7.206. UQADD8：无符号饱和 8 位加法

无符号饱和 8 位加法（Unsigned Saturating Add 8）执行四个 8 位无符号整数加法，把结果饱和到 8 位无符号整数范围 0 ≤ x ≤ 2^8^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQADD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQADD8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum1 = UInt(R[n]<7:0>) + UInt(R[m]<7:0>);
    sum2 = UInt(R[n]<15:8>) + UInt(R[m]<15:8>);
    sum3 = UInt(R[n]<23:16>) + UInt(R[m]<23:16>);
    sum4 = UInt(R[n]<31:24>) + UInt(R[m]<31:24>);
    R[d]<7:0>   = UnsignedSat(sum1, 8);
    R[d]<15:8>  = UnsignedSat(sum2, 8);
    R[d]<23:16> = UnsignedSat(sum3, 8);
    R[d]<31:24> = UnsignedSat(sum4, 8);
```

**异常**：无。

### 7.207. UQASX：无符号饱和带交换的加法与减法

无符号饱和带交换的加法与减法（Unsigned Saturating Add and Subtract with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数加法和一个 16 位无符号整数减法，把结果饱和到 16 位无符号整数范围 0 ≤ x ≤ 2^16^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQASX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQASX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `UQADDSUBX<c>` 等价于 `UQASX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff = UInt(R[n]<15:0>) - UInt(R[m]<31:16>);
    sum  = UInt(R[n]<31:16>) + UInt(R[m]<15:0>);
    R[d]<15:0>  = UnsignedSat(diff, 16);
    R[d]<31:16> = UnsignedSat(sum, 16);
```

**异常**：无。

### 7.208. UQSAX：无符号饱和带交换的减法与加法

无符号饱和带交换的减法与加法（Unsigned Saturating Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数减法和一个 16 位无符号整数加法，把结果饱和到 16 位无符号整数范围 0 ≤ x ≤ 2^16^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQSAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQSAX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `UQSUBADDX<c>` 等价于 `UQSAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = UInt(R[n]<15:0>) + UInt(R[m]<31:16>);
    diff = UInt(R[n]<31:16>) - UInt(R[m]<15:0>);
    R[d]<15:0>  = UnsignedSat(sum, 16);
    R[d]<31:16> = UnsignedSat(diff, 16);
```

**异常**：无。

### 7.209. UQSUB16：无符号饱和 16 位减法

无符号饱和 16 位减法（Unsigned Saturating Subtract 16）执行两个 16 位无符号整数减法，把结果饱和到 16 位无符号整数范围 0 ≤ x ≤ 2^16^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQSUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQSUB16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<15:0>) - UInt(R[m]<15:0>);
    diff2 = UInt(R[n]<31:16>) - UInt(R[m]<31:16>);
    R[d]<15:0>  = UnsignedSat(diff1, 16);
    R[d]<31:16> = UnsignedSat(diff2, 16);
```

**异常**：无。

### 7.210. UQSUB8：无符号饱和 8 位减法

无符号饱和 8 位减法（Unsigned Saturating Subtract 8）执行四个 8 位无符号整数减法，把结果饱和到 8 位无符号整数范围 0 ≤ x ≤ 2^8^ – 1，并把结果写入目的寄存器。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UQSUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 1 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UQSUB8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<7:0>) - UInt(R[m]<7:0>);
    diff2 = UInt(R[n]<15:8>) - UInt(R[m]<15:8>);
    diff3 = UInt(R[n]<23:16>) - UInt(R[m]<23:16>);
    diff4 = UInt(R[n]<31:24>) - UInt(R[m]<31:24>);
    R[d]<7:0>   = UnsignedSat(diff1, 8);
    R[d]<15:8>  = UnsignedSat(diff2, 8);
    R[d]<23:16> = UnsignedSat(diff3, 8);
    R[d]<31:24> = UnsignedSat(diff4, 8);
```

**异常**：无。

### 7.211. USAD8：无符号绝对差之和

无符号绝对差之和（Unsigned Sum of Absolute Differences）执行四个 8 位无符号减法，并把各差值的绝对值相加。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USAD8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
USAD8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    absdiff1 = Abs(UInt(R[n]<7:0>)   - UInt(R[m]<7:0>));
    absdiff2 = Abs(UInt(R[n]<15:8>)  - UInt(R[m]<15:8>));
    absdiff3 = Abs(UInt(R[n]<23:16>) - UInt(R[m]<23:16>));
    absdiff4 = Abs(UInt(R[n]<31:24>) - UInt(R[m]<31:24>));
    result = absdiff1 + absdiff2 + absdiff3 + absdiff4;
    R[d] = result<31:0>;
```

**异常**：无。

### 7.212. USADA8：无符号绝对差之和并累加

无符号绝对差之和并累加（Unsigned Sum of Absolute Differences and Accumulate）执行四个 8 位无符号减法，并把各差值的绝对值加到一个 32 位累加操作数上。

**编码专用伪代码**

```arm
if Ra == '1111' then SEE USAD8;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  a = UInt(Ra);
if d IN {13,15} || n IN {13,15} || m IN {13,15} || a == 13 then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USADA8<c> <Rd>,<Rn>,<Rm>,<Ra>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | Ra | Ra | Ra | Ra | Rd | Rd | Rd | Rd | 0 | 0 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
USADA8<c><q>
  <Rd>, <Rn>, <Rm>, <Ra>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<Ra>`：包含累加值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    absdiff1 = Abs(UInt(R[n]<7:0>)   - UInt(R[m]<7:0>));
    absdiff2 = Abs(UInt(R[n]<15:8>)  - UInt(R[m]<15:8>));
    absdiff3 = Abs(UInt(R[n]<23:16>) - UInt(R[m]<23:16>));
    absdiff4 = Abs(UInt(R[n]<31:24>) - UInt(R[m]<31:24>));
    result = UInt(R[a]) + absdiff1 + absdiff2 + absdiff3 + absdiff4;
    R[d] = result<31:0>;
```

**异常**：无。

### 7.213. USAT：无符号饱和

无符号饱和（Unsigned Saturate）把一个可选移位的符号值饱和到一个选定的无符号范围。

如果操作发生饱和，Q 标志置 1。

**编码专用伪代码**

```arm
if sh == '1' && (imm3:imm2) == '00000' then
    if HaveDSPExt() then
        SEE USAT16;
    else
        UNDEFINED;
d = UInt(Rd);  n = UInt(Rn);  saturate_to = UInt(sat_imm);
(shift_t, shift_n) = DecodeImmShift(sh:'0', imm3:imm2);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7-M）：`USAT<c> <Rd>,#<imm5>,<Rn>{,<shift>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 1 | 0 | sh | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | imm3 | imm3 | imm3 | Rd | Rd | Rd | Rd | imm2 | imm2 | (0) | sat_imm | sat_imm | sat_imm | sat_imm | sat_imm |

**汇编语法**

```arm
USAT<c><q>
  <Rd>, #<imm>, <Rn> {,<shift>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<imm>`：饱和的位位置，范围为 0-31。
* `<Rn>`：包含待饱和值的寄存器。
* `<shift>`：可选移位。如果出现，必须为以下之一：
  * `LSL #N`：N 必须在 0-31 范围内。
  * `ASR #N`：N 必须在 1-31 范围内。

如果省略 `<shift>`，则使用 `LSL #0`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    operand = Shift(R[n], shift_t, shift_n, APSR.C);  // 忽略 APSR.C
    (result, sat) = UnsignedSatQ(SInt(operand), saturate_to);
    R[d] = ZeroExtend(result, 32);
    if sat then
        APSR.Q = '1';
```

**异常**：无。

### 7.214. USAT16：无符号饱和 16

无符号饱和 16（Unsigned Saturate 16）把两个有符号 16 位值饱和到一个选定的无符号范围。

如果操作发生饱和，Q 标志置 1。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  saturate_to = UInt(sat_imm);
if d IN {13,15} || n IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USAT16<c> <Rd>,#<imm4>,<Rn>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 0 | (0) | 1 | 1 | 1 | 0 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 0 | 0 | 0 | 0 | Rd | Rd | Rd | Rd | 0 | 0 | (0) | (0) | sat_imm | sat_imm | sat_imm | sat_imm |

**汇编语法**

```arm
USAT16<c><q>
  <Rd>, #<imm>, <Rn>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<imm>`：饱和的位位置，范围为 0-15。
* `<Rn>`：包含待饱和值的寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    (result1, sat1) = UnsignedSatQ(SInt(R[n]<15:0>), saturate_to);
    (result2, sat2) = UnsignedSatQ(SInt(R[n]<31:16>), saturate_to);
    R[d]<15:0> = ZeroExtend(result1, 16);
    R[d]<31:16> = ZeroExtend(result2, 16);
    if sat1 || sat2 then
        APSR.Q = '1';
```

**异常**：无。

### 7.215. USAX：无符号带交换的减法与加法

无符号带交换的减法与加法（Unsigned Subtract and Add with Exchange）交换第二个操作数的两个半字，执行一个 16 位无符号整数减法和一个 16 位无符号整数加法，并把结果写入目的寄存器。它根据结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USAX<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
USAX<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

pre-UAL 语法 `USUBADDX<c>` 等价于 `USAX<c>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    sum  = UInt(R[n]<15:0>) + UInt(R[m]<31:16>);
    diff = UInt(R[n]<31:16>) - UInt(R[m]<15:0>);
    R[d]<15:0>  = sum<15:0>;
    R[d]<31:16> = diff<15:0>;
    APSR.GE<1:0> = if sum  >= 0x10000 then '11' else '00';
    APSR.GE<3:2> = if diff >= 0 then '11' else '00';
```

**异常**：无。

### 7.216. USUB16：无符号 16 位减法

无符号 16 位减法（Unsigned Subtract 16）执行两个 16 位无符号整数减法，并把结果写入目的寄存器。它根据减法结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USUB16<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
USUB16<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<15:0>) - UInt(R[m]<15:0>);
    diff2 = UInt(R[n]<31:16>) - UInt(R[m]<31:16>);
    R[d]<15:0>  = diff1<15:0>;
    R[d]<31:16> = diff2<15:0>;
    APSR.GE<1:0> = if diff1 >= 0 then '11' else '00';
    APSR.GE<3:2> = if diff2 >= 0 then '11' else '00';
```

**异常**：无。

### 7.217. USUB8：无符号 8 位减法

无符号 8 位减法（Unsigned Subtract 8）执行四个 8 位无符号整数减法，并把结果写入目的寄存器。它根据减法结果设置 APSR.GE 位。

**编码专用伪代码**

```arm
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);
if d IN {13,15} || n IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`USUB8<c> <Rd>,<Rn>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 0 | 1 | 0 | 0 | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
USUB8<c><q>
  {<Rd>,} <Rn>, <Rm>
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    diff1 = UInt(R[n]<7:0>) - UInt(R[m]<7:0>);
    diff2 = UInt(R[n]<15:8>) - UInt(R[m]<15:8>);
    diff3 = UInt(R[n]<23:16>) - UInt(R[m]<23:16>);
    diff4 = UInt(R[n]<31:24>) - UInt(R[m]<31:24>);
    R[d]<7:0>   = diff1<7:0>;
    R[d]<15:8>  = diff2<7:0>;
    R[d]<23:16> = diff3<7:0>;
    R[d]<31:24> = diff4<7:0>;
    APSR.GE<0>  = if diff1 >= 0 then '1' else '0';
    APSR.GE<1>  = if diff2 >= 0 then '1' else '0';
    APSR.GE<2>  = if diff3 >= 0 then '1' else '0';
    APSR.GE<3>  = if diff4 >= 0 then '1' else '0';
```

**异常**：无。

### 7.218. UXTAB：无符号扩展并加字节

无符号扩展并加字节（Unsigned Extend and Add Byte）从一个寄存器中提取一个 8 位值，把它零扩展到 32 位，将结果加到另一个寄存器中的值上，并把最终结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE UXTB;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UXTAB<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTAB<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = R[n] + ZeroExtend(rotated<7:0>, 32);
```

**异常**：无。

### 7.219. UXTAB16：无符号扩展并加字节 16

无符号扩展并加字节 16（Unsigned Extend and Add Byte 16）从一个寄存器中提取两个 8 位值，把它们各自零扩展到 16 位，将结果加到另一个寄存器的两个 16 位值上，并把最终结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE UXTB16;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UXTAB16<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTAB16<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d]<15:0>  = R[n]<15:0> + ZeroExtend(rotated<7:0>, 16);
    R[d]<31:16> = R[n]<31:16> + ZeroExtend(rotated<23:16>, 16);
```

**异常**：无。

### 7.220. UXTAH：无符号扩展并加半字

无符号扩展并加半字（Unsigned Extend and Add Halfword）从一个寄存器中提取一个 16 位值，把它零扩展到 32 位，将结果加到另一个寄存器中的值上，并把最终结果写入目的寄存器。在提取 16 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
if Rn == '1111' then SEE UXTH;
d = UInt(Rd);  n = UInt(Rn);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || n == 13 || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UXTAH<c> <Rd>,<Rn>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | Rn | Rn | Rn | Rn |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTAH<c><q>
  {<Rd>,} <Rn>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rn>`：第一个操作数寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = R[n] + ZeroExtend(rotated<15:0>, 32);
```

**异常**：无。

### 7.221. UXTB：无符号扩展字节

无符号扩展字节（Unsigned Extend Byte）从一个寄存器中提取一个 8 位值，把它零扩展到 32 位，并把结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = 0;
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`UXTB<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`UXTB<c>.W <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTB<c><q>
  <Rd>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：包含第二个操作数的寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 如果你的汇编器接受移位 `#0` 并将其视为等同于无移位或 `LSL #0`，那么它必须在此处接受 `ROR #0`。它等价于省略 `<rotation>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = ZeroExtend(rotated<7:0>, 32);
```

**异常**：无。

### 7.222. UXTB16：无符号扩展字节 16

无符号扩展字节 16（Unsigned Extend Byte 16）从一个寄存器中提取两个 8 位值，把它们各自零扩展到 16 位，并把结果写入目的寄存器。在提取 8 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv7E-M）：`UXTB16<c> <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTB16<c><q>
  {<Rd>,} <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：第二个操作数寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 汇编器可以把 `ROR #0` 视为与省略旋转相同（可能对允许的编码有限制），但这不是标准 UAL，不得用于反汇编。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d]<15:0>  = ZeroExtend(rotated<7:0>, 16);
    R[d]<31:16> = ZeroExtend(rotated<23:16>, 16);
```

**异常**：无。

### 7.223. UXTH：无符号扩展半字

无符号扩展半字（Unsigned Extend Halfword）从一个寄存器中提取一个 16 位值，把它零扩展到 32 位，并把结果写入目的寄存器。在提取 16 位值之前，可以指定 0、8、16 或 24 位的旋转。

**编码专用伪代码**

```arm
d = UInt(Rd);  m = UInt(Rm);  rotation = 0;
d = UInt(Rd);  m = UInt(Rm);  rotation = UInt(rotate:'000');
if d IN {13,15} || m IN {13,15} then UNPREDICTABLE;
```

**编码 T1**（Armv6-M、Armv7-M）：`UXTH<c> <Rd>,<Rm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | Rm | Rm | Rm | Rd | Rd | Rd |

**编码 T2**（Armv7-M）：`UXTH<c>.W <Rd>,<Rm>{,<rotation>}`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| [31:16] | 1 | 1 | 1 | 1 | Rd | Rd | Rd | Rd | 1 | (0) | rotate | rotate | Rm | Rm | Rm | Rm |

**汇编语法**

```arm
UXTH<c><q>
  <Rd>, <Rm> {, <rotation>}
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Rd>`：目的寄存器。
* `<Rm>`：包含第二个操作数的寄存器。
* `<rotation>`：可以是以下之一：
  * 省略：编码为 `rotate = '00'`。
  * `ROR #8`：编码为 `rotate = '01'`。
  * `ROR #16`：编码为 `rotate = '10'`。
  * `ROR #24`：编码为 `rotate = '11'`。

**注意：** 如果你的汇编器接受移位 `#0` 并将其视为等同于无移位或 `LSL #0`，那么它必须在此处接受 `ROR #0`。它等价于省略 `<rotation>`。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    rotated = ROR(R[m], rotation);
    R[d] = ZeroExtend(rotated<15:0>, 32);
```

**异常**：无。

### 7.224. VABS：浮点绝对值

浮点绝对值（Floating-point Absolute）取一个单精度寄存器的绝对值，并把结果放入第二个寄存器。

**编码专用伪代码**

```arm
dp_operation = (sz == '1');
d = if dp_operation then UInt(D:Vd) else UInt(Vd:D);
m = if dp_operation then UInt(M:Vm) else UInt(Vm:M);
```

**编码 T1**（FPv4-SP、FPv5；在仅单精度变体中 `sz = 1` 为未定义）：`VABS<c>.F32 <Sd>,<Sm>`、`VABS<c>.F64 <Dd>,<Dm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | D | 1 | 1 | 0 | 0 | 0 | 0 |
| [31:16] | Vd | Vd | Vd | Vd | 1 | 0 | 1 | sz | 1 | 1 | M | 0 | Vm | Vm | Vm | Vm |

**汇编语法**

```arm
VABS<c><q>.F32
  <Sd>, <Sm>                   // 编码为 sz = 0
VABS<c><q>.F64
  <Dd>, <Dm>                   // 编码为 sz = 1
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Sd>`、`<Sm>`：目的单精度寄存器与操作数单精度寄存器。
* `<Dd>`、`<Dm>`：双精度运算的目的双精度寄存器与操作数双精度寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    ExecuteFPCheck();
    if dp_operation then
        D[d] = FPAbs(D[m]);
    else
        S[d] = FPAbs(S[m]);
```

**异常**：未定义指令。

### 7.225. VADD：浮点加法

浮点加法（Floating-point Add）把两个单精度或双精度寄存器相加，并把结果放入目的寄存器。

**编码专用伪代码**

```arm
dp_operation = (sz == '1');
d = if dp_operation then UInt(D:Vd) else UInt(Vd:D);
n = if dp_operation then UInt(N:Vn) else UInt(Vn:N);
m = if dp_operation then UInt(M:Vm) else UInt(Vm:M);
```

**编码 T1**（FPv4-SP、FPv5；在仅单精度变体中 `sz = 1` 为未定义）：`VADD<c>.F32 <Sd>,<Sn>,<Sm>`、`VADD<c>.F64 <Dd>,<Dn>,<Dm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | D | 1 | 1 | Vn | Vn | Vn | Vn |
| [31:16] | Vd | Vd | Vd | Vd | 1 | 0 | 1 | sz | N | 0 | M | 0 | Vm | Vm | Vm | Vm |

**汇编语法**

```arm
VADD<c><q>.F32
  {<Sd>,} <Sn>, <Sm>           // 编码为 sz = 0
VADD<c><q>.F64
  {<Dd>,} <Dn>, <Dm>           // 编码为 sz = 1
```

where：

* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Sd>`、`<Sn>`、`<Sm>`：目的单精度寄存器与操作数单精度寄存器。
* `<Dd>`、`<Dn>`、`<Dm>`：双精度运算的目的双精度寄存器与操作数双精度寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    ExecuteFPCheck();
    if dp_operation then
        D[d] = FPAdd(D[n], D[m], TRUE);
    else
        S[d] = FPAdd(S[n], S[m], TRUE);
```

**异常**：未定义指令。

浮点异常：输入非规格化（Input Denormal）、无效运算（Invalid Operation）、溢出（Overflow）、下溢（Underflow）、不精确（Inexact）。

### 7.226. VCMP、VCMPE：浮点比较

浮点比较（Floating-point Compare）比较两个寄存器，或一个寄存器与零，并把结果写入 FPSCR 标志。这些标志通常由随后的 `VMRS` 指令传送到 Arm 标志。

若任一操作数为任意类型的 NaN，它可以选择产生无效运算异常。若任一操作数为信号 NaN，它总是产生无效运算异常。

**编码专用伪代码**

```arm
dp_operation = (sz == '1');  quiet_nan_exc = (E == '1');  with_zero = FALSE;
d = if dp_operation then UInt(D:Vd) else UInt(Vd:D);
m = if dp_operation then UInt(M:Vm) else UInt(Vm:M);

dp_operation = (sz == '1');  quiet_nan_exc = (E == '1');  with_zero = TRUE;
d = if dp_operation then UInt(D:Vd) else UInt(Vd:D);
```

**编码 T1**（FPv4-SP、FPv5；在仅单精度变体中 `sz = 1` 为未定义）：`VCMP{E}<c>.F32 <Sd>,<Sm>`、`VCMP{E}<c>.F64 <Dd>,<Dm>`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | D | 1 | 1 | 0 | 1 | 0 | 0 |
| [31:16] | Vd | Vd | Vd | Vd | 1 | 0 | 1 | sz | E | 1 | M | 0 | Vm | Vm | Vm | Vm |

**编码 T2**（FPv4-SP、FPv5；在仅单精度变体中 `sz = 1` 为未定义）：`VCMP{E}<c>.F32 <Sd>,#0.0`、`VCMP{E}<c>.F64 <Dd>,#0.0`

| 位段 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [15:0] | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | D | 1 | 1 | 0 | 1 | 0 | 1 |
| [31:16] | Vd | Vd | Vd | Vd | 1 | 0 | 1 | sz | E | 1 | (0) | 0 | (0) | (0) | (0) | (0) |

**汇编语法**

```arm
VCMP{E}<c><q>.F32
  <Sd>, <Sm>                   // 编码 T1，编码为 sz = 0
VCMP{E}<c><q>.F64
  <Dd>, <Dm>                   // 编码 T1，编码为 sz = 1
VCMP{E}<c><q>.F32
  <Sd>, #0.0                   // 编码 T2，编码为 sz = 0
VCMP{E}<c><q>.F64
  <Dd>, #0.0                   // 编码 T2，编码为 sz = 1
```

where：

* `E`：如果出现，任一 NaN 操作数都会引起无效运算异常，编码为 `E = 1`。否则只有信号 NaN 才引起异常，编码为 `E = 0`。
* `<c><q>`：参见第 A7-177 页的「标准汇编语法字段」。
* `<Sd>`、`<Sm>`：操作数单精度寄存器。
* `<Dd>`、`<Dm>`：操作数双精度寄存器。

**操作**

```arm
if ConditionPassed() then
    EncodingSpecificOperations();
    ExecuteFPCheck();
    if dp_operation then
        op64 = if with_zero then FPZero('0',64) else D[m];
        (FPSCR.N, FPSCR.Z, FPSCR.C, FPSCR.V) = FPCompare(D[d], op64, quiet_nan_exc, TRUE);
    else
        op32 = if with_zero then FPZero('0',32) else S[m];
        (FPSCR.N, FPSCR.Z, FPSCR.C, FPSCR.V) = FPCompare(S[d], op32, quiet_nan_exc, TRUE);
```

**异常**：未定义指令。

浮点异常：无效运算、输入非规格化。

**NaN**：IEEE 754 标准规定比较的结果精确地是 <、==、> 或无序（unordered）之一。如果任一或两个操作数为 NaN，它们是无序的，并且 (Operand1 < Operand2)、(Operand1 == Operand2) 与 (Operand1 > Operand2) 三者都为假。这导致 FPSCR 标志被设置为 N=0、Z=0、C=1、V=1。参见第 A2-37 页的「浮点状态与控制寄存器 FPSCR」。

如果任一操作数为任意类型的 NaN，`VCMPE` 会引起无效运算异常。软件可以使用 `VCMPE` 来测试 <、<=、>、>= 等操作数无序时会引发异常的谓词。
