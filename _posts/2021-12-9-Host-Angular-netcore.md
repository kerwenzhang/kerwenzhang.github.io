---                
layout: post            
title: "如何在一个IIS端口里同时host Angular和.NET Core Web Api"                
date:   2021-12-9 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

# 前言
上一篇JWT文章里在Angular客户端使用了代理`proxy`，请求http的url由`https://localhost:5001/api/weatherforecast`缩短成了`./api/weatherforecast`。在平时debug的时候没有问题，运行`npm start`会自动启用代理，但是当进行部署的时候问题就出现了。  
Angular客户端请求资源的时候发送的url是`./api/weatherforecast`，会返回404 error。  
我在想能不能把Angular客户端和Web Api放在同一个IIS applicaiion里，让它们共享一个端口。这样就不会出现404的问题了。  

# 解决方案  
## VS默认模板  
其实微软已经提供了解决方案。 打开VS2019，创建一个新工程，模板搜索`Asp.net core with Angular`。创建一个示例工程。  
创建完成之后，在`ClientApp` 文件夹下是Angular客户端代码。直接F5，Visual studio会打开浏览器，web页面是`Angular`的，后端服务是`.NET Core Web Api`提供的。  
打开`Startup.cs`，跟默认的`Web api`代码比较一下，发现有些不一样：  

    public void ConfigureServices(IServiceCollection services)
    {
       ...
        // In production, the Angular files will be served from this directory
        services.AddSpaStaticFiles(configuration =>
        {
            configuration.RootPath = "ClientApp/dist";
        });
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        ...
        app.UseStaticFiles();
        if (!env.IsDevelopment())
        {
            app.UseSpaStaticFiles();
        }
        ...
        app.UseSpa(spa =>
        {
            spa.Options.SourcePath = "ClientApp";

            if (env.IsDevelopment())
            {
                spa.UseAngularCliServer(npmScript: "start");
            }
        });
    }

`ConfigureServices`和`Configure`里加了`Spa(Single Page application)`相关的配置。  
这个其实就是我们找的东西。  

## 修改工程
修改我们的JWT工程  
1. 打开Nuget package， 添加新的引用 `Microsoft.AspNetCore.SpaServices.Extensions`  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/spa.png?raw=true)

2. 修改`Startup`

        public void ConfigureServices(IServiceCollection services)
        {
            ...
            services.AddSpaStaticFiles(configuration =>
            {
                configuration.RootPath = "wwwroot";
            });
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            ...
            app.UseStaticFiles();
            app.UseSpaStaticFiles();

            ...
            app.UseSpa(spa => {});
        }

3. 客户端`npm run build`，生成`dist`文件夹  
4. Server端 publish，选择默认文件夹  
5. 在`C:\inetpub\wwwroot\`下创建新的文件夹`Login`，将Server publish出来的东西直接拷到根目录下， 客户端生成的`dist\client`文件夹拷贝到Login文件夹下，重命名为`wwwroot`。  
6. 打开IIS, 创建一个新的web站点，路径指定到`C:\inetpub\wwwroot\Login`，右键browse，浏览器自动定位到Login界面  

# Reference
[How to host an Angular app inside .NET Core 3.1 WebAPI?](https://stackoverflow.com/a/62059506)  
[ASP.NET Core: Deploy Web API and Angular from the Same Project to the Same IIS Port](https://www.codeproject.com/Tips/5267505/ASP-NET-Core-Deploy-Web-API-and-Angular-from-the-S)
