---
layout: post
title: "COM+ Queued Components"
date: 2023-12-05 9:00:00
categories: "C#"
catalog: true
tags:
  - C#
---
 
# 基本概念
基于消息队列( Message Queuing)服务，COM+ QC服务(Queued Components service)提供了一种以异步方式调用和执行组件的简单方法。可以在不考虑发送方或接收方的可用性或可访问性的情况下进行处理。  
队列是一种无连接通信机制。 也就是说，发送方和接收方不直接连接，只能通过队列进行通信。 队列提供了一种保存信息的方法，直到接收方准备好获取信息。 发送方和接收方间接通信，以便各自可以独立运行，不受另一方影响。  

过去，开发人员需要深入了解相关知识，才能对异步的消息进行队列、发送和接收。而COM+ QC会自动以队列消息的形式对数据进行封装，更易于开发人员理解和使用。 而且QC服务内置了事务支持，如果服务器发生故障，则不一致的状态不会危及最终数据。    

## QC优点  
+ 提高组件可用性  
  在同步应用程序中，如果因为服务器过载或者网络问题导致一个组件不可用，则整个应用程序会不可用。使用COM+ QC，会将事务分为现在必须完成的活动和可以以后完成的活动。这样，消息可以在队列等候处理，组件就不需要挂起，可以处理其他任务。  
+ 组件生存期更短  
  在实时同步系统中，服务器组件必须一直存在，等待客户端进行方法调用并返回结果。 而使用QC服务的应用程序允许服务器组件独立于客户端运行。 提高了服务器对象的快速循环并提高了服务器的可伸缩性。  
+ 支持短暂连接的客户端  
  随着笔记本电脑的使用越来越多，我们需要为偶尔会断开连接的客户端或移动用户提供服务。在QC系统中，这些用户可以在断开连接或未连接服务器的情况下工作，然后连接到服务器处理请求。例如，销售人员可以线下从客户那获取订单，然后连接到服务器来处理这些订单。  
+ 消息可靠  
   QC使用数据库技术以可靠的方式保护数据。 当服务器发生故障时，消息队列可以回滚事务，以便保证消息不会丢失且数据不会损坏。  
+ 服务器资源合理规划  
  使用QC的应用程序可以将非关键工作推迟到服务器资源使用的非高峰期。不着急的请求不要求服务器立即响应。  

## 系统架构  
消息传递应用程序类似于电子邮件系统。 请求者向服务器发送消息;当服务器接收到消息时，将处理消息。 与电子邮件一样，QC系统负责处理网络详细信息，并确保邮件从客户端移动到服务器。


COM+ QC服务由以下部分组成：  

+ 客户端/发送端的记录器Recorder
+ 服务器/接收方监听器Listener  
+ 服务器/接收方的播放器Player   
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/qc1.png?raw=true)

### Recorder  
在典型的队列方案中，客户端调用队列组件。 调用组件Recorder，该Recorder将其打包为向服务器发送的消息的一部分，并将其放入队列中。 Recorder将客户端的安全上下文封送到消息中，并记录客户端的所有方法调用。 作为服务器组件的代理，Recorder从 COM+ 目录中的可队列接口中选择接口。  
录制的具体表示形式是将消息发送到消息队列。   
如果将事务属性设置为“Required”或“Supported”，当客户端调用transaction commit提交消息，并且消息队列是事务性（默认）时，消息队列才接受次消息。   
如果事务属性为“RequireNew”，即使客户端调用transaction abort，中止事务，消息队列也可以接受此消息。   

### Listener
Listener从队列中检索消息，并将其传递给Player组件。    

### Player  
Player在服务器端对客户端的安全上下文进行解封，然后调用服务器组件并执行相同的方法调用。 在客户端组件完成且事务提交transaction commit之前，player不会播放此方法调用。  

## 事务性消息队列
事务是针对数据存储（数据库或文件）的一系列修改操作， 保证要么全部执行成功，要么根本不执行。 在事务开始前会保留数据存储状态的快照，如果其中一项修改失败，事务将return失败，并回滚到初始状态。 事务用于维护数据的完整性，在业务软件编程中发挥着重要作用。  

通常，可以将业务流拆分为多个较小的事务或活动。 这些活动按时间分隔，然后使用可靠消息队列进行连接。

1. 事务涉及订单数据库。 消息队列使用事务功能将消息从一个队列移动到另一个队列，每次一个。 如果数据库能更新成功，则队列上会显示一条成功消息。 如果消息未能到达队列，则会中止该消息并回滚数据库。  

2. 一段时间后，消息队列发现服务器可用。 这是第二个事务。
3. 第三个事务涉及发货数据库查询和更新。 如果此事务执行失败，则会回滚修改，并将消息返回到输入队列。 这就保证了在事务执行期间数据和数据库的完整性。  

## QC的安全性
当客户端调用QC时，实际上是对Recorder进行调用。Recorder将其打包为消息的一部分到服务器。 Listener从队列中读取消息并将其传递给Player。 Player调用实际的服务器组件并执行相同的方法调用。 当Player调用方法时，服务器组件必须观察客户端的上下文 (而不是Player的上下文) 。 因为Recorder将客户端的上下文封送在了消息中。 就服务器对象而言，来自客户端的直接调用与来自Player的间接调用之间的上下文没有区别。 

COM+ 队列组件支持基于角色的安全语义，就像为与 COM+ 应用程序一起使用而构建的其他组件一样。 因此，组件可以使用编程接口来发现其调用方的角色成员身份 (ISecurityCallContext：：IsCallerInRole) 或特定用户 (ISecurityCallContext：：IsUserInRole) 。 建议任何具有潜在安全影响的队列组件使用这些接口显式检查发送方的凭据。
 
## QC组件开发
COM+ QC服务要求所有方法仅包含输入型参数，没有返回值。 由于服务器对象在客户端进行调用时不一定可用，因此可以创建另一个 对象的方式来返回服务器结果。 这样，双向通信并非一定发生，而是仅在在需要时，通过对象之间的一系列单向消息进行。

若要使用 COM+ QC服务，必须手动安装 消息队列 服务。在控制面板，添加/删除程序中选择消息队列进行安装。 

### 将对象作为参数传递
COM+ QC服务不会为每个现有 COM 组件启用队列。它对可以队列的方法类型有限制， 方法必须遵循以下规则：

+ 方法必须仅包含输入参数。
+ 不得返回任何特定于应用程序的结果。  

此外，对输入参数类型有限制。 在运行时，QC服务会打包客户端的参数，并使用 消息队列将参数传递给服务器组件。 简单类型（如整数和布尔值）可以直接封装传递 -- 更复杂的类型无法直接封装。  

如果在QC的方法中使用参数传递对象，客户端会将对象传递给Recorder。 Recroder将对象封装到消息队列消息中，并将其传递给Listener。 Listener接收消息并将其传递给player后，Player必须恢复该对象才能将其调度到客户端指定的方法调用。 根据队列环境中的客户端和服务器的生存期，这意味着这些对象必须能够按值进行封装。 因此针对更复杂的类型，Recorder和Player需要开发者提供的帮助来封装。  

如果想传递对象参数，则对象必须支持 `IPersistStream` 接口.该接口无法假定服务器何时会重新初始化对象。 例如，服务器可能不可用，或者直到当天晚些时候才启动服务器组件。 不支持 `IPersistStream` 的对象将返回错误。

#### 特殊的VB6
由于Visual Basic 6 允许创建可持久对象。 这些对象自动支持IPersistStream接口，并且可以作为参数传递给队列方法调用。 在将Visual Basic对象传递给队列组件之前，必须先初始化可保留的对象。 这可以通过以下两种方式之一完成：

+ 如果创建持久化对象的应用程序是用Visual Basic编写的，则Visual Basic运行时会自动处理对象初始化。
+ 如果创建Visual Basic可持久对象的应用程序是用Visual Basic以外的语言编写的，例如C++，则应用程序必须通过查询可持久对象的 IPersistStream 接口或调用 IPersistStreamInit：：InitNew或IPersistStream：：Load 方法。

#### ADO 记录集和 OLE DB 行集
QC允许在组件之间传递 ADO Recordset 或 OLE DB rowset对象， 这样也就允许一个组件处理另一个组件执行的查询结果。 在多台计算机上部署应用程序时，这非常有用。 Recordset and rowse对象可以作为方法参数传递给队列中的组件，但有以下限制：

+ 无法使用 IPersistStream封装服务器端 Recordset 对象。 只能将客户端 Recordset 对象作为参数传递给队列中的组件方法调用。
+ 如果直接使用 OLE DB，则必须将 OLE DB rowset 定义为客户端rowset。

### 工作组模式下的安全限制
消息队列工作组配置不允许 COM+ QC服务支持应用程序安全性。 如果你已安装具有工作组配置的消息队列，则必须在COM+ 应用程序-属性-队列选项卡中选择“不对消息进行身份验证”。 应仅在受信任的网络上执行此操作，并且必须在客户端和服务器上执行此操作。  

### 线程处理注意事项
COM+ 队列组件Recorder能在进程的多线程单元 (MTA) 或单线程单元 (STA) 中运行。 当Recorder在单线程中运行时，COM+ 要求包含对象的每个单元都必须具有 消息队列，以处理来自同一进程中其他单元的调用。 这意味着线程的工作函数必须具有消息循环。 实例化队列组件时，返回的接口指针始终是代理接口指针，而不是直接接口指针。 指针实际上是对Recorder实例的引用。 如果将此Recorder接口引用传递给另一个线程，则原始线程必须仍运行 Windows 消息循环，以便接收线程可以解封接口。 如果不是这种情况，则接收线程可以在调用 CoUnmarshalInterface 时挂起。

如果您使用原语（primitives）来同步线程，请考虑使用 MsgWaitForMultipleObjects 而不是其他同步函数。 这将检查队列中的消息以及同步对象的状态。  

### 接收响应
由于QC组件重点是设计成异步工作，客户端应该支持异步操作，在等待队列响应的时候继续执行其他操作。 不过，最终响应对于客户端来说通常很有用。 例如，客户端可能想在请求的事务成功完成时收到通知，知道事务已经结束了。

队列组件可以通过多种方式以异步方式将响应发送回调用方。 例如，它可以发送电子邮件。 或者，服务器可以发布客户端可以订阅的事件。

客户端从服务器上运行的队列组件获取响应的另一种方法是由客户端传递的包含回调函数的引用对象。引用对象可能非常简单，只包含用于表示错误值的整数，或者可能相当复杂，包含回滚客户端上的事务所需的所有信息。 无论哪种情况，调用客户端都会将通知对象作为输入参数传递。 在此方案中，COM+ QC服务用于客户端和服务器，以允许双向异步通信。
 
## QC Errors  
当对队列组件的调用失败时，可能是因为无法将其传输到服务器 (客户端故障) ，或者由于在到达时无法执行 (服务器端故障) ，相应的 消息队列中的消息称为脏消息。

COM+ QC服务使用一系列重试队列来处理脏消息。 多次重试后，消息将移动到最终的静态队列。 消息将保留在静态队列中，直到使用消息移动工具（message mover utility）手动移除它们。

### 服务器端错误
Listener和Player共同处理脏消息。 如果事务执行失败， 消息队列会将输入消息移回输入队列。 如果Player从服务器组件收到失败的 HRESULT 或捕获异常，则Player中止事务。 如果问题仍然存在，Listener可以在下列模式不断循环：

+ 消息出队
+ 实例化对象
+ 事务回滚
+ 将消息放回队列顶部

QC服务使用一系列重试队列来处理此故障。 这些队列在安装组件时创建，每个应用程序都有七个队列，如下所示：

1. 普通输入队列。 此队列的名称是 COM+ 应用程序名称。 这是公共消息队列。

2. 第一重试队列。 如果事务在普通输入队列里反复失败，则会将消息移动移到第一个重试队列。 此队列里的消息会在一分钟后处理。 在此队列上可以重试三次消息，三次之后，再移动到第二重试队列的最后面。 此队列名为 ApplicationName_0。 此队列是private消息队列。

3. 第二重试队列。 如果事务在第一个重试队列里反复失败，则会移动消息到第二重试队列。 此队列里的消息会在两分钟后处理。 在此队列上可以重试三次消息，三次之后，移动到第三个重试队列的后面。 此队列名为 ApplicationName_1。 此队列是private消息队列。

4. 第三重试队列。 与前边类似，但此队列的消息会在四分钟后处理。 队列名为 ApplicationName_2。  

5. 第四重试队列。  与前边类似，但此队列的消息在 8 分钟后处理。 队列名为 ApplicationName_3。  

6. 第五重试队列。 与前边类似，但队列的消息在 16 分钟后处理。队列名为 ApplicationName_4。   

7. 应用程序的最终静态队列。 如果事务在第五重试队列上反复中止，则会移动消息到最终静态队列。 此队列名为 ApplicationName_DeadQueue。 是private消息队列。 最终的休息队列不是由Listener来提供服务。 消息将保留在此处，直到被消息移动工具（queued components message mover utility）手动移动或由消息队列Explorer清除。

无法播放的消息，由于每次重试都将失败，因此直接移动到最终休息队列，而无需通过所有重试队列。  
通常由Player发出 COM+ 事件，通知相关方无法播放消息。 在以下情况下会发出 COM+ 事件：  

+ 事务中止abort
+ 将消息从一个队列移动到另一个队列时
+ 将消息存入最终休息队列时

将消息从一个队列移动到另一个队列之前，可以修改消息。 COM+ QC组件安全机制允许将消息移动到重试队列，然后重新插入应用程序的初始输入队列。  

当应用程序被组件服务admin tool标记为队列，或使用 COM+ SDK 函数进行队列时，会随主应用程序队列一起创建重试队列。  
QC服务允许通过删除重试队列来灵活地使用重试机制。 例如，如果删除所有重试队列，则会将永久中止的消息直接从应用程序队列移动到最终休息队列。   
通过删除一个或多个重试队列，可以减少重试次数和长度。  

重试机制旨在尽最大可能来完成消息。 在某些情况下，消息可能根本无法成功。 例如，客户可能试图从资金不足的帐户中取款。 在这些情况下，可以通过多种方式处理此错误，包括以下内容：

+ 生成诊断并发出警告
+ 创建补偿事务
+ 忽略问题并消除消息  

与客户端永久性故障一样，QC服务允许异常类与组件相关联。 异常类通过使用Addmin tool属性页中的 “高级 ”选项卡或使用 COM+接口与组件关联。 异常类允许开发人员在消息重试之后以及该消息移动到最终休息队列之前控制该消息。

下面是服务器端异常处理的事件序列：

1. 消息通过可用的重试队列移动。
2. 上次重试队列的最后一次重试失败。
3. QC服务运行时从消息中检索目标组件，并检查异常类。
4. 运行时实例化异常类。
5. 运行时查询异常类上的 IPlaybackControl 。
6. 运行时调用异常类中的 IPlaybackControl：：FinalServerRetry 。
7. 运行时播放从消息到异常类的所有属性和方法调用。
8. 如果步骤 4 到 6 不成功，运行时会将消息移到最终休息队列。  

如果需要干预上述过程，或者需要将脏消息移出其最终休息队列，请使用消息移动器实用工具。  

### Client-Side错误

客户端故障的处理方式类似于服务器端故障。 例如，如果消息无法从客户端发送到服务器，则消息队列可以将消息移动到其目标队列。 比如客户端死信队列。

COM+ QC服务会监视死信队列。 如果消息已移动，QC服务会创建异常类的实例，并调用 QueryInterface 来请求 IPlaybackControl。 如果此操作成功，死信队列监视器将调用 IPlaybackControl：：FinalClientRetry。

对象可以采取一些操作来反转先前事务的效果。 如果播放提交，则会从 Xact 死信队列中删除该消息。 如果播放失败或所需的 CLSID 和接口不可用，则消息将保留在 Xact 死信队列中。  

如果需要干预上述过程，或者需要将脏消息移出最终队列，请使用消息移动器实用工具。   


### 永久性Client-Side故障

在某些情况下， 消息队列 可以将消息移动到目标队列。 例如，如果队列安全控制不允许将消息从客户端发送到服务器，则会将违规消息移动到客户端死信队列。 发生这种情况时，COM+ QC服务允许创建一个异常类，并将异常类与组件相关联。 若要将异常类与组件相关联，请使用Admin tool属性页中的 “高级 ”选项卡。 还可以使用 COM+ API中的 `ExceptionClass`以编程方式关联异常类。  

异常类是必须实现 IPlaybackControl 的组件的 ProgID 或 CLSID。 QC服务有一个死信队列监视器，用于扫描 Xact 死信队列。 如果队列上有消息，死信队列监视器将实例化异常处理程序，并调用 IPlaybackControl：：FinalClientRetry，指示客户端存在一个不可恢复的错误。  

除了 IPlaybackControl 之外，异常处理程序还应实现与处理异常的服务器组件相同的接口集。 调用 IPlaybackControl：：FinalClientRetry 时，队列组件运行时会将失败消息重放给异常处理程序。 这允许异常处理程序为无法移动到服务器的消息实现替代行为，例如，通过生成补偿事务。  

如果异常处理程序完成回放的所有方法调用，则会从 Xact 死信队列中删除消息并消除。 但是，如果异常处理程序通过从方法调用之一返回失败状态来中止消息，则消息将返回到 Xact 死信队列。   

以下事件序列显示了如何处理客户端异常：  
1. 消息队列无法将消息发送到服务器，将消息放入 Xact 死信队列。
2. 死信队列Listener (DLQL) 在 Xact 死信队列中查找消息。
3. DLQL 从消息中检索目标组件 CLSID 并检查异常类。
4. DLQL 实例化异常类。
5. DLQL 查询异常类的 IPlaybackControl 。
6. DLQL 在异常类中调用 IPlaybackControl：：FinalClientRetry 方法。
7. DLQL 将消息中的所有属性和方法调用回放到异常类。
8. 如果异常处理程序成功完成事务，DLQL 将删除消息。 异常处理程序可能会发出 IObjectContext：：SetAbort，并且消息将保留在死信队列中。
如果上述任何步骤失败，则消息将保留在 Xact 死信队列中。  

启动时，DLQL 会读取消息队列事务性死信队列上的每条消息，并实例化每个队列组件消息的异常类。 一个通过队列后，它会等待新消息。 然后，当每个新的死信队列消息到达时，它都会对其进行处理。  

如果需要干预此处所述的过程，或者需要将脏消息移出其最终的静态队列，请使用消息移动器实用工具。   

# COM+ 队列任务QC Tasks
## 创建可队列化的组件
具有至少一个可队列化接口的组件叫 可队列组件（A component with at least one queuable interface is a queuable component.）对于要由队列调用的组件，接口必须标记为可队列化，并且该组件必须安装在队列应用程序中。 但是，一个可队列化组件可以是非队列应用程序的一部分。

可队列化接口必须仅包含输入参数，没有输出参数(out parameters)和返回值。 这些特征是在组件安装时验证。 如果接口不可队列化，则无法激活包含该组件的应用程序队列。  

若要将 COM+ 接口指定为可队列化接口，请参照以下步骤：

1. 在Admin tool中，打开要管理的COM+ 应用程序。

2. 打开要队列化的 Interfaces 文件夹。

3. 右键单击要队列化的接口，然后选择属性。

4. 在“属性”对话框中选择“ 队列 ”选项卡。

5. 选中“队列”的checkbox。
6. 单击“确定”。

如果“队列”复选框灰色，则接口不满足上述队列化条件。

将 QUEUEABLE 属性宏添加到接口定义语言的“接口”部分 (IDL) 这样标识可队列化组件。

    #include "mtxattr.h" 
    [ object, dual, uuid(), helpstring(IShiphip"), QUEUEABLE ] 
    interface IShip:IDispatch
    { 
      [propput, id(1)] HRESULT CustomerId ([in] long CustId);   
      [propput, id(2)] HRESULT OrderId ([in] long OrderID); 
      [id(3)] HRESULT LineItem ([in] long Qty); 
      [id(4)] HRESULT Process (); 
    }

## 创建队列
可以使用Admin tool将包含至少一个可队列化组件的应用程序标记为队列组件（queuable component）。

当应用程序标记为队列时，COM+ 会自动为其创建消息队列。 队列名称是应用程序的名称;如果队列名称与现有队列的名称匹配，则 COM+ 将使用现有队列。

 备注

消息队列 PathName 参数是远程服务器名称 (Remote Server Name RSN) 和 COM+ 应用程序名称的组合。 RSN 是指远程激活的目标。 在客户端计算机上安装时指定 RSN。 安装过程使用 RSN 将定向激活指定的客户端。  

若要将 COM+ 应用程序指定为队列，请参考以下步骤：

1. 打开与要管理的COM+ Applications。
2. 右键单击应用程序,然后单击“ 属性”。
3. 在属性对话框中选择“ 队列 ”选项卡。
4. 选择已队列复选框。
5. 单击确定  
如果该复选框灰色，则应用程序不包含任何可队列组件。  
 
不适用Visual Basic或C/C++

COM+ 创建的队列使用消息队列事务属性进行标记。

在服务器上安装队列的应用程序后，可以通过导出应用程序，然后在每个客户端上导入应用程序，使其可供客户端使用。  


## 激活组件队列

调用队列组件的方法并不会直接执行该方法。 相反， 消息队列 会先进行封装，将方法调用和参数存储在队列中。队列组件稍后会在消息队列中检索和执行这些调用和参数。 与激活远程 DCOM 对象不同，在调用 方法时不会实例化队列组件。 这是使用队列组件背后的基本理念 - 队列组件不需要与调用方同时实例化。

若要启动一个已经队列化的应用程序，请考虑以下步骤：

1. 在Admin tool中，打开要管理的COM+ Applications
2. 右键单击要激活队列的应用程序。
3. 单击“启动”。

Visual Basic参阅 COMAdminCatalog.StartApplication 示例。  
C/C++参阅 ICOMAdminCatalog::StartApplication 示例。 


## 使用队列名字对象Queue Moniker 
队列名字对象(Queue Moniker)用于以编程方式激活队列组件。 队列名字对象要求它直接从新名字对象的右侧接收要调用的对象的类 ID (CLSID)。 当使用左前缀时，新名字对象将 CLSID 传递给其左侧的名字对象。

此方法不适用Admin tool UI界面。 

### Visual Basic
GetObject 显示名称参数是`queue:/new:`，后跟要实例化的服务器对象的程序 ID 或字符串形式的 GUID（带或不带大括号）。   

    Set objMyQC = GetObject ("queue:/new:QCShip.Ship")
    Set objMyQC = GetObject ("queue:/new:{812DF40E-BD88-11D0-8A6D-00C04FC340EE}")
    Set objMyQC = GetObject ("queue:/new:812DF40E-BD88-11D0-8A6D-00C04FC340EE")

### C/C++
CoGetObject 显示名称参数是`queue:/new:`，后跟要实例化的服务器对象的程序 ID 或字符串形式的 GUID（带或不带大括号）。 

    hr = CoGetObject(L"queue:/new:QCShip.Ship", NULL, IID_IShip, (void**)&pShip);

    hr = CoGetObject(L"queue:/new:{812DF40E-BD88-11D0-8A6D-00C04FC340EE}", NULL, IID_IShip, (void**)&pShip);

    hr = CoGetObject(L"queue:/new:812DF40E-BD88-11D0-8A6D-00C04FC340EE", NULL, IID_IShip, (void**)&pShip);


队列名字对象接受可选参数，这些参数会更改发送到消息队列的消息的属性。 例如，若要使消息队列消息以优先级 6 发送，将按如下所示激活队列组件：

    hr = CoGetObject(L"queue:Priority=6,ComputerName=MyComp/new:QCShip.Ship", NULL, IID_IShip, (void**)&pShip);

下表列出了队列名字对象参数。

+ 计算机名
  指定消息队列队列路径名称的计算机名称部分。 消息队列队列路径名称的格式为 ComputerName<em>QueueName。 如果未指定，则使用与配置的应用程序关联的计算机名称。  
+ QueueName
  指定消息队列队列名称。 消息队列队列路径名称的格式为 ComputerName<em>QueueName。 如果未指定，则使用与配置的应用程序关联的队列名称。
  若要获取非事务性队列，可以先指定队列名称，然后创建同名的 COM+ 应用程序。
+ PathName
  指定完整的消息队列队列路径名称。 如果未指定，则使用与配置的应用程序关联的消息队列路径名称。 若要替代目标名称，可以在以下窗体中为消息队列工作组安装指定路径：
  Queue：PathName=ComputerName\PRIVATE$\AppName/new：Myproject.CMyClass
  注意：C 和 Microsoft Visual C++ 编程语言都需要两个反斜杠来表示字符串文本中的一个反斜杠
+ FormatName
  将 COM+ 应用程序标记为队列时，COM+ 会创建名称与应用程序相同的消息队列队列。 该队列的消息队列格式名称位于 COM+ 目录中，与 COM+ 应用程序相关联。 若要替代目标名称，可以在消息队列工作组安装的以下窗体中指定格式名称：
  Queue：FormatName=DIRECT=OS：ComputerName\PRIVATE$\AppName/new：ProgId



当启动COM+ 应用程序时，它是启动整个应用程序，而不是应用程序中的各个独立组件。 如果应用程序调用了一个未队列化的组件，则会启动包含该组件的 COM+ 应用程序。 如果Listener复选框被勾选，则Listener也会启动并开始处理队列组件的消息。 虽然可以通过这种方式启动QC服务，但如果将队列组件和非队列组件打包到同一个 COM+ 应用程序中，请确保在执行非队列组件时， 你真正希望队列化的组件已经启动。 如果不是这样，请将队列组件打包到独立于其他组件的 COM+ 应用程序中。

## 处理队列组件中的错误
有时，出现无法将消息成功传递到其预期目标的情况，通常是由于系统或配置存在问题。 例如，消息可能定向到不存在的队列，或者目标队列可能未处于要接收的状态。 消息移动器是一种工具，可将所有失败 的消息队列 消息从一个队列移动到另一个队列，以便可以重试。 消息移动器实用工具是可以使用 VBScript 调用的自动化对象。  
[Handling Errors in Queued Components](https://learn.microsoft.com/en-us/windows/win32/cossdk/handling-errors-in-queued-components)  


# C#实例
在 C# 中，我们还可以使用 MessageQueue 类的 Create（） 方法以编程方式创建消息队列。使用 Create（） 方法，必须传递新队列的路径。路径由队列所在的主机名和队列名称组成。  
1. 创建一个新的C# .net framework winform工程FirstQueue
2. 在form上添加四个button： Create,Find, Send和Read，添加一个label，用来显示读取的队列消息
3. 在Create button单击事件里添加以下代码创建队列

        private void buttonCreate_Click(object sender, EventArgs e)
        {
            using (MessageQueue queue = MessageQueue.Create(@". \myqueue"))
            {
                queue.Label = "First Queue";
                MessageBox.Show($"Queue Created, Path: {queue.Path}, FormatName: {queue.FormatName}");
            }
        }


    我们将在 localhost 上创建一个新的public队列“myQueue”。若要创建私有队列，路径名必须包含 private$。例如：\private$\MynewPrivateQueue。  
    调用 create（） 方法后，可以更改队列的属性。使用 label 属性，将队列的标签设置为“First Queue”。然后将队列的路径和格式名称打出来。格式名称是使用 UUID（通用唯一标识符）自动创建的，该 UUID 可用于访问队列，而无需服务器名称。  

    ![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mq1.png?raw=true)

    如果你遇到以下错误 `A workgroup installation computer does not support the operation.`  
    说明你是在一个domain域里，domain的policy不允许创建public的消息队列，将消息队列改为private，`@".\private$\myqueue"` 



4. 在Find button的事件里添加以下代码来发现队列  

        private void buttonFind_Click(object sender, EventArgs e)
        {
            string publicQueuePath = string.Empty;
            foreach (MessageQueue queue in MessageQueue.GetPublicQueues())
            {
                publicQueuePath += queue.Path + "\r\n";
            }

            string privateQueuePath = string.Empty;
            foreach(MessageQueue queue in MessageQueue.GetPrivateQueuesByMachine("localhost"))
            {
                privateQueuePath += queue.Path + "\r\n";
            }
            MessageBox.Show($"Get all public queues: \r\n {publicQueuePath} Get all private queues: \r\n {privateQueuePath}");
        }

    若要查找队列，可以使用路径名和格式名称。还可以区分公共队列和private队列。公用队列在 Active Directory 中发布。对于这些队列，没有必要知道它们所在的机器名。

    private队列只能在已知队列所在的机器名称中找到。
    类 MessageQueue 具有用于搜索队列的静态方法：

        GetPublicQueuesByLable()
        GetPublicQueuesByCategory()
        GetPublicQueuesByMachine()
        GetPublicQueues()

    以上方法返回域中所有公共队列的数组。
    还可以使用`GetPrivateQueuesByMachine()`获取私有队列。需要指定机器名  
    注意：  如果你的机器在domain域里，调用`GetPublicQueues`也会抛出异常`A workgroup installation computer does not support the operation.`  
5. 在Send button的事件里添加以下代码来发送消息  

        private void buttonSend_Click(object sender, EventArgs e)
        {
            try
            {
                if (!MessageQueue.Exists(@".\Private$\myqueue"))
                {
                    MessageQueue.Create(@".\Private$\myqueue");
                }
                MessageQueue queue = new MessageQueue(@".\Private$\myqueue");
                queue.Send("First Message ", "Label1");
            }
            catch (MessageQueueException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

    需要为打开的队列指定格式名称。在断开连接的环境中，在发送消息时无法访问队列，因此必须使用格式名称。  
    格式名称队列的语法为：

    |队列类型|语法|
    |-------|----|
    |专用队列|MachineName\Private$\QueueName|
    |公共队列|MachineName\QueueName|
    |日记队列|MachineName\QueueName\Journal$|
    |计算机日志队列|MachineName\Journal$|
    |机器死信队列|MachineName\DeadLetter$|
    |计算机事务死信队列|计算机名称\XactDeadLetter$|

    消息发送成功后，可以在 Component Management 管理工具中查看到该消息
    ![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mq2.png?raw=true)  
6. 在Read button的事件里添加以下代码来读取消息   

        private void buttonRead_Click(object sender, EventArgs e)
        {
            MessageQueue queue = new MessageQueue(@".\Private$\myqueue");
            queue.Formatter  = new XmlMessageFormatter(new Type[2] { typeof(string), typeof(string)});
            System.Messaging.Message Mymessage = queue.Receive();
            labelQueue.Text = Mymessage.Body.ToString();
        }

    再次查看Component Management 管理工具，消息已经清空了

7. 发送自定消息  
    上边我们只是发送了一个string消息，在实际中，我们可能自定义一个数据格式进行发送。  

        public class Employee
        {
            public int Id;
            public string Name;
            public int Hours;
            public double Rate;
        }
        
    比如，我们自己创建一个员工信息类，在消息队列里传送一个该类的实例  

        private void Send()
        {
            try
            {
                if (!MessageQueue.Exists(@".\Private$\myqueue"))
                {
                    MessageQueue.Create(@".\Private$\myqueue");
                }
                MessageQueue queue = new MessageQueue(@".\Private$\myqueue");

                var emp = new Employee()
                {
                    Id = 100,
                    Name = "John Doe",
                    Hours = 55,
                    Rate = 21.0
                };
                System.Messaging.Message msg = new System.Messaging.Message();
                msg.Body = emp;
                queue.Send(msg);
            }
            catch (MessageQueueException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

    读取队列消息  

        private void Read()
        {
            MessageQueue queue = new MessageQueue(@".\Private$\myqueue");
            
            var emp = new Employee();
            Object o = new object();
            System.Type[] arrTypes = new System.Type[2];
            arrTypes[0] = emp.GetType();
            arrTypes[1] = o.GetType();
            queue.Formatter = new XmlMessageFormatter(arrTypes);
            emp = ((Employee)queue.Receive().Body);
            labelQueue.Text = $"Employee name: {emp.Name} Salary: {emp.Hours * emp.Rate}";
        }

# Reference
[COM+ Queued Components](https://learn.microsoft.com/en-us/windows/win32/cossdk/com--queued-components-concepts)  
[Using Message Queues In C#](https://www.c-sharpcorner.com/article/using-message-queues-in-c-sharp/)  
[Message Queuing Using C#](https://www.c-sharpcorner.com/article/message-queuing-using-C-Sharp/)  
[Message Queue](https://www.codeproject.com/Articles/1260171/Message-Queue-2)  
[Send Message to Microsoft Message Queue (MSMQ) – C# Example](https://coding-examples.com/csharp/remoting/send-message-to-microsoft-message-queue-msmq-c-example/)  
[Use Visual C# to write to and read from Microsoft Message Queuing](https://learn.microsoft.com/en-us/previous-versions/troubleshoot/msmq/write-read-msmq-visual-csharp)  
[MessageQueue Class](https://learn.microsoft.com/en-us/dotnet/api/system.messaging.messagequeue?view=netframework-4.8.1)  
