<section id="title">AUTOSAR Crypto Driver（加密驱动程序）</section>

# 1. 简介和功能概述

本规范介绍了 **AUTOSAR** 基础软件模块加密驱动程序的功能、API 和配置。

加密驱动程序位于微控制器抽象层中，该层位于加密硬件抽象层-加密接口（Crypto Interface）[4]和上层服务层-加密服务管理器（Crypto Service Manager）[5] 之下。 加密驱动程序是针对特定设备的驱动程序，它只是抽象硬件支持的功能。

加密驱动程序允许定义不同的加密驱动程序对象。如：AES 加速器、SW 组件等。这些对象可应用于不同缓冲区中的并发请求。对于每个硬件对象，应支持优先级相关的作业处理。加密软件解决方案（如：基于软件的CDD）可以定义与加密驱动程序相同的接口，用于与上层交互，并应为应用程序提供接口。

# 2. 缩略语

**CDD**
> Complex Device Driver：复杂设备驱动程序

**CSM**
> Crypto Service Manager

**CRYIF**
> Crypto Interface

**CRYPTO**
> Crypto Driver

**DET**
> Default Error Tracer

**HSM**
> Hardware Security Module

**HW**
> Hardware

**SHE**
> Security Hardware Extension

**SW**
> Software

## 2.1. 专业术语

**Crypto Driver Object**
> A Crypto Driver implements one or more Crypto Driver Objects. The Crypto Driver Object can offer different crypto primitives in hardware or software. The Crypto Driver Objects of one Crypto Driver are independent of each other. There is only one workspace for each Crypto Driver Object (i.e. only one crypto primitive can be performed at the same time) The only exception of independency between Crypto Driver Object is the usage of a default Random Number Generator (see [SWS_Crypto_00225]).

**Key**
> A Key can be referenced by a job in the Csm. In the Crypto Driver, the key references a specific key type.

**Key Type**
> A key type consists of references to key elements. The key types are typically pre-configured by the vendor of the Crypto Driver.

**Key Element**
> Key elements are used to store data. This data can be e.g. key material or the IV needed for AES encryption. It can also be used to configure the behaviour of the key management functions. 

**Channel**
> A channel is the path from a Crypto Service Manager queue via the Crypto Interface to a specific Crypto Driver Object. 

**Job**
> A 'Job' is a configured 'CsmJob'. Among others, it refers to a key, a cryptographic primitive and a reference channel.

**Crypto Primitive**
> 'Primitive' is an instance of a configured cryptographic algorithm realized in a Crypto Driver Object. Among others it refers to a functionality provided by the CSM to the application, the concrete underlining 'algorithmfamily' (e.g. AES, MD5, RSA, ...), and a 'algorithmmode' (e.g. ECB, CBC, ...).

**Operation**
> An operation of a crypto primitive declares what part of the crypto primitive shall be performed. 

> There are three different operation modes: 
* START：Operation mode indicates a new request of a crypto primitive, and it shall cancel all previous requests of the same job and primitive.
* UPDATE：Operation mode indicates, that the crypto primitive expects input data.
* FINISH: Operation mode indicates, that after this part all data are fed completely and the crypto primitive can finalize the calculations.

> It is also possible to perform more than one operation at once by concatenating the corresponding bits of the operation mode argument.

**Priority**
> The priority of a job defines the importance of it. The higher the priority (as well in value), the more immediate the job will be executed. The priority of a cryptographic job is part of the configuration.

**Service**
> A 'Service' shall be understood as defined in the TR_Glossary document: A service is a type of operation that has a published specification of interface and behavior, involving a contract between the provider of the capability and the potential clients.