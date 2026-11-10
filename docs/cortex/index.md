---
title: "ARM Cortex"
---

## 1. 背景概念

### 1.1. 高速缓存（Cache）

1. [多级缓存组织](concept/cache/multilevel_cache/index.md)
2. [直写和回写缓存](concept/cache/write_through_and_back_in_cache/index.md)

### 1.2. 通讯协议

1. [什么是SerDes](concept/communication/serdes/index.md)


## 2. ARM Cortex M7 处理器

本内核的译文按**源文档 → 章节**组织，分为两份文档：

1. [Cortex-M7 TRM（DDI0489F r1p2）](m7-trm/index.md) — 实现手册，逐章翻译 15 章 + 术语表
2. [Armv7-M 架构参考手册（DDI0403E E.e）](armv7-m/index.md) — 该内核实现的架构规则，收录 A3–A6、B2–B5

## 3. ARM Cortex R52+ 处理器

1. [Cortex-R52+ TRM（102199 r0p3）](r52plus-trm/index.md) — 逐章翻译程序员模型、系统控制、时钟复位、初始化、内存系统、内存保护单元

## 4. Armv8-M 架构

1. [Armv8-M 架构参考手册（DDI0553B B.y）](armv8-m/index.md) — M-profile 架构规则，独立于具体内核，收录 Part A 简介与概述
