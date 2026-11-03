---
title: "AUTOSAR API 函数清单（按模块）"
---

本页按模块分表（模块与表内函数均按字母排序）汇总站内已翻译 AUTOSAR 文章中定义的函数：**名称**直达文章中该条目的定义小节，**简述**取自条目「说明」的第一句。**由脚本自动生成，请勿手工编辑**（`python .agents/skills/autosar-translate/scripts/gen_api_list.py`；源：站内已翻译文章的章节标题与「说明」块）。

## AUTOSAR ADC Driver（模数转换器驱动）（18）

来源：[AUTOSAR ADC Driver（模数转换器驱动）](../io/adc_driver/index.md) · SWS_ADCDriver

| 函数 | 简述 |
|---|---|
| [**Adc_DeInit**](../io/adc_driver/index.md#733-adc_deinit) | 将所有ADC硬件单元恢复到与其上电复位状态相当的状态。 |
| [**Adc_DisableGroupNotification**](../io/adc_driver/index.md#7310-adc_disablegroupnotification) | 为所请求ADC通道组禁用通知机制。 |
| [**Adc_DisableHardwareTrigger**](../io/adc_driver/index.md#738-adc_disablehardwaretrigger) | 为所请求ADC通道组禁用硬件触发。 |
| [**Adc_EnableGroupNotification**](../io/adc_driver/index.md#739-adc_enablegroupnotification) | 为所请求ADC通道组启用通知机制。 |
| [**Adc_EnableHardwareTrigger**](../io/adc_driver/index.md#737-adc_enablehardwaretrigger) | 为所请求ADC通道组启用硬件触发。 |
| [**Adc_GetCurrentPowerState**](../io/adc_driver/index.md#7315-adc_getcurrentpowerstate) | 此API返回ADC硬件单元的当前电源状态。 |
| [**Adc_GetGroupStatus**](../io/adc_driver/index.md#7311-adc_getgroupstatus) | 返回所请求ADC通道组的转换状态。 |
| [**Adc_GetStreamLastPointer**](../io/adc_driver/index.md#7312-adc_getstreamlastpointer) | 返回存储在结果缓冲区中每通道的有效采样数。 |
| [**Adc_GetTargetPowerState**](../io/adc_driver/index.md#7316-adc_gettargetpowerstate) | 此API返回ADC硬件单元的目标电源状态。 |
| [**Adc_GetVersionInfo**](../io/adc_driver/index.md#7313-adc_getversioninfo) | 返回此模块的版本信息。 |
| [**Adc_Init**](../io/adc_driver/index.md#731-adc_init) | 初始化ADC硬件单元和驱动程序。 |
| [**Adc_Main_PowerTransitionManager**](../io/adc_driver/index.md#751-adc_main_powertransitionmanager) | 此API被周期性调用，监督电源状态切换，检查模块的就绪状态并发出回调IoHwAb_Adc_NotifyReadyForPowerState\<Mode\>（见AdcPowerStateReadyCbkRef配置参数）。 |
| [**Adc_PreparePowerState**](../io/adc_driver/index.md#7317-adc_preparepowerstate) | 此API启动允许ADC硬件模块进入请求电源状态所需的过程。 |
| [**Adc_ReadGroup**](../io/adc_driver/index.md#736-adc_readgroup) | 读取所请求组最近一轮已完成转换的组转换结果，并将通道值从DataBufferPtr地址开始存储。 |
| [**Adc_SetPowerState**](../io/adc_driver/index.md#7314-adc_setpowerstate) | 此API配置Adc模块，使其进入已准备的电源状态（从预定义的一组已配置电源状态中选择）。 |
| [**Adc_SetupResultBuffer**](../io/adc_driver/index.md#732-adc_setupresultbuffer) | 使用组特定的结果缓冲区起始地址初始化ADC驱动，转换结果将存储在该缓冲区中。 |
| [**Adc_StartGroupConversion**](../io/adc_driver/index.md#734-adc_startgroupconversion) | 启动所请求ADC通道组所有通道的转换。 |
| [**Adc_StopGroupConversion**](../io/adc_driver/index.md#735-adc_stopgroupconversion) | 停止所请求ADC通道组的转换。 |

## AUTOSAR Basic Software Mode Manager（BSW模式管理器）（36）

来源：[AUTOSAR Basic Software Mode Manager（BSW模式管理器）](../mode_management/basic_software_mode_manager/index.md) · SWS_BSWModeManager

| 函数 | 简述 |
|---|---|
| [**BswM_BswMPartitionRestarted**](../mode_management/basic_software_mode_manager/index.md#731-bswm_bswmpartitionrestarted) | 如果包含BswM的分区已经被重新启动，函数则被Restart Task调用。 |
| [**BswM_CanSM_CurrentState**](../mode_management/basic_software_mode_manager/index.md#732-bswm_cansm_currentstate) | 函数被CanSM模块调用，用于指示CanSM当前状态。 |
| [**BswM_ClientModeRequestEnum**](../mode_management/basic_software_mode_manager/index.md#7761-bswm_clientmoderequestenum) | — |
| [**BswM_ComM_CurrentMode**](../mode_management/basic_software_mode_manager/index.md#733-bswm_comm_currentmode) | 函数被ComM模块调用，用于指示ComM通道的当前通信模式。 |
| [**BswM_ComM_CurrentPNCMode**](../mode_management/basic_software_mode_manager/index.md#734-bswm_comm_currentpncmode) | 函数被ComM模块调用，用于指示PNC的当前模式。 |
| [**BswM_ComM_InitiateReset**](../mode_management/basic_software_mode_manager/index.md#735-bswm_comm_initiatereset) | 函数被ComM模块调用，用于发出关闭信号。 |
| [**BswM_Dcm_ApplicationUpdated**](../mode_management/basic_software_mode_manager/index.md#736-bswm_dcm_applicationupdated) | 函数被DCM模块调用，用于报告更新的应用程序。 |
| [**BswM_Dcm_CommunicationMode_CurrentState**](../mode_management/basic_software_mode_manager/index.md#737-bswm_dcm_communicationmode_currentstate) | 函数被DCM模块调用，用于通知BswM通信模式的当前状态。 |
| [**BswM_Deinit**](../mode_management/basic_software_mode_manager/index.md#738-bswm_deinit) | 去初始化BSW模式管理器。 |
| [**BswM_EcuM_CurrentState**](../mode_management/basic_software_mode_manager/index.md#739-bswm_ecum_currentstate) | 函数被EcuM模块调用，用于指示当前的ECU操作模式。 |
| [**BswM_EcuM_CurrentWakeup**](../mode_management/basic_software_mode_manager/index.md#7310-bswm_ecum_currentwakeup) | 函数被EcuM模块调用，用于指示唤醒源的当前状态。 |
| [**BswM_EcuM_RequestedState**](../mode_management/basic_software_mode_manager/index.md#7311-bswm_ecum_requestedstate) | 函数被EcuM模块调用，用于通知运行请求协议（Run Request Protocol）的当前状态。 |
| [**BswM_EthIf_PortGroupLinkStateChg**](../mode_management/basic_software_mode_manager/index.md#7312-bswm_ethif_portgrouplinkstatechg) | 函数被EthIf模块调用，用于指示某个以太网交换机端口组（Ethernet switch port group）的链路状态变化。 |
| [**BswM_EthSM_CurrentState**](../mode_management/basic_software_mode_manager/index.md#7313-bswm_ethsm_currentstate) | 函数被EthSM模块调用，用于指示EthSM当前状态。 |
| [**BswM_FrSM_CurrentState**](../mode_management/basic_software_mode_manager/index.md#7314-bswm_frsm_currentstate) | 函数被FrSM模块调用，用于指示FrSM当前状态。 |
| [**BswM_GetVersionInfo**](../mode_management/basic_software_mode_manager/index.md#7315-bswm_getversioninfo) | 返回BswM模块的版本信息。 |
| [**BswM_Init**](../mode_management/basic_software_mode_manager/index.md#7316-bswm_init) | 初始化BSW模式管理器。 |
| [**BswM_J1939DcmBroadcastStatus**](../mode_management/basic_software_mode_manager/index.md#7317-bswm_j1939dcmbroadcaststatus) | 此API告诉BswM可用网络的所需通信状态。 |
| [**BswM_J1939Nm_StateChangeNotification**](../mode_management/basic_software_mode_manager/index.md#7318-bswm_j1939nm_statechangenotification) | J1939Nm状态更改后，通知当前的J1939Nm状态。 |
| [**BswM_LinSM_CurrentSchedule**](../mode_management/basic_software_mode_manager/index.md#7319-bswm_linsm_currentschedule) | 函数被LinSM模块调用，用于指示特定LIN通道的当前活动调度表。 |
| [**BswM_LinSM_CurrentState**](../mode_management/basic_software_mode_manager/index.md#7320-bswm_linsm_currentstate) | 函数被LinSM模块调用，用于指示LinSM当前状态。 |
| [**BswM_LinTp_RequestMode**](../mode_management/basic_software_mode_manager/index.md#7321-bswm_lintp_requestmode) | 函数被LinTP模块调用，用于请求相应LIN通道的模式。 |
| [**BswM_MainFunction**](../mode_management/basic_software_mode_manager/index.md#751-bswm_mainfunction) | BswM的主函数。 |
| [**BswM_modeNotificationPort**](../mode_management/basic_software_mode_manager/index.md#7721-bswm_modenotificationport) | — |
| [**BswM_modeRequestPort**](../mode_management/basic_software_mode_manager/index.md#7722-bswm_moderequestport) | — |
| [**BswM_modeSwitchPort**](../mode_management/basic_software_mode_manager/index.md#7723-bswm_modeswitchport) | — |
| [**BswM_Nm_CarWakeUpIndication**](../mode_management/basic_software_mode_manager/index.md#7322-bswm_nm_carwakeupindication) | 函数被Nm模块调用，用于指示整车被唤醒。 |
| [**BswM_Nm_StateChangeNotification**](../mode_management/basic_software_mode_manager/index.md#7323-bswm_nm_statechangenotification) | Nm状态更改后，当前Nm状态的通知。 |
| [**BswM_NvM_CurrentBlockMode**](../mode_management/basic_software_mode_manager/index.md#7324-bswm_nvm_currentblockmode) | 函数被NvM模块调用，用于指示NvM Block的当前块模式（block mode）。 |
| [**BswM_NvM_CurrentJobMode**](../mode_management/basic_software_mode_manager/index.md#7325-bswm_nvm_currentjobmode) | 函数被NvM模块调用，用于通知BswM多块作业（multi block job）的当前状态。 |
| [**BswM_OfferModeEnum**](../mode_management/basic_software_mode_manager/index.md#7762-bswm_offermodeenum) | — |
| [**BswM_RequestMode**](../mode_management/basic_software_mode_manager/index.md#7326-bswm_requestmode) | 对请求模式（request mode）的通用函数调用（Generic function call）。 |
| [**BswM_Sd_ClientServiceCurrentState**](../mode_management/basic_software_mode_manager/index.md#7327-bswm_sd_clientservicecurrentstate) | 函数被Sd模块调用，用于指示客户端服务的当前状态（可用/关闭）。 |
| [**BswM_Sd_ConsumedEventGroupCurrentState**](../mode_management/basic_software_mode_manager/index.md#7328-bswm_sd_consumedeventgroupcurrentstate) | 函数被Sd模块调用，用于指示Consumed Eventgroup的当前状态（可用/关闭）。 |
| [**BswM_Sd_EventHandlerCurrentState**](../mode_management/basic_software_mode_manager/index.md#7329-bswm_sd_eventhandlercurrentstate) | 函数被Sd模块调用，用于指示EventHandler的当前状态（已请求/已释放）。 |
| [**BswM_SoAd_SoConModeChg**](../mode_management/basic_software_mode_manager/index.md#7330-bswm_soad_soconmodechg) | 函数被SoAd模块调用，用于通知套接字连接的状态变化。 |

## AUTOSAR BndM（非易失性大容量数据管理器）（13）

来源：[AUTOSAR BndM（非易失性大容量数据管理器）](../memory/bulk_nv_data_manager/index.md) · SWS_BulkNvDataManager

| 函数 | 简述 |
|---|---|
| [**BndM_GetBlockPtr**](../memory/bulk_nv_data_manager/index.md#733-bndm_getblockptr) | 服务 ID 0x3。 |
| [**BndM_GetVersionInfo**](../memory/bulk_nv_data_manager/index.md#732-bndm_getversioninfo) | 服务 ID 0x2。 |
| [**BndM_Init**](../memory/bulk_nv_data_manager/index.md#731-bndm_init) | 服务 ID 0x1。 |
| [**BndM_JobEndNotification**](../memory/bulk_nv_data_manager/index.md#741-bndm_jobendnotification) | 服务 ID 0x8。 |
| [**BndM_JobErrorNotification**](../memory/bulk_nv_data_manager/index.md#742-bndm_joberrornotification) | 服务 ID 0x9。 |
| [**BndM_MainFunction**](../memory/bulk_nv_data_manager/index.md#751-bndm_mainfunction) | 服务 ID 0x55。 |
| [**BndM_WriteBlock**](../memory/bulk_nv_data_manager/index.md#735-bndm_writeblock) | 服务 ID 0x5。 |
| [**BndM_WriteCancel**](../memory/bulk_nv_data_manager/index.md#737-bndm_writecancel) | 服务 ID 0x7。 |
| [**BndM_WriteFinalize**](../memory/bulk_nv_data_manager/index.md#736-bndm_writefinalize) | 服务 ID 0x6。 |
| [**BndM_WriteStart**](../memory/bulk_nv_data_manager/index.md#734-bndm_writestart) | 服务 ID 0x4。 |
| [**xxx_BndMWriteBlockFinish**](../memory/bulk_nv_data_manager/index.md#7632-xxx_bndmwriteblockfinish) | 服务 ID 0x57。 |
| [**xxx_BndMWriteFinalizeFinish**](../memory/bulk_nv_data_manager/index.md#7633-xxx_bndmwritefinalizefinish) | 服务 ID 0x58。 |
| [**xxx_BndMWriteStartFinish**](../memory/bulk_nv_data_manager/index.md#7631-xxx_bndmwritestartfinish) | 服务 ID 0x56。 |

## AUTOSAR Bus Mirroring（总线镜像）（29）

来源：[AUTOSAR Bus Mirroring（总线镜像）](../communication/mirror/index.md) · SWS_BusMirroring

| 函数 | 简述 |
|---|---|
| [**Mirror_AddCanMaskFilter**](../communication/mirror/index.md#7424-mirror_addcanmaskfilter) | C |
| [**Mirror_AddCanRangeFilter**](../communication/mirror/index.md#7423-mirror_addcanrangefilter) | C |
| [**Mirror_AddFlexRayFilter**](../communication/mirror/index.md#7427-mirror_addflexrayfilter) | C |
| [**Mirror_AddLinMaskFilter**](../communication/mirror/index.md#7426-mirror_addlinmaskfilter) | C |
| [**Mirror_AddLinRangeFilter**](../communication/mirror/index.md#7425-mirror_addlinrangefilter) | C |
| [**Mirror_DeInit**](../communication/mirror/index.md#7412-mirror_deinit) | C |
| [**Mirror_GetDestNetwork**](../communication/mirror/index.md#7433-mirror_getdestnetwork) | C |
| [**Mirror_GetNetworkHandle**](../communication/mirror/index.md#7443-mirror_getnetworkhandle) | C |
| [**Mirror_GetNetworkId**](../communication/mirror/index.md#7442-mirror_getnetworkid) | C |
| [**Mirror_GetNetworkType**](../communication/mirror/index.md#7441-mirror_getnetworktype) | C |
| [**Mirror_GetStaticFilterState**](../communication/mirror/index.md#7421-mirror_getstaticfilterstate) | C |
| [**Mirror_GetVersionInfo**](../communication/mirror/index.md#7413-mirror_getversioninfo) | C |
| [**Mirror_Init**](../communication/mirror/index.md#7411-mirror_init) | C |
| [**Mirror_IsMirrorActive**](../communication/mirror/index.md#7431-mirror_ismirroractive) | C |
| [**Mirror_IsSourceNetworkStarted**](../communication/mirror/index.md#7435-mirror_issourcenetworkstarted) | C |
| [**Mirror_MainFunction**](../communication/mirror/index.md#761-mirror_mainfunction) | C |
| [**Mirror_Offline**](../communication/mirror/index.md#7432-mirror_offline) | C |
| [**Mirror_RemoveFilter**](../communication/mirror/index.md#7428-mirror_removefilter) | C |
| [**Mirror_ReportCanFrame**](../communication/mirror/index.md#751-mirror_reportcanframe) | C |
| [**Mirror_ReportFlexRayChannelStatus**](../communication/mirror/index.md#754-mirror_reportflexraychannelstatus) | C |
| [**Mirror_ReportFlexRayFrame**](../communication/mirror/index.md#753-mirror_reportflexrayframe) | C |
| [**Mirror_ReportLinFrame**](../communication/mirror/index.md#752-mirror_reportlinframe) | C |
| [**Mirror_SetStaticFilterState**](../communication/mirror/index.md#7422-mirror_setstaticfilterstate) | C |
| [**Mirror_StartSourceNetwork**](../communication/mirror/index.md#7436-mirror_startsourcenetwork) | C |
| [**Mirror_StopSourceNetwork**](../communication/mirror/index.md#7437-mirror_stopsourcenetwork) | C |
| [**Mirror_SwitchDestNetwork**](../communication/mirror/index.md#7434-mirror_switchdestnetwork) | C |
| [**Mirror_TriggerTransmit**](../communication/mirror/index.md#756-mirror_triggertransmit) | C |
| [**Mirror_TxConfirmation**](../communication/mirror/index.md#755-mirror_txconfirmation) | C |
| [**MirrorControl**](../communication/mirror/index.md#7821-mirrorcontrol) | — |

## AUTOSAR CAN Driver（CAN驱动程序）（22）

来源：[AUTOSAR CAN Driver（CAN驱动程序）](../communication/can_driver/index.md) · SWS_CANDriver

| 函数 | 简述 |
|---|---|
| [**Can_CheckWakeup**](../communication/can_driver/index.md#7325-can_checkwakeup) | 该函数检查给定的控制器是否发生了唤醒。 |
| [**Can_DeInit**](../communication/can_driver/index.md#7313-can_deinit) | 该函数去初始化模块。 |
| [**Can_DisableControllerInterrupts**](../communication/can_driver/index.md#7323-can_disablecontrollerinterrupts) | 该函数禁用此CAN控制器的所有中断。 |
| [**Can_EnableControllerInterrupts**](../communication/can_driver/index.md#7324-can_enablecontrollerinterrupts) | 该函数启用所有允许的中断。 |
| [**Can_EnableEgressTimeStamp**](../communication/can_driver/index.md#73211-can_enableegresstimestamp) | 在专用的 HTH 上激活出口时间戳（egress time stamping）。 |
| [**Can_GetControllerErrorState**](../communication/can_driver/index.md#7326-can_getcontrollererrorstate) | 该服务获取CAN控制器的错误状态。 |
| [**Can_GetControllerMode**](../communication/can_driver/index.md#7327-can_getcontrollermode) | 该服务报告所请求的CAN控制器的当前状态。 |
| [**Can_GetControllerRxErrorCounter**](../communication/can_driver/index.md#7328-can_getcontrollerrxerrorcounter) | 返回CAN控制器的Rx错误计数器。 |
| [**Can_GetControllerTxErrorCounter**](../communication/can_driver/index.md#7329-can_getcontrollertxerrorcounter) | 返回CAN控制器的Tx错误计数器。 |
| [**Can_GetCurrentTime**](../communication/can_driver/index.md#73210-can_getcurrenttime) | 根据硬件的能力从硬件寄存器返回一个时间值。 |
| [**Can_GetEgressTimeStamp**](../communication/can_driver/index.md#73212-can_getegresstimestamp) | 在专用的消息对象上读回出口时间戳。 |
| [**Can_GetIngressTimeStamp**](../communication/can_driver/index.md#73213-can_getingresstimestamp) | 在专用的消息对象上读回入口时间戳（ingress time stamp）。 |
| [**Can_GetVersionInfo**](../communication/can_driver/index.md#7312-can_getversioninfo) | 该函数返回该模块的版本信息。 |
| [**Can_Init**](../communication/can_driver/index.md#7311-can_init) | 该函数初始化模块。 |
| [**Can_MainFunction_BusOff**](../communication/can_driver/index.md#753-can_mainfunction_busoff) | 该函数执行被静态配置为「待轮询」的Bus-Off事件的轮询。 |
| [**Can_MainFunction_Mode**](../communication/can_driver/index.md#755-can_mainfunction_mode) | 该函数执行CAN控制器模式转换的轮询。 |
| [**Can_MainFunction_Read**](../communication/can_driver/index.md#752-can_mainfunction_read) | 当 CAN_RX_PROCESSING 设置为 POLLING 时，该函数执行RX指示的轮询。 |
| [**Can_MainFunction_Wakeup**](../communication/can_driver/index.md#754-can_mainfunction_wakeup) | 该函数执行被静态配置为「待轮询」的唤醒事件的轮询。 |
| [**Can_MainFunction_Write**](../communication/can_driver/index.md#751-can_mainfunction_write) | 当 CAN_TX_PROCESSING 设置为 POLLING 时，该函数执行TX确认的轮询。 |
| [**Can_SetBaudrate**](../communication/can_driver/index.md#7321-can_setbaudrate) | 该服务应设置CAN控制器的波特率配置。 |
| [**Can_SetControllerMode**](../communication/can_driver/index.md#7322-can_setcontrollermode) | 该函数执行CAN控制器状态机的软件触发状态转换。 |
| [**Can_Write**](../communication/can_driver/index.md#7331-can_write) | CanIf调用该函数以将CAN消息传递给CAN驱动程序进行传输。 |

## AUTOSAR CAN NM（CAN网络管理）（27）

来源：[AUTOSAR CAN NM（CAN网络管理）](../communication/can_network_management/index.md) · SWS_CANNetworkManagement

| 函数 | 简述 |
|---|---|
| [**CanNm_ActivateTxPnShutdownMsg**](../communication/can_network_management/index.md#7321-cannm_activatetxpnshutdownmsg) | NM指示激活给定NM通道上PN关闭消息的传输。 |
| [**CanNm_CheckRemoteSleepIndication**](../communication/can_network_management/index.md#7318-cannm_checkremotesleepindication) | 检查远程睡眠指示是否发生。 |
| [**CanNm_ConfirmPnAvailability**](../communication/can_network_management/index.md#743-cannm_confirmpnavailability) | 在指定的NM通道上启用PN过滤器功能。 |
| [**CanNm_DeactivateTxPnShutdownMsg**](../communication/can_network_management/index.md#7322-cannm_deactivatetxpnshutdownmsg) | NM指示停用给定NM通道上PN关闭消息的传输。 |
| [**CanNm_DeInit**](../communication/can_network_management/index.md#732-cannm_deinit) | 去初始化CanNm模块。 |
| [**CanNm_DisableCommunication**](../communication/can_network_management/index.md#736-cannm_disablecommunication) | 由于ISO 14229通信控制（28 hex）服务而禁用NM PDU传输能力。 |
| [**CanNm_EnableCommunication**](../communication/can_network_management/index.md#737-cannm_enablecommunication) | 由于ISO 14229通信控制（28 hex）服务而启用NM PDU传输能力。 |
| [**CanNm_GetLocalNodeIdentifier**](../communication/can_network_management/index.md#7312-cannm_getlocalnodeidentifier) | 获取为本地节点配置的节点标识符。 |
| [**CanNm_GetNodeIdentifier**](../communication/can_network_management/index.md#7311-cannm_getnodeidentifier) | 从最近收到的NM PDU中获取节点标识符。 |
| [**CanNm_GetPduData**](../communication/can_network_management/index.md#7314-cannm_getpdudata) | 从最近收到的NM PDU中获取整个PDU数据。 |
| [**CanNm_GetState**](../communication/can_network_management/index.md#7315-cannm_getstate) | 返回网络管理的状态和模式。 |
| [**CanNm_GetUserData**](../communication/can_network_management/index.md#739-cannm_getuserdata) | 从最近收到的NM PDU中获取用户数据。 |
| [**CanNm_GetVersionInfo**](../communication/can_network_management/index.md#7316-cannm_getversioninfo) | 该服务返回该模块的版本信息。 |
| [**CanNm_Init**](../communication/can_network_management/index.md#731-cannm_init) | 初始化CanNm模块。 |
| [**CanNm_MainFunction**](../communication/can_network_management/index.md#751-cannm_mainfunction) | 处理本文档中所描述算法的CanNm主函数。 |
| [**CanNm_NetworkRelease**](../communication/can_network_management/index.md#735-cannm_networkrelease) | ECU无需在总线上通信，从而释放网络。 |
| [**CanNm_NetworkRequest**](../communication/can_network_management/index.md#734-cannm_networkrequest) | ECU需要在总线上通信，从而请求网络。 |
| [**CanNm_PassiveStartUp**](../communication/can_network_management/index.md#733-cannm_passivestartup) | AUTOSAR CAN NM的被动启动。 |
| [**CanNm_PnLearningRequest**](../communication/can_network_management/index.md#7320-cannm_pnlearningrequest) | 为总线上接下来传输的NM消息设置重复消息请求位和部分网络学习位。 |
| [**CanNm_RepeatMessageRequest**](../communication/can_network_management/index.md#7313-cannm_repeatmessagerequest) | 为总线上接下来传输的NM PDU设置重复消息请求位。 |
| [**CanNm_RequestBusSynchronization**](../communication/can_network_management/index.md#7317-cannm_requestbussynchronization) | 请求总线同步。 |
| [**CanNm_RxIndication**](../communication/can_network_management/index.md#742-cannm_rxindication) | 指示从较低层通信接口模块接收到的PDU。 |
| [**CanNm_SetSleepReadyBit**](../communication/can_network_management/index.md#7319-cannm_setsleepreadybit) | 设置控制位向量中的NM协调器睡眠就绪位。 |
| [**CanNm_SetUserData**](../communication/can_network_management/index.md#738-cannm_setuserdata) | 为总线上接下来传输的NM PDU设置用户数据。 |
| [**CanNm_Transmit**](../communication/can_network_management/index.md#7310-cannm_transmit) | 请求传输PDU。 |
| [**CanNm_TriggerTransmit**](../communication/can_network_management/index.md#744-cannm_triggertransmit) | 在此API中，上层模块将检查可用数据是否适合PduInfoPtr->SduLength报告的缓冲区大小。 |
| [**CanNm_TxConfirmation**](../communication/can_network_management/index.md#741-cannm_txconfirmation) | 下层通信接口模块确认PDU的传输，或者PDU的传输失败。 |

## AUTOSAR CAN Transceiver Driver（17）

来源：[AUTOSAR CAN Transceiver Driver](../communication/can_transceiver_driver/index.md) · SWS_CANTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**CanTrcv_CheckWakeFlag**](../communication/can_transceiver_driver/index.md#7314-cantrcv_checkwakeflag) | 请求从收发器硬件检查唤醒标志的状态。 |
| [**CanTrcv_CheckWakeup**](../communication/can_transceiver_driver/index.md#7312-cantrcv_checkwakeup) | 在检测到唤醒中断的情况下，由底层CanIf调用的服务。 |
| [**CanTrcv_ClearTrcvTimeoutFlag**](../communication/can_transceiver_driver/index.md#7310-cantrcv_cleartrcvtimeoutflag) | 清除收发器硬件中超时标志的状态。 |
| [**CanTrcv_ClearTrcvWufFlag**](../communication/can_transceiver_driver/index.md#738-cantrcv_cleartrcvwufflag) | 清除收发器硬件中的WUF标志。 |
| [**CanTrcv_DeInit**](../communication/can_transceiver_driver/index.md#7315-cantrcv_deinit) | 取消初始化CanTrcv模块。 |
| [**CanTrcv_GetBusWuReason**](../communication/can_transceiver_driver/index.md#734-cantrcv_getbuswureason) | 获取收发器的唤醒原因，并保存在参数Reason中返回。 |
| [**CanTrcv_GetOpMode**](../communication/can_transceiver_driver/index.md#733-cantrcv_getopmode) | 获取收发器的模式，并保存在OpMode中返回。 |
| [**CanTrcv_GetTrcvSystemData**](../communication/can_transceiver_driver/index.md#737-cantrcv_gettrcvsystemdata) | 读取收发器配置/状态数据，并通过参数TrcvSysData返回。 |
| [**CanTrcv_Init**](../communication/can_transceiver_driver/index.md#731-cantrcv_init) | 初始化CanTrcv模块。 |
| [**CanTrcv_MainFunction**](../communication/can_transceiver_driver/index.md#741-cantrcv_mainfunction) | 用于扫描所有总线以查找唤醒事件并执行这些事件的服务。 |
| [**CanTrcv_MainFunctionDiagnostics**](../communication/can_transceiver_driver/index.md#742-cantrcv_mainfunctiondiagnostics) | 定期读取收发器诊断状态并相应地报告生产或开发的错误。 |
| [**CanTrcv_ReadTrcvSilenceFlag**](../communication/can_transceiver_driver/index.md#7311-cantrcv_readtrcvsilenceflag) | 从收发器硬件读取沉默标志的状态。 |
| [**CanTrcv_ReadTrcvTimeoutFlag**](../communication/can_transceiver_driver/index.md#739-cantrcv_readtrcvtimeoutflag) | 从收发器硬件读取超时标志的状态。 |
| [**CanTrcv_SetOpMode**](../communication/can_transceiver_driver/index.md#732-cantrcv_setopmode) | 将收发器的模式设置为值OpMode。 |
| [**CanTrcv_SetPNActivationState**](../communication/can_transceiver_driver/index.md#7313-cantrcv_setpnactivationstate) | 该API将收发器的唤醒配置为待机和睡眠模式：CAN收发器由远程唤醒模式（标准CAN唤醒）唤醒，或由配置的远程唤醒帧唤醒。 |
| [**CanTrcv_SetWakeupMode**](../communication/can_transceiver_driver/index.md#736-cantrcv_setwakeupmode) | 根据TrcvWakeupMode启用、禁用或清除收发器的唤醒事件。 |
| [**CanTrcv_VersionInfo**](../communication/can_transceiver_driver/index.md#735-cantrcv_versioninfo) | 获取模块的版本并保存在VersionInfo中返回。 |

## AUTOSAR CAN XL Driver（CAN XL 驱动程序）（19）

来源：[AUTOSAR CAN XL Driver（CAN XL 驱动程序）](../communication/canxl_driver/index.md) · SWS_CANXLDriver

| 函数 | 简述 |
|---|---|
| [**CanXL_EnableEgressTimeStamp**](../communication/canxl_driver/index.md#731-canxl_enableegresstimestamp) | 在专用的消息对象上激活 egress 时间戳。 |
| [**CanXL_GetControllerMode**](../communication/canxl_driver/index.md#732-canxl_getcontrollermode) | 获取被索引控制器的通信状态。 |
| [**CanXL_GetCounterValues**](../communication/canxl_driver/index.md#733-canxl_getcountervalues) | 读取相应控制器的丢弃计数器值列表。 |
| [**CanXL_GetCurrentTime**](../communication/canxl_driver/index.md#734-canxl_getcurrenttime) | 根据硬件的能力从硬件寄存器返回一个时间值。 |
| [**CanXL_GetCurrentTimeTuple**](../communication/canxl_driver/index.md#735-canxl_getcurrenttimetuple) | 在一个原子操作中读取时间戳时钟的当前时间与 PHC 的当前时间所组成的时间元组（time tuple）。 |
| [**CanXL_GetEgressTimeStamp**](../communication/canxl_driver/index.md#736-canxl_getegresstimestamp) | 在专用的消息对象上读回 egress 时间戳。 |
| [**CanXL_GetIngressTimeStamp**](../communication/canxl_driver/index.md#737-canxl_getingresstimestamp) | 在专用的消息对象上读回 ingress 时间戳。 |
| [**CanXL_GetPhysAddr**](../communication/canxl_driver/index.md#738-canxl_getphysaddr) | 获取被索引控制器所使用的物理源地址。 |
| [**CanXL_GetRxStats**](../communication/canxl_driver/index.md#739-canxl_getrxstats) | 返回依据 IETF RFC2819 的以下列表，其中最大可能取值应表示无效值，例如该计数器不可用时：1. etherStatsDropEvents；2. etherStatsOctets；3. etherStatsPkts；4. et… |
| [**CanXL_GetTxErrorCounterValues**](../communication/canxl_driver/index.md#7310-canxl_gettxerrorcountervalues) | 返回由 Eth_TxErrorCounterValuesType 定义的、来自 IETF RFC1213 和 RFC1643 的发送错误计数器列表，其中最大可能取值应表示无效值，例如该计数器不可用时。 |
| [**CanXL_GetTxStats**](../communication/canxl_driver/index.md#7311-canxl_gettxstats) | 返回由 Eth_TxStatsType 定义的、来自 IETF RFC1213 的发送统计信息列表，其中最大可能取值应表示无效值，例如该计数器不可用时。 |
| [**CanXL_ProvideTxBuffer**](../communication/canxl_driver/index.md#7312-canxl_providetxbuffer) | 提供对与指定优先级相关的队列的发送缓冲区的访问。 |
| [**CanXL_Receive**](../communication/canxl_driver/index.md#7313-canxl_receive) | 从相关队列接收一个帧。 |
| [**CanXL_SetControllerMode**](../communication/canxl_driver/index.md#7314-canxl_setcontrollermode) | 启用/禁用被索引控制器的 Rx/Tx 通信。 |
| [**CanXL_SetPhysAddr**](../communication/canxl_driver/index.md#7315-canxl_setphysaddr) | 设置被索引控制器所使用的物理源地址。 |
| [**CanXL_Transmit**](../communication/canxl_driver/index.md#7316-canxl_transmit) | 触发发送一个先前已填充的发送缓冲区。 |
| [**CanXL_TxConfirmation**](../communication/canxl_driver/index.md#7317-canxl_txconfirmation) | 触发帧发送确认。 |
| [**CanXL_UpdatePhysAddrFilter**](../communication/canxl_driver/index.md#7318-canxl_updatephysaddrfilter) | 向被索引控制器的过滤器中添加物理地址，或从中移除物理地址。 |
| [**CanXL_Write**](../communication/canxl_driver/index.md#7319-canxl_write) | 本函数由 CanIf 调用，用于将一条 CAN XL 报文传递给 CAN XL 驱动程序进行发送。 |

## AUTOSAR CAN XL Transceiver Driver（CAN XL 收发器驱动程序）（6）

来源：[AUTOSAR CAN XL Transceiver Driver（CAN XL 收发器驱动程序）](../communication/canxl_transceiver_driver/index.md) · SWS_CANXLTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**CanXLTrcv_CheckWakeup**](../communication/canxl_transceiver_driver/index.md#736-canxltrcv_checkwakeup) | 在检测到唤醒中断时由 EthIf 调用的服务。 |
| [**CanXLTrcv_GetLinkState**](../communication/canxl_transceiver_driver/index.md#735-canxltrcv_getlinkstate) | 获取被索引收发器的链路状态。 |
| [**CanXLTrcv_GetTransceiverMode**](../communication/canxl_transceiver_driver/index.md#734-canxltrcv_gettransceivermode) | 获取被索引收发器的状态。 |
| [**CanXLTrcv_ReportErrorState**](../communication/canxl_transceiver_driver/index.md#731-canxltrcv_reporterrorstate) | 报告 CAN 错误状态的每一次变化。 |
| [**CanXLTrcv_SetTransceiverMode**](../communication/canxl_transceiver_driver/index.md#733-canxltrcv_settransceivermode) | 启用/禁用被索引的收发器。 |
| [**CanXLTrcv_TransceiverLinkStateRequest**](../communication/canxl_transceiver_driver/index.md#732-canxltrcv_transceiverlinkstaterequest) | 为给定的收发器请求给定的链路状态。 |

## AUTOSAR CanSM（CAN状态管理器）（18）

来源：[AUTOSAR CanSM（CAN状态管理器）](../communication/cansm/index.md) · SWS_CANStateManager

| 函数 | 简述 |
|---|---|
| [**CanSM_CheckTransceiverWakeFlagIndication**](../communication/cansm/index.md#746-cansm_checktransceiverwakeflagindication) | C |
| [**CanSM_ClearTrcvWufFlagIndication**](../communication/cansm/index.md#745-cansm_cleartrcvwufflagindication) | C |
| [**CanSM_ConfirmCtrlPnAvailability**](../communication/cansm/index.md#748-cansm_confirmctrlpnavailability) | C |
| [**CanSM_ConfirmPnAvailability**](../communication/cansm/index.md#747-cansm_confirmpnavailability) | C |
| [**CanSM_ControllerBusOff**](../communication/cansm/index.md#741-cansm_controllerbusoff) | C |
| [**CanSM_ControllerModeIndication**](../communication/cansm/index.md#742-cansm_controllermodeindication) | C |
| [**CanSM_DeInit**](../communication/cansm/index.md#732-cansm_deinit) | C |
| [**CanSM_GetCurrentComMode**](../communication/cansm/index.md#734-cansm_getcurrentcommode) | C |
| [**CanSM_GetVersionInfo**](../communication/cansm/index.md#7371-cansm_getversioninfo) | C |
| [**CanSM_Init**](../communication/cansm/index.md#731-cansm_init) | C |
| [**CanSM_MainFunction**](../communication/cansm/index.md#751-cansm_mainfunction) | C |
| [**CanSM_RequestComMode**](../communication/cansm/index.md#733-cansm_requestcommode) | C |
| [**CanSM_SetBaudrate**](../communication/cansm/index.md#7372-cansm_setbaudrate) | C |
| [**CanSM_SetEcuPassive**](../communication/cansm/index.md#7373-cansm_setecupassive) | C |
| [**CanSM_StartWakeupSource**](../communication/cansm/index.md#735-cansm_startwakeupsource) | C |
| [**CanSM_StopWakeupSource**](../communication/cansm/index.md#736-cansm_stopwakeupsource) | C |
| [**CanSM_TransceiverModeIndication**](../communication/cansm/index.md#743-cansm_transceivermodeindication) | C |
| [**CanSM_TxTimeoutException**](../communication/cansm/index.md#744-cansm_txtimeoutexception) | C |

## AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）（13）

来源：[AUTOSAR Cellular V2X Driver（蜂窝V2X驱动程序）](../communication/cellularv2x_driver/index.md) · SWS_CellularV2XDriver

| 函数 | 简述 |
|---|---|
| [**CV2x_GetBufCV2xPC5RxParams**](../communication/cellularv2x_driver/index.md#739-cv2x_getbufcv2xpc5rxparams) | 读取与接收到的包相关的值。 |
| [**CV2x_GetBufCV2xPC5TxParams**](../communication/cellularv2x_driver/index.md#7310-cv2x_getbufcv2xpc5txparams) | 读取与所发送包的接收方向相关的值。 |
| [**CV2x_GetChanCV2xPC5TxParams**](../communication/cellularv2x_driver/index.md#7312-cv2x_getchancv2xpc5txparams) | 读取与信道接收方向相关的值。 |
| [**CV2x_GetControllerMode**](../communication/cellularv2x_driver/index.md#734-cv2x_getcontrollermode) | 获取被索引控制器的状态。 |
| [**CV2x_GetVersionInfo**](../communication/cellularv2x_driver/index.md#732-cv2x_getversioninfo) | 返回本模块的版本信息。 |
| [**CV2x_Init**](../communication/cellularv2x_driver/index.md#731-cv2x_init) | 初始化 Cellular V2X 驱动程序。 |
| [**CV2x_MainFunction**](../communication/cellularv2x_driver/index.md#751-cv2x_mainfunction) | 支持间接发送（扩展帧时序约束）。 |
| [**CV2x_ProvideTxBuffer**](../communication/cellularv2x_driver/index.md#735-cv2x_providetxbuffer) | 提供对指定控制器发送缓冲区的访问。 |
| [**CV2x_Receive**](../communication/cellularv2x_driver/index.md#738-cv2x_receive) | 触发帧接收。 |
| [**CV2x_SetBufCV2xPC5TxParams**](../communication/cellularv2x_driver/index.md#7311-cv2x_setbufcv2xpc5txparams) | 为特定缓冲区（待发送的包）设置与发送方向相关的值。 |
| [**CV2x_SetControllerMode**](../communication/cellularv2x_driver/index.md#733-cv2x_setcontrollermode) | 启用/禁用被索引的控制器。 |
| [**CV2x_Transmit**](../communication/cellularv2x_driver/index.md#736-cv2x_transmit) | 触发发送一个先前已填充的发送缓冲区。 |
| [**CV2x_TxConfirmation**](../communication/cellularv2x_driver/index.md#737-cv2x_txconfirmation) | 触发发送确认。 |

## AUTOSAR Charging Manager（充电管理器）（17）

来源：[AUTOSAR Charging Manager（充电管理器）](../communication/chargingmanager/index.md) · SWS_ChargingManager

| 函数 | 简述 |
|---|---|
| [**ChrgM_CpLineStatus**](../communication/chargingmanager/index.md#733-chrgm_cplinestatus) | 上层调用本 API 向 ChrgM 通报 CP 线状态。 |
| [**ChrgM_DataLinkIndication**](../communication/chargingmanager/index.md#734-chrgm_datalinkindication) | 本 API 由 EthSM 调用，向 ChrgM 通报数据链路连接的状态。 |
| [**ChrgM_ErrorIndication**](../communication/chargingmanager/index.md#735-chrgm_errorindication) | ChrgM 向上层通报错误。 |
| [**ChrgM_Init**](../communication/chargingmanager/index.md#731-chrgm_init) | 本服务初始化 ChrgM 模块。 |
| [**ChrgM_MainFunction_Rx**](../communication/chargingmanager/index.md#736-chrgm_mainfunction_rx) | 本函数执行 AUTOSAR ChrgM 模块的接收处理。 |
| [**ChrgM_MainFunction_Tx**](../communication/chargingmanager/index.md#737-chrgm_mainfunction_tx) | 本函数执行 AUTOSAR ChrgM 模块的发送处理。 |
| [**ChrgM_PaymentServiceSelectionIndication**](../communication/chargingmanager/index.md#738-chrgm_paymentserviceselectionindication) | ChrgM 向上层通报 SECC 提供的支付方式。 |
| [**ChrgM_SessionSetupIndication**](../communication/chargingmanager/index.md#739-chrgm_sessionsetupindication) | ChrgM 向上层通报 V2G 会话建立信息。 |
| [**ChrgM_SessionStopIndication**](../communication/chargingmanager/index.md#7310-chrgm_sessionstopindication) | ChrgM 向上层通报 V2G 会话的状态。 |
| [**ChrgM_StartProcess**](../communication/chargingmanager/index.md#732-chrgm_startprocess) | 上层调用本 API 以启动充电过程：如果布尔参数设置为 TRUE，ChrgM 将启动 IP 地址分配过程，否则不启动。 |
| [**ChrgM_V2GTpCopyRxData**](../communication/chargingmanager/index.md#7311-chrgm_v2gtpcopyrxdata) | 调用本函数以向上层提供 I-PDU 段（N-PDU）的接收数据。 |
| [**ChrgM_V2GTpCopyTxData**](../communication/chargingmanager/index.md#7312-chrgm_v2gtpcopytxdata) | 调用本函数以获取 I-PDU 段（N-PDU）的发送数据。 |
| [**ChrgM_V2GTpLocalIpAddrAssignmentChg**](../communication/chargingmanager/index.md#741-chrgm_v2gtplocalipaddrassignmentchg) | SoAd 调用本 API 向 ChrgM 通报 IP 地址的状态。 |
| [**ChrgM_V2GTpRxIndication**](../communication/chargingmanager/index.md#742-chrgm_v2gtprxindication) | 在收到 I-PDU 之后（分段情况下为收到最后一个 I-PDU 之后）由下层调用。 |
| [**ChrgM_V2GTpSoConModeChg**](../communication/chargingmanager/index.md#743-chrgm_v2gtpsoconmodechg) | SoAd 调用本 API 向 ChrgM 通报套接字连接的状态。 |
| [**ChrgM_V2GTpStartOfReception**](../communication/chargingmanager/index.md#744-chrgm_v2gtpstartofreception) | 在开始接收 N-SDU 时调用本函数。 |
| [**ChrgM_V2GTpTxConfirmation**](../communication/chargingmanager/index.md#745-chrgm_v2gtptxconfirmation) | 下层调用 ChrgM 的本 API 向 ChrgM 通报所发送 PDU 的状态。 |

## AUTOSAR Chinese V2X Management（中国V2X管理）（4）

来源：[AUTOSAR Chinese V2X Management（中国V2X管理）](../communication/chinesev2x_mgmt/index.md) · SWS_ChineseV2XManagement

| 函数 | 简述 |
|---|---|
| [**CnV2xM_GetChanTxParams**](../communication/chinesev2x_mgmt/index.md#733-cnv2xm_getchantxparams) | 读取与信道接收方向相关的值。 |
| [**CnV2xM_GetVersionInfo**](../communication/chinesev2x_mgmt/index.md#732-cnv2xm_getversioninfo) | 返回本模块的版本信息。 |
| [**CnV2xM_Init**](../communication/chinesev2x_mgmt/index.md#731-cnv2xm_init) | 初始化 CnV2xM 模块。 |
| [**CnV2xM_MainFunction**](../communication/chinesev2x_mgmt/index.md#751-cnv2xm_mainfunction) | CnV2xM 模块的主函数，用于周期性执行协议操作。 |

## AUTOSAR Chinese V2X Message（中国V2X消息）（35）

来源：[AUTOSAR Chinese V2X Message（中国V2X消息）](../communication/chinesev2x_msg/index.md) · SWS_ChineseV2XMessage

| 函数 | 简述 |
|---|---|
| [**CnV2xApplRxIndicationBsm**](../communication/chinesev2x_msg/index.md#7712-cnv2xapplrxindicationbsm) | — |
| [**CnV2xApplRxIndicationMap**](../communication/chinesev2x_msg/index.md#7716-cnv2xapplrxindicationmap) | — |
| [**CnV2xApplRxIndicationRsm**](../communication/chinesev2x_msg/index.md#7714-cnv2xapplrxindicationrsm) | — |
| [**CnV2xApplRxIndicationSpat**](../communication/chinesev2x_msg/index.md#7715-cnv2xapplrxindicationspat) | — |
| [**CnV2xApplRxIndicationzRsi**](../communication/chinesev2x_msg/index.md#7713-cnv2xapplrxindicationzrsi) | — |
| [**CnV2xMsg_AbortPseudonymChange**](../communication/chinesev2x_msg/index.md#738-cnv2xmsg_abortpseudonymchange) | 当并非所有模块都同意假名证书更改且该更改将被回退时，CnV2xSec 模块调用本函数。 |
| [**CnV2xMsg_BsmBs_MainFunction**](../communication/chinesev2x_msg/index.md#751-cnv2xmsg_bsmbs_mainfunction) | 这是 BSM 基本服务的主处理函数。 |
| [**CnV2xMsg_CheckDistance**](../communication/chinesev2x_msg/index.md#734-cnv2xmsg_checkdistance) | 检查当前地理位置点与 CnV2xSec 在海拔 0 处提交假名证书更改时的点之间的距离。 |
| [**CnV2xMsg_CnV2xApplRxIndicationBSM**](../communication/chinesev2x_msg/index.md#7742-cnv2xmsg_cnv2xapplrxindicationbsm) | — |
| [**CnV2xMsg_CnV2xApplRxIndicationMAP**](../communication/chinesev2x_msg/index.md#7747-cnv2xmsg_cnv2xapplrxindicationmap) | — |
| [**CnV2xMsg_CnV2xApplRxIndicationRSI**](../communication/chinesev2x_msg/index.md#7744-cnv2xmsg_cnv2xapplrxindicationrsi) | — |
| [**CnV2xMsg_CnV2xApplRxIndicationRSM**](../communication/chinesev2x_msg/index.md#7745-cnv2xmsg_cnv2xapplrxindicationrsm) | — |
| [**CnV2xMsg_CnV2xApplRxIndicationSPAT**](../communication/chinesev2x_msg/index.md#7746-cnv2xmsg_cnv2xapplrxindicationspat) | — |
| [**CnV2xMsg_CommitPseudonymChange**](../communication/chinesev2x_msg/index.md#737-cnv2xmsg_commitpseudonymchange) | 当所有模块都同意假名证书更改且该更改将被提交时，CnV2xSec 模块调用本函数。 |
| [**CnV2xMsg_DecapConfirmation**](../communication/chinesev2x_msg/index.md#744-cnv2xmsg_decapconfirmation) | 当解封装完成时，CnV2xSec 模块调用本函数。 |
| [**CnV2xMsg_EncapConfirmation**](../communication/chinesev2x_msg/index.md#743-cnv2xmsg_encapconfirmation) | 当封装完成时，V2xSecCN 模块调用本函数。 |
| [**CnV2xMsg_GetRefTimePtr**](../communication/chinesev2x_msg/index.md#733-cnv2xmsg_getreftimeptr) | 提供指向中国 V2X 协议栈时间基准的指针。 |
| [**CnV2xMsg_GetTime32**](../communication/chinesev2x_msg/index.md#739-cnv2xmsg_gettime32) | 获取当前参考时间的服务。 |
| [**CnV2xMsg_GetVehickeEventFlagsStatus**](../communication/chinesev2x_msg/index.md#735-cnv2xmsg_getvehickeeventflagsstatus) | 提供指向当前车辆事件状态的指针。 |
| [**CnV2xMsg_GetVersionInfo**](../communication/chinesev2x_msg/index.md#732-cnv2xmsg_getversioninfo) | 返回本模块的版本信息。 |
| [**CnV2xMsg_Init**](../communication/chinesev2x_msg/index.md#731-cnv2xmsg_init) | 初始化 CnV2xMsg 模块。 |
| [**CnV2xMsg_MapS_MainFunction**](../communication/chinesev2x_msg/index.md#756-cnv2xmsg_maps_mainfunction) | 这是 MAP 服务的主处理函数。 |
| [**CnV2xMsg_Mgt_MainFunction**](../communication/chinesev2x_msg/index.md#752-cnv2xmsg_mgt_mainfunction) | CnV2xMsg 的调度管理函数。 |
| [**CnV2xMsg_Poti**](../communication/chinesev2x_msg/index.md#7743-cnv2xmsg_poti) | — |
| [**CnV2xMsg_PreparePseudonymChange**](../communication/chinesev2x_msg/index.md#736-cnv2xmsg_preparepseudonymchange) | 通过本 API 原语，CnV2xMsg 模块获得一个指示：给定的假名证书以及由此而来的 Msg count 和 Vehicle ID 即将被更改。 |
| [**CnV2xMsg_RsiS_MainFunction**](../communication/chinesev2x_msg/index.md#753-cnv2xmsg_rsis_mainfunction) | 这是 RSI 服务的主处理函数。 |
| [**CnV2xMsg_RsmS_MainFunction**](../communication/chinesev2x_msg/index.md#754-cnv2xmsg_rsms_mainfunction) | 这是 RSM 服务的主处理函数。 |
| [**CnV2xMsg_RxIndication**](../communication/chinesev2x_msg/index.md#742-cnv2xmsg_rxindication) | 通过本 API 原语，CnV2xMsg 模块获得一个确认：具有某一 ID 的 V2X 消息已成功发送。 |
| [**CnV2xMsg_RxS_MainFunction**](../communication/chinesev2x_msg/index.md#757-cnv2xmsg_rxs_mainfunction) | 当接收到的 V2X 消息经 V2xDm 模块发送到应用层或 PDUR 时，这是消息接收服务的主处理函数。 |
| [**CnV2xMsg_SetPositionAndTime**](../communication/chinesev2x_msg/index.md#7310-cnv2xmsg_setpositionandtime) | 用于设置与 V2X-Stack 相关的位置和时间信息的服务。 |
| [**CnV2xMsg_SpatS_MainFunction**](../communication/chinesev2x_msg/index.md#755-cnv2xmsg_spats_mainfunction) | 这是 SPAT 服务的主处理函数。 |
| [**CnV2xMsg_TxConfirmation**](../communication/chinesev2x_msg/index.md#741-cnv2xmsg_txconfirmation) | 通过本 API 原语，CnV2xMsg 模块获得一个确认：具有某一 ID 的 V2X 消息已成功发送。 |
| [**CnV2xMsg_Vdp**](../communication/chinesev2x_msg/index.md#7741-cnv2xmsg_vdp) | — |
| [**CnV2xMsgPoti**](../communication/chinesev2x_msg/index.md#7721-cnv2xmsgpoti) | — |
| [**CnV2xMsgVdp**](../communication/chinesev2x_msg/index.md#7711-cnv2xmsgvdp) | — |

## AUTOSAR Chinese V2X Network（中国V2X网络）（9）

来源：[AUTOSAR Chinese V2X Network（中国V2X网络）](../communication/chinesev2x_net/index.md) · SWS_ChineseV2XNetwork

| 函数 | 简述 |
|---|---|
| [**CnV2xNet_AbortAppLayerIdChange**](../communication/chinesev2x_net/index.md#736-cnv2xnet_abortapplayeridchange) | 当并非所有模块都同意假名证书更改且该更改将被回退时，CnV2xMsg 模块调用本函数。 |
| [**CnV2xNet_CommitAppLayerIdChange**](../communication/chinesev2x_net/index.md#735-cnv2xnet_commitapplayeridchange) | 当所有模块都同意假名证书更改且该更改将被提交时，CnV2xMsg 模块调用本函数。 |
| [**CnV2xNet_GetVersionInfo**](../communication/chinesev2x_net/index.md#732-cnv2xnet_getversioninfo) | 返回本模块的版本信息。 |
| [**CnV2xNet_Init**](../communication/chinesev2x_net/index.md#731-cnv2xnet_init) | 初始化 CnV2xNet 模块。 |
| [**CnV2xNet_PrepareAppLayerIdChange**](../communication/chinesev2x_net/index.md#734-cnv2xnet_prepareapplayeridchange) | 通过本 API 原语，CnV2xNet 模块获得一个指示：应用层 Id 即将更改，因此源 Layer-2 ID 即将更改。 |
| [**CnV2xNet_RxIndication**](../communication/chinesev2x_net/index.md#741-cnv2xnet_rxindication) | 指示以太网帧的接收。 |
| [**CnV2xNet_Transmit**](../communication/chinesev2x_net/index.md#733-cnv2xnet_transmit) | CvxMsgCN 模块调用本 API 以请求向对端网络实体发送一个网络层 V2X PDU。 |
| [**CnV2xNet_TxConfirmation**](../communication/chinesev2x_net/index.md#742-cnv2xnet_txconfirmation) | 确认以太网帧的发送。 |
| [**CnV2xNetMainFunction**](../communication/chinesev2x_net/index.md#751-cnv2xnetmainfunction) | CnV2xNet 模块的主函数，用于周期性执行协议操作。 |

## AUTOSAR Chinese V2X Security（中国V2X安全）（5）

来源：[AUTOSAR Chinese V2X Security（中国V2X安全）](../communication/chinesev2x_sec/index.md) · SWS_ChineseV2XSecurity

| 函数 | 简述 |
|---|---|
| [**CnV2xSec_GetVersionInfo**](../communication/chinesev2x_sec/index.md#732-cnv2xsec_getversioninfo) | 返回本模块的版本信息。 |
| [**CnV2xSec_Init**](../communication/chinesev2x_sec/index.md#731-cnv2xsec_init) | 初始化 CnV2xSec 模块。 |
| [**CnV2xSec_MainFunction**](../communication/chinesev2x_sec/index.md#751-cnv2xsec_mainfunction) | CnV2xSec 的调度主函数。 |
| [**CnV2xSec_ReqDecap**](../communication/chinesev2x_sec/index.md#734-cnv2xsec_reqdecap) | CnV2xMsg 调用本函数以解封装 SPDU。 |
| [**CnV2xSec_ReqEncap**](../communication/chinesev2x_sec/index.md#733-cnv2xsec_reqencap) | CnV2xMsg 调用本函数以生成 SPDU，其中包含 V2X 消息、签名和假名。 |

## AUTOSAR COM Based Transformer（3）

来源：[AUTOSAR COM Based Transformer](../communication/com_based_transformer/index.md) · SWS_COMBasedTransformer

| 函数 | 简述 |
|---|---|
| [**ComXf_DeInit**](../communication/com_based_transformer/index.md#734-comxf_deinit) | 此服务反初始化转换器。 |
| [**ComXf_GetVersionInfo**](../communication/com_based_transformer/index.md#735-comxf_getversioninfo) | 此服务返回被调用的转换器模块的版本信息。 |
| [**ComXf_Init**](../communication/com_based_transformer/index.md#733-comxf_init) | 此服务初始化转换器以进行后续处理。 |

## AUTOSAR Communication Manager（通信管理器）（53）

来源：[AUTOSAR Communication Manager（通信管理器）](../system_services/comm/index.md) · SWS_COMManager

| 函数 | 简述 |
|---|---|
| [**ComM_BusSM_BusSleepMode**](../system_services/comm/index.md#7452-comm_bussm_bussleepmode) | C |
| [**ComM_BusSM_ModeIndication**](../system_services/comm/index.md#7451-comm_bussm_modeindication) | C |
| [**ComM_ChannelLimitation**](../system_services/comm/index.md#7721-comm_channellimitation) | — |
| [**ComM_ChannelWakeup**](../system_services/comm/index.md#7722-comm_channelwakeup) | — |
| [**ComM_CL**](../system_services/comm/index.md#7751-comm_cl) | — |
| [**ComM_CommunicationAllowed**](../system_services/comm/index.md#7441-comm_communicationallowed) | C |
| [**ComM_CR**](../system_services/comm/index.md#7752-comm_cr) | — |
| [**ComM_CurrentChannelRequest**](../system_services/comm/index.md#7711-comm_currentchannelrequest) | — |
| [**ComM_CurrentMode**](../system_services/comm/index.md#7731-comm_currentmode) | — |
| [**ComM_CW**](../system_services/comm/index.md#7753-comm_cw) | — |
| [**ComM_DCM_ActiveDiagnostic**](../system_services/comm/index.md#7421-comm_dcm_activediagnostic) | C |
| [**ComM_DCM_InactiveDiagnostic**](../system_services/comm/index.md#7422-comm_dcm_inactivediagnostic) | C |
| [**ComM_DeInit**](../system_services/comm/index.md#732-comm_deinit) | C |
| [**ComM_DynamicPncToChannelMapping**](../system_services/comm/index.md#7726-comm_dynamicpnctochannelmapping) | — |
| [**ComM_EcuM_PNCWakeUpIndication**](../system_services/comm/index.md#7432-comm_ecum_pncwakeupindication) | C |
| [**ComM_EcuM_WakeUpIndication**](../system_services/comm/index.md#7431-comm_ecum_wakeupindication) | C |
| [**ComM_ECUModeLimitation**](../system_services/comm/index.md#7723-comm_ecumodelimitation) | — |
| [**ComM_GetCurrentComMode**](../system_services/comm/index.md#738-comm_getcurrentcommode) | C |
| [**ComM_GetCurrentPNCComMode**](../system_services/comm/index.md#739-comm_getcurrentpnccommode) | C |
| [**ComM_GetInhibitionStatus**](../system_services/comm/index.md#734-comm_getinhibitionstatus) | C |
| [**ComM_GetMaxComMode**](../system_services/comm/index.md#736-comm_getmaxcommode) | C |
| [**ComM_GetPncToChannelMapping**](../system_services/comm/index.md#7310-comm_getpnctochannelmapping) | C |
| [**ComM_GetRequestedComMode**](../system_services/comm/index.md#737-comm_getrequestedcommode) | C |
| [**ComM_GetStatus**](../system_services/comm/index.md#733-comm_getstatus) | C |
| [**ComM_GetVersionInfo**](../system_services/comm/index.md#7321-comm_getversioninfo) | C |
| [**ComM_Init**](../system_services/comm/index.md#731-comm_init) | C |
| [**ComM_LimitChannelToNoComMode**](../system_services/comm/index.md#7316-comm_limitchanneltonocommode) | C |
| [**ComM_LimitECUToNoComMode**](../system_services/comm/index.md#7317-comm_limitecutonocommode) | C |
| [**ComM_modeLimitation**](../system_services/comm/index.md#7754-comm_modelimitation) | — |
| [**ComM_Nm_BusSleepMode**](../system_services/comm/index.md#7414-comm_nm_bussleepmode) | C |
| [**ComM_Nm_ForwardSynchronizedPncShutdown**](../system_services/comm/index.md#7418-comm_nm_forwardsynchronizedpncshutdown) | C |
| [**ComM_Nm_NetworkMode**](../system_services/comm/index.md#7412-comm_nm_networkmode) | C |
| [**ComM_Nm_NetworkStartIndication**](../system_services/comm/index.md#7411-comm_nm_networkstartindication) | C |
| [**ComM_Nm_PncLearningBitIndication**](../system_services/comm/index.md#7417-comm_nm_pnclearningbitindication) | C |
| [**ComM_Nm_PrepareBusSleepMode**](../system_services/comm/index.md#7413-comm_nm_preparebussleepmode) | C |
| [**ComM_Nm_RepeatMessageLeftIndication**](../system_services/comm/index.md#7416-comm_nm_repeatmessageleftindication) | C |
| [**ComM_Nm_RestartIndication**](../system_services/comm/index.md#7415-comm_nm_restartindication) | C |
| [**ComM_Nm_UpdateEIRA**](../system_services/comm/index.md#7419-comm_nm_updateeira) | C |
| [**ComM_Nm_UpdateERA**](../system_services/comm/index.md#74110-comm_nm_updateera) | C |
| [**ComM_PncToChannelMapping**](../system_services/comm/index.md#7725-comm_pnctochannelmapping) | — |
| [**ComM_PnLearningRequest**](../system_services/comm/index.md#7313-comm_pnlearningrequest) | C |
| [**ComM_PreventWakeUp**](../system_services/comm/index.md#7315-comm_preventwakeup) | C |
| [**ComM_ReadInhibitCounter**](../system_services/comm/index.md#7318-comm_readinhibitcounter) | C |
| [**ComM_RequestComMode**](../system_services/comm/index.md#735-comm_requestcommode) | C |
| [**ComM_ResetInhibitCounter**](../system_services/comm/index.md#7319-comm_resetinhibitcounter) | C |
| [**ComM_ResetPncToChannelMapping**](../system_services/comm/index.md#7312-comm_resetpnctochannelmapping) | C |
| [**ComM_SetECUGroupClassification**](../system_services/comm/index.md#7320-comm_setecugroupclassification) | C |
| [**ComM_UM**](../system_services/comm/index.md#7755-comm_um) | — |
| [**ComM_UpdatePncMembership**](../system_services/comm/index.md#7314-comm_updatepncmembership) | C |
| [**ComM_UpdatePncToChannelMapping**](../system_services/comm/index.md#7311-comm_updatepnctochannelmapping) | C |
| [**ComM_UR**](../system_services/comm/index.md#7756-comm_ur) | — |
| [**ComM_UserRequest**](../system_services/comm/index.md#7724-comm_userrequest) | — |
| [**ComMMode**](../system_services/comm/index.md#7761-commmode) | — |

## AUTOSAR COM（COM模块）（40）

来源：[AUTOSAR COM（COM模块）](../communication/com/index.md) · SWS_COM

| 函数 | 简述 |
|---|---|
| [**Com_CopyRxData**](../communication/com/index.md#7347-com_copyrxdata) | C |
| [**Com_CopyTxData**](../communication/com/index.md#7348-com_copytxdata) | C |
| [**Com_DeInit**](../communication/com/index.md#7322-com_deinit) | C |
| [**Com_DisableReceptionDM**](../communication/com/index.md#7326-com_disablereceptiondm) | C |
| [**Com_EnableReceptionDM**](../communication/com/index.md#7325-com_enablereceptiondm) | C |
| [**Com_GetStatus**](../communication/com/index.md#7327-com_getstatus) | C |
| [**Com_GetVersionInfo**](../communication/com/index.md#7328-com_getversioninfo) | C |
| [**Com_Init**](../communication/com/index.md#7321-com_init) | C |
| [**Com_InvalidateSignal**](../communication/com/index.md#73317-com_invalidatesignal) | C |
| [**Com_InvalidateSignalGroup**](../communication/com/index.md#73318-com_invalidatesignalgroup) | C |
| [**Com_IpduGroupStart**](../communication/com/index.md#7323-com_ipdugroupstart) | C |
| [**Com_IpduGroupStop**](../communication/com/index.md#7324-com_ipdugroupstop) | C |
| [**Com_MainFunctionRouteSignals**](../communication/com/index.md#7353-com_mainfunctionroutesignals) | C |
| [**Com_MainFunctionRx**](../communication/com/index.md#7351-com_mainfunctionrx) | C |
| [**Com_MainFunctionTx**](../communication/com/index.md#7352-com_mainfunctiontx) | C |
| [**Com_ReceiveDynSignal**](../communication/com/index.md#7334-com_receivedynsignal) | C |
| [**Com_ReceiveDynSignalWithMetaData**](../communication/com/index.md#73310-com_receivedynsignalwithmetadata) | C |
| [**Com_ReceiveSignal**](../communication/com/index.md#7333-com_receivesignal) | C |
| [**Com_ReceiveSignalGroup**](../communication/com/index.md#7336-com_receivesignalgroup) | C |
| [**Com_ReceiveSignalGroupArray**](../communication/com/index.md#7338-com_receivesignalgrouparray) | C |
| [**Com_ReceiveSignalGroupArrayWithMetaData**](../communication/com/index.md#73312-com_receivesignalgrouparraywithmetadata) | C |
| [**Com_ReceiveSignalGroupWithMetaData**](../communication/com/index.md#73311-com_receivesignalgroupwithmetadata) | C |
| [**Com_ReceiveSignalWithMetaData**](../communication/com/index.md#7339-com_receivesignalwithmetadata) | C |
| [**Com_RxIndication**](../communication/com/index.md#7342-com_rxindication) | C |
| [**Com_SendDynSignal**](../communication/com/index.md#7332-com_senddynsignal) | C |
| [**Com_SendDynSignalWithMetaData**](../communication/com/index.md#73314-com_senddynsignalwithmetadata) | C |
| [**Com_SendSignal**](../communication/com/index.md#7331-com_sendsignal) | C |
| [**Com_SendSignalGroup**](../communication/com/index.md#7335-com_sendsignalgroup) | C |
| [**Com_SendSignalGroupArray**](../communication/com/index.md#7337-com_sendsignalgrouparray) | C |
| [**Com_SendSignalGroupArrayWithMetaData**](../communication/com/index.md#73316-com_sendsignalgrouparraywithmetadata) | C |
| [**Com_SendSignalGroupWithMetaData**](../communication/com/index.md#73315-com_sendsignalgroupwithmetadata) | C |
| [**Com_SendSignalWithMetaData**](../communication/com/index.md#73313-com_sendsignalwithmetadata) | C |
| [**Com_StartOfReception**](../communication/com/index.md#7346-com_startofreception) | C |
| [**Com_SwitchIpduTxMode**](../communication/com/index.md#73321-com_switchipdutxmode) | C |
| [**Com_TpRxIndication**](../communication/com/index.md#7343-com_tprxindication) | C |
| [**Com_TpTxConfirmation**](../communication/com/index.md#7345-com_tptxconfirmation) | C |
| [**Com_TriggerIPDUSend**](../communication/com/index.md#73319-com_triggeripdusend) | C |
| [**Com_TriggerIPDUSendWithMetaData**](../communication/com/index.md#73320-com_triggeripdusendwithmetadata) | C |
| [**Com_TriggerTransmit**](../communication/com/index.md#7341-com_triggertransmit) | C |
| [**Com_TxConfirmation**](../communication/com/index.md#7344-com_txconfirmation) | C |

## AUTOSAR CoreTest（内核测试）（10）

来源：[AUTOSAR CoreTest（内核测试）](../mcal/core_test/index.md) · SWS_CoreTest

| 函数 | 简述 |
|---|---|
| [**CorTst_Abort**](../mcal/core_test/index.md#733-cortst_abort) | 从 CORTST_INIT 状态转换到 CORTST_ABORT 状态的服务。 |
| [**CorTst_DeInit**](../mcal/core_test/index.md#732-cortst_deinit) | 从 CORTST_ABORT 或 CORTST_INIT 状态转换到 CORTST_UNINIT 状态的服务。 |
| [**CorTst_GetCurrentStatus**](../mcal/core_test/index.md#735-cortst_getcurrentstatus) | 内核测试用于获取上次已执行测试指示的服务。 |
| [**CorTst_GetFgndSignature**](../mcal/core_test/index.md#737-cortst_getfgndsignature) | 获取上次在前台模式下执行的内核测试签名的服务。 |
| [**CorTst_GetSignature**](../mcal/core_test/index.md#736-cortst_getsignature) | 获取上次在后台模式下执行的内核测试签名的服务。 |
| [**CorTst_GetState**](../mcal/core_test/index.md#734-cortst_getstate) | 返回当前执行的内核测试状态的服务。 |
| [**CorTst_GetVersionInfo**](../mcal/core_test/index.md#739-cortst_getversioninfo) | 返回本模块的版本信息的服务。 |
| [**CorTst_Init**](../mcal/core_test/index.md#731-cortst_init) | 用于初始化和更改内核测试状态的服务。 |
| [**CorTst_MainFunction**](../mcal/core_test/index.md#751-cortst_mainfunction) | 由调度器循环调用以执行内核测试的处理。 |
| [**CorTst_Start**](../mcal/core_test/index.md#738-cortst_start) | 执行前台内核测试的服务。 |

## AUTOSAR Crypto Driver（加密驱动程序）（20）

来源：[AUTOSAR Crypto Driver（加密驱动程序）](../crypto/crypto_driver/index.md) · SWS_CryptoDriver

| 函数 | 简述 |
|---|---|
| [**Crypto_CancelJob**](../crypto/crypto_driver/index.md#7331-crypto_canceljob) | 本接口从队列中移除所提供的作业，并尽可能取消该作业的处理。 |
| [**Crypto_CustomSync**](../crypto/crypto_driver/index.md#7351-crypto_customsync) | 请求执行由给定分发 ID 所指定的函数。 |
| [**Crypto_GetVersionInfo**](../crypto/crypto_driver/index.md#7312-crypto_getversioninfo) | 此服务返回本模块的版本信息。 |
| [**Crypto_Init**](../crypto/crypto_driver/index.md#7311-crypto_init) | 此服务初始化加密驱动程序。 |
| [**Crypto_KeyCopy**](../crypto/crypto_driver/index.md#73443-crypto_keycopy) | 将一个密钥及其所有元素复制到同一加密驱动程序中的另一个密钥。 |
| [**Crypto_KeyDerive**](../crypto/crypto_driver/index.md#73461-crypto_keyderive) | 通过使用 cryptoKeyId 所标识给定密钥中的密钥元素来派生新密钥。 |
| [**Crypto_KeyElementCopy**](../crypto/crypto_driver/index.md#73441-crypto_keyelementcopy) | 将一个密钥元素复制到同一加密驱动程序中的另一个密钥元素。 |
| [**Crypto_KeyElementCopyPartial**](../crypto/crypto_driver/index.md#73442-crypto_keyelementcopypartial) | 将一个密钥元素复制到同一加密驱动程序中的另一个密钥元素。 |
| [**Crypto_KeyElementGet**](../crypto/crypto_driver/index.md#73421-crypto_keyelementget) | 本接口用于获取 cryptoKeyId 所标识密钥的密钥元素，并将该密钥元素存储到结果指针所指向的内存位置中。 |
| [**Crypto_KeyElementIdsGet**](../crypto/crypto_driver/index.md#73444-crypto_keyelementidsget) | 用于检索给定密钥中有哪些密钥元素可用的信息。 |
| [**Crypto_KeyElementSet**](../crypto/crypto_driver/index.md#73411-crypto_keyelementset) | 将给定的密钥元素字节设置到 cryptoKeyId 所标识的密钥中。 |
| [**Crypto_KeyExchangeCalcPubVal**](../crypto/crypto_driver/index.md#73471-crypto_keyexchangecalcpubval) | 为密钥交换计算公开值，并将公开密钥存储在公开值指针所指向的内存位置中。 |
| [**Crypto_KeyExchangeCalcSecret**](../crypto/crypto_driver/index.md#73472-crypto_keyexchangecalcsecret) | 使用 cryptoKeyId 所标识密钥的密钥材料和对方的公开密钥，为密钥交换计算共享密钥。 |
| [**Crypto_KeyGenerate**](../crypto/crypto_driver/index.md#73452-crypto_keygenerate) | 生成新的密钥材料，并将其存储到 cryptoKeyId 所标识的密钥中。 |
| [**Crypto_KeyGetStatus**](../crypto/crypto_driver/index.md#73431-crypto_keygetstatus) | 返回 cryptoKeyId 所标识密钥的密钥状态。 |
| [**Crypto_KeySetInvalid**](../crypto/crypto_driver/index.md#73413-crypto_keysetinvalid) | 将 cryptoKeyId 所标识密钥的状态设置为无效。 |
| [**Crypto_KeySetValid**](../crypto/crypto_driver/index.md#73412-crypto_keysetvalid) | 将 cryptoKeyId 所标识密钥的密钥状态设置为有效。 |
| [**Crypto_MainFunction**](../crypto/crypto_driver/index.md#751-crypto_mainfunction) | 如果配置了异步作业处理并且存在作业队列，则该函数会被周期性地调用以处理排队的作业。 |
| [**Crypto_ProcessJob**](../crypto/crypto_driver/index.md#7321-crypto_processjob) | 此服务执行在 job 参数中配置的加密原语。 |
| [**Crypto_RandomSeed**](../crypto/crypto_driver/index.md#73451-crypto_randomseed) | 此函数使用所提供的熵源生成内部种子状态。 |

## AUTOSAR Crypto Interface（加密接口）（19）

来源：[AUTOSAR Crypto Interface（加密接口）](../crypto/crypto_interface/index.md) · SWS_CryptoInterface

| 函数 | 简述 |
|---|---|
| [**CryIf_CallbackNotification**](../crypto/crypto_interface/index.md#741-cryif_callbacknotification) | 将请求的完成情况及加密操作的结果通知 CRYIF。 |
| [**CryIf_CancelJob**](../crypto/crypto_interface/index.md#7331-cryif_canceljob) | 该接口将作业取消函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_CustomSync**](../crypto/crypto_interface/index.md#7351-cryif_customsync) | 请求执行由给定分发 ID 所指定的函数。 |
| [**CryIf_GetVersionInfo**](../crypto/crypto_interface/index.md#7312-cryif_getversioninfo) | 返回本模块的版本信息。 |
| [**CryIf_Init**](../crypto/crypto_interface/index.md#7311-cryif_init) | 初始化 CRYIF 模块。 |
| [**CryIf_KeyCopy**](../crypto/crypto_interface/index.md#73443-cryif_keycopy) | 该函数应将源密钥的所有密钥元素复制到目标密钥。 |
| [**CryIf_KeyDerive**](../crypto/crypto_interface/index.md#73461-cryif_keyderive) | 该函数应将密钥派生函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyElementCopy**](../crypto/crypto_interface/index.md#73441-cryif_keyelementcopy) | 该函数应将一个密钥元素从一个密钥复制到目标密钥。 |
| [**CryIf_KeyElementCopyPartial**](../crypto/crypto_interface/index.md#73442-cryif_keyelementcopypartial) | 将一个密钥元素复制到另一个密钥元素。 |
| [**CryIf_KeyElementGet**](../crypto/crypto_interface/index.md#73431-cryif_keyelementget) | 该函数应将获取密钥元素函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyElementSet**](../crypto/crypto_interface/index.md#73411-cryif_keyelementset) | 该函数应将设置密钥元素函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyExchangeCalcPubVal**](../crypto/crypto_interface/index.md#73471-cryif_keyexchangecalcpubval) | 该函数应将密钥交换公开值计算函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyExchangeCalcSecret**](../crypto/crypto_interface/index.md#73472-cryif_keyexchangecalcsecret) | 该函数应将密钥交换公共共享密钥计算函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyGenerate**](../crypto/crypto_interface/index.md#73452-cryif_keygenerate) | 该函数应将密钥生成函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_KeyGetStatus**](../crypto/crypto_interface/index.md#73421-cryif_keygetstatus) | 返回 cryIfKeyId 所标识密钥的密钥状态。 |
| [**CryIf_KeySetInvalid**](../crypto/crypto_interface/index.md#73413-cryif_keysetinvalid) | 将 cryIfKeyId 所标识密钥的状态设置为无效。 |
| [**CryIf_KeySetValid**](../crypto/crypto_interface/index.md#73412-cryif_keysetvalid) | 该函数应将设置密钥有效函数分发给已配置的加密驱动程序对象。 |
| [**CryIf_ProcessJob**](../crypto/crypto_interface/index.md#7321-cryif_processjob) | 该接口将接收到的作业分发给已配置的加密驱动程序对象。 |
| [**CryIf_RandomSeed**](../crypto/crypto_interface/index.md#73451-cryif_randomseed) | 该函数应将随机种子函数分发给已配置的加密驱动程序对象。 |

## AUTOSAR Crypto Service Manager（加密服务管理器）（58）

来源：[AUTOSAR Crypto Service Manager（加密服务管理器）](../crypto/crypto_service_manager/index.md) · SWS_CryptoServiceManager

| 函数 | 简述 |
|---|---|
| [**CallbackNotification**](../crypto/crypto_service_manager/index.md#7551-callbacknotification) | — |
| [**Csm_AEADDecrypt**](../crypto/crypto_service_manager/index.md#7352-csm_aeaddecrypt) | 使用给定数据执行 AEAD 加密，并将密文和 MAC 存储在密文指针和 Tag 指针指向的内存位置。 |
| [**Csm_AEADEncrypt**](../crypto/crypto_service_manager/index.md#7351-csm_aeadencrypt) | 使用给定的输入数据执行 AEAD 加密，并将密文和 MAC 存储在密文指针和 Tag 指针指向的内存位置。 |
| [**Csm_CallbackNotification**](../crypto/crypto_service_manager/index.md#73131-csm_callbacknotification) | 通知 CSM 作业已完成。 |
| [**Csm_CancelJob**](../crypto/crypto_service_manager/index.md#73111-csm_canceljob) | 取消异步或流作业的作业处理。 |
| [**Csm_CustomService**](../crypto/crypto_service_manager/index.md#73121-csm_customservice) | 分发安全相关作业以在安全环境中进行自定义执行。 |
| [**Csm_CustomSync**](../crypto/crypto_service_manager/index.md#73122-csm_customsync) | 请求执行由给定分发 ID 所指定的函数。 |
| [**Csm_Decrypt**](../crypto/crypto_service_manager/index.md#7342-csm_decrypt) | 解密给定的加密数据，并将解密后的明文存储在结果指针指向的内存位置。 |
| [**Csm_Encrypt**](../crypto/crypto_service_manager/index.md#7341-csm_encrypt) | 加密给定数据并将密文存储在结果指针指向的内存位置。 |
| [**Csm_GetVersionInfo**](../crypto/crypto_service_manager/index.md#7312-csm_getversioninfo) | 返回此模块的版本信息。 |
| [**Csm_Hash**](../crypto/crypto_service_manager/index.md#7321-csm_hash) | 使用给定的数据执行哈希计算并存储哈希。 |
| [**Csm_Init**](../crypto/crypto_service_manager/index.md#7311-csm_init) | 初始化 CSM 模块。 |
| [**Csm_JobKeyDerive**](../crypto/crypto_service_manager/index.md#7395-csm_jobkeyderive) | 使用由 keyId 标识的给定密钥中的密钥元素派生新密钥。 |
| [**Csm_JobKeyExchangeCalcPubVal**](../crypto/crypto_service_manager/index.md#7396-csm_jobkeyexchangecalcpubval) | 计算当前用户用于密钥交换的公钥，并将公钥存储在公钥指针指向的内存位置。 |
| [**Csm_JobKeyExchangeCalcSecret**](../crypto/crypto_service_manager/index.md#7397-csm_jobkeyexchangecalcsecret) | 计算共享密钥，用于与由keyId标识的密钥的密钥材料和伙伴公钥进行密钥交换。 |
| [**Csm_JobKeyGenerate**](../crypto/crypto_service_manager/index.md#7394-csm_jobkeygenerate) | 生成新的密钥材料并将其存储在由 keyId 标识的密钥中。 |
| [**Csm_JobKeySetInvalid**](../crypto/crypto_service_manager/index.md#7392-csm_jobkeysetinvalid) | 将密钥状态设置为无效。 |
| [**Csm_JobKeySetValid**](../crypto/crypto_service_manager/index.md#7391-csm_jobkeysetvalid) | 必要时存储密钥，并将 keyId 标识的密钥的密钥状态设置为有效。 |
| [**Csm_JobRandomSeed**](../crypto/crypto_service_manager/index.md#7393-csm_jobrandomseed) | 为用于关联随机数生成器的指定密钥提供新种子。 |
| [**Csm_KeyCopy**](../crypto/crypto_service_manager/index.md#73842-csm_keycopy) | 此函数将所有密钥元素从源密钥复制到目标密钥。 |
| [**Csm_KeyDerive**](../crypto/crypto_service_manager/index.md#73861-csm_keyderive) | 使用由 keyId 标识的给定密钥中的密钥元素派生新密钥。 |
| [**Csm_KeyElementCopy**](../crypto/crypto_service_manager/index.md#73841-csm_keyelementcopy) | 此函数将密钥元素从一个密钥复制到目标键。 |
| [**Csm_KeyElementCopyPartial**](../crypto/crypto_service_manager/index.md#73843-csm_keyelementcopypartial) | 将一个密钥元素复制到同一加密驱动程序中的另一个密钥元素。 |
| [**Csm_KeyElementGet**](../crypto/crypto_service_manager/index.md#73831-csm_keyelementget) | 从由 keyId 标识的密钥的特定密钥元素中检索密钥元素字节，并将密钥元素存储在密钥指针指向的内存位置。 |
| [**Csm_KeyElementSet**](../crypto/crypto_service_manager/index.md#73811-csm_keyelementset) | 将给定的密钥元素字节设置为由 keyId 标识的键。 |
| [**Csm_KeyExchangeCalcPubVal**](../crypto/crypto_service_manager/index.md#73871-csm_keyexchangecalcpubval) | 计算当前用户用于密钥交换的公钥，并将公钥存储在公钥指针指向的内存位置。 |
| [**Csm_KeyExchangeCalcSecret**](../crypto/crypto_service_manager/index.md#73872-csm_keyexchangecalcsecret) | 计算共享密钥，用于与由keyId标识的密钥的密钥材料和伙伴公钥进行密钥交换。 |
| [**Csm_KeyGenerate**](../crypto/crypto_service_manager/index.md#73852-csm_keygenerate) | 生成新的密钥材料并将其存储在由 keyId 标识的密钥中。 |
| [**Csm_KeyGetStatus**](../crypto/crypto_service_manager/index.md#73821-csm_keygetstatus) | 返回由 keyId 标识的密钥的密钥状态。 |
| [**Csm_KeySetInvalid**](../crypto/crypto_service_manager/index.md#73813-csm_keysetinvalid) | 将密钥状态设置为无效。 |
| [**Csm_KeySetValid**](../crypto/crypto_service_manager/index.md#73812-csm_keysetvalid) | 将由 keyId 标识的密钥的密钥状态设置为有效。 |
| [**Csm_MacGenerate**](../crypto/crypto_service_manager/index.md#7331-csm_macgenerate) | 使用给定数据执行 MAC 生成并将 MAC 存储在 MAC 指针指向的内存位置。 |
| [**Csm_MacVerify**](../crypto/crypto_service_manager/index.md#7332-csm_macverify) | 通过比较是否使用给定数据生成 MAC 来验证给定的 MAC。 |
| [**Csm_MainFunction**](../crypto/crypto_service_manager/index.md#73141-csm_mainfunction) | 此 API 被周期性的调用以处理请求的作业。 |
| [**Csm_RandomGenerate**](../crypto/crypto_service_manager/index.md#7371-csm_randomgenerate) | 产生一个随机数，存放在结果指针指向的内存位置。 |
| [**Csm_RandomSeed**](../crypto/crypto_service_manager/index.md#73851-csm_randomseed) | 为密钥元素 CRYPTO_KE_RANDOM_SEED 提供随机种子。 |
| [**Csm_RestoreContextJob**](../crypto/crypto_service_manager/index.md#73102-csm_restorecontextjob) | 加密驱动程序从 contextBuffer 中提取上下文数据并恢复内部状态，以便此加密服务的进一步加密操作将在获取上下文的确切时间点继续。 |
| [**Csm_SaveContextJob**](../crypto/crypto_service_manager/index.md#73101-csm_savecontextjob) | 加密驱动程序将相应加密操作的内部上下文存储到 contextBuffer。 |
| [**Csm_SignatureGenerate**](../crypto/crypto_service_manager/index.md#7361-csm_signaturegenerate) | 使用给定的数据进行签名计算，并将签名存储在结果指针指向的内存位置。 |
| [**Csm_SignatureVerify**](../crypto/crypto_service_manager/index.md#7362-csm_signatureverify) | 通过比较是否使用给定数据生成签名来验证给定的 MAC。 |
| [**CsmAEADDecrypt**](../crypto/crypto_service_manager/index.md#7527-csmaeaddecrypt) | — |
| [**CsmAEADEncrypt**](../crypto/crypto_service_manager/index.md#7526-csmaeadencrypt) | — |
| [**CsmCustom**](../crypto/crypto_service_manager/index.md#75211-csmcustom) | — |
| [**CsmDecrypt**](../crypto/crypto_service_manager/index.md#7525-csmdecrypt) | — |
| [**CsmEncrypt**](../crypto/crypto_service_manager/index.md#7524-csmencrypt) | — |
| [**CsmHash**](../crypto/crypto_service_manager/index.md#7521-csmhash) | — |
| [**CsmJobKeyDerive**](../crypto/crypto_service_manager/index.md#7535-csmjobkeyderive) | — |
| [**CsmJobKeyExchangeCalcPubVal**](../crypto/crypto_service_manager/index.md#7536-csmjobkeyexchangecalcpubval) | — |
| [**CsmJobKeyExchangeCalcSecret**](../crypto/crypto_service_manager/index.md#7537-csmjobkeyexchangecalcsecret) | — |
| [**CsmJobKeyGenerate**](../crypto/crypto_service_manager/index.md#7534-csmjobkeygenerate) | — |
| [**CsmJobKeySetInvalid**](../crypto/crypto_service_manager/index.md#7532-csmjobkeysetinvalid) | — |
| [**CsmJobKeySetValid**](../crypto/crypto_service_manager/index.md#7531-csmjobkeysetvalid) | — |
| [**CsmJobRandomSeed**](../crypto/crypto_service_manager/index.md#7533-csmjobrandomseed) | — |
| [**CsmMacGenerate**](../crypto/crypto_service_manager/index.md#7522-csmmacgenerate) | — |
| [**CsmMacVerify**](../crypto/crypto_service_manager/index.md#7523-csmmacverify) | — |
| [**CsmRandomGenerate**](../crypto/crypto_service_manager/index.md#75210-csmrandomgenerate) | — |
| [**CsmSignatureGenerate**](../crypto/crypto_service_manager/index.md#7528-csmsignaturegenerate) | — |
| [**CsmSignatureVerify**](../crypto/crypto_service_manager/index.md#7529-csmsignatureverify) | — |

## Data Distribution Service for Classic Platform（经典平台数据分发服务）（8）

来源：[Data Distribution Service for Classic Platform（经典平台数据分发服务）](../communication/data_distribution/index.md) · SWS_DataDistributionService

| 函数 | 简述 |
|---|---|
| [**Dds_GetVersionInfo**](../communication/data_distribution/index.md#732-dds_getversioninfo) | 返回本模块的版本信息。 |
| [**Dds_Init**](../communication/data_distribution/index.md#731-dds_init) | 初始化 AUTOSAR Dds 层的接口和变量。 |
| [**Dds_MainFunction_Rx**](../communication/data_distribution/index.md#751-dds_mainfunction_rx) | Dds 模块用于接收的调度函数。 |
| [**Dds_MainFunction_Tx**](../communication/data_distribution/index.md#752-dds_mainfunction_tx) | Dds 模块用于发送的调度函数。 |
| [**Dds_RxIndication**](../communication/data_distribution/index.md#741-dds_rxindication) | 指示从 PDU 路由器接口模块接收到一个 PDU。 |
| [**Dds_Transmit**](../communication/data_distribution/index.md#733-dds_transmit) | 请求发送一条消息。 |
| [**Dds_TriggerTransmit**](../communication/data_distribution/index.md#743-dds_triggertransmit) | 在该 API 中，上层模块（被调用模块）应检查可用数据是否适合 PduInfoPtr->SduLength 所报告的缓冲区大小。 |
| [**Dds_TxConfirmation**](../communication/data_distribution/index.md#742-dds_txconfirmation) | PDU 路由器接口模块确认一个 PDU 的发送，或发送失败。 |

## AUTOSAR Default Error Tracer（默认错误跟踪器）（7）

来源：[AUTOSAR Default Error Tracer（默认错误跟踪器）](../system_services/default_error_tracer/index.md) · SWS_DefaultErrorTracer

| 函数 | 简述 |
|---|---|
| [**API**](../system_services/default_error_tracer/index.md#71-api) | — |
| [**Det_GetVersionInfo**](../system_services/default_error_tracer/index.md#7136-det_getversioninfo) | 返回本模块的版本信息。 |
| [**Det_Init**](../system_services/default_error_tracer/index.md#7131-det_init) | 此服务初始化默认错误跟踪器。 |
| [**Det_ReportError**](../system_services/default_error_tracer/index.md#7132-det_reporterror) | 此服务报告开发错误。 |
| [**Det_ReportRuntimeError**](../system_services/default_error_tracer/index.md#7134-det_reportruntimeerror) | 此服务报告运行时错误。 |
| [**Det_ReportTransientFault**](../system_services/default_error_tracer/index.md#7135-det_reporttransientfault) | 此服务报告瞬态故障。 |
| [**Det_Start**](../system_services/default_error_tracer/index.md#7133-det_start) | 此服务启动默认错误跟踪器。 |

## AUTOSAR Diagnostic Communication Manager（诊断通信管理器）（96）

来源：[AUTOSAR Diagnostic Communication Manager（诊断通信管理器）](../diagnostics/diagnostic_communication_manager/index.md) · SWS_DiagnosticCommunicationManager

| 函数 | 简述 |
|---|---|
| [**CallbackDCMRequestServices**](../diagnostics/diagnostic_communication_manager/index.md#787-callbackdcmrequestservices) | — |
| [**ClearDTCCheckFnc**](../diagnostics/diagnostic_communication_manager/index.md#789-cleardtccheckfnc) | — |
| [**DataServices**](../diagnostics/diagnostic_communication_manager/index.md#782-dataservices) | — |
| [**DataServices_DIDRange**](../diagnostics/diagnostic_communication_manager/index.md#783-dataservices_didrange) | — |
| [**Dcm_AuthenticationStateModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#7977-dcm_authenticationstatemodeswitchinterface) | — |
| [**Dcm_AuthenticationStateMSI**](../diagnostics/diagnostic_communication_manager/index.md#79522-dcm_authenticationstatemsi) | — |
| [**Dcm_BndMWriteBlockFinish**](../diagnostics/diagnostic_communication_manager/index.md#7315-dcm_bndmwriteblockfinish) | 由 BndM 调用，用于指示一次块写操作已结束。 |
| [**Dcm_ComM_FullComModeEntered**](../diagnostics/diagnostic_communication_manager/index.md#749-dcm_comm_fullcommodeentered) | 该调用向 Dcm 模块通知 ComM 模式已变更为 COMM_FULL_COMMUNICATION。 |
| [**Dcm_ComM_NoComModeEntered**](../diagnostics/diagnostic_communication_manager/index.md#747-dcm_comm_nocommodeentered) | 该调用向 Dcm 模块通知 ComM 模式已变更为 COMM_NO_COMMUNICATION。 |
| [**Dcm_ComM_SilentComModeEntered**](../diagnostics/diagnostic_communication_manager/index.md#748-dcm_comm_silentcommodeentered) | 该调用向 Dcm 模块通知 ComM 模式已变更为 COMM_SILENT_COMMUNICATION。 |
| [**Dcm_CommunicationControlModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#7974-dcm_communicationcontrolmodeswitchinterface) | — |
| [**Dcm_ControlDTCSettingModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#79518-dcm_controldtcsettingmodeswitchinterface) | — |
| [**Dcm_CopyRxData**](../diagnostics/diagnostic_communication_manager/index.md#742-dcm_copyrxdata) | 调用该函数以向上层提供某个 I-PDU 段（N-PDU）的已接收数据。 |
| [**Dcm_CopyTxData**](../diagnostics/diagnostic_communication_manager/index.md#744-dcm_copytxdata) | 调用该函数以获取某个 I-PDU 段（N-PDU）的发送数据。 |
| [**Dcm_CsmAsyncJobFinished**](../diagnostics/diagnostic_communication_manager/index.md#7410-dcm_csmasyncjobfinished) | 可在 Csm 完成一次异步作业处理时由 Csm 调用。 |
| [**Dcm_DemTriggerOnDTCStatus**](../diagnostics/diagnostic_communication_manager/index.md#7313-dcm_demtriggerondtcstatus) | 在 UDS 状态字节发生变化时触发。 |
| [**Dcm_DiagnosticSessionControlModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#79514-dcm_diagnosticsessioncontrolmodeswitchinterface) | — |
| [**Dcm_EcuResetModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#79515-dcm_ecuresetmodeswitchinterface) | — |
| [**Dcm_GetProgConditions**](../diagnostics/diagnostic_communication_manager/index.md#754-dcm_getprogconditions) | Dcm_GetProgConditions Callout 在 Dcm 初始化时被调用，用于确定是否必须发送响应（$50 或 $51）。 |
| [**Dcm_GetSecurityLevel**](../diagnostics/diagnostic_communication_manager/index.md#7322-dcm_getsecuritylevel) | 该函数提供活动的安全等级值。 |
| [**Dcm_GetSesCtrlType**](../diagnostics/diagnostic_communication_manager/index.md#7323-dcm_getsesctrltype) | 该函数提供活动的会话控制类型值。 |
| [**Dcm_GetVersionInfo**](../diagnostics/diagnostic_communication_manager/index.md#7312-dcm_getversioninfo) | 返回本模块的版本信息。 |
| [**Dcm_GetVin**](../diagnostics/diagnostic_communication_manager/index.md#7314-dcm_getvin) | 获取 VIN 的函数（按 SAE J1979-DA 定义）。 |
| [**Dcm_Init**](../diagnostics/diagnostic_communication_manager/index.md#7311-dcm_init) | DCM 模块的基本初始化服务。 |
| [**Dcm_KeyMAsyncCertificateVerifyFinished**](../diagnostics/diagnostic_communication_manager/index.md#7411-dcm_keymasynccertificateverifyfinished) | 可在 KeyM 完成一次异步证书校验时由 KeyM 调用。 |
| [**Dcm_MainFunction**](../diagnostics/diagnostic_communication_manager/index.md#761-dcm_mainfunction) | 该服务用于处理主循环的任务。 |
| [**Dcm_ModeRapidPowerShutDownModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#79516-dcm_moderapidpowershutdownmodeswitchinterface) | — |
| [**Dcm_ProcessRequestAddFile**](../diagnostics/diagnostic_communication_manager/index.md#755-dcm_processrequestaddfile) | Callout 函数。 |
| [**Dcm_ProcessRequestDeleteFile**](../diagnostics/diagnostic_communication_manager/index.md#756-dcm_processrequestdeletefile) | Callout 函数。 |
| [**Dcm_ProcessRequestDownload**](../diagnostics/diagnostic_communication_manager/index.md#75121-dcm_processrequestdownload) | Callout 函数。 |
| [**Dcm_ProcessRequestReadDir**](../diagnostics/diagnostic_communication_manager/index.md#759-dcm_processrequestreaddir) | Callout 函数。 |
| [**Dcm_ProcessRequestReadFile**](../diagnostics/diagnostic_communication_manager/index.md#758-dcm_processrequestreadfile) | Callout 函数。 |
| [**Dcm_ProcessRequestReplaceFile**](../diagnostics/diagnostic_communication_manager/index.md#757-dcm_processrequestreplacefile) | Callout 函数。 |
| [**Dcm_ProcessRequestTransferExit**](../diagnostics/diagnostic_communication_manager/index.md#75122-dcm_processrequesttransferexit) | Callout 函数。 |
| [**Dcm_ProcessRequestUpload**](../diagnostics/diagnostic_communication_manager/index.md#75123-dcm_processrequestupload) | Callout 函数。 |
| [**Dcm_ProcessTransferDataRead**](../diagnostics/diagnostic_communication_manager/index.md#75124-dcm_processtransferdataread) | ProcessTransferDataRead Callout 用于从 UDS 请求消息中请求由参数 memoryAddress 与 memorySize 标识的存储器数据。 |
| [**Dcm_ProcessTransferDataWrite**](../diagnostics/diagnostic_communication_manager/index.md#75125-dcm_processtransferdatawrite) | ProcessTransferDataWrite Callout 用于写入由参数 memoryAddress 与 memorySize 标识的存储器数据。 |
| [**Dcm_ReadFileOrDir**](../diagnostics/diagnostic_communication_manager/index.md#7511-dcm_readfileordir) | Callout 函数。 |
| [**Dcm_ReadMemory**](../diagnostics/diagnostic_communication_manager/index.md#751-dcm_readmemory) | Dcm_ReadMemory Callout 用于从 UDS 请求消息中读取由参数 memoryAddress 与 memorySize 标识的存储器数据。 |
| [**Dcm_ResetToDefaultSession**](../diagnostics/diagnostic_communication_manager/index.md#7324-dcm_resettodefaultsession) | 调用该函数允许应用将当前会话复位为默认会话。 |
| [**Dcm_SecurityAccessModeSwitchInterface**](../diagnostics/diagnostic_communication_manager/index.md#79519-dcm_securityaccessmodeswitchinterface) | — |
| [**Dcm_SetActiveDiagnostic**](../diagnostics/diagnostic_communication_manager/index.md#7325-dcm_setactivediagnostic) | 允许激活和停用对 ComM_DCM_ActiveDiagnostic() 函数的调用。 |
| [**Dcm_SetDeauthenticatedRole**](../diagnostics/diagnostic_communication_manager/index.md#7321-dcm_setdeauthenticatedrole) | 为该连接设置在去认证状态下使用的新角色。 |
| [**Dcm_SetProgConditions**](../diagnostics/diagnostic_communication_manager/index.md#753-dcm_setprogconditions) | Dcm_SetProgConditions Callout 允许集成方在跳转到 Bootloader / 因 ECUReset 请求而跳转之前存储相关信息。 |
| [**Dcm_StartOfReception**](../diagnostics/diagnostic_communication_manager/index.md#741-dcm_startofreception) | 在开始接收一个 N-SDU 时调用该函数。 |
| [**Dcm_TpRxIndication**](../diagnostics/diagnostic_communication_manager/index.md#743-dcm_tprxindication) | 在通过 TP API 接收到一个 I-PDU 之后调用，结果指示该传输是否成功。 |
| [**Dcm_TpTxConfirmation**](../diagnostics/diagnostic_communication_manager/index.md#745-dcm_tptxconfirmation) | 在 I-PDU 已在其网络上发送之后调用该函数，结果指示该传输是否成功。 |
| [**Dcm_TxConfirmation**](../diagnostics/diagnostic_communication_manager/index.md#746-dcm_txconfirmation) | 下层通信接口模块确认某个 PDU 已发送，或确认某个 PDU 发送失败。 |
| [**Dcm_UploadDownloadServices**](../diagnostics/diagnostic_communication_manager/index.md#79520-dcm_uploaddownloadservices) | — |
| [**Dcm_WriteFile**](../diagnostics/diagnostic_communication_manager/index.md#7510-dcm_writefile) | Callout 函数。 |
| [**Dcm_WriteMemory**](../diagnostics/diagnostic_communication_manager/index.md#752-dcm_writememory) | Dcm_WriteMemory Callout 用于写入由参数 memoryAddress 与 memorySize 标识的存储器数据。 |
| [**DcmAuthenticationState**](../diagnostics/diagnostic_communication_manager/index.md#7967-dcmauthenticationstate) | — |
| [**DcmCommunicationControl**](../diagnostics/diagnostic_communication_manager/index.md#7964-dcmcommunicationcontrol) | — |
| [**DcmControlDTCSetting**](../diagnostics/diagnostic_communication_manager/index.md#7965-dcmcontroldtcsetting) | — |
| [**DcmDiagnosticSessionControl**](../diagnostics/diagnostic_communication_manager/index.md#7961-dcmdiagnosticsessioncontrol) | — |
| [**DcmEcuReset**](../diagnostics/diagnostic_communication_manager/index.md#7962-dcmecureset) | — |
| [**DcmModeRapidPowerShutDown**](../diagnostics/diagnostic_communication_manager/index.md#7963-dcmmoderapidpowershutdown) | — |
| [**DcmSecurityAccess**](../diagnostics/diagnostic_communication_manager/index.md#7966-dcmsecurityaccess) | — |
| [**DCMServices**](../diagnostics/diagnostic_communication_manager/index.md#79310-dcmservices) | — |
| [**DsdInternal_ProcessPage**](../diagnostics/diagnostic_communication_manager/index.md#7118-dsdinternal_processpage) | — |
| [**DsdInternal_StartPagedProcessing**](../diagnostics/diagnostic_communication_manager/index.md#7116-dsdinternal_startpagedprocessing) | — |
| [**DslInternal_ResponseOnOneDataByPeriodicId**](../diagnostics/diagnostic_communication_manager/index.md#7115-dslinternal_responseononedatabyperiodicid) | — |
| [**DslInternal_ResponseOnOneEvent**](../diagnostics/diagnostic_communication_manager/index.md#7114-dslinternal_responseononeevent) | — |
| [**DslInternal_SetSecurityLevel**](../diagnostics/diagnostic_communication_manager/index.md#7111-dslinternal_setsecuritylevel) | — |
| [**DslInternal_SetSesCtrlType**](../diagnostics/diagnostic_communication_manager/index.md#7112-dslinternal_setsesctrltype) | — |
| [**DspInternal_CancelPagedBufferProcessing**](../diagnostics/diagnostic_communication_manager/index.md#7117-dspinternal_cancelpagedbufferprocessing) | — |
| [**DspInternal_DcmConfirmation**](../diagnostics/diagnostic_communication_manager/index.md#7113-dspinternal_dcmconfirmation) | — |
| [**InfoTypesServices**](../diagnostics/diagnostic_communication_manager/index.md#784-infotypesservices) | — |
| [**RequestControlServices**](../diagnostics/diagnostic_communication_manager/index.md#786-requestcontrolservices) | — |
| [**RoutineServices**](../diagnostics/diagnostic_communication_manager/index.md#785-routineservices) | — |
| [**SecurityAccess**](../diagnostics/diagnostic_communication_manager/index.md#781-securityaccess) | — |
| [**ServiceRequestNotification**](../diagnostics/diagnostic_communication_manager/index.md#788-servicerequestnotification) | — |
| [**UploadDownloadServices**](../diagnostics/diagnostic_communication_manager/index.md#7512-uploaddownloadservices) | — |
| [**Xxx_ClearDTCCheckFnc**](../diagnostics/diagnostic_communication_manager/index.md#7891-xxx_cleardtccheckfnc) | 用于条件检查的 Callout 函数，对请求清除的 groupOfDTC 执行制造商/供应商特定的检查。 |
| [**Xxx_CompareKey**](../diagnostics/diagnostic_communication_manager/index.md#7812-xxx_comparekey) | 向应用请求异步比较密钥（DcmDspSecurityUsePort = USE_ASYNCH_CLIENT_SERVER）。 |
| [**Xxx_ConditionCheckRead**](../diagnostics/diagnostic_communication_manager/index.md#7824-xxx_conditioncheckread) | 该函数向应用询问读取该 Data 的条件是否满足。 |
| [**Xxx_Confirmation**](../diagnostics/diagnostic_communication_manager/index.md#7882-xxx_confirmation) | 该函数向应用确认某个诊断服务已成功发送或发送出错。 |
| [**Xxx_FreezeCurrentState**](../diagnostics/diagnostic_communication_manager/index.md#7828-xxx_freezecurrentstate) | — |
| [**Xxx_GetInfotypeValueData**](../diagnostics/diagnostic_communication_manager/index.md#7841-xxx_getinfotypevaluedata) | 该函数提供与所请求 InfoType 相关的数据。 |
| [**Xxx_GetScalingInformation**](../diagnostics/diagnostic_communication_manager/index.md#7825-xxx_getscalinginformation) | 该函数向应用请求某个 Data 的定标信息。 |
| [**Xxx_GetSecurityAttemptCounter**](../diagnostics/diagnostic_communication_manager/index.md#7813-xxx_getsecurityattemptcounter) | 从应用读取特定安全等级的尝试计数器。 |
| [**Xxx_GetSeed**](../diagnostics/diagnostic_communication_manager/index.md#7811-xxx_getseed) | 向应用请求异步提供种子值。 |
| [**Xxx_Indication**](../diagnostics/diagnostic_communication_manager/index.md#7881-xxx_indication) | 该函数向应用指示某个服务即将被执行，并允许应用拒绝执行该服务请求。 |
| [**Xxx_IsDidAvailable**](../diagnostics/diagnostic_communication_manager/index.md#7831-xxx_isdidavailable) | 该函数询问某个特定 DID 是否在该范围内可用。 |
| [**Xxx_ReadData**](../diagnostics/diagnostic_communication_manager/index.md#7821-xxx_readdata) | 若 DcmDspDataUsePort 设置为 USE_DATA_SYNCH_CLIENT_SERVER，该函数向应用请求某个 DID/PID 的数据值。 |
| [**Xxx_ReadDataLength**](../diagnostics/diagnostic_communication_manager/index.md#7823-xxx_readdatalength) | 该函数请求应用返回某个 Data 的字节长度。 |
| [**Xxx_ReadDidData**](../diagnostics/diagnostic_communication_manager/index.md#7832-xxx_readdiddata) | 该函数向应用请求某个 DID 的数据值。 |
| [**Xxx_ReadDidRangeDataLength**](../diagnostics/diagnostic_communication_manager/index.md#7834-xxx_readdidrangedatalength) | 该函数请求应用返回某个 DID 范围的数据长度。 |
| [**Xxx_ResetToDefault**](../diagnostics/diagnostic_communication_manager/index.md#7827-xxx_resettodefault) | 该函数请求应用将某个 IOControl 复位为默认值。 |
| [**Xxx_ReturnControlToECU**](../diagnostics/diagnostic_communication_manager/index.md#7826-xxx_returncontroltoecu) | 该函数请求应用将某个 IOControl 的控制权交还给 ECU。 |
| [**Xxx_SetSecurityAttemptCounter**](../diagnostics/diagnostic_communication_manager/index.md#7814-xxx_setsecurityattemptcounter) | 在应用中设置特定安全等级的尝试计数器。 |
| [**Xxx_ShortTermAdjustment**](../diagnostics/diagnostic_communication_manager/index.md#7829-xxx_shorttermadjustment) | — |
| [**Xxx_StartProtocol**](../diagnostics/diagnostic_communication_manager/index.md#7871-xxx_startprotocol) | 该函数允许应用检查环境条件并启用/禁用对该协议的进一步处理。 |
| [**Xxx_StopProtocol**](../diagnostics/diagnostic_communication_manager/index.md#7872-xxx_stopprotocol) | 该函数向应用通知协议已停止。 |
| [**Xxx_WriteData**](../diagnostics/diagnostic_communication_manager/index.md#7822-xxx_writedata) | 该函数请求应用写入某个 DID 的数据值。 |
| [**Xxx_WriteDidData**](../diagnostics/diagnostic_communication_manager/index.md#7833-xxx_writediddata) | 该函数请求应用写入某个 DID 的数据值。 |

## AUTOSAR Diagnostic Event Manager（诊断事件管理器）（182）

来源：[AUTOSAR Diagnostic Event Manager（诊断事件管理器）](../diagnostics/diagnostic_event_manager/index.md) · SWS_DiagnosticEventManager

| 函数 | 简述 |
|---|---|
| [**CallbackClearEventAllowed**](../diagnostics/diagnostic_event_manager/index.md#7631-callbackcleareventallowed) | — |
| [**CallbackComponentStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#7632-callbackcomponentstatuschanged) | — |
| [**CallbackDTCStatusChange**](../diagnostics/diagnostic_event_manager/index.md#7633-callbackdtcstatuschange) | — |
| [**CallbackEventDataChanged**](../diagnostics/diagnostic_event_manager/index.md#7634-callbackeventdatachanged) | — |
| [**CallbackEventUdsStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#7635-callbackeventudsstatuschanged) | — |
| [**CallbackGetFaultDetectCounter**](../diagnostics/diagnostic_event_manager/index.md#7636-callbackgetfaultdetectcounter) | — |
| [**CallbackInitMonitorForEvent**](../diagnostics/diagnostic_event_manager/index.md#7637-callbackinitmonitorforevent) | — |
| [**CallbackMonitorStatusChange**](../diagnostics/diagnostic_event_manager/index.md#7638-callbackmonitorstatuschange) | — |
| [**CBClrEvt**](../diagnostics/diagnostic_event_manager/index.md#7641-cbclrevt) | — |
| [**CBDataEvt**](../diagnostics/diagnostic_event_manager/index.md#7642-cbdataevt) | — |
| [**CBEventUdsStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#7646-cbeventudsstatuschanged) | — |
| [**CBFaultDetectCtr**](../diagnostics/diagnostic_event_manager/index.md#7643-cbfaultdetectctr) | — |
| [**CBInitEvt**](../diagnostics/diagnostic_event_manager/index.md#7644-cbinitevt) | — |
| [**CBMonitorStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#7647-cbmonitorstatuschanged) | — |
| [**CBStatusComp**](../diagnostics/diagnostic_event_manager/index.md#7648-cbstatuscomp) | — |
| [**CBStatusDTC**](../diagnostics/diagnostic_event_manager/index.md#7645-cbstatusdtc) | — |
| [**ClearDTC**](../diagnostics/diagnostic_event_manager/index.md#76310-cleardtc) | — |
| [**ClearDtcNotification**](../diagnostics/diagnostic_event_manager/index.md#7432-cleardtcnotification) | — |
| [**ClearEventAllowed**](../diagnostics/diagnostic_event_manager/index.md#7439-cleareventallowed) | — |
| [**ControlDTCSuppression**](../diagnostics/diagnostic_event_manager/index.md#76411-controldtcsuppression) | — |
| [**ControlEventFailureCycleCounterThreshold**](../diagnostics/diagnostic_event_manager/index.md#76413-controleventfailurecyclecounterthreshold) | — |
| [**Dem_ClearDTC**](../diagnostics/diagnostic_event_manager/index.md#7331-dem_cleardtc) | 清除单个 DTC 以及 DTC 组。 |
| [**Dem_ClearPrestoredFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#7332-dem_clearprestoredfreezeframe) | 清除特定事件的预存储冻结帧。 |
| [**Dem_DcmGetAvailableOBDMIDs**](../diagnostics/diagnostic_event_manager/index.md#73514-dem_dcmgetavailableobdmids) | 在 Service $06 请求时向 Dcm 报告所请求"可用性 OBDMID"的值。 |
| [**Dem_DcmGetDTCOfOBDFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#73513-dem_dcmgetdtcofobdfreezeframe) | 按冻结帧记录号获取 DTC。 |
| [**Dem_DcmGetDTRData**](../diagnostics/diagnostic_event_manager/index.md#73516-dem_dcmgetdtrdata) | 报告 DTR 数据及其 TID 值、UaSID、带下限和上限的测试结果。 |
| [**Dem_DcmGetInfoTypeValue08**](../diagnostics/diagnostic_event_manager/index.md#7351-dem_dcmgetinfotypevalue08) | 用于按照 InfoType $08 请求 IUMPR 数据的服务。 |
| [**Dem_DcmGetInfoTypeValue0B**](../diagnostics/diagnostic_event_manager/index.md#7352-dem_dcmgetinfotypevalue0b) | 用于按照 InfoType $0B 请求 IUMPR 数据的服务。 |
| [**Dem_DcmGetInfoTypeValue79**](../diagnostics/diagnostic_event_manager/index.md#73517-dem_dcmgetinfotypevalue79) | 报告 Dem 计算的监视器活动分母 PID 值的服务。 |
| [**Dem_DcmGetNumTIDsOfOBDMID**](../diagnostics/diagnostic_event_manager/index.md#73515-dem_dcmgetnumtidsofobdmid) | 获取每个（功能性）OBDMID 的 TID 数量。 |
| [**Dem_DcmReadDataOfOBDFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#73512-dem_dcmreaddataofobdfreezeframe) | 按 PID 和索引获取为服务 $02 的输出而选择的最重要的冻结帧的数据元素。 |
| [**Dem_DcmReadDataOfPID01**](../diagnostics/diagnostic_event_manager/index.md#7353-dem_dcmreaddataofpid01) | 报告 Dem 计算的 PID $01 值的服务。 |
| [**Dem_DcmReadDataOfPID1C**](../diagnostics/diagnostic_event_manager/index.md#7354-dem_dcmreaddataofpid1c) | 报告 Dem 计算的 PID $1C 值的服务。 |
| [**Dem_DcmReadDataOfPID21**](../diagnostics/diagnostic_event_manager/index.md#7355-dem_dcmreaddataofpid21) | 报告 Dem 计算的 PID $21 值的服务。 |
| [**Dem_DcmReadDataOfPID30**](../diagnostics/diagnostic_event_manager/index.md#7356-dem_dcmreaddataofpid30) | 报告 Dem 计算的 PID $30 值的服务。 |
| [**Dem_DcmReadDataOfPID31**](../diagnostics/diagnostic_event_manager/index.md#7357-dem_dcmreaddataofpid31) | 报告 Dem 计算的 PID $31 值的服务。 |
| [**Dem_DcmReadDataOfPID41**](../diagnostics/diagnostic_event_manager/index.md#7358-dem_dcmreaddataofpid41) | 报告 Dem 计算的 PID $41 值的服务。 |
| [**Dem_DcmReadDataOfPID4D**](../diagnostics/diagnostic_event_manager/index.md#7359-dem_dcmreaddataofpid4d) | 报告 Dem 计算的 PID $4D 值的服务。 |
| [**Dem_DcmReadDataOfPID4E**](../diagnostics/diagnostic_event_manager/index.md#73510-dem_dcmreaddataofpid4e) | 报告 Dem 计算的 PID $4E 值的服务。 |
| [**Dem_DcmReadDataOfPID91**](../diagnostics/diagnostic_event_manager/index.md#73511-dem_dcmreaddataofpid91) | 报告 Dem 计算的 PID $91 值的服务。 |
| [**Dem_DcmReadDataOfPIDF501**](../diagnostics/diagnostic_event_manager/index.md#73518-dem_dcmreaddataofpidf501) | 报告 Dem 计算的 PID 0xF501 值的函数。 |
| [**Dem_DisableDTCRecordUpdate**](../diagnostics/diagnostic_event_manager/index.md#73421-dem_disabledtcrecordupdate) | 禁用特定 DTC（一次仅一个）的事件内存更新。 |
| [**Dem_DisableDTCSetting**](../diagnostics/diagnostic_event_manager/index.md#73431-dem_disabledtcsetting) | 为分配给所寻址客户端的 DemEventMemorySet 的所有 DTC 禁用 DTC 设置。 |
| [**Dem_EnableDTCRecordUpdate**](../diagnostics/diagnostic_event_manager/index.md#73422-dem_enabledtcrecordupdate) | 启用之前由 Dem_DisableDTCRecordUpdate() 禁用的 DTC 的事件内存更新。 |
| [**Dem_EnableDTCSetting**](../diagnostics/diagnostic_event_manager/index.md#73432-dem_enabledtcsetting) | （重新）启用分配给所寻址客户端的 DemEventMemorySet 的所有 DTC 的 DTC 设置。 |
| [**Dem_GetB1Counter**](../diagnostics/diagnostic_event_manager/index.md#73716-dem_getb1counter) | 报告 Dem 计算的 B1 计数器值的服务。 |
| [**Dem_GetComponentFailed**](../diagnostics/diagnostic_event_manager/index.md#7333-dem_getcomponentfailed) | 获取 DemComponent 的失败状态。 |
| [**Dem_GetCycleQualified**](../diagnostics/diagnostic_event_manager/index.md#73713-dem_getcyclequalified) | 返回从属运行周期的鉴定状态。 |
| [**Dem_GetDataOfPID21**](../diagnostics/diagnostic_event_manager/index.md#7378-dem_getdataofpid21) | 软件组件从 Dem 获取 PID $21 值的服务。 |
| [**Dem_GetDebouncingOfEvent**](../diagnostics/diagnostic_event_manager/index.md#7338-dem_getdebouncingofevent) | 获取事件的去抖动状态。 |
| [**Dem_GetDTCByOccurrenceTime**](../diagnostics/diagnostic_event_manager/index.md#734113-dem_getdtcbyoccurrencetime) | 按发生时间获取 DTC。 |
| [**Dem_GetDTCOfEvent**](../diagnostics/diagnostic_event_manager/index.md#7339-dem_getdtcofevent) | 获取事件的 DTC。 |
| [**Dem_GetDTCSelectionResult**](../diagnostics/diagnostic_event_manager/index.md#7334-dem_getdtcselectionresult) | 提供上次 Dem_SelectDTC 调用是否选择了有效 DTC 或 DTC 组的信息。 |
| [**Dem_GetDTCSelectionResultForClearDTC**](../diagnostics/diagnostic_event_manager/index.md#7335-dem_getdtcselectionresultforcleardtc) | 在考虑 Dem 是否仅允许清除所有 DTC 的设置的前提下，提供上次 Dem_SelectDTC 调用是否选择了有效 DTC 或 DTC 组的信息。 |
| [**Dem_GetDTCSeverityAvailabilityMask**](../diagnostics/diagnostic_event_manager/index.md#73715-dem_getdtcseverityavailabilitymask) | 获取 DTC 严重度可用性掩码。 |
| [**Dem_GetDTCStatusAvailabilityMask**](../diagnostics/diagnostic_event_manager/index.md#73412-dem_getdtcstatusavailabilitymask) | 获取所选故障内存的 DTC 状态可用性掩码。 |
| [**Dem_GetDTCSuppression**](../diagnostics/diagnostic_event_manager/index.md#73310-dem_getdtcsuppression) | 返回特定 DTC 的抑制状态。 |
| [**Dem_GetEventAvailable**](../diagnostics/diagnostic_event_manager/index.md#73311-dem_geteventavailable) | 获取事件的可用性。 |
| [**Dem_GetEventExtendedDataRecordEx**](../diagnostics/diagnostic_event_manager/index.md#73315-dem_geteventextendeddatarecordex) | 按事件获取扩展数据记录的数据。 |
| [**Dem_GetEventFreezeFrameDataEx**](../diagnostics/diagnostic_event_manager/index.md#73314-dem_geteventfreezeframedataex) | 按事件获取冻结帧的数据。 |
| [**Dem_GetEventMemoryOverflow**](../diagnostics/diagnostic_event_manager/index.md#73316-dem_geteventmemoryoverflow) | 获取事件内存溢出指示状态。 |
| [**Dem_GetEventUdsStatus**](../diagnostics/diagnostic_event_manager/index.md#7336-dem_geteventudsstatus) | 获取分配给事件 DTC 的当前 UDS 状态字节。 |
| [**Dem_GetFaultDetectionCounter**](../diagnostics/diagnostic_event_manager/index.md#73312-dem_getfaultdetectioncounter) | 获取事件的故障检测计数器。 |
| [**Dem_GetFunctionalUnitOfDTC**](../diagnostics/diagnostic_event_manager/index.md#73415-dem_getfunctionalunitofdtc) | 获取所请求 DTC 的功能单元。 |
| [**Dem_GetIndicatorStatus**](../diagnostics/diagnostic_event_manager/index.md#73313-dem_getindicatorstatus) | 获取从 UDS 状态推导的指示器状态。 |
| [**Dem_GetIUMPRDenCondition**](../diagnostics/diagnostic_event_manager/index.md#7374-dem_getiumprdencondition) | 为了在 OBD 相关 ECU 之间传递（附加）分母条件的状态，此 API 用于从计算这些条件的 ECU 的 Dem 中检索条件状态。 |
| [**Dem_GetMonitorStatus**](../diagnostics/diagnostic_event_manager/index.md#7337-dem_getmonitorstatus) | 获取事件的当前监视器状态。 |
| [**Dem_GetNextExtendedDataRecord**](../diagnostics/diagnostic_event_manager/index.md#73425-dem_getnextextendeddatarecord) | 为 Dem_SelectExtendedDataRecord 所选 DTC 获取扩展数据记录。 |
| [**Dem_GetNextFilteredDTC**](../diagnostics/diagnostic_event_manager/index.md#73418-dem_getnextfiltereddtc) | 获取下一个匹配过滤判据的 DTC。 |
| [**Dem_GetNextFilteredDTCAndFDC**](../diagnostics/diagnostic_event_manager/index.md#73419-dem_getnextfiltereddtcandfdc) | 获取下一个匹配过滤判据的 DTC 及其关联的故障检测计数器（FDC）。 |
| [**Dem_GetNextFilteredDTCAndSeverity**](../diagnostics/diagnostic_event_manager/index.md#734110-dem_getnextfiltereddtcandseverity) | 获取下一个匹配过滤判据的 DTC 及其关联的严重度。 |
| [**Dem_GetNextFilteredRecord**](../diagnostics/diagnostic_event_manager/index.md#734112-dem_getnextfilteredrecord) | 获取事件内存中存储的下一个冻结帧记录号及其关联的 DTC。 |
| [**Dem_GetNextFreezeFrameData**](../diagnostics/diagnostic_event_manager/index.md#73426-dem_getnextfreezeframedata) | 为 Dem_SelectFreezeFrameData 所选 DTC 获取冻结帧数据。 |
| [**Dem_GetNumberOfEventMemoryEntries**](../diagnostics/diagnostic_event_manager/index.md#73317-dem_getnumberofeventmemoryentries) | 返回当前存储在所请求事件内存中的条目数量。 |
| [**Dem_GetNumberOfFilteredDTC**](../diagnostics/diagnostic_event_manager/index.md#73417-dem_getnumberoffiltereddtc) | 获取过滤后的 DTC 数量。 |
| [**Dem_GetNumberOfFreezeFrameRecords**](../diagnostics/diagnostic_event_manager/index.md#73429-dem_getnumberoffreezeframerecords) | 此函数返回当前存储在主事件内存中的所有冻结帧记录的数量。 |
| [**Dem_GetSeverityOfDTC**](../diagnostics/diagnostic_event_manager/index.md#73414-dem_getseverityofdtc) | 获取所请求 DTC 的严重度。 |
| [**Dem_GetSizeOfExtendedDataRecordSelection**](../diagnostics/diagnostic_event_manager/index.md#73423-dem_getsizeofextendeddatarecordselection) | 获取通过调用 Dem_SelectExtendedDataRecord 所选 DTC 的扩展数据记录的大小。 |
| [**Dem_GetSizeOfFreezeFrameSelection**](../diagnostics/diagnostic_event_manager/index.md#73424-dem_getsizeoffreezeframeselection) | 获取通过调用 Dem_SelectFreezeFrameData 所选 DTC 的冻结帧数据的大小。 |
| [**Dem_GetStatusOfDTC**](../diagnostics/diagnostic_event_manager/index.md#73413-dem_getstatusofdtc) | 获取 DTC 的状态。 |
| [**Dem_GetTranslationType**](../diagnostics/diagnostic_event_manager/index.md#73411-dem_gettranslationtype) | 获取 ECU 支持的 DTC 格式。 |
| [**Dem_GetVersionInfo**](../diagnostics/diagnostic_event_manager/index.md#731-dem_getversioninfo) | 返回此模块的版本信息。 |
| [**Dem_Init**](../diagnostics/diagnostic_event_manager/index.md#7322-dem_init) | 初始化或重新初始化本模块。 |
| [**Dem_J1939DcmClearDTC**](../diagnostics/diagnostic_event_manager/index.md#73621-dem_j1939dcmcleardtc) | 清除与指定 DTC 相关的所有事件的状态，以及这些事件的所有关联事件内存条目。 |
| [**Dem_J1939DcmFirstDTCwithLampStatus**](../diagnostics/diagnostic_event_manager/index.md#73614-dem_j1939dcmfirstdtcwithlampstatus) | 该函数为特定节点设置 DM31 响应的第一个适用 DTC 的过滤器。 |
| [**Dem_J1939DcmGetNextDTCwithLampStatus**](../diagnostics/diagnostic_event_manager/index.md#73615-dem_j1939dcmgetnextdtcwithlampstatus) | 获取 DM31 的下一个过滤 J1939 DTC，包括当前的 LampStatus。 |
| [**Dem_J1939DcmGetNextFilteredDTC**](../diagnostics/diagnostic_event_manager/index.md#73613-dem_j1939dcmgetnextfiltereddtc) | 获取下一个过滤后的 J1939 DTC。 |
| [**Dem_J1939DcmGetNextFilteredRatio**](../diagnostics/diagnostic_event_manager/index.md#73632-dem_j1939dcmgetnextfilteredratio) | 获取下一个过滤后的比率。 |
| [**Dem_J1939DcmGetNextFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#73623-dem_j1939dcmgetnextfreezeframe) | 获取下一个冻结帧数据。 |
| [**Dem_J1939DcmGetNextSPNInFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#73624-dem_j1939dcmgetnextspninfreezeframe) | 获取下一个 SPN。 |
| [**Dem_J1939DcmGetNumberOfFilteredDTC**](../diagnostics/diagnostic_event_manager/index.md#73612-dem_j1939dcmgetnumberoffiltereddtc) | 获取由 Dem_J1939DcmSetDTCFilter 函数设置的当前过滤 DTC 的数量。 |
| [**Dem_J1939DcmReadDiagnosticReadiness1**](../diagnostics/diagnostic_event_manager/index.md#73633-dem_j1939dcmreaddiagnosticreadiness1) | 报告 Dem 计算的 Diagnostic Readiness 1（DM05）值的服务。 |
| [**Dem_J1939DcmReadDiagnosticReadiness2**](../diagnostics/diagnostic_event_manager/index.md#73634-dem_j1939dcmreaddiagnosticreadiness2) | 报告 Dem 计算的 Diagnostic Readiness 2（DM21）值的服务。 |
| [**Dem_J1939DcmReadDiagnosticReadiness3**](../diagnostics/diagnostic_event_manager/index.md#73635-dem_j1939dcmreaddiagnosticreadiness3) | 报告 Dem 计算的 Diagnostic Readiness 3（DM26）值的服务。 |
| [**Dem_J1939DcmSetDTCFilter**](../diagnostics/diagnostic_event_manager/index.md#73611-dem_j1939dcmsetdtcfilter) | 该函数为特定节点设置 DTC 过滤器，并返回过滤后 DTC 的组合灯状态。 |
| [**Dem_J1939DcmSetFreezeFrameFilter**](../diagnostics/diagnostic_event_manager/index.md#73622-dem_j1939dcmsetfreezeframefilter) | 该函数为特定节点设置 FreezeFrame 过滤器。 |
| [**Dem_J1939DcmSetRatioFilter**](../diagnostics/diagnostic_event_manager/index.md#73631-dem_j1939dcmsetratiofilter) | 该函数为特定节点设置 Ratio 过滤器，并返回相应的点火循环计数器和通用分母。 |
| [**Dem_MainFunction**](../diagnostics/diagnostic_event_manager/index.md#751-dem_mainfunction) | — |
| [**Dem_PreInit**](../diagnostics/diagnostic_event_manager/index.md#7321-dem_preinit) | 初始化处理 BSW 模块所报告事件所需的内部状态。 |
| [**Dem_PrestoreFreezeFrame**](../diagnostics/diagnostic_event_manager/index.md#73322-dem_prestorefreezeframe) | 为特定事件捕获冻结帧数据。 |
| [**Dem_ReadDataOfPID01**](../diagnostics/diagnostic_event_manager/index.md#7377-dem_readdataofpid01) | 报告 Dem 计算的 PID $01 值的服务。 |
| [**Dem_RepIUMPRDenRelease**](../diagnostics/diagnostic_event_manager/index.md#7375-dem_repiumprdenrelease) | 用于释放特定监视器分母的服务。 |
| [**Dem_RepIUMPRFaultDetect**](../diagnostics/diagnostic_event_manager/index.md#7372-dem_repiumprfaultdetect) | 报告可能发现故障（因为所有条件均已满足）的服务。 |
| [**Dem_ResetEventDebounceStatus**](../diagnostics/diagnostic_event_manager/index.md#73318-dem_reseteventdebouncestatus) | 由 BSW 模块和 SW-C 控制内部去抖动计数器/计时器。 |
| [**Dem_ResetEventStatus**](../diagnostics/diagnostic_event_manager/index.md#73319-dem_reseteventstatus) | 复位事件的失败状态。 |
| [**Dem_ResetMonitorStatus**](../diagnostics/diagnostic_event_manager/index.md#73320-dem_resetmonitorstatus) | 复位监视器的失败状态。 |
| [**Dem_RestartOperationCycle**](../diagnostics/diagnostic_event_manager/index.md#73321-dem_restartoperationcycle) | 设置一个运行周期状态。 |
| [**Dem_SelectDTC**](../diagnostics/diagnostic_event_manager/index.md#73323-dem_selectdtc) | 选择一个 DTC 或 DTC 组作为进一步操作的目标。 |
| [**Dem_SelectExtendedDataRecord**](../diagnostics/diagnostic_event_manager/index.md#73427-dem_selectextendeddatarecord) | 设置由 Dem_GetNextExtendedDataRecord 和 Dem_GetSizeOfExtendedDataRecordSelection 使用的过滤器。 |
| [**Dem_SelectFreezeFrameData**](../diagnostics/diagnostic_event_manager/index.md#73428-dem_selectfreezeframedata) | 设置由 Dem_GetNextFreezeFrameData 和 Dem_GetSizeOfFreezeFrameSelection 使用的过滤器。 |
| [**Dem_SetComponentAvailable**](../diagnostics/diagnostic_event_manager/index.md#73324-dem_setcomponentavailable) | 设置特定 DemComponent 的可用性。 |
| [**Dem_SetCycleQualified**](../diagnostics/diagnostic_event_manager/index.md#73714-dem_setcyclequalified) | 将一个从属运行周期设置为已鉴定，使其可以与其主控周期一起处理。 |
| [**Dem_SetDataOfPID21**](../diagnostics/diagnostic_event_manager/index.md#7379-dem_setdataofpid21) | 软件组件在 Dem 中设置 PID $21 值的服务。 |
| [**Dem_SetDataOfPID31**](../diagnostics/diagnostic_event_manager/index.md#73710-dem_setdataofpid31) | 软件组件在 Dem 中设置 PID $31 值的服务。 |
| [**Dem_SetDataOfPID4D**](../diagnostics/diagnostic_event_manager/index.md#73711-dem_setdataofpid4d) | 软件组件在 Dem 中设置 PID $4D 值的服务。 |
| [**Dem_SetDataOfPID4E**](../diagnostics/diagnostic_event_manager/index.md#73712-dem_setdataofpid4e) | 软件组件在 Dem 中设置 PID $4E 值的服务。 |
| [**Dem_SetDTCFilter**](../diagnostics/diagnostic_event_manager/index.md#73416-dem_setdtcfilter) | 设置 DTC 过滤器。 |
| [**Dem_SetDTCFilterByExtendedDataRecordNumber**](../diagnostics/diagnostic_event_manager/index.md#734114-dem_setdtcfilterbyextendeddatarecordnumber) | 基于给定的扩展数据记录在主故障内存上设置 DTC 过滤器。 |
| [**Dem_SetDTCFilterByReadinessGroup**](../diagnostics/diagnostic_event_manager/index.md#734115-dem_setdtcfilterbyreadinessgroup) | 基于给定的 DTC 就绪组在主故障内存上设置 DTC 过滤器。 |
| [**Dem_SetDTCSuppression**](../diagnostics/diagnostic_event_manager/index.md#73325-dem_setdtcsuppression) | 设置特定 DTC 的抑制状态。 |
| [**Dem_SetDTR**](../diagnostics/diagnostic_event_manager/index.md#73717-dem_setdtr) | 报告带下限和上限的 DTR 结果。 |
| [**Dem_SetEnableCondition**](../diagnostics/diagnostic_event_manager/index.md#73326-dem_setenablecondition) | 设置一个使能条件。 |
| [**Dem_SetEventAvailable**](../diagnostics/diagnostic_event_manager/index.md#73327-dem_seteventavailable) | 设置特定事件的可用状态。 |
| [**Dem_SetEventConfirmationThresholdCounter**](../diagnostics/diagnostic_event_manager/index.md#73328-dem_seteventconfirmationthresholdcounter) | 设置事件的故障确认阈值。 |
| [**Dem_SetEventDisabled**](../diagnostics/diagnostic_event_manager/index.md#7371-dem_seteventdisabled) | 将事件报告为已禁用（针对 PID $41 计算）的服务。 |
| [**Dem_SetEventStatus**](../diagnostics/diagnostic_event_manager/index.md#73329-dem_seteventstatus) | 由 SW-C 或 BSW 模块调用，向 Dem 报告监视器状态信息。 |
| [**Dem_SetEventStatusWithMonitorData**](../diagnostics/diagnostic_event_manager/index.md#73330-dem_seteventstatuswithmonitordata) | 此 API 仅在 ({Dem/DemConfigSet/DemEventParameter/DemEventReportingType} == STANDARD_REPORTING_WITH_MONITOR_DATA) 时可用。 |
| [**Dem_SetFreezeFrameRecordFilter**](../diagnostics/diagnostic_event_manager/index.md#734111-dem_setfreezeframerecordfilter) | 设置冻结帧记录过滤器。 |
| [**Dem_SetIUMPRDenCondition**](../diagnostics/diagnostic_event_manager/index.md#7373-dem_setiumprdencondition) | 为了在 OBD 相关 ECU 之间传递（附加）分母条件的状态，此 API 用于将条件状态转发给特定 ECU 的 Dem。 |
| [**Dem_SetPtoStatus**](../diagnostics/diagnostic_event_manager/index.md#7376-dem_setptostatus) | 设置 PTO 状态的 API。 |
| [**Dem_SetStorageCondition**](../diagnostics/diagnostic_event_manager/index.md#73331-dem_setstoragecondition) | 设置一个存储条件。 |
| [**Dem_SetWIRStatus**](../diagnostics/diagnostic_event_manager/index.md#73332-dem_setwirstatus) | 通过失效安全 SW-C 设置 WIR 状态位。 |
| [**Dem_Shutdown**](../diagnostics/diagnostic_event_manager/index.md#7323-dem_shutdown) | 关闭本模块。 |
| [**DemGeneralTriggerOnEventUdsStatus**](../diagnostics/diagnostic_event_manager/index.md#7434-demgeneraltriggeroneventudsstatus) | — |
| [**DemGeneralTriggerOnMonitorStatus**](../diagnostics/diagnostic_event_manager/index.md#7433-demgeneraltriggeronmonitorstatus) | — |
| [**DemTriggerOnComponentStatus**](../diagnostics/diagnostic_event_manager/index.md#74312-demtriggeroncomponentstatus) | — |
| [**DemTriggerOnDTCStatus**](../diagnostics/diagnostic_event_manager/index.md#7436-demtriggerondtcstatus) | — |
| [**DemTriggerOnEventUdsStatus**](../diagnostics/diagnostic_event_manager/index.md#7435-demtriggeroneventudsstatus) | — |
| [**DemTriggerOnMonitorStatus**](../diagnostics/diagnostic_event_manager/index.md#7437-demtriggeronmonitorstatus) | — |
| [**DiagnosticInfo**](../diagnostics/diagnostic_event_manager/index.md#76314-diagnosticinfo) | — |
| [**DiagnosticMonitor**](../diagnostics/diagnostic_event_manager/index.md#76315-diagnosticmonitor) | — |
| [**DiagnosticMonitor_MonitorData**](../diagnostics/diagnostic_event_manager/index.md#76316-diagnosticmonitor_monitordata) | — |
| [**DTCSuppression**](../diagnostics/diagnostic_event_manager/index.md#76311-dtcsuppression) | — |
| [**DTR**](../diagnostics/diagnostic_event_manager/index.md#76415-dtr) | — |
| [**DTRCentralReport**](../diagnostics/diagnostic_event_manager/index.md#76313-dtrcentralreport) | — |
| [**EnableCond**](../diagnostics/diagnostic_event_manager/index.md#76416-enablecond) | — |
| [**EnableCondition**](../diagnostics/diagnostic_event_manager/index.md#76317-enablecondition) | — |
| [**EventAvailable**](../diagnostics/diagnostic_event_manager/index.md#76318-eventavailable) | — |
| [**EventDataChanged**](../diagnostics/diagnostic_event_manager/index.md#7438-eventdatachanged) | — |
| [**EventFailureCycleCounterThreshold**](../diagnostics/diagnostic_event_manager/index.md#76319-eventfailurecyclecounterthreshold) | — |
| [**EventInfo**](../diagnostics/diagnostic_event_manager/index.md#76420-eventinfo) | — |
| [**EventStatus**](../diagnostics/diagnostic_event_manager/index.md#76321-eventstatus) | — |
| [**EvMemOverflowIndication**](../diagnostics/diagnostic_event_manager/index.md#76320-evmemoverflowindication) | — |
| [**GeneralCallbackEventDataChanged**](../diagnostics/diagnostic_event_manager/index.md#76322-generalcallbackeventdatachanged) | — |
| [**GeneralCallbackEventUdsStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#76323-generalcallbackeventudsstatuschanged) | — |
| [**GeneralCallbackMonitorStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#76324-generalcallbackmonitorstatuschanged) | — |
| [**GeneralCBDataEvt**](../diagnostics/diagnostic_event_manager/index.md#76421-generalcbdataevt) | — |
| [**GeneralCBMonitorStatusChanged**](../diagnostics/diagnostic_event_manager/index.md#76422-generalcbmonitorstatuschanged) | — |
| [**GeneralCBStatusEvt**](../diagnostics/diagnostic_event_manager/index.md#76423-generalcbstatusevt) | — |
| [**GeneralDiagnosticInfo**](../diagnostics/diagnostic_event_manager/index.md#76325-generaldiagnosticinfo) | — |
| [**GeneralEvtInfo**](../diagnostics/diagnostic_event_manager/index.md#76424-generalevtinfo) | — |
| [**GetDataOfPID21**](../diagnostics/diagnostic_event_manager/index.md#76326-getdataofpid21) | — |
| [**GetFaultDetectionCounter**](../diagnostics/diagnostic_event_manager/index.md#74311-getfaultdetectioncounter) | — |
| [**IndicatorStatus**](../diagnostics/diagnostic_event_manager/index.md#76327-indicatorstatus) | — |
| [**IndStatus**](../diagnostics/diagnostic_event_manager/index.md#76425-indstatus) | — |
| [**InitMonitorForEvent**](../diagnostics/diagnostic_event_manager/index.md#74311-initmonitorforevent) | — |
| [**IUMPRDenominator**](../diagnostics/diagnostic_event_manager/index.md#76328-iumprdenominator) | — |
| [**IUMPRDenominatorCondition**](../diagnostics/diagnostic_event_manager/index.md#76329-iumprdenominatorcondition) | — |
| [**IUMPRNumerator**](../diagnostics/diagnostic_event_manager/index.md#76330-iumprnumerator) | — |
| [**OpCycle**](../diagnostics/diagnostic_event_manager/index.md#76429-opcycle) | — |
| [**OperationCycle**](../diagnostics/diagnostic_event_manager/index.md#76331-operationcycle) | — |
| [**OverflowIndPrimaryMemory**](../diagnostics/diagnostic_event_manager/index.md#76430-overflowindprimarymemory) | — |
| [**OverflowIndUserDefinedMemory**](../diagnostics/diagnostic_event_manager/index.md#76431-overflowinduserdefinedmemory) | — |
| [**PowerTakeOff**](../diagnostics/diagnostic_event_manager/index.md#76332-powertakeoff) | — |
| [**PowerTakeOffStatus**](../diagnostics/diagnostic_event_manager/index.md#76432-powertakeoffstatus) | — |
| [**ReadDataElement**](../diagnostics/diagnostic_event_manager/index.md#74310-readdataelement) | — |
| [**SetDataOfPID21**](../diagnostics/diagnostic_event_manager/index.md#76333-setdataofpid21) | — |
| [**SetDataOfPID31**](../diagnostics/diagnostic_event_manager/index.md#76334-setdataofpid31) | — |
| [**SetDataOfPID4D**](../diagnostics/diagnostic_event_manager/index.md#76335-setdataofpid4d) | — |
| [**SetDataOfPID4E**](../diagnostics/diagnostic_event_manager/index.md#76336-setdataofpid4e) | — |
| [**StorageCond**](../diagnostics/diagnostic_event_manager/index.md#76438-storagecond) | — |
| [**StorageCondition**](../diagnostics/diagnostic_event_manager/index.md#76337-storagecondition) | — |

## AUTOSAR DIO Driver（数字输入输出驱动）（9）

来源：[AUTOSAR DIO Driver（数字输入输出驱动）](../io/dio_driver/index.md) · SWS_DIODriver

| 函数 | 简述 |
|---|---|
| [**Dio_FlipChannel**](../io/dio_driver/index.md#738-dio_flipchannel) | 翻转（从 1 到 0 或从 0 到 1）通道电平并返回翻转后通道电平的服务。 |
| [**Dio_GetVersionInfo**](../io/dio_driver/index.md#737-dio_getversioninfo) | 获取本模块版本信息的服务。 |
| [**Dio_MaskedWritePort**](../io/dio_driver/index.md#739-dio_maskedwriteport) | 以所需掩码设置给定端口值的服务。 |
| [**Dio_ReadChannel**](../io/dio_driver/index.md#731-dio_readchannel) | 返回指定DIO通道的值。 |
| [**Dio_ReadChannelGroup**](../io/dio_driver/index.md#735-dio_readchannelgroup) | 此服务读取端口相邻位的子集。 |
| [**Dio_ReadPort**](../io/dio_driver/index.md#733-dio_readport) | 返回该端口所有通道的电平。 |
| [**Dio_WriteChannel**](../io/dio_driver/index.md#732-dio_writechannel) | 设置通道电平的服务。 |
| [**Dio_WriteChannelGroup**](../io/dio_driver/index.md#736-dio_writechannelgroup) | 将端口相邻位的子集设置为指定电平的服务。 |
| [**Dio_WritePort**](../io/dio_driver/index.md#734-dio_writeport) | 设置端口值的服务。 |

## AUTOSAR Dlt（诊断日志与跟踪）（38）

来源：[AUTOSAR Dlt（诊断日志与跟踪）](../communication/diagnostic_log_and_trace/index.md) · SWS_DiagnosticLogAndTrace

| 函数 | 简述 |
|---|---|
| [**Dlt_ControlService**](../communication/diagnostic_log_and_trace/index.md#7731-dlt_controlservice) | — |
| [**Dlt_CopyRxData**](../communication/diagnostic_log_and_trace/index.md#748-dlt_copyrxdata) | 调用此函数以将 I-PDU 段（N-PDU）的接收数据提供给上层。 |
| [**Dlt_CopyTxData**](../communication/diagnostic_log_and_trace/index.md#745-dlt_copytxdata) | 调用此函数以获取 I-PDU 段（N-PDU）的发送数据。 |
| [**Dlt_DetForwardErrorTrace**](../communication/diagnostic_log_and_trace/index.md#737-dlt_detforwarderrortrace) | 用于将错误报告从 Det 转发到 Dlt 的服务。 |
| [**Dlt_GetDefaultLogLevel**](../communication/diagnostic_log_and_trace/index.md#7311-dlt_getdefaultloglevel) | 返回 Dlt 模块当前使用的默认日志级别。 |
| [**Dlt_GetDefaultTraceStatus**](../communication/diagnostic_log_and_trace/index.md#7317-dlt_getdefaulttracestatus) | 返回所寻址日志通道当前的跟踪状态。 |
| [**Dlt_GetLogChannelNames**](../communication/diagnostic_log_and_trace/index.md#7318-dlt_getlogchannelnames) | 调用者提供要返回的 logChannelNames 的数量。 |
| [**Dlt_GetLogChannelThreshold**](../communication/diagnostic_log_and_trace/index.md#7322-dlt_getlogchannelthreshold) | 返回给定日志通道的过滤阈值。 |
| [**Dlt_GetLogInfo**](../communication/diagnostic_log_and_trace/index.md#7310-dlt_getloginfo) | 调用此函数以请求关于已注册 ApplicationId、其 ContextId 以及相应日志级别的信息。 |
| [**Dlt_GetTraceStatus**](../communication/diagnostic_log_and_trace/index.md#7319-dlt_gettracestatus) | 返回给定 ApplicationId/ContextId 元组当前的跟踪状态。 |
| [**Dlt_GetVersionInfo**](../communication/diagnostic_log_and_trace/index.md#732-dlt_getversioninfo) | 返回本模块的版本信息。 |
| [**Dlt_Init**](../communication/diagnostic_log_and_trace/index.md#731-dlt_init) | Dlt 使用 NVRamManager，应在 ECU 启动阶段的很晚的时候初始化。 |
| [**Dlt_RegisterContext**](../communication/diagnostic_log_and_trace/index.md#735-dlt_registercontext) | 当一个软件模块希望针对特定上下文使用 DLT 软件组件提供的服务时，必须调用本服务。 |
| [**Dlt_ResetToFactoryDefault**](../communication/diagnostic_log_and_trace/index.md#7313-dlt_resettofactorydefault) | 服务 Dlt_ResetToFactoryDefault 将 LogLevel 和 TraceStatus 复位为持久存储的默认值。 |
| [**Dlt_RxIndication**](../communication/diagnostic_log_and_trace/index.md#741-dlt_rxindication) | 来自下层通信接口模块的已接收 PDU 的指示。 |
| [**Dlt_SendLogMessage**](../communication/diagnostic_log_and_trace/index.md#734-dlt_sendlogmessage) | 本服务表示基础软件模块或软件组件用于发送日志消息的接口。 |
| [**Dlt_SendLogMessageWithAttributes**](../communication/diagnostic_log_and_trace/index.md#7323-dlt_sendlogmessagewithattributes) | 本服务表示基础软件模块或软件组件用于发送带属性的日志消息的接口。 |
| [**Dlt_SendTraceMessage**](../communication/diagnostic_log_and_trace/index.md#733-dlt_sendtracemessage) | 本服务表示基础软件模块或软件组件用于跟踪参数的接口。 |
| [**Dlt_SendTraceMessageWithAttributes**](../communication/diagnostic_log_and_trace/index.md#7324-dlt_sendtracemessagewithattributes) | 本服务表示基础软件模块或软件组件用于带属性跟踪参数的接口。 |
| [**Dlt_SetDefaultLogLevel**](../communication/diagnostic_log_and_trace/index.md#7315-dlt_setdefaultloglevel) | 调用此函数以修改所有未显式设置 ContextId 的日志消息的通过范围。 |
| [**Dlt_SetDefaultTraceStatus**](../communication/diagnostic_log_and_trace/index.md#7316-dlt_setdefaulttracestatus) | 调用此函数以为所有未显式设置的 ContextId 启用或禁用跟踪消息。 |
| [**Dlt_SetLogChannelAssignment**](../communication/diagnostic_log_and_trace/index.md#7320-dlt_setlogchannelassignment) | 将所寻址的 ApplicationId/ContextId 元组添加到所寻址的日志通道，或从中移除。 |
| [**Dlt_SetLogChannelThreshold**](../communication/diagnostic_log_and_trace/index.md#7321-dlt_setlogchannelthreshold) | 为给定的日志通道设置过滤阈值。 |
| [**Dlt_SetLogLevel**](../communication/diagnostic_log_and_trace/index.md#738-dlt_setloglevel) | 本服务用于更改给定 ApplicationID/ContextID 元组的 LogLevel。 |
| [**Dlt_SetMessageFiltering**](../communication/diagnostic_log_and_trace/index.md#7314-dlt_setmessagefiltering) | 开启/关闭 Dlt 模块的消息过滤功能。 |
| [**Dlt_SetTraceStatus**](../communication/diagnostic_log_and_trace/index.md#739-dlt_settracestatus) | 服务 Dlt_SetTraceStatus 为特定的 ApplicationID 和 ContextID 元组设置跟踪状态。 |
| [**Dlt_StartOfReception**](../communication/diagnostic_log_and_trace/index.md#746-dlt_startofreception) | 在开始接收一个 N-SDU 时调用此函数。 |
| [**Dlt_StoreConfiguration**](../communication/diagnostic_log_and_trace/index.md#7312-dlt_storeconfiguration) | 通过调用 NvM_WriteBlock() 将当前 Dlt 配置复制到 NvRAM。 |
| [**Dlt_TpRxIndication**](../communication/diagnostic_log_and_trace/index.md#747-dlt_tprxindication) | 在通过 TP API 接收到一个 I-PDU 之后调用此函数，result 指示接收是否成功。 |
| [**Dlt_TpTxConfirmation**](../communication/diagnostic_log_and_trace/index.md#744-dlt_tptxconfirmation) | 在 I-PDU 已于其网络上发送之后调用此函数，result 指示传输是否成功。 |
| [**Dlt_TriggerTransmit**](../communication/diagnostic_log_and_trace/index.md#742-dlt_triggertransmit) | 在此 API 内，上层模块（被调用模块）应检查可用数据是否适合 PduInfoPtr->SduLength 报告的缓冲区大小。 |
| [**Dlt_TxConfirmation**](../communication/diagnostic_log_and_trace/index.md#743-dlt_txconfirmation) | 下层通信接口模块确认一个 PDU 的传输，或传输失败。 |
| [**Dlt_TxFunction**](../communication/diagnostic_log_and_trace/index.md#751-dlt_txfunction) | -。 |
| [**Dlt_UnregisterContext**](../communication/diagnostic_log_and_trace/index.md#736-dlt_unregistercontext) | 当一个软件模块即将停止时必须调用本服务。 |
| [**DltControlService**](../communication/diagnostic_log_and_trace/index.md#7711-dltcontrolservice) | — |
| [**DltSwcMessageService**](../communication/diagnostic_log_and_trace/index.md#7714-dltswcmessageservice) | — |
| [**InjectionCallback**](../communication/diagnostic_log_and_trace/index.md#7712-injectioncallback) | — |
| [**LogTraceSessionControl**](../communication/diagnostic_log_and_trace/index.md#7713-logtracesessioncontrol) | — |

## AUTOSAR DoIP（基于 IP 的诊断）（19）

来源：[AUTOSAR DoIP（基于 IP 的诊断）](../communication/diagnostic_over_ip/index.md) · SWS_DiagnosticOverIP

| 函数 | 简述 |
|---|---|
| [**DoIP_ActivationLineSwitch**](../communication/diagnostic_over_ip/index.md#738-doip_activationlineswitch) | 此函数供集成者使用，将具有给定 InterfaceId 的 DoIP 接口的激活线状态告知 DoIP 实现。 |
| [**DoIP_GetVersionInfo**](../communication/diagnostic_over_ip/index.md#737-doip_getversioninfo) | 返回本模块的版本信息。 |
| [**DoIP_IfCancelTransmit**](../communication/diagnostic_over_ip/index.md#735-doip_ifcanceltransmit) | 请求取消下层通信模块中一个正在进行的 PDU 传输。 |
| [**DoIP_IfTransmit**](../communication/diagnostic_over_ip/index.md#734-doip_iftransmit) | 请求传输一个 PDU。 |
| [**DoIP_Init**](../communication/diagnostic_over_ip/index.md#736-doip_init) | 此服务初始化 DoIP 模块的所有全局变量。 |
| [**DoIP_LocalIpAddrAssignmentChg**](../communication/diagnostic_over_ip/index.md#749-doip_localipaddrassignmentchg) | 如果与套接字连接相关的 IP 地址分配发生变化（即分配了新地址或已分配的地址变为无效），则 SoAd 调用此函数。 |
| [**DoIP_MainFunction**](../communication/diagnostic_over_ip/index.md#751-doip_mainfunction) | 调度基于 IP 的诊断模块。 |
| [**DoIP_SoAdIfRxIndication**](../communication/diagnostic_over_ip/index.md#746-doip_soadifrxindication) | 来自下层通信接口模块的已接收 PDU 的指示。 |
| [**DoIP_SoAdIfTxConfirmation**](../communication/diagnostic_over_ip/index.md#747-doip_soadiftxconfirmation) | 下层通信接口模块确认一个 PDU 的传输，或传输失败。 |
| [**DoIP_SoAdTpCopyRxData**](../communication/diagnostic_over_ip/index.md#743-doip_soadtpcopyrxdata) | 调用此函数以将 I-PDU 段（N-PDU）的接收数据提供给上层。 |
| [**DoIP_SoAdTpCopyTxData**](../communication/diagnostic_over_ip/index.md#741-doip_soadtpcopytxdata) | 调用此函数以获取 I-PDU 段（N-PDU）的发送数据。 |
| [**DoIP_SoAdTpRxIndication**](../communication/diagnostic_over_ip/index.md#745-doip_soadtprxindication) | 在通过 TP API 接收到一个 I-PDU 之后调用此函数，result 指示接收是否成功。 |
| [**DoIP_SoAdTpStartOfReception**](../communication/diagnostic_over_ip/index.md#744-doip_soadtpstartofreception) | 在开始接收一个 N-SDU 时调用此函数。 |
| [**DoIP_SoAdTpTxConfirmation**](../communication/diagnostic_over_ip/index.md#742-doip_soadtptxconfirmation) | 在 I-PDU 已于其网络上发送之后调用此函数，result 指示传输是否成功。 |
| [**DoIP_SoConModeChg**](../communication/diagnostic_over_ip/index.md#748-doip_soconmodechg) | 关于 SoAd 套接字连接状态变化的通知，例如套接字连接变为在线。 |
| [**DoIP_TpCancelReceive**](../communication/diagnostic_over_ip/index.md#733-doip_tpcancelreceive) | 请求取消下层传输协议模块中一个正在进行的 PDU 接收。 |
| [**DoIP_TpCancelTransmit**](../communication/diagnostic_over_ip/index.md#732-doip_tpcanceltransmit) | 请求取消下层通信模块中一个正在进行的 PDU 传输。 |
| [**DoIP_TpTransmit**](../communication/diagnostic_over_ip/index.md#731-doip_tptransmit) | 请求传输一个 PDU。 |
| [**DoIP_TriggerVehicleAnnouncement**](../communication/diagnostic_over_ip/index.md#739-doip_triggervehicleannouncement) | 此函数用于通知 DoIP 模块为具有给定 InterfaceId 的 DoIP 接口启动车辆通告。 |

## E2E Transformer (E2E转换器)（13）

来源：[E2E Transformer (E2E转换器)](../communication/e2e_transformer/index.md) · SWS_E2ETransformer

| 函数 | 简述 |
|---|---|
| [**E2EXf_DeInit**](../communication/e2e_transformer/index.md#734-e2exf_deinit) | 本服务为同步调用，可重入。 |
| [**E2EXf_GetVersionInfo**](../communication/e2e_transformer/index.md#735-e2exf_getversioninfo) | 此服务为同步调用，可重入。 |
| [**E2EXf_handling_P01_P02**](../communication/e2e_transformer/index.md#6723-e2exf_handling_p01_p02) | — |
| [**E2EXf_Init**](../communication/e2e_transformer/index.md#733-e2exf_init) | 初始化 E2E 转换器的状态。 |
| [**E2EXf_input_checks**](../communication/e2e_transformer/index.md#6722-e2exf_input_checks) | — |
| [**E2EXf_Inv_handle_Statemachine**](../communication/e2e_transformer/index.md#6739-e2exf_inv_handle_statemachine) | — |
| [**E2EXf_Inv_handling_main_check**](../communication/e2e_transformer/index.md#6735-e2exf_inv_handling_main_check) | — |
| [**E2EXf_Inv_handling_P01_P02**](../communication/e2e_transformer/index.md#6733-e2exf_inv_handling_p01_p02) | — |
| [**E2EXf_Inv_handling_P01_P02_forceConstantMaxDeltaCounter**](../communication/e2e_transformer/index.md#6734-e2exf_inv_handling_p01_p02_forceconstantmaxdeltacounter) | — |
| [**E2EXf_Inv_handling_PXXm**](../communication/e2e_transformer/index.md#6736-e2exf_inv_handling_pxxm) | — |
| [**E2EXf_Inv_input_checks**](../communication/e2e_transformer/index.md#6732-e2exf_inv_input_checks) | — |
| [**E2EXf_Inv_set_check_counter**](../communication/e2e_transformer/index.md#6737-e2exf_inv_set_check_counter) | — |
| [**E2EXf_Inv_store_request_counter**](../communication/e2e_transformer/index.md#6738-e2exf_inv_store_request_counter) | — |

## AUTOSAR Ea（EEPROM抽象）（11）

来源：[AUTOSAR Ea（EEPROM抽象）](../memory/ea/index.md) · SWS_EEPROMAbstraction

| 函数 | 简述 |
|---|---|
| [**Ea_Cancel**](../memory/ea/index.md#734-ea_cancel) | 服务 ID 0x04。 |
| [**Ea_EraseImmediateBlock**](../memory/ea/index.md#739-ea_eraseimmediateblock) | 服务 ID 0x09。 |
| [**Ea_GetJobResult**](../memory/ea/index.md#736-ea_getjobresult) | 服务 ID 0x06。 |
| [**Ea_GetStatus**](../memory/ea/index.md#735-ea_getstatus) | 服务 ID 0x05。 |
| [**Ea_GetVersionInfo**](../memory/ea/index.md#738-ea_getversioninfo) | 服务 ID 0x08。 |
| [**Ea_Init**](../memory/ea/index.md#731-ea_init) | 服务 ID 0x00。 |
| [**Ea_InvalidateBlock**](../memory/ea/index.md#737-ea_invalidateblock) | 服务 ID 0x07。 |
| [**Ea_JobEndNotification**](../memory/ea/index.md#741-ea_jobendnotification) | 服务 ID 0x10。 |
| [**Ea_MainFunction**](../memory/ea/index.md#751-ea_mainfunction) | 服务 ID 0x12。 |
| [**Ea_Read**](../memory/ea/index.md#732-ea_read) | 服务 ID 0x02。 |
| [**Ea_Write**](../memory/ea/index.md#733-ea_write) | 服务 ID 0x03。 |

## AUTOSAR ECU State Manager（ECU状态管理器）（52）

来源：[AUTOSAR ECU State Manager（ECU状态管理器）](../mode_management/ecu_state_manager/index.md) · SWS_ECUStateManager

| 函数 | 简述 |
|---|---|
| [**EcuM_AbortWakeupAlarm**](../mode_management/ecu_state_manager/index.md#7363-ecum_abortwakeupalarm) | EcuM_AbortWakeupAlarm中止此用户先前设置的唤醒警报。 |
| [**EcuM_AL_DriverInitOne**](../mode_management/ecu_state_manager/index.md#7524-ecum_al_driverinitone) | 此Callout应在上电复位的情况下提供驱动程序初始化和其他与硬件相关的启动活动。 |
| [**EcuM_AL_DriverInitZero**](../mode_management/ecu_state_manager/index.md#7522-ecum_al_driverinitzero) | 此Callout应提供驱动程序初始化和其他与硬件相关的启动活动，以加载post-build数据。 |
| [**EcuM_AL_DriverRestart**](../mode_management/ecu_state_manager/index.md#7548-ecum_al_driverrestart) | 此Callout应在唤醒情况下，提供驱动程序初始化和其他与硬件相关的启动活动。 |
| [**EcuM_AL_Reset**](../mode_management/ecu_state_manager/index.md#7534-ecum_al_reset) | 此Callout会执行重置ECU的代码。 |
| [**EcuM_AL_SetProgrammableInterrupts**](../mode_management/ecu_state_manager/index.md#7521-ecum_al_setprogrammableinterrupts) | 如果配置参数EcuMSetProgrammableInterrupts设置为true，则执行此Callout函数EcuM_AL_SetProgrammableInterrupts，在具有可编程中断的ECU上设置中断。 |
| [**EcuM_AL_SwitchOff**](../mode_management/ecu_state_manager/index.md#7533-ecum_al_switchoff) | 此Callout会执行关闭ECU电源的代码。 |
| [**EcuM_CheckRamHash**](../mode_management/ecu_state_manager/index.md#7546-ecum_checkramhash) | 此Callout旨在提供RAM完整性测试。 |
| [**EcuM_CheckValidation**](../mode_management/ecu_state_manager/index.md#7552-ecum_checkvalidation) | EcuM调用此Callout以验证唤醒源。 |
| [**EcuM_CheckWakeup**](../mode_management/ecu_state_manager/index.md#7351-ecum_checkwakeup) | 可以调用此函数来检查给定的唤醒源 它将参数传递给集成函数EcuM_CheckWakeupHook。 |
| [**EcuM_CheckWakeupHook**](../mode_management/ecu_state_manager/index.md#7545-ecum_checkwakeuphook) | EcuM调用此Callout来轮询唤醒源。 |
| [**EcuM_ClearWakeupEvent**](../mode_management/ecu_state_manager/index.md#7353-ecum_clearwakeupevent) | 清除唤醒事件。 |
| [**EcuM_DeterminePbConfiguration**](../mode_management/ecu_state_manager/index.md#7523-ecum_determinepbconfiguration) | 此Callout应评估某些条件，如端口引脚（port pin）或NVRAM值，以确定应在启动过程的其余部分使用哪个post-build。 |
| [**EcuM_DisableWakeupSources**](../mode_management/ecu_state_manager/index.md#7547-ecum_disablewakeupsources) | ECU管理器模块通过调用EcuM_DisableWakeupSources来设置在wakeupSource位域中定义的唤醒源，实现禁止相应的唤醒源唤醒ECU。 |
| [**EcuM_EnableWakeupSources**](../mode_management/ecu_state_manager/index.md#7541-ecum_enablewakeupsources) | ECU管理器模块调用EcuM_EnableWakeupSource以允许系统设计人员通知在wakeupSource位域中定义的唤醒源将进入SLEEP并相应地调整它们的源。 |
| [**EcuM_ErrorHook**](../mode_management/ecu_state_manager/index.md#7511-ecum_errorhook) | 如果发生致命错误，ECU状态管理器将调用此错误Hook。 |
| [**EcuM_GenerateRamHash**](../mode_management/ecu_state_manager/index.md#7542-ecum_generateramhash) | 参见EcuM_CheckRamHash。 |
| [**EcuM_GetBootTarget**](../mode_management/ecu_state_manager/index.md#7372-ecum_getboottarget) | EcuM_GetBootTarget返回当前引导目标 - 请参阅EcuM_SelectBootTarget。 |
| [**EcuM_GetCurrentTime**](../mode_management/ecu_state_manager/index.md#7364-ecum_getcurrenttime) | EcuM_GetCurrentTime返回EcuM时钟的当前值（即电池连接后的时间）。 |
| [**EcuM_GetExpiredWakeupEvents**](../mode_management/ecu_state_manager/index.md#7355-ecum_getexpiredwakeupevents) | 获取过期的唤醒事件。 |
| [**EcuM_GetLastShutdownTarget**](../mode_management/ecu_state_manager/index.md#7343-ecum_getlastshutdowntarget) | EcuM_GetLastShutdownTarget返回上一个关机进程的关机目标。 |
| [**EcuM_GetPendingWakeupEvents**](../mode_management/ecu_state_manager/index.md#7352-ecum_getpendingwakeupevents) | 获取挂起的唤醒事件。 |
| [**EcuM_GetShutdownCause**](../mode_management/ecu_state_manager/index.md#7345-ecum_getshutdowncause) | EcuM_GetShutdownCause返回由EcuM_SelectShutdownCause设置的选定关机原因。 |
| [**EcuM_GetShutdownTarget**](../mode_management/ecu_state_manager/index.md#7342-ecum_getshutdowntarget) | EcuM_GetShutdownTarget返回由EcuM_SelectShutdownTarget设置的当前选择的关闭目标。 |
| [**EcuM_GetValidatedWakeupEvents**](../mode_management/ecu_state_manager/index.md#7354-ecum_getvalidatedwakeupevents) | 获取经过验证的唤醒事件。 |
| [**EcuM_GetVersionInfo**](../mode_management/ecu_state_manager/index.md#7311-ecum_getversioninfo) | 返回此模块的版本信息。 |
| [**EcuM_GetWakeupTime**](../mode_management/ecu_state_manager/index.md#7365-ecum_getwakeuptime) | EcuM_GetWakeupTime返回主闹钟的当前值（所有用户闹钟的最小绝对时间）。 |
| [**EcuM_GoDownHaltPoll**](../mode_management/ecu_state_manager/index.md#7321-ecum_godownhaltpoll) | 根据先前选择的关闭目标，指示ECU状态管理器模块进入睡眠、重启或关闭模式。 |
| [**EcuM_Init**](../mode_management/ecu_state_manager/index.md#7322-ecum_init) | 初始化ECU状态管理器并执行启动程序。 |
| [**EcuM_LoopDetection**](../mode_management/ecu_state_manager/index.md#7525-ecum_loopdetection) | 如果配置参数EcuMResetLoopDetection设置为true，则每次启动时都会调用此Callout。 |
| [**EcuM_MainFunction**](../mode_management/ecu_state_manager/index.md#761-ecum_mainfunction) | 此服务的目的是在操作系统启动并运行时执行ECU状态管理器的所有活动。 |
| [**EcuM_OnGoOffOne**](../mode_management/ecu_state_manager/index.md#7531-ecum_ongooffone) | 该调用允许系统设计者通知将要进入GO OFF I状态。 |
| [**EcuM_OnGoOffTwo**](../mode_management/ecu_state_manager/index.md#7532-ecum_ongoofftwo) | 此调用允许系统设计人员通知即将进入GO OFF II状态。 |
| [**EcuM_ReleasePOST_RUN**](../mode_management/ecu_state_manager/index.md#7335-ecum_releasepost_run) | 释放先前通过调用EcuM_RequestPOST_RUN完成的POST_RUN请求。 |
| [**EcuM_ReleaseRUN**](../mode_management/ecu_state_manager/index.md#7333-ecum_releaserun) | 释放先前通过调用EcuM_RequestRUN完成的RUN请求。 |
| [**EcuM_RequestPOST_RUN**](../mode_management/ecu_state_manager/index.md#7334-ecum_requestpost_run) | 发出对POST_RUN状态的请求。 |
| [**EcuM_RequestRUN**](../mode_management/ecu_state_manager/index.md#7332-ecum_requestrun) | 请求RUN状态。 |
| [**EcuM_SelectBootTarget**](../mode_management/ecu_state_manager/index.md#7371-ecum_selectboottarget) | EcuM_SelectBootTarget选择一个引导目标。 |
| [**EcuM_SelectShutdownCause**](../mode_management/ecu_state_manager/index.md#7344-ecum_selectshutdowncause) | EcuM_SelectShutdownCause选择关机的原因。 |
| [**EcuM_SelectShutdownTarget**](../mode_management/ecu_state_manager/index.md#7341-ecum_selectshutdowntarget) | EcuM_SelectShutdownTarget选择关机目标。 |
| [**EcuM_SetAbsWakeupAlarm**](../mode_management/ecu_state_manager/index.md#7362-ecum_setabswakeupalarm) | EcuM_SetAbsWakeupAlarm将用户的唤醒警报设置为绝对时间点。 |
| [**EcuM_SetClock**](../mode_management/ecu_state_manager/index.md#7366-ecum_setclock) | EcuM_SetClock将EcuM时钟时间设置为提供的值。 |
| [**EcuM_SetRelWakeupAlarm**](../mode_management/ecu_state_manager/index.md#7361-ecum_setrelwakeupalarm) | EcuM_SetRelWakeupAlarm设置用户的唤醒警报相对于当前时间点。 |
| [**EcuM_SetState**](../mode_management/ecu_state_manager/index.md#7331-ecum_setstate) | BswM 调用的函数，用于通知状态切换。 |
| [**EcuM_SetWakeupEvent**](../mode_management/ecu_state_manager/index.md#7411-ecum_setwakeupevent) | 设置唤醒事件。 |
| [**EcuM_Shutdown**](../mode_management/ecu_state_manager/index.md#7324-ecum_shutdown) | 通常由关机挂钩（shutdown hook）调用，此函数接管执行控制并执行GO OFF II活动。 |
| [**EcuM_SleepActivity**](../mode_management/ecu_state_manager/index.md#7543-ecum_sleepactivity) | 在reduced clock sleep模式下Callout会被定期调用。 |
| [**EcuM_StartCheckWakeup**](../mode_management/ecu_state_manager/index.md#7544-ecum_startcheckwakeup) | 此API由ECU固件调用，以启动相应WakeupSource的CheckWakeupTimer。 |
| [**EcuM_StartupTwo**](../mode_management/ecu_state_manager/index.md#7323-ecum_startuptwo) | 该函数实现了STARTUP II状态。 |
| [**EcuM_StartWakeupSources**](../mode_management/ecu_state_manager/index.md#7551-ecum_startwakeupsources) | 此Callout将启动给定的唤醒源，以便它们准备好执行唤醒验证。 |
| [**EcuM_StopWakeupSources**](../mode_management/ecu_state_manager/index.md#7553-ecum_stopwakeupsources) | 在唤醒验证不成功后，此Callout需停止给定的唤醒源。 |
| [**EcuM_ValidateWakeupEvent**](../mode_management/ecu_state_manager/index.md#7412-ecum_validatewakeupevent) | 唤醒后ECU状态管理器将在WAKEUP VALIDATION状态/序列期间，停止进程以等待唤醒事件的验证。 |

## AUTOSAR Eep（EEPROM驱动程序）（11）

来源：[AUTOSAR Eep（EEPROM驱动程序）](../memory/eep/index.md) · SWS_EEPROMDriver

| 函数 | 简述 |
|---|---|
| [**Eep_Cancel**](../memory/eep/index.md#737-eep_cancel) | 服务 ID 0x06。 |
| [**Eep_Compare**](../memory/eep/index.md#736-eep_compare) | 服务 ID 0x05。 |
| [**Eep_Erase**](../memory/eep/index.md#735-eep_erase) | 服务 ID 0x04。 |
| [**Eep_GetJobResult**](../memory/eep/index.md#739-eep_getjobresult) | 服务 ID 0x08。 |
| [**Eep_GetStatus**](../memory/eep/index.md#738-eep_getstatus) | 服务 ID 0x07。 |
| [**Eep_GetVersionInfo**](../memory/eep/index.md#7310-eep_getversioninfo) | 服务 ID 0x0a。 |
| [**Eep_Init**](../memory/eep/index.md#731-eep_init) | 服务 ID 0x00。 |
| [**Eep_MainFunction**](../memory/eep/index.md#751-eep_mainfunction) | 服务 ID 0x09。 |
| [**Eep_Read**](../memory/eep/index.md#733-eep_read) | 服务 ID 0x02。 |
| [**Eep_SetMode**](../memory/eep/index.md#732-eep_setmode) | 服务 ID 0x01。 |
| [**Eep_Write**](../memory/eep/index.md#734-eep_write) | 服务 ID 0x03。 |

## AUTOSAR Ethernet Driver（以太网驱动程序）（21）

来源：[AUTOSAR Ethernet Driver（以太网驱动程序）](../communication/ethernet_driver/index.md) · SWS_EthernetDriver

| 函数 | 简述 |
|---|---|
| [**Eth_EnableEgressTimeStamp**](../communication/ethernet_driver/index.md#714-eth_enableegresstimestamp) | — |
| [**Eth_GetControllerMode**](../communication/ethernet_driver/index.md#73-eth_getcontrollermode) | — |
| [**Eth_GetCounterValues**](../communication/ethernet_driver/index.md#79-eth_getcountervalues) | — |
| [**Eth_GetCurrentTime**](../communication/ethernet_driver/index.md#713-eth_getcurrenttime) | — |
| [**Eth_GetEgressTimeStamp**](../communication/ethernet_driver/index.md#715-eth_getegresstimestamp) | — |
| [**Eth_GetIngressTimeStamp**](../communication/ethernet_driver/index.md#716-eth_getingresstimestamp) | — |
| [**Eth_GetPhysAddr**](../communication/ethernet_driver/index.md#74-eth_getphysaddr) | — |
| [**Eth_GetRxStats**](../communication/ethernet_driver/index.md#710-eth_getrxstats) | — |
| [**Eth_GetTxErrorCounterValues**](../communication/ethernet_driver/index.md#712-eth_gettxerrorcountervalues) | — |
| [**Eth_GetTxStats**](../communication/ethernet_driver/index.md#711-eth_gettxstats) | — |
| [**Eth_GetVersionInfo**](../communication/ethernet_driver/index.md#721-eth_getversioninfo) | — |
| [**Eth_Init**](../communication/ethernet_driver/index.md#71-eth_init) | — |
| [**Eth_ProvideTxBuffer**](../communication/ethernet_driver/index.md#717-eth_providetxbuffer) | — |
| [**Eth_ReadMii**](../communication/ethernet_driver/index.md#78-eth_readmii) | — |
| [**Eth_Receive**](../communication/ethernet_driver/index.md#719-eth_receive) | — |
| [**Eth_SetControllerMode**](../communication/ethernet_driver/index.md#72-eth_setcontrollermode) | — |
| [**Eth_SetPhysAddr**](../communication/ethernet_driver/index.md#75-eth_setphysaddr) | — |
| [**Eth_Transmit**](../communication/ethernet_driver/index.md#718-eth_transmit) | — |
| [**Eth_TxConfirmation**](../communication/ethernet_driver/index.md#720-eth_txconfirmation) | — |
| [**Eth_UpdatePhysAddrFilter**](../communication/ethernet_driver/index.md#76-eth_updatephysaddrfilter) | — |
| [**Eth_WriteMii**](../communication/ethernet_driver/index.md#77-eth_writemii) | — |

## AUTOSAR Ethernet Interface（以太网接口）（136）

来源：[AUTOSAR Ethernet Interface（以太网接口）](../communication/ethernet_interface/index.md) · SWS_EthernetInterface

| 函数 | 简述 |
|---|---|
| [**EthIf_CheckWakeup**](../communication/ethernet_interface/index.md#734-ethif_checkwakeup) | 此 API 请求受影响的以太网硬件检查是否有被通知的唤醒。 |
| [**EthIf_ClearSwitchPortSignalQuality**](../communication/ethernet_interface/index.md#7337-ethif_clearswitchportsignalquality) | 清除给定以太网交换机端口链路的已存储信号质量。 |
| [**EthIf_ClearTrcvSignalQuality**](../communication/ethernet_interface/index.md#7336-ethif_cleartrcvsignalquality) | 清除给定以太网收发器链路的已存储信号质量。 |
| [**EthIf_CtrlModeIndication**](../communication/ethernet_interface/index.md#743-ethif_ctrlmodeindication) | 在模式被读取出来时异步调用。 |
| [**EthIf_DeletePortMirrorConfiguration**](../communication/ethernet_interface/index.md#7372-ethif_deleteportmirrorconfiguration) | 删除给定 MirroredSwitchIdx 的已存储端口镜像配置。 |
| [**EthIf_EnableEgressTimeStamp**](../communication/ethernet_interface/index.md#7323-ethif_enableegresstimestamp) | 在专用的报文对象上激活发送方向时间戳（egress time stamping）。 |
| [**EthIf_EthGetSpiStatus**](../communication/ethernet_interface/index.md#7385-ethif_ethgetspistatus) | 当使用 MACPHY 控制器时，获取 SPI 接口状态。 |
| [**EthIf_GetAndResetMeasurementData**](../communication/ethernet_interface/index.md#7314-ethif_getandresetmeasurementdata) | 允许出于诊断目的读取和重置详细的测量数据。 |
| [**EthIf_GetArlTable**](../communication/ethernet_interface/index.md#7311-ethif_getarltable) | 获取交换机的地址解析表（address resolution table）并将该列表复制到用户提供的缓冲区中。 |
| [**EthIf_GetBufCV2xPC5RxParams**](../communication/ethernet_interface/index.md#7386-ethif_getbufcv2xpc5rxparams) | 读出与所接收数据包的蜂窝 V2X 接收方向相关的值。 |
| [**EthIf_GetBufCV2xPC5TxParams**](../communication/ethernet_interface/index.md#7387-ethif_getbufcv2xpc5txparams) | 读出与所发送数据包的蜂窝 V2X 发送方向相关的值。 |
| [**EthIf_GetBufWRxParams**](../communication/ethernet_interface/index.md#7343-ethif_getbufwrxparams) | 读出与所接收数据包的收发器接收方向相关的值。 |
| [**EthIf_GetBufWTxParams**](../communication/ethernet_interface/index.md#7344-ethif_getbufwtxparams) | 读出与所发送数据包的收发器发送方向相关的值。 |
| [**EthIf_GetCableDiagnosticsResult**](../communication/ethernet_interface/index.md#7341-ethif_getcablediagnosticsresult) | 获取给定收发器的电缆诊断结果。 |
| [**EthIf_GetChanCV2xPC5TxParams**](../communication/ethernet_interface/index.md#7389-ethif_getchancv2xpc5txparams) | 读取与信道接收方向相关的值。 |
| [**EthIf_GetChanRxParams**](../communication/ethernet_interface/index.md#7349-ethif_getchanrxparams) | 读取与收发器接收方向相关的值。 |
| [**EthIf_GetControllerMode**](../communication/ethernet_interface/index.md#733-ethif_getcontrollermode) | 获取被索引控制器的状态。 |
| [**EthIf_GetCtrlIdxList**](../communication/ethernet_interface/index.md#7312-ethif_getctrlidxlist) | 返回所有激活的以太网控制器的数量和索引。 |
| [**EthIf_GetCurrentTime**](../communication/ethernet_interface/index.md#7317-ethif_getcurrenttime) | 根据 HW 的能力，从 HW 寄存器返回一个时间值。 |
| [**EthIf_GetCurrentTimeTuple**](../communication/ethernet_interface/index.md#7318-ethif_getcurrenttimetuple) | 在一个原子操作中读取时间戳时钟的当前时间和 PHC 的当前时间。 |
| [**EthIf_GetEgressTimeStamp**](../communication/ethernet_interface/index.md#7324-ethif_getegresstimestamp) | 在专用的报文对象上读回发送方向时间戳。 |
| [**EthIf_GetIngressTimeStamp**](../communication/ethernet_interface/index.md#7325-ethif_getingresstimestamp) | 在专用的报文对象上读回接收方向时间戳（ingress time stamp）。 |
| [**EthIf_GetPhcTime**](../communication/ethernet_interface/index.md#7321-ethif_getphctime) | 从 PHC 的 HW 寄存器中返回当前时间值。 |
| [**EthIf_GetPhyIdentifier**](../communication/ethernet_interface/index.md#7342-ethif_getphyidentifier) | 按照 IEEE 802.3-2015 第 22.2.4.3.1 节 PHY 标识符（PHY Identifier）的规定获取以太网接口的 PHY 标识符。 |
| [**EthIf_GetPhysAddr**](../communication/ethernet_interface/index.md#737-ethif_getphysaddr) | 获取被索引控制器所使用的物理源地址。 |
| [**EthIf_GetPhyWakeupReason**](../communication/ethernet_interface/index.md#735-ethif_getphywakeupreason) | 此函数通过调用 EthTrcv_GetBusWuReason(...) 获取被索引以太网收发器（PHY）的唤醒原因。 |
| [**EthIf_GetPortCableDiagnosticsResult**](../communication/ethernet_interface/index.md#7378-ethif_getportcablediagnosticsresult) | 获取被索引以太网交换机端口的电缆诊断结果。 |
| [**EthIf_GetPortMacAddr**](../communication/ethernet_interface/index.md#7310-ethif_getportmacaddr) | 获取可以通过其到达该 MAC 地址的端口。 |
| [**EthIf_GetPortMirrorState**](../communication/ethernet_interface/index.md#7373-ethif_getportmirrorstate) | 获取被索引以太网交换机端口的端口镜像当前状态。 |
| [**EthIf_GetRxMgmtObject**](../communication/ethernet_interface/index.md#7329-ethif_getrxmgmtobject) | 请求（在此上下文中）唯一的 DataPtr 的管理对象（MgmtObject）。 |
| [**EthIf_GetStreamHandleIdxStatistics**](../communication/ethernet_interface/index.md#73124-ethif_getstreamhandleidxstatistics) | 此函数由防火墙模块调用，用于从交换机获取桶计数器（bucket counter）统计信息。 |
| [**EthIf_GetSwitchIdentifier**](../communication/ethernet_interface/index.md#7369-ethif_getswitchidentifier) | 获取由 IEEE 为被索引以太网交换机给出的组织唯一标识符。 |
| [**EthIf_GetSwitchPortIdentifier**](../communication/ethernet_interface/index.md#7368-ethif_getswitchportidentifier) | 此函数获取被索引以太网交换机端口的 OUI（24 位）。 |
| [**EthIf_GetSwitchPortMode**](../communication/ethernet_interface/index.md#7355-ethif_getswitchportmode) | 获取被索引交换机端口的模式。 |
| [**EthIf_GetSwitchPortSignalQuality**](../communication/ethernet_interface/index.md#7335-ethif_getswitchportsignalquality) | 获取给定以太网交换机端口链路的信号质量。 |
| [**EthIf_GetSwitchPortWakeupReason**](../communication/ethernet_interface/index.md#736-ethif_getswitchportwakeupreason) | 此函数通过调用 EthSwt_GetSwitchPortWakeupReason() 获取被索引以太网交换机端口的唤醒原因。 |
| [**EthIf_GetTransceiverMode**](../communication/ethernet_interface/index.md#7356-ethif_gettransceivermode) | 获取被索引收发器的状态。 |
| [**EthIf_GetTrcvSignalQuality**](../communication/ethernet_interface/index.md#7334-ethif_gettrcvsignalquality) | 获取给定以太网收发器链路的信号质量。 |
| [**EthIf_GetTxMgmtObject**](../communication/ethernet_interface/index.md#7330-ethif_gettxmgmtobject) | 请求（在此上下文中）唯一的 BufIdx 的管理对象。 |
| [**EthIf_GetVersionInfo**](../communication/ethernet_interface/index.md#7354-ethif_getversioninfo) | 返回本模块的版本信息。 |
| [**EthIf_GetVlanId**](../communication/ethernet_interface/index.md#7313-ethif_getvlanid) | 返回所请求以太网控制器的 VLAN 标识符。 |
| [**EthIf_ImmediateTransmit**](../communication/ethernet_interface/index.md#7352-ethif_immediatetransmit) | 请求发送一个 PDU。 |
| [**EthIf_Init**](../communication/ethernet_interface/index.md#731-ethif_init) | 初始化以太网接口。 |
| [**EthIf_MacSecAddRxSa**](../communication/ethernet_interface/index.md#73107-ethif_macsecaddrxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序在收发器中创建一个接收安全关联。 |
| [**EthIf_MacSecAddRxSaNotification**](../communication/ethernet_interface/index.md#73109-ethif_macsecaddrxsanotification) | 通知 EthIf_MacSecAddRxSa 已完成的回调。 |
| [**EthIf_MacSecAddTxSa**](../communication/ethernet_interface/index.md#7399-ethif_macsecaddtxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序在收发器中创建一个传输安全关联。 |
| [**EthIf_MacSecAddTxSaNotification**](../communication/ethernet_interface/index.md#73101-ethif_macsecaddtxsanotification) | 通知 EthIf_MacSecAddTxSa 已完成的回调。 |
| [**EthIf_MacSecDeleteRxSa**](../communication/ethernet_interface/index.md#73113-ethif_macsecdeleterxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序移除由所提供的关联编号标识的接收安全关联。 |
| [**EthIf_MacSecDeleteTxSa**](../communication/ethernet_interface/index.md#73105-ethif_macsecdeletetxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序移除由所提供的关联编号标识的传输安全关联。 |
| [**EthIf_MacSecGetMacSecStats**](../communication/ethernet_interface/index.md#73117-ethif_macsecgetmacsecstats) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序提供 MACsec 统计信息。 |
| [**EthIf_MacSecGetMacSecStatsNotification**](../communication/ethernet_interface/index.md#73119-ethif_macsecgetmacsecstatsnotification) | 通知 EthIf_MacSecGetMacSecStats 已完成并提供所请求统计信息的回调。 |
| [**EthIf_MacSecGetTxSaNextPn**](../communication/ethernet_interface/index.md#73115-ethif_macsecgettxsanextpn) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序返回给定传输安全关联中用于下一个数据包的包编号。 |
| [**EthIf_MacSecInitRxSc**](../communication/ethernet_interface/index.md#7395-ethif_macsecinitrxsc) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序为给定的安全通道标识符配置一个接收安全通道。 |
| [**EthIf_MacSecOperational**](../communication/ethernet_interface/index.md#73121-ethif_macsecoperational) | 通知 EthIf MACsec 已可运行且可以告知 EthSM。 |
| [**EthIf_MacSecResetRxSc**](../communication/ethernet_interface/index.md#7397-ethif_macsecresetrxsc) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序将给定安全通道标识符的接收安全通道的 MACsec 值重置为默认值。 |
| [**EthIf_MacSecSetControlledPortEnabled**](../communication/ethernet_interface/index.md#73123-ethif_macsecsetcontrolledportenabled) | 请求设置 PAE 的受控端口启用参数。 |
| [**EthIf_MacSecUpdateRxSa**](../communication/ethernet_interface/index.md#73111-ethif_macsecupdaterxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序使用给定的包编号更新接收安全关联。 |
| [**EthIf_MacSecUpdateSecY**](../communication/ethernet_interface/index.md#7391-ethif_macsecupdatesecy) | 请求以太网接口（软件实现的 MACsec）或以太网收发器使用所提供的参数更新 PHY 的 SecY/PAC。 |
| [**EthIf_MacSecUpdateSecYNotification**](../communication/ethernet_interface/index.md#7393-ethif_macsecupdatesecynotification) | 通知 EthIf_SwitchMacSecUpdateSecY 已完成的回调。 |
| [**EthIf_MacSecUpdateTxSa**](../communication/ethernet_interface/index.md#73103-ethif_macsecupdatetxsa) | 请求以太网接口（软件实现的 MACsec）或以太网收发器驱动程序使用给定的包编号更新传输安全关联。 |
| [**EthIf_MainFunctionRx**](../communication/ethernet_interface/index.md#751-ethif_mainfunctionrx) | 该函数检查新接收的帧，并以轮询模式发出接收指示。 |
| [**EthIf_MainFunctionState**](../communication/ethernet_interface/index.md#755-ethif_mainfunctionstate) | 该函数轮询不同的通信硬件（以太网收发器、以太网交换机端口）相关信息，例如链路状态、信号质量。 |
| [**EthIf_MainFunctionTx**](../communication/ethernet_interface/index.md#754-ethif_mainfunctiontx) | 该函数以轮询模式发出发送确认。 |
| [**EthIf_ProvideTxBuffer**](../communication/ethernet_interface/index.md#7350-ethif_providetxbuffer) | 提供对指定以太网控制器的发送缓冲区的访问。 |
| [**EthIf_ReadPortMirrorConfiguration**](../communication/ethernet_interface/index.md#7371-ethif_readportmirrorconfiguration) | 获取给定以太网交换机的端口镜像配置。 |
| [**EthIf_ReleaseRxBuffer**](../communication/ethernet_interface/index.md#7353-ethif_releaserxbuffer) | 来自上层的指示，用于释放底层的接收缓冲区。 |
| [**EthIf_ResetConfiguration**](../communication/ethernet_interface/index.md#7316-ethif_resetconfiguration) | 该函数应以持久的方式请求重置以太网交换机所学习的 MAC/端口表的配置。 |
| [**EthIf_RunCableDiagnostic**](../communication/ethernet_interface/index.md#7380-ethif_runcablediagnostic) | 触发给定以太网收发器的电缆诊断。 |
| [**EthIf_RunPortCableDiagnostic**](../communication/ethernet_interface/index.md#7379-ethif_runportcablediagnostic) | 通过调用所引用以太网收发器的 EthTrcv_RunCableDiagnostic 触发给定以太网交换机端口（PortIdx）的电缆诊断。 |
| [**EthIf_RxIndication**](../communication/ethernet_interface/index.md#741-ethif_rxindication) | 由被索引控制器接收到的以太网帧的接收指示。 |
| [**EthIf_SetBufCV2xPC5TxParams**](../communication/ethernet_interface/index.md#7388-ethif_setbufcv2xpc5txparams) | 为特定缓冲区（要发送的数据包）设置与蜂窝 V2X 发送方向相关的值。 |
| [**EthIf_SetBufWTxParams**](../communication/ethernet_interface/index.md#7345-ethif_setbufwtxparams) | 为特定缓冲区（要发送的数据包）设置与收发器发送方向相关的值。 |
| [**EthIf_SetChanRxParams**](../communication/ethernet_interface/index.md#7347-ethif_setchanrxparams) | 设置与收发器无线信道接收方向相关的值。 |
| [**EthIf_SetChanTxParams**](../communication/ethernet_interface/index.md#7348-ethif_setchantxparams) | 设置与收发器无线信道发送方向相关的值。 |
| [**EthIf_SetControllerMode**](../communication/ethernet_interface/index.md#732-ethif_setcontrollermode) | 启用/禁用被索引的控制器。 |
| [**EthIf_SetForwardingMode**](../communication/ethernet_interface/index.md#7333-ethif_setforwardingmode) | 验证交换机配置。 |
| [**EthIf_SetPhcCorrection**](../communication/ethernet_interface/index.md#7320-ethif_setphccorrection) | 设置 PHC 参数以调整 PHC 的速率和偏移。 |
| [**EthIf_SetPhcTime**](../communication/ethernet_interface/index.md#7319-ethif_setphctime) | 设置 PHC 的绝对时间。 |
| [**EthIf_SetPhyLoopbackMode**](../communication/ethernet_interface/index.md#7339-ethif_setphyloopbackmode) | 激活给定的环回模式（loopback mode）。 |
| [**EthIf_SetPhysAddr**](../communication/ethernet_interface/index.md#738-ethif_setphysaddr) | 设置被索引控制器所使用的物理源地址。 |
| [**EthIf_SetPhyTestMode**](../communication/ethernet_interface/index.md#7338-ethif_setphytestmode) | 激活给定的测试模式。 |
| [**EthIf_SetPhyTxMode**](../communication/ethernet_interface/index.md#7340-ethif_setphytxmode) | 激活给定的发送模式。 |
| [**EthIf_SetPortLoopbackMode**](../communication/ethernet_interface/index.md#7376-ethif_setportloopbackmode) | 激活被索引以太网交换机端口的给定测试环回模式。 |
| [**EthIf_SetPortMirrorState**](../communication/ethernet_interface/index.md#7374-ethif_setportmirrorstate) | 请求为给定的以太网交换机设置端口镜像配置的给定端口镜像状态。 |
| [**EthIf_SetPortTestMode**](../communication/ethernet_interface/index.md#7375-ethif_setporttestmode) | 激活被索引以太网交换机端口的给定测试模式。 |
| [**EthIf_SetPortTxMode**](../communication/ethernet_interface/index.md#7377-ethif_setporttxmode) | 激活被索引以太网交换机端口的给定发送模式。 |
| [**EthIf_SetPpsSignalMode**](../communication/ethernet_interface/index.md#7322-ethif_setppssignalmode) | 启用/禁用 PPS 信号的生成。 |
| [**EthIf_SetRadioParams**](../communication/ethernet_interface/index.md#7346-ethif_setradioparams) | 设置与收发器的无线射频相关的值。 |
| [**EthIf_SetStreamHandleIdxConfiguration**](../communication/ethernet_interface/index.md#73125-ethif_setstreamhandleidxconfiguration) | 此函数由防火墙模块调用，用于控制交换机中某个 StreamHandleIdx 的活动状态。 |
| [**EthIf_SetSwitchMgmtInfo**](../communication/ethernet_interface/index.md#7328-ethif_setswitchmgmtinfo) | 随以太网帧一起提供额外的管理信息，该帧在交换机内需要特殊处理。 |
| [**EthIf_SleepIndication**](../communication/ethernet_interface/index.md#746-ethif_sleepindication) | 如果在网络中检测到睡眠指示（sleep indication），则由相应的 EthTrcv 调用此 API。 |
| [**EthIf_StartAllPorts**](../communication/ethernet_interface/index.md#7327-ethif_startallports) | 请求将所有已配置且受影响的 EthSwtPort 置为 ETH_MODE_ACTIVE。 |
| [**EthIf_StoreConfiguration**](../communication/ethernet_interface/index.md#7315-ethif_storeconfiguration) | 以持久的方式触发存储/重置交换机所学习的 MAC/端口表的配置，例如将由 CDD 使用。 |
| [**EthIf_StreamHandleIdxConfiguration**](../communication/ethernet_interface/index.md#747-ethif_streamhandleidxconfiguration) | 一旦 EthSwtDrv 在交换机中成功设置了 StreamHandleIdx 活动状态，该函数就由 EthSwtDrv 调用。 |
| [**EthIf_StreamHandleIdxStatistics**](../communication/ethernet_interface/index.md#748-ethif_streamhandleidxstatistics) | 一旦 EthSwtDrv 成功地从交换机中获取了桶计数器值，该函数就由 EthSwtDrv 调用。 |
| [**EthIf_SwitchEnableTimeStamping**](../communication/ethernet_interface/index.md#7331-ethif_switchenabletimestamping) | 在由 CtrlIdx 和 BufIdx 寻址的专用报文对象上激活发送方向时间戳。 |
| [**EthIf_SwitchGetCfgDataInfo**](../communication/ethernet_interface/index.md#7382-ethif_switchgetcfgdatainfo) | 获取被索引以太网交换机的数据总大小和内存起始地址。 |
| [**EthIf_SwitchGetCfgDataRaw**](../communication/ethernet_interface/index.md#7381-ethif_switchgetcfgdataraw) | 以可变长度获取被索引以太网交换机内存中的数据。 |
| [**EthIf_SwitchMacSecAddRxSa**](../communication/ethernet_interface/index.md#73106-ethif_switchmacsecaddrxsa) | 请求以太网交换机驱动程序在所提供的端口中创建一个接收安全关联（Reception Secure Association）。 |
| [**EthIf_SwitchMacSecAddRxSaNotification**](../communication/ethernet_interface/index.md#73108-ethif_switchmacsecaddrxsanotification) | 通知 EthIf_SwitchMacSecAddRxSa 已完成的回调。 |
| [**EthIf_SwitchMacSecAddTxSa**](../communication/ethernet_interface/index.md#7398-ethif_switchmacsecaddtxsa) | 请求以太网交换机驱动程序在所提供的端口中创建一个传输安全关联（Transmission Secure Association）。 |
| [**EthIf_SwitchMacSecAddTxSaNotification**](../communication/ethernet_interface/index.md#73100-ethif_switchmacsecaddtxsanotification) | 通知 EthIf_SwitchMacSecAddTxSa 已完成的回调。 |
| [**EthIf_SwitchMacSecDeleteRxSa**](../communication/ethernet_interface/index.md#73112-ethif_switchmacsecdeleterxsa) | 请求以太网交换机驱动程序移除由所提供的关联编号标识的接收安全关联。 |
| [**EthIf_SwitchMacSecDeleteTxSa**](../communication/ethernet_interface/index.md#73104-ethif_switchmacsecdeletetxsa) | 请求以太网交换机驱动程序移除由所提供的关联编号标识的传输安全关联。 |
| [**EthIf_SwitchMacSecGetMacSecStats**](../communication/ethernet_interface/index.md#73116-ethif_switchmacsecgetmacsecstats) | 请求以太网交换机驱动程序提供 MACsec 统计信息。 |
| [**EthIf_SwitchMacSecGetMacSecStatsNotification**](../communication/ethernet_interface/index.md#73118-ethif_switchmacsecgetmacsecstatsnotification) | 通知 EthIf_SwitchMacSecGetMacSecStats 已完成并提供所请求统计信息的回调。 |
| [**EthIf_SwitchMacSecGetTxSaNextPn**](../communication/ethernet_interface/index.md#73114-ethif_switchmacsecgettxsanextpn) | 请求以太网交换机驱动程序返回给定传输安全关联中用于下一个数据包的包编号。 |
| [**EthIf_SwitchMacSecInitRxSc**](../communication/ethernet_interface/index.md#7394-ethif_switchmacsecinitrxsc) | 请求以太网交换机驱动程序为给定的安全通道标识符配置一个接收安全通道（Reception Secure Channel）。 |
| [**EthIf_SwitchMacSecOperational**](../communication/ethernet_interface/index.md#73120-ethif_switchmacsecoperational) | 通知 EthIf MACsec 已可运行（operational）且可以通知 EthSM。 |
| [**EthIf_SwitchMacSecResetRxSc**](../communication/ethernet_interface/index.md#7396-ethif_switchmacsecresetrxsc) | 请求以太网交换机驱动程序将给定安全通道标识符的接收安全通道的 MACsec 值重置为默认值。 |
| [**EthIf_SwitchMacSecSetControlledPortEnabled**](../communication/ethernet_interface/index.md#73122-ethif_switchmacsecsetcontrolledportenabled) | 请求设置 PAE 的受控端口启用（Controlled Port enabled）参数。 |
| [**EthIf_SwitchMacSecUpdateRxSa**](../communication/ethernet_interface/index.md#73110-ethif_switchmacsecupdaterxsa) | 请求以太网交换机驱动程序使用给定的包编号更新接收安全关联。 |
| [**EthIf_SwitchMacSecUpdateSecY**](../communication/ethernet_interface/index.md#7390-ethif_switchmacsecupdatesecy) | 请求以太网交换机使用所提供的参数更新所提供端口的 SecY/PAC。 |
| [**EthIf_SwitchMacSecUpdateSecYNotification**](../communication/ethernet_interface/index.md#7392-ethif_switchmacsecupdatesecynotification) | 通知 EthIf_SwitchMacSecUpdateSecY 已完成的回调。 |
| [**EthIf_SwitchMacSecUpdateTxSa**](../communication/ethernet_interface/index.md#73102-ethif_switchmacsecupdatetxsa) | 请求以太网交换机驱动程序使用给定的包编号更新传输安全关联。 |
| [**EthIf_SwitchPortGetBaudRate**](../communication/ethernet_interface/index.md#7359-ethif_switchportgetbaudrate) | 获取被索引交换机端口的波特率。 |
| [**EthIf_SwitchPortGetCounterValues**](../communication/ethernet_interface/index.md#7363-ethif_switchportgetcountervalues) | 读取交换机相应端口的丢弃计数器值列表。 |
| [**EthIf_SwitchPortGetDuplexMode**](../communication/ethernet_interface/index.md#7361-ethif_switchportgetduplexmode) | 获取被索引交换机端口的双工模式（duplex mode）。 |
| [**EthIf_SwitchPortGetLinkState**](../communication/ethernet_interface/index.md#7357-ethif_switchportgetlinkstate) | 获取被索引交换机端口的链路状态。 |
| [**EthIf_SwitchPortGetMacLearningMode**](../communication/ethernet_interface/index.md#7367-ethif_switchportgetmaclearningmode) | 返回 MAC 学习模式，即 1.) 硬件学习已启用；2.) 硬件学习已禁用；3.) 软件学习已启用。 |
| [**EthIf_SwitchPortGetMaxFIFOBufferFillLevel**](../communication/ethernet_interface/index.md#7383-ethif_switchportgetmaxfifobufferfilllevel) | 该函数获取被索引以太网交换机发送（egress）端口分配的 FIFO 缓冲区的最大数量。 |
| [**EthIf_SwitchPortGetRxStats**](../communication/ethernet_interface/index.md#7364-ethif_switchportgetrxstats) | 返回以 Eth_RxStatsType 定义的一系列统计计数器。 |
| [**EthIf_SwitchPortGetTxErrorCounterValues**](../communication/ethernet_interface/index.md#7366-ethif_switchportgettxerrorcountervalues) | 用于读取发送统计错误计数器值的值列表。 |
| [**EthIf_SwitchPortGetTxStats**](../communication/ethernet_interface/index.md#7365-ethif_switchportgettxstats) | 用于读取发送统计值的值列表。 |
| [**EthIf_SwitchPortGroupRequestMode**](../communication/ethernet_interface/index.md#7326-ethif_switchportgrouprequestmode) | 为 EthIfSwtPortGroup 请求一个模式。 |
| [**EthIf_SwitchPortModeIndication**](../communication/ethernet_interface/index.md#745-ethif_switchportmodeindication) | EthIf 应根据 EthSwtPort 配置确定预期的通知。 |
| [**EthIf_TransceiverGetBaudRate**](../communication/ethernet_interface/index.md#7360-ethif_transceivergetbaudrate) | 获取被索引收发器的波特率。 |
| [**EthIf_TransceiverGetDuplexMode**](../communication/ethernet_interface/index.md#7362-ethif_transceivergetduplexmode) | 获取被索引收发器的双工模式。 |
| [**EthIf_TransceiverGetLinkState**](../communication/ethernet_interface/index.md#7358-ethif_transceivergetlinkstate) | 获取被索引收发器的链路状态。 |
| [**EthIf_TransceiverGetMacMethod**](../communication/ethernet_interface/index.md#7384-ethif_transceivergetmacmethod) | 获取收发器的介质访问模式。 |
| [**EthIf_Transmit**](../communication/ethernet_interface/index.md#7351-ethif_transmit) | 触发对之前已填充的发送缓冲区的发送。 |
| [**EthIf_TrcvModeIndication**](../communication/ethernet_interface/index.md#744-ethif_trcvmodeindication) | 在模式变更被读取出来时异步调用。 |
| [**EthIf_TxConfirmation**](../communication/ethernet_interface/index.md#742-ethif_txconfirmation) | 确认由被索引控制器进行的帧发送。 |
| [**EthIf_UpdatePhysAddrFilter**](../communication/ethernet_interface/index.md#739-ethif_updatephysaddrfilter) | 向被索引控制器的过滤器中添加物理源地址或从中移除物理源地址。 |
| [**EthIf_VerifyConfig**](../communication/ethernet_interface/index.md#7332-ethif_verifyconfig) | 转发给 EthSwt_VerifyConfig。 |
| [**EthIf_WritePortMirrorConfiguration**](../communication/ethernet_interface/index.md#7370-ethif_writeportmirrorconfiguration) | 将给定的端口镜像配置存储在以太网交换机驱动程序中给定 MirroredSwitchIdx 的影子缓冲区（shadow buffer）中。 |

## AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）（76）

来源：[AUTOSAR Ethernet Switch Driver（以太网交换机驱动程序）](../communication/ethernet_switch_driver/index.md) · SWS_EthernetSwitchDriver

| 函数 | 简述 |
|---|---|
| [**EthSwt_BackgroundTask**](../communication/ethernet_switch_driver/index.md#752-ethswt_backgroundtask) | C |
| [**EthSwt_CheckWakeup**](../communication/ethernet_switch_driver/index.md#735-ethswt_checkwakeup) | C |
| [**EthSwt_DeletePortMirrorConfiguration**](../communication/ethernet_switch_driver/index.md#7342-ethswt_deleteportmirrorconfiguration) | C |
| [**EthSwt_EnableVlan**](../communication/ethernet_switch_driver/index.md#7320-ethswt_enablevlan) | C |
| [**EthSwt_EthRxFinishedIndication**](../communication/ethernet_switch_driver/index.md#7328-ethswt_ethrxfinishedindication) | C |
| [**EthSwt_EthRxProcessFrame**](../communication/ethernet_switch_driver/index.md#7327-ethswt_ethrxprocessframe) | C |
| [**EthSwt_EthTxAdaptBufferLength**](../communication/ethernet_switch_driver/index.md#7330-ethswt_ethtxadaptbufferlength) | C |
| [**EthSwt_EthTxFinishedIndication**](../communication/ethernet_switch_driver/index.md#7333-ethswt_ethtxfinishedindication) | C |
| [**EthSwt_EthTxPrepareFrame**](../communication/ethernet_switch_driver/index.md#7329-ethswt_ethtxprepareframe) | C |
| [**EthSwt_EthTxProcessFrame**](../communication/ethernet_switch_driver/index.md#7332-ethswt_ethtxprocessframe) | C |
| [**EthSwt_ExtractStreamHandleIdx**](../communication/ethernet_switch_driver/index.md#7372-ethswt_extractstreamhandleidx) | C |
| [**EthSwt_GetArlTable**](../communication/ethernet_switch_driver/index.md#7311-ethswt_getarltable) | C |
| [**EthSwt_GetBaudRate**](../communication/ethernet_switch_driver/index.md#738-ethswt_getbaudrate) | C |
| [**EthSwt_GetCfgDataInfo**](../communication/ethernet_switch_driver/index.md#7351-ethswt_getcfgdatainfo) | C |
| [**EthSwt_GetCfgDataRaw**](../communication/ethernet_switch_driver/index.md#7350-ethswt_getcfgdataraw) | C |
| [**EthSwt_GetCounterValues**](../communication/ethernet_switch_driver/index.md#7312-ethswt_getcountervalues) | C |
| [**EthSwt_GetDuplexMode**](../communication/ethernet_switch_driver/index.md#739-ethswt_getduplexmode) | C |
| [**EthSwt_GetLinkState**](../communication/ethernet_switch_driver/index.md#737-ethswt_getlinkstate) | C |
| [**EthSwt_GetMacLearningMode**](../communication/ethernet_switch_driver/index.md#7324-ethswt_getmaclearningmode) | C |
| [**EthSwt_GetMaxFIFOBufferFillLevel**](../communication/ethernet_switch_driver/index.md#7353-ethswt_getmaxfifobufferfilllevel) | C |
| [**EthSwt_GetPortCableDiagnosticsResult**](../communication/ethernet_switch_driver/index.md#7349-ethswt_getportcablediagnosticsresult) | C |
| [**EthSwt_GetPortIdentifier**](../communication/ethernet_switch_driver/index.md#7338-ethswt_getportidentifier) | C |
| [**EthSwt_GetPortMacAddr**](../communication/ethernet_switch_driver/index.md#7310-ethswt_getportmacaddr) | C |
| [**EthSwt_GetPortMirrorState**](../communication/ethernet_switch_driver/index.md#7343-ethswt_getportmirrorstate) | C |
| [**EthSwt_GetPortSignalQuality**](../communication/ethernet_switch_driver/index.md#7337-ethswt_getportsignalquality) | C |
| [**EthSwt_GetRxMgmtObject**](../communication/ethernet_switch_driver/index.md#7354-ethswt_getrxmgmtobject) | C |
| [**EthSwt_GetRxStats**](../communication/ethernet_switch_driver/index.md#7313-ethswt_getrxstats) | C |
| [**EthSwt_GetStreamHandleIdxStatistics**](../communication/ethernet_switch_driver/index.md#7373-ethswt_getstreamhandleidxstatistics) | C |
| [**EthSwt_GetSwitchIdentifier**](../communication/ethernet_switch_driver/index.md#7339-ethswt_getswitchidentifier) | C |
| [**EthSwt_GetSwitchPortMode**](../communication/ethernet_switch_driver/index.md#733-ethswt_getswitchportmode) | C |
| [**EthSwt_GetSwitchPortWakeupReason**](../communication/ethernet_switch_driver/index.md#736-ethswt_getswitchportwakeupreason) | C |
| [**EthSwt_GetSwitchReg**](../communication/ethernet_switch_driver/index.md#7316-ethswt_getswitchreg) | C |
| [**EthSwt_GetTxErrorCounterValues**](../communication/ethernet_switch_driver/index.md#7315-ethswt_gettxerrorcountervalues) | C |
| [**EthSwt_GetTxMgmtObject**](../communication/ethernet_switch_driver/index.md#7355-ethswt_gettxmgmtobject) | C |
| [**EthSwt_GetTxStats**](../communication/ethernet_switch_driver/index.md#7314-ethswt_gettxstats) | C |
| [**EthSwt_GetVersionInfo**](../communication/ethernet_switch_driver/index.md#7326-ethswt_getversioninfo) | C |
| [**EthSwt_Init**](../communication/ethernet_switch_driver/index.md#731-ethswt_init) | C |
| [**EthSwt_MacSecAddRxSa**](../communication/ethernet_switch_driver/index.md#7364-ethswt_macsecaddrxsa) | C |
| [**EthSwt_MacSecAddRxSaNotification**](../communication/ethernet_switch_driver/index.md#7365-ethswt_macsecaddrxsanotification) | C |
| [**EthSwt_MacSecAddTxSa**](../communication/ethernet_switch_driver/index.md#7360-ethswt_macsecaddtxsa) | C |
| [**EthSwt_MacSecAddTxSaNotification**](../communication/ethernet_switch_driver/index.md#7361-ethswt_macsecaddtxsanotification) | C |
| [**EthSwt_MacSecDeleteRxSa**](../communication/ethernet_switch_driver/index.md#7367-ethswt_macsecdeleterxsa) | C |
| [**EthSwt_MacSecDeleteTxSa**](../communication/ethernet_switch_driver/index.md#7363-ethswt_macsecdeletetxsa) | C |
| [**EthSwt_MacSecGetMacSecStats**](../communication/ethernet_switch_driver/index.md#7369-ethswt_macsecgetmacsecstats) | C |
| [**EthSwt_MacSecGetMacSecStatsNotification**](../communication/ethernet_switch_driver/index.md#7370-ethswt_macsecgetmacsecstatsnotification) | C |
| [**EthSwt_MacSecGetTxSaNextPn**](../communication/ethernet_switch_driver/index.md#7368-ethswt_macsecgettxsanextpn) | C |
| [**EthSwt_MacSecInitRxSc**](../communication/ethernet_switch_driver/index.md#7358-ethswt_macsecinitrxsc) | C |
| [**EthSwt_MacSecResetRxSc**](../communication/ethernet_switch_driver/index.md#7359-ethswt_macsecresetrxsc) | C |
| [**EthSwt_MacSecSetControlledPortEnabled**](../communication/ethernet_switch_driver/index.md#7371-ethswt_macsecsetcontrolledportenabled) | C |
| [**EthSwt_MacSecUpdateRxSa**](../communication/ethernet_switch_driver/index.md#7366-ethswt_macsecupdaterxsa) | C |
| [**EthSwt_MacSecUpdateSecY**](../communication/ethernet_switch_driver/index.md#7356-ethswt_macsecupdatesecy) | C |
| [**EthSwt_MacSecUpdateSecYNotification**](../communication/ethernet_switch_driver/index.md#7357-ethswt_macsecupdatesecynotification) | C |
| [**EthSwt_MacSecUpdateTxSa**](../communication/ethernet_switch_driver/index.md#7362-ethswt_macsecupdatetxsa) | C |
| [**EthSwt_MainFunction**](../communication/ethernet_switch_driver/index.md#751-ethswt_mainfunction) | C |
| [**EthSwt_NvmSingleBlockCallback**](../communication/ethernet_switch_driver/index.md#7325-ethswt_nvmsingleblockcallback) | C |
| [**EthSwt_PortEnableTimeStamp**](../communication/ethernet_switch_driver/index.md#7334-ethswt_portenabletimestamp) | C |
| [**EthSwt_PortLinkStateRequest**](../communication/ethernet_switch_driver/index.md#7352-ethswt_portlinkstaterequest) | C |
| [**EthSwt_ReadPortMirrorConfiguration**](../communication/ethernet_switch_driver/index.md#7341-ethswt_readportmirrorconfiguration) | C |
| [**EthSwt_ReadTrcvRegister**](../communication/ethernet_switch_driver/index.md#7318-ethswt_readtrcvregister) | C |
| [**EthSwt_ResetConfiguration**](../communication/ethernet_switch_driver/index.md#7322-ethswt_resetconfiguration) | C |
| [**EthSwt_RunPortCableDiagnostic**](../communication/ethernet_switch_driver/index.md#7348-ethswt_runportcablediagnostic) | C |
| [**EthSwt_SetForwardingMode**](../communication/ethernet_switch_driver/index.md#7336-ethswt_setforwardingmode) | C |
| [**EthSwt_SetMacLearningMode**](../communication/ethernet_switch_driver/index.md#7323-ethswt_setmaclearningmode) | C |
| [**EthSwt_SetMgmtInfo**](../communication/ethernet_switch_driver/index.md#7331-ethswt_setmgmtinfo) | C |
| [**EthSwt_SetPortLoopbackMode**](../communication/ethernet_switch_driver/index.md#7346-ethswt_setportloopbackmode) | C |
| [**EthSwt_SetPortMirrorState**](../communication/ethernet_switch_driver/index.md#7344-ethswt_setportmirrorstate) | C |
| [**EthSwt_SetPortTestMode**](../communication/ethernet_switch_driver/index.md#7345-ethswt_setporttestmode) | C |
| [**EthSwt_SetPortTxMode**](../communication/ethernet_switch_driver/index.md#7347-ethswt_setporttxmode) | C |
| [**EthSwt_SetStreamHandleIdxConfiguration**](../communication/ethernet_switch_driver/index.md#7374-ethswt_setstreamhandleidxconfiguration) | C |
| [**EthSwt_SetSwitchPortMode**](../communication/ethernet_switch_driver/index.md#732-ethswt_setswitchportmode) | C |
| [**EthSwt_SetSwitchReg**](../communication/ethernet_switch_driver/index.md#7317-ethswt_setswitchreg) | C |
| [**EthSwt_StartSwitchPortAutoNegotiation**](../communication/ethernet_switch_driver/index.md#734-ethswt_startswitchportautonegotiation) | C |
| [**EthSwt_StoreConfiguration**](../communication/ethernet_switch_driver/index.md#7321-ethswt_storeconfiguration) | C |
| [**EthSwt_VerifyConfig**](../communication/ethernet_switch_driver/index.md#7335-ethswt_verifyconfig) | C |
| [**EthSwt_WritePortMirrorConfiguration**](../communication/ethernet_switch_driver/index.md#7340-ethswt_writeportmirrorconfiguration) | C |
| [**EthSwt_WriteTrcvRegister**](../communication/ethernet_switch_driver/index.md#7319-ethswt_writetrcvregister) | C |

## AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）（38）

来源：[AUTOSAR Ethernet Transceiver Driver（以太网收发器驱动程序）](../communication/eth_trcv/index.md) · SWS_EthernetTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**EthTrcv_CheckWakeup**](../communication/eth_trcv/index.md#735-ethtrcv_checkwakeup) | 在检测到唤醒中断时由 EthIf 调用的服务。 |
| [**EthTrcv_EthSwitchMacSecAddTxSa**](../communication/eth_trcv/index.md#7333-ethtrcv_ethswitchmacsecaddtxsa) | 请求 Ethernet Transceiver Driver 在收发器中创建一个发送安全关联。 |
| [**EthTrcv_EthSwitchMacSecUpdateSecY**](../communication/eth_trcv/index.md#7332-ethtrcv_ethswitchmacsecupdatesecy) | 请求 Ethernet Transceiver Driver 用所提供的参数更新交换机端口 PHY 的 SecY/PAC。 |
| [**EthTrcv_GetBaudRate**](../communication/eth_trcv/index.md#739-ethtrcv_getbaudrate) | 获取被索引收发器的波特率。 |
| [**EthTrcv_GetBusWuReason**](../communication/eth_trcv/index.md#734-ethtrcv_getbuswureason) | 该函数返回最近一次的唤醒原因。 |
| [**EthTrcv_GetCableDiagnosticsResult**](../communication/eth_trcv/index.md#7316-ethtrcv_getcablediagnosticsresult) | 获取给定收发器的电缆诊断结果。 |
| [**EthTrcv_GetDuplexMode**](../communication/eth_trcv/index.md#7310-ethtrcv_getduplexmode) | 获取被索引收发器的双工模式。 |
| [**EthTrcv_GetLinkState**](../communication/eth_trcv/index.md#738-ethtrcv_getlinkstate) | 获取被索引收发器的链路状态。 |
| [**EthTrcv_GetMacMethod**](../communication/eth_trcv/index.md#7318-ethtrcv_getmacmethod) | 获取被索引收发器的介质访问控制方法。 |
| [**EthTrcv_GetPhyIdentifier**](../communication/eth_trcv/index.md#7317-ethtrcv_getphyidentifier) | 按照 IEEE 802.3-2015 第 22.2.4.3.1 章「PHY Identifier」获取以太网收发器的 PHY 标识。 |
| [**EthTrcv_GetPhySignalQuality**](../communication/eth_trcv/index.md#7313-ethtrcv_getphysignalquality) | 获取被索引收发器链路的当前信号质量。 |
| [**EthTrcv_GetTransceiverMode**](../communication/eth_trcv/index.md#733-ethtrcv_gettransceivermode) | 获取被索引收发器的状态。 |
| [**EthTrcv_GetVersionInfo**](../communication/eth_trcv/index.md#7319-ethtrcv_getversioninfo) | 返回本模块的版本信息。 |
| [**EthTrcv_Init**](../communication/eth_trcv/index.md#731-ethtrcv_init) | 初始化 Ethernet Transceiver Driver。 |
| [**EthTrcv_MacSecAddRxSa**](../communication/eth_trcv/index.md#7326-ethtrcv_macsecaddrxsa) | 请求 Ethernet Transceiver Driver 在收发器中创建一个接收安全关联（Reception Secure Association）。 |
| [**EthTrcv_MacSecAddTxSa**](../communication/eth_trcv/index.md#7323-ethtrcv_macsecaddtxsa) | 请求 Ethernet Transceiver Driver 在收发器中创建一个发送安全关联（Transmission Secure Association）。 |
| [**EthTrcv_MacSecDeleteRxSa**](../communication/eth_trcv/index.md#7328-ethtrcv_macsecdeleterxsa) | 请求 Ethernet Transceiver Driver 移除由所提供关联编号标识的接收安全关联。 |
| [**EthTrcv_MacSecDeleteTxSa**](../communication/eth_trcv/index.md#7325-ethtrcv_macsecdeletetxsa) | 请求 Ethernet Transceiver Driver 移除由所提供关联编号标识的发送安全关联。 |
| [**EthTrcv_MacSecGetMacSecStats**](../communication/eth_trcv/index.md#7330-ethtrcv_macsecgetmacsecstats) | 请求 Ethernet Transceiver Driver 提供 MACsec 统计信息。 |
| [**EthTrcv_MacSecGetTxSaNextPn**](../communication/eth_trcv/index.md#7329-ethtrcv_macsecgettxsanextpn) | 请求 Ethernet Transceiver Driver 返回在给定发送安全关联中用于下一个包的包编号。 |
| [**EthTrcv_MacSecInitRxSc**](../communication/eth_trcv/index.md#7321-ethtrcv_macsecinitrxsc) | 请求 Ethernet Transceiver Driver 为给定的安全通道标识符配置一个接收安全通道（Reception Secure Channel）。 |
| [**EthTrcv_MacSecResetRxSc**](../communication/eth_trcv/index.md#7322-ethtrcv_macsecresetrxsc) | 请求 Ethernet Transceiver Driver 将给定安全通道标识符的接收安全通道的 MACsec 取值重置为默认值。 |
| [**EthTrcv_MacSecSetControlledPortEnabled**](../communication/eth_trcv/index.md#7331-ethtrcv_macsecsetcontrolledportenabled) | 请求设置 PAE 的受控端口（Controlled Port）启用参数。 |
| [**EthTrcv_MacSecUpdateRxSa**](../communication/eth_trcv/index.md#7327-ethtrcv_macsecupdaterxsa) | 请求 Ethernet Transceiver Driver 用给定的包编号更新接收安全关联。 |
| [**EthTrcv_MacSecUpdateSecY**](../communication/eth_trcv/index.md#7320-ethtrcv_macsecupdatesecy) | 请求以太网收发器用所提供的参数更新 PHY 的 SecY/PAC。 |
| [**EthTrcv_MacSecUpdateTxSa**](../communication/eth_trcv/index.md#7324-ethtrcv_macsecupdatetxsa) | 请求 Ethernet Transceiver Driver 用给定的包编号更新发送安全关联。 |
| [**EthTrcv_MainFunction**](../communication/eth_trcv/index.md#751-ethtrcv_mainfunction) | 用于轮询状态变化和唤醒原因。 |
| [**EthTrcv_ReadMiiIndication**](../communication/eth_trcv/index.md#741-ethtrcv_readmiiindication) | 当经由 MII 接口读出信息时被调用。 |
| [**EthTrcv_RunCableDiagnostic**](../communication/eth_trcv/index.md#7315-ethtrcv_runcablediagnostic) | 为给定的以太网收发器触发电缆诊断。 |
| [**EthTrcv_SetPhyLoopbackMode**](../communication/eth_trcv/index.md#7312-ethtrcv_setphyloopbackmode) | 激活给定的回环模式。 |
| [**EthTrcv_SetPhyTestMode**](../communication/eth_trcv/index.md#7311-ethtrcv_setphytestmode) | 激活给定的测试模式。 |
| [**EthTrcv_SetPhyTxMode**](../communication/eth_trcv/index.md#7314-ethtrcv_setphytxmode) | 激活给定的发送模式。 |
| [**EthTrcv_SetTransceiverMode**](../communication/eth_trcv/index.md#732-ethtrcv_settransceivermode) | 启用/禁用被索引的收发器。 |
| [**EthTrcv_StartAutoNegotiation**](../communication/eth_trcv/index.md#736-ethtrcv_startautonegotiation) | 重新启动被索引收发器所使用的传输参数的协商。 |
| [**EthTrcv_SwitchMacSecAddRxSa**](../communication/eth_trcv/index.md#7334-ethtrcv_switchmacsecaddrxsa) | 请求 Ethernet Transceiver Driver 在收发器中创建一个接收安全关联。 |
| [**EthTrcv_SwitchMacSecGetMacSecStats**](../communication/eth_trcv/index.md#7335-ethtrcv_switchmacsecgetmacsecstats) | 请求 Ethernet Transceiver Driver 提供 MACsec 统计信息。 |
| [**EthTrcv_TransceiverLinkStateRequest**](../communication/eth_trcv/index.md#737-ethtrcv_transceiverlinkstaterequest) | 为给定的收发器请求给定的链路状态。 |
| [**EthTrcv_WriteMiiIndication**](../communication/eth_trcv/index.md#742-ethtrcv_writemiiindication) | 当经由 MII 接口写入信息时被调用。 |

## AUTOSAR FEE（闪存EEPROM仿真）（11）

来源：[AUTOSAR FEE（闪存EEPROM仿真）](../memory/flash_eeprom_emulation/index.md) · SWS_FlashEEPROMEmulation

| 函数 | 简述 |
|---|---|
| [**Fee_Cancel**](../memory/flash_eeprom_emulation/index.md#734-fee_cancel) | 服务 ID 0x04。 |
| [**Fee_EraseImmediateBlock**](../memory/flash_eeprom_emulation/index.md#739-fee_eraseimmediateblock) | 服务 ID 0x09。 |
| [**Fee_GetJobResult**](../memory/flash_eeprom_emulation/index.md#736-fee_getjobresult) | 服务 ID 0x06。 |
| [**Fee_GetStatus**](../memory/flash_eeprom_emulation/index.md#735-fee_getstatus) | 服务 ID 0x05。 |
| [**Fee_GetVersionInfo**](../memory/flash_eeprom_emulation/index.md#738-fee_getversioninfo) | 服务 ID 0x08。 |
| [**Fee_Init**](../memory/flash_eeprom_emulation/index.md#731-fee_init) | 服务 ID 0x00。 |
| [**Fee_InvalidateBlock**](../memory/flash_eeprom_emulation/index.md#737-fee_invalidateblock) | 服务 ID 0x07。 |
| [**Fee_JobEndNotification**](../memory/flash_eeprom_emulation/index.md#741-fee_jobendnotification) | 服务 ID 0x10。 |
| [**Fee_MainFunction**](../memory/flash_eeprom_emulation/index.md#751-fee_mainfunction) | 服务 ID 0x12。 |
| [**Fee_Read**](../memory/flash_eeprom_emulation/index.md#732-fee_read) | 服务 ID 0x02。 |
| [**Fee_Write**](../memory/flash_eeprom_emulation/index.md#733-fee_write) | 服务 ID 0x03。 |

## AUTOSAR FiM（功能禁止管理器）（10）

来源：[AUTOSAR FiM（功能禁止管理器）](../system_services/function_inhibition_manager/index.md) · SWS_FunctionInhibitionManager

| 函数 | 简述 |
|---|---|
| [**FiM_ControlFunctionAvailable**](../system_services/function_inhibition_manager/index.md#7412-fim_controlfunctionavailable) | — |
| [**FiM_DemInit**](../system_services/function_inhibition_manager/index.md#7333-fim_deminit) | 此服务重新初始化FIM。 |
| [**FiM_DemTriggerOnComponentStatus**](../system_services/function_inhibition_manager/index.md#7332-fim_demtriggeroncomponentstatus) | 该服务触发组件失败状态的变化。 |
| [**FiM_DemTriggerOnMonitorStatus**](../system_services/function_inhibition_manager/index.md#7331-fim_demtriggeronmonitorstatus) | 该服务由Dem调用，以通知Fim监视器状态更改。 |
| [**FiM_FunctionInhibition**](../system_services/function_inhibition_manager/index.md#7411-fim_functioninhibition) | — |
| [**FiM_GetFunctionPermission**](../system_services/function_inhibition_manager/index.md#7321-fim_getfunctionpermission) | 此服务将权限状态报告给功能组。 |
| [**FiM_GetVersionInfo**](../system_services/function_inhibition_manager/index.md#7334-fim_getversioninfo) | 该服务返回该模块的版本信息。 |
| [**FiM_Init**](../system_services/function_inhibition_manager/index.md#7311-fim_init) | 此服务初始化FIM。 |
| [**FiM_MainFunction**](../system_services/function_inhibition_manager/index.md#7351-fim_mainfunction) | 该服务由基础软件模块调度程序直接调用。 |
| [**FiM_SetFunctionAvailable**](../system_services/function_inhibition_manager/index.md#7322-fim_setfunctionavailable) | 该服务设置功能的可用性。 |

## AUTOSAR FlexRay AUTOSAR 传输层（FlexRay AUTOSAR Transport Layer）（11）

来源：[AUTOSAR FlexRay AUTOSAR 传输层（FlexRay AUTOSAR Transport Layer）](../communication/flexray_ar_transport_layer/index.md) · SWS_FlexRayARTransportLayer

| 函数 | 简述 |
|---|---|
| [**FrArTp_CancelReceive**](../communication/flexray_ar_transport_layer/index.md#8333-frartp_cancelreceive) | — |
| [**FrArTp_CancelTransmit**](../communication/flexray_ar_transport_layer/index.md#8332-frartp_canceltransmit) | — |
| [**FrArTp_ChangeParameter**](../communication/flexray_ar_transport_layer/index.md#8334-frartp_changeparameter) | — |
| [**FrArTp_GetVersionInfo**](../communication/flexray_ar_transport_layer/index.md#8311-frartp_getversioninfo) | — |
| [**FrArTp_Init**](../communication/flexray_ar_transport_layer/index.md#8321-frartp_init) | — |
| [**FrArTp_MainFunction**](../communication/flexray_ar_transport_layer/index.md#851-frartp_mainfunction) | — |
| [**FrArTp_RxIndication**](../communication/flexray_ar_transport_layer/index.md#842-frartp_rxindication) | — |
| [**FrArTp_Shutdown**](../communication/flexray_ar_transport_layer/index.md#8322-frartp_shutdown) | — |
| [**FrArTp_Transmit**](../communication/flexray_ar_transport_layer/index.md#8331-frartp_transmit) | — |
| [**FrArTp_TriggerTransmit**](../communication/flexray_ar_transport_layer/index.md#841-frartp_triggertransmit) | — |
| [**FrArTp_TxConfirmation**](../communication/flexray_ar_transport_layer/index.md#843-frartp_txconfirmation) | — |

## AUTOSAR FlexRay Driver（FlexRay 驱动程序）（32）

来源：[AUTOSAR FlexRay Driver（FlexRay 驱动程序）](../communication/flexray_driver/index.md) · SWS_FlexRayDriver

| 函数 | 简述 |
|---|---|
| [**Fr_AbortCommunication**](../communication/flexray_driver/index.md#747-fr_abortcommunication) | 调用 CC CHI 命令「FREEZE」。 |
| [**Fr_AckAbsoluteTimerIRQ**](../communication/flexray_driver/index.md#7428-fr_ackabsolutetimerirq) | 复位一个绝对定时器的中断条件。 |
| [**Fr_AllowColdstart**](../communication/flexray_driver/index.md#744-fr_allowcoldstart) | 调用 CC CHI 命令「ALLOW_COLDSTART」。 |
| [**Fr_AllSlots**](../communication/flexray_driver/index.md#745-fr_allslots) | 调用 CC CHI 命令「ALL_SLOTS」。 |
| [**Fr_CancelAbsoluteTimer**](../communication/flexray_driver/index.md#7426-fr_cancelabsolutetimer) | 停止一个绝对定时器。 |
| [**Fr_CancelTxLPdu**](../communication/flexray_driver/index.md#7412-fr_canceltxlpdu) | 取消控制器物理发送资源（例如报文缓冲区）中已挂起的 LPdu 发送。 |
| [**Fr_CheckTxLPduStatus**](../communication/flexray_driver/index.md#7414-fr_checktxlpdustatus) | 检查 LSdu 的发送状态。 |
| [**Fr_ControllerInit**](../communication/flexray_driver/index.md#742-fr_controllerinit) | 初始化一个 FlexRay CC。 |
| [**Fr_DisableAbsoluteTimerIRQ**](../communication/flexray_driver/index.md#7429-fr_disableabsolutetimerirq) | 禁用一个绝对定时器的中断线路。 |
| [**Fr_DisableLPdu**](../communication/flexray_driver/index.md#7417-fr_disablelpdu) | 禁用一个 LPdu。 |
| [**Fr_EnableAbsoluteTimerIRQ**](../communication/flexray_driver/index.md#7427-fr_enableabsolutetimerirq) | 启用一个绝对定时器的中断线路。 |
| [**Fr_GetAbsoluteTimerIRQStatus**](../communication/flexray_driver/index.md#7430-fr_getabsolutetimerirqstatus) | 返回绝对定时器的中断挂起状态。 |
| [**Fr_GetChannelStatus**](../communication/flexray_driver/index.md#7421-fr_getchannelstatus) | 获取信道状态信息。 |
| [**Fr_GetClockCorrection**](../communication/flexray_driver/index.md#7422-fr_getclockcorrection) | 获取当前的时钟校正取值。 |
| [**Fr_GetGlobalTime**](../communication/flexray_driver/index.md#7418-fr_getglobaltime) | 获取当前的全局 FlexRay 时间。 |
| [**Fr_GetNmVector**](../communication/flexray_driver/index.md#7419-fr_getnmvector) | 获取上一个通信循环的网络管理向量。 |
| [**Fr_GetNumOfStartupFrames**](../communication/flexray_driver/index.md#7420-fr_getnumofstartupframes) | 获取在集群上看到的当前启动帧数量。 |
| [**Fr_GetPOCStatus**](../communication/flexray_driver/index.md#7410-fr_getpocstatus) | 获取 POC 状态。 |
| [**Fr_GetSyncFrameList**](../communication/flexray_driver/index.md#7423-fr_getsyncframelist) | 获取在信道 A 和信道 B 上经由偶数和奇数通信循环接收或发送的同步帧列表。 |
| [**Fr_GetVersionInfo**](../communication/flexray_driver/index.md#7431-fr_getversioninfo) | 返回本模块的版本信息。 |
| [**Fr_GetWakeupRxStatus**](../communication/flexray_driver/index.md#7424-fr_getwakeuprxstatus) | 从 FlexRay 控制器获取唤醒接收信息。 |
| [**Fr_HaltCommunication**](../communication/flexray_driver/index.md#746-fr_haltcommunication) | 调用 CC CHI 命令「DEFERRED_HALT」。 |
| [**Fr_Init**](../communication/flexray_driver/index.md#741-fr_init) | 初始化 Fr。 |
| [**Fr_PrepareLPdu**](../communication/flexray_driver/index.md#7415-fr_preparelpdu) | 准备一个 LPdu。 |
| [**Fr_ReadCCConfig**](../communication/flexray_driver/index.md#7432-fr_readccconfig) | 从模块的配置中为特定 FlexRay 控制器读取一个 FlexRay 协议配置参数。 |
| [**Fr_ReceiveRxLPdu**](../communication/flexray_driver/index.md#7413-fr_receiverxlpdu) | 从 FlexRay 网络接收数据。 |
| [**Fr_ReconfigLPdu**](../communication/flexray_driver/index.md#7416-fr_reconfiglpdu) | 在运行时根据参数（FrameId、Channel、CycleRepetition、CycleOffset、PayloadLength、HeaderCRC）重新配置一个给定的 LPdu。 |
| [**Fr_SendWUP**](../communication/flexray_driver/index.md#748-fr_sendwup) | 调用 CC CHI 命令「WAKEUP」。 |
| [**Fr_SetAbsoluteTimer**](../communication/flexray_driver/index.md#7425-fr_setabsolutetimer) | 设置绝对的 FlexRay 定时器。 |
| [**Fr_SetWakeupChannel**](../communication/flexray_driver/index.md#749-fr_setwakeupchannel) | 设置唤醒信道。 |
| [**Fr_StartCommunication**](../communication/flexray_driver/index.md#743-fr_startcommunication) | 启动通信。 |
| [**Fr_TransmitTxLPdu**](../communication/flexray_driver/index.md#7411-fr_transmittxlpdu) | 在 FlexRay 网络上发送数据。 |

## AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）（11）

来源：[AUTOSAR FlexRay ISO Transport Layer（FlexRay ISO 传输层）](../communication/flexray_iso_transport_layer/index.md) · SWS_FlexRayISOTransportLayer

| 函数 | 简述 |
|---|---|
| [**FrTp_CancelReceive**](../communication/flexray_iso_transport_layer/index.md#7334-frtp_cancelreceive) | C |
| [**FrTp_CancelTransmit**](../communication/flexray_iso_transport_layer/index.md#7332-frtp_canceltransmit) | C |
| [**FrTp_ChangeParameter**](../communication/flexray_iso_transport_layer/index.md#7333-frtp_changeparameter) | C |
| [**FrTp_GetVersionInfo**](../communication/flexray_iso_transport_layer/index.md#7311-frtp_getversioninfo) | C |
| [**FrTp_Init**](../communication/flexray_iso_transport_layer/index.md#7321-frtp_init) | C |
| [**FrTp_MainFunction**](../communication/flexray_iso_transport_layer/index.md#751-frtp_mainfunction) | C |
| [**FrTp_RxIndication**](../communication/flexray_iso_transport_layer/index.md#742-frtp_rxindication) | C |
| [**FrTp_Shutdown**](../communication/flexray_iso_transport_layer/index.md#7322-frtp_shutdown) | C |
| [**FrTp_Transmit**](../communication/flexray_iso_transport_layer/index.md#7331-frtp_transmit) | C |
| [**FrTp_TriggerTransmit**](../communication/flexray_iso_transport_layer/index.md#741-frtp_triggertransmit) | C |
| [**FrTp_TxConfirmation**](../communication/flexray_iso_transport_layer/index.md#743-frtp_txconfirmation) | C |

## AUTOSAR FlexRay 接口（FlexRay Interface）（43）

来源：[AUTOSAR FlexRay 接口（FlexRay Interface）](../communication/flexray_interface/index.md) · SWS_FlexRayInterface

| 函数 | 简述 |
|---|---|
| [**FrIf_AbortCommunication**](../communication/flexray_interface/index.md#738-frif_abortcommunication) | — |
| [**FrIf_AckAbsoluteTimerIRQ**](../communication/flexray_interface/index.md#735-frif_ackabsolutetimerirq) | — |
| [**FrIf_AllowColdstart**](../communication/flexray_interface/index.md#7315-frif_allowcoldstart) | — |
| [**FrIf_AllSlots**](../communication/flexray_interface/index.md#741-frif_allslots) | — |
| [**FrIf_CancelAbsoluteTimer**](../communication/flexray_interface/index.md#7323-frif_cancelabsolutetimer) | — |
| [**FrIf_CancelTransmit**](../communication/flexray_interface/index.md#747-frif_canceltransmit) | — |
| [**FrIf_CheckWakeupByTransceiver**](../communication/flexray_interface/index.md#761-frif_checkwakeupbytransceiver) | — |
| [**FrIf_ClearTransceiverWakeup**](../communication/flexray_interface/index.md#7322-frif_cleartransceiverwakeup) | — |
| [**FrIf_ControllerInit**](../communication/flexray_interface/index.md#732-frif_controllerinit) | — |
| [**FrIf_DisableAbsoluteTimerIRQ**](../communication/flexray_interface/index.md#7325-frif_disableabsolutetimerirq) | — |
| [**FrIf_DisableLPdu**](../communication/flexray_interface/index.md#748-frif_disablelpdu) | — |
| [**FrIf_DisableTransceiverBranch**](../communication/flexray_interface/index.md#7411-frif_disabletransceiverbranch) | — |
| [**FrIf_EnableAbsoluteTimerIRQ**](../communication/flexray_interface/index.md#734-frif_enableabsolutetimerirq) | — |
| [**FrIf_EnableBusMirroring**](../communication/flexray_interface/index.md#7416-frif_enablebusmirroring) | — |
| [**FrIf_EnableTransceiverBranch**](../communication/flexray_interface/index.md#7410-frif_enabletransceiverbranch) | — |
| [**FrIf_GetAbsoluteTimerIRQStatus**](../communication/flexray_interface/index.md#7324-frif_getabsolutetimerirqstatus) | — |
| [**FrIf_GetChannelStatus**](../communication/flexray_interface/index.md#742-frif_getchannelstatus) | — |
| [**FrIf_GetClockCorrection**](../communication/flexray_interface/index.md#743-frif_getclockcorrection) | — |
| [**FrIf_GetCycleLength**](../communication/flexray_interface/index.md#7326-frif_getcyclelength) | — |
| [**FrIf_GetGlobalTime**](../communication/flexray_interface/index.md#7314-frif_getglobaltime) | — |
| [**FrIf_GetMacrotickDuration**](../communication/flexray_interface/index.md#7317-frif_getmacrotickduration) | — |
| [**FrIf_GetMacroticksPerCycle**](../communication/flexray_interface/index.md#7316-frif_getmacrotickspercycle) | — |
| [**FrIf_GetNmVector**](../communication/flexray_interface/index.md#7413-frif_getnmvector) | — |
| [**FrIf_GetNumOfStartupFrames**](../communication/flexray_interface/index.md#745-frif_getnumofstartupframes) | — |
| [**FrIf_GetPOCStatus**](../communication/flexray_interface/index.md#7313-frif_getpocstatus) | — |
| [**FrIf_GetState**](../communication/flexray_interface/index.md#739-frif_getstate) | — |
| [**FrIf_GetSyncFrameList**](../communication/flexray_interface/index.md#744-frif_getsyncframelist) | — |
| [**FrIf_GetTransceiverError**](../communication/flexray_interface/index.md#749-frif_gettransceivererror) | — |
| [**FrIf_GetTransceiverMode**](../communication/flexray_interface/index.md#7320-frif_gettransceivermode) | — |
| [**FrIf_GetTransceiverWUReason**](../communication/flexray_interface/index.md#7321-frif_gettransceiverwureason) | — |
| [**FrIf_GetVersionInfo**](../communication/flexray_interface/index.md#7414-frif_getversioninfo) | — |
| [**FrIf_GetWakeupRxStatus**](../communication/flexray_interface/index.md#746-frif_getwakeuprxstatus) | — |
| [**FrIf_HaltCommunication**](../communication/flexray_interface/index.md#737-frif_haltcommunication) | — |
| [**FrIf_Init**](../communication/flexray_interface/index.md#731-frif_init) | — |
| [**FrIf_ReadCCConfig**](../communication/flexray_interface/index.md#7415-frif_readccconfig) | — |
| [**FrIf_ReconfigLPdu**](../communication/flexray_interface/index.md#7412-frif_reconfiglpdu) | — |
| [**FrIf_SendWUP**](../communication/flexray_interface/index.md#7312-frif_sendwup) | — |
| [**FrIf_SetAbsoluteTimer**](../communication/flexray_interface/index.md#733-frif_setabsolutetimer) | — |
| [**FrIf_SetState**](../communication/flexray_interface/index.md#7310-frif_setstate) | — |
| [**FrIf_SetTransceiverMode**](../communication/flexray_interface/index.md#7319-frif_settransceivermode) | — |
| [**FrIf_SetWakeupChannel**](../communication/flexray_interface/index.md#7311-frif_setwakeupchannel) | — |
| [**FrIf_StartCommunication**](../communication/flexray_interface/index.md#736-frif_startcommunication) | — |
| [**FrIf_Transmit**](../communication/flexray_interface/index.md#7318-frif_transmit) | — |

## AUTOSAR FlexRay 收发器驱动（FlexRay Transceiver Driver）（11）

来源：[AUTOSAR FlexRay 收发器驱动（FlexRay Transceiver Driver）](../communication/flexray_transceiver_driver/index.md) · SWS_FlexRayTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**FrTrcv_CheckWakeupByTransceiver**](../communication/flexray_transceiver_driver/index.md#737-frtrcv_checkwakeupbytransceiver) | — |
| [**FrTrcv_ClearTransceiverWakeup**](../communication/flexray_transceiver_driver/index.md#736-frtrcv_cleartransceiverwakeup) | — |
| [**FrTrcv_DisableTransceiverBranch**](../communication/flexray_transceiver_driver/index.md#739-frtrcv_disabletransceiverbranch) | — |
| [**FrTrcv_EnableTransceiverBranch**](../communication/flexray_transceiver_driver/index.md#7310-frtrcv_enabletransceiverbranch) | — |
| [**FrTrcv_GetTransceiverError**](../communication/flexray_transceiver_driver/index.md#738-frtrcv_gettransceivererror) | — |
| [**FrTrcv_GetTransceiverMode**](../communication/flexray_transceiver_driver/index.md#733-frtrcv_gettransceivermode) | — |
| [**FrTrcv_GetTransceiverWUReason**](../communication/flexray_transceiver_driver/index.md#734-frtrcv_gettransceiverwureason) | — |
| [**FrTrcv_GetVersionInfo**](../communication/flexray_transceiver_driver/index.md#735-frtrcv_getversioninfo) | — |
| [**FrTrcv_Init**](../communication/flexray_transceiver_driver/index.md#731-frtrcv_init) | — |
| [**FrTrcv_MainFunction**](../communication/flexray_transceiver_driver/index.md#751-frtrcv_mainfunction) | — |
| [**FrTrcv_SetTransceiverMode**](../communication/flexray_transceiver_driver/index.md#732-frtrcv_settransceivermode) | — |

## AUTOSAR FlexRay 状态管理器（FlexRay State Manager）（6）

来源：[AUTOSAR FlexRay 状态管理器（FlexRay State Manager）](../communication/flexray_state_manager/index.md) · SWS_FlexRayStateManager

| 函数 | 简述 |
|---|---|
| [**FrSM_AllSlots**](../communication/flexray_state_manager/index.md#735-frsm_allslots) | — |
| [**FrSM_GetCurrentComMode**](../communication/flexray_state_manager/index.md#733-frsm_getcurrentcommode) | — |
| [**FrSM_GetVersionInfo**](../communication/flexray_state_manager/index.md#734-frsm_getversioninfo) | — |
| [**FrSM_Init**](../communication/flexray_state_manager/index.md#731-frsm_init) | — |
| [**FrSM_RequestComMode**](../communication/flexray_state_manager/index.md#732-frsm_requestcommode) | — |
| [**FrSM_SetEcuPassive**](../communication/flexray_state_manager/index.md#736-frsm_setecupassive) | — |

## AUTOSAR FlexRay 网络管理（FlexRay Network Management）（30）

来源：[AUTOSAR FlexRay 网络管理（FlexRay Network Management）](../communication/flexray_network_management/index.md) · SWS_FlexRayNetworkManagement

| 函数 | 简述 |
|---|---|
| [**FrNm_ActivateTxPnShutdownMsg**](../communication/flexray_network_management/index.md#7321-frnm_activatetxpnshutdownmsg) | — |
| [**FrNm_CheckRemoteSleepIndication**](../communication/flexray_network_management/index.md#7312-frnm_checkremotesleepindication) | — |
| [**FrNm_DeactivateTxPnShutdownMsg**](../communication/flexray_network_management/index.md#7322-frnm_deactivatetxpnshutdownmsg) | — |
| [**FrNm_DisableCommunication**](../communication/flexray_network_management/index.md#7318-frnm_disablecommunication) | — |
| [**FrNm_EnableCommunication**](../communication/flexray_network_management/index.md#7317-frnm_enablecommunication) | — |
| [**FrNm_GetLocalNodeIdentifier**](../communication/flexray_network_management/index.md#7310-frnm_getlocalnodeidentifier) | — |
| [**FrNm_GetNodeIdentifier**](../communication/flexray_network_management/index.md#739-frnm_getnodeidentifier) | — |
| [**FrNm_GetPduData**](../communication/flexray_network_management/index.md#737-frnm_getpdudata) | — |
| [**FrNm_GetState**](../communication/flexray_network_management/index.md#7313-frnm_getstate) | — |
| [**FrNm_GetUserData**](../communication/flexray_network_management/index.md#736-frnm_getuserdata) | — |
| [**FrNm_GetVersionInfo**](../communication/flexray_network_management/index.md#7314-frnm_getversioninfo) | — |
| [**FrNm_Init**](../communication/flexray_network_management/index.md#731-frnm_init) | — |
| [**FrNm_NetworkRelease**](../communication/flexray_network_management/index.md#734-frnm_networkrelease) | — |
| [**FrNm_NetworkRequest**](../communication/flexray_network_management/index.md#733-frnm_networkrequest) | — |
| [**FrNm_PassiveStartUp**](../communication/flexray_network_management/index.md#732-frnm_passivestartup) | — |
| [**FrNm_PnLearningRequest**](../communication/flexray_network_management/index.md#7320-frnm_pnlearningrequest) | — |
| [**FrNm_RepeatMessageRequest**](../communication/flexray_network_management/index.md#738-frnm_repeatmessagerequest) | — |
| [**FrNm_RequestBusSynchronization**](../communication/flexray_network_management/index.md#7311-frnm_requestbussynchronization) | — |
| [**FrNm_RxIndication**](../communication/flexray_network_management/index.md#741-frnm_rxindication) | — |
| [**FrNm_SetSleepReadyBit**](../communication/flexray_network_management/index.md#7319-frnm_setsleepreadybit) | — |
| [**FrNm_SetUserData**](../communication/flexray_network_management/index.md#735-frnm_setuserdata) | — |
| [**FrNm_StartupError**](../communication/flexray_network_management/index.md#7315-frnm_startuperror) | — |
| [**FrNm_Transmit**](../communication/flexray_network_management/index.md#7316-frnm_transmit) | — |
| [**FrNm_TriggerTransmit**](../communication/flexray_network_management/index.md#742-frnm_triggertransmit) | — |
| [**FrNm_TxConfirmation**](../communication/flexray_network_management/index.md#743-frnm_txconfirmation) | — |
| [**NetworkStartIndication**](../communication/flexray_network_management/index.md#7631-networkstartindication) | — |
| [**PduRxIndication**](../communication/flexray_network_management/index.md#7632-pdurxindication) | — |
| [**RemoteSleepCancellation**](../communication/flexray_network_management/index.md#7633-remotesleepcancellation) | — |
| [**RemoteSleepIndication**](../communication/flexray_network_management/index.md#7634-remotesleepindication) | — |
| [**TransmissionTimeoutException**](../communication/flexray_network_management/index.md#7635-transmissiontimeoutexception) | — |

## AUTOSAR FlsTst（闪存测试驱动程序）（15）

来源：[AUTOSAR FlsTst（闪存测试驱动程序）](../memory/flstst/index.md) · SWS_FlashTest

| 函数 | 简述 |
|---|---|
| [**FlsTst_Abort**](../memory/flstst/index.md#734-flstst_abort) | 服务 ID 0x03。 |
| [**FlsTst_DeInit**](../memory/flstst/index.md#732-flstst_deinit) | 服务 ID 0x01。 |
| [**FlsTst_GetCurrentState**](../memory/flstst/index.md#737-flstst_getcurrentstate) | 服务 ID 0x06。 |
| [**FlsTst_GetErrorDetails**](../memory/flstst/index.md#7313-flstst_geterrordetails) | 服务 ID 0x0b。 |
| [**FlsTst_GetTestResultBgnd**](../memory/flstst/index.md#738-flstst_gettestresultbgnd) | 服务 ID 0x07。 |
| [**FlsTst_GetTestResultFgnd**](../memory/flstst/index.md#739-flstst_gettestresultfgnd) | 服务 ID 0x0f。 |
| [**FlsTst_GetTestSignatureBgnd**](../memory/flstst/index.md#7311-flstst_gettestsignaturebgnd) | 服务 ID 0x09。 |
| [**FlsTst_GetTestSignatureFgnd**](../memory/flstst/index.md#7312-flstst_gettestsignaturefgnd) | 服务 ID 0x0a。 |
| [**FlsTst_GetVersionInfo**](../memory/flstst/index.md#7310-flstst_getversioninfo) | 服务 ID 0x08。 |
| [**FlsTst_Init**](../memory/flstst/index.md#731-flstst_init) | 服务 ID 0x00。 |
| [**FlsTst_MainFunction**](../memory/flstst/index.md#751-flstst_mainfunction) | 服务 ID 0x0d。 |
| [**FlsTst_Resume**](../memory/flstst/index.md#736-flstst_resume) | 服务 ID 0x05。 |
| [**FlsTst_StartFgnd**](../memory/flstst/index.md#733-flstst_startfgnd) | 服务 ID 0x02。 |
| [**FlsTst_Suspend**](../memory/flstst/index.md#735-flstst_suspend) | 服务 ID 0x04。 |
| [**FlsTst_TestEcc**](../memory/flstst/index.md#7314-flstst_testecc) | 服务 ID 0x0c。 |

## AUTOSAR FLS（闪存驱动程序）（14）

来源：[AUTOSAR FLS（闪存驱动程序）](../memory/flash_driver/index.md) · SWS_FlashDriver

| 函数 | 简述 |
|---|---|
| [**Fee_JobEndNotification**](../memory/flash_driver/index.md#7631-fee_jobendnotification) | 当作业已以肯定结果完成时调用此回调函数。 |
| [**Fee_JobErrorNotification**](../memory/flash_driver/index.md#7632-fee_joberrornotification) | 当作业已被取消或以否定结果完成时调用此回调函数。 |
| [**Fls_BlankCheck**](../memory/flash_driver/index.md#7311-fls_blankcheck) | 服务 ID 0x0a。 |
| [**Fls_Cancel**](../memory/flash_driver/index.md#734-fls_cancel) | 服务 ID 0x03。 |
| [**Fls_Compare**](../memory/flash_driver/index.md#738-fls_compare) | 服务 ID 0x08。 |
| [**Fls_Erase**](../memory/flash_driver/index.md#732-fls_erase) | 服务 ID 0x01。 |
| [**Fls_GetJobResult**](../memory/flash_driver/index.md#736-fls_getjobresult) | 服务 ID 0x05。 |
| [**Fls_GetStatus**](../memory/flash_driver/index.md#735-fls_getstatus) | 服务 ID 0x04。 |
| [**Fls_GetVersionInfo**](../memory/flash_driver/index.md#7310-fls_getversioninfo) | 服务 ID 0x10。 |
| [**Fls_Init**](../memory/flash_driver/index.md#731-fls_init) | 服务 ID 0x00。 |
| [**Fls_MainFunction**](../memory/flash_driver/index.md#751-fls_mainfunction) | 服务 ID 0x06。 |
| [**Fls_Read**](../memory/flash_driver/index.md#737-fls_read) | 服务 ID 0x07。 |
| [**Fls_SetMode**](../memory/flash_driver/index.md#739-fls_setmode) | 服务 ID 0x09。 |
| [**Fls_Write**](../memory/flash_driver/index.md#733-fls_write) | 服务 ID 0x02。 |

## AUTOSAR GPT Driver（通用定时器驱动）（14）

来源：[AUTOSAR GPT Driver（通用定时器驱动）](../mcal/gpt_driver/index.md) · SWS_GPTDriver

| 函数 | 简述 |
|---|---|
| [**Gpt_CheckWakeup**](../mcal/gpt_driver/index.md#7313-gpt_checkwakeup) | 检查一个具备唤醒能力的GPT通道是否为唤醒事件的源，并在有效的GPT通道唤醒事件情况下调用ECU状态管理器服务 EcuM_SetWakeupEvent。 |
| [**Gpt_DeInit**](../mcal/gpt_driver/index.md#733-gpt_deinit) | 去初始化GPT驱动程序。 |
| [**Gpt_DisableNotification**](../mcal/gpt_driver/index.md#739-gpt_disablenotification) | 禁用一个通道的中断通知（在正常模式下相关）。 |
| [**Gpt_DisableWakeup**](../mcal/gpt_driver/index.md#7311-gpt_disablewakeup) | 禁用一个通道的唤醒中断（在睡眠模式下相关）。 |
| [**Gpt_EnableNotification**](../mcal/gpt_driver/index.md#738-gpt_enablenotification) | 启用一个通道的中断通知（在正常模式下相关）。 |
| [**Gpt_EnableWakeup**](../mcal/gpt_driver/index.md#7312-gpt_enablewakeup) | 启用一个通道的唤醒中断（在睡眠模式下相关）。 |
| [**Gpt_GetPredefTimerValue**](../mcal/gpt_driver/index.md#7314-gpt_getpredeftimervalue) | 提供所需GPT Predef Timer的当前值。 |
| [**Gpt_GetTimeElapsed**](../mcal/gpt_driver/index.md#734-gpt_gettimeelapsed) | 返回已流逝的时间。 |
| [**Gpt_GetTimeRemaining**](../mcal/gpt_driver/index.md#735-gpt_gettimeremaining) | 返回到达目标时间之前的剩余时间。 |
| [**Gpt_GetVersionInfo**](../mcal/gpt_driver/index.md#731-gpt_getversioninfo) | 返回本模块的版本信息。 |
| [**Gpt_Init**](../mcal/gpt_driver/index.md#732-gpt_init) | 初始化GPT驱动程序。 |
| [**Gpt_SetMode**](../mcal/gpt_driver/index.md#7310-gpt_setmode) | 设置GPT的运行模式。 |
| [**Gpt_StartTimer**](../mcal/gpt_driver/index.md#736-gpt_starttimer) | 启动一个定时器通道。 |
| [**Gpt_StopTimer**](../mcal/gpt_driver/index.md#737-gpt_stoptimer) | 停止一个定时器通道。 |

## AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）（1）

来源：[AUTOSAR I/O Hardware Abstraction（I/O 硬件抽象）](../io/iohwab/index.md) · SWS_IOHardwareAbstraction

| 函数 | 简述 |
|---|---|
| [**IoHwAb_GetVersionInfo**](../io/iohwab/index.md#732-iohwab_getversioninfo) | 返回此模块的版本信息。 |

## AUTOSAR ICU Driver（输入捕获驱动）（26）

来源：[AUTOSAR ICU Driver（输入捕获驱动）](../io/icu_driver/index.md) · SWS_ICUDriver

| 函数 | 简述 |
|---|---|
| [**Icu_CheckWakeup**](../io/icu_driver/index.md#736-icu_checkwakeup) | 检查某个唤醒能力ICU通道是否为唤醒事件的源，若为有效的ICU通道唤醒事件，则调用ECU状态管理器服务EcuM_SetWakeupEvent。 |
| [**Icu_DeInit**](../io/icu_driver/index.md#732-icu_deinit) | 将ICU模块去初始化：把配置使用的外设状态设置为与上电复位后相同（只读寄存器除外），仅影响静态配置和/或上次Icu_Init()传入的运行时配置所分配的外设；禁用所有已用中断和通知。 |
| [**Icu_DisableEdgeCount**](../io/icu_driver/index.md#7318-icu_disableedgecount) | 禁用给定通道的边沿计数（复位边沿计数器请使用服务Icu_ResetEdgeCount()）。 |
| [**Icu_DisableEdgeDetection**](../io/icu_driver/index.md#7317-icu_disableedgedetection) | 禁用给定通道的边沿检测。 |
| [**Icu_DisableNotification**](../io/icu_driver/index.md#738-icu_disablenotification) | 禁用给定通道的通知。 |
| [**Icu_DisableNotificationAsync**](../io/icu_driver/index.md#7325-icu_disablenotificationasync) | 禁用给定通道的通知。 |
| [**Icu_DisableWakeup**](../io/icu_driver/index.md#734-icu_disablewakeup) | 禁用单个ICU通道的唤醒能力，仅对静态配置为唤醒能力（wakeup capable）为真的通道有效。 |
| [**Icu_EnableEdgeCount**](../io/icu_driver/index.md#7315-icu_enableedgecount) | 使能给定通道的边沿计数（本服务自身不做实际计数），仅计数配置的边沿（上升/下降/双边沿，即Icu_Init()后的默认边沿或Icu_SetActivationCondition()设置的边沿）。 |
| [**Icu_EnableEdgeDetection**](../io/icu_driver/index.md#7316-icu_enableedgedetection) | 使能/重新使能给定通道的边沿检测，仅检测配置的边沿（上升/下降/双边沿）。 |
| [**Icu_EnableNotification**](../io/icu_driver/index.md#739-icu_enablenotification) | 使能给定通道的通知。 |
| [**Icu_EnableNotificationAsync**](../io/icu_driver/index.md#7326-icu_enablenotificationasync) | 使能给定通道的通知。 |
| [**Icu_EnableWakeup**](../io/icu_driver/index.md#735-icu_enablewakeup) | 重新使能给定ICU通道的唤醒能力，仅对静态配置为唤醒能力为真的通道可行；需再调用请求ICU_MODE_SLEEP的Icu_SetMode方使选择生效。 |
| [**Icu_GetDutyCycleValues**](../io/icu_driver/index.md#7323-icu_getdutycyclevalues) | 为给定ICU通道读取一致的有效时间与周期时间（配置为"Signal Measurement, Duty Cycle Values"测量模式时），结果（高电平时间与周期时间）写入DutyCycleValues指向的缓冲区。 |
| [**Icu_GetEdgeNumbers**](../io/icu_driver/index.md#7319-icu_getedgenumbers) | 读取自上次调用Icu_ResetEdgeCount()以来计得的边沿数量。 |
| [**Icu_GetInputState**](../io/icu_driver/index.md#7310-icu_getinputstate) | 返回ICU输入的状态。 |
| [**Icu_GetTimeElapsed**](../io/icu_driver/index.md#7322-icu_gettimeelapsed) | 读取给定通道经过的时间，具体取决于通道所配置的测量模式与测量属性：低电平时间（下降沿与相邻上升沿之间）、高电平时间（上升沿与相邻下降沿之间）或周期时间（相邻上升沿或下降沿之间，周期起始边沿可配置）。 |
| [**Icu_GetTimestampIndex**](../io/icu_driver/index.md#7313-icu_gettimestampindex) | 读取给定通道的时间戳索引，即下一个待写入位置的索引。 |
| [**Icu_GetVersionInfo**](../io/icu_driver/index.md#7324-icu_getversioninfo) | 返回本模块的版本信息（写入versioninfo指向的位置）。 |
| [**Icu_Init**](../io/icu_driver/index.md#731-icu_init) | 初始化驱动。 |
| [**Icu_ResetEdgeCount**](../io/icu_driver/index.md#7314-icu_resetedgecount) | 将计得的边沿数值复位为零。 |
| [**Icu_SetActivationCondition**](../io/icu_driver/index.md#737-icu_setactivationcondition) | 为给定通道设置激活边沿（ICU_RISING_EDGE/ICU_FALLING_EDGE/ICU_BOTH_EDGES，若硬件支持），支持配置为ICU_MODE_SIGNAL_EDGE_DETECT、ICU_MODE_TIMESTAM… |
| [**Icu_SetMode**](../io/icu_driver/index.md#733-icu_setmode) | 将ICU模块设置为给定模式（ICU_MODE_NORMAL或ICU_MODE_SLEEP），影响各ICU通道的功能，因此模块模式切换必须与ECU整体状态兼容。 |
| [**Icu_StartSignalMeasurement**](../io/icu_driver/index.md#7320-icu_startsignalmeasurement) | 从调用本服务后最先出现的配置默认起始边沿开始，启动信号测量，并将给定通道状态复位为ICU_IDLE。 |
| [**Icu_StartTimestamp**](../io/icu_driver/index.md#7311-icu_starttimestamp) | 从缓冲区起始处开始在边沿上捕获定时器值到外部缓冲区。 |
| [**Icu_StopSignalMeasurement**](../io/icu_driver/index.md#7321-icu_stopsignalmeasurement) | 停止给定通道的信号测量。 |
| [**Icu_StopTimestamp**](../io/icu_driver/index.md#7312-icu_stoptimestamp) | 停止给定通道的时间戳测量。 |

## AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）（11）

来源：[AUTOSAR IEEE1722Tp（IEEE 1722 传输协议）](../communication/ieee1722tp/index.md) · SWS_IEEE1722TransportLayer

| 函数 | 简述 |
|---|---|
| [**IEEE1722Tp_ActivateStream**](../communication/ieee1722tp/index.md#7421-ieee1722tp_activatestream) | — |
| [**IEEE1722Tp_DeactivateStream**](../communication/ieee1722tp/index.md#7422-ieee1722tp_deactivatestream) | — |
| [**IEEE1722Tp_DeInit**](../communication/ieee1722tp/index.md#7412-ieee1722tp_deinit) | — |
| [**IEEE1722Tp_GetVersionInfo**](../communication/ieee1722tp/index.md#7413-ieee1722tp_getversioninfo) | — |
| [**IEEE1722Tp_Init**](../communication/ieee1722tp/index.md#7411-ieee1722tp_init) | — |
| [**IEEE1722Tp_MainFunctionRx**](../communication/ieee1722tp/index.md#762-ieee1722tp_mainfunctionrx) | — |
| [**IEEE1722Tp_MainFunctionTx**](../communication/ieee1722tp/index.md#761-ieee1722tp_mainfunctiontx) | — |
| [**IEEE1722Tp_ReleaseRxBuffer**](../communication/ieee1722tp/index.md#7432-ieee1722tp_releaserxbuffer) | — |
| [**IEEE1722Tp_RxIndication**](../communication/ieee1722tp/index.md#752-ieee1722tp_rxindication) | — |
| [**IEEE1722Tp_Transmit**](../communication/ieee1722tp/index.md#7431-ieee1722tp_transmit) | — |
| [**IEEE1722Tp_TxConfirmation**](../communication/ieee1722tp/index.md#751-ieee1722tp_txconfirmation) | — |

## AUTOSAR J1939Nm（SAE J1939 网络管理）（12）

来源：[AUTOSAR J1939Nm（SAE J1939 网络管理）](../communication/j1939nm/index.md) · SWS_SAEJ1939NetworkManagement

| 函数 | 简述 |
|---|---|
| [**J1939Nm_DeInit**](../communication/j1939nm/index.md#742-j1939nm_deinit) | — |
| [**J1939Nm_GetBusOffDelay**](../communication/j1939nm/index.md#747-j1939nm_getbusoffdelay) | — |
| [**J1939Nm_GetState**](../communication/j1939nm/index.md#746-j1939nm_getstate) | — |
| [**J1939Nm_GetVersionInfo**](../communication/j1939nm/index.md#743-j1939nm_getversioninfo) | — |
| [**J1939Nm_Init**](../communication/j1939nm/index.md#741-j1939nm_init) | — |
| [**J1939Nm_MainFunction**](../communication/j1939nm/index.md#761-j1939nm_mainfunction) | — |
| [**J1939Nm_NetworkRelease**](../communication/j1939nm/index.md#745-j1939nm_networkrelease) | — |
| [**J1939Nm_NetworkRequest**](../communication/j1939nm/index.md#744-j1939nm_networkrequest) | — |
| [**J1939Nm_PassiveStartUp**](../communication/j1939nm/index.md#748-j1939nm_passivestartup) | — |
| [**J1939Nm_RequestIndication**](../communication/j1939nm/index.md#753-j1939nm_requestindication) | — |
| [**J1939Nm_RxIndication**](../communication/j1939nm/index.md#751-j1939nm_rxindication) | — |
| [**J1939Nm_TxConfirmation**](../communication/j1939nm/index.md#752-j1939nm_txconfirmation) | — |

## AUTOSAR J1939Rm（SAE J1939 请求管理器）（20）

来源：[AUTOSAR J1939Rm（SAE J1939 请求管理器）](../communication/j1939rm/index.md) · SWS_SAEJ1939RequestManager

| 函数 | 简述 |
|---|---|
| [**AppAckIndication**](../communication/j1939rm/index.md#7834-appackindication) | — |
| [**AppCancelRequestTimeout**](../communication/j1939rm/index.md#7833-appcancelrequesttimeout) | — |
| [**AppRequestIndication**](../communication/j1939rm/index.md#7835-apprequestindication) | — |
| [**AppRequestTimeoutIndication**](../communication/j1939rm/index.md#7836-apprequesttimeoutindication) | — |
| [**AppSendAck**](../communication/j1939rm/index.md#7831-appsendack) | — |
| [**AppSendRequest**](../communication/j1939rm/index.md#7832-appsendrequest) | — |
| [**J1939Rm_AckIndication**](../communication/j1939rm/index.md#7821-j1939rm_ackindication) | — |
| [**J1939Rm_CancelRequestTimeout**](../communication/j1939rm/index.md#746-j1939rm_cancelrequesttimeout) | — |
| [**J1939Rm_CheckReceivedComIPdu**](../communication/j1939rm/index.md#753-j1939rm_checkreceivedcomipdu) | — |
| [**J1939Rm_DeInit**](../communication/j1939rm/index.md#742-j1939rm_deinit) | — |
| [**J1939Rm_GetVersionInfo**](../communication/j1939rm/index.md#743-j1939rm_getversioninfo) | — |
| [**J1939Rm_Init**](../communication/j1939rm/index.md#741-j1939rm_init) | — |
| [**J1939Rm_MainFunction**](../communication/j1939rm/index.md#761-j1939rm_mainfunction) | — |
| [**J1939Rm_RequestIndication**](../communication/j1939rm/index.md#7822-j1939rm_requestindication) | — |
| [**J1939Rm_RequestTimeoutIndication**](../communication/j1939rm/index.md#7823-j1939rm_requesttimeoutindication) | — |
| [**J1939Rm_RxIndication**](../communication/j1939rm/index.md#751-j1939rm_rxindication) | — |
| [**J1939Rm_SendAck**](../communication/j1939rm/index.md#747-j1939rm_sendack) | — |
| [**J1939Rm_SendRequest**](../communication/j1939rm/index.md#745-j1939rm_sendrequest) | — |
| [**J1939Rm_SetState**](../communication/j1939rm/index.md#744-j1939rm_setstate) | — |
| [**J1939Rm_TxConfirmation**](../communication/j1939rm/index.md#752-j1939rm_txconfirmation) | — |

## AUTOSAR J1939Tp（SAE J1939 传输层）（10）

来源：[AUTOSAR J1939Tp（SAE J1939 传输层）](../communication/j1939tp/index.md) · SWS_SAEJ1939TransportLayer

| 函数 | 简述 |
|---|---|
| [**J1939Tp_CancelReceive**](../communication/j1939tp/index.md#746-j1939tp_cancelreceive) | — |
| [**J1939Tp_CancelTransmit**](../communication/j1939tp/index.md#745-j1939tp_canceltransmit) | — |
| [**J1939Tp_ChangeParameter**](../communication/j1939tp/index.md#747-j1939tp_changeparameter) | — |
| [**J1939Tp_GetVersionInfo**](../communication/j1939tp/index.md#743-j1939tp_getversioninfo) | — |
| [**J1939Tp_Init**](../communication/j1939tp/index.md#741-j1939tp_init) | — |
| [**J1939Tp_MainFunction**](../communication/j1939tp/index.md#761-j1939tp_mainfunction) | — |
| [**J1939Tp_RxIndication**](../communication/j1939tp/index.md#751-j1939tp_rxindication) | — |
| [**J1939Tp_Shutdown**](../communication/j1939tp/index.md#742-j1939tp_shutdown) | — |
| [**J1939Tp_Transmit**](../communication/j1939tp/index.md#744-j1939tp_transmit) | — |
| [**J1939Tp_TxConfirmation**](../communication/j1939tp/index.md#752-j1939tp_txconfirmation) | — |

## AUTOSAR Key Manager（密钥管理器）（41）

来源：[AUTOSAR Key Manager（密钥管理器）](../crypto/key_manager/index.md) · SWS_KeyManager

| 函数 | 简述 |
|---|---|
| [**KeyM_CertElementGet**](../crypto/key_manager/index.md#7337-keym_certelementget) | 提供特定证书元素的内容。 |
| [**KeyM_CertElementGetByIndex**](../crypto/key_manager/index.md#7338-keym_certelementgetbyindex) | 本函数提供证书的元素数据。 |
| [**KeyM_CertElementGetCount**](../crypto/key_manager/index.md#7339-keym_certelementgetcount) | 本函数提供指定证书元素可用的数据元素总数。 |
| [**KeyM_CertElementGetFirst**](../crypto/key_manager/index.md#73310-keym_certelementgetfirst) | 本函数用于初始化证书数据元素的迭代式提取。 |
| [**KeyM_CertElementGetNext**](../crypto/key_manager/index.md#73311-keym_certelementgetnext) | 本函数提供证书元素的后续数据，例如当一组数据位于一个证书元素中且需要依次读取时。 |
| [**KeyM_CertGetStatus**](../crypto/key_manager/index.md#73312-keym_certgetstatus) | 本函数提供证书的状态。 |
| [**KeyM_Certificate**](../crypto/key_manager/index.md#7831-keym_certificate) | — |
| [**KeyM_CertificateVerifyCallbackNotification**](../crypto/key_manager/index.md#77311-keym_certificateverifycallbacknotification) | 通知应用程序证书验证已经完成。 |
| [**KeyM_CryptoKeyFinalizeCallbackNotification**](../crypto/key_manager/index.md#7738-keym_cryptokeyfinalizecallbacknotification) | 通知应用程序加密密钥最终处理操作已经完成。 |
| [**KeyM_CryptoKeyUpdateCallbackNotification**](../crypto/key_manager/index.md#7737-keym_cryptokeyupdatecallbacknotification) | 通知应用程序加密密钥更新操作已经完成。 |
| [**KeyM_CryptoKeyVerifyCallbackNotification**](../crypto/key_manager/index.md#7739-keym_cryptokeyverifycallbacknotification) | 通知应用程序加密密钥验证操作已经完成。 |
| [**KeyM_Deinit**](../crypto/key_manager/index.md#7312-keym_deinit) | 此函数将密钥管理模块重置为未初始化状态。 |
| [**KeyM_Finalize**](../crypto/key_manager/index.md#7324-keym_finalize) | 此函数用于最终完成密钥更新操作。 |
| [**KeyM_GetCertificate**](../crypto/key_manager/index.md#7333-keym_getcertificate) | 本函数提供 DER 编码的证书数据。 |
| [**KeyM_GetVersionInfo**](../crypto/key_manager/index.md#7313-keym_getversioninfo) | 提供本模块的版本信息。 |
| [**KeyM_Init**](../crypto/key_manager/index.md#7311-keym_init) | 此函数初始化密钥管理模块。 |
| [**KeyM_KH_Finalize**](../crypto/key_manager/index.md#7734-keym_kh_finalize) | 如果 KeyMCryptoKeyStartFinalizeFunctionEnabled 和 KeyMCryptoKeyHandlerStartFinalizeEnabled 设置为 TRUE，本函数将在 KeyM_Finalize … |
| [**KeyM_KH_Prepare**](../crypto/key_manager/index.md#7732-keym_kh_prepare) | 如果配置参数 KeyMCryptoKeyPrepareFunctionEnabled 和 KeyMCryptoKeyHandlerPrepareEnabled 均设置为 TRUE，则本函数将在 KeyM_Prepare 被调用时立即被调用。 |
| [**KeyM_KH_ServiceCertificate**](../crypto/key_manager/index.md#7736-keym_kh_servicecertificate) | 如果 KeyMCryptoKeyHandlerServiceCertificateEnabled 设置为 TRUE，KeyM_ServiceCertificate() 将调用本函数，把操作委托给这个用户特定的服务函数。 |
| [**KeyM_KH_Start**](../crypto/key_manager/index.md#7731-keym_kh_start) | 如果 KeyMCryptoKeyStartFinalizeFunctionEnabled 和 KeyMCryptoKeyHandlerStartFinalizeEnabled 设置为 TRUE，本函数将在 KeyM_Start 被调用… |
| [**KeyM_KH_Update**](../crypto/key_manager/index.md#7733-keym_kh_update) | 如果配置项 KeyMCryptoKeyHandlerUpdateEnabled 设置为 TRUE，KeyM_Update 函数将不执行任何操作，而是把该操作委托给密钥处理程序。 |
| [**KeyM_KH_Verify**](../crypto/key_manager/index.md#7735-keym_kh_verify) | 如果 KeyMCryptoKeyHandlerVerifyEnabled 设置为 TRUE，KeyM_Verify 函数将不执行任何操作，而是把其操作委托给此服务回调。 |
| [**KeyM_MainBackgroudFunction**](../crypto/key_manager/index.md#762-keym_mainbackgroudfunction) | 本函数在不需要执行其他任务操作时由可抢占操作系统调用。 |
| [**KeyM_MainFunction**](../crypto/key_manager/index.md#761-keym_mainfunction) | 本函数按照指定的时间间隔被周期性调用。 |
| [**KeyM_Prepare**](../crypto/key_manager/index.md#7322-keym_prepare) | 此函数用于准备一次密钥更新操作。 |
| [**KeyM_ServiceCertificate**](../crypto/key_manager/index.md#7331-keym_servicecertificate) | 密钥服务器向密钥客户端请求一个操作。 |
| [**KeyM_ServiceCertificateCallbackNotification**](../crypto/key_manager/index.md#77310-keym_servicecertificatecallbacknotification) | 通知应用程序证书服务操作已经完成。 |
| [**KeyM_SetCertificate**](../crypto/key_manager/index.md#7332-keym_setcertificate) | 本函数向密钥管理模块提供证书数据，以临时存储该证书。 |
| [**KeyM_Start**](../crypto/key_manager/index.md#7321-keym_start) | 此函数为可选函数，仅在配置项 KeyMCryptoKeyStartFinalizeFunctionEnabled 设置为 true 时使用，其意图是允许密钥更新操作。 |
| [**KeyM_Update**](../crypto/key_manager/index.md#7323-keym_update) | 此函数用于发起密钥生成或更新过程。 |
| [**KeyM_Verify**](../crypto/key_manager/index.md#7325-keym_verify) | 密钥服务器请求验证所提供的密钥。 |
| [**KeyM_VerifyCertificate**](../crypto/key_manager/index.md#7335-keym_verifycertificate) | 本函数将先前通过 KeyM_SetCertificate() 提供的证书，与已用其他证书 ID 存储的证书进行相互验证。 |
| [**KeyM_VerifyCertificateChain**](../crypto/key_manager/index.md#7336-keym_verifycertificatechain) | 本函数针对一个证书列表执行证书验证。 |
| [**KeyM_VerifyCertificates**](../crypto/key_manager/index.md#7334-keym_verifycertificates) | 本函数对两个已在内部存储并解析的证书进行相互验证。 |
| [**KeyMCertificateElement**](../crypto/key_manager/index.md#7832-keymcertificateelement) | — |
| [**KeyMCryptoKey**](../crypto/key_manager/index.md#7833-keymcryptokey) | — |
| [**KeyMCryptoKeyNotification**](../crypto/key_manager/index.md#7838-keymcryptokeynotification) | — |
| [**KeyMServiceCertificate**](../crypto/key_manager/index.md#7835-keymservicecertificate) | — |
| [**KeyMServiceCertificateNotification**](../crypto/key_manager/index.md#7837-keymservicecertificatenotification) | — |
| [**KeyMServiceCertificatetByCertId**](../crypto/key_manager/index.md#7836-keymservicecertificatetbycertid) | — |
| [**KeyMVerifyCertificateNotification**](../crypto/key_manager/index.md#7834-keymverifycertificatenotification) | — |

## AUTOSAR L-SDU Router（链路层 SDU 路由模块）（3）

来源：[AUTOSAR L-SDU Router（链路层 SDU 路由模块）](../communication/lsdu_router/index.md) · SWS_LSduRouter

| 函数 | 简述 |
|---|---|
| [**LSduR_GetConfigurationId**](../communication/lsdu_router/index.md#7313-lsdur_getconfigurationid) | 返回 L-SDU Router 的 post-build 时配置的唯一标识符。 |
| [**LSduR_GetVersionInfo**](../communication/lsdu_router/index.md#7312-lsdur_getversioninfo) | 返回本模块的版本信息。 |
| [**LSduR_Init**](../communication/lsdu_router/index.md#7311-lsdur_init) | 初始化 L-SDU Router。 |

## AUTOSAR Large Data COM（大数据 COM）（21）

来源：[AUTOSAR Large Data COM（大数据 COM）](../communication/large_data_com/index.md) · SWS_LargeDataCOM

| 函数 | 简述 |
|---|---|
| [**LdCom_CopyRxData**](../communication/large_data_com/index.md#744-ldcom_copyrxdata) | 调用此函数以将 I-PDU 段（N-PDU）的接收数据提供给上层。 |
| [**LdCom_CopyTxData**](../communication/large_data_com/index.md#741-ldcom_copytxdata) | 调用此函数以获取 I-PDU 段（N-PDU）的发送数据。 |
| [**LdCom_DeInit**](../communication/large_data_com/index.md#732-ldcom_deinit) | 调用 LdCom_DeInit 后，AUTOSAR LdCom 模块被置于未初始化状态。 |
| [**LdCom_GetVersionInfo**](../communication/large_data_com/index.md#733-ldcom_getversioninfo) | 返回本模块的版本信息。 |
| [**LdCom_Init**](../communication/large_data_com/index.md#731-ldcom_init) | 此服务初始化 AUTOSAR LdCom 模块的内部和外部接口与变量，以进行后续处理。 |
| [**LdCom_RxIndication**](../communication/large_data_com/index.md#746-ldcom_rxindication) | 来自下层通信接口模块的已接收 PDU 的指示。 |
| [**LdCom_StartOfReception**](../communication/large_data_com/index.md#743-ldcom_startofreception) | 在开始接收一个 N-SDU 时调用此函数。 |
| [**LdCom_TpRxIndication**](../communication/large_data_com/index.md#745-ldcom_tprxindication) | 在通过 TP API 接收到一个 I-PDU 之后调用此函数，result 指示接收是否成功。 |
| [**LdCom_TpTxConfirmation**](../communication/large_data_com/index.md#742-ldcom_tptxconfirmation) | 在 I-PDU 已于其网络上发送之后调用此函数，result 指示传输是否成功。 |
| [**LdCom_Transmit**](../communication/large_data_com/index.md#734-ldcom_transmit) | 请求传输一个信号。 |
| [**LdCom_TriggerTransmit**](../communication/large_data_com/index.md#748-ldcom_triggertransmit) | 在此 API 内，上层模块（被调用模块）应检查可用数据是否适合 PduInfoPtr->SduLength 报告的缓冲区大小。 |
| [**LdCom_TxConfirmation**](../communication/large_data_com/index.md#747-ldcom_txconfirmation) | 下层通信接口模块确认一个 PDU 的传输，或传输失败。 |
| [**LdComCbkCopyRxData**](../communication/large_data_com/index.md#7634-ldcomcbkcopyrxdata) | 调用此函数以将 I-PDU 段（N-PDU）的接收数据提供给上层。 |
| [**LdComCbkCopyTxData**](../communication/large_data_com/index.md#7631-ldcomcbkcopytxdata) | 调用此函数以获取 I-PDU 段（N-PDU）的发送数据。 |
| [**LdComCbkRxIndication**](../communication/large_data_com/index.md#7636-ldcomcbkrxindication) | 来自下层通信接口模块的已接收 PDU 的指示。 |
| [**LdComCbkStartOfReception**](../communication/large_data_com/index.md#7633-ldcomcbkstartofreception) | 在开始接收一个 N-SDU 时调用此函数。 |
| [**LdComCbkTpRxIndication**](../communication/large_data_com/index.md#7635-ldcomcbktprxindication) | 在通过 TP API 接收到一个 I-PDU 之后调用此函数，result 指示接收是否成功。 |
| [**LdComCbkTpTxConfirmation**](../communication/large_data_com/index.md#7632-ldcomcbktptxconfirmation) | 在一个信号已通过 TP-API 于其网络上发送之后调用此函数。 |
| [**LdComCbkTriggerTransmit**](../communication/large_data_com/index.md#7637-ldcomcbktriggertransmit) | 在此 API 内，上层模块（被调用模块）应检查可用数据是否适合 PduInfoPtr->SduLength 报告的缓冲区大小。 |
| [**LdComCbkTxConfirmation**](../communication/large_data_com/index.md#7638-ldcomcbktxconfirmation) | 下层通信接口模块确认一个 PDU 的传输，或传输失败。 |
| [**TriggerTransmit**](../communication/large_data_com/index.md#813-triggertransmit) | — |

## AUTOSAR LIN Driver（9）

来源：[AUTOSAR LIN Driver](../communication/lin_driver/index.md) · SWS_LINDriver

| 函数 | 简述 |
|---|---|
| [**Lin_CheckWakeup**](../communication/lin_driver/index.md#712-lin_checkwakeup) | 这个函数检查在指定的LIN通道上是否发生了唤醒。 |
| [**Lin_GetStatus**](../communication/lin_driver/index.md#719-lin_getstatus) | 获取LIN驱动程序的状态。 |
| [**Lin_GetVersionInfo**](../communication/lin_driver/index.md#713-lin_getversioninfo) | 返回此模块的版本信息。 |
| [**Lin_GoToSleep**](../communication/lin_driver/index.md#715-lin_gotosleep) | 该服务指示驱动程序在指定的LIN通道上发送一个“进入休眠”命令。 |
| [**Lin_GoToSleepInternal**](../communication/lin_driver/index.md#716-lin_gotosleepinternal) | 将通道状态设置为LIN_CH_SLEEP，启用唤醒检测，并可选择将LIN硬件单元设置为降低功耗的运行模式（如果HW支持）。 |
| [**Lin_Init**](../communication/lin_driver/index.md#711-lin_init) | 初始化LIN模块。 |
| [**Lin_SendFrame**](../communication/lin_driver/index.md#714-lin_sendframe) | 如果需要发送LIN报头和LIN响应。 |
| [**Lin_Wakeup**](../communication/lin_driver/index.md#717-lin_wakeup) | 生成一个唤醒脉冲并将通道状态设置为LIN_CH_OPERATIONAL。 |
| [**LIN_WakeupInternal**](../communication/lin_driver/index.md#718-lin_wakeupinternal) | 将通道状态设置为LIN_CH_OPERATIONAL，而不产生唤醒脉冲。 |

## AUTOSAR LinIf (LIN Interface)（26）

来源：[AUTOSAR LinIf (LIN Interface)](../communication/lin_interface/index.md) · SWS_LINInterface

| 函数 | 简述 |
|---|---|
| [**LinIf_CheckWakeup**](../communication/lin_interface/index.md#7320-linif_checkwakeup) | 当 EcuM 已被通知某个特定 LIN 通道上有唤醒时，将调用此函数。 |
| [**LinIf_EnableBusMirroring**](../communication/lin_interface/index.md#7321-linif_enablebusmirroring) | 启用或禁用 LIN 通道的镜像。 |
| [**LinIf_GetConfiguredNAD**](../communication/lin_interface/index.md#7313-linif_getconfigurednad) | 报告当前已配置的 NAD。 |
| [**LinIf_GetPIDTable**](../communication/lin_interface/index.md#7311-linif_getpidtable) | 检索所有已分配的 PID 值。 |
| [**LinIf_GetTrcvMode**](../communication/lin_interface/index.md#738-linif_gettrcvmode) | 返回 LIN 收发器驱动程序的实际状态。 |
| [**LinIf_GetTrcvWakeupReason**](../communication/lin_interface/index.md#739-linif_gettrcvwakeupreason) | 返回 LIN 收发器驱动程序检测到的唤醒原因。 |
| [**LinIf_GetVersionInfo**](../communication/lin_interface/index.md#732-linif_getversioninfo) | 返回本模块的版本信息。 |
| [**LinIf_GotoSleep**](../communication/lin_interface/index.md#735-linif_gotosleep) | 在选定通道上发起向睡眠模式的迁移。 |
| [**LinIf_HeaderIndication**](../communication/lin_interface/index.md#742-linif_headerindication) | LIN 驱动程序将调用此函数以报告接收到的 LIN 报头。 |
| [**LinIf_Init**](../communication/lin_interface/index.md#731-linif_init) | 初始化 LIN 接口。 |
| [**LinIf_LinErrorIndication**](../communication/lin_interface/index.md#745-linif_linerrorindication) | LIN 驱动程序将调用此函数以报告在报头或响应处理期间检测到的错误事件。 |
| [**LinIf_RxIndication**](../communication/lin_interface/index.md#743-linif_rxindication) | LIN 驱动程序将调用此函数以报告成功接收的响应，并将接收数据提供给 LIN 接口。 |
| [**LinIf_ScheduleRequest**](../communication/lin_interface/index.md#734-linif_schedulerequest) | 请求执行一个调度表。 |
| [**LinIf_SetConfiguredNAD**](../communication/lin_interface/index.md#7314-linif_setconfigurednad) | 设置当前已配置的 NAD。 |
| [**LinIf_SetPIDTable**](../communication/lin_interface/index.md#7312-linif_setpidtable) | 设置所有已分配的 PID 值。 |
| [**LinIf_SetTrcvMode**](../communication/lin_interface/index.md#737-linif_settrcvmode) | 将给定的 LIN 收发器设置为给定的模式。 |
| [**LinIf_SetTrcvWakeupMode**](../communication/lin_interface/index.md#7310-linif_settrcvwakeupmode) | 此 API 启用、禁用和清除被寻址网络上唤醒事件的通知。 |
| [**LinIf_Transmit**](../communication/lin_interface/index.md#733-linif_transmit) | 请求发送一个 PDU。 |
| [**LinIf_TxConfirmation**](../communication/lin_interface/index.md#744-linif_txconfirmation) | 本服务为同步调用，对不同的 Channel 可重入，对相同的 Channel 不可重入。 |
| [**LinIf_Wakeup**](../communication/lin_interface/index.md#736-linif_wakeup) | 发起唤醒过程。 |
| [**LinIf_WakeupConfirmation**](../communication/lin_interface/index.md#741-linif_wakeupconfirmation) | 在 CheckWakeup 期间成功检测到唤醒后或总线通电后，LIN 驱动程序或 LIN 收发器驱动程序将调用此函数以报告唤醒源。 |
| [**LinTp_ChangeParameter**](../communication/lin_interface/index.md#7319-lintp_changeparameter) | 请求更改特定的传输协议参数（例如块大小）。 |
| [**LinTp_GetVersionInfo**](../communication/lin_interface/index.md#7317-lintp_getversioninfo) | 返回本模块的版本信息。 |
| [**LinTp_Init**](../communication/lin_interface/index.md#7315-lintp_init) | 初始化 LIN 传输层。 |
| [**LinTp_Shutdown**](../communication/lin_interface/index.md#7318-lintp_shutdown) | 关闭 LIN TP。 |
| [**LinTp_Transmit**](../communication/lin_interface/index.md#7316-lintp_transmit) | 请求发送一个 PDU。 |

## AUTOSAR LinSM（LIN 状态管理器）（10）

来源：[AUTOSAR LinSM（LIN 状态管理器）](../communication/linsm/index.md) · SWS_LINStateManager

| 函数 | 简述 |
|---|---|
| [**LinSM_GetCurrentComMode**](../communication/linsm/index.md#734-linsm_getcurrentcommode) | — |
| [**LinSM_GetVersionInfo**](../communication/linsm/index.md#733-linsm_getversioninfo) | — |
| [**LinSM_GotoSleepConfirmation**](../communication/linsm/index.md#753-linsm_gotosleepconfirmation) | — |
| [**LinSM_GotoSleepIndication**](../communication/linsm/index.md#752-linsm_gotosleepindication) | — |
| [**LinSM_Init**](../communication/linsm/index.md#731-linsm_init) | — |
| [**LinSM_MainFunction**](../communication/linsm/index.md#741-linsm_mainfunction) | — |
| [**LinSM_RequestComMode**](../communication/linsm/index.md#735-linsm_requestcommode) | — |
| [**LinSM_ScheduleRequest**](../communication/linsm/index.md#732-linsm_schedulerequest) | — |
| [**LinSM_ScheduleRequestConfirmation**](../communication/linsm/index.md#751-linsm_schedulerequestconfirmation) | — |
| [**LinSM_WakeupConfirmation**](../communication/linsm/index.md#754-linsm_wakeupconfirmation) | — |

## AUTOSAR LinTrcv（LIN 收发器驱动程序）（7）

来源：[AUTOSAR LinTrcv（LIN 收发器驱动程序）](../communication/lintrcv/index.md) · SWS_LINTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**LinTrcv_CheckWakeup**](../communication/lintrcv/index.md#736-lintrcv_checkwakeup) | — |
| [**LinTrcv_GetBusWuReason**](../communication/lintrcv/index.md#734-lintrcv_getbuswureason) | — |
| [**LinTrcv_GetOpMode**](../communication/lintrcv/index.md#733-lintrcv_getopmode) | — |
| [**LinTrcv_GetVersionInfo**](../communication/lintrcv/index.md#735-lintrcv_getversioninfo) | — |
| [**LinTrcv_Init**](../communication/lintrcv/index.md#731-lintrcv_init) | — |
| [**LinTrcv_SetOpMode**](../communication/lintrcv/index.md#732-lintrcv_setopmode) | — |
| [**LinTrcv_SetWakeupMode**](../communication/lintrcv/index.md#737-lintrcv_setwakeupmode) | — |

## AUTOSAR MCU Driver（微控制器单元驱动）（11）

来源：[AUTOSAR MCU Driver（微控制器单元驱动）](../mcal/mcu_driver/index.md) · SWS_MCUDriver

| 函数 | 简述 |
|---|---|
| [**Mcu_DistributePllClock**](../mcal/mcu_driver/index.md#734-mcu_distributepllclock) | 此服务将PLL时钟激活到MCU时钟分配。 |
| [**Mcu_GetPllStatus**](../mcal/mcu_driver/index.md#735-mcu_getpllstatus) | 此服务提供PLL的状态。 |
| [**Mcu_GetRamState**](../mcal/mcu_driver/index.md#7311-mcu_getramstate) | 此服务提供微控制器 RAM 的实际状态（如果支持）。 |
| [**Mcu_GetResetRawValue**](../mcal/mcu_driver/index.md#737-mcu_getresetrawvalue) | 此服务在硬件支持时从硬件寄存器读取复位的原始值。 |
| [**Mcu_GetResetReason**](../mcal/mcu_driver/index.md#736-mcu_getresetreason) | 此服务在硬件支持时从硬件读取复位类型。 |
| [**Mcu_GetVersionInfo**](../mcal/mcu_driver/index.md#7310-mcu_getversioninfo) | 此服务返回本模块的版本信息。 |
| [**Mcu_Init**](../mcal/mcu_driver/index.md#731-mcu_init) | 此服务初始化MCU驱动程序。 |
| [**Mcu_InitClock**](../mcal/mcu_driver/index.md#733-mcu_initclock) | 此服务初始化PLL和其他MCU特定的时钟选项。 |
| [**Mcu_InitRamSection**](../mcal/mcu_driver/index.md#732-mcu_initramsection) | 此服务按区段初始化 RAM。 |
| [**Mcu_PerformReset**](../mcal/mcu_driver/index.md#738-mcu_performreset) | 此服务执行微控制器复位。 |
| [**Mcu_SetMode**](../mcal/mcu_driver/index.md#739-mcu_setmode) | 此服务激活MCU电源模式。 |

## AUTOSAR MemIf（内存抽象接口）（8）

来源：[AUTOSAR MemIf（内存抽象接口）](../memory/memory_abstraction_interface/index.md) · SWS_MemoryAbstractionInterface

| 函数 | 简述 |
|---|---|
| [**MemIf_Cancel**](../memory/memory_abstraction_interface/index.md#733-memif_cancel) | 服务 ID 0x04。 |
| [**MemIf_EraseImmediateBlock**](../memory/memory_abstraction_interface/index.md#738-memif_eraseimmediateblock) | 服务 ID 0x09。 |
| [**MemIf_GetJobResult**](../memory/memory_abstraction_interface/index.md#735-memif_getjobresult) | 服务 ID 0x06。 |
| [**MemIf_GetStatus**](../memory/memory_abstraction_interface/index.md#734-memif_getstatus) | 服务 ID 0x05。 |
| [**MemIf_GetVersionInfo**](../memory/memory_abstraction_interface/index.md#737-memif_getversioninfo) | 服务 ID 0x08。 |
| [**MemIf_InvalidateBlock**](../memory/memory_abstraction_interface/index.md#736-memif_invalidateblock) | 服务 ID 0x07。 |
| [**MemIf_Read**](../memory/memory_abstraction_interface/index.md#731-memif_read) | 服务 ID 0x02。 |
| [**MemIf_Write**](../memory/memory_abstraction_interface/index.md#732-memif_write) | 服务 ID 0x03。 |

## AUTOSAR Memory Access（存储访问）（20）

来源：[AUTOSAR Memory Access（存储访问）](../memory/memory_access/index.md) · SWS_MemoryAccess

| 函数 | 简述 |
|---|---|
| [**MemAcc_ActivateMem**](../memory/memory_access/index.md#7319-memacc_activatemem) | 对由 hwId 和 headerAddress 所引用的 Mem 驱动进行动态激活和初始化。 |
| [**MemAcc_BlankCheck**](../memory/memory_access/index.md#7326-memacc_blankcheck) | 检查所传递的地址空间是否为空白（blank），即已被擦除且可写。 |
| [**MemAcc_Cancel**](../memory/memory_access/index.md#7321-memacc_cancel) | 对由该地址区 ID 所引用的地址区上的挂起作业触发取消操作。 |
| [**MemAcc_Compare**](../memory/memory_access/index.md#7325-memacc_compare) | 触发一个作业，将所传递的数据与所提供的地址区的存储内容进行比较。 |
| [**MemAcc_DeactivateMem**](../memory/memory_access/index.md#73110-memacc_deactivatemem) | 对由 hwId 和 headerAddress 所引用的 Mem 驱动进行动态去激活。 |
| [**MemAcc_DeInit**](../memory/memory_access/index.md#7312-memacc_deinit) | 去初始化模块。 |
| [**MemAcc_Erase**](../memory/memory_access/index.md#7324-memacc_erase) | 对给定区域触发擦除作业。 |
| [**MemAcc_GetJobInfo**](../memory/memory_access/index.md#7318-memacc_getjobinfo) | 返回当前存储作业的详细信息，例如存储设备 ID、作业类型、作业处理状态或作业结果、地址区以及地址和长度。 |
| [**MemAcc_GetJobResult**](../memory/memory_access/index.md#7314-memacc_getjobresult) | 返回由 addressAreaId 所引用的地址区的合并作业结果。 |
| [**MemAcc_GetJobStatus**](../memory/memory_access/index.md#7315-memacc_getjobstatus) | 返回由 addressAreaId 所引用的 MemAcc 作业的状态。 |
| [**MemAcc_GetMemoryInfo**](../memory/memory_access/index.md#7316-memacc_getmemoryinfo) | 该服务函数检索特定地址区的物理存储设备信息。 |
| [**MemAcc_GetProcessedLength**](../memory/memory_access/index.md#7317-memacc_getprocessedlength) | 返回当前作业中已被处理累积的字节数。 |
| [**MemAcc_GetVersionInfo**](../memory/memory_access/index.md#7313-memacc_getversioninfo) | 返回 MemAcc 模块的版本信息的服务。 |
| [**MemAcc_HwSpecificService**](../memory/memory_access/index.md#7327-memacc_hwspecificservice) | 触发一个由 hwServiceId 所引用的硬件特定的作业请求。 |
| [**MemAcc_Init**](../memory/memory_access/index.md#7311-memacc_init) | 初始化函数——初始化所有变量并将模块状态设置为已初始化。 |
| [**MemAcc_MainFunction**](../memory/memory_access/index.md#751-memacc_mainfunction) | 处理所请求的作业和内部管理操作的服务。 |
| [**MemAcc_Read**](../memory/memory_access/index.md#7322-memacc_read) | 触发一个读作业，将数据从源地址复制到所引用的目标数据缓冲区中。 |
| [**MemAcc_ReleaseLock**](../memory/memory_access/index.md#7329-memacc_releaselock) | 释放所提供地址区的访问锁。 |
| [**MemAcc_RequestLock**](../memory/memory_access/index.md#7328-memacc_requestlock) | 请求锁定一个地址区以进行独占访问。 |
| [**MemAcc_Write**](../memory/memory_access/index.md#7323-memacc_write) | 触发一个写作业，将所传递的数据以给定的地址和长度存储到所提供的地址区中。 |

## AUTOSAR Mem（内存驱动程序）（13）

来源：[AUTOSAR Mem（内存驱动程序）](../memory/memory_driver/index.md) · SWS_MemoryDriver

| 函数 | 简述 |
|---|---|
| [**Mem_BlankCheck**](../memory/memory_driver/index.md#7324-mem_blankcheck) | 服务 ID 0x9。 |
| [**Mem_DeInit**](../memory/memory_driver/index.md#7312-mem_deinit) | 服务 ID 0x0b。 |
| [**Mem_Erase**](../memory/memory_driver/index.md#7323-mem_erase) | 服务 ID 0x07。 |
| [**Mem_GetJobResult**](../memory/memory_driver/index.md#7314-mem_getjobresult) | 服务 ID 0x04。 |
| [**Mem_GetVersionInfo**](../memory/memory_driver/index.md#7313-mem_getversioninfo) | 服务 ID 0x02。 |
| [**Mem_HwSpecificService**](../memory/memory_driver/index.md#7325-mem_hwspecificservice) | 服务 ID 0x0a。 |
| [**Mem_Init**](../memory/memory_driver/index.md#7311-mem_init) | 服务 ID 0x01。 |
| [**Mem_MainFunction**](../memory/memory_driver/index.md#751-mem_mainfunction) | 服务 ID 0x03。 |
| [**Mem_PropagateError**](../memory/memory_driver/index.md#7317-mem_propagateerror) | 服务 ID 0x08。 |
| [**Mem_Read**](../memory/memory_driver/index.md#7321-mem_read) | 服务 ID 0x05。 |
| [**Mem_Resume**](../memory/memory_driver/index.md#7316-mem_resume) | 服务 ID 0x0d。 |
| [**Mem_Suspend**](../memory/memory_driver/index.md#7315-mem_suspend) | 服务 ID 0x0c。 |
| [**Mem_Write**](../memory/memory_driver/index.md#7322-mem_write) | 服务 ID 0x06。 |

## AUTOSAR Mka（MACsec 密钥协商）（18）

来源：[AUTOSAR Mka（MACsec 密钥协商）](../communication/macsec/index.md) · SWS_MACsecKeyAgreement

| 函数 | 简述 |
|---|---|
| [**Mka_GetCknStatus**](../communication/macsec/index.md#734-mka_getcknstatus) | — |
| [**Mka_GetEnable**](../communication/macsec/index.md#736-mka_getenable) | — |
| [**Mka_GetMacSecStatistics**](../communication/macsec/index.md#7310-mka_getmacsecstatistics) | — |
| [**Mka_GetMacSecStatisticsNotification**](../communication/macsec/index.md#741-mka_getmacsecstatisticsnotification) | — |
| [**Mka_GetPaeStatus**](../communication/macsec/index.md#737-mka_getpaestatus) | — |
| [**Mka_GetVersionInfo**](../communication/macsec/index.md#732-mka_getversioninfo) | — |
| [**Mka_Init**](../communication/macsec/index.md#731-mka_init) | — |
| [**Mka_LinkStateChange**](../communication/macsec/index.md#7311-mka_linkstatechange) | — |
| [**Mka_MacSecAddRxSaNotification**](../communication/macsec/index.md#746-mka_macsecaddrxsanotification) | — |
| [**Mka_MacSecAddTxSaNotification**](../communication/macsec/index.md#745-mka_macsecaddtxsanotification) | — |
| [**Mka_MacSecUpdateSecYNotification**](../communication/macsec/index.md#744-mka_macsecupdatesecynotification) | — |
| [**Mka_MainFunction**](../communication/macsec/index.md#751-mka_mainfunction) | — |
| [**Mka_RxIndication**](../communication/macsec/index.md#742-mka_rxindication) | — |
| [**Mka_SetCknStatus**](../communication/macsec/index.md#733-mka_setcknstatus) | — |
| [**Mka_SetEnable**](../communication/macsec/index.md#735-mka_setenable) | — |
| [**Mka_SetPaePermissiveMode**](../communication/macsec/index.md#738-mka_setpaepermissivemode) | — |
| [**Mka_StartPae**](../communication/macsec/index.md#739-mka_startpae) | — |
| [**Mka_TxConfirmation**](../communication/macsec/index.md#743-mka_txconfirmation) | — |

## AUTOSAR Nm（网络管理接口）（1）

来源：[AUTOSAR Nm（网络管理接口）](../communication/nm/index.md) · SWS_NetworkManagementInterface

| 函数 | 简述 |
|---|---|
| [**NmCarWakeUpCallout**](../communication/nm/index.md#7631-nmcarwakeupcallout) | — |

## AUTOSAR NVM（非易失性存储管理器）（29）

来源：[AUTOSAR NVM（非易失性存储管理器）](../memory/nvram_manager/index.md) · SWS_NVRAMManager

| 函数 | 简述 |
|---|---|
| [**NvM_Admin**](../memory/nvram_manager/index.md#7711-nvm_admin) | — |
| [**NvM_CancelJobs**](../memory/nvram_manager/index.md#7318-nvm_canceljobs) | 取消一个 NV 块的所有挂起作业的服务。 |
| [**NvM_CancelWriteAll**](../memory/nvram_manager/index.md#7333-nvm_cancelwriteall) | 取消正在运行的 NvM_WriteAll 请求的服务。 |
| [**NvM_EraseNvBlock**](../memory/nvram_manager/index.md#7324-nvm_erasenvblock) | 擦除一个 NV 块的服务。 |
| [**NvM_FirstInitAll**](../memory/nvram_manager/index.md#7335-nvm_firstinitall) | 发起多块优先初始化请求的服务。 |
| [**NvM_GetDataIndex**](../memory/nvram_manager/index.md#7313-nvm_getdataindex) | 获取数据集 NVRAM 块当前设置的 DataIndex 的服务。 |
| [**NvM_GetErrorStatus**](../memory/nvram_manager/index.md#7315-nvm_geterrorstatus) | 读取块相关的错误/状态信息的服务。 |
| [**NvM_GetVersionInfo**](../memory/nvram_manager/index.md#7316-nvm_getversioninfo) | 获取 NvM 模块版本信息的服务。 |
| [**NvM_Init**](../memory/nvram_manager/index.md#7311-nvm_init) | 重置所有内部变量的服务。 |
| [**NvM_InvalidateNvBlock**](../memory/nvram_manager/index.md#7325-nvm_invalidatenvblock) | 使一个 NV 块无效的服务。 |
| [**NvM_JobEndNotification**](../memory/nvram_manager/index.md#73361-nvm_jobendnotification) | 供底层内存抽象用于报告作业无错误结束的函数。 |
| [**NvM_JobErrorNotification**](../memory/nvram_manager/index.md#73362-nvm_joberrornotification) | 供底层内存抽象用于报告作业带错误结束的函数。 |
| [**NvM_MainFunction**](../memory/nvram_manager/index.md#741-nvm_mainfunction) | 用于执行 NvM 作业处理的服务。 |
| [**NvM_Mirror**](../memory/nvram_manager/index.md#7712-nvm_mirror) | — |
| [**NvM_NotifyInitBlock**](../memory/nvram_manager/index.md#7713-nvm_notifyinitblock) | — |
| [**NvM_NotifyJobFinished**](../memory/nvram_manager/index.md#7714-nvm_notifyjobfinished) | — |
| [**NvM_ReadAll**](../memory/nvram_manager/index.md#7331-nvm_readall) | 发起多块读请求的服务。 |
| [**NvM_ReadBlock**](../memory/nvram_manager/index.md#7321-nvm_readblock) | 将 NV 块的数据复制到其相应 RAM 块的服务。 |
| [**NvM_ReadPRAMBlock**](../memory/nvram_manager/index.md#7326-nvm_readpramblock) | 将 NV 块的数据复制到其相应永久 RAM 块的服务。 |
| [**NvM_RestoreBlockDefaults**](../memory/nvram_manager/index.md#7323-nvm_restoreblockdefaults) | 将默认数据恢复到其相应 RAM 块的服务。 |
| [**NvM_RestorePRAMBlockDefaults**](../memory/nvram_manager/index.md#7328-nvm_restorepramblockdefaults) | 将默认数据恢复到其相应永久 RAM 块的服务。 |
| [**NvM_Service**](../memory/nvram_manager/index.md#7715-nvm_service) | — |
| [**NvM_SetBlockProtection**](../memory/nvram_manager/index.md#7314-nvm_setblockprotection) | 设置或重置 NV 块写保护的服务。 |
| [**NvM_SetDataIndex**](../memory/nvram_manager/index.md#7312-nvm_setdataindex) | 设置数据集 NVRAM 块（Dataset NVRAM block）的 DataIndex 的服务。 |
| [**NvM_SetRamBlockStatus**](../memory/nvram_manager/index.md#7317-nvm_setramblockstatus) | 设置永久 RAM 块的 RAM 块状态或 NVRAM 块显式同步状态的服务。 |
| [**NvM_ValidateAll**](../memory/nvram_manager/index.md#7334-nvm_validateall) | 发起多块验证请求的服务。 |
| [**NvM_WriteAll**](../memory/nvram_manager/index.md#7332-nvm_writeall) | 发起多块写请求的服务。 |
| [**NvM_WriteBlock**](../memory/nvram_manager/index.md#7322-nvm_writeblock) | 将 RAM 块的数据复制到其相应 NV 块的服务。 |
| [**NvM_WritePRAMBlock**](../memory/nvram_manager/index.md#7327-nvm_writepramblock) | 将永久 RAM 块的数据复制到其相应 NV 块的服务。 |

## AUTOSAR OCU Driver（输出比较单元驱动）（12）

来源：[AUTOSAR OCU Driver（输出比较单元驱动）](../io/ocu_driver/index.md) · SWS_OCUDriver

| 函数 | 简述 |
|---|---|
| [**Ocu_DeInit**](../io/ocu_driver/index.md#732-ocu_deinit) | 此函数反初始化OCU模块。 |
| [**Ocu_DisableNotification**](../io/ocu_driver/index.md#7310-ocu_disablenotification) | 此服务用于禁用来自OCU通道的通知。 |
| [**Ocu_EnableNotification**](../io/ocu_driver/index.md#7311-ocu_enablenotification) | 此服务用于启用来自OCU通道的通知。 |
| [**Ocu_GetCounter**](../io/ocu_driver/index.md#737-ocu_getcounter) | 读取计数器当前值的服务。 |
| [**Ocu_GetVersionInfo**](../io/ocu_driver/index.md#7312-ocu_getversioninfo) | 此服务返回此模块的版本信息。 |
| [**Ocu_Init**](../io/ocu_driver/index.md#731-ocu_init) | OCU初始化服务。 |
| [**Ocu_SetAbsoluteThreshold**](../io/ocu_driver/index.md#738-ocu_setabsolutethreshold) | 使用绝对输入数据设置通道阈值值的服务。 |
| [**Ocu_SetPinAction**](../io/ocu_driver/index.md#736-ocu_setpinaction) | 告知驱动程序比较匹配时硬件（如果支持）应自动执行什么动作的服务。 |
| [**Ocu_SetPinState**](../io/ocu_driver/index.md#735-ocu_setpinstate) | 立即设置与OCU通道关联的引脚电平的服务。 |
| [**Ocu_SetRelativeThreshold**](../io/ocu_driver/index.md#739-ocu_setrelativethreshold) | 相对于计数器当前值设置通道阈值值的服务。 |
| [**Ocu_StartChannel**](../io/ocu_driver/index.md#733-ocu_startchannel) | 启动OCU通道的服务。 |
| [**Ocu_StopChannel**](../io/ocu_driver/index.md#734-ocu_stopchannel) | 停止OCU通道的服务。 |

## AUTOSAR Operating System（操作系统）（42）

来源：[AUTOSAR Operating System（操作系统）](../system_services/operating_system/index.md) · SWS_OS

| 函数 | 简述 |
|---|---|
| [**ActivateTaskAsyn**](../system_services/operating_system/index.md#7437-activatetaskasyn) | ActivateTask() 函数的异步版本。 |
| [**AllowAccess**](../system_services/operating_system/index.md#7421-allowaccess) | 该服务将 OS-Application 自身的状态从 APPLICATION_RESTARTING 设置为 APPLICATION_ACCESSIBLE。 |
| [**CallTrustedFunction**](../system_services/operating_system/index.md#744-calltrustedfunction) | （受信任或非受信任的）OS-Application 使用该服务调用一个可信函数。 |
| [**CheckISRMemoryAccess**](../system_services/operating_system/index.md#745-checkisrmemoryaccess) | 该服务检查一个内存区域是否可写/可读/可执行访问，并返回该内存区域是否属于堆栈空间的信息。 |
| [**CheckObjectAccess**](../system_services/operating_system/index.md#747-checkobjectaccess) | 该服务确定由 ApplID 给出的 OS-Application 是否被允许在 API 调用中使用某个任务（Task）、资源（Resource）、计数器（Counter）、警报（Alarm）或调度表（ScheduleTable）的 ID。 |
| [**CheckObjectOwnership**](../system_services/operating_system/index.md#748-checkobjectownership) | 该服务确定一个给定的任务（Task）、ISR、计数器（Counter）、警报（Alarm）或调度表（ScheduleTable）属于哪个 OS-Application。 |
| [**CheckTaskMemoryAccess**](../system_services/operating_system/index.md#746-checktaskmemoryaccess) | 该服务检查一个内存区域是否可写/可读/可执行访问，并返回该内存区域是否属于堆栈空间的信息。 |
| [**ClearPendingInterrupt**](../system_services/operating_system/index.md#7436-clearpendinginterrupt) | 通过修改中断控制器寄存器来清除中断挂起标志。 |
| [**ControlIdle**](../system_services/operating_system/index.md#7430-controlidle) | 该 API 允许调用者选择在 OS 空闲时间（例如没有任务（Task）/ISR 活动时）执行的空闲模式动作。 |
| [**DisableInterruptSource**](../system_services/operating_system/index.md#7435-disableinterruptsource) | 通过修改中断控制器寄存器来禁用中断源。 |
| [**EnableInterruptSource**](../system_services/operating_system/index.md#7434-enableinterruptsource) | 通过修改中断控制器寄存器来使能中断源。 |
| [**GetApplicationID**](../system_services/operating_system/index.md#741-getapplicationid) | 该服务确定调用者原本所属（被配置到）的 OS-Application（每个应用必须被分配一个唯一的标识符）。 |
| [**GetApplicationState**](../system_services/operating_system/index.md#7422-getapplicationstate) | 该服务返回一个 OS-Application 的当前状态。 |
| [**GetCoreID**](../system_services/operating_system/index.md#7424-getcoreid) | 该函数返回一个唯一的内核标识符。 |
| [**GetCounterValue**](../system_services/operating_system/index.md#7418-getcountervalue) | 该服务读取计数器（Counter）的当前计数值（如果计数器由硬件驱动，则返回硬件定时器滴答值；如果计数器由用户驱动，则返回软件滴答值）。 |
| [**GetCurrentApplicationID**](../system_services/operating_system/index.md#742-getcurrentapplicationid) | 该服务确定服务的调用者当前正在其中执行的 OS-Application。 |
| [**GetElapsedValue**](../system_services/operating_system/index.md#7419-getelapsedvalue) | 该服务获取当前滴答值与先前读取的滴答值之间的滴答数。 |
| [**GetISRID**](../system_services/operating_system/index.md#743-getisrid) | 该服务返回当前正在执行的 ISR 的标识符。 |
| [**GetNumberOfActivatedCores**](../system_services/operating_system/index.md#7423-getnumberofactivatedcores) | 该函数返回运行 AUTOSAR OS 的内核数量。 |
| [**GetScheduleTableStatus**](../system_services/operating_system/index.md#7416-getscheduletablestatus) | 该服务查询调度表（ScheduleTable）的状态（包括与同步有关的状态）。 |
| [**GetSpinlock**](../system_services/operating_system/index.md#7426-getspinlock) | GetSpinlock 尝试占用一个自旋锁变量。 |
| [**IncrementCounter**](../system_services/operating_system/index.md#7417-incrementcounter) | 该服务递增一个软件计数器（Counter）。 |
| [**IOC**](../system_services/operating_system/index.md#75-ioc) | — |
| [**IocEmptyQueue**](../system_services/operating_system/index.md#7536-iocemptyqueue) | 在由函数名中的 &lt;IocId&gt; 标识的排队通信中，应删除 IOC 内部通信队列的内容。 |
| [**IocInit**](../system_services/operating_system/index.md#7531-iocinit) | 该服务初始化 IOC 的数据结构。 |
| [**isOsStarted**](../system_services/operating_system/index.md#7439-isosstarted) | 该 API 返回一个布尔值，指示 OS 是否已被启动。 |
| [**NextScheduleTable**](../system_services/operating_system/index.md#7412-nextscheduletable) | 该服务将处理从一个调度表（ScheduleTable）切换到另一个调度表。 |
| [**Os_Service**](../system_services/operating_system/index.md#7821-os_service) | — |
| [**ProtectionHook**](../system_services/operating_system/index.md#771-protectionhook) | 只要发生严重错误（例如超出最坏情况执行时间或违反内存保护），就会调用保护钩子。 |
| [**ReceiverPullCB**](../system_services/operating_system/index.md#7621-receiverpullcb) | 该回调函数可以为通信的接收方配置。 |
| [**ReleaseSpinlock**](../system_services/operating_system/index.md#7427-releasespinlock) | ReleaseSpinlock 释放一个先前被占用的自旋锁变量。 |
| [**SetEventAsyn**](../system_services/operating_system/index.md#7438-seteventasyn) | SetEvent() 函数的异步版本。 |
| [**SetScheduleTableAsync**](../system_services/operating_system/index.md#7415-setscheduletableasync) | 该服务停止调度表（ScheduleTable）的同步。 |
| [**ShutdownAllCores**](../system_services/operating_system/index.md#7429-shutdownallcores) | 在该服务之后，所有 AUTOSAR 内核上的 OS 被关闭。 |
| [**StartCore**](../system_services/operating_system/index.md#7425-startcore) | 不支持在 StartOS() 之后调用该函数。 |
| [**StartScheduleTableAbs**](../system_services/operating_system/index.md#7410-startscheduletableabs) | 该服务以底层计数器上的绝对值"Start"开始调度表（ScheduleTable）的处理。 |
| [**StartScheduleTableRel**](../system_services/operating_system/index.md#749-startscheduletablerel) | 该服务以底层计数器上"当前"值为基准，在相对的"Offset"处开始调度表（ScheduleTable）的处理。 |
| [**StartScheduleTableSynchron**](../system_services/operating_system/index.md#7413-startscheduletablesynchron) | 该服务同步地启动一个显式同步的调度表（ScheduleTable）。 |
| [**StopScheduleTable**](../system_services/operating_system/index.md#7411-stopscheduletable) | 该服务在调度表（ScheduleTable）运行期间的任意时刻，立即取消其处理。 |
| [**SyncScheduleTable**](../system_services/operating_system/index.md#7414-syncscheduletable) | 该服务为调度表（ScheduleTable）提供同步计数并启动同步。 |
| [**TerminateApplication**](../system_services/operating_system/index.md#7420-terminateapplication) | 该服务终止调用它的任务（Task）/类别2 ISR/应用特定错误钩子所关联的 OS-Application。 |
| [**TryToGetSpinlock**](../system_services/operating_system/index.md#7428-trytogetspinlock) | TryToGetSpinlock 与 GetSpinlock 具有相同的功能，不同之处在于：如果自旋锁已被另一个内核上的某个 TASK 占用，该函数会设置 OUT 参数"Success"并以 E_OK 返回。 |

## AUTOSAR PduR (PDU Router)（5）

来源：[AUTOSAR PduR (PDU Router)](../communication/pdu_router/index.md) · SWS_PduR

| 函数 | 简述 |
|---|---|
| [**PduR_DisableRouting**](../communication/pdu_router/index.md#7315-pdur_disablerouting) | 禁用一个路由路径组。 |
| [**PduR_EnableRouting**](../communication/pdu_router/index.md#7314-pdur_enablerouting) | 使能一个路由路径组。 |
| [**PduR_GetConfigurationId**](../communication/pdu_router/index.md#7313-pdur_getconfigurationid) | 返回PDU路由器构建后配置的唯一标识符。 |
| [**PduR_GetVersionInfo**](../communication/pdu_router/index.md#7312-pdur_getversioninfo) | 返回本模块的版本信息。 |
| [**PduR_Init**](../communication/pdu_router/index.md#7311-pdur_init) | 初始化PDU路由器。 |

## AUTOSAR Platform Types（平台类型）（3）

来源：[AUTOSAR Platform Types（平台类型）](../general/platform_types/index.md) · SWS_PlatformTypes

| 函数 | 简述 |
|---|---|
| [**CPU_BIT_ORDER**](../general/platform_types/index.md#722-cpu_bit_order) | — |
| [**CPU_BYTE_ORDER**](../general/platform_types/index.md#723-cpu_byte_order) | — |
| [**CPU_TYPE**](../general/platform_types/index.md#721-cpu_type) | — |

## AUTOSAR Port Driver（端口驱动）（5）

来源：[AUTOSAR Port Driver（端口驱动）](../io/port_driver/index.md) · SWS_PortDriver

| 函数 | 简述 |
|---|---|
| [**Port_GetVersionInfo**](../io/port_driver/index.md#734-port_getversioninfo) | 返回本模块的版本信息。 |
| [**Port_Init**](../io/port_driver/index.md#731-port_init) | 初始化Port驱动程序模块。 |
| [**Port_RefreshPortDirection**](../io/port_driver/index.md#733-port_refreshportdirection) | 刷新端口方向。 |
| [**Port_SetPinDirection**](../io/port_driver/index.md#732-port_setpindirection) | 设置端口引脚方向。 |
| [**Port_SetPinMode**](../io/port_driver/index.md#735-port_setpinmode) | 设置端口引脚模式。 |

## AUTOSAR PWM Driver（脉冲宽度调制驱动）（14）

来源：[AUTOSAR PWM Driver（脉冲宽度调制驱动）](../io/pwm_driver/index.md) · SWS_PWMDriver

| 函数 | 简述 |
|---|---|
| [**Pwm_DeInit**](../io/pwm_driver/index.md#732-pwm_deinit) | PWM去初始化服务。 |
| [**Pwm_DisableNotification**](../io/pwm_driver/index.md#737-pwm_disablenotification) | 禁用PWM信号边沿通知的服务。 |
| [**Pwm_EnableNotification**](../io/pwm_driver/index.md#738-pwm_enablenotification) | 根据通知参数启用PWM信号边沿通知的服务。 |
| [**Pwm_GetCurrentPowerState**](../io/pwm_driver/index.md#7310-pwm_getcurrentpowerstate) | 此API返回PWM HW单元的当前电源状态。 |
| [**Pwm_GetOutputState**](../io/pwm_driver/index.md#736-pwm_getoutputstate) | 读取PWM输出信号内部状态的服务。 |
| [**Pwm_GetTargetPowerState**](../io/pwm_driver/index.md#7311-pwm_gettargetpowerstate) | 此API返回PWM HW单元的目标电源状态。 |
| [**Pwm_GetVersionInfo**](../io/pwm_driver/index.md#7313-pwm_getversioninfo) | 返回本模块版本信息的服务。 |
| [**Pwm_Init**](../io/pwm_driver/index.md#731-pwm_init) | PWM初始化服务。 |
| [**Pwm_Main_PowerTransitionManager**](../io/pwm_driver/index.md#751-pwm_main_powertransitionmanager) | 此API被周期性调用，监督电源状态转换，检查模块的就绪状态并发出回调IoHwAb_Pwm_NotifyReadyForPowerState\<Mode\>（参见PwmPowerStateReadyCbkRef配置参数）。 |
| [**Pwm_PreparePowerState**](../io/pwm_driver/index.md#7312-pwm_preparepowerstate) | 此API启动允许PWM HW模块进入请求的电源状态所需的过程。 |
| [**Pwm_SetDutyCycle**](../io/pwm_driver/index.md#733-pwm_setdutycycle) | 设置PWM通道占空比的服务。 |
| [**Pwm_SetOutputToIdle**](../io/pwm_driver/index.md#735-pwm_setoutputtoidle) | 将PWM输出设置为配置的空闲状态的服务。 |
| [**Pwm_SetPeriodAndDuty**](../io/pwm_driver/index.md#734-pwm_setperiodandduty) | 设置PWM通道周期和占空比的服务。 |
| [**Pwm_SetPowerState**](../io/pwm_driver/index.md#739-pwm_setpowerstate) | 此API配置Pwm模块，使其进入已准备的电源状态（从预定义的一组已配置电源状态中选择）。 |

## AUTOSAR RamTst（RAM测试）（20）

来源：[AUTOSAR RamTst（RAM测试）](../memory/ramtst/index.md) · SWS_RAMTest

| 函数 | 简述 |
|---|---|
| [**RamTst_Allow**](../memory/ramtst/index.md#734-ramtst_allow) | 服务 ID 0x03。 |
| [**RamTst_ChangeNumberOfTestedCells**](../memory/ramtst/index.md#7315-ramtst_changenumberoftestedcells) | 服务 ID 0x08。 |
| [**RamTst_DeInit**](../memory/ramtst/index.md#732-ramtst_deinit) | 服务 ID 0x0c。 |
| [**RamTst_ErrorNotification**](../memory/ramtst/index.md#7632-ramtst_errornotification) | — |
| [**RamTst_GetAlgParams**](../memory/ramtst/index.md#7311-ramtst_getalgparams) | 服务 ID 0x12。 |
| [**RamTst_GetExecutionStatus**](../memory/ramtst/index.md#737-ramtst_getexecutionstatus) | 服务 ID 0x04。 |
| [**RamTst_GetNumberOfTestedCells**](../memory/ramtst/index.md#7313-ramtst_getnumberoftestedcells) | 服务 ID 0x09。 |
| [**RamTst_GetTestAlgorithm**](../memory/ramtst/index.md#7312-ramtst_gettestalgorithm) | 服务 ID 0x07。 |
| [**RamTst_GetTestResult**](../memory/ramtst/index.md#738-ramtst_gettestresult) | 服务 ID 0x05。 |
| [**RamTst_GetTestResultPerBlock**](../memory/ramtst/index.md#739-ramtst_gettestresultperblock) | 服务 ID 0x06。 |
| [**RamTst_GetVersionInfo**](../memory/ramtst/index.md#7310-ramtst_getversioninfo) | 服务 ID 0x0a。 |
| [**RamTst_Init**](../memory/ramtst/index.md#731-ramtst_init) | 服务 ID 0x00。 |
| [**RamTst_MainFunction**](../memory/ramtst/index.md#751-ramtst_mainfunction) | 服务 ID 0x01。 |
| [**RamTst_Resume**](../memory/ramtst/index.md#736-ramtst_resume) | 服务 ID 0x0e。 |
| [**RamTst_RunFullTest**](../memory/ramtst/index.md#7316-ramtst_runfulltest) | 服务 ID 0x10。 |
| [**RamTst_RunPartialTest**](../memory/ramtst/index.md#7317-ramtst_runpartialtest) | 服务 ID 0x11。 |
| [**RamTst_SelectAlgParams**](../memory/ramtst/index.md#7314-ramtst_selectalgparams) | 服务 ID 0x0b。 |
| [**RamTst_Stop**](../memory/ramtst/index.md#733-ramtst_stop) | 服务 ID 0x02。 |
| [**RamTst_Suspend**](../memory/ramtst/index.md#735-ramtst_suspend) | 服务 ID 0x0d。 |
| [**RamTst_TestCompletedNotification**](../memory/ramtst/index.md#7631-ramtst_testcompletednotification) | — |

## AUTOSAR RTE（运行时环境）（64）

来源：[AUTOSAR RTE（运行时环境）](../rte/rte/index.md) · SWS_RTE

| 函数 | 简述 |
|---|---|
| [**Rte_Call**](../rte/rte/index.md#71613-rte_call) | — |
| [**Rte_CData**](../rte/rte/index.md#71616-rte_cdata) | — |
| [**Rte_DRead**](../rte/rte/index.md#71611-rte_dread) | — |
| [**Rte_Enter**](../rte/rte/index.md#71630-rte_enter) | — |
| [**Rte_Exit**](../rte/rte/index.md#71631-rte_exit) | — |
| [**Rte_Feedback**](../rte/rte/index.md#7168-rte_feedback) | — |
| [**Rte_GetMetaDataItem**](../rte/rte/index.md#71642-rte_getmetadataitem) | — |
| [**Rte_GetMetaDataLength**](../rte/rte/index.md#71643-rte_getmetadatalength) | — |
| [**Rte_IFeedback**](../rte/rte/index.md#71636-rte_ifeedback) | — |
| [**Rte_IInvalidate**](../rte/rte/index.md#71622-rte_iinvalidate) | — |
| [**Rte_Init**](../rte/rte/index.md#7183-rte_init) | — |
| [**Rte_Invalidate**](../rte/rte/index.md#7167-rte_invalidate) | — |
| [**Rte_IRead**](../rte/rte/index.md#71618-rte_iread) | — |
| [**Rte_IReadRef**](../rte/rte/index.md#71619-rte_ireadref) | — |
| [**Rte_IrTrigger**](../rte/rte/index.md#71635-rte_irtrigger) | — |
| [**Rte_IrvIRead**](../rte/rte/index.md#71624-rte_irviread) | — |
| [**Rte_IrvIReadRef**](../rte/rte/index.md#71625-rte_irvireadref) | — |
| [**Rte_IrvIWrite**](../rte/rte/index.md#71626-rte_irviwrite) | — |
| [**Rte_IrvIWriteRef**](../rte/rte/index.md#71627-rte_irviwriteref) | — |
| [**Rte_IrvRead**](../rte/rte/index.md#71628-rte_irvread) | — |
| [**Rte_IrvWrite**](../rte/rte/index.md#71629-rte_irvwrite) | — |
| [**Rte_IsAvailable**](../rte/rte/index.md#71639-rte_isavailable) | — |
| [**Rte_IStatus**](../rte/rte/index.md#71623-rte_istatus) | — |
| [**Rte_IsUpdated**](../rte/rte/index.md#71637-rte_isupdated) | — |
| [**Rte_IWrite**](../rte/rte/index.md#71620-rte_iwrite) | — |
| [**Rte_IWriteRef**](../rte/rte/index.md#71621-rte_iwriteref) | — |
| [**Rte_Mode**](../rte/rte/index.md#71632-rte_mode) | — |
| [**Rte_NPorts**](../rte/rte/index.md#7162-rte_nports) | — |
| [**Rte_PBCon**](../rte/rte/index.md#71638-rte_pbcon) | — |
| [**Rte_Pim**](../rte/rte/index.md#71615-rte_pim) | — |
| [**Rte_Port**](../rte/rte/index.md#7163-rte_port) | — |
| [**Rte_Ports**](../rte/rte/index.md#7161-rte_ports) | — |
| [**Rte_Prm**](../rte/rte/index.md#71617-rte_prm) | — |
| [**Rte_Read**](../rte/rte/index.md#71610-rte_read) | — |
| [**Rte_Receive**](../rte/rte/index.md#71612-rte_receive) | — |
| [**Rte_Result**](../rte/rte/index.md#71614-rte_result) | — |
| [**Rte_Send**](../rte/rte/index.md#7165-rte_send) | — |
| [**Rte_SetAvailable**](../rte/rte/index.md#71640-rte_setavailable) | — |
| [**Rte_SetMetaDataItem**](../rte/rte/index.md#71641-rte_setmetadataitem) | — |
| [**Rte_Start**](../rte/rte/index.md#7181-rte_start) | — |
| [**Rte_StartTiming**](../rte/rte/index.md#7184-rte_starttiming) | — |
| [**Rte_Stop**](../rte/rte/index.md#7182-rte_stop) | — |
| [**Rte_Switch**](../rte/rte/index.md#7166-rte_switch) | — |
| [**Rte_SwitchAck**](../rte/rte/index.md#7169-rte_switchack) | — |
| [**Rte_Trigger**](../rte/rte/index.md#71634-rte_trigger) | — |
| [**Rte_Write**](../rte/rte/index.md#7164-rte_write) | — |
| [**SchM_ActMainFunction**](../rte/rte/index.md#72512-schm_actmainfunction) | — |
| [**SchM_Call**](../rte/rte/index.md#7253-schm_call) | — |
| [**SchM_CData**](../rte/rte/index.md#72513-schm_cdata) | — |
| [**SchM_Deinit**](../rte/rte/index.md#7274-schm_deinit) | — |
| [**SchM_Enter**](../rte/rte/index.md#7251-schm_enter) | — |
| [**SchM_Exit**](../rte/rte/index.md#7252-schm_exit) | — |
| [**SchM_GetVersionInfo**](../rte/rte/index.md#7275-schm_getversioninfo) | — |
| [**SchM_Init**](../rte/rte/index.md#7271-schm_init) | — |
| [**SchM_Mode**](../rte/rte/index.md#7258-schm_mode) | — |
| [**SchM_Pim**](../rte/rte/index.md#72514-schm_pim) | — |
| [**SchM_Receive**](../rte/rte/index.md#7256-schm_receive) | — |
| [**SchM_Result**](../rte/rte/index.md#7254-schm_result) | — |
| [**SchM_Send**](../rte/rte/index.md#7255-schm_send) | — |
| [**SchM_Start**](../rte/rte/index.md#7272-schm_start) | — |
| [**SchM_StartTiming**](../rte/rte/index.md#7273-schm_starttiming) | — |
| [**SchM_Switch**](../rte/rte/index.md#7257-schm_switch) | — |
| [**SchM_SwitchAck**](../rte/rte/index.md#72510-schm_switchack) | — |
| [**SchM_Trigger**](../rte/rte/index.md#72511-schm_trigger) | — |

## AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）（18）

来源：[AUTOSAR SAE J1939 Diagnostic Communication Manager（SAE J1939 诊断通信管理器）](../diagnostics/j1939dcm/index.md) · SWS_SAEJ1939DiagnosticCommunicationManager

| 函数 | 简述 |
|---|---|
| [**DataCondition**](../diagnostics/j1939dcm/index.md#7731-datacondition) | — |
| [**J1939Dcm_CalibrationInformation**](../diagnostics/j1939dcm/index.md#7721-j1939dcm_calibrationinformation) | — |
| [**J1939Dcm_CopyRxData**](../diagnostics/j1939dcm/index.md#745-j1939dcm_copyrxdata) | C |
| [**J1939Dcm_CopyTxData**](../diagnostics/j1939dcm/index.md#747-j1939dcm_copytxdata) | C |
| [**J1939Dcm_DeInit**](../diagnostics/j1939dcm/index.md#732-j1939dcm_deinit) | C |
| [**J1939Dcm_DemTriggerOnDTCStatus**](../diagnostics/j1939dcm/index.md#7491-j1939dcm_demtriggerondtcstatus) | C |
| [**J1939Dcm_GenericDMxTransmit**](../diagnostics/j1939dcm/index.md#735-j1939dcm_genericdmxtransmit) | C |
| [**J1939Dcm_GetVersionInfo**](../diagnostics/j1939dcm/index.md#733-j1939dcm_getversioninfo) | C |
| [**J1939Dcm_Init**](../diagnostics/j1939dcm/index.md#731-j1939dcm_init) | C |
| [**J1939Dcm_MainFunction**](../diagnostics/j1939dcm/index.md#751-j1939dcm_mainfunction) | C |
| [**J1939Dcm_RequestIndication**](../diagnostics/j1939dcm/index.md#741-j1939dcm_requestindication) | C |
| [**J1939Dcm_RxIndication**](../diagnostics/j1939dcm/index.md#742-j1939dcm_rxindication) | C |
| [**J1939Dcm_SetState**](../diagnostics/j1939dcm/index.md#734-j1939dcm_setstate) | C |
| [**J1939Dcm_StartOfReception**](../diagnostics/j1939dcm/index.md#744-j1939dcm_startofreception) | C |
| [**J1939Dcm_TpRxIndication**](../diagnostics/j1939dcm/index.md#746-j1939dcm_tprxindication) | C |
| [**J1939Dcm_TpTxConfirmation**](../diagnostics/j1939dcm/index.md#748-j1939dcm_tptxconfirmation) | C |
| [**J1939Dcm_TxConfirmation**](../diagnostics/j1939dcm/index.md#743-j1939dcm_txconfirmation) | C |
| [**ModeCondition**](../diagnostics/j1939dcm/index.md#7743-modecondition) | — |

## AUTOSAR SchM（基础软件调度器）（18）

来源：[AUTOSAR SchM（基础软件调度器）](../rte/schm/index.md) · SWS_RTE

| 函数 | 简述 |
|---|---|
| [**SchM_ActMainFunction**](../rte/schm/index.md#912-schm_actmainfunction) | — |
| [**SchM_Call**](../rte/schm/index.md#93-schm_call) | — |
| [**SchM_CData**](../rte/schm/index.md#913-schm_cdata) | — |
| [**SchM_Deinit**](../rte/schm/index.md#114-schm_deinit) | — |
| [**SchM_Enter**](../rte/schm/index.md#91-schm_enter) | — |
| [**SchM_Exit**](../rte/schm/index.md#92-schm_exit) | — |
| [**SchM_GetVersionInfo**](../rte/schm/index.md#115-schm_getversioninfo) | — |
| [**SchM_Init**](../rte/schm/index.md#111-schm_init) | — |
| [**SchM_Mode**](../rte/schm/index.md#98-schm_mode) | — |
| [**SchM_Pim**](../rte/schm/index.md#914-schm_pim) | — |
| [**SchM_Receive**](../rte/schm/index.md#96-schm_receive) | — |
| [**SchM_Result**](../rte/schm/index.md#94-schm_result) | — |
| [**SchM_Send**](../rte/schm/index.md#95-schm_send) | — |
| [**SchM_Start**](../rte/schm/index.md#112-schm_start) | — |
| [**SchM_StartTiming**](../rte/schm/index.md#113-schm_starttiming) | — |
| [**SchM_Switch**](../rte/schm/index.md#97-schm_switch) | — |
| [**SchM_SwitchAck**](../rte/schm/index.md#910-schm_switchack) | — |
| [**SchM_Trigger**](../rte/schm/index.md#911-schm_trigger) | — |

## AUTOSAR SD（服务发现）（13）

来源：[AUTOSAR SD（服务发现）](../communication/service_discovery/index.md) · SWS_ServiceDiscovery

| 函数 | 简述 |
|---|---|
| [**Sd_AclPolicyCheck**](../communication/service_discovery/index.md#7311-sd_aclpolicycheck) | C |
| [**Sd_AclUpdate**](../communication/service_discovery/index.md#7310-sd_aclupdate) | C |
| [**Sd_ClientServiceSetState**](../communication/service_discovery/index.md#734-sd_clientservicesetstate) | C |
| [**Sd_ConsumedEventGroupSetState**](../communication/service_discovery/index.md#735-sd_consumedeventgroupsetstate) | C |
| [**Sd_GetVersionInfo**](../communication/service_discovery/index.md#732-sd_getversioninfo) | C |
| [**Sd_Init**](../communication/service_discovery/index.md#731-sd_init) | C |
| [**Sd_LocalIpAddrAssignmentChg**](../communication/service_discovery/index.md#736-sd_localipaddrassignmentchg) | C |
| [**Sd_MainFunction**](../communication/service_discovery/index.md#751-sd_mainfunction) | C |
| [**Sd_RxIndication**](../communication/service_discovery/index.md#741-sd_rxindication) | C |
| [**Sd_ServerServiceSetState**](../communication/service_discovery/index.md#733-sd_serverservicesetstate) | C |
| [**Sd_ServiceGroupStart**](../communication/service_discovery/index.md#738-sd_servicegroupstart) | C |
| [**Sd_ServiceGroupStop**](../communication/service_discovery/index.md#739-sd_servicegroupstop) | C |
| [**Sd_SoConModeChg**](../communication/service_discovery/index.md#737-sd_soconmodechg) | C |

## AUTOSAR SecOC (Secure Onboard Communication)（31）

来源：[AUTOSAR SecOC (Secure Onboard Communication)](../communication/sec_oc/index.md) · SWS_SecOc

| 函数 | 简述 |
|---|---|
| [**FreshnessManagement**](../communication/sec_oc/index.md#7832-freshnessmanagement) | — |
| [**SecOC_CopyRxData**](../communication/sec_oc/index.md#746-secoc_copyrxdata) | 调用本函数以向本模块提供 I-PDU 段（N-PDU）的接收数据。 |
| [**SecOC_CopyTxData**](../communication/sec_oc/index.md#747-secoc_copytxdata) | 本函数用于获取 I-PDU 段（N-PDU）的发送数据。 |
| [**SecOC_DeInit**](../communication/sec_oc/index.md#732-secoc_deinit) | 本服务停止安全板载通信。 |
| [**SecOC_GetRxFreshness**](../communication/sec_oc/index.md#751-secoc_getrxfreshness) | SecOC 使用本接口获取当前的新鲜度值。 |
| [**SecOC_GetRxFreshnessAuthData**](../communication/sec_oc/index.md#752-secoc_getrxfreshnessauthdata) | SecOC 使用本接口获取当前的新鲜度值。 |
| [**SecOC_GetTxFreshness**](../communication/sec_oc/index.md#753-secoc_gettxfreshness) | 本 API 以大端格式返回新鲜度值，数组（SecOCFreshnessValue）中第一个字节为最高有效位。 |
| [**SecOC_GetTxFreshnessTruncData**](../communication/sec_oc/index.md#754-secoc_gettxfreshnesstruncdata) | SecOC 使用本接口获取当前的新鲜度值。 |
| [**SecOC_GetVersionInfo**](../communication/sec_oc/index.md#733-secoc_getversioninfo) | 返回本模块的版本信息。 |
| [**SecOC_IfCancelTransmit**](../communication/sec_oc/index.md#736-secoc_ifcanceltransmit) | 请求取消下层通信模块中正在进行的某个 PDU 的传输。 |
| [**SecOC_IfTransmit**](../communication/sec_oc/index.md#734-secoc_iftransmit) | 请求发送一个 PDU。 |
| [**SecOC_Init**](../communication/sec_oc/index.md#731-secoc_init) | 初始化 SecOC 模块。 |
| [**SecOC_MainFunctionRx**](../communication/sec_oc/index.md#761-secoc_mainfunctionrx) | 本函数执行 SecOC 模块 Rx 路径的认证与验证处理。 |
| [**SecOC_MainFunctionTx**](../communication/sec_oc/index.md#762-secoc_mainfunctiontx) | 本函数执行 SecOC 模块 Tx 路径的认证与验证处理。 |
| [**SecOC_RxIndication**](../communication/sec_oc/index.md#741-secoc_rxindication) | 指示从下层通信接口模块接收到一个 PDU。 |
| [**SecOC_SPduTxConfirmation**](../communication/sec_oc/index.md#755-secoc_spdutxconfirmation) | SecOC 使用本接口指示受保护的 I-PDU 已发起传输。 |
| [**SecOC_StartOfReception**](../communication/sec_oc/index.md#748-secoc_startofreception) | 在开始接收一个被分段为多个 N-PDU（FF 带一个或多个后续 CF）或由单个 N-PDU（SF）组成的 N-SDU 时调用本函数。 |
| [**SecOC_TpCancelReceive**](../communication/sec_oc/index.md#738-secoc_tpcancelreceive) | 请求取消下层传输协议模块中正在进行的某个 PDU 的接收。 |
| [**SecOC_TpCancelTransmit**](../communication/sec_oc/index.md#737-secoc_tpcanceltransmit) | 请求取消下层通信模块中正在进行的某个 PDU 的传输。 |
| [**SecOC_TpRxIndication**](../communication/sec_oc/index.md#742-secoc_tprxindication) | 在通过 TP API 接收到一个 I-PDU 之后被调用，结果参数指示传输是否成功。 |
| [**SecOC_TpTransmit**](../communication/sec_oc/index.md#735-secoc_tptransmit) | 请求发送一个 PDU。 |
| [**SecOC_TpTxConfirmation**](../communication/sec_oc/index.md#744-secoc_tptxconfirmation) | 在 I-PDU 已在其网络上传输之后被调用，结果参数指示传输是否成功。 |
| [**SecOC_TriggerTransmit**](../communication/sec_oc/index.md#745-secoc_triggertransmit) | 应将数据复制到 PduInfoPtr-&gt;SduDataPtr 提供的缓冲区中，并更新 PduInfoPtr-&gt;SduLength。 |
| [**SecOC_TxConfirmation**](../communication/sec_oc/index.md#743-secoc_txconfirmation) | 下层通信接口模块确认一个 PDU 的传输成功或传输失败。 |
| [**SecOC_VerificationStatusCallout**](../communication/sec_oc/index.md#7731-secoc_verificationstatuscallout) | 本服务用于将 SecOC 模块每次验证尝试的状态传播给其他模块。 |
| [**SecOC_VerifyStatus**](../communication/sec_oc/index.md#7732-secoc_verifystatus) | 本服务提供了向应用通知 SecOC 模块对所接收 PDU 的验证尝试结果的能力。 |
| [**SecOC_VerifyStatusOverride**](../communication/sec_oc/index.md#739-secoc_verifystatusoverride) | 本服务提供了强制 SecOC 特定行为的能力：接受或丢弃一个 I-PDU，可以执行验证器验证，也可以不执行，或者独立于验证器验证结果，并为 SecOC_VerificationResultType 强制一个特定结果，以便在应用中实现额… |
| [**SendDefaultAuthenticationInformation**](../communication/sec_oc/index.md#7842-senddefaultauthenticationinformation) | — |
| [**VerificationStatus**](../communication/sec_oc/index.md#7843-verificationstatus) | — |
| [**VerificationStatusNotification**](../communication/sec_oc/index.md#7845-verificationstatusnotification) | — |
| [**VerifyStatusConfiguration**](../communication/sec_oc/index.md#7844-verifystatusconfiguration) | — |

## AUTOSAR SoAd (Socket Adaptor)（37）

来源：[AUTOSAR SoAd (Socket Adaptor)](../communication/soad/index.md) · SWS_SocketAdaptor

| 函数 | 简述 |
|---|---|
| [**SoAd_CloseSoCon**](../communication/soad/index.md#7343-soad_closesocon) | C |
| [**SoAd_CopyTxData**](../communication/soad/index.md#742-soad_copytxdata) | C |
| [**SoAd_DisableRouting**](../communication/soad/index.md#73412-soad_disablerouting) | C |
| [**SoAd_DisableSpecificRouting**](../communication/soad/index.md#73413-soad_disablespecificrouting) | C |
| [**SoAd_EnableRouting**](../communication/soad/index.md#73410-soad_enablerouting) | C |
| [**SoAd_EnableSpecificRouting**](../communication/soad/index.md#73411-soad_enablespecificrouting) | C |
| [**SoAd_GetAndResetMeasurementData**](../communication/soad/index.md#73420-soad_getandresetmeasurementdata) | C |
| [**SoAd_GetLocalAddr**](../communication/soad/index.md#7347-soad_getlocaladdr) | C |
| [**SoAd_GetPhysAddr**](../communication/soad/index.md#7348-soad_getphysaddr) | C |
| [**SoAd_GetRemoteAddr**](../communication/soad/index.md#7349-soad_getremoteaddr) | C |
| [**SoAd_GetSoConId**](../communication/soad/index.md#7341-soad_getsoconid) | C |
| [**SoAd_GetSoConMode**](../communication/soad/index.md#7344-soad_getsoconmode) | C |
| [**SoAd_GetVersionInfo**](../communication/soad/index.md#7311-soad_getversioninfo) | C |
| [**SoAd_IfRoutingGroupTransmit**](../communication/soad/index.md#7322-soad_ifroutinggrouptransmit) | C |
| [**SoAd_IfSpecificRoutingGroupTransmit**](../communication/soad/index.md#7323-soad_ifspecificroutinggrouptransmit) | C |
| [**SoAd_IfTransmit**](../communication/soad/index.md#7321-soad_iftransmit) | C |
| [**SoAd_Init**](../communication/soad/index.md#7312-soad_init) | C |
| [**SoAd_IsConnectionReady**](../communication/soad/index.md#73421-soad_isconnectionready) | C |
| [**SoAd_LocalIpAddrAssignmentChg**](../communication/soad/index.md#747-soad_localipaddrassignmentchg) | C |
| [**SoAd_MainFunction**](../communication/soad/index.md#752-soad_mainfunction) | C |
| [**SoAd_OpenSoCon**](../communication/soad/index.md#7342-soad_opensocon) | C |
| [**SoAd_ReadDhcpHostNameOption**](../communication/soad/index.md#73418-soad_readdhcphostnameoption) | C |
| [**SoAd_ReleaseIpAddrAssignment**](../communication/soad/index.md#7346-soad_releaseipaddrassignment) | C |
| [**SoAd_ReleaseRemoteAddr**](../communication/soad/index.md#73416-soad_releaseremoteaddr) | C |
| [**SoAd_RequestIpAddrAssignment**](../communication/soad/index.md#7345-soad_requestipaddrassignment) | C |
| [**SoAd_RxIndication**](../communication/soad/index.md#741-soad_rxindication) | C |
| [**SoAd_SetRemoteAddr**](../communication/soad/index.md#73414-soad_setremoteaddr) | C |
| [**SoAd_SetUniqueRemoteAddr**](../communication/soad/index.md#73415-soad_setuniqueremoteaddr) | C |
| [**SoAd_TcpAccepted**](../communication/soad/index.md#744-soad_tcpaccepted) | C |
| [**SoAd_TcpConnected**](../communication/soad/index.md#745-soad_tcpconnected) | C |
| [**SoAd_TcpIpEvent**](../communication/soad/index.md#746-soad_tcpipevent) | C |
| [**SoAd_TpCancelReceive**](../communication/soad/index.md#7332-soad_tpcancelreceive) | C |
| [**SoAd_TpCancelTransmit**](../communication/soad/index.md#7331-soad_tpcanceltransmit) | C |
| [**SoAd_TpChangeParameter**](../communication/soad/index.md#73417-soad_tpchangeparameter) | C |
| [**SoAd_TpTransmit**](../communication/soad/index.md#7324-soad_tptransmit) | C |
| [**SoAd_TxConfirmation**](../communication/soad/index.md#743-soad_txconfirmation) | C |
| [**SoAd_WriteDhcpHostNameOption**](../communication/soad/index.md#73419-soad_writedhcphostnameoption) | C |

## Specification of Bit Handling Routines（位处理例程规范）（25）

来源：[Specification of Bit Handling Routines（位处理例程规范）](../libraries/bfx/index.md) · SWS_BFXLibrary

| 函数 | 简述 |
|---|---|
| [**Bfx_ClrBit**](../libraries/bfx/index.md#742-bfx_clrbit) | 该函数应将输入数据在请求的位位置上的逻辑状态清除为「0」。 |
| [**Bfx_ClrBitMask**](../libraries/bfx/index.md#747-bfx_clrbitmask) | 该函数应按照掩码的规定，将输入数据所有位位置的逻辑状态清除为「0」。 |
| [**Bfx_CopyBit**](../libraries/bfx/index.md#7417-bfx_copybit) | 该函数应将一个位从源数据的某个位位置复制到目标数据的某个位位置。 |
| [**Bfx_CountLeadingOnes**](../libraries/bfx/index.md#7422-bfx_countleadingones) | 从最高有效位开始统计数据中连续 1 的数量并返回结果。 |
| [**Bfx_CountLeadingSigns**](../libraries/bfx/index.md#7423-bfx_countleadingsigns) | 从 msb 减一的位置开始，统计数据中与最高有效位具有相同值的连续位的数量。 |
| [**Bfx_CountLeadingZeros**](../libraries/bfx/index.md#7424-bfx_countleadingzeros) | 从最高有效位开始统计数据中连续 0 的数量并返回结果。 |
| [**Bfx_GetBit**](../libraries/bfx/index.md#743-bfx_getbit) | 该函数应返回输入数据在请求的位位置上的逻辑状态。 |
| [**Bfx_GetBits**](../libraries/bfx/index.md#745-bfx_getbits) | 该函数应返回输入数据从「BitStartPn」开始、长度为「BitLn」的各个位。 |
| [**Bfx_GetVersionInfo**](../libraries/bfx/index.md#781-bfx_getversioninfo) | 返回本库的版本信息。 |
| [**Bfx_PutBit**](../libraries/bfx/index.md#7420-bfx_putbit) | 该函数应按照「Status」值，将输入数据中由 BitPn 指定的位更新为「1」或「0」。 |
| [**Bfx_PutBits**](../libraries/bfx/index.md#7418-bfx_putbits) | 该函数应按照 Pattern 中的规定，将位从指定的位位置开始放入输入 Data 中。 |
| [**Bfx_PutBitsMask**](../libraries/bfx/index.md#7419-bfx_putbitsmask) | 该函数应将 Pattern 中定义的、且相应 Mask 位置位为 1 的所有位放入输入 Data 中。 |
| [**Bfx_RotBitLt**](../libraries/bfx/index.md#7416-bfx_rotbitlt) | 该函数应将数据向左循环移位 ShiftCnt 位。 |
| [**Bfx_RotBitRt**](../libraries/bfx/index.md#7415-bfx_rotbitrt) | 该函数应将数据向右循环移位 ShiftCnt 位。 |
| [**Bfx_SetBit**](../libraries/bfx/index.md#741-bfx_setbit) | 该函数应将输入数据在请求的位位置上的逻辑状态设置为「1」。 |
| [**Bfx_SetBitMask**](../libraries/bfx/index.md#746-bfx_setbitmask) | 该函数应按照相应的 Mask 位设置为 1 的情况，将数据设置为逻辑状态「1」，其余位保持其原始值。 |
| [**Bfx_SetBits**](../libraries/bfx/index.md#744-bfx_setbits) | 该函数应按照「Status」值，从「BitStartPn」开始、以「BitLn」为长度，将输入数据设置为「1」或「0」。 |
| [**Bfx_ShiftBitLt**](../libraries/bfx/index.md#7414-bfx_shiftbitlt) | 该函数应将数据左移 ShiftCnt 位。 |
| [**Bfx_ShiftBitRt**](../libraries/bfx/index.md#7413-bfx_shiftbitrt) | 该函数应将数据右移 ShiftCnt 位。 |
| [**Bfx_ShiftBitSat**](../libraries/bfx/index.md#7421-bfx_shiftbitsat) | 带饱和的算术移位。 |
| [**Bfx_ToggleBitMask**](../libraries/bfx/index.md#7412-bfx_togglebitmask) | 当掩码的相应位被启用并置为 1 时，该函数切换数据的相应位。 |
| [**Bfx_ToggleBits**](../libraries/bfx/index.md#7411-bfx_togglebits) | 该函数切换数据的所有位（数据的 1 的补码）。 |
| [**Bfx_TstBitLnMask**](../libraries/bfx/index.md#749-bfx_tstbitlnmask) | 该函数对输入数据进行测试，如果按照掩码至少有一个位被置位，则该函数应返回 TRUE，否则应返回 FALSE。 |
| [**Bfx_TstBitMask**](../libraries/bfx/index.md#748-bfx_tstbitmask) | 如果掩码值中定义的所有位都在输入 Data 值中被置位，则该函数应返回 TRUE。 |
| [**Bfx_TstParityEven**](../libraries/bfx/index.md#7410-bfx_tstparityeven) | 该函数测试被置位为 1 的位的数量。 |

## Specification of CRC Routines（CRC 例程规范）（1）

来源：[Specification of CRC Routines（CRC 例程规范）](../libraries/crc/index.md) · SWS_CRCLibrary

| 函数 | 简述 |
|---|---|
| [**Crc_GetVersionInfo**](../libraries/crc/index.md#735-crc_getversioninfo) | 此服务返回本模块的版本信息。 |

## Specification of SW-C End-to-End Communication Protection Library（SW-C 端到端通信保护库规范）（91）

来源：[Specification of SW-C End-to-End Communication Protection Library（SW-C 端到端通信保护库规范）](../libraries/e2e/index.md) · SWS_E2ELibrary

| 函数 | 简述 |
|---|---|
| [**E2E_GetVersionInfo**](../libraries/e2e/index.md#73161-e2e_getversioninfo) | 返回本模块的版本信息。 |
| [**E2E_P01Check**](../libraries/e2e/index.md#7314-e2e_p01check) | 使用 E2E profile 1 校验接收到的 Data。 |
| [**E2E_P01CheckInit**](../libraries/e2e/index.md#7315-e2e_p01checkinit) | 初始化校验状态。 |
| [**E2E_P01Forward**](../libraries/e2e/index.md#7313-e2e_p01forward) | 使用 E2E profile 01 保护被转发的数据。 |
| [**E2E_P01MapStatusToSM**](../libraries/e2e/index.md#7316-e2e_p01mapstatustosm) | 该函数将 Profile 1 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P01Protect**](../libraries/e2e/index.md#7311-e2e_p01protect) | 使用 E2E profile 1 保护要发送的数组/缓冲区。 |
| [**E2E_P01ProtectInit**](../libraries/e2e/index.md#7312-e2e_p01protectinit) | 初始化保护状态。 |
| [**E2E_P02Check**](../libraries/e2e/index.md#7324-e2e_p02check) | 使用 E2E profile 2 校验数组/缓冲区。 |
| [**E2E_P02CheckInit**](../libraries/e2e/index.md#7325-e2e_p02checkinit) | 初始化校验状态。 |
| [**E2E_P02Forward**](../libraries/e2e/index.md#7323-e2e_p02forward) | 使用 E2E profile 02 保护被转发的数据。 |
| [**E2E_P02MapStatusToSM**](../libraries/e2e/index.md#7326-e2e_p02mapstatustosm) | 该函数将 Profile 2 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P02Protect**](../libraries/e2e/index.md#7321-e2e_p02protect) | 使用 E2E profile 2 保护要发送的数组/缓冲区。 |
| [**E2E_P02ProtectInit**](../libraries/e2e/index.md#7322-e2e_p02protectinit) | 初始化保护状态。 |
| [**E2E_P04Check**](../libraries/e2e/index.md#7334-e2e_p04check) | 使用 E2E profile 4 校验接收到的 Data。 |
| [**E2E_P04CheckInit**](../libraries/e2e/index.md#7335-e2e_p04checkinit) | 初始化校验状态。 |
| [**E2E_P04Forward**](../libraries/e2e/index.md#7333-e2e_p04forward) | 使用 E2E profile 04 保护被转发的数据。 |
| [**E2E_P04MapStatusToSM**](../libraries/e2e/index.md#7336-e2e_p04mapstatustosm) | 该函数将 Profile 4 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P04mCheckInit**](../libraries/e2e/index.md#7346-e2e_p04mcheckinit) | 初始化校验状态。 |
| [**E2E_P04mForward**](../libraries/e2e/index.md#7343-e2e_p04mforward) | 使用 E2E profile 4m 保护被转发的数据。 |
| [**E2E_P04mMapStatusToSM**](../libraries/e2e/index.md#7347-e2e_p04mmapstatustosm) | 该函数将 Profile 4m 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P04mProtect**](../libraries/e2e/index.md#7341-e2e_p04mprotect) | 使用 E2E profile 4m 保护要发送的数组/缓冲区。 |
| [**E2E_P04mProtectInit**](../libraries/e2e/index.md#7342-e2e_p04mprotectinit) | 初始化保护状态。 |
| [**E2E_P04mSinkCheck**](../libraries/e2e/index.md#7345-e2e_p04msinkcheck) | 使用 E2E profile 4m 校验接收到的 Data。 |
| [**E2E_P04mSourceCheck**](../libraries/e2e/index.md#7344-e2e_p04msourcecheck) | 使用 E2E profile 4m 校验接收到的 Data。 |
| [**E2E_P04Protect**](../libraries/e2e/index.md#7331-e2e_p04protect) | 使用 E2E profile 4 保护要发送的数组/缓冲区。 |
| [**E2E_P04ProtectInit**](../libraries/e2e/index.md#7332-e2e_p04protectinit) | 初始化保护状态。 |
| [**E2E_P05Check**](../libraries/e2e/index.md#7354-e2e_p05check) | 使用 E2E profile 5 校验接收到的 Data。 |
| [**E2E_P05CheckInit**](../libraries/e2e/index.md#7355-e2e_p05checkinit) | 初始化校验状态。 |
| [**E2E_P05Forward**](../libraries/e2e/index.md#7353-e2e_p05forward) | 使用 E2E profile 05 保护被转发的数据。 |
| [**E2E_P05MapStatusToSM**](../libraries/e2e/index.md#7356-e2e_p05mapstatustosm) | 该函数将 Profile 5 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P05Protect**](../libraries/e2e/index.md#7351-e2e_p05protect) | 使用 E2E profile 5 保护要发送的数组/缓冲区。 |
| [**E2E_P05ProtectInit**](../libraries/e2e/index.md#7352-e2e_p05protectinit) | 初始化保护状态。 |
| [**E2E_P06Check**](../libraries/e2e/index.md#7364-e2e_p06check) | 使用 E2E profile 6 校验接收到的 Data。 |
| [**E2E_P06CheckInit**](../libraries/e2e/index.md#7365-e2e_p06checkinit) | 初始化校验状态。 |
| [**E2E_P06Forward**](../libraries/e2e/index.md#7363-e2e_p06forward) | 使用 E2E profile 06 保护被转发的数据。 |
| [**E2E_P06MapStatusToSM**](../libraries/e2e/index.md#7366-e2e_p06mapstatustosm) | 该函数将 Profile 6 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P06Protect**](../libraries/e2e/index.md#7361-e2e_p06protect) | 使用 E2E profile 6 保护要发送的数组/缓冲区。 |
| [**E2E_P06ProtectInit**](../libraries/e2e/index.md#7362-e2e_p06protectinit) | 初始化保护状态。 |
| [**E2E_P07Check**](../libraries/e2e/index.md#7374-e2e_p07check) | 使用 E2E profile 7 校验接收到的 Data。 |
| [**E2E_P07CheckInit**](../libraries/e2e/index.md#7375-e2e_p07checkinit) | 初始化校验状态。 |
| [**E2E_P07Forward**](../libraries/e2e/index.md#7373-e2e_p07forward) | 使用 E2E profile 07 保护被转发的数据。 |
| [**E2E_P07MapStatusToSM**](../libraries/e2e/index.md#7376-e2e_p07mapstatustosm) | 该函数将 Profile 7 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P07mCheckInit**](../libraries/e2e/index.md#7386-e2e_p07mcheckinit) | 初始化校验状态。 |
| [**E2E_P07mForward**](../libraries/e2e/index.md#7383-e2e_p07mforward) | 使用 E2E profile 7m 保护被转发的数据。 |
| [**E2E_P07mMapStatusToSM**](../libraries/e2e/index.md#7387-e2e_p07mmapstatustosm) | 该函数将 Profile 7m 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P07mProtect**](../libraries/e2e/index.md#7381-e2e_p07mprotect) | 使用 E2E profile 7m 保护要发送的数组/缓冲区。 |
| [**E2E_P07mProtectInit**](../libraries/e2e/index.md#7382-e2e_p07mprotectinit) | 初始化保护状态。 |
| [**E2E_P07mSinkCheck**](../libraries/e2e/index.md#7385-e2e_p07msinkcheck) | 使用 E2E profile 7m 校验接收到的 Data。 |
| [**E2E_P07mSourceCheck**](../libraries/e2e/index.md#7384-e2e_p07msourcecheck) | 使用 E2E profile 7m 校验接收到的 Data。 |
| [**E2E_P07Protect**](../libraries/e2e/index.md#7371-e2e_p07protect) | 使用 E2E profile 7 保护要发送的数组/缓冲区。 |
| [**E2E_P07ProtectInit**](../libraries/e2e/index.md#7372-e2e_p07protectinit) | 初始化保护状态。 |
| [**E2E_P08Check**](../libraries/e2e/index.md#7394-e2e_p08check) | 使用 E2E profile 08 校验接收到的 Data。 |
| [**E2E_P08CheckInit**](../libraries/e2e/index.md#7395-e2e_p08checkinit) | 初始化校验状态。 |
| [**E2E_P08Forward**](../libraries/e2e/index.md#7393-e2e_p08forward) | 使用 E2E profile 08 保护被转发的数据。 |
| [**E2E_P08MapStatusToSM**](../libraries/e2e/index.md#7396-e2e_p08mapstatustosm) | 该函数将 Profile 08 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P08mCheckInit**](../libraries/e2e/index.md#73106-e2e_p08mcheckinit) | 初始化校验状态。 |
| [**E2E_P08mForward**](../libraries/e2e/index.md#73103-e2e_p08mforward) | 使用 E2E profile 08m 保护被转发的数据。 |
| [**E2E_P08mMapStatusToSM**](../libraries/e2e/index.md#73107-e2e_p08mmapstatustosm) | 该函数将 Profile 08m 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P08mProtect**](../libraries/e2e/index.md#73101-e2e_p08mprotect) | 使用 E2E profile 08m 保护要发送的数组/缓冲区。 |
| [**E2E_P08mProtectInit**](../libraries/e2e/index.md#73102-e2e_p08mprotectinit) | 初始化保护状态。 |
| [**E2E_P08mSinkCheck**](../libraries/e2e/index.md#73105-e2e_p08msinkcheck) | 使用 E2E profile 8m 校验接收到的 Data。 |
| [**E2E_P08mSourceCheck**](../libraries/e2e/index.md#73104-e2e_p08msourcecheck) | 使用 E2E profile 8m 校验接收到的 Data。 |
| [**E2E_P08Protect**](../libraries/e2e/index.md#7391-e2e_p08protect) | 使用 E2E profile 08 保护要发送的数组/缓冲区。 |
| [**E2E_P08ProtectInit**](../libraries/e2e/index.md#7392-e2e_p08protectinit) | 初始化保护状态。 |
| [**E2E_P11Check**](../libraries/e2e/index.md#73114-e2e_p11check) | 使用 E2E profile 11 校验接收到的 Data。 |
| [**E2E_P11CheckInit**](../libraries/e2e/index.md#73115-e2e_p11checkinit) | 初始化校验状态。 |
| [**E2E_P11Forward**](../libraries/e2e/index.md#73113-e2e_p11forward) | 使用 E2E profile 11 保护被转发的数据。 |
| [**E2E_P11MapStatusToSM**](../libraries/e2e/index.md#73116-e2e_p11mapstatustosm) | 该函数将 Profile 11 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P11Protect**](../libraries/e2e/index.md#73111-e2e_p11protect) | 使用 E2E profile 11 保护要发送的数组/缓冲区。 |
| [**E2E_P11ProtectInit**](../libraries/e2e/index.md#73112-e2e_p11protectinit) | 初始化保护状态。 |
| [**E2E_P22Check**](../libraries/e2e/index.md#73124-e2e_p22check) | 使用 E2E profile 22 校验接收到的 Data。 |
| [**E2E_P22CheckInit**](../libraries/e2e/index.md#73125-e2e_p22checkinit) | 初始化校验状态。 |
| [**E2E_P22Forward**](../libraries/e2e/index.md#73123-e2e_p22forward) | 使用 E2E profile 22 保护被转发的数据。 |
| [**E2E_P22MapStatusToSM**](../libraries/e2e/index.md#73126-e2e_p22mapstatustosm) | 该函数将 Profile 22 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P22Protect**](../libraries/e2e/index.md#73121-e2e_p22protect) | 使用 E2E profile 22 保护要发送的数组/缓冲区。 |
| [**E2E_P22ProtectInit**](../libraries/e2e/index.md#73122-e2e_p22protectinit) | 初始化保护状态。 |
| [**E2E_P44Check**](../libraries/e2e/index.md#73134-e2e_p44check) | 使用 E2E profile 44 校验接收到的 Data。 |
| [**E2E_P44CheckInit**](../libraries/e2e/index.md#73135-e2e_p44checkinit) | 初始化校验状态。 |
| [**E2E_P44Forward**](../libraries/e2e/index.md#73133-e2e_p44forward) | 使用 E2E profile 44 保护被转发的数据。 |
| [**E2E_P44MapStatusToSM**](../libraries/e2e/index.md#73136-e2e_p44mapstatustosm) | 该函数将 Profile 44 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P44mCheckInit**](../libraries/e2e/index.md#73146-e2e_p44mcheckinit) | 初始化校验状态。 |
| [**E2E_P44mForward**](../libraries/e2e/index.md#73143-e2e_p44mforward) | 使用 E2E profile 44m 保护被转发的数据。 |
| [**E2E_P44mMapStatusToSM**](../libraries/e2e/index.md#73147-e2e_p44mmapstatustosm) | 该函数将 Profile 44m 的校验状态映射为一个通用校验状态，E2E 状态机校验函数可以使用该状态。 |
| [**E2E_P44mProtect**](../libraries/e2e/index.md#73141-e2e_p44mprotect) | 使用 E2E profile 44m 保护要发送的数组/缓冲区。 |
| [**E2E_P44mProtectInit**](../libraries/e2e/index.md#73142-e2e_p44mprotectinit) | 初始化保护状态。 |
| [**E2E_P44mSinkCheck**](../libraries/e2e/index.md#73145-e2e_p44msinkcheck) | 使用 E2E profile 44m 校验接收到的 Data。 |
| [**E2E_P44mSourceCheck**](../libraries/e2e/index.md#73144-e2e_p44msourcecheck) | 使用 E2E profile 44m 校验接收到的 Data。 |
| [**E2E_P44Protect**](../libraries/e2e/index.md#73131-e2e_p44protect) | 使用 E2E profile 44 保护要发送的数组/缓冲区。 |
| [**E2E_P44ProtectInit**](../libraries/e2e/index.md#73132-e2e_p44protectinit) | 初始化保护状态。 |
| [**E2E_SMCheck**](../libraries/e2e/index.md#73151-e2e_smcheck) | 校验通信信道。 |
| [**E2E_SMCheckInit**](../libraries/e2e/index.md#73152-e2e_smcheckinit) | 初始化状态机。 |

## AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）（17）

来源：[AUTOSAR SPI Handler/Driver（SPI 处理器/驱动程序）](../communication/spi_handler_driver/index.md) · SWS_SPIHandlerDriver

| 函数 | 简述 |
|---|---|
| [**Spi_AsyncTransmit**](../communication/spi_handler_driver/index.md#734-spi_asynctransmit) | 此服务用于在 SPI 总线上传输数据。 |
| [**Spi_Cancel**](../communication/spi_handler_driver/index.md#7313-spi_cancel) | 此服务取消正在进行的指定序列传输。 |
| [**Spi_DeInit**](../communication/spi_handler_driver/index.md#732-spi_deinit) | 此服务用于 SPI 去初始化。 |
| [**Spi_GetHWUnitStatus**](../communication/spi_handler_driver/index.md#7312-spi_gethwunitstatus) | 此服务返回指定的 SPI 硬件微控制器外设的状态。 |
| [**Spi_GetJobResult**](../communication/spi_handler_driver/index.md#738-spi_getjobresult) | 此服务返回指定作业的上一次传输结果。 |
| [**Spi_GetSequenceResult**](../communication/spi_handler_driver/index.md#739-spi_getsequenceresult) | 此服务返回指定序列的上一次传输结果。 |
| [**Spi_GetStatus**](../communication/spi_handler_driver/index.md#737-spi_getstatus) | 此服务返回 SPI 处理器/驱动程序软件模块的状态。 |
| [**Spi_GetVersionInfo**](../communication/spi_handler_driver/index.md#7310-spi_getversioninfo) | 此服务返回本模块的版本信息。 |
| [**Spi_Init**](../communication/spi_handler_driver/index.md#731-spi_init) | 此服务用于初始化。 |
| [**Spi_JobEndNotification**](../communication/spi_handler_driver/index.md#7631-spi_jobendnotification) | 使用者为每个作业提供的回调例程，用于通知调用者某个作业已经完成。 |
| [**Spi_MainFunction_Handling**](../communication/spi_handler_driver/index.md#751-spi_mainfunction_handling) | -。 |
| [**Spi_ReadIB**](../communication/spi_handler_driver/index.md#735-spi_readib) | 此服务用于从参数指定的 IB SPI 处理器/驱动程序通道同步读取一个或多个数据。 |
| [**Spi_SeqEndNotification**](../communication/spi_handler_driver/index.md#7632-spi_seqendnotification) | 使用者为每个序列提供的回调例程，用于通知调用者某个序列已经完成。 |
| [**Spi_SetAsyncMode**](../communication/spi_handler_driver/index.md#7314-spi_setasyncmode) | 此服务用于为以异步方式处理的 SPI 总线设置异步机制模式。 |
| [**Spi_SetupEB**](../communication/spi_handler_driver/index.md#736-spi_setupeb) | 此服务用于为指定的 EB SPI 处理器/驱动程序通道设置缓冲区和数据长度。 |
| [**Spi_SyncTransmit**](../communication/spi_handler_driver/index.md#7311-spi_synctransmit) | 此服务用于在 SPI 总线上传输数据。 |
| [**Spi_WriteIB**](../communication/spi_handler_driver/index.md#733-spi_writeib) | 此服务用于向参数指定的 IB SPI 处理器/驱动程序通道写入一个或多个数据。 |

## AUTOSAR Standard Types（标准类型）（1）

来源：[AUTOSAR Standard Types（标准类型）](../general/standard_types/index.md) · SWS_StandardTypes

| 函数 | 简述 |
|---|---|
| [**NULL_PTR**](../general/standard_types/index.md#725-null_ptr) | — |

## AUTOSAR Synchronized Time-Base Manager（同步时基管理器）（60）

来源：[AUTOSAR Synchronized Time-Base Manager（同步时基管理器）](../globaltime/stbm/index.md) · SWS_SynchronizedTimeBaseManager

| 函数 | 简述 |
|---|---|
| [**FreshnessManagement**](../globaltime/stbm/index.md#7726-freshnessmanagement) | — |
| [**GetRxFreshnessFct**](../globaltime/stbm/index.md#7638-getrxfreshnessfct) | StbM 使用该接口查询当前的新鲜度值。 |
| [**GetTxFreshnessFct**](../globaltime/stbm/index.md#7637-gettxfreshnessfct) | 本 API 以大端格式从新鲜度（Freshness）数组第一个字节的最高有效位返回新鲜度值。 |
| [**GetTxFreshnessTruncDataFct**](../globaltime/stbm/index.md#7636-gettxfreshnesstruncdatafct) | StbM 使用该接口获取当前的新鲜度值。 |
| [**GlobalTime_Master**](../globaltime/stbm/index.md#7711-globaltime_master) | — |
| [**GlobalTime_Measurement**](../globaltime/stbm/index.md#7722-globaltime_measurement) | — |
| [**GlobalTime_Slave**](../globaltime/stbm/index.md#7712-globaltime_slave) | — |
| [**GlobalTime_StatusEvent**](../globaltime/stbm/index.md#7713-globaltime_statusevent) | — |
| [**GlobalTime_TimeEvent**](../globaltime/stbm/index.md#7721-globaltime_timeevent) | — |
| [**MeasurementNotification**](../globaltime/stbm/index.md#7745-measurementnotification) | — |
| [**OffsetTimeRecordBlockCallback**](../globaltime/stbm/index.md#7632-offsettimerecordblockcallback) | 提供属于偏移时基的测量数据表的已记录快照数据块。 |
| [**SPduTxConfirmationFct**](../globaltime/stbm/index.md#7635-spdutxconfirmationfct) | StbM 使用该接口指示受保护的时间同步报文已被发起传输。 |
| [**StartTimer**](../globaltime/stbm/index.md#7714-starttimer) | — |
| [**StatusNotification**](../globaltime/stbm/index.md#7731-statusnotification) | — |
| [**StatusNotificationCallback**](../globaltime/stbm/index.md#7633-statusnotificationcallback) | 当由通知掩码启用的与 &lt;TimeBase&gt; 相关的事件发生时，该回调通知客户。 |
| [**StbM_BusGetCurrentTime**](../globaltime/stbm/index.md#7313-stbm_busgetcurrenttime) | 返回时基的当前时间元组、状态和用户数据。 |
| [**StbM_BusSetGlobalTime**](../globaltime/stbm/index.md#7314-stbm_bussetglobaltime) | 允许时基提供者模块将接收时间元组转发给 StbM。 |
| [**StbM_CanSetMasterTimingData**](../globaltime/stbm/index.md#7329-stbm_cansetmastertimingdata) | 向 StbM 提供时基主节点的 CAN Timesync 模块特定数据。 |
| [**StbM_CanSetSlaveTimingData**](../globaltime/stbm/index.md#7326-stbm_cansetslavetimingdata) | 允许 CanTSyn 模块将 CAN 特定的细节转发给 StbM。 |
| [**StbM_CloneTimeBase**](../globaltime/stbm/index.md#7319-stbm_clonetimebase) | 将时基数据（当前时间、用户数据、速率校正）从源时基复制到目标时基。 |
| [**StbM_EthSetMasterTimingData**](../globaltime/stbm/index.md#7331-stbm_ethsetmastertimingdata) | 向 StbM 提供时基主节点的 Ethernet Timesync 模块特定数据。 |
| [**StbM_EthSetPdelayInitiatorData**](../globaltime/stbm/index.md#7332-stbm_ethsetpdelayinitiatordata) | 允许 EthTSyn 模块将 Pdelay 发起方特定的细节转发给 StbM。 |
| [**StbM_EthSetPdelayResponderData**](../globaltime/stbm/index.md#7333-stbm_ethsetpdelayresponderdata) | 允许 EthTSyn 模块将 Pdelay 响应方特定的细节转发给 StbM。 |
| [**StbM_EthSetSlaveTimingData**](../globaltime/stbm/index.md#7328-stbm_ethsetslavetimingdata) | 允许 EthTSyn 模块将 Ethernet 特定的细节转发给 StbM。 |
| [**StbM_FrSetMasterTimingData**](../globaltime/stbm/index.md#7330-stbm_frsetmastertimingdata) | 向 StbM 提供时基主节点的 FlexRay Timesync 模块特定数据。 |
| [**StbM_FrSetSlaveTimingData**](../globaltime/stbm/index.md#7327-stbm_frsetslavetimingdata) | 允许 FrTSyn 模块将 FlexRay 特定的细节转发给 StbM。 |
| [**StbM_GetBusProtocolParam**](../globaltime/stbm/index.md#7334-stbm_getbusprotocolparam) | 本 API 用于从接收到的 Follow_Up 报文获取总线特定的参数。 |
| [**StbM_GetCurrentSafeTime**](../globaltime/stbm/index.md#734-stbm_getcurrentsafetime) | 返回时间三元组（本地时间、备用本地时间、全局时间和时基状态）以及用户数据详情。 |
| [**StbM_GetCurrentTime**](../globaltime/stbm/index.md#733-stbm_getcurrenttime) | 返回时间元组（本地时间、全局时间和时基状态）以及用户数据详情。 |
| [**StbM_GetCurrentTimeExtended**](../globaltime/stbm/index.md#735-stbm_getcurrenttimeextended) | 以扩展格式返回时间值（从全局时基导出的本地时基）。 |
| [**StbM_GetCurrentVirtualLocalTime**](../globaltime/stbm/index.md#736-stbm_getcurrentvirtuallocaltime) | 返回被引用时基的虚拟本地时间。 |
| [**StbM_GetFallbackVirtualLocalTime**](../globaltime/stbm/index.md#737-stbm_getfallbackvirtuallocaltime) | 返回被引用时基的备用虚拟本地时间。 |
| [**StbM_GetMasterConfig**](../globaltime/stbm/index.md#7325-stbm_getmasterconfig) | 指示对于给定时基，系统范围主节点功能（例如 StbM_SetGlobalTime）是否可用。 |
| [**StbM_GetOffset**](../globaltime/stbm/index.md#7312-stbm_getoffset) | 允许 Timesync 模块获取当前的偏移时间和用户数据。 |
| [**StbM_GetOffsetTimeRecordHead**](../globaltime/stbm/index.md#7322-stbm_getoffsettimerecordhead) | 访问属于偏移时基的表的已记录快照数据头部。 |
| [**StbM_GetRateDeviation**](../globaltime/stbm/index.md#7315-stbm_getratedeviation) | 返回时基当前速率偏差的值。 |
| [**StbM_GetRxFreshness**](../globaltime/stbm/index.md#7339-stbm_getrxfreshness) | StbM 使用该接口查询当前的新鲜度值。 |
| [**StbM_GetSyncTimeRecordHead**](../globaltime/stbm/index.md#7321-stbm_getsynctimerecordhead) | 访问属于同步时基的表的已记录快照数据头部。 |
| [**StbM_GetTimeBaseStatus**](../globaltime/stbm/index.md#7318-stbm_gettimebasestatus) | 返回同步时基（或纯本地时基）的详细状态信息；如果针对偏移时基调用，则还返回该偏移时基及其底层同步时基的详细状态信息。 |
| [**StbM_GetTimeBaseUpdateCounter**](../globaltime/stbm/index.md#7324-stbm_gettimebaseupdatecounter) | 允许 Timesync 模块检测某时基是否应在随后的 &lt;Bus&gt;TSyn_MainFunction() 周期中立即发送。 |
| [**StbM_GetTimeLeap**](../globaltime/stbm/index.md#7317-stbm_gettimeleap) | 返回时间跳变的值。 |
| [**StbM_GetTxFreshness**](../globaltime/stbm/index.md#7336-stbm_gettxfreshness) | 本 API 以大端格式从新鲜度（Freshness）数组第一个字节的最高有效位返回新鲜度值。 |
| [**StbM_GetTxFreshnessTruncData**](../globaltime/stbm/index.md#7337-stbm_gettxfreshnesstruncdata) | StbM 使用该接口获取当前的新鲜度值。 |
| [**StbM_GetVersionInfo**](../globaltime/stbm/index.md#731-stbm_getversioninfo) | 返回本模块的版本信息。 |
| [**StbM_Init**](../globaltime/stbm/index.md#732-stbm_init) | 初始化同步时基管理器。 |
| [**StbM_MainFunction**](../globaltime/stbm/index.md#751-stbm_mainfunction) | 该函数将由 BSW 调度器提供的任务体周期性地调用。 |
| [**StbM_SetBusProtocolParam**](../globaltime/stbm/index.md#7335-stbm_setbusprotocolparam) | 本 API 用于设置时基主节点的总线特定参数。 |
| [**StbM_SetGlobalTime**](../globaltime/stbm/index.md#738-stbm_setglobaltime) | 允许客户设置对系统生效并将被发送到各总线的新全局时间。 |
| [**StbM_SetOffset**](../globaltime/stbm/index.md#7311-stbm_setoffset) | 允许客户和 Timesync 模块设置偏移时间和用户数据。 |
| [**StbM_SetRateCorrection**](../globaltime/stbm/index.md#7316-stbm_setratecorrection) | 允许设置同步时基（无论是否为纯本地时基）的速率。 |
| [**StbM_SetUserData**](../globaltime/stbm/index.md#7310-stbm_setuserdata) | 允许客户设置对系统生效并将被发送到各总线的新用户数据。 |
| [**StbM_SPduTxConfirmation**](../globaltime/stbm/index.md#7338-stbm_spdutxconfirmation) | StbM 使用该接口指示受保护的时间同步报文已被发起传输。 |
| [**StbM_StartTimer**](../globaltime/stbm/index.md#7320-stbm_starttimer) | 设置一个时间值，时基的值将与该值进行比较。 |
| [**StbM_TriggerTimeTransmission**](../globaltime/stbm/index.md#7323-stbm_triggertimetransmission) | 由 &lt;上层&gt; 调用，以强制 Timesync 模块由于 timeBaseUpdateCounter[timeBaseId] 已递增而再次发送当前时基。 |
| [**StbM_UpdateGlobalTime**](../globaltime/stbm/index.md#739-stbm_updateglobaltime) | 允许客户设置将被发送到各总线的全局时间。 |
| [**SyncTimeRecordBlockCallback**](../globaltime/stbm/index.md#7631-synctimerecordblockcallback) | 提供属于同步时基的测量数据表的已记录快照数据块。 |
| [**TimeBaseProviderNotification_Can**](../globaltime/stbm/index.md#7725-timebaseprovidernotification_can) | — |
| [**TimeBaseProviderNotification_Eth**](../globaltime/stbm/index.md#7723-timebaseprovidernotification_eth) | — |
| [**TimeBaseProviderNotification_Fr**](../globaltime/stbm/index.md#7724-timebaseprovidernotification_fr) | — |
| [**TimeNotification**](../globaltime/stbm/index.md#7744-timenotification) | — |

## AUTOSAR Time Service（时间服务）（20）

来源：[AUTOSAR Time Service（时间服务）](../system_services/time_service/index.md) · SWS_TimeService

| 函数 | 简述 |
|---|---|
| [**Tm_BusyWait1us16bit**](../system_services/time_service/index.md#736-tm_busywait1us16bit) | 通过以保证的最短等待时间轮询来执行繁忙等待。 |
| [**Tm_BusyWait1us24bit**](../system_services/time_service/index.md#7311-tm_busywait1us24bit) | 通过以保证的最短等待时间轮询来执行繁忙等待。 |
| [**Tm_BusyWait1us32bit**](../system_services/time_service/index.md#7316-tm_busywait1us32bit) | 通过以保证的最短等待时间轮询来执行繁忙等待。 |
| [**Tm_GetTimeSpan100us32bit**](../system_services/time_service/index.md#7318-tm_gettimespan100us32bit) | 提供时差（当前时间 - 参考时间）。 |
| [**Tm_GetTimeSpan1us16bit**](../system_services/time_service/index.md#733-tm_gettimespan1us16bit) | 提供时差（当前时间 - 参考时间）。 |
| [**Tm_GetTimeSpan1us24bit**](../system_services/time_service/index.md#738-tm_gettimespan1us24bit) | 提供时差（当前时间 - 参考时间）。 |
| [**Tm_GetTimeSpan1us32bit**](../system_services/time_service/index.md#7313-tm_gettimespan1us32bit) | 提供时差（当前时间 - 参考时间）。 |
| [**Tm_GetVersionInfo**](../system_services/time_service/index.md#731-tm_getversioninfo) | 返回此模块的版本信息。 |
| [**Tm_ResetTimer100us32bit**](../system_services/time_service/index.md#7317-tm_resettimer100us32bit) | 重置计时器实例（用户观点）。 |
| [**Tm_ResetTimer1us16bit**](../system_services/time_service/index.md#732-tm_resettimer1us16bit) | 重置计时器实例（用户观点）。 |
| [**Tm_ResetTimer1us24bit**](../system_services/time_service/index.md#737-tm_resettimer1us24bit) | 重置计时器实例（用户观点）。 |
| [**Tm_ResetTimer1us32bit**](../system_services/time_service/index.md#7312-tm_resettimer1us32bit) | 重置计时器实例（用户观点）。 |
| [**Tm_ShiftTimer100us32bit**](../system_services/time_service/index.md#7319-tm_shifttimer100us32bit) | 移动计时器实例的参考时间。 |
| [**Tm_ShiftTimer1us16bit**](../system_services/time_service/index.md#734-tm_shifttimer1us16bit) | 移动计时器实例的参考时间。 |
| [**Tm_ShiftTimer1us24bit**](../system_services/time_service/index.md#739-tm_shifttimer1us24bit) | 移动计时器实例的参考时间。 |
| [**Tm_ShiftTimer1us32bit**](../system_services/time_service/index.md#7314-tm_shifttimer1us32bit) | 移动计时器实例的参考时间。 |
| [**Tm_SyncTimer100us32bit**](../system_services/time_service/index.md#7320-tm_synctimer100us32bit) | 同步两个计时器实例。 |
| [**Tm_SyncTimer1us16bit**](../system_services/time_service/index.md#735-tm_synctimer1us16bit) | 同步两个计时器实例。 |
| [**Tm_SyncTimer1us24bit**](../system_services/time_service/index.md#7310-tm_synctimer1us24bit) | 同步两个计时器实例。 |
| [**Tm_SyncTimer1us32bit**](../system_services/time_service/index.md#7315-tm_synctimer1us32bit) | 同步两个计时器实例。 |

## AUTOSAR Time Synchronization over CAN（CAN 时间同步）（8）

来源：[AUTOSAR Time Synchronization over CAN（CAN 时间同步）](../globaltime/can_tsyn/index.md) · SWS_TimeSyncOverCAN

| 函数 | 简述 |
|---|---|
| [**CanTSyn_GetVersionInfo**](../globaltime/can_tsyn/index.md#732-cantsyn_getversioninfo) | 返回本模块的版本信息。 |
| [**CanTSyn_IcvGenerationIndication**](../globaltime/can_tsyn/index.md#743-cantsyn_icvgenerationindication) | 通过该 API 服务，CanTSyn 获得 ICV 生成的指示和结果。 |
| [**CanTSyn_IcvVerificationIndication**](../globaltime/can_tsyn/index.md#744-cantsyn_icvverificationindication) | 通过该 API 服务，CanTSyn 获得 ICV 验证的指示和结果。 |
| [**CanTSyn_Init**](../globaltime/can_tsyn/index.md#731-cantsyn_init) | 该函数初始化 CAN 时间同步。 |
| [**CanTSyn_MainFunction**](../globaltime/can_tsyn/index.md#751-cantsyn_mainfunction) | 用于周期性调用 / 相应 Timesync 报文发送的主函数。 |
| [**CanTSyn_RxIndication**](../globaltime/can_tsyn/index.md#741-cantsyn_rxindication) | 从下层通信接口模块接收 PDU 的指示。 |
| [**CanTSyn_SetTransmissionMode**](../globaltime/can_tsyn/index.md#733-cantsyn_settransmissionmode) | 本 API 用于打开和关闭 CanTSyn 的 TX 能力。 |
| [**CanTSyn_TxConfirmation**](../globaltime/can_tsyn/index.md#742-cantsyn_txconfirmation) | 下层通信接口模块确认一个 PDU 的发送，或 PDU 发送的失败。 |

## AUTOSAR Time Synchronization over Ethernet（以太网时间同步）（11）

来源：[AUTOSAR Time Synchronization over Ethernet（以太网时间同步）](../globaltime/eth_tsyn/index.md) · SWS_TimeSyncOverEthernet

| 函数 | 简述 |
|---|---|
| [**EthTSyn_GetProtocolParam**](../globaltime/eth_tsyn/index.md#735-ethtsyn_getprotocolparam) | 本 API 用于从接收到的 Follow_Up 报文读取 FollowUp 信息 TLV 参数。 |
| [**EthTSyn_GetVersionInfo**](../globaltime/eth_tsyn/index.md#732-ethtsyn_getversioninfo) | 返回本模块的版本信息。 |
| [**EthTSyn_IcvGenerationIndication**](../globaltime/eth_tsyn/index.md#744-ethtsyn_icvgenerationindication) | 通过该 API 服务，EthTSyn 获得 ICV 生成的指示和结果。 |
| [**EthTSyn_IcvVerificationIndication**](../globaltime/eth_tsyn/index.md#745-ethtsyn_icvverificationindication) | 通过该 API 服务，EthTSyn 获得 ICV 验证的指示和结果。 |
| [**EthTSyn_Init**](../globaltime/eth_tsyn/index.md#731-ethtsyn_init) | 该函数初始化 Ethernet 时间同步。 |
| [**EthTSyn_MainFunction**](../globaltime/eth_tsyn/index.md#751-ethtsyn_mainfunction) | 用于周期性调用 / 相应 Sync、Follow_Up 和 Pdelay_Req 发送的主函数。 |
| [**EthTSyn_RxIndication**](../globaltime/eth_tsyn/index.md#741-ethtsyn_rxindication) | 通过该 API 服务，EthTSyn 获得接收帧的指示和数据。 |
| [**EthTSyn_SetProtocolParam**](../globaltime/eth_tsyn/index.md#734-ethtsyn_setprotocolparam) | 本 API 用于在发送之前设置 Follow_Up 报文的 FollowUp 信息 TLV 参数。 |
| [**EthTSyn_SetTransmissionMode**](../globaltime/eth_tsyn/index.md#733-ethtsyn_settransmissionmode) | 本 API 用于打开和关闭 EthTSyn 的 TX 能力。 |
| [**EthTSyn_TrcvLinkStateChg**](../globaltime/eth_tsyn/index.md#743-ethtsyn_trcvlinkstatechg) | 允许在意外链路丢失的情况下复位状态机，以避免不一致的 Sync 和 Follow_Up 序列。 |
| [**EthTSyn_TxConfirmation**](../globaltime/eth_tsyn/index.md#742-ethtsyn_txconfirmation) | 确认一个以太网帧的发送。 |

## AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）（8）

来源：[AUTOSAR Time Synchronization over FlexRay（FlexRay 时间同步）](../globaltime/fr_tsyn/index.md) · SWS_TimeSyncOverFlexRay

| 函数 | 简述 |
|---|---|
| [**FrTSyn_GetVersionInfo**](../globaltime/fr_tsyn/index.md#732-frtsyn_getversioninfo) | 返回本模块的版本信息。 |
| [**FrTSyn_IcvGenerationIndication**](../globaltime/fr_tsyn/index.md#743-frtsyn_icvgenerationindication) | 该 API 服务向 FrTSyn 提供 ICV 生成的指示及结果。 |
| [**FrTSyn_IcvVerificationIndication**](../globaltime/fr_tsyn/index.md#744-frtsyn_icvverificationindication) | 该 API 服务向 FrTSyn 提供 ICV 验证的指示及结果。 |
| [**FrTSyn_Init**](../globaltime/fr_tsyn/index.md#731-frtsyn_init) | 初始化 FlexRay 时间同步。 |
| [**FrTSyn_MainFunction**](../globaltime/fr_tsyn/index.md#751-frtsyn_mainfunction) | 用于周期性调用和/或发送时间同步报文的主函数。 |
| [**FrTSyn_RxIndication**](../globaltime/fr_tsyn/index.md#741-frtsyn_rxindication) | 指示从下层通信接口模块接收到 PDU。 |
| [**FrTSyn_SetTransmissionMode**](../globaltime/fr_tsyn/index.md#733-frtsyn_settransmissionmode) | 本 API 用于启用和禁用 FrTSyn 的 TX 能力。 |
| [**FrTSyn_TriggerTransmit**](../globaltime/fr_tsyn/index.md#742-frtsyn_triggertransmit) | 在此 API 中，上层模块（称为调用模块）应检查可用数据是否适合 PduInfoPtr->SduLength 所报告的缓冲区大小。 |

## AUTOSAR TTCAN Driver（TTCAN 驱动程序）（19）

来源：[AUTOSAR TTCAN Driver（TTCAN 驱动程序）](../communication/ttcan_driver/index.md) · SWS_TTCANDriver

| 函数 | 简述 |
|---|---|
| [**Can_TTAckTimeMark**](../communication/ttcan_driver/index.md#744-can_ttacktimemark) | — |
| [**Can_TTCancelTimeMark**](../communication/ttcan_driver/index.md#743-can_ttcanceltimemark) | — |
| [**Can_TTDisableTimeMarkIRQ**](../communication/ttcan_driver/index.md#746-can_ttdisabletimemarkirq) | — |
| [**Can_TTEnableTimeMarkIRQ**](../communication/ttcan_driver/index.md#745-can_ttenabletimemarkirq) | — |
| [**Can_TTGetControllerTime**](../communication/ttcan_driver/index.md#731-can_ttgetcontrollertime) | — |
| [**Can_TTGetErrorLevel**](../communication/ttcan_driver/index.md#734-can_ttgeterrorlevel) | — |
| [**Can_TTGetMasterState**](../communication/ttcan_driver/index.md#732-can_ttgetmasterstate) | — |
| [**Can_TTGetNTUActual**](../communication/ttcan_driver/index.md#733-can_ttgetntuactual) | — |
| [**Can_TTGetSyncQuality**](../communication/ttcan_driver/index.md#741-can_ttgetsyncquality) | — |
| [**Can_TTGetTimeMarkIRQStatus**](../communication/ttcan_driver/index.md#747-can_ttgettimemarkirqstatus) | — |
| [**Can_TTGlobalTimePreset**](../communication/ttcan_driver/index.md#738-can_ttglobaltimepreset) | — |
| [**Can_TTMainFunction_IRQ**](../communication/ttcan_driver/index.md#751-can_ttmainfunction_irq) | — |
| [**Can_TTReceive**](../communication/ttcan_driver/index.md#748-can_ttreceive) | — |
| [**Can_TTSetEndOfGap**](../communication/ttcan_driver/index.md#736-can_ttsetendofgap) | — |
| [**Can_TTSetExtClockSyncCommand**](../communication/ttcan_driver/index.md#739-can_ttsetextclocksynccommand) | — |
| [**Can_TTSetNextIsGap**](../communication/ttcan_driver/index.md#735-can_ttsetnextisgap) | — |
| [**Can_TTSetNTUAdjust**](../communication/ttcan_driver/index.md#7310-can_ttsetntuadjust) | — |
| [**Can_TTSetTimeCommand**](../communication/ttcan_driver/index.md#737-can_ttsettimecommand) | — |
| [**Can_TTSetTimeMark**](../communication/ttcan_driver/index.md#742-can_ttsettimemark) | — |

## AUTOSAR TTCAN Interface（TTCAN 接口）（24）

来源：[AUTOSAR TTCAN Interface（TTCAN 接口）](../communication/ttcan_interface/index.md) · SWS_TTCANInterface

| 函数 | 简述 |
|---|---|
| [**CanIf_TTAckTimeMark**](../communication/ttcan_interface/index.md#745-canif_ttacktimemark) | — |
| [**CanIf_TTApplWatchdogError**](../communication/ttcan_interface/index.md#761-canif_ttapplwatchdogerror) | — |
| [**CanIf_TTCancelTimeMark**](../communication/ttcan_interface/index.md#744-canif_ttcanceltimemark) | — |
| [**CanIf_TTDisableTimeMarkIRQ**](../communication/ttcan_interface/index.md#747-canif_ttdisabletimemarkirq) | — |
| [**CanIf_TTEnableTimeMarkIRQ**](../communication/ttcan_interface/index.md#746-canif_ttenabletimemarkirq) | — |
| [**CanIf_TTGap**](../communication/ttcan_interface/index.md#764-canif_ttgap) | — |
| [**CanIf_TTGetControllerTime**](../communication/ttcan_interface/index.md#731-canif_ttgetcontrollertime) | — |
| [**CanIf_TTGetErrorLevel**](../communication/ttcan_interface/index.md#734-canif_ttgeterrorlevel) | — |
| [**CanIf_TTGetMasterState**](../communication/ttcan_interface/index.md#732-canif_ttgetmasterstate) | — |
| [**CanIf_TTGetNTUActual**](../communication/ttcan_interface/index.md#733-canif_ttgetntuactual) | — |
| [**CanIf_TTGetSyncQuality**](../communication/ttcan_interface/index.md#742-canif_ttgetsyncquality) | — |
| [**CanIf_TTGetTimeMarkIRQStatus**](../communication/ttcan_interface/index.md#748-canif_ttgettimemarkirqstatus) | — |
| [**CanIf_TTGlobalTimePreset**](../communication/ttcan_interface/index.md#738-canif_ttglobaltimepreset) | — |
| [**CanIf_TTMasterStateChange**](../communication/ttcan_interface/index.md#767-canif_ttmasterstatechange) | — |
| [**CanIf_TTSetEndOfGap**](../communication/ttcan_interface/index.md#736-canif_ttsetendofgap) | — |
| [**CanIf_TTSetExtClockSyncCommand**](../communication/ttcan_interface/index.md#739-canif_ttsetextclocksynccommand) | — |
| [**CanIf_TTSetNextIsGap**](../communication/ttcan_interface/index.md#735-canif_ttsetnextisgap) | — |
| [**CanIf_TTSetNTUAdjust**](../communication/ttcan_interface/index.md#7310-canif_ttsetntuadjust) | — |
| [**CanIf_TTSetTimeCommand**](../communication/ttcan_interface/index.md#737-canif_ttsettimecommand) | — |
| [**CanIf_TTSetTimeMark**](../communication/ttcan_interface/index.md#743-canif_ttsettimemark) | — |
| [**CanIf_TTSevereError**](../communication/ttcan_interface/index.md#763-canif_ttsevereerror) | — |
| [**CanIf_TTStartOfCycle**](../communication/ttcan_interface/index.md#765-canif_ttstartofcycle) | — |
| [**CanIf_TTTimeDisc**](../communication/ttcan_interface/index.md#766-canif_tttimedisc) | — |
| [**CanIf_TTTimingError**](../communication/ttcan_interface/index.md#762-canif_tttimingerror) | — |

## AUTOSAR UdpNm (UDP Network Management)（25）

来源：[AUTOSAR UdpNm (UDP Network Management)](../communication/udp_network_management/index.md) · SWS_UDPNetworkManagement

| 函数 | 简述 |
|---|---|
| [**UdpNm_ActivateTxPnShutdownMsg**](../communication/udp_network_management/index.md#7320-udpnm_activatetxpnshutdownmsg) | NM指示激活给定NM通道上PN关闭消息的传输。 |
| [**UdpNm_CheckRemoteSleepIndication**](../communication/udp_network_management/index.md#7316-udpnm_checkremotesleepindication) | 检查远程睡眠指示是否发生。 |
| [**UdpNm_DeactivateTxPnShutdownMsg**](../communication/udp_network_management/index.md#7321-udpnm_deactivatetxpnshutdownmsg) | NM指示停用给定NM通道上PN关闭消息的传输。 |
| [**UdpNm_DisableCommunication**](../communication/udp_network_management/index.md#735-udpnm_disablecommunication) | 由于 ISO14229 通信控制（0x28）服务而禁用 NM PDU 传输能力。 |
| [**UdpNm_EnableCommunication**](../communication/udp_network_management/index.md#736-udpnm_enablecommunication) | 由于 ISO14229 通信控制（0x28）服务而启用 NM PDU 传输能力。 |
| [**UdpNm_GetLocalNodeIdentifier**](../communication/udp_network_management/index.md#7310-udpnm_getlocalnodeidentifier) | 获取为本地节点（local node）配置的节点标识符。 |
| [**UdpNm_GetNodeIdentifier**](../communication/udp_network_management/index.md#739-udpnm_getnodeidentifier) | 从最近收到的 NM PDU 中获取节点标识符。 |
| [**UdpNm_GetPduData**](../communication/udp_network_management/index.md#7312-udpnm_getpdudata) | 从最近收到的 NM 消息中获取整个 PDU 数据。 |
| [**UdpNm_GetState**](../communication/udp_network_management/index.md#7313-udpnm_getstate) | 返回网络管理的状态和模式。 |
| [**UdpNm_GetUserData**](../communication/udp_network_management/index.md#738-udpnm_getuserdata) | 从最近收到的 NM 消息（NM messages）中获取用户数据。 |
| [**UdpNm_GetVersionInfo**](../communication/udp_network_management/index.md#7314-udpnm_getversioninfo) | 该服务返回该模块的版本信息。 |
| [**UdpNm_Init**](../communication/udp_network_management/index.md#731-udpnm_init) | 初始化完整的 UdpNm 模块，即：配置时激活的所有通道都被初始化。 |
| [**UdpNm_NetworkRelease**](../communication/udp_network_management/index.md#734-udpnm_networkrelease) | 释放网络，因为ECU不必在总线上通信。 |
| [**UdpNm_NetworkRequest**](../communication/udp_network_management/index.md#733-udpnm_networkrequest) | 请求网络，因为ECU需要在总线上通信。 |
| [**UdpNm_PassiveStartUp**](../communication/udp_network_management/index.md#732-udpnm_passivestartup) | AUTOSAR UdpNm的被动启动。 |
| [**UdpNm_PnLearningRequest**](../communication/udp_network_management/index.md#7319-udpnm_pnlearningrequest) | 为总线上接下来传输的NM消息设置重复消息请求位和部分网络学习位。 |
| [**UdpNm_RepeatMessageIndication**](../communication/udp_network_management/index.md#7322-udpnm_repeatmessageindication) | 指示已接收到设置了重复消息请求位的NM消息的服务。 |
| [**UdpNm_RepeatMessageRequest**](../communication/udp_network_management/index.md#7311-udpnm_repeatmessagerequest) | 在此函数无错误返回后，为总线上传输的所有NM消息设置重复消息请求位（Repeat Message Request Bit）。 |
| [**UdpNm_RequestBusSynchronization**](../communication/udp_network_management/index.md#7315-udpnm_requestbussynchronization) | 请求总线同步。 |
| [**UdpNm_SetSleepReadyBit**](../communication/udp_network_management/index.md#7317-udpnm_setsleepreadybit) | 设置控制位向量（CBV）中的 NM 协调器睡眠就绪位。 |
| [**UdpNm_SetUserData**](../communication/udp_network_management/index.md#737-udpnm_setuserdata) | 在此函数无错误返回后，为总线上传输的所有 NM 消息（NM messages）设置用户数据。 |
| [**UdpNm_SoAdIfRxIndication**](../communication/udp_network_management/index.md#742-udpnm_soadifrxindication) | 指示从较低层通信接口模块接收到的 PDU。 |
| [**UdpNm_SoAdIfTriggerTransmit**](../communication/udp_network_management/index.md#743-udpnm_soadiftriggertransmit) | 在此API中，上层模块将检查可用数据是否适合PduInfoPtr->SduLength报告的缓冲区大小。 |
| [**UdpNm_SoAdIfTxConfirmation**](../communication/udp_network_management/index.md#741-udpnm_soadiftxconfirmation) | 下层通信接口模块确认PDU的传输，或者PDU的传输失败。 |
| [**UdpNm_Transmit**](../communication/udp_network_management/index.md#7318-udpnm_transmit) | 请求传输 PDU。 |

## AUTOSAR Watchdog Driver（看门狗驱动）（4）

来源：[AUTOSAR Watchdog Driver（看门狗驱动）](../safety/watchdog_driver/index.md) · SWS_WatchdogDriver

| 函数 | 简述 |
|---|---|
| [**Wdg_GetVersionInfo**](../safety/watchdog_driver/index.md#734-wdg_getversioninfo) | 此服务返回该模块的版本信息。 |
| [**Wdg_Init**](../safety/watchdog_driver/index.md#731-wdg_init) | 此服务初始化模块。 |
| [**Wdg_SetMode**](../safety/watchdog_driver/index.md#732-wdg_setmode) | 此服务将看门狗切换到模式 Mode。 |
| [**Wdg_SetTriggerCondition**](../safety/watchdog_driver/index.md#733-wdg_settriggercondition) | 此服务为触发计数器设置超时值。 |

## AUTOSAR Watchdog Interface（看门狗接口）（3）

来源：[AUTOSAR Watchdog Interface（看门狗接口）](../safety/watchdog_interface/index.md) · SWS_WatchdogInterface

| 函数 | 简述 |
|---|---|
| [**WdgIf_GetVersionInfo**](../safety/watchdog_interface/index.md#733-wdgif_getversioninfo) | 此服务返回版本信息。 |
| [**WdgIf_SetMode**](../safety/watchdog_interface/index.md#731-wdgif_setmode) | 此服务将服务 WdgIf_SetMode 映射到相应看门狗驱动的服务 Wdg_SetMode。 |
| [**WdgIf_SetTriggerCondition**](../safety/watchdog_interface/index.md#732-wdgif_settriggercondition) | 此服务将服务 WdgIf_SetTriggerCondition 映射到相应看门狗驱动的服务 Wdg_SetTriggerCondition。 |

## AUTOSAR Watchdog Manager（看门狗管理器）（11）

来源：[AUTOSAR Watchdog Manager（看门狗管理器）](../safety/watchdog_manager/index.md) · SWS_WatchdogManager

| 函数 | 简述 |
|---|---|
| [**WdgM_CheckpointReached**](../safety/watchdog_manager/index.md#736-wdgm_checkpointreached) | 此服务向看门狗管理器指示已到达被监督实体内的某个检查点。 |
| [**WdgM_DeInit**](../safety/watchdog_manager/index.md#732-wdgm_deinit) | 此服务去初始化看门狗管理器。 |
| [**WdgM_GetFirstExpiredSEID**](../safety/watchdog_manager/index.md#7310-wdgm_getfirstexpiredseid) | 此服务返回首个达到 WDGM_LOCAL_STATUS_EXPIRED 状态的 SEID。 |
| [**WdgM_GetGlobalStatus**](../safety/watchdog_manager/index.md#738-wdgm_getglobalstatus) | 此服务返回看门狗管理器的全局监督状态。 |
| [**WdgM_GetLocalStatus**](../safety/watchdog_manager/index.md#737-wdgm_getlocalstatus) | 此服务返回单个被监督实体的监督状态。 |
| [**WdgM_GetMode**](../safety/watchdog_manager/index.md#735-wdgm_getmode) | 此服务返回看门狗管理器的当前模式。 |
| [**WdgM_GetVersionInfo**](../safety/watchdog_manager/index.md#733-wdgm_getversioninfo) | 此服务返回本模块的版本信息。 |
| [**WdgM_Init**](../safety/watchdog_manager/index.md#731-wdgm_init) | 此服务初始化看门狗管理器。 |
| [**WdgM_MainFunction**](../safety/watchdog_manager/index.md#741-wdgm_mainfunction) | 此服务执行看门狗管理器周期性作业的处理。 |
| [**WdgM_PerformReset**](../safety/watchdog_manager/index.md#739-wdgm_performreset) | 此服务指示看门狗管理器产生看门狗复位。 |
| [**WdgM_SetMode**](../safety/watchdog_manager/index.md#734-wdgm_setmode) | 此服务设置看门狗管理器的当前模式。 |

## AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）（20）

来源：[AUTOSAR Wireless Ethernet Driver（无线以太网驱动程序）](../communication/wlan_driver/index.md) · SWS_WirelessEthernetDriver

| 函数 | 简述 |
|---|---|
| [**WEth_GetBufWRxParams**](../communication/wlan_driver/index.md#7315-weth_getbufwrxparams) | 为一个已接收的包读出与接收方向相关的取值。 |
| [**WEth_GetBufWTxParams**](../communication/wlan_driver/index.md#7316-weth_getbufwtxparams) | 为一个已发送的包读出与发送方向相关的取值。 |
| [**WEth_GetControllerMode**](../communication/wlan_driver/index.md#733-weth_getcontrollermode) | 获取被索引控制器的状态。 |
| [**WEth_GetPhysAddr**](../communication/wlan_driver/index.md#734-weth_getphysaddr) | 获取被索引控制器所使用的物理源地址。 |
| [**WEth_GetVersionInfo**](../communication/wlan_driver/index.md#7318-weth_getversioninfo) | 返回本模块的版本信息。 |
| [**WEth_GetWEtherStats32**](../communication/wlan_driver/index.md#7311-weth_getwetherstats32) | 返回依据 IEEE 802.11-2012 的以下列表，其中最大可能取值应表示无效值，例如该计数器不可用时：1. dot11STAStatisticsTransmittedFragmentCount；2. dot11STAStatis… |
| [**WEth_GetWEtherStats64**](../communication/wlan_driver/index.md#7312-weth_getwetherstats64) | 返回依据 IEEE 802.11-2012 的以下列表，其中最大可能取值应表示无效值，例如该计数器不可用时：1. dot11STAStatisticsTransmittedOctetsInAMSDUCount；2. dot11STAS… |
| [**WEth_Init**](../communication/wlan_driver/index.md#731-weth_init) | 初始化 Wireless Ethernet Driver。 |
| [**WEth_MainFunction**](../communication/wlan_driver/index.md#751-weth_mainfunction) | 支持间接发送（扩展的帧时序约束）以及使用多个信道时的信道选择机制。 |
| [**WEth_ProvideTxBuffer**](../communication/wlan_driver/index.md#737-weth_providetxbuffer) | 提供对指定控制器的发送缓冲区的访问。 |
| [**WEth_ReadTrcvRegs**](../communication/wlan_driver/index.md#7314-weth_readtrcvregs) | 读取一个收发器寄存器。 |
| [**WEth_Receive**](../communication/wlan_driver/index.md#7310-weth_receive) | 触发帧接收。 |
| [**WEth_SetBufWTxParams**](../communication/wlan_driver/index.md#7317-weth_setbufwtxparams) | 为一个特定缓冲区（待发送的包）设置与发送方向相关的取值。 |
| [**WEth_SetControllerMode**](../communication/wlan_driver/index.md#732-weth_setcontrollermode) | 启用/禁用被索引的控制器。 |
| [**WEth_SetPhysAddr**](../communication/wlan_driver/index.md#735-weth_setphysaddr) | 设置被索引控制器所使用的物理源地址。 |
| [**WEth_Transmit**](../communication/wlan_driver/index.md#738-weth_transmit) | 触发发送一个先前已填充的发送缓冲区。 |
| [**WEth_TriggerPriorityQueueTransmit**](../communication/wlan_driver/index.md#7319-weth_triggerpriorityqueuetransmit) | 触发发送一个在软件优先级队列中等待的、先前已填充的发送缓冲区。 |
| [**WEth_TxConfirmation**](../communication/wlan_driver/index.md#739-weth_txconfirmation) | 触发帧发送确认。 |
| [**WEth_UpdatePhysAddrFilter**](../communication/wlan_driver/index.md#736-weth_updatephysaddrfilter) | 向被索引上下文的过滤器中添加物理地址，或从中移除物理地址。 |
| [**WEth_WriteTrcvRegs**](../communication/wlan_driver/index.md#7313-weth_writetrcvregs) | 配置收发器的寄存器，或触发接收器提供的功能。 |

## AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）（10）

来源：[AUTOSAR Wireless Ethernet Transceiver Driver（无线以太网收发器驱动程序）](../communication/wlan_transceiver_driver/index.md) · SWS_WirelessEthernetTransceiverDriver

| 函数 | 简述 |
|---|---|
| [**WEthTrcv_GetChanRxParams**](../communication/wlan_transceiver_driver/index.md#738-wethtrcv_getchanrxparams) | 读取与收发器接收方向相关的取值。 |
| [**WEthTrcv_GetLinkState**](../communication/wlan_transceiver_driver/index.md#734-wethtrcv_getlinkstate) | 获取被索引收发器的链路状态。 |
| [**WEthTrcv_GetTransceiverMode**](../communication/wlan_transceiver_driver/index.md#733-wethtrcv_gettransceivermode) | 获取被索引收发器的状态。 |
| [**WEthTrcv_GetVersionInfo**](../communication/wlan_transceiver_driver/index.md#739-wethtrcv_getversioninfo) | 返回本模块的版本信息。 |
| [**WEthTrcv_Init**](../communication/wlan_transceiver_driver/index.md#731-wethtrcv_init) | 初始化 Wireless Ethernet Transceiver Driver。 |
| [**WEthTrcv_MainFunction**](../communication/wlan_transceiver_driver/index.md#751-wethtrcv_mainfunction) | 用于轮询状态变化。 |
| [**WEthTrcv_SetChanRxParams**](../communication/wlan_transceiver_driver/index.md#736-wethtrcv_setchanrxparams) | 设置与收发器无线信道的接收方向相关的取值。 |
| [**WEthTrcv_SetChanTxParams**](../communication/wlan_transceiver_driver/index.md#737-wethtrcv_setchantxparams) | 设置与收发器无线信道的发送方向相关的取值。 |
| [**WEthTrcv_SetRadioParams**](../communication/wlan_transceiver_driver/index.md#735-wethtrcv_setradioparams) | 设置与收发器的无线射频相关的取值。 |
| [**WEthTrcv_SetTransceiverMode**](../communication/wlan_transceiver_driver/index.md#732-wethtrcv_settransceivermode) | 启用/禁用被索引的收发器。 |

## AUTOSAR XCP（通用测量与校准协议）（4）

来源：[AUTOSAR XCP（通用测量与校准协议）](../communication/xcp/index.md) · SWS_XCP

| 函数 | 简述 |
|---|---|
| [**Xcp_GetVersionInfo**](../communication/xcp/index.md#732-xcp_getversioninfo) | 返回本模块的版本信息。 |
| [**Xcp_Init**](../communication/xcp/index.md#731-xcp_init) | 此服务初始化 AUTOSAR XCP 层的接口和变量。 |
| [**Xcp_MainFunction**](../communication/xcp/index.md#751-xcp_mainfunction) | XCP 模块的调度函数。 |
| [**Xcp_SetTransmissionMode**](../communication/xcp/index.md#733-xcp_settransmissionmode) | 此 API 用于在 XCP 模块中开启和关闭所用通信总线通道的 TX 能力。 |
