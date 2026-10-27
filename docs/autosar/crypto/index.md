---
title: "加密（Crypto）"
---



**AUTOSAR** 加密（**Crypto**）相关的基础软件模块笔记：包括位于服务层的 **Crypto Service Manager**（**Csm**，加密服务管理器，以作业（**Job**）为单位向上层提供加密、解密、哈希、**MAC** 与签名等密码学服务），位于加密硬件抽象层、把 **Csm** 的作业与密钥请求分发到各个底层驱动的 **Crypto Interface**（**CryIf**，加密接口），执行实际密码学运算的 **Crypto Driver**（加密驱动程序，支持硬件与软件实现的密码学原语），以及负责密钥与证书的全生命周期管理——密钥更新、派生与持久化，证书解析、验证与存储——的 **Key Manager**（**KeyM**，密钥管理器）。

## 文章

* [AUTOSAR Crypto Driver（加密驱动程序）](crypto_driver/index.md)
* [AUTOSAR Crypto Interface（加密接口）](crypto_interface/index.md)
* [AUTOSAR Key Manager（密钥管理器）](key_manager/index.md)
* [AUTOSAR Crypto Service Manager（加密服务管理器）](crypto_service_manager/index.md)

## 相关内容

* [CP AUTOSAR 总览](../index.md)
