---
title: "Requirements on IPsec Protocol（IPsec 协议需求）"
spec: AUTOSAR_FO_RS_IPsecProtocol
release: R23-11
---

<!-- 源文档 AUTOSAR_FO_RS_IPsecProtocol（R23-11），需求规范（RS），不受 Type A 七章骨架约束；章节结构镜像源文档自身编号（1–4 + A 附录）。需求项 ID [RS_IPSEC_*] 与 {DRAFT} 标记按 2026-11-03 批次决议整体省略（标题仅翻译），需求项按其在源文档中的出现顺序补予小节编号（4.2.1–4.2.27，其中 00001/00002 在 markdown 转换中丢失标题级别，已按需求项恢复）；项间依赖引用改写为章节号交叉引用。源第 5 章「Requirements Tracing」为纯 ID 追溯表，按 2026-11-03 决议整章省略并将后续章节重编号（源 6→5）；每项之后的追溯回引（RS_Main_*）随追溯章一并省略；参考文献后的孤立页脚标题「AUTOSAR_CP_RS_Features」为页脚噪声，一并丢弃。封面元数据表、免责声明与目录按 EXP 流程省略；全部图引用均为页面装饰，未嵌入内容图。源文中的标识符空格伪影（ENCR _ AES _ GCM _ 16 等）已重构为真实标识符；00001 描述中的「IETF RTF 4301」为源拼写笔误，按标题中的 RFC 修正。 -->

## 1. 文档范围

本文档定义 **AUTOSAR Foundation** 中 **IPsec** 的需求。其动机是确保 **IPsec** 在自适应平台内部以及自适应与经典配置之间的互操作性。

## 2. 所用约定

### 2.1. 文档约定

**AUTOSAR** 文档中需求的表述遵循约束 TPS\_STDT\_00078 规定的表格，见 **Standardization Template** 的「Support for Traceability」章（[\[1\]](#ref-1)）。

需求的表达应使用约束 TPS\_STDT\_00053 规定的义务表达动词形式，见 **Standardization Template** 的「Support for Traceability」章（[\[1\]](#ref-1)）。

## 3. 缩略语和缩写

**AH**
> 认证报头（**Authentication Header**）

**DB**
> 数据库（**Database**）

**ESP**
> 封装安全载荷（**Encapsulating Security Payload**）

**ICV**
> 完整性校验值（**Integrity Check Value**）

**IKE**
> 互联网密钥交换（**Internet Key Exchange**）

**IKEv2**
> 互联网密钥交换版本 2（**Internet Key Exchange version 2**）

**IP**
> 互联网协议（**Internet Protocol**）

**IPsec**
> 互联网协议安全（**Internet Protocol Security**）

**PAD**
> 对端授权数据库（**Peer Authorization Database**）

**PKI**
> 公钥基础设施（**Public Key Infrastructure**）

**PSK**
> 预共享密钥（**Pre-Shared Keys**）

**RAM**
> 随机存取存储器（**Random Access Memory**）

**SA**
> 安全关联（**Security Association**）

**SAD**
> 安全关联数据库（**Security Association Database**）

**SPD**
> 安全策略数据库（**Security Policy Database**）

**TCP/IP**
> 传输控制协议/互联网协议（**Transmission Control Protocol / Internet Protocol**）

**V2X**
> 车联万物（**Vehicle to everything**）

上表未提供的缩略语/缩写和术语收录于 **AUTOSAR** 术语表 [\[2\]](#ref-2)。

## 4. 需求规格

本章描述驱动 **IPsecProtocol** 定义工作的全部需求。

### 4.1. 功能概述

**IPsec** 是 **IP** 协议第 3 层上认证和加密的标准。其总体工作方式以及在 **AUTOSAR** 中的预期使用方式在 **IPsec** 实现说明 [\[3\]](#ref-3) 中描述。

总体上，以 strongSwan [\[4\]](#ref-4) 作为参考。它是 **IPsec** 的一个开源实现。如果对描述 **IPsec** 协议的通用 **RFC**（[\[5\]](#ref-5)、[\[6\]](#ref-6)、[\[7\]](#ref-7)、[\[8\]](#ref-8)）或本文档中定义的需求有任何不确定之处，可以查阅 strongSwan 实现加以澄清。

### 4.2. 功能需求

#### 4.2.1. IPsec 应按照 IETF RFC 4301 提供支持

| 描述 | 应按照 **IETF** RFC 4301 提供对 **IPsec** 的支持。限制：与隧道模式相关的所有需求均为可选，例如第 5.1.2、7.1 和 7.2 节。 |
| --- | --- |
| 理由 | 实现经由 **IP** 的安全通信 |
| 依赖项 | - |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4301 [5] |

#### 4.2.2. IP 认证报头（AH）应按照 IETF RFC 4302 提供支持

| 描述 | 应按照 **IETF** RFC 4302 的陈述在 **TCP/IP** 协议栈中实现 **IP** 认证报头（**AH**）。限制：与隧道模式相关的第 3.1.2 节可以实现也可以不实现。 |
| --- | --- |
| 理由 | 实现经由 **IP** 的安全通信 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4302 [6] |

#### 4.2.3. IP 封装安全载荷（ESP）应按照 IETF RFC 4303 提供支持

| 描述 | 应按照 **IETF** RFC 4303 的陈述在 **TCP/IP** 协议栈中实现 **IP** 封装安全载荷（**ESP**）。限制：与隧道模式相关的任何章节可以实现也可以不实现，例如第 3.1.2 节。 |
| --- | --- |
| 理由 | 实现经由 **IP** 的安全通信 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4303 [7] |

#### 4.2.4. 互联网密钥交换（IKEv2）协议应按照 IETF RFC 7296 提供支持

| 描述 | 应按照 **IETF** RFC 7296 的陈述在 **TCP/IP** 协议栈中实现互联网密钥交换（**IKEv2**）协议。不应支持旧的 **IKEv1**。限制：支持仅限于场景 1.1.2「端到端传输」（**Endpoint-to-Endpoint Transport**）。 |
| --- | --- |
| 理由 | 实现经由 **IP** 的安全通信 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7296 [8] |

#### 4.2.5. AH 和 ESP 的扩展序列号（ESN）应按照 IETF RFC 4304 提供支持

| 描述 | 应按照 **IETF** RFC 4304 支持 **AH** 和 **ESP** 的扩展序列号（**ESN**）。 |
| --- | --- |
| 理由 | 实现经由 **IP** 的安全通信 |
| 依赖项 | [§4.2.2](#422-ip-认证报头ah应按照-ietf-rfc-4302-提供支持)、[§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4304 [9] |

#### 4.2.6. 如果在 IPsec 中使用加密，则也应使用认证

| 描述 | 如果在 **IPsec** 中使用加密，则也应按照 **IETF** RFC 8221 第 4 节使用认证。 |
| --- | --- |
| 理由 | 未认证的加密是不安全的 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 8221 [10] |

#### 4.2.7. 预共享密钥（PSK）可与 IKEv2 结合使用

| 描述 | 预共享密钥（**PSK**）可与 **IKEv2** 结合使用。 |
| --- | --- |
| 理由 | 与使用数字签名相比，可以使启动稍快，但代价是额外的密钥管理 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | - |

#### 4.2.8. 预共享密钥（PSK）不应用于直接建立 IPsec 安全关联（SA）

| 描述 | 预共享密钥（**PSK**）不应用于直接建立 **IPsec** 安全关联（**SA**）。见 **IETF** RFC 8221 第 3 节。 |
| --- | --- |
| 理由 | 使用 **PSK** 直接建立 **SA** 会破坏完美前向保密等许多安全特性，并使重放攻击更容易 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 8221 [10] |

#### 4.2.9. 直接建立 SA 时，计数器模式加密算法不应与预共享密钥结合使用

| 描述 | 根据 **IETF** RFC 8221 第 3 节，在直接建立 **SA** 时，计数器模式加密算法（例如 `ENCR_AES_CCM_16` 和 `ENCR_AES_GCM_16`）不应与预共享密钥结合使用。 |
| --- | --- |
| 理由 | 计数器模式算法比 [§4.2.8](#428-预共享密钥psk不应用于直接建立-ipsec-安全关联sa) 破坏更多的安全假设 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 8221 [10] |

#### 4.2.10. IKEv2 应支持周期性重认证和重密钥

| 描述 | **IKEv2** 应按照 **IETF** RFC 7296 第 1.3.2 和 1.3.3 节支持对 **IKEv2** 通信伙伴的周期性重认证和重密钥（**rekeying**）。 |
| --- | --- |
| 理由 | 被视为良好的安全实践，将被盗密钥的有用性限制在更短的时间段内 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7296 [8] |

#### 4.2.11. IKEv2 应支持交换密钥的无缝切换

| 描述 | **IKEv2** 应按照 **IETF** RFC 7296 第 2.8 节支持交换密钥的无缝切换。这意味着，在重密钥或重认证期间，应先创建新的重叠 **SA**，然后再删除旧的 **SA**（「先建后断」（**make before break**）），以使服务不被中断。可支持 **IETF** RFC 4478。 |
| --- | --- |
| 理由 | 避免在重密钥阶段服务中断 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7296 [8]、**IETF** RFC 4478 [11] |

#### 4.2.12. IKEv2 应在关机时优雅地删除所有 SA，并在下次启动后立即重建已删除的 SA

| 描述 | **IKEv2** 应按照 **IETF** RFC 7296 第 1.4.1 节在关机时优雅地删除所有 **SA**，并在下次启动后立即重建已删除的 **SA**。 |
| --- | --- |
| 理由 | 在最小化服务中断的同时保持 **IPsec** 的无状态特性 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7296 [8] |

#### 4.2.13. IKEv2 应支持死亡对端检测

| 描述 | **IKEv2** 应按照 **IETF** RFC 7296 第 2.4 节使用死亡对端检测（**dead peer detection**）。可支持 **IETF** RFC 3706。 |
| --- | --- |
| 理由 | 带宽管理，避免向死亡对端发送数据 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7296 [8]、**IETF** RFC 3706 [12] |

#### 4.2.14. IKEv2 应支持基于带数字签名的 X.509v3 证书的认证

| 描述 | **IKEv2** 应按照 **IETF** RFC 7427 支持基于带数字签名的 **X.509v3** 证书的认证。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 7427 [13] |

#### 4.2.15. IPsec 应支持以下认证算法：带 256 位密钥的 AES Galois 消息认证码

| 描述 | **IPsec** 应按照 **IETF** RFC 4543 支持以下认证算法：带 256 位密钥的 **AES** Galois 消息认证码（`AUTH_AES_256_GMAC`）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.2](#422-ip-认证报头ah应按照-ietf-rfc-4302-提供支持)、[§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4543 [14] |

#### 4.2.16. IPsec 应支持以下认证算法：带 128 位密钥的 AES 基于密码的消息认证码

| 描述 | **IPsec** 应按照 **IETF** RFC 4494 支持以下认证算法：带 128 位密钥的 **AES** 基于密码的消息认证码（`AUTH_AES_CMAC_96`）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.2](#422-ip-认证报头ah应按照-ietf-rfc-4302-提供支持)、[§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4494 [15] |

#### 4.2.17. IPsec 应支持以下加密算法：带 256 位密钥和 16 字节完整性校验值（ICV）的 AES Galois/计数器模式

| 描述 | **IPsec** 应按照 **IETF** RFC 4106 支持以下加密算法：带 256 位密钥和 16 字节完整性校验值（**ICV**）的 **AES** Galois/计数器模式（`ENCR_AES_GCM_16`）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4106 [16] |

#### 4.2.18. IPsec 应支持以下加密算法：带 256 位密钥和 16 字节完整性校验值（ICV）的 CBC-Mac 计数器模式 AES

| 描述 | **IPsec** 应按照 **IETF** RFC 4309 支持以下加密算法：带 256 位密钥和 16 字节完整性校验值（**ICV**）的 **CBC-Mac** 计数器模式 **AES**（`ENCR_AES_CCM_16`）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4309 [17] |

#### 4.2.19. IPsec 和 IKEv2 应支持以下密码套件：Suite-B-GMAC-256。如果使用 NULL 加密，认证应由 AH 而非 ESP 提供

| 描述 | **IPsec** 和 **IKEv2** 应按照 **IETF** RFC 6379 第 3.4 节支持以下密码套件：**Suite-B-GMAC-256**。如果使用 **NULL** 加密，认证应由 **AH** 而非 **ESP** 提供。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 6379 [18] |

#### 4.2.20. IPsec 和 IKEv2 应支持以下密码套件：Suite-B-GMAC-128。如果使用 NULL 加密，认证应由 AH 而非 ESP 提供

| 描述 | **IPsec** 和 **IKEv2** 应按照 **IETF** RFC 6379 第 3.3 节支持以下密码套件：**Suite-B-GMAC-128**。如果使用 **NULL** 加密，认证应由 **AH** 而非 **ESP** 提供。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.3](#423-ip-封装安全载荷esp应按照-ietf-rfc-4303-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 6379 [18] |

#### 4.2.21. IETF RFC 8247 中归类为「MUST」的所有算法均应受到 IKEv2 支持

| 描述 | **IETF** RFC 8247 中归类为「**MUST**」的所有算法均应受到 **IKEv2** 支持。归类为「**MUST-**」或更低的算法可以支持。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 8247 [19] |

#### 4.2.22. IPsec 的安全策略数据库（SPD）应可针对 IP、IP 范围、协议、端口和端口范围进行配置

| 描述 | **IPsec** 的安全策略数据库（**SPD**）应按照 **IETF** RFC 4301 第 4.4.1.1 节支持针对 **IP**、**IP** 范围、协议、端口和端口范围的配置。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4301 [5] |

#### 4.2.23. IPsec 的安全策略数据库（SPD）默认行为应为 BYPASS

| 描述 | **IPsec** 的安全策略数据库（**SPD**）默认行为应为 **BYPASS**，即不使用 **IPsec**。这意味着，对于在 **SPD** 中找不到任何配置的 **TCP/IP** 端点，流量应在没有 **IPsec** 保护的情况下通过。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | - |

#### 4.2.24. IPsec 不应用于保护以下端口：500/UDP 和 4500/UDP（由 IKEv2 使用）

| 描述 | **IPsec** 不应用于保护以下端口：500/**UDP** 和 4500/**UDP**（由 **IKEv2** 使用）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | - |

#### 4.2.25. IPsec 的对端授权数据库（PAD）应可配置为使用 X.509v3

| 描述 | **IPsec** 的对端授权数据库（**PAD**）应按照 **IETF** RFC 4301 第 4.4.3 节支持配置为使用 **X.509v3** 证书。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.1](#421-ipsec-应按照-ietf-rfc-4301-提供支持)、[§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | **IETF** RFC 4301 [5] |

#### 4.2.26. IPsec 的对端授权数据库（PAD）应可配置为使用预共享密钥（PSK）

| 描述 | **IPsec** 的对端授权数据库（**PAD**）应支持配置为使用预共享密钥（**PSK**）。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | |

#### 4.2.27. 应能够定义 IKEv2 在 IKE_INIT 协商期间使用的算法的优先顺序

| 描述 | **IKEv2** 将用于协商在 **IKEv2 INIT** 阶段使用哪些算法。应能够（但不要求）设置可用算法的优先顺序。 |
| --- | --- |
| 理由 | 支持行业安全标准 |
| 依赖项 | [§4.2.4](#424-互联网密钥交换ikev2协议应按照-ietf-rfc-7296-提供支持) |
| 用例 | 车内安全通信 |
| 支撑材料 | |

## 5. 参考文献

<a id="ref-1"></a>[1] Standardization Template
> AUTOSAR_FO_TPS_StandardizationTemplate

<a id="ref-2"></a>[2] Glossary
> AUTOSAR_FO_TR_Glossary

<a id="ref-3"></a>[3] Explanation of IPsec Implementation Guidelines
> AUTOSAR_AP_EXP_IPsecImplementationGuidelines

<a id="ref-4"></a>[4] strongSwan website
> https://www.strongswan.org

<a id="ref-5"></a>[5] RFC 4301, Security Architecture for the Internet Protocol

<a id="ref-6"></a>[6] RFC 4302, IP Authentication Header

<a id="ref-7"></a>[7] RFC 4303, IP Encapsulating Security Payload (ESP)

<a id="ref-8"></a>[8] RFC 7296, Internet Key Exchange Protocol Version 2 (IKEv2)

<a id="ref-9"></a>[9] RFC 4304, Extended Sequence Number (ESN) Addendum to IPsec Domain of Interpretation (DOI) for Internet Security Association

<a id="ref-10"></a>[10] RFC 8221, Cryptographic Algorithm Implementation Requirements and Usage Guidance for Encapsulating Security Payload (ESP) and Authentication Header (AH)

<a id="ref-11"></a>[11] RFC 4478, Repeated Authentication in Internet Key Exchange (IKEv2) Protocol

<a id="ref-12"></a>[12] RFC 3706, A Traffic-Based Method of Detecting Dead Internet Key Exchange (IKE) Peers

<a id="ref-13"></a>[13] RFC 7427, Signature Authentication in the Internet Key Exchange Version 2 (IKEv2)

<a id="ref-14"></a>[14] RFC 4543, The Use of Galois Message Authentication Code (GMAC) in IPsec ESP and AH

<a id="ref-15"></a>[15] RFC 4494, The AES-CMAC-96 Algorithm and Its Use with IPsec

<a id="ref-16"></a>[16] RFC 4106, The Use of Galois/Counter Mode (GCM) in IPsec Encapsulating Security Payload (ESP)

<a id="ref-17"></a>[17] RFC 4309, Using Advanced Encryption Standard (AES) CCM Mode with IPsec Encapsulating Security Payload (ESP)

<a id="ref-18"></a>[18] RFC 6379, Suite B Cryptographic Suites for IPsec

<a id="ref-19"></a>[19] RFC 8247, Algorithm Implementation Requirements and Usage Guidance for the Internet Key Exchange Protocol Version 2 (IKEv2)

<a id="ref-20"></a>[20] Requirements on AUTOSAR Features
> AUTOSAR_CP_RS_Features

## A. AUTOSAR 可追溯项变更历史

请注意，本章中的列表还包括在后续版本中已从规范中移除的可追溯项。这些可追溯项在文档中不作为超链接出现。

### A.1. 本文档依据 AUTOSAR 版本 R23-11 的可追溯项变更历史

#### A.1.1. R23-11 中新增的需求

无

#### A.1.2. R23-11 中变更的需求

无

#### A.1.3. R23-11 中删除的需求

无
