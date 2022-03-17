---                
layout: post            
title: "WCF 异步操作"                
date:   2022-3-9 21:00:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      


# 疑问

1. WCF Service接收到的每次请求是开启一个新线程还是在主线程里执行？需不需要自己开一个线程？
2. WCF如果一个请求需要较长时间，该怎么设计？异步？跨线程怎么处理？
3. 异步 vs 双工callback？

# Cretae Demo Project
## WCF Service

1. 以Admin权限打开Visual Studio 2022, 创建新的project   
2. In “Visual C#” -> “WCF”, 选 “WCF Service", solution名字WCF_Async, project名字WCFService    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async1.png?raw=true)
1. Visual Sutdio会自动创建两个cs：`IService.cs` 和 `Server.cs`,直接按F5，会弹出WCF TEST Client  
2. 修改接口 IService.cs  
   
        [ServiceContract]
        public interface IService
        {

            [OperationContract]
            string GetData(string value);
        }

3. 修改服务实现 Service.cs  

        public class Service : IService
        {
            public string GetData(string value)
            {
                Thread.Sleep(5000);
                return string.Format("Server return: {0}", value);
            }
        }

4. 按F5，弹出WCF TEST Client， 尝试调用GetData 方法  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async2.png?raw=true)  

## Client
1. 新建console app， 名称 Client
2. 保持系统托盘里IIS Express -> WCF Service是否运行，右键Client Reference，添加Service Reference  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async3.png?raw=true)  
3. 修改main函数  

        internal class Program
        {
            static ServiceClient client = new ServiceClient();
            static void Main(string[] args)
            {
                CallSynMethod();
                Console.Read();
            }

            private static void CallSynMethod()
            {
                Console.WriteLine(client.GetData("Call Server Synchronize Method."));
                Console.WriteLine("Waiting for Synchronize operation...");
            }
        }

# 会话Sessions 、实例化Instancing和并发Concurrency

WCF的会话具有以下特性：  
1. 它们由调用它的客户端显式启动和终止。  
2. 在会话期间 Service是按照消息接收的顺序进行处理。  
   
WCF Service的实例化行为由 ServiceBehaviorAttribute.InstanceContextMode 属性进行设置， 用来控制如何创建 InstanceContext 以响应传入的消息。  
实例化模式有三种：

1. `PerCall`：为每个客户端请求创建一个新的 InstanceContext （以及相应的服务对象）。  
2. `PerSession`：为每个新的客户端会话创建一个新的 InstanceContext （以及相应的服务对象），并在该会话的生存期内对其进行维护（这需要使用支持会话的绑定）。  
3. `Single`：单个 InstanceContext （以及相应的服务对象）处理服务器生存期内的所有客户端请求。  
   
如果不设置，默认是`PerSession`

        [ServiceBehavior(InstanceContextMode=InstanceContextMode.PerSession)]
        public class CalculatorService : ICalculatorInstance
        {
            ...  
        }

并发是对 InstanceContext 中在任一时刻处于活动状态的线程数量的控制.  通过`ServiceBehaviorAttribute.ConcurrencyMode`来控制.  
有以下三种可用的并发模式：  

1. `Single`：最多允许每个实例上下文同时拥有一个对该实例上下文中的消息进行处理的线程。 其他希望使用同一个实例上下文的线程必须一直阻塞，直到原始线程退出该实例上下文为止。  
2. `Multiple`：每个服务实例都可以拥有多个同时处理消息的线程。 若要使用此并发模式，服务实现必须是线程安全的。  
3. `Reentrant`：每个服务实例一次只能处理一个消息，但可以接受可重入的操作调用。 服务仅在通过 WCF 客户端对象调用 时接受这些调用。  


# 异步
可以通过使用下列三种方法之一实现异步操作：  

1. 基于事件的异步模式  
2. IAsyncResult 异步模式  
3. 基于任务的异步模式  


## 基于事件的异步模式
支持基于事件的异步模式的服务将有一个或多个名为 MethodNameAsync 的操作。 这些方法可能会创建同步版本的镜像，这些同步版本会在当前线程上执行相同的操作。 该类还可能具有 MethodNameCompleted 事件，并且可能会具有 MethodNameAsyncCancel（或只是 CancelAsync）方法。 希望调用操作的客户端将定义操作完成时要调用的事件处理程序.  
基于事件的异步模型仅在 .NET Framework 3.5 中提供。 此外，如果使用创建 WCF 客户端通道，则不支持此方法，即使在 .NET Framework 3.5 中也是如此 System.ServiceModel.ChannelFactory<TChannel> 。 使用 WCF 客户端通道对象时，必须使用 System.IAsyncResult 对象异步调用操作。  
1. 新建一个WCF service `Service1.svc`  
2. 修改`IService1.cs`  

        [ServiceContract]
        public interface IService1
        {
            [OperationContract]
            string GetData(string message);
        }

3. 修改`Service1.cs`  

        public class Service1 : IService1
        {
            public string GetData(string message)
            {
                Thread.Sleep(5000);
                return string.Format("Server return: {0}", message);
            }
        }

服务端代码和同步调用的代码一模一样。    
4. Client端添加新的service引用, 勾选异步操作，
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async6.png?raw=true) 

这样会自动生成 基于事件的函数和IAsyncResult 异步函数
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async7.png?raw=true) 

5. 修改Client端代码

        internal class Program
        {
            static Service1Client client1 = new Service1Client();
            static void Main(string[] args)
            {
                CallEventBasedAsync();
                Console.Read();
            }

            private static void CallEventBasedAsync()
            {
                client1.GetDataCompleted += client_GetDataCompleted;
                client1.GetDataAsync("event-based asynchronous pattern");
                Console.WriteLine("Waiting for async operation...");
            }
            static void client_GetDataCompleted(object sender, ServiceReference1.GetDataCompletedEventArgs e)
            {
                Console.WriteLine(e.Result.ToString());
            }
        }

## IAsyncResult 异步模式
服务操作可以使用 .NET Framework 异步编程模式，并标记 `<Begin>` 属性设置为的方法，以异步方式实现 AsyncPattern true 。  
定义一个异步执行（而不考虑它在客户端应用程序中的调用方式）的协定操作 X：  
使用 BeginOperation 和 EndOperation 模式定义两个方法。  
BeginOperation 方法包括该操作的 in 和 ref 参数，并返回一个 IAsyncResult 类型。  
EndOperation 方法包括一个 IAsyncResult 参数以及 out 和 ref 参数，并返回操作的返回类型。  
可以将IAsyncResult异步模式分为两种：  
### 客户端异步模式  
客户端异步模式可以直接使用事件异步模式的例子。修改Client端代码：  

        internal class Program
        {
            static Service1Client client1 = new Service1Client();
            static void Main(string[] args)
            {
                CallIAsyncResultClientSide();
                Console.Read();
            }

            private static void CallIAsyncResultClientSide()
            {
                client1.BeginGetData("IAsyncResult asynchronous pattern (Client-Side)", new AsyncCallback(GetDataCallBackClient), null);
                Console.WriteLine("Waiting for async operation...");
            }
            static void GetDataCallBackClient(IAsyncResult result)
            {
                Console.WriteLine(client1.EndGetData(result).ToString());
            }
        }

### 服务 & 客户端异步模式  
1. 新建服务Service2.svc
2. 修改接口,添加属性`AsyncPattern`
   
        [ServiceContract]
        public interface IService2
        {
            [OperationContractAttribute(AsyncPattern = true)]
            IAsyncResult BeginGetData(string message, AsyncCallback callback, object asyncState);

            string EndGetData(IAsyncResult result);
        }

3. 实现接口

        public class Service2 : IService2
        {
            public IAsyncResult BeginGetData(string message, AsyncCallback callback, object asyncState)
            {
                var task = Task<string>.Factory.StartNew((res) => GetData(asyncState, message), asyncState);
                return task.ContinueWith(res => callback(task));
            }

            public string EndGetData(IAsyncResult result)
            {
                return ((Task<string>)result).Result;
            }

            private string GetData(object asyncState, string message)
            {
                Thread.Sleep(5000);
                return string.Format("Server return: {0}", message);
            }
        }

4. 客户端引用新的服务
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async8.png?raw=true) 

5. 修改client端实现  

        internal class Program
        {
            static Service2Client client2 = new Service2Client();
            static void Main(string[] args)
            {
                CallIAsyncResultServerSide();
                Console.Read();
            }

            private static void CallIAsyncResultServerSide()
            {
                client2.BeginGetData("IAsyncResult asynchronous pattern (Server-Side)", new AsyncCallback(GetDataCallBackServer), null);
                Console.WriteLine("Waiting for async operation...");
            }
            static void GetDataCallBackServer(IAsyncResult result)
            {
                Console.WriteLine(client2.EndGetData(result).ToString());
            }
        }

## 基于任务的异步模式
基于任务的异步模式是实现异步操作的首选方法，因为它最简单且最直接。  
客户端只需使用 await 关键字调用操作。  

服务器端：  
1. 新建服务Service3.svc
2. 修改接口
   
        [ServiceContract]
        public interface IService3
        {
            //task-based asynchronous pattern
            [OperationContract]
            Task<string> GetDataAsync(string message);
        }

3. 实现接口

        public class Service3 : IService3
        {
            public async Task<string> GetDataAsync(string message)
            {
                return await Task.Factory.StartNew(() => GetData(message));
            }

            private string GetData(string message)
            {
                Thread.Sleep(5000);
                return string.Format("Server return: {0}", message);
            }
        }

客户端：  
1. 添加服务引用
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async9.png?raw=true) 
   
2. 修改代码

        internal class Program
        {
            static Service3Client client3 = new Service3Client();
            static void Main(string[] args)
            {
                CallTaskBasedAsync();
                Console.Read();
            }

            private static void CallTaskBasedAsync()
            {
                InvokeAsyncMethod("task-based asynchronous pattern");
                Console.WriteLine("Waiting for async operation...");
            }
            static async void InvokeAsyncMethod(string message)
            {
                Console.WriteLine(await client3.GetDataAsync(message));
            }
        }

最后的输出：  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async10.png?raw=true) 

# Reference  
[同步和异步操作](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/synchronous-and-asynchronous-operations)  
[c#中为什么async方法里必须还要有await？](https://www.zhihu.com/question/58922017)  
[WCF技术剖析之十一：异步操作在WCF中的应用（上篇）](https://www.cnblogs.com/artech/archive/2009/07/08/1519423.html)  
[WCF技术剖析之十一：异步操作在WCF中的应用（下篇）](https://www.cnblogs.com/artech/archive/2009/07/08/1519499.html)  
[我的WCF之旅（1）：创建一个简单的WCF程序](https://www.cnblogs.com/artech/archive/2007/02/26/656901.html)  
[如何：控制服务实例化](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/feature-details/how-to-control-service-instancing)  
[WCF Service which creates a new thread for every new request](https://stackoverflow.com/questions/1431180/wcf-service-which-creates-a-new-thread-for-every-new-request)  
[Task-based Asynchronous Operation in WCF](https://www.codeproject.com/Articles/613678/Task-based-Asynchronous-Operation-in-WCF)  
[Asynchronous Operations in WCF](https://social.technet.microsoft.com/wiki/contents/articles/16346.asynchronous-operations-in-wcf.aspx)  
