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


# Reference：  
[同步和异步操作](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/synchronous-and-asynchronous-operations)  
[c#中为什么async方法里必须还要有await？](https://www.zhihu.com/question/58922017)  