---                
layout: post            
title: "SequenceManager"                
date:   2022-6-24 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

# 安装

## SQL Server
SequenceManager uses SQL Server and FactoryTalk Event Archiver to archive event records for reporting.  
SQL Server 2019 (English version only)  
SQL Server 2017 (English version only)  
SQL Server 2016 Service Pack 1 (English version only)  
SQL Server 2014 Service Pack 3 (32-bit and 64-bit, English version only)  
SQL Server 2012 Service Pack 4 (32-bit and 64-bit, English version only)  

These SQL Server features must be enabled:  
• Database Engine Services  
• Reporting Services (if using FactoryTalk Event Archiver with Batch reports)  


## Create a system DSN
A system data source name (DSN) is used by Sequence Manager to connect to the SQL database. Create the DSN on the computer running SQL Server.  

1. Click Start and then, in the Search box, type ODBC.  
2. Double-click the ODBC Data Source (32-bit) app.  
3. If prompted to allow the app to make changes to your system, click Yes.  
4. In the ODBC Data Source Administrator (32-bit) window click Add.  
5. In the Create New Data Source dialog box, select ODBC Driver 13 for SQL Server.  
6. Complete the data source name information.   
    a. Name - The name used to connect to the database.  
    b. Description - (optional) Additional identifying information to distinguish this data source.  
    c. Server - Enter (local) or select the name of the SQL Server instance from the list.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm1.png?raw=true)
7. (optional) In the ODBC Microsoft SQL Server Setup dialog box, select Test Data Source to confirm connectivity to the database.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm2.png?raw=true)
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm3.png?raw=true)
8. Click OK to close the dialog box.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm4.png?raw=true)


## Configure Reporting Services 
Configure SQL Server Reporting Services so that FactoryTalk Event Archiver can create SequenceManager reports. The instructions differ slightly between SQL Server version.  

1. In the Windows search bar, type Report Server Configuration Manager and then select the app to open it.
2. In Report Server Configuration Connection, select the report server instance to configure.
a. In Server Name, specify the name of the computer on which the report server instance is installed.
b. In Report Server Instance, select the SQL Server Reporting Services instance to configure. Only report server instances for this version of SQL Server appear in the list.
c. Click Connect. The Report Server Configuration Manager opens.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm5.png?raw=true)
3. On the left pane, select Web Service URL.
4. Select Apply to accept the default values. Observe the Results pane. If all tasks completed successfully, continue the configuration.
5. On the left pane, select Database.
6. Under Current Report Server Database, select Change Database to open the Report Server Database Configuration Wizard.
7. On the Action page, select Create a new report server database then select Next.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm6.png?raw=true)
8. On the Database Server page complete the settings:
• In Server Name type the name of the SQL Server.
• In Authentication Type select Current User - Integrated Security.
• Select Test Connection to verify the user account can login to the server.
• Select Next.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm7.png?raw=true)
9. On the Database page, in Database Name provide a name for the initial reporting database and then select Next.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm8.png?raw=true)
10. On the Credentials page specify an existing account that the report server will use to connect to the report server database and then select Next.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm9.png?raw=true)
11. On the Summary page confirm the settings are correct and then select Next.
12. Once the report server database is created, select Finish to close the wizard.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm10.png?raw=true)
13. On the left pane, select Web Portal URL.
14. Select Apply to accept the default values. Observe the Results pane. If all tasks completed successfully, continue the configuration.
15. In the Web Portal URL pane (on the right), select the URLs: link to open SQL Server Reporting Services in a web browser.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm11.png?raw=true)
16. In Execution Account, select Specify an execution account.
17. In Account enter the SequenceManager user account.
18. Select Apply. Observe the Results pane and verify the task completed successfully.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm12.png?raw=true)


[关于Reporting Service web url第一次加载很慢](https://stackoverflow.com/questions/11207049/sql-reporting-services-first-call-is-very-slow)


# 使用
使用 SequenceManager 使用以下任务中描述的 ControlLogix 功能对顺序制造流程进行建模和执行：  
• 使用设备序列编辑器配置设备阶段执行的协调。  
• 使用 ControlLogix 执行设备序列程序。  
• 使用Logix Designer 应用程序监控和管理正在运行的设备序列。  
• 通过将 SequenceManager ActiveX 控件添加到 FactoryTalk View SE 显示器，使操作员能够监控和管理正在运行的设备序列和设备阶段。  
• 使用SequenceManager 事件客户端服务和SequenceManager 事件归档服务订阅和收集生成的序列事件。  

The following diagram illustrates the components that are part of the SequenceManager and their responsibilities.   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm13.png?raw=true)

## Logix Designer, Sequence Editor, and Sequence Monitor
设备序列编辑器用于创建设备序列程序。 序列图定义了要运行的设备阶段序列、执行顺序以及制造产品所需的参数数据。 使用序列标签编辑器在设备序列中定义输入和输出参数。 设备序列程序及其标签与所有 Logix 程序和标签创作功能完全集成。  
设备序列监控器是设备序列编辑器的在线版本，用于监控已下载到控制器的设备序列并与之交互。 控制工程师可以执行以下操作：  
• 命令设备序列。  
• 更改参数和属性的值。  
• 与执行序列交互。  

The Equipment Sequence program firmware implements all the code necessary to manage the use of Equipment Phase programs, shares data between a sequence program and one or more Equipment Phase programs, and coordinates execution of the Equipment Phases. 
When an Equipment Sequence or sequence element changes status or an operator interacts with the Equipment Sequence, the firmware generates an event. Once an event is generated, it is published for external applications to receive.   

Sequence Manager ActiveX 控件提供设备序列程序的操作员可视化。共有三个操作员控件用于查看设备序列并与之交互。  
序列详细信息控件(Sequence Detail Control)为操作员提供设备序列的详细视图，包括其图表结构、步骤和转换。顺控程序的运行状态及其顺控元素也会显示出来。操作员可以通过该控件命令设备序列。  
序列汇总控件(Sequence Summary Control)显示下载到控制器的每个设备序列的序列程序状态。序列摘要控件还允许操作员查看和命令选定的设备序列。  
序列参数控件(Sequence Parameters Control)显示指定设备序列的所有序列参数和步骤标签的表格，并允许操作员命令选定的序列参数或步骤标签。要细化显示，请配置表格以过滤显示的信息。  

Sequence Manager 事件服务控制台(Event Services Console )提供了用于执行以下任务的用户界面：
• 启动和停止设备序列管理器事件客户端服务和设备序列管理器事件归档服务。
• 显示设备序列管理器事件客户端服务和设备序列管理器事件归档服务的状态。
• 配置设备序列管理器事件客户端服务设置和序列管理器事件归档服务设置。
序列管理器事件客户端(Event Client)是controller的外部的服务，它从通用事件日志接收事件。事件客户端将生成的原始事件保存到一个临时文件中。
Sequence Manager 归档服务(Archiving Service)处理原始事件文件，将数据本地化、翻译和组合成 PlantPAx Historian 和报告应用程序使用的格式。此数据将写入 EVT 文件，并且可以选择写入 SQL Server 数据库。
PlantPAx 应用程序读取生成的事件并对其进行处理。  

# Equipment Sequence Editor
设备序列编辑器（Equipment Sequence Editor）包含在 Logix Designer 应用程序主窗口的例程窗口中。 使用此编辑器编辑设备序列图例程。 例行程序窗口包含用于
所有打开的例程、每个例程的视图和设备序列工具栏。 当一个新的序列图首次显示时，它包含一个初始步，链接到具有默认表达式 TRUE 的转换，链接到一个终端步。
设备序列编辑器布局由设备序列元素工具栏、设备序列图工作区和序列标签编辑器组成。
下图标识了设备序列编辑器的主要区域。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/sm14.png?raw=true)
