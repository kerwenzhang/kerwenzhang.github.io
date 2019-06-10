---                                  
layout: post                                  
title: "Temporary ASP.Net Files 研究"                                  
date:   2019-06-10 9:00:00                                   
categories: "C#"                                  
catalog: true                                  
tags:                                   
    - C#                                  
---                        
    

## .NET
.net采用动态编译, 也就是说我们常说的build生成的dll只是中间代码 而在web第一次请求的时候才是真正意义上的编译生成二进制代码 这也就是为什么刚编译完第一次打开web页面的时候会比较慢的原因. 当我们第一次请求的时候，也就是正式编译的时候，dotnet会写一些临时文件到 %SystemRoot%\Microsoft.NET\Framework\versionNumber\Temporary ASP.NET Files 文件夹下.

Temporary ASP.NET Files 文件夹包含为页面和资源提供服务而创建的所有临时文件和程序集。要找到为您的 Web 页面动态创建的文件，您需要查看此文件夹子树。请注意，Temporary ASP.NET Files 目录是存放动态创建的文件的默认位置，但可以使用 web.config 文件中的              `<compilation>` 部分按应用程序对其进行配置：
    
    <system.web>
        <compilation tempDirectory="d:\www\abc.com\temp"  />
    </system.web>

当应用程序第一次在计算机上执行时，在临时文件目录下就会创建一个新的子文件夹。编译子文件夹的名称与应用程序的 IIS 虚拟目录的名称相同。  
ASP.NET 会定期在应用程序发生改变、需要重新编译时清理编译文件夹并删除陈旧的资源，但 Temporary ASP.NET Files 目录下的子树的大小可能会显著地增加.

## Reference
[https://www.cnblogs.com/bobzhao/articles/1937169.html](https://www.cnblogs.com/bobzhao/articles/1937169.html)

[https://docs.microsoft.com/en-us/previous-versions/ms366723(v=vs.140)](https://docs.microsoft.com/en-us/previous-versions/ms366723(v=vs.140))