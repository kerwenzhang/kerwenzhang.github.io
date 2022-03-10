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
2. In “Visual C#” -> “WCF”, 选 “WCF Service Library”    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async1.png?raw=true)
3. Visual Sutdio会自动创建两个cs：`IService1.cs` 和 `Server1.cs`, App.config里已经有默认`basicHttpBinding`,直接按F5，会弹出WCF TEST Client  
4. 新建接口 ICalculator.cs  
   
        using System.ServiceModel;
        namespace Server
        {
            [ServiceContract(Name = "CalculatorService")]
            public interface ICalculator
            {
                [OperationContract]
                double Add(double x, double y);

                [OperationContract]
                double Subtract(double x, double y);

                [OperationContract]
                double Multiply(double x, double y);

                [OperationContract]
                double Divide(double x, double y);
            }
        }

5. 新建服务实现 CalculatorService.cs  

        namespace Server
        {
            public class CalculatorService : ICalculator
            {
                public double Add(double x, double y)
                {
                    return x + y;
                }

                public double Subtract(double x, double y)
                {
                    return x - y;
                }

                public double Multiply(double x, double y)
                {
                    return x * y;
                }

                public double Divide(double x, double y)
                {
                    return x / y;
                }
            }
        }

6. 修改App.config，将service1改成CalculatorService  

        <services>
            <service name="Server.CalculatorService">
                <host>
                <baseAddresses>
                    <add baseAddress = "http://localhost:8733/Design_Time_Addresses/Server/CalculatorService/" />
                </baseAddresses>
                </host>
                <endpoint address="" binding="basicHttpBinding" contract="Server.ICalculator">
                <identity>
                    <dns value="localhost"/>
                </identity>
                </endpoint>
                <endpoint address="mex" binding="mexHttpBinding" contract="IMetadataExchange"/>
            </service>
        </services>

7. 按F5，弹出WCF TEST Client， 尝试Add 方法  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async2.png?raw=true)  

## Host 
我们将WCF 服务托管到self host exe上，也可以托管到IIS上。  
1. 新建一个console app，修改Main函数

        static void Main(string[] args)
        {
            using (ServiceHost host = new ServiceHost(typeof(CalculatorService)))
            {
                host.Opened += delegate
                {
                    Console.WriteLine("CalculaorService has started, press any key to stop");
                };

                host.Open();
                Console.ReadKey();
            }
        }

2. 修改App.config

    <configuration>
        <startup>
            <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8" />
        </startup>
        <system.serviceModel>
            <behaviors>
            <serviceBehaviors>
                <behavior name="metadataBehavior">
                <serviceMetadata httpGetEnabled="true" httpGetUrl="http://127.0.0.1:9999/calculatorservice/metadata" />
                </behavior>
            </serviceBehaviors>
            </behaviors>
            <services>
            <service behaviorConfiguration="metadataBehavior" name="Server.CalculatorService">
                <endpoint address="http://127.0.0.1:9999/calculatorservice" binding="wsHttpBinding"
                        contract="Server.ICalculator" />
            </service>
            </services>
        </system.serviceModel>
    </configuration>

3. 编译之后以Admin权限运行Host.exe, 当服务启动之后，打开浏览器，输入`http://127.0.0.1:9999/calculatorservice/metadata`，可以拿到WCF 服务的metadata  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async4.png?raw=true)  

## Client
1. 新建console app， 名称 Client
2. 保持Host.exe 运行情况下，右键Reference，添加Service Reference  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/async3.png?raw=true)  
3. 修改main函数  

        static void Main(string[] args)
        {
            using (CalculatorServiceClient proxy = new CalculatorServiceClient())
            {
                Console.WriteLine("x + y = {2} when x = {0} and y = {1}", 1, 2, proxy.Add(1, 2));
                Console.WriteLine("x - y = {2} when x = {0} and y = {1}", 1, 2, proxy.Subtract(1, 2));
                Console.WriteLine("x * y = {2} when x = {0} and y = {1}", 1, 2, proxy.Multiply(1, 2));
                Console.WriteLine("x / y = {2} when x = {0} and y = {1}", 1, 2, proxy.Divide(1, 2));
            }
            Console.ReadKey();
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

# Reference：  
[同步和异步操作](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/synchronous-and-asynchronous-operations)  
[c#中为什么async方法里必须还要有await？](https://www.zhihu.com/question/58922017)  
[WCF技术剖析之十一：异步操作在WCF中的应用（上篇）](https://www.cnblogs.com/artech/archive/2009/07/08/1519423.html)  
[WCF技术剖析之十一：异步操作在WCF中的应用（下篇）](https://www.cnblogs.com/artech/archive/2009/07/08/1519499.html)  
[我的WCF之旅（1）：创建一个简单的WCF程序](https://www.cnblogs.com/artech/archive/2007/02/26/656901.html)  
[如何：控制服务实例化](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/feature-details/how-to-control-service-instancing)  
[WCF Service which creates a new thread for every new request](https://stackoverflow.com/questions/1431180/wcf-service-which-creates-a-new-thread-for-every-new-request)  
