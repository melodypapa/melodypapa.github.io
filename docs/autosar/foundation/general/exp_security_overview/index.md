---
title: "Security Overview（信息安全概览）"
spec: AUTOSAR_FO_EXP_SecurityOverview
release: R23-11
---

<!-- 源文档 AUTOSAR_FO_EXP_SecurityOverview（R23-11），说明文档（EXP），不受 Type A 七章骨架约束；章节结构镜像源文档自身编号（1–4）。封面表格、Disclaimer、Contents 属于文档框架信息，不译；源文档开头的 References 列表保留为文末不编号的「参考文献」注册表，使正文中的 [n] 引用可链接。源文档各小节标题下的「System Level: …」标签保留为粗体行。源文档的页脚脚注按 <sup>N</sup> 标记保留，脚注文本以 `> N …` 引用块跟随其所属段落或表格；源文档 markdown 中脚注 14–17 与 27–35 的脚注文本在转换中丢失，这些标记不保留（避免无指向的标记），其余脚注文本均来自源文档。表 4.2 中对 [\[17\]](#ref-17)/[\[18\]](#ref-18) 的引用是文档引用而非脚注，保留为 [n] 引用标记。表 4.10 的 OpenBSD 行在 PDF→markdown 转换中被分页切断、句尾残缺，按可读内容保守翻译并在该行注明。 -->

## 1. 简介和功能概述

本说明文档为 AUTOSAR 标准的安全设计提供附加信息。本文档目前仅限于 AUTOSAR 自适应平台（**AUTOSAR Adaptive Platform**）。对 AUTOSAR 经典平台的支持可能在本文档的未来版本中加入。

### 1.1. 目标

本文档解释可在 AUTOSAR 自适应平台中使用的安全特性。其动机是为自适应应用（**Adaptive Application**）以及整个 AUTOSAR 自适应平台提供标准化、可移植的信息安全。

### 1.2. 范围

本文档应具有说明性，帮助信息安全工程师识别自适应应用（**Adaptive Application**）与 AUTOSAR 自适应平台中与信息安全相关的主题。

本文档的内容将涉及以下主题：

- 针对内存破坏攻击的防护。
- 软件组件彼此之间的隔离。
- 操作系统与软件组件之间的隔离。
- 现有的信息安全方案

## 2. 定义和缩略语

### 2.1. 缩略语

所使用的全部缩略语均包含在 AUTOSAR TR 术语表中。

## 3. 相关文档

### 3.1. 输入文件和相关标准与规范

<a id="ref-1"></a>- [1] Explanation of Adaptive Platform Design AUTOSAR_AP_EXP_PlatformDesign
<a id="ref-2"></a>- [2] SoK: Eternal War in Memory
<a id="ref-3"></a>- [3] C++ Core Guidelines https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md
<a id="ref-4"></a>- [4] The SPARC Architectural Manual, Version 8 http://sparc.org/wp-content/uploads/2014/01/v8.pdf.gz
<a id="ref-5"></a>- [5] OpenBSD-3.3 announcement, public release of WˆX http://www.openbsd.org/33.html
<a id="ref-6"></a>- [6] Smashing The Stack For Fun And Profit http://phrack.org/issues/49/14.html
<a id="ref-7"></a>- [7] The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)
<a id="ref-8"></a>- [8] Jump-oriented Programming: A New Class of Code-reuse Attack
<a id="ref-9"></a>- [9] On the Expressiveness of Return-into-libc Attacks
<a id="ref-10"></a>- [10] Code-Pointer Integrity
<a id="ref-11"></a>- [11] ARM Pointer Authentication https://lwn.net/Articles/718888/
<a id="ref-12"></a>- [12] PaX ASLR (Address Space Layout Randomization)
<a id="ref-13"></a>- [13] Control-flow Integrity
<a id="ref-14"></a>- [14] AMD64 Architecture Programmer's Manual Volume 2: System Programming http://support.amd.com/TechDocs/24593.pdf
<a id="ref-15"></a>- [15] PowerPC Architecture Book, Version 2.02 https://www.ibm.com/developerworks/systems/library/es-archguide-v2.html
<a id="ref-16"></a>- [16] PowerPC Operating Environment Architecture Book III http://public.dhe.ibm.com/software/dw/library/es-ppcbook3.zip
<a id="ref-17"></a>- [17] Linux Kernel, Summary of changes from v2.6.7 to v2.6.8 https://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.8
<a id="ref-18"></a>- [18] PAX https://pax.grsecurity.net/docs/pax.txt
<a id="ref-19"></a>- [19] CPI LLVM on github https://github.com/cpi-llvm
<a id="ref-20"></a>- [20] Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors
<a id="ref-21"></a>- [21] Drammer: Deterministic Rowhammer Attacks on Mobile Platforms
<a id="ref-22"></a>- [22] ANVIL: Software-Based Protection Against Next-Generation Rowhammer Attacks
<a id="ref-23"></a>- [23] A seccomp overview https://lwn.net/Articles/656307/
<a id="ref-24"></a>- [24] Frequently Asked Questions for FreeBSD 10.X and 11.X https://www.freebsd.org/doc/en/books/faq/security.html
<a id="ref-25"></a>- [25] pledge(2) https://man.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man2/pledge.2

## 4. 安全概览（Security Overview）

### 4.1. 受保护的运行时环境（Protected Runtime Environment）

#### 4.1.1. 引言

软件程序中的漏洞在被运行时攻击利用时会导致未授权的系统操纵与访问。未授权的系统操纵例如任意代码执行、权限提升或对存储的持久性操纵。漏洞的起因主要是编程错误和设计缺陷。尽管在开发过程中可能遵循了设计规则和指南，或者执行了静态代码分析、模糊测试等质量保证过程，但几乎所有项目中都统计性地存在漏洞。AUTOSAR 自适应平台规范只能对这些措施作定性规定。然而，在操作系统层级存在使系统针对此类攻击得到强化的技术对策。注意，"强化"（**harden**）一词的含义是：仍然没有可保证的系统安全，但成功攻击所需的代价可以被提升到更高的水平。

这些强化措施在 AUTOSAR 自适应平台的语境下合并为"受保护的运行时环境"（**Protected Runtime Environment**, PRE）这一术语。PRE 包含针对复杂软件环境最重要的基础保护机制。没有它，任何其他安全机制都可以被绕过，因为任何被攻陷的进程或服务都将能够危害系统上运行的任何其他进程。受保护运行时环境的目标是在运行期间保护进程控制流的完整性，并限制成功攻击的影响。因此，AUTOSAR 自适应平台考虑两种强化策略：应当缓解漏洞被利用的主动防护，以及隔离不可信进程的"事后"（**post-mortem**）措施。

本文档面向将要开发符合 AUTOSAR 自适应平台规范的汽车系统的集成者和实现者，是一份指导文档。它包含满足本文档所列期望安全需求的建议与提示。具体措施的实际实现尚待定义，可能取决于手头的具体系统，也可能是多种措施的组合。

[4.1.2](#412-针对内存破坏攻击的防护) 节介绍漏洞利用缓解方法并给出相关的集成选项。随后，[4.1.7](#417-隔离) 节讨论限制被攻陷或不可信进程作用范围的隔离方面。各章详细说明一般性的攻击与缓解技术，并给出已有的对策实现。此外，还强调了集成的技术前提。

#### 4.1.2. 针对内存破坏攻击的防护

C 或 C++ 等非托管语言使程序员能够以高度的自由度实现管理资源的代码。这样，代码可以针对运行时性能或内存消耗进行优化，并且可以访问操作系统的低层函数。然而，由于 C/C++ 在内存方面是不安全的，程序员对边界检查和内存管理负有全部责任。在实践中，这经常导致违反内存安全（**Memory Safety**）策略或产生内存错误，因为手工内存管理非常容易出错。

内存错误进而可被用来造成内存破坏（**memory corruption**），这是软件组件中几乎所有漏洞的根本原因。如果攻击者利用这些漏洞，可能的影响例如任意代码执行、权限提升或敏感信息泄露。

AUTOSAR 自适应平台所选的语言是平台设计说明文档 [1，2.3.1 节] 中提议的 C++14。因此，自适应应用（**AA**）、AUTOSAR Runtime for Adaptive Applications（**ARA**）以及自适应平台基础或自适应平台服务上的功能簇所指定的编程语言都是非托管的，从而导致很大的攻击面。PRE 的一个目标是最小化这一攻击面。

本章结构如下。[4.1.3](#413-概述) 节概述内存破坏漏洞的潜在类型。[4.1.4](#414-安全编码) 节详述编码过程中的典型陷阱。[4.1.5](#415-攻击与对策) 节解释内存破坏攻击的基本技术原因以及各攻击阶段上相应的最先进防护技术。此外，[4.1.6](#416-现有方案) 节给出在 AUTOSAR AP 语境下实现和集成所介绍防护技术的可能实用方案。

#### 4.1.3. 概述

漏洞的利用及其缓解是一个复杂的主题。计算机安全研究人员持续开发新的攻击和相应的防御。[\[2\]](#ref-2) 中描述了内存破坏攻击及相应防护技术的一般模型。该模型（参见图 4.1）总结了漏洞的一般成因、按照攻击目标影响利用它们的方式，以及针对四类攻击（代码破坏攻击（**Code corruption attack**）、控制流劫持攻击（**Control-flow hijack attack**）、纯数据攻击（**Data-only attack**）和信息泄露（**Information leak**））在各攻击阶段上的缓解策略。在每个攻击阶段，模型都定义了为阻止成功攻击必须成立的若干策略。

前两个阶段为所有攻击类型所共有，描述漏洞的根本原因。在第一阶段，内存破坏操纵一个指针。当这个无效指针随后被解引用时，触发破坏。指针无效是指它是一个越界指针（**out-of-bounds pointer**），即指向先前分配的内存区域边界之外，或者它变成了悬空指针（**dangling pointer**），即指向一个已被删除的对象。众所周知的越界漏洞例如：缓冲区上溢/下溢（**buffer over/underflow**）、格式化字符串漏洞（**format string bug**），以及整数溢出（**integer overflow**）、截断（**truncation**）或符号（**signedness**）错误等索引类漏洞，或错误的指针转换（**pointer casting**）。典型的悬空指针漏洞有：释放后使用（**use-after-free**）或双重释放（**double-free**）。与 C 和 C++ 相关的问题集合例如可以在 MITRE 的通用缺陷枚举（**Common Weakness Enumeration**, CWE）的软件弱点类型列表中找到<sup>1</sup>。内存错误的探查是攻击的第一步。随后，指针被解引用以读取、写入或释放内存。

![图 4.1：[\[2\]](#ref-2) 中的攻击模型，展示四类攻击及各攻击阶段的缓解策略（Attack model from [\[2\]](#ref-2) demonstrating four attack types, policies mitigating the attacks in different attack stages）](Figure4-1.png)

> 1 http://cwe.mitre.org/data/definitions/659.html

#### 4.1.4. 安全编码

在根源上对抗漏洞的第一项措施是首先避免错误和失误。为达到这一目标，程序员在开发过程中必须注意许多陷阱。一个简单的例子是使用标准 C 库中的不安全函数，如 strcpy()。它将一个以空字符结尾的字符串复制到一个缓冲区，直到遇到空字符。如果所分配的目标缓冲区不够大，该函数仍会在缓冲区末尾之后继续复制字符，从而覆盖其他数据。这是通常称为缓冲区溢出（**buffer overflow**）的众多陷阱之一，攻击者可以利用它，例如在缓冲区分配在栈上时覆盖存储的返回指针。对于给定的例子，程序员应改用更安全的变体。为此，许多标准 C 库函数都补充了包含边界检查的版本，对 strcpy() 而言即 strncpy()。这样输入的长度受到限制，只要缓冲区分配得当，就不会被溢出。虽然据信有更多安全的函数（如 strncpy()），但它们自身也带有各自的怪癖和缺陷。此外，还必须考虑更复杂的、与上下文相关的问题。

为避免内存泄漏、悬空指针或内存的多次释放，强烈鼓励使用"资源获取即初始化"（**resource acquisition is initialization**, RAII）惯用法。其目标是确保每个先前分配的资源都会被正确释放。将 RAII 应用于 C++ 意味着把资源的分配和相应的释放封装到一个专门的类中：资源在构造函数中分配，而由同一对象的析构函数释放。这保证了在对象生存期结束时正确地释放资源。然而，必须确保封装对象的生存期限于所论资源被使用的时间。通常，这通过创建放置在栈上的块作用域对象来实现。虽然 RAII 也可以用于堆上的内存分配，但它并不限于这一用例。在处理互斥量时，RAII 还有助于防止死锁：由互斥量保护的全部逻辑将在获取和释放锁的对象的上下文中执行。同样值得注意的是，RAII 不一定需要封装类，也可以借助编译器扩展实现——栈对象（例如局部变量或结构体）可以与相应的清理函数关联。此类扩展可用于 LLVM 以及其他支持 GNU 语法的编译器（如 GCC）。这使得可以将 RAII 应用于纯 C。

在实践中，程序员应当随手掌握编码指南，例如面向安全相关系统的 MISRA。遗憾的是，C++ 核心指南并未涵盖与信息安全相关问题的规则集 [\[3\]](#ref-3)。但有处理这些问题的第三方指南，例如 SEI CERT C++ 编码标准<sup>2</sup>。

由于这些指南非常全面，出于时间原因，实践中只有少数程序员会遵循它们。不过，有一些工具可以在静态代码分析中支持对某些规则的检查，例如 Flawfinder<sup>3</sup>、RATS<sup>4</sup> 或 CodeSonar<sup>5</sup>。无论如何，使用工具并不保证代码没有漏洞，因为运行时条件（或执行上下文）超出了此类工具的范围。类似地，已识别的漏洞在运行时行为方面可能没有得到充分修复。

> 2 https://www.securecoding.cert.org/confluence/pages/viewpage.action?pageId=637
> 3 https://www.dwheeler.com/flawfinder/
> 4 https://security.web.cern.ch/security/recommendations/en/codetools/rats.shtml
> 5 https://www.grammatech.com/products/codesonar

#### 4.1.5. 攻击与对策

作为第二道防线，假设漏洞确实存在，并且开发者总会引入一些漏洞。因此，对增强型对策的一项要求是独立于所编写的代码。目标是缓解漏洞被利用。

##### 4.1.5.1. 代码破坏攻击

代码破坏攻击（**Code Corruption Attack**）意图操纵虚拟内存空间中文本段内的可执行指令，并破坏代码完整性（**Code Integrity**）策略（参见图 4.1）。

对策是将包含代码的内存页设置为只读，或分别为 W⊕X（写异或执行，**write xor execute**）。这必须在两个系统层级上实现，即处理器和操作系统。CPU 的 MMU 必须提供细粒度的内存权限布局（例如 NX 位 [\[4, p.248\]](#ref-4)），否则操作系统应模拟这一点。此外，操作系统层级必须支持底层的权限布局，例如 W⊕X [\[5\]](#ref-5) 或数据执行防护（**Data Execution Prevention**, DEP）。但如果使用自修改代码和即时（**Just-In-Time**, JIT）编译则须小心，因为生成的代码必须先写入可写页，然后再将这些页设置为可执行。

##### 4.1.5.2. 控制流劫持攻击

控制流劫持攻击（**Control-flow Hijack Attack**）从利用内存破坏修改一个代码指针开始，使其指向攻击者定义的地址，从而破坏代码指针完整性（**Code Pointer Integrity**）策略（参见图 4.1）。随后原始代码中的间接控制流转移使用该指针。这样控制流从原始流被转移，其控制流完整性（**Control-flow Integrity**）被违反。最后一步是执行攻击载荷。文献区分两种方式：代码注入攻击（**code-injection attacks**）和代码重用攻击（**code-reuse attacks**）。代码注入攻击 [\[6\]](#ref-6) 基于向内存注入任意自定义指令（又称 shellcode）作为攻击载荷；而代码重用攻击，如面向返回的编程（**Return Oriented Programming**, ROP）[\[7\]](#ref-7)、面向跳转的编程（**Jump Oriented Programming**, JOP）[\[8\]](#ref-8) 和 return-to-libc [\[9\]](#ref-9)，则利用进程内存中已有的代码构造所谓的 gadgets（代码片段），实现针对性的恶意功能。

总而言之，如果代码指针和控制流的完整性被破坏，控制流劫持攻击就会成功。此外，恶意功能目标地址的值必须已知，并且在代码注入的情况下，承载注入代码的内存页必须是可执行的。

如果所有对敏感指针（例如代码指针的直接引用和对代码指针的引用）的解引用都未被修改，则代码指针完整性（**CPI**）的目标即得到满足（参见 [\[10\]](#ref-10)）。近期已有若干可行方法能在此早期阶段检测代码指针及代码指针引用的篡改。代码指针完整性 [\[10\]](#ref-10) 机制提供完整的内存安全，但只针对代码指针的直接引用和对代码指针的引用。据作者所述，该方法能防御所有控制流劫持攻击。CPI 是静态代码分析（识别所有敏感指针）、程序重写（将被识别的指针保护到一个称为安全栈（**safe-stack**）的安全内存区域）以及指令级隔离（控制对安全区域的访问）的结合。这些机制需要编译器和运行时支持，运行时开销约 8%。另一个要求是代码完整性。代码指针分离（**Code Pointer Separation**, CPS）[\[10\]](#ref-10) 是 CPI 的放宽版本。除其他外，CPS 将受保护指针的集合限制为代码指针（无间接引用），从而把开销降低到约 2%，但仍具有很强的检测保证。

检测代码指针修改的另一种方法是指针认证（**Pointer Authentication**）[\[11\]](#ref-11)。该方法使用密码学函数在解引用之前对指针进行认证与验证。指针被替换为生成的签名，不能直接解引用。这需要编译器和指令集支持。为降低开销，需要为密码学原语提供硬件加速。

借助栈破坏保护（**Stack Smashing Protection**, SSP），可以检测覆盖已保存返回地址的基于栈的缓冲区溢出。为此，在函数序言中、在已保存的基指针和已保存的返回地址之前，向栈中插入一个伪随机值，也称为栈金丝雀（**Stack Canary**）或栈饼干（**Stack Cookie**）。当函数返回并执行函数尾声时，将该值与受保护的副本比较。如果针对返回地址的缓冲区溢出覆盖了该值，则程序中止，因为两个值不再匹配。

如前所述，代码注入攻击要求注入的指令位于可执行内存页。根据 W⊕X 原则（也称为数据执行防护（**DEP**）），一个内存页要么被标记为可写，要么被标记为可执行，但不能二者兼有。这防止了指令覆盖栈或堆等数据内存并在之后执行它们。该方法需要细粒度的页权限支持：或者由 CPU 的 MMU 提供所谓的 NX 位（**No-execute bit**），或者按 [4.1.5.1](#4151-代码破坏攻击) 节所述在软件中模拟。此外，所使用的操作系统必须支持它。

代码重用攻击不受 W⊕X 机制影响，因为它们利用已标记为可执行的现有内存区域，不需要向内存注入额外代码。为缓解此类攻击，目前已部署的对策在更早的攻击阶段实现。在第四攻击阶段，恶意功能的目标地址必须已知。一般而言，攻击者知道或可以估计虚拟地址空间中的地址，因为对二进制文件而言它在编译后是静态的。实践中的对策是通过地址空间布局随机化（**Address Space Layout Randomization**, ASLR）[\[12\]](#ref-12) 混淆地址空间布局：各内存段的位置被随机化，使得预测正确的目标地址更加困难。ASLR 需要高熵来阻止暴力的去随机化攻击，并依赖于阻止动态构造攻击载荷所利用的意外信息泄露（[4.1.5.4](#4154-信息泄露) 节）。为保证高熵，ASLR 应在 64 位（或更高）架构上实现。此外，每个内存区域都必须被随机化，包括栈、堆、主代码段和库。

除 ASLR 外，控制流完整性策略意图检测原始控制流的转移。已确立的技术有：影子栈（**Shadow Stack**）和控制流完整性（Abadi）（**CFI**）[\[13\]](#ref-13)。影子栈的思想是将已保存的返回地址压入一个单独的影子栈，以便在函数返回时进行比较。此外，CFI 还保护间接调用和跳转。原始 CFI 通过静态确定有效目标来创建静态控制流图，并为它们赋予唯一身份（**ID**）。随后对调用和返回进行插桩，在跳转之前将目标地址与该 ID 比较。必须通过 W⊕X 保护有效目标不被覆盖。

##### 4.1.5.3. 纯数据攻击

内存破坏也可以被利用来修改与控制流数据无关的安全关键数据。例如，利用缓冲区溢出改变某个条件构造可能导致非预期的程序行为。这样，数据完整性（**Data Integrity**）策略被违反。数据空间随机化（**Data Space Randomization**）和写完整性测试（**Write Integrity Testing**, WIT）等技术使此类攻击更难实施，但它们尚未在实践中确立。

##### 4.1.5.4. 信息泄露

内存破坏攻击也被用于泄露内存内容。这样，ASLR 等概率性对策可以通过对随机生成数据的了解而被绕过。与纯数据攻击一样，数据空间随机化可能有助于缓解信息泄露。

#### 4.1.6. 现有方案

本节介绍前文各节所述对策的当前最先进实现方案。对每种方法，给出实施该方案的系统层级（编译器、操作系统或硬件），以及对其技术和安全要求的期望。

##### 4.1.6.1. 写异或执行、数据执行防护（Write xor Execute, Data Execution Prevention (DEP)）

**系统层级：硬件、操作系统**

该方法的思想是将内存页标记为可写或可执行，但不能同时标记为二者。由此缓解代码注入攻击。在最低的系统层级，需要一种细粒度内存页权限机制。此外，操作系统必须支持该硬件机制，甚至模拟内存页权限机制。

表4.1：执行防护的硬件支持示例（**Examples of Hardware Support for Execution Prevention**）

| 架构 | 指令集 | 强制机制 |
|---|---|---|
| x86 | AMD64 [\[14, p. 56\]](#ref-14)、Intel64 | 不可执行位（**NX 位**）、页表执行禁用（**XD 位**）、页表 |
| ARM | ARMv6、ARMv8-A | 永不执行位（**XN 位**）、页表 PEN（特权永不执行）、PAN（特权访问永不） |
| SPARC | Oracle SPARC Architecture 2011 | Translation Storage Buffer（可选） |
| PowerPC | IBM PowerISA [\[15\]](#ref-15) [\[16, p. 33\]](#ref-16) | Segment Lookaside Buffer（**SLB**） |

表4.2：执行防护的操作系统支持示例（**Examples of Operating System Support for Execution Prevention**）

| 族 | 名称 | 实现 |
|---|---|---|
| Linux | Linux kernel | Linux 内核主线 ≥ 2.6.8 [\[17\]](#ref-17) |
|  | PaX | 针对 Linux 内核的补丁，使用或模拟内存页硬件权限 [\[18\]](#ref-18) |
|  | Exec Shield | 针对 Linux 内核的补丁，Fedora Core 1 至 6<sup>6</sup> 以及 Red Hat Enterprise Linux ≥ 3<sup>7</sup> <sup>8</sup> 的一部分，使用硬件支持或模拟内存页权限 |
|  | grsecurity | 针对 Linux 内核的补丁，使用硬件支持或模拟内存页权限 <sup>9</sup> <sup>10</sup> |
|  | Android | Android ≥ 2.3 <sup>11</sup> |
| Unix | OpenBSD | OpenBSD ≥ 3.3 <sup>12</sup> |
|  | NetBSD | NetBSD ≥ 2.0 <sup>13</sup> |
|  | FreeBSD | FreeBSD ≥ 5.3 |

> 6 https://archives.fedoraproject.org/pub/archive/fedora/linux/core/1/x86_64/os/RELEASE-NOTES.html
> 7 http://people.redhat.com/mingo/exec-shield/
> 8 https://www.redhat.com/f/pdf/rhel/WHP0006US_Execshield.pdf
> 9 https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options#Enforce_non-executable_kernel_pages
> 10 https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options#Paging_based_non-executable_pages
> 11 https://source.android.com/security/#memory-management-security-enhancements
> 12 http://www.openbsd.org/33.html
> 13 http://www.netbsd.org/docs/kernel/non-exec.html
> 17 https://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.8
> 18 https://pax.grsecurity.net/docs/pax.txt

##### 4.1.6.2. 栈破坏保护（Stack Smashing Protection (SSP)）

**系统层级：编译器**

栈破坏保护（**SSP**）机制在函数序言中、在已保存的基指针和已保存的返回地址之前，将伪随机值（栈金丝雀（**Stack Canary**）或栈饼干（**Stack Cookie**））放置在栈上，并在函数返回之前再次比较该值。SSP 在编译期强制实施。出于性能原因，编译器必须决定哪些函数需要保护。如果编译器实现做出了错误决定而相关函数存在漏洞，SSP 就会失效。此外，信息泄露使攻击者能够读取该伪随机值并将其整合到其攻击中，从而用正确的值覆盖缓冲区。

表4.3：栈破坏保护的编译器支持示例（**Examples of Stack Smashing Protection Compiler Support**）

| 编译器 | 选项 | 说明 |
|---|---|---|
| GNU Compiler Collection (GCC) | -fstack-protector | 生成额外代码以检查缓冲区溢出（例如栈破坏攻击）。做法是向带有易受攻击对象的函数添加保护变量，包括调用 alloca 的函数以及缓冲区大于 8 字节的函数。保护变量在函数进入时初始化，在函数退出时检查。如果保护检查失败，则打印错误消息并且程序退出。 |
|  | -fstack-protector-all | 与 -fstack-protector 类似，但保护所有函数。 |
|  | -fstack-protector-strong | 与 -fstack-protector 类似，但包括需要保护的附加函数——具有局部数组定义或引用局部帧地址的函数。 |
|  | -fstack-protector-explicit | 与 -fstack-protector 类似，但只保护带有 stack_protect 属性的函数。 |
| Clang | -fstack-protector-all | 对所有函数强制使用栈保护器。 |
|  | -fstack-protector-strong | 使用强启发式方法为函数应用栈保护器。 |
|  | -fstack-protector | 为可能易受栈破坏影响的函数启用栈保护器。 |
| Intel C++ Compiler | -fstack-security-check | 该选项决定编译器是否生成检测某些覆盖返回地址的缓冲区越界的代码。这是对未强制实施缓冲区大小限制的代码进行利用的常用技术。 |
| Keil ARM C/C++ Compiler | -protect_stack | 使用 -protect_stack 启用栈保护特性。使用 -no_protect_stack 显式禁用该特性。如果同时指定两个选项，则以最后指定的选项为准。 |


##### 4.1.6.3. 地址空间布局随机化（Address Space Layout Randomization (ASLR)）

**系统层级：编译器、操作系统**

地址空间布局随机化（**ASLR**）混淆进程的地址空间布局。由此，各内存段的位置被随机化，使得预测执行代码重用攻击所需的正确目标地址更加困难。ASLR 需要高熵来阻止暴力的去随机化攻击，并依赖于阻止意外信息泄露（[4.1.5.4](#4154-信息泄露) 节）——动态构造的攻击载荷会利用它们。为保证高熵，ASLR 应在 64 位（或更高）架构上实现。此外，ASLR 要求位置无关可执行文件（**position-independent executables**, PIE），它允许主可执行二进制文件使用随机基址。

ASLR 主要由操作系统强制实施，但要求二进制文件为位置无关可执行文件、共享库为编译器生成的位置无关代码。

表4.4：ASLR 的操作系统支持示例（**Examples of ASLR Operating System Support**）

| 族 | 名称 | 实现 |
|---|---|---|
| Linux | Linux kernel | Linux 内核主线 ≥ 3.14 <sup>18</sup>。用户态程序的 ASLR 以及针对内核自身的内核地址空间布局随机化（**KASLR**）<sup>19</sup>。 |
|  | PaX | 针对 Linux 内核的补丁 <sup>20</sup> |
|  | Exec Shield | 针对 Linux 内核的补丁 <sup>21</sup> |
|  | grsecurity | 针对 Linux 内核的补丁 <sup>22</sup> |
|  | Android | Android ≥ 4.1 <sup>23</sup> |
| BSD | OpenBSD | OpenBSD ≥ 4.4 <sup>24</sup> |
|  | NetBSD | NetBSD ≥ 5.0 <sup>25</sup> |
|  | FreeBSD | 以补丁形式提供的 FreeBSD <sup>26</sup> |

> 18 https://lwn.net/Articles/569635/
> 19 http://selinuxproject.org/~jmorris/lss2013_slides/cook_kaslr.pdf
> 20 https://pax.grsecurity.net/docs/aslr.txt
> 21 http://www.redhat.com/f/pdf/rhel/WHP0006US_Execshield.pdf
> 22 https://en.wikibooks.org/wiki/Grsecurity/Appendix/Grsecurity_and_PaX_Configuration_Options#Restrict_mprotect.28.29
> 23 https://source.android.com/security/enhancements/enhancements41
> 24 https://www.openbsd.org/plus44.html
> 25 https://netbsd.org/releases/formal-5/NetBSD-5.0.html
> 26 https://hardenedbsd.org/content/freebsd-and-hardenedbsd-feature-comparisons

表4.5：ASLR 的编译器支持示例（**Examples of ASLR Compiler Support**）

| 编译器 | 选项 | 说明 |
|---|---|---|
| GNU Compiler Collection (GCC) | -fpie、-fPIE | 这些选项与 -fpic 和 -fPIC 类似，但生成的位置无关代码只能链接进可执行文件。通常在链接期间使用 -pie GCC 选项时使用这些选项。以安全的方式将其融入打包特别困难，因为要求最终以 -pie 链接的所有 .o 文件都以 -fPIE 构建。会有一定的性能损失，但这仅由 -fPIE 引起——对所有已链接的库（通过其 -fPIC）而言已是如此。 |
|  | -fPIC | 如果目标机器支持，则生成适合动态链接且对全局偏移表大小没有限制的位置无关代码。该选项在 AArch64、m68k、PowerPC 和 SPARC 上有区别。位置无关代码需要特殊支持，因此只能在特定机器上工作。 |
| Clang | -fpie、-fPIE | 参见 GCC。 |
|  | -fPIC | 参见 GCC。 |
| Intel C++ Compiler | -pie | 决定编译器是否生成将被链接进可执行文件的位置无关代码。 |
|  | -fpic | 决定编译器是否生成位置无关代码。 |
| Keil ARM C/C++ Compiler | -bare_metal_pie | （裸金属 PIE 支持已弃用。armclang 中提供了对 -fropi 和 -frwpi 的支持。可以使用这些选项创建裸金属位置无关可执行文件。）裸金属位置无关可执行文件（**PIE**）是不需要在特定地址执行、而可以在任何适当对齐的地址执行的可执行文件。 |
|  | -fropi、-fno-ropi | 启用或禁用只读位置无关（**ROPI**）代码的生成。 |
|  | -frwpi、-fno-rwpi | 启用或禁用读/写位置无关（**RWPI**）代码的生成。 |


##### 4.1.6.4. 控制流完整性（Control-flow Integrity (CFI)）

**系统层级：编译器**

控制流完整性（**CFI**）是当前的研究课题。不过，Clang 包含多种控制流完整性（**CFI**）方案的实现，这些方案设计为在检测到可能允许攻击者破坏程序控制流的某些未定义行为时中止程序。这些方案针对性能进行了优化，允许开发者在发布构建中启用它们。Clang 中的 CFI 实现具有约 1% 的性能开销和约 15% 的二进制大小开销（仅前向边）。

表4.6：CFI 的编译器支持示例（**Examples of CFI Compiler Support**）

| 编译器 | 选项 | 说明 |
|---|---|---|
| GNU Compiler Collection (GCC) | -fvtable-verify=[std&#124;preinit&#124;none] | 该选项仅在编译 C++ 代码时可用。它开启（或在使用 -fvtable-verify=none 时关闭）如下安全特性：在运行时对每次虚调用验证进行调用所经过的 vtable 指针对该对象类型有效，并且未被破坏或覆盖。如果在运行时检测到无效的 vtable 指针，则报告错误并立即停止程序执行。该选项导致在程序启动时构建用于验证 vtable 指针的运行时数据结构。选项 std 和 preinit 控制这些数据结构构建的时机。在这两种情况下，数据结构都在执行到达 main 之前构建。使用 -fvtable-verify=std 会在共享库被加载并初始化之后构建数据结构；-fvtable-verify=preinit 会在共享库被加载并初始化之前构建它们。如果该选项在命令行中多次出现且指定了不同取值，none 的优先级高于 std 和 preinit；preinit 的优先级高于 std。 |
| Clang | -fsanitize=cfi-cast-strict | 启用严格转换检查。派生自错误动态类型的基类到派生类转换。 |
|  | -fsanitize=cfi-unrelated-cast | 从 void* 或其他无关类型到错误动态类型的转换。 |
|  | -fsanitize=cfi-nvcall | 通过 vptr 属于错误动态类型的对象进行的非虚调用。 |
|  | -fsanitize=cfi-vcall | 通过 vptr 属于错误动态类型的对象进行的虚调用。 |
|  | -fsanitize=cfi-icall | 调用具有错误动态类型的函数的间接调用。 |
|  | -fsanitize=cfi | 启用所有方案。 |


##### 4.1.6.5. 代码指针完整性（CPI）、代码指针分离（CPS）

**系统层级：编译器**

代码指针完整性（**CPI**）是 C/C++ 程序的一种性质，它通过要求所有指向代码的直接和间接指针的完整性来保证不存在控制流劫持攻击。代码指针分离（**CPS**）是 CPI 的简化版本，在实践中针对此类攻击提供强保护。SafeStack 是 CPI/CPS 的一个组件，可以独立使用，并防御基于栈的控制流劫持。

CPI/CPS/SafeStack 可以通过编译期插桩对 C/C++ 程序自动强制实施，性能开销分别仅为 8.5%/1.9%/0.05%。SafeStack 强制机制现在是 Clang 编译器的一部分，而 CPI 和 CPS 以研究原型形式提供。当前状态请参见 [\[19\]](#ref-19)。

表4.7：CPI 与 CPS 的编译器支持示例（**Examples of CPI and CPS Compiler Support**）

| 编译器 | 选项 | 说明 |
|---|---|---|
| Clang <sup>36</sup> <sup>37</sup> | -fsanitize=safe-stack | SafeStack 是一个插桩 pass，它保护程序免受基于栈缓冲区溢出的攻击，而不引入任何可测量的性能开销。它将程序栈分成两个不同的区域：安全栈（**safe stack**）和不安全栈（**unsafe stack**）。安全栈存储返回地址、寄存器溢出以及始终以安全方式访问的局部变量，而不安全栈存储其余所有内容。这种分离确保不安全栈上的缓冲区溢出不能用于覆盖安全栈上的任何内容。 |

> 36 http://dslab.epfl.ch/proj/cpi/
> 37 https://clang.llvm.org/docs/SafeStack.html

##### 4.1.6.6. 指针认证（Pointer Authentication）

**系统层级：硬件、编译器**

指针认证（**Pointer Authentication**）使用密码学函数在解引用之前对指针进行认证与验证 [\[11\]](#ref-11)。指针被替换为生成的签名，不能直接解引用。这需要编译器和指令集支持。ARM 最近在 ARMv8.3-A 规范中引入了指针认证扩展<sup>38</sup>。GCC 在版本 7<sup>39</sup> 中为 AArch64 目标（ARMv8.3-A 架构）引入了对指针认证的基本支持<sup>40</sup>。由于对密码学原语的硬件加速，其开销可以忽略不计<sup>40</sup>。

表4.8：指针认证的编译器支持示例（**Examples of Pointer Authentication Compiler Support**）

| 编译器 | 选项 | 说明 |
|---|---|---|
| GNU Compiler Collection (GCC) <sup>41</sup> | -msign-return-address=scope | 选择对返回地址签名施行的函数范围。允许的取值为 none（禁用返回地址签名）、non-leaf（对非叶函数启用指针签名）和 all（对所有函数启用指针签名）。默认值为 none。 |

> 38 https://community.arm.com/processors/b/blog/posts/armv8-a-architecture-2016-addition
> 39 https://gcc.gnu.org/gcc-7/changes.html
> 40 https://lwn.net/Articles/719270/
> 41 https://gcc.gnu.org/onlinedocs/gcc-7.1.0/gcc/AArch64-Options.html#AArch64-Options

#### 4.1.7. 隔离

在系统内隔离软件组件是一种常见的保护措施，用于保护其他组件免受错误组件的影响——无论这种影响是通过无意中的编程错误，还是由接管了可被攻陷组件的攻击者造成的蓄意危害。[4.1.2](#412-针对内存破坏攻击的防护) 节详述的防护措施是一种预防性措施，目的在于阻止攻击者通过利用编程错误接管软件组件；而隔离的目的在于限制攻击者在接管某个软件组件之后对其他软件组件可能产生的影响。因此，只有当系统架构经过恰当设计、相应地划分并隔离系统的不同功能方面时，隔离才是一项有效的措施。注意，本指南不涉及隔离的这一架构方面，而是技术方面，即隔离可以如何实现。

以下各节描述两种隔离方法：多个软件组件彼此之间的隔离，以及软件组件与操作系统本身的隔离。这两种方法是正交的——即应用之间的水平隔离以及应用与 OS 之间的垂直隔离——并且可以相应地组合。

#### 4.1.8. 水平隔离

##### 4.1.8.1. 虚拟内存

最古老且最普遍的隔离机制是虚拟内存（**virtual memory**）概念，即为系统中每个正在运行的软件组件呈现其自己的虚拟地址空间，由操作系统将其映射到可用的物理内存。其起源可以追溯到 20 世纪 50 年代，最初的意图是隐藏物理内存的碎片化，但也提供了隔离软件组件的可能性。由于每个组件在虚拟地址空间中运行，它无法访问其他组件的内存（除非操作系统显式允许）。该特性需要硬件支持，例如内存管理单元（**MMU**），但除了非常小的微控制器之外，这种支持在大多数计算机系统中几乎无处不在。

该概念的扩展是虚拟机（或虚拟化（**virtualization**））概念，即由 hypervisor 仿真多台虚拟机（**VM**）。每台 VM 都可以运行一个完整的操作系统，取决于虚拟化的程度，甚至可以在不加修改的状态下运行。hypervisor 控制每台 VM 对物理硬件组件的访问，甚至可以仿真某些组件（如网络接口）。与虚拟内存类似，虚拟化需要专门的硬件支持以达到适当的性能和安全水平。

注意，这两种方法都有其局限。虚拟内存或虚拟化提供的隔离只与操作系统或 hypervisor 本身一样强，因为恶意应用可能通过编程错误取得对 OS 或 hypervisor 的控制（[4.1.10](#4110-垂直隔离) 节所述的措施旨在最小化这一攻击面）。类似地，恶意应用可能利用其对其他硬件组件的访问来绕过隔离，因为某些硬件组件可能对系统内存具有不受限制的访问。IOMMU（向硬件组件呈现虚拟地址空间的技术）可用于对抗这一点。最后，攻击者可能利用物理内存本身的易失特性来绕过隔离。例如 [\[20\]](#ref-20) 描述了"rowhammer"攻击，它能够翻转通常应用程序无法访问的内存位置中的位。该攻击对某个内存位置以快速连续的方式执行长时间读取，在 DRAM 内存的情况下这将导致相邻内存单元改变状态。已证明这种效应能够在 Linux 和 Android（参见 [\[21\]](#ref-21)）系统中提升应用程序的权限。系统设计者必须考虑针对此类攻击使用一种或多种缓解措施，例如使用带纠错的内存，或 [\[22\]](#ref-22) 中所示的软件缓解措施。

#### 4.1.9. 操作系统级虚拟化

现代操作系统中存在一种更轻量的虚拟化形式，通常称为操作系统级虚拟化（**operating-system-level virtualization**）或容器化（**containerization**）。著名的例子有构建在 Linux 内核命名空间（**Namespacing**）功能之上的 LXC<sup>42</sup>，以及 FreeBSD 操作系统提供的 Jail<sup>43</sup> 功能。这些工具只虚拟化操作系统的某些资源，例如文件系统、进程树或网络栈。这样，操作系统创建了一个对系统资源或其他容器具有严格受控访问的容器。与完全虚拟化相反，这些容器不能执行不同的操作系统，尽管可以并排运行一个完全独立的用户空间实例。

表4.9：操作系统虚拟化/容器实现（**Operating System Virtualization / Container Implementations**）

| 操作系统族 | 方案 | 说明 |
|---|---|---|
| UNIX | chroot | 这是许多类 UNIX 系统中提供的系统调用，可用于建立一个具有不同根文件系统的执行环境。因此，它只将宿主的文件系统与容器隔离。如果容器中包含特权进程，它们可以轻易影响系统。 |
| Linux | Namespaces、LXC、Docker、systemd-nspawn | 存在许多构建于 Linux 命名空间功能之上的解决方案，其中许多允许建立隔离的容器。运行在这些容器内的进程看不到其他容器或宿主的资源，除非被指派。这样，即使容器内的特权进程也无法影响系统的其余部分。 |
| FreeBSD | Jails | 与 chroot 类似的方案，但安全性有所改进。例如，这些容器（在此语境中称为"jails"）提供隔离的网络，并限制其中特权进程的能力（例如特权进程不能影响系统的其余部分）。 |

> 42 https://linuxcontainers.org/
> 43 https://www.freebsd.org/doc/handbook/jails.html

#### 4.1.10. 垂直隔离

将操作系统与应用隔离（通常称为沙箱化（**sandboxing**））是受保护运行时环境的另一个重要方面。基本思想是限制进程的能力，即限制进程可以做什么<sup>44</sup>。经典的做法是在权限不再需要时立即放弃它们，即权限撤销（**privilege revocation**）。例如，在 UNIX 系统上 ping 命令需要 root 权限来创建原始网络套接字，但在创建之后会将其权限降至普通用户。理想情况下，软件组件应当放弃（或从不被给予）它不需要的任何权限，或者在权限不再需要时立即放弃它们。与 ping 的例子一样，任何软件组件都必须以一个建立阶段来构造，其中所有高级权限被使用并随后被放弃。下面给出几个操作系统功能的例子，它们允许应用放弃能力或权限。

表4.10：操作系统中的沙箱机制（**Sandboxing Mechanisms in Operating Systems**）

| 操作系统族 | 方案 | 说明 |
|---|---|---|
| Linux | Seccomp 模式 1（严格）[\[23\]](#ref-23) | Linux 操作系统上的进程可以非常容易地限制其允许的系统调用集合。允许的子集极其严格，将进程限制为 read、write、exit 和 sigreturn。一旦激活，该 Seccomp 模式无法再次停用。 |
| Linux | Seccomp 模式 2（过滤器）[\[23\]](#ref-23) | 较新的 Seccomp 模式版本——seccomp 过滤器模式——允许更加细粒度的控制。其概念是允许进程附加一个小的过滤器程序，该程序将检查每个系统调用。该过滤器程序必须是"Berkley Packet Filter"（**BPF**）——一种限制性很强的字节码形式——它会在每次系统调用之前由内核执行。该过滤器随后可以检查每个系统调用，例如检查进行的是哪个系统调用或参数如何设置。过滤器然后返回关于内核应如何处理的决策。系统调用可以被允许或阻止，如果调用被阻止，可以有若干关于如何阻止的选择。过滤器可以决定立即杀死进程、简单地让系统调用返回错误、向违规进程发送信号，或通知附加到程序的跟踪器（如调试器）。这些过滤器的一个显著性质是它们会被派生的子进程继承，这使得可以在启动一个有潜在危险的进程之前建立过滤器。 |
| FreeBSD | Securelevel [\[24, chapter 13\]](#ref-24) | 该功能以递增级别限制系统上运行的所有进程的可能性，一旦进入便不能降低（直到重启系统）。 |
| OpenBSD | pledge(2) [\[25\]](#ref-25) | 该功能可用于限制进程可以执行的系统调用。某些系统调用可以被完全禁止，其他系统调用的功能可以受到限制。例如，open 系统调用可以被限制为只打开一小组系统文件，或者 mprotect 不能将内存设置为可执行。一旦限制生效，进程在其整个生存期内都受其约束（注：源文档该行在 PDF 分页处被切断，句尾残缺；此处按可读内容保守翻译，pledge(2) 的完整行为见参考文献 [\[25\]](#ref-25)）。 |

> 44 不要与"进程做什么"相混淆，因为进程的行为会被攻击改变。
