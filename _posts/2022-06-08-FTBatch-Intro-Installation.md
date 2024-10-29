---                
layout: post            
title: "FactoryTalk Batch简介，组成和安装"                
date:   2022-6-8 12:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

对FactoryTalk Batch所知甚少，需要花一些时间去了解这个产品。今后可能会开一个系列的文章介绍FTBatch这个产品，主要参考FTBatch的用户手册，目前手册只有英文版，我尽量把它写成中文版，边学边记录，虽然多花些时间，但能对产品有更深的理解。  

# 什么是Batch

        Generally, a batch process is defined as “a process that leads to the production of finite quantities of material 
        by subjecting quantities of input materials to an ordered set of processing activities over a finite period of time 
        using one or more pieces of equipment” (Instrument Society of America 1995)

一般来说，批处理被定义为“通过使用一台或多台设备在有限的时间内对一定数量的输入材料进行一系列有序的处理活动，从而生产出有限数量的产品的过程”. 批处理被用在各种各样的行业里，比如食品、饮料、制药、化工等等。  

# 什么是ISA S88

S88是ANSI/ISA-88的简写，它为批次控制系统的设计和规范提供指南。是专门针对⼴泛应⽤于流程⼯业中的批量控制系统的设计和规范。它不是一个软件的标准，它同样适用于手动流程。它于 1995 年获得ISA批准并于 2010 年更新。其原始版本于 1997 年被 IEC 采用为 IEC 61512-1。  
S88 的目的是：  
1. 定义特定于批次控制系统的术语，以促进制造商和用户之间的理解。  
2. 提供标准的数据结构批处理控制语言，以简化系统各个组件之间的编程、配置任务和通信。    
3. 为批处理系统提供标准数据结构，这将简化系统架构内的数据通信任务。    
4. 确定物理模型和功能模型的标准架构。  
   
S88 为批处理控制提供了一套一致的标准和术语，并定义了物理模型(physical model)、程序(procedures)和配方(recipes)。  

该标准定义了一个过程模型(process model)，该模型由一个过程(process)组成，该过程由一组有序的过程阶段(process stages)组成，这些阶段由一组有序的过程操作(process operations)组成，这些过程操作由一组有序的过程动作(process actions)组成。  

物理模型从企业(enterprise)开始，该企业可能包含一个站点(site)，该站点可能包含  含有过程单元(process cells)的区域(areas)，过程单元必须包含一个单元(unit)，该单元可能包含  含有控制模块(control modules)的设备模块(equipment modules)。  

程序控制模型(procedural control model)由配方程序(recipes procedures)组成，这些程序由一组有序的单元程序(unit procedures)组成，这些单元程序由一组有序的操作(operations)组成，这些操作由一组有序的阶段(phases)组成。  

配方可以有以下类型：一般、站点、主控、控制(general, site, master, control)。配方内容包括：表头、配方、设备要求、程序等制作配方所需的信息(header, formula, equipment requirements)。  

有关S88的其他详细信息，需要深入研究之后再补充。<font color="red">挖个坑</font>  

# FTBatch
以下是官方介绍的直翻：  

作为 FactoryTalk 系列的一部分，FactoryTalk Batch 组件通过提供优化制造所需的可见性、控制和报告来提高工厂的整体效率。通过协调执行，您可以减少废品和返工并提高产品质量和一致性。通过设备利用率的实时管理，您可以最大限度地提高资产回报率。通过实施优化的配方和程序，您可以提高工厂产能。通过使用电子化、无纸化操作，您可以提高生产力。您还可以通过使用电子批记录实施、无纸化制造和质量签核来降低合规成本。通过减轻制造方面的合规负担，您可以降低库存水平和周期时间，从而大大改善客户服务。
FactoryTalk Batch 组件可帮助您优化车间操作，让您快速获得净资产回报。新产品定义迅速部署到制造中。生产订单信息准确。业务和工厂级控制系统紧密协调，多个站点作为一个团队运行。 FactoryTalk Batch 组件是一组开放的、可配置的产品，可帮助您定义、管理、监控和控制本地、远程或承包商工厂的制造。您可以在任何需要的地方部署任何 FactoryTalk Batch 组件，一次一个或一次全部部署，以提高生产力和工厂控制。  

# FTBatch的组成部分
FTBatch 包括以下组件：   

| 组件 | 说明 |
| --- | ----------- |
| FactoryTalk Batch Server |是运行FT Batch的引擎。它是控制系统信息、阶段(phases)和配方的组件。是一个Windows服务|   
| FactoryTalk Batch Recipe Editor |以图形方式创建和配置配方,指定阶段的顺序(phases sequence),高阶功能包括配方的批准，配方的版本控制等等|   
| FactoryTalk Batch Equipment Editor |以图形的方式定义和维护Process中的各种设备|   
| FactoryTalk Batch View |操作员启动配方和执行程序的界面，显示正在运行的Batch并用图形的方式展示相关数据|   
| FactoryTalk Batch View HMI Controls | Batch View的HMI 版， Batch View是需要license收费的，HMI 直接运行在FactoryTalk View里，免费的|   
| FactoryTalk Event Archiver |是一个Windows服务，用于将Batch Server传送来的事件进行归档。事件会被写入SQL数据库。可以使用SQL Server Reporting Services以 HTML报告形式查看存储在数据库中的事件|   
| FactoryTalk Batch Network Editor |FTBatch是分布式系统，可以将组件部署在网络中的不同位置。Network Editor用于指定FT Batch Server 和FT Batch Material Server在网络上的位置|   
| FactoryTalk eProcedure | 分Client和Server，Client允许操作员在IE上运行批处理配方，Server则是用来提供相应的HTML指令服务|  
| FactoryTalk Batch Enterprise Integration Server |  openapi指令接口，提供一些指令来获取Batch信息 |
| FactoryTalk Batch Material Manager |用于跟踪批处理配方中的材料消耗,分Server和Editor，Server提供SQL数据库以及和FT Batch Server之间的通信， Editor提供界面帮助用户创建管理物料数据库|    

下图是FTBatch的一个典型部署结构：  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/Batch_install_structure.png?raw=true)

# FTBatch安装
以Batch v14.0为例，Batch的默认安装组件如下  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/Batch_install1.png?raw=true)  
Batch View Server会自动跟着Batch Server组件一起安装，Batch View Web Client不需要额外的安装，View Server装完之后自带View web client   
子组件展开之后：  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/Batch_install2.png?raw=true)

Batch Server安装需要将以下服务改成Auto执行

        Remote Registry

Batch Material Manager 需要激活以下windows组件：

        Message Queuing

eProcedure Server 需要激活以下IIS 组件：
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/Batch_install3.png?raw=true)  

以下组件需要用到SQL Server：  

        Batch Server（以RDB格式存储配方）  
        Event Archiver（归档batch事件记录，生成report）  
        Material Manager Server(存储配方所需材料)  

如果使用一个SQL Server存储配方，Batch报告和Material，需要使用默认的SQL实例名(MSSQLSERVER)。 Material Manager Server目前只支持默认实例名.  

官方文档的安装建议  
1. 不要把FactoryTalk Batch Material Manager 和 FactoryTalk Batch Server 装在同一台机器上，但在实际操作中我们经常把所有组件都装到一起。
2. 把FactoryTalk Event Archiver放在有SQL Server的机器上  