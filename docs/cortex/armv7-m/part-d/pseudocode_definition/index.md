---
title: "伪代码定义（Pseudocode Definition）"
---

本附录给出本手册所用伪代码的正式定义，并列出伪代码用于执行架构相关工作的一些辅助过程与函数。本章包含以下小节：

* 第 D6-804 页的**指令编码图与伪代码**。
* 第 D6-806 页的**伪代码的限制**。
* 第 D6-807 页的**数据类型**。
* 第 D6-811 页的**表达式**。
* 第 D6-813 页的**运算符与内建函数**。
* 第 D6-818 页的**语句与程序结构**。
* 第 D6-822 页的**其他辅助过程与函数**。

## 1. 指令编码图与伪代码

本手册中的指令描述包含：

* **编码**（**Encoding**）小节，包含一张或多张编码图，每张图后跟一些特定于该编码的伪代码。这些伪代码把编码的字段转换为该指令公共伪代码的输入，并挑出该编码特有的特殊情况。
* **操作**（**Operation**）小节，包含适用于所描述全部编码的公共伪代码。操作小节中的伪代码在开头、或在仅由 `if ConditionPassed() then` 执行一次条件检查之后，调用 `EncodingSpecificOperations()` 函数。

编码图把指令的每一位指定为下列之一：

* 必须为 **0** 或 **1** 的位，在图中表示为 0 或 1。若该位不取此值，则该编码对应另一条指令。
* 应为（**should be**）**0** 或 **1** 的位，在图中表示为 (0) 或 (1)。若该位不取此值，则该指令为 UNPREDICTABLE。
* 具名的单个位，或具名的多位字段中的某一位。

若编码图与指令的所有必须位都相同，则该编码图与该指令**匹配**。

指令的执行模型为：

1. 找出所有与该指令匹配的编码图。有可能没有任何编码图匹配。这种情况下，放弃该执行模型，改为查阅相关指令集章节以确定该指令的处理方式。（此类指令的位模式通常是保留且 UNDEFINED 的，但也有其他可能。例如，未分配的提示（**hint**）指令被记录为保留并按 `NOP` 执行）。
2. 若匹配编码图的操作伪代码以条件检查开头，则执行该条件检查。若条件检查失败，放弃该执行模型并把该指令按 `NOP` 处理。（若有多张匹配的编码图，则它们对应的公共伪代码要么全部、要么全都不以条件检查开头）。
3. 独立且并行地执行每张匹配编码图的特定于编码的伪代码。每段此类伪代码都以位串变量开头，为其对应编码图中每个具名位或多位字段各声明一个，变量名与该位或字段名相同，并以指令位模式中相应位的值初始化。

少数情况下，编码图中含多个同名位或字段。此时这些位或字段的值应全部相同，特定于编码的伪代码会包含一个使用 `Consistent()` 函数的特殊情况，用于规定不满足该条件时的行为。若所有与其参数同名的指令位或字段取值相同，该函数返回 TRUE，否则返回 FALSE。

若有多张匹配的编码图，则除一个之外，所有对应的伪代码段都必须包含一个表示其不适用的特殊情况。丢弃所有此类伪代码段及其对应编码图的结果。

此时只剩一段伪代码及其对应编码图需要考虑。该伪代码也可能包含特殊情况（最常见的是表示 UNPREDICTABLE 的情况）。若是如此，放弃该执行模型并按该特殊情况处理该指令。

4. 把编码图中所有应为位与指令位模式中的对应位比较。若有任何一位不匹配，放弃该执行模型并把该指令按 UNPREDICTABLE 处理。
5. 执行包含该编码图的指令描述中操作伪代码的其余部分。该伪代码以特定于编码的伪代码所留下的变量值作为初值。

公共伪代码中的 `ConditionPassed()` 调用（如存在）执行第 2 步，`EncodingSpecificOperations()` 调用执行第 3、4 步。

### 1.1. 伪代码

伪代码精确描述指令的行为。指令字段以该指令编码图中所示的名字引用。

伪代码在下列小节中详细描述。

## 2. 伪代码的限制

指令功能的伪代码描述有一些限制，主要源于为了清晰与简洁，伪代码是一种顺序的、且在大多数情况下确定性的语言。

这些限制包括：

* 当一条指令产生多次内存访问时，伪代码不描述其顺序要求。关于内存访问顺序要求的描述参见第 A3-89 页的**内存访问顺序**。
* 当未定义指令的条件检查失败时，伪代码不描述确切的规则。这种情况下，UNDEFINED 伪代码语句位于 `if ConditionPassed() then ...` 结构内部，要么直接位于其中，要么在 `EncodingSpecificOperations()` 函数调用内部，因此伪代码表示该指令按 `NOP` 执行。更多信息参见第 A7-179 页的**未定义指令的条件执行**。
* 伪代码语句 `UNDEFINED`、`UNPREDICTABLE` 与 `SEE` 表示的行为与正在执行的伪代码所表示的行为不同。若遇到其中之一：
    * 伪代码所表示的先前行为，仅在确定该语句被执行所需的范围内被规定为发生。
    * 伪代码所表示的后续行为不再发生。也就是说，这些语句终止伪代码的执行。

更多信息参见第 D6-818 页的**简单语句**。

## 3. 数据类型

本小节描述：

* **通用数据类型规则**。
* **位串**。
* 第 D6-808 页的**整数**。
* 第 D6-808 页的**实数**。
* 第 D6-808 页的**布尔**。
* 第 D6-808 页的**枚举**。
* 第 D6-808 页的**列表**。
* 第 D6-809 页的**数组**。

### 3.1. 通用数据类型规则

Arm 体系结构伪代码是一种强类型语言。每个常量与变量都属于下列类型之一：

* 位串（**Bitstring**）。
* 整数（**Integer**）。
* 布尔（**Boolean**）。
* 实数（**Real**）。
* 枚举（**Enumeration**）。
* 列表（**List**）。
* 数组（**Array**）。

常量的类型由语法决定。变量的类型通常由赋值决定：变量被隐式声明为与赋给它的值相同的类型。例如，赋值 `x = 1`、`y = '1'` 与 `z = TRUE` 分别隐式声明变量 `x`、`y` 与 `z` 的类型为 integer、长度为 1 的 bitstring 与 Boolean。

也可以在变量名前加上类型名，显式声明变量的类型。这最常用于函数定义中声明参数与函数结果的类型。

下列小节更详细地描述这些数据类型。

### 3.2. 位串

位串（**bitstring**）是由 0 和 1 构成的有限长度字符串。每一种长度的位串是不同的类型。位串允许的最小长度为 1。

长度为 N 的位串的类型名为 `bits(N)`。`bits(1)` 的同义词是 `bit`。

位串常量写作一个单引号、后跟 0 和 1 构成的字符串、再跟一个单引号。例如，类型为 `bit` 的两个常量是 `'0'` 与 `'1'`。为清晰起见，位串中可以包含空格。

位串比较中允许使用含 "x" 位的特殊形式位串常量，详情参见第 D6-813 页的**相等与不等测试**。

每个位串值都有从左到右的顺序，位按标准的**小端序**编号，即长度为 N 的位串最左位是 bit N-1，最右位是 bit 0。在与整数相互转换时，该顺序用作从最高有效位到最低有效位的顺序。对位串常量以及由编码图导出的位串，该顺序与它们的书写形式一致。

位串是伪代码中唯一的**具体**（**concrete**）数据类型，即它直接对应寄存器、内存位置与指令的内容。其余数据类型都是抽象的。

### 3.3. 整数

伪代码整数大小无界，可为正或负。也就是说，它们是数学整数，而不是计算机语言与体系结构通常所说的整数。计算机整数在伪代码中表示为适当长度的位串，并配以把这些位串解释为整数的相应函数。

整数的类型名为 `integer`。

整数常量通常用十进制书写，例如 `0`、`15`、`-1234`；也可以用 C 风格的十六进制书写，例如 `0x55` 或 `0x80000000`。十六进制整数常量按正数处理，除非前面有负号。例如，`0x80000000` 是整数 +2³¹。若需用十六进制书写 -2³¹，应写作 `-0x80000000`。

### 3.4. 实数

伪代码实数的大小与精度无界。也就是说，它们是数学实数，而不是计算机浮点数。计算机浮点数在伪代码中表示为适当长度的位串，并配以把这些位串解释为实数的相应函数。

实数的类型名为 `real`。

实数常量用带小数点的十进制书写（因此 `0` 是整数常量，而 `0.0` 是实数常量）。

### 3.5. 布尔

布尔（**Boolean**）是逻辑真或假的值。

布尔的类型名为 `boolean`。它与 `bit`（长度为 1 的位串）不是同一类型。布尔常量为 `TRUE` 与 `FALSE`。

### 3.6. 枚举

枚举（**enumeration**）是一组已定义的符号常量，例如：

```arm
enumeration SRType (SRType_None, SRType_LSL, SRType_LSR, SRType_ASR, SRType_ROR, SRType_RRX);
```

枚举至少包含一个符号常量，且符号常量不允许在枚举之间共享。

枚举必须显式声明，但枚举类型的变量可以像通常那样通过把某个符号常量赋给它来隐式声明。按约定，每个符号常量以枚举名后跟下划线开头。枚举名即其类型名，符号常量即其可能的常量。

**注意：** 布尔本质上是一个预先声明的枚举：

```arm
enumeration boolean {FALSE, TRUE};
```

它不遵循通常的命名约定，并在某些伪代码构造（例如 `if` 语句）中具有特殊作用。

列表（**list**）是其他数据项的有序集合，各项之间用逗号分隔并括在圆括号中，例如：

```arm
(bits(32) shifter_result, bit shifter_carry_out)
```

列表至少包含一个数据项。

### 3.7. 列表

列表常用作返回多个结果的函数的返回类型。例如，当函数 `Shift_C()` 的第一个操作数为 `bits(32)` 类型时，该列表就是执行标准 Arm 移位或循环移位的该函数的返回类型。

某些特定的伪代码运算符使用以其他括号形式包围的列表，包括：

* **位串提取**运算符，使用以尖括号 `&lt;...&gt;` 包围的位编号或位编号范围列表。
* **数组索引**，使用以方括号 `[...]` 包围的数组索引列表。
* **类数组函数的参数传递**，使用以方括号 `[...]` 包围的函数参数列表。

列表中数据类型的每一种组合都是单独的类型，其类型名就是按顺序列出各数据类型（即上例中的 `(bits(32),bit)`）。类型可以由赋值声明这一通用原则，也适用于列表中各个列表项的类型。例如：

```arm
(shift_t, shift_n) = ('00', 0);
```

隐式声明 `shift_t`、`shift_n` 与 `(shift_t,shift_n)` 的类型分别为 `bits(2)`、`integer` 与 `(bits(2),integer)`。

列表类型也可以显式命名，并为列表中的元素显式命名。例如：

```arm
type ShiftSpec is (bits(2) shift, integer amount);
```

完成该定义并声明：

```arm
ShiftSpec abc;
```

之后，所得列表的元素可以用 `abc.shift` 与 `abc.amount` 引用。这种对列表元素的限定命名，只允许用于显式声明的变量，不允许用于仅通过赋值声明的变量。

显式命名一个类型并不改变该类型本身。例如，在定义 `ShiftSpec` 之后，`ShiftSpec` 与 `(bits(2),integer)` 是同一类型的两个不同名字，而不是两个不同类型的名字。为避免引用列表元素时出现歧义，若使用其类型的不同名字多次声明同一个列表变量，或使用与其声明所用名字不对应的列表元素名对其进行限定，则属于错误。

被赋值的列表中的某一项可以写作 `-`，表示丢弃所赋值列表中对应的项。例如：

```arm
(shifted, -) = LSL_C(operand, amount);
```

列表常量写作相应类型常量的列表，如上例中的 `('00', 0)`。

### 3.8. 数组

伪代码数组以下列两种方式索引：枚举，或整数范围。整数范围由范围的闭合下端、`..`、范围的闭合上端依次表示。例如：

```arm
enumeration PhysReg { PhysReg_R0,    PhysReg_R1,     PhysReg_R2,    PhysReg_R3,
                      PhysReg_R4,    PhysReg_R5,     PhysReg_R6,    PhysReg_R7,
                      PhysReg_R8,    PhysReg_R9,     PhysReg_R10,   PhysReg_R11,
                      PhysReg_R12,   PhysReg_SP_Process,            PhysReg_SP_Main,
                      PhysReg_LR,    PhysReg_PC};
array bits(32) _R[PhysReg];
array bits(8) _Memory[0..0xFFFFFFFF];
```

数组总是显式声明，且没有常量数组的表示法。数组至少包含一个元素，因为枚举至少包含一个符号常量，整数范围至少包含一个整数。

数组通常不直接出现在伪代码中。伪代码中语法上像数组的项通常是 `R[i]`、`MemU[address,size]` 或 `Element[i,type]` 之类的类数组函数。这些函数封装并抽象了对底层数组访问时通常执行的附加操作，例如寄存器分组、内存保护、端序相关的字节排序、独占访问的簿记以及向量元素处理。

## 4. 表达式

本小节描述：

* **通用表达式语法**。
* **运算符与函数的多态与原型**。
* 第 D6-812 页的**优先级规则**。

### 4.1. 通用表达式语法

表达式为下列之一：

* 常量。
* 变量，可选择在其前面加类型名以声明其类型。
* 在类型名后跟 `UNKNOWN` 以声明其类型。
* 把语言定义的运算符作用于其他表达式的结果。
* 把函数作用于其他表达式的结果。

变量名通常由字母数字与下划线字符构成，并以字母或下划线开头。

正文中描述的每个寄存器都应视为声明了一个同名的位串变量，该变量具有该寄存器所述的行为。例如，若某寄存器的某位被描述为读出为 0 且忽略写入，则该变量对应的位也读出为 0 且忽略写入。

`bits(32) UNKNOWN` 之类的表达式表示表达式的结果是给定类型的值，但体系结构不规定其具体取值，软件不得依赖此类值。产生的值不得构成安全漏洞，也不得声称向软件提供任何有用信息。（在早期的 Arm 体系结构文档中，这称为 UNPREDICTABLE 值。它与 UNPREDICTABLE 相关但不相同，后者表示整个体系结构状态同样变为未指定。）

一部分表达式是**可赋值的**（**assignable**），即可以放在赋值的左侧。这一部分包括：

* 变量。
* 把某些运算符作用于其他表达式的结果。每个能够产生可赋值表达式的语言定义运算符，都在其描述中规定产生可赋值表达式的条件。（例如，这些条件可能包括该运算符所作用的表达式本身是或不是可赋值表达式）。
* 把类数组函数作用于其他表达式的结果。类数组函数的描述规定其能够产生可赋值表达式的条件。

每个表达式都有数据类型。类型由下列因素决定：

* 对常量，由常量的语法决定。
* 对变量，可能来自三个来源：
    * 其前面可选的类型名。
    * 伪代码中先前通过递归应用本规则给它指定的类型。
    * 通过赋值给它指定的类型（可以是直接对它赋值，或对包含它的列表赋值）。

若变量不存在上述任何类型来源，或存在多个来源但它们给出的类型不一致，则属于伪代码错误。

* 对语言定义的运算符，由该运算符的定义决定。
* 对函数，由该函数的定义决定。

### 4.2. 运算符与函数的多态与原型

伪代码中的运算符与函数可以是**多态**的（**polymorphic**），对不同数据类型产生不同功能。运算符或函数由此得到的每一种形式都有不同的原型定义。例如，运算符 `+` 有作用于整数、实数与位串多种组合的形式。

一种特别常见的多态形式是不同长度位串之间的多态，在原型定义中用 `bits(N)`、`bits(M)` 等表示。

### 4.3. 优先级规则

表达式的优先级规则为：

1. 常量、变量与函数调用在求值时优先于任何使用其结果作为操作数的运算符。
2. 整数表达式遵循通常的优先级规则，即幂运算优先于乘除、乘除优先于加减；连续乘除或连续加减按从左到右求值。
3. 其他表达式在可能出现歧义时必须加括号以表明运算符优先级；若按类型规则所有可能的优先级顺序必然得出相同结果，则不必加括号。例如，若 `i`、`j` 与 `k` 是整数变量，则 `i &gt; 0 &amp;&amp; j &gt; 0 &amp;&amp; k &gt; 0` 可以接受，而 `i &gt; 0 &amp;&amp; j &gt; 0 || k &gt; 0` 不可以。

## 5. 运算符与内建函数

本小节描述：

* **通用类型上的运算**。
* **布尔运算**。
* **位串操作**。
* 第 D6-816 页的**算术**。

### 5.1. 通用类型上的运算

下列运算对所有类型都有定义。

#### 5.1.1. 相等与不等测试

同一类型的任意两个值 `x` 与 `y`，可以用表达式 `x == y` 测试相等，用表达式 `x != y` 测试不相等。两种情况下结果都是 **Boolean** 类型。

允许使用一种特殊形式的比较：与同时包含 "x" 位和 `'0'`、`'1'` 位的位串常量比较。在确定比较结果时，与 "x" 位对应的位被忽略。例如，若 `opcode` 是 4 位位串，则 `opcode == '1x0x'` 等价于 `opcode&lt;3&gt; == '1' &amp;&amp; opcode&lt;1&gt; == '0'`。`case ... of ...` 结构 `when` 部分中的隐式相等比较也允许使用该特殊形式。

伪代码用 `"…"` 引号而不是 `'…'` 引号包围这种特殊形式的常量以示区别，如表 D6-1 所示。

表 D6-1 含与不含无关位的位串的约定：

| 字符串类型 | 所用引号 | 示例 |
| --- | --- | --- |
| 位串 | `'…'` | `'1101'` |
| 含无关位的位串 | `"…"` | `"1x0x"` |

#### 5.1.2. 条件选择

若 `x` 与 `y` 是同一类型的两个值，`t` 是 **Boolean** 类型的值，则 `if t then x else y` 是与 `x`、`y` 同类型的表达式：`t` 为 TRUE 时产生 `x`，为 FALSE 时产生 `y`。

### 5.2. 布尔运算

若 `x` 是 **Boolean**，则 `!x` 是其逻辑取反。

若 `x` 与 `y` 是布尔值，则 `x &amp;&amp; y` 是把二者相与的结果。与 C 语言一样，若 `x` 为 FALSE，则不求值 `y` 而直接确定结果为 FALSE。

若 `x` 与 `y` 是布尔值，则 `x || y` 是把二者相或的结果。与 C 语言一样，若 `x` 为 TRUE，则不求值 `y` 而直接确定结果为 TRUE。

若 `x` 与 `y` 是布尔值，则 `x ^ y` 是把二者相异或的结果。

### 5.3. 位串操作

下列位串操作函数有定义：

#### 5.3.1. 位串长度与最高位

若 `x` 是位串，则位串长度函数 `Len(x)` 返回其长度（整数），`TopBit(x)` 是 `x` 的最左位（即使用位串提取得到的 `x&lt;Len(x)-1&gt;`）。

#### 5.3.2. 位串拼接与复制

若 `x` 与 `y` 分别是长度为 N 与 M 的位串，则 `x:y` 是按从左到右顺序拼接 `x` 与 `y` 得到的长度为 N+M 的位串。

若 `x` 是位串，`n` 是满足 `n &gt; 0` 的整数，则 `Replicate(x,n)` 是由 n 个 `x` 副本拼接而成的、长度为 `n*Len(x)` 的位串，且：

```arm
Zeros(n) = Replicate('0',n)
Ones(n)  = Replicate('1',n)
```

#### 5.3.3. 位串提取

位串提取运算符从另一个位串或整数中提取出位串。其语法为 `x&lt;integer_list&gt;`，其中 `x` 是被提取的整数或位串，`&lt;integer_list&gt;` 是用尖括号而不是通常的圆括号包围的整数列表。所得位串的长度等于 `&lt;integer_list&gt;` 中整数的个数。在 `x&lt;integer_list&gt;` 中，`&lt;integer_list&gt;` 的每个整数必须：

* 大于等于 0。
* 若 `x` 是位串，则小于 `Len(x)`。

`x&lt;integer_list&gt;` 的定义取决于 `integer_list` 是否含多个整数。若含多个，`x&lt;i,j,k,...,n&gt;` 定义为拼接：

```arm
x<i> : x<j> : x<k> : ... : x<n>
```

若 `integer_list` 只含一个整数 i，则 `x&lt;i&gt;` 定义为：

* 若 `x` 是位串，则 `x` 的 bit i 为 0 时取 `'0'`，为 1 时取 `'1'`。
* 若 `x` 是整数，令 `y` 为 0 到 2^(i+1)-1 范围内唯一与 `x` 模 2^(i+1) 同余的整数，则 `y &lt; 2^i` 时 `x&lt;i&gt;` 为 `'0'`，否则为 `'1'`。

粗略地说，第二种定义把整数视为与其足够长的二进制补码位串表示等价。

在 `&lt;integer_list&gt;` 中，`i:j` 在 `i &gt;= j` 时是从 i 递减到 j（两端含）的整数的简写。例如，`instr&lt;31:28&gt;` 是 `instr&lt;31,30,29,28&gt;` 的简写。

表达式 `x&lt;integer_list&gt;` 可赋值，条件是 `x` 是可赋值位串，且 `&lt;integer_list&gt;` 中没有整数重复出现。特别地，若 `x` 是可赋值位串且 `0 &lt;= i &lt; Len(x)`，则 `x&lt;i&gt;` 可赋值。

寄存器的编码图经常标出具名位或多位字段。例如，APSR 的编码图把其 `bit&lt;31&gt;` 标为 N。这种情况下，使用语法 `APSR.N` 作为 `APSR&lt;31&gt;` 的更易读的同义词。

#### 5.3.4. 位串的逻辑运算

若 `x` 是位串，`NOT(x)` 是把 `x` 的每一位逻辑取反得到的同长度位串。

若 `x` 与 `y` 是长度相同的位串，则 `x AND y`、`x OR y` 与 `x EOR y` 分别是把 `x` 与 `y` 的对应位逻辑相与、相或、相异或得到的同长度位串。

#### 5.3.5. 位串计数

若 `x` 是位串，`BitCount(x)` 产生一个整数结果，等于 `x` 中值为 1 的位的个数。

#### 5.3.6. 测试位串是否全零或全一

若 `x` 是位串，则 `x` 的所有位为零时 `IsZero(x)` 产生 TRUE，任一位为 1 时产生 FALSE；`x` 的所有位为零时 `IsZeroBit(x)` 产生 `'1'`，任一位为 1 时产生 `'0'`。`IsOnes(x)` 与 `IsOnesBit(x)` 的行为与之对应。即：

```arm
IsZero(x)    = (BitCount(x) == 0)
IsOnes(x)    = (BitCount(x) == Len(x))
IsZeroBit(x) = if IsZero(x) then '1' else '0'
IsOnesBit(x) = if IsOnes(x) then '1' else '0'
```

#### 5.3.7. 位串的最低与最高置位

若 `x` 是位串，且 `N = Len(x)`：

* `LowestSetBit(x)` 是其值为 1 的位中最小的位编号。若所有位为零，则 `LowestSetBit(x) = N`。
* `HighestSetBit(x)` 是其值为 1 的位中最大的位编号。若所有位为零，则 `HighestSetBit(x) = -1`。
* `CountLeadingZeroBits(x) = N - 1 - HighestSetBit(x)`，即 `x` 左端的零位个数，范围为 0 到 N。
* `CountLeadingSignBits(x) = CountLeadingZeroBits(x&lt;N-1:1&gt; EOR x&lt;N-2:0&gt;)`，即 `x` 左端符号位的副本个数（不含符号位本身），范围为 0 到 N-1。

#### 5.3.8. 位串的零扩展与符号扩展

若 `x` 是位串，`i` 是整数，则 `ZeroExtend(x,i)` 是通过在其左侧添加足够多的零位把 `x` 扩展到 i 位。即若 `i == Len(x)`，则 `ZeroExtend(x,i) = x`；若 `i &gt; Len(x)`，则：

```arm
ZeroExtend(x,i) = Zeros(i-Len(x)) : x
```

若 `x` 是位串，`i` 是整数，则 `SignExtend(x,i)` 是通过在其左侧添加足够多的最左位副本把 `x` 扩展到 i 位。即若 `i == Len(x)`，则 `SignExtend(x,i) = x`；若 `i &gt; Len(x)`，则：

```arm
SignExtend(x,i) = Replicate(TopBit(x), i-Len(x)) : x
```

在可能出现 `i &lt; Len(x)` 的上下文中使用 `ZeroExtend(x,i)` 或 `SignExtend(x,i)`，属于伪代码错误。

#### 5.3.9. 位串转换为整数

若 `x` 是位串，`SInt(x)` 是以 `x` 为二进制补码表示的整数：

```arm
// SInt()
// ======
integer SInt(bits(N) x)
    result = 0;
    for i = 0 to N-1
        if x<i> == '1' then
            result = result + 2^i;
    if x<N-1> == '1' then
        result = result - 2^N;
    return result;
```

`UInt(x)` 是以 `x` 为无符号表示的整数：

```arm
// UInt()
// ======
integer UInt(bits(N) x)
    result = 0;
    for i = 0 to N-1
        if x<i> == '1' then
            result = result + 2^i;
    return result;
```

`Int(x, unsigned)` 根据第二个参数的值返回 `SInt(x)` 或 `UInt(x)`：

```arm
// Int()
// =====
integer Int(bits(N) x, boolean unsigned)
    result = if unsigned then UInt(x) else SInt(x);
    return result;
```

### 5.4. 算术

伪代码中的算术大多在整数或实数上进行，操作数由位串转换而来，结果之后再转换回位串。由于这些数据类型是无界的数学类型，不存在溢出之类的问题。

#### 5.4.1. 一元正号、负号与绝对值

若 `x` 是整数或实数，则 `+x` 是 `x` 本身，`-x` 是符号取反的 `x`，`ABS(x)` 是 `x` 的绝对值。三者都与 `x` 类型相同。

#### 5.4.2. 加法与减法

若 `x` 与 `y` 是整数或实数，`x+y` 与 `x-y` 是它们的和与差。`x` 与 `y` 都是 `integer` 类型时二者为 integer 类型，否则为 real 类型。

加法和减法是伪代码中特别常见的算术运算，因此也便于定义直接作用于位串操作数的加法与减法。

若 `x` 与 `y` 是长度相同（`N = Len(x) = Len(y)`）的位串，则 `x+y` 与 `x-y` 是把它们转换为整数后相加或相减所得结果的低 N 位。有符号与无符号转换产生相同结果：

```arm
x+y = (SInt(x) + SInt(y))<N-1:0> = (UInt(x) + UInt(y))<N-1:0>
x-y = (SInt(x) - SInt(y))<N-1:0> = (UInt(x) - UInt(y))<N-1:0>
```

若 `x` 是长度为 N 的位串、`y` 是整数，`x+y` 与 `x-y` 是长度为 N 的位串，定义为 `x+y = x + y&lt;N-1:0&gt;` 与 `x-y = x - y&lt;N-1:0&gt;`。类似地，若 `x` 是整数、`y` 是长度为 M 的位串，`x+y` 与 `x-y` 是长度为 M 的位串，定义为 `x+y = x&lt;M-1:0&gt; + y` 与 `x-y = x&lt;M-1:0&gt; - y`。

#### 5.4.3. 比较

若 `x` 与 `y` 是整数或实数，则 `x == y`、`x != y`、`x &lt; y`、`x &lt;= y`、`x &gt; y` 与 `x &gt;= y` 分别是二者之间的等于、不等于、小于、小于等于、大于、大于等于比较，产生布尔结果。对 `==` 与 `!=`，这扩展了适用于同类型任意两个值的通用定义，使其也可作用于整数与实数之间。

#### 5.4.4. 乘法

若 `x` 与 `y` 是整数或实数，`x * y` 是 `x` 与 `y` 的积；`x` 与 `y` 都是 integer 类型时为 integer 类型，否则为 `real` 类型。

#### 5.4.5. 除法与取模

若 `x` 与 `y` 是整数或实数，`x / y` 是 `x` 除以 `y` 的结果，总是 **real** 类型。

若 `x` 与 `y` 是整数，`x DIV y` 与 `x MOD y` 定义为：

```arm
x DIV y = RoundDown(x / y)
```

```arm
x MOD y = x - y * (x DIV y)
```

在 `y` 可能为零的任何上下文中使用 `x / y`、`x MOD y` 或 `x DIV y`，属于伪代码错误。

#### 5.4.6. 平方根

若 `x` 是整数或实数，`Sqrt(x)` 是其平方根，总是 **real** 类型。

#### 5.4.7. 舍入与对齐

若 `x` 是实数：

* `RoundDown(x)` 产生满足 `n &lt;= x` 的最大整数 n。
* `RoundUp(x)` 产生满足 `n &gt;= x` 的最小整数 n。
* `RoundTowardsZero(x)` 在 `x &gt; 0.0` 时产生 `RoundDown(x)`，在 `x == 0.0` 时产生 0，在 `x &lt; 0.0` 时产生 `RoundUp(x)`。

若 `x` 与 `y` 是整数，`Align(x,y) = y * (x DIV y)` 是整数。

若 `x` 是位串、`y` 是整数，`Align(x,y) = (Align(UInt(x),y))&lt;Len(x)-1:0&gt;` 是与 `x` 长度相同的位串。

在 `y` 可能为 0 的任何上下文中使用任一形式的 `Align(x,y)`，属于伪代码错误。实际使用中 `Align(x,y)` 的 `y` 总是 2 的幂常量，而 `y = 2^n` 的位串形式的效果是使其参数的低 n 位强制为零。

#### 5.4.8. 缩放

若 `n` 是整数，`2^n` 是把 2 提升到 n 次幂的结果，为 **real** 类型。

若 `x` 与 `n` 是整数，则：

* `x &lt;&lt; n = RoundDown(x * 2^n)`。
* `x &gt;&gt; n = RoundDown(x * 2^(-n))`。

#### 5.4.9. 最大值与最小值

若 `x` 与 `y` 是整数或实数，`Max(x,y)` 与 `Min(x,y)` 分别是它们的最大值与最小值。`x` 与 `y` 都是 integer 类型时二者为 integer 类型，否则为 real 类型。

## 6. 语句与程序结构

本小节描述伪代码中使用的控制语句。

### 6.1. 简单语句

下列简单语句都必须以分号结尾，如下所示。

#### 6.1.1. 赋值

赋值语句的形式为：

```arm
<assignable_expression> = <expression>;
```

#### 6.1.2. 过程调用

过程调用的形式为：

```arm
<procedure_name>(<arguments>);
```

#### 6.1.3. 返回语句

过程的返回形式为：

```arm
return;
```

函数的返回形式为：

```arm
return <expression>;
```

其中 `&lt;expression&gt;` 的类型为函数原型行所声明的类型。

#### 6.1.4. UNDEFINED

语句：

```arm
UNDEFINED;
```

表示一个特殊情况，它取代当前伪代码所定义的行为（确定该特殊情况适用所需的行为除外）。取代后的行为是采用**未定义指令**（**Undefined Instruction**）异常。

#### 6.1.5. UNPREDICTABLE

语句：

```arm
UNPREDICTABLE;
```

表示一个特殊情况，它取代当前伪代码所定义的行为（确定该特殊情况适用所需的行为除外）。取代后的行为不由体系结构定义，软件不得依赖。它不得构成安全漏洞，不得使系统停止或挂起，也不得声称向软件提供任何有用信息。

#### 6.1.6. SEE...

语句：

```arm
SEE <reference>;
```

表示一个特殊情况，它取代当前伪代码所定义的行为（确定该特殊情况适用所需的行为除外）。取代后的行为是：由于另一段伪代码已定义所需行为，当前伪代码不产生任何结果。`&lt;reference&gt;` 指出那段伪代码的位置。

#### 6.1.7. IMPLEMENTATION_DEFINED

语句：

```arm
IMPLEMENTATION_DEFINED <text>;
```

表示一个特殊情况，规定该行为为实现定义（**IMPLEMENTATION DEFINED**）。其后的文本可以给出更多信息。

### 6.2. 复合语句

复合语句通常用缩进表示结构。`if ... then ... else ...` 或过程、函数定义等结构中所含的语句，比该语句本身缩进更深，其结束由缩进回到原层级或更浅的层级表示。

每一级缩进通常为四个空格。

#### 6.2.1. 条件语句 if ... then ... else ...

多行的 `if ... then ... else ...` 结构形式为：

```arm
if <boolean_expression> then
    <statement 1>
    <statement 2>
    ...
    <statement n>
else
    <statement A>
    <statement B>
    ...
    <statement Z>
```

`else` 及其后续语句是可选的。

```arm
if <boolean_expression> then
    <statement 1>
    <statement 2>
    ...
    <statement n>
elsif <boolean_expression> then
    <statement a>
    <statement b>
    ...
    <statement z>
else
    <statement A>
    <statement B>
    ...
    <statement Z>
```

由 `elsif` 及其缩进语句构成的行块是可选的，并且可以使用多个这样的块。

由 `else` 及其缩进语句构成的块是可选的。

当 `then` 部分（以及 `else` 部分，如有）只含简单语句时，可以使用如下缩写的一行形式：

```arm
if <boolean_expression> then <statement 1>
if <boolean_expression> then <statement 1> else <statement A>
if <boolean_expression> then <statement 1> <statement 2> else <statement A>
```

**注意：** 这些形式中 `&lt;statement 1&gt;`、`&lt;statement 2&gt;` 与 `&lt;statement A&gt;` 必须以分号结尾。这一点以及 `else` 部分是可选的，都是与 `if ... then ... else ...` **表达式**的不同之处。

#### 6.2.2. 循环语句 repeat ... until ...

`repeat ... until ...` 结构的形式为：

```arm
repeat
    <statement 1>
    <statement 2>
    ...
    <statement n>
until <boolean_expression>;
```

#### 6.2.3. 循环语句 while ... do

`while ... do` 结构的形式为：

```arm
while <boolean_expression> do
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

#### 6.2.4. 循环语句 for ...

`for ...` 结构的形式为：

```arm
for <assignable_expression> = <integer_expr1> to <integer_expr2>
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

#### 6.2.5. 分支语句 case ... of ...

`case ... of ...` 结构的形式为：

```arm
case <expression> of
    when <constant values>
        <statement 1>
        <statement 2>
        ...
        <statement n>
    ... more "when" groups ...
    otherwise
        <statement A>
        <statement B>
        ...
        <statement Z>
```

其中 `&lt;constant values&gt;` 由一个或多个与 `&lt;expression&gt;` 同类型的常量值构成，之间用逗号分隔。`when` 与 `otherwise` 部分只含简单语句时，可以使用缩写的一行形式。

若 `&lt;expression&gt;` 是位串类型，`&lt;constant values&gt;` 中也可以包含含 "x" 位的位串常量。详情参见第 D6-813 页的**相等与不等测试**。

#### 6.2.6. 过程与函数定义

过程定义的形式为：

```arm
<procedure name>(<argument prototypes>)
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

其中 `&lt;argument prototypes&gt;` 由零个或多个参数定义构成，之间用逗号分隔。每个参数定义由一个类型名后跟参数名构成。

**注意：** 这第一行原型行不以分号结尾。这有助于把它与过程调用区分开。

函数定义与之类似，但还要声明函数的返回类型：

```arm
<return type> <function name>(<argument prototypes>)
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

类数组函数与之类似，但使用方括号：

```arm
<return type> <function name>[<argument prototypes>]
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

类数组函数通常还有一个赋值原型：

```arm
<function name>[<argument prototypes>] = <value prototypes>
    <statement 1>
    <statement 2>
    ...
    <statement n>
```

### 6.3. 注释

伪代码注释有两种风格：

* `//` 开始一条以行尾结束的注释。
* `/*` 开始一条以 `*/` 结束的注释。

## 7. 其他辅助过程与函数

本小节描述的函数不属于伪代码规范。它们是伪代码用来执行有用的架构相关工作的辅助过程与函数。每个都有一个简短描述与一个伪代码原型，其中一些附有伪代码定义。

### 7.1. ArchVersion()

该函数返回体系结构的主版本号。

```arm
integer ArchVersion()
```

### 7.2. BKPTInstrDebugEvent()

该过程为 `BKPT` 指令产生一个调试事件。

### 7.3. BreakPoint()

该过程使一个调试点（**debug breakpoint**）发生。

### 7.4. CallSupervisor()

在 M 配置文件中，该过程产生 **SVCall** 异常。

### 7.5. ConditionPassed()

该函数执行指令的条件测试，依据为：

* **Thumb** 条件分支的两种编码（`B` 指令的编码 T1 与 T3）。
* 其他 **Thumb** 指令下 xPSR.IT[7:0] 的当前值。

```arm
Boolean ConditionPassed()
```

### 7.6. ConsumptionOfSpeculativeDataBarrier()

该函数执行一条 `CSDB` 指令。

```arm
ConsumptionOfSpeculativeDataBarrier()
```

### 7.7. Coproc_Accepted()

该函数确定协处理器是否接受某条指令。

```arm
Boolean Coproc_Accepted(integer cp_num, bits(32) instr)
```

### 7.8. Coproc_DoneLoading()

该函数确定对 `LDC` 指令而言是否已加载足够多的字。

```arm
Boolean Coproc_DoneLoading(integer cp_num, bits(32) instr)
```

### 7.9. Coproc_DoneStoring()

该函数确定对 `STC` 指令而言是否已存储足够多的字。

```arm
Boolean Coproc_DoneStoring(integer cp_num, bits(32) instr)
```

### 7.10. Coproc_GetOneWord()

该函数从协处理器取得 `MRC` 指令所需的字。

```arm
bits(32) Coproc_GetOneWord(integer cp_num, bits(32) instr)
```

### 7.11. Coproc_GetTwoWords()

该函数从协处理器取得 `MRRC` 指令所需的两个字。

```arm
(bits(32), bits(32)) Coproc_GetTwoWords(integer cp_num, bits(32) instr)
```

### 7.12. Coproc_GetWordToStore()

该函数从协处理器取得 `STC` 指令所需存储的下一个字。

```arm
bits(32) Coproc_GetWordToStore(integer cp_num, bits(32) instr)
```

### 7.13. Coproc_InternalOperation()

该过程指示协处理器执行 `CDP` 指令所请求的内部操作。

```arm
Coproc_InternalOperation(integer cp_num, bits(32) instr)
```

### 7.14. Coproc_SendLoadedWord()

该过程把 `LDC` 指令所加载的一个字发送给协处理器。

```arm
Coproc_SendLoadedWord(bits(32) word, integer cp_num, bits(32) instr)
```

### 7.15. Coproc_SendOneWord()

该过程把 `MCR` 指令所需的字发送给协处理器。

```arm
Coproc_SendOneWord(bits(32) word, integer cp_num, bits(32) instr)
```

### 7.16. Coproc_SendTwoWords()

该过程把 `MCRR` 指令所需的两个字发送给协处理器。

```arm
Coproc_SendTwoWords(bits(32) word1, bits(32) word2, integer cp_num, bits(32) instr)
```

### 7.17. DataMemoryBarrier()

该过程产生一次**数据内存屏障**（**Data Memory Barrier**）。

```arm
DataMemoryBarrier(bits(4) option)
```

### 7.18. DataSynchronizationBarrier()

该过程执行一次**数据同步屏障**（**Data Synchronization Barrier**）。

```arm
DataSynchronizationBarrier(bits(4) option)
```

### 7.19. EncodingSpecificOperations()

该过程调用某条指令编码的特定于编码的伪代码，并检查编码的“应为”位，参见第 D6-804 页的**指令编码图与伪代码**。

### 7.20. GenerateCoprocessorException()

该过程为被拒绝的协处理器指令引发 **UsageFault** 异常。

### 7.21. GenerateIntegerZeroDivide()

该过程为整数除法指令 `SDIV` 与 `UDIV` 中的除零引发相应异常。

在 M 配置文件中，这是 **UsageFault** 异常。

### 7.22. HaveDSPExt()

该过程在实现包含 **DSP** 扩展时返回 TRUE。

```arm
boolean HaveDSPExt()
```

### 7.23. HaveFPExt()

该过程在实现包含**浮点**（**floating-point**，**FP**）扩展时返回 TRUE。

```arm
boolean HaveFPExt()
```

### 7.24. Hint_Debug()

该过程向调试系统提供一个提示（**hint**）。

```arm
Hint_Debug(bits(4) option)
```

### 7.25. Hint_PreloadData()

该过程执行一次数据预加载提示。

```arm
Hint_PreloadData(bits(32) address)
```

### 7.26. Hint_PreloadInstr()

该过程执行一次指令预加载提示。

```arm
Hint_PreloadInstr(bits(32) address)
```

### 7.27. Hint_SendEvent()

该过程执行一次发送事件（**send event**）提示。

### 7.28. Hint_Yield()

该过程执行一次 **Yield** 提示。

### 7.29. InstructionSynchronizationBarrier()

该过程产生一次**指令同步屏障**（**Instruction Synchronization Barrier**）。

```arm
InstructionSynchronizationBarrier(bits(4) option)
```

### 7.30. IntegerZeroDivideTrappingEnabled()

该函数在整数除法指令 `SDIV` 与 `UDIV` 中的除零陷阱已使能时返回 TRUE，否则返回 FALSE。

在 M 配置文件中，这由**配置控制寄存器**（**Configuration Control register**）中的 DIV_0_TRP 位控制：该位为 1 时返回 TRUE，为 0 时返回 FALSE。

### 7.31. ProcessorID()

标识正在执行的处理器。

### 7.32. ResetSCSRegs()

把**系统控制空间**（**System Control Space**，**SCS**）中所有具有体系结构定义的复位值的寄存器恢复为这些值。

```arm
ResetSCSRegs()
```

### 7.33. SetPending()

该过程把关联的异常状态置为 **Pending**。关于不同异常状态的定义参见第 B1-513 页的**异常**。

### 7.34. SerializeVFP()

该过程确保先前浮点指令中的任何异常条件都已被检测到。

### 7.35. SpeculativeSynchronizationBarrierToPA()

该函数执行一条 `PSSBB` 指令。

```arm
SpeculativeSynchronizationBarrierToPA()
```

### 7.36. SpeculativeSynchronizationBarrierToVA()

该函数执行一条 `SSBB` 指令。

```arm
SpeculativeSynchronizationBarrierToVA()
```

### 7.37. ThisInstr()

该函数返回当前正在执行的指令。它只用于 32 位指令编码。

```arm
bits(32) ThisInstr()
```

### 7.38. VFPExcBarrier()

该过程确保所有浮点异常处理都已完成。
