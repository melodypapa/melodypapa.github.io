---
title: "通信（Communication）"
---



**AUTOSAR** 通信（**Communication**）相关的基础软件模块笔记：涵盖车辆网络驱动与接口（**CAN**、**LIN**）、车载以太网栈（以太网驱动/接口/交换机、**SoAd**、**UdpNm**），以及通信数据处理与安全机制（**PDU Router**、**COM**/**E2E** 变换器、总线镜像、**SecOC**、**FVM**、服务发现等）。

## 文章

### CAN

* [AUTOSAR CAN Driver（CAN驱动程序）](can_driver/index.md)
* [AUTOSAR CAN Interface](can_interface/index.md)
* [AUTOSAR CAN NM（CAN网络管理）](can_network_management/index.md)
* [AUTOSAR J1939Nm（SAE J1939 网络管理）](j1939nm/index.md)
* [AUTOSAR J1939Rm（SAE J1939 请求管理器）](j1939rm/index.md)
* [AUTOSAR J1939Tp（SAE J1939 传输层）](j1939tp/index.md)
* [AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](ieee1722tp/index.md)
* [AUTOSAR Nm（网络管理接口）](nm/index.md)
* [AUTOSAR CanSM（CAN状态管理器）](cansm/index.md)
* [AUTOSAR CanTp（CAN传输层）](cantp/index.md)
* [AUTOSAR CAN Transceiver Driver](can_transceiver_driver/index.md)
* [AUTOSAR CAN XL Driver（CAN XL 驱动程序）](canxl_driver/index.md)
* [AUTOSAR CAN XL Transceiver Driver（CAN XL 收发器驱动程序）](canxl_transceiver_driver/index.md)

### LIN

* [AUTOSAR LIN Driver](lin_driver/index.md)
* [AUTOSAR LinIf (LIN Interface)](lin_interface/index.md)
* [AUTOSAR LinSM（LIN 状态管理器）](linsm/index.md)
* [AUTOSAR LinTrcv（LIN 收发器驱动程序）](lintrcv/index.md)

### 以太网

* [AUTOSAR Ethernet Driver（以太网驱动程序）](ethernet_driver/index.md)
* [AUTOSAR Ethernet Interface（以太网接口）](ethernet_interface/index.md)
* [AUTOSAR Ethernet State Manager（以太网状态管理器）](ethsm/index.md)
* [AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](ethernet_switch_driver/index.md)
* [AUTOSAR I-PDU Multiplexer（I-PDU多路复用器）](ipdum/index.md)
* [AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](eth_trcv/index.md)
* [AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](wlan_driver/index.md)
* [AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](wlan_transceiver_driver/index.md)
* [AUTOSAR SOME/IP Transport Protocol（SOME/IP传输协议）](someiptp/index.md)
* [AUTOSAR SOME/IP Transformer（SOME/IP转换器）](someipxf/index.md)
* [AUTOSAR SoAd (Socket Adaptor)](soad/index.md)
* [AUTOSAR TcpIp（TCP/IP协议栈）](tcpip/index.md)
* [AUTOSAR TTCAN Driver（TTCAN 驱动程序）](ttcan_driver/index.md)
* [AUTOSAR TTCAN Interface（TTCAN 接口）](ttcan_interface/index.md)
* [AUTOSAR UdpNm (UDP Network Management)](udp_network_management/index.md)
* [AUTOSAR XCP（通用测量与校准协议）](xcp/index.md)

### FlexRay

* [AUTOSAR FlexRay Driver（FlexRay 驱动程序）](flexray_driver/index.md)
* [AUTOSAR FlexRay AUTOSAR 传输层（FlexRay AUTOSAR Transport Layer）](flexray_ar_transport_layer/index.md)
* [AUTOSAR FlexRay 接口（FlexRay Interface）](flexray_interface/index.md)
* [AUTOSAR FlexRay 网络管理（FlexRay Network Management）](flexray_network_management/index.md)
* [AUTOSAR FlexRay 状态管理器（FlexRay State Manager）](flexray_state_manager/index.md)
* [AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](flexray_iso_transport_layer/index.md)
* [AUTOSAR FlexRay 收发器驱动（FlexRay Transceiver Driver）](flexray_transceiver_driver/index.md)

### 数据处理与安全

* [AUTOSAR DoIP（基于 IP 的诊断）](diagnostic_over_ip/index.md)
* [AUTOSAR Dlt（诊断日志与跟踪）](diagnostic_log_and_trace/index.md)
* [AUTOSAR Large Data COM（大数据 COM）](large_data_com/index.md)
* [AUTOSAR L-SDU Router（链路层 SDU 路由模块）](lsdu_router/index.md)
* [AUTOSAR Mka（MACsec 密钥协商）](macsec/index.md)
* [AUTOSAR PduR (PDU Router)](pdu_router/index.md)
* [AUTOSAR COM（COM模块）](com/index.md)
* [AUTOSAR COM Based Transformer](com_based_transformer/index.md)
* [E2E Transformer (E2E转换器)](e2e_transformer/index.md)
* [AUTOSAR Bus Mirroring（总线镜像）](mirror/index.md)
* [AUTOSAR SecOC (Secure Onboard Communication)](sec_oc/index.md)
* [AUTOSAR FVM (Freshness Value Manager)](fvm/fvm.md)
* [AUTOSAR SD (Service Discovery)](service_discovery/index.md)
* [AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](spi_handler_driver/index.md)
* [Data Distribution Service for Classic Platform（经典平台数据分发服务）](data_distribution/index.md)

### V2X

* [AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](cellularv2x_driver/index.md)
* [AUTOSAR Charging Manager（充电管理器）](chargingmanager/index.md)
* [AUTOSAR Chinese V2X Management（中国V2X管理）](chinesev2x_mgmt/index.md)
* [AUTOSAR Chinese V2X Message（中国V2X消息）](chinesev2x_msg/index.md)
* [AUTOSAR Chinese V2X Network（中国V2X网络）](chinesev2x_net/index.md)
* [AUTOSAR Chinese V2X Security（中国V2X安全）](chinesev2x_sec/index.md)
* [AUTOSAR V2X Basic Transport（V2X基本传输协议）](v2x_basictp/index.md)
* [AUTOSAR V2X Data Manager（V2X数据管理器）](v2x_datamgr/index.md)
* [AUTOSAR V2X Facilities（V2X设施层）](v2x_facilities/index.md)
* [AUTOSAR V2X GeoNetworking（V2X地理网络）](v2x_geonet/index.md)
* [AUTOSAR V2X Management（V2X管理）](v2x_mgmt/index.md)

## 相关内容

* [CP AUTOSAR 总览](../index.md)
