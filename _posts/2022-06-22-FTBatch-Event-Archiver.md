---                
layout: post            
title: "FactoryTalk Batch实操5：Batch Event Archiver"                
date:   2022-6-22 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

# FactoryTalk事件归档器 Event Archiver   
FactoryTalk事件归档器从FactoryTalk Batch服务器生成的批次记录文件（.evt文件）收集数据，并将数据存储在SQL Server数据库中。  


## 功能特性  
FactoryTalk Batch服务器为批次列表中的每个批次创建电子批次记录，可使用文本处理器或电子表格应用程序查看该记录文件。FactoryTalk事件归档器从每个电子批次记录文件收集数据并写入数据库，每个文件包含独立行，每行代表批次中发生的事件，归档器会为每个事件插入带日期和时间的唯一标识符到数据库。  

带Reporting Services的FactoryTalk事件归档器将数据写入BatchHistoryEx数据库的BHBatchHis SQL表。  

可通过以下两种方式配置FactoryTalk事件归档器将数据归档到数据库：  
- **批次结束（End-of-Batch）**：批次从列表移除后，归档器将记录插入数据库。当批次从列表移除时，Batch服务器启动归档器归档该批次。  
- **增量（Incremental）**：归档器按预定义计划将记录插入数据库，归档时间间隔在FactoryTalk Batch设备编辑器中配置。  

当Batch服务器执行控制配方时，服务器将批次记录文件名添加到归档器工作队列文件（Archque.txt）。归档器将所有电子批次记录插入数据库并标记文件从列表移除后，会从工作队列文件中删除该文件名。除非特别配置，否则归档器不删除批次记录文件。  

若归档器无法成功插入批次记录文件中的每项数据，不会从工作队列文件中删除文件名。每次归档器运行时，会尝试将队列中每个文件的记录插入数据库。失败时，归档器会尝试稍后存储数据，确保失败不会导致归档数据丢失。  

**重要提示**：批次结束时运行归档器时，Batch服务器将其作为Windows IDLE_PRIORITY进程运行。若系统繁忙，高优先级功能会优先执行，导致归档过程变慢。  


## 系统架构  
FactoryTalk事件归档器是从Batch服务器归档事件的Windows服务，事件写入SQL数据库表。可通过Reporting Services将数据库中存储的事件查看为HTML报告。  


### 带Reporting Services的系统架构  
FactoryTalk事件归档器可在批次运行时增量运行或在批次完成后运行，按以下基本步骤循环执行：  
1. Batch服务器创建事件文件。  
2. 归档器从事件文件读取记录并转换为SQL语句。  
3. 归档器将数据写入SQL数据库。  
4. 归档器将所有归档活动记录到日志文件。  
5. 安装Reporting Services后，可从数据库存储的事件数据生成报告。  


## 运行FactoryTalk事件归档器  
使用以下说明运行归档器以插入批次记录数据：  

### 运行步骤：  
1. 操作员或制造执行系统（MES）启动批次。若以增量模式运行，需将归档器启用为Windows服务。  
2. 创建电子批次记录文件（.evt）。  
3. 文件名添加到电子批次记录目录文件EventDir.txt。  
4. Batch服务器增量写入归档器工作队列文件ArchQue.txt，文件数据包含电子批次记录文件路径；若批次从列表移除，文件名后跟随制表符和“REMOVED”。  
   - **批次结束归档**：批次从列表移除时，Batch服务器发送消息启动归档器（需已启用）。  
   - **增量归档**：归档器按预定义计划运行，批次处理期间需始终处于活动状态。  
5. 归档器读取ArchQue.txt中的文件名和批次状态。  
6. 归档器读取电子批次记录文件。  
7. 归档器将记录插入数据库。  
8. 若数据成功插入数据库，从ArchQue.txt中删除该文件名。  

步骤4至7重复执行，直至归档器尝试将ArchQue.txt中列出的每个电子批次记录文件插入数据库。