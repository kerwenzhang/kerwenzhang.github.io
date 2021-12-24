---                
layout: post            
title: "AddTransient AddScoped AddSingleton"                
date:   2021-12-23 17:30:00                 
categories: ".Net Core"                
catalog: true                
tags:                 
    - .Net Core                
---      


Transient objects are always different; a new instance is provided to every controller and every service.

Scoped objects are the same within a request, but different across different requests.

Singleton objects are the same for every object and every request.

权重：

AddSingleton→AddTransient→AddScoped

AddSingleton的生命周期：

项目启动-项目关闭   相当于静态类  只会有一个  

AddScoped的生命周期：

请求开始-请求结束  在这次请求中获取的对象都是同一个 

AddTransient的生命周期：

请求获取-（GC回收-主动释放） 每一次获取的对象都不是同一个


[AddTransient, AddScoped and AddSingleton Services Differences](https://stackoverflow.com/a/38139500)