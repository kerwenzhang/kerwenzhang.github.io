---                
layout: post            
title: "DelegatingHandler"                
date:   2022-2-22 10:30:00                 
categories: ".Net Core"                
catalog: true                
tags:                 
    - .Net Core                
---      

# 什么是DelegateHandler
ASP.NET Web API的核心框架是一个消息处理管道，这个管道是一组HttpMessageHandler的有序组合。这是一个双工管道，请求消息从一端流入并依次经过所有HttpMessageHandler的处理。在另一端，目标HttpController被激活，Action方法被执行，响应消息随之被生成。响应消息逆向流入此管道，同样会经过逐个HttpMessageHandler的处理。  

## HttpMessageHandler
ASP.NET Web API的消息处理管道由一组HttpMessageHandler经过“首尾相连”而成，ASP.NET Web API之所以具有较高的可扩展性，主要源于采用的管道式设计。虽然ASP.NET Web API框架旨在实现针对请求的处理和响应的回复，但是采用的处理策略因具体的场景而不同。  

## DelegateHandler

我们说ASP.NET Web API消息处理管道是通过一组有序的HttpMessagHandler“首尾相连”而成，具体实现“管道串联”是通过DelegatingHandler这个类型来完成的。顾名思义，DelegatingHandler具有委托功能，当它自己负责的消息处理任务完成之后可以委托另一个HttpMessagHandler进行后续的处理。如果这个被委托的也是一个DelegatingHandler对象，不就可以组成一个委托链了吗？而这个委托链不就是由一个个DelegatingHandler组成的消息处理管道吗？  

如下面的代码片断所示，DelegatingHandler是一个继承自HttpMessageHandler类的抽象类。

    public abstract class DelegatingHandler : HttpMessageHandler
    {  
        protected internal override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken);
        public HttpMessageHandler InnerHandler get;  set; }
    }

如果ASP.NET Web API的消息处理管道均由DelegatingHandler组成（位于管道尾端的HttpMessageHandler除外），我们就可以根据其InnerHandler获得对被委托的HttpMessageHandler对象的引用，由此便构成具有如下图所示的链式结构。组成ASP.NET Web API核心框架的消息处理管道就这么简单。  
    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/delegate.png?raw=true)  

# .net core
在.net core中可以使用中间件来实现类似的功能。  
Middleware is software that's assembled into an app pipeline to handle requests and responses. Each component:

1. Chooses whether to pass the request to the next component in the pipeline.  
2. Can perform work before and after the next component in the pipeline.  

这篇[微软的文章](https://docs.microsoft.com/en-us/aspnet/core/migration/http-modules?view=aspnetcore-5.0)介绍了如何将handler转为.net core 中间件  

    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/delegate2.png?raw=true)  

# Reference  

[ASP.NET Web API标准的“管道式”设计](https://www.cnblogs.com/artech/p/asp-net-web-api-pipeline.html)  
[Implement DelegatingHandler in ASP.NET Core 5.0 Web API?](https://stackoverflow.com/questions/69812922/implement-delegatinghandler-in-asp-net-core-5-0-web-api)  
[Registering a new DelegatingHandler in ASP.NET Core Web API](https://stackoverflow.com/questions/40385676/registering-a-new-delegatinghandler-in-asp-net-core-web-api)  
[ASP.NET Core Middleware](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-6.0#writing-middleware)  
[Migrate HTTP handlers and modules to ASP.NET Core middleware](https://docs.microsoft.com/en-us/aspnet/core/migration/http-modules?view=aspnetcore-5.0)  