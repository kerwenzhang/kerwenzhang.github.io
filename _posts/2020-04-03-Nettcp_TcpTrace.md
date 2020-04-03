---                
layout: post                
title: "如何在IIS host的NetTcpBinding上监听消息" 
date:   2020-04-03 10:30:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      
最近一直在做WCF的通信加密，最终采用了windows认证的方式。 做完之后需要抓一下包，验证消息已经进行了加密。  
这里主要参考了以下文章：   
[https://www.cnblogs.com/chnking/archive/2008/10/07/1305891.html](https://www.cnblogs.com/chnking/archive/2008/10/07/1305891.html)   
[https://sites.google.com/site/wcfpandu/configuring-wcf-service-with-nettcpbinding](https://sites.google.com/site/wcfpandu/configuring-wcf-service-with-nettcpbinding)   

在第一篇文章里主要介绍了如何添加NetTcp监听端口，但是Wcf的Service是自己的写的程序host的，而我的程序是放在IIS上。后来翻了很久，找到了第二篇文章。 这篇文章是讲如何在IIS上host NetTCPBinding，关键点是我们可以修改IIS，配置默认的net.tcp端口。 IIS默认net.tcp端口是808， 所以当我们启动TcpTrace去监听端口时，应该将目标地址设成808，源地址可以设成807。这样就能监听到消息了。   
这样Client端的代码需要做如下修改：

    // 808端口可以省略，IIS默认端口就是808
    EndpointAddress ea = new EndpointAddress("net.tcp://localhost:808/WCFService/GetIdentity");
    GetIdentityClient gc = new GetIdentityClient(myBinding, ea); 

    //为使用TcpTrace跟踪消息设置的TcpTrace监听端口
    ClientViaBehavior myClientViaBehavior = new ClientViaBehavior(new Uri("net.tcp://localhost:807/WCFService/GetIdentity"));
    gc.Endpoint.Behaviors.Add(myClientViaBehavior);

Service端不做修改，继续在IIS上host。

最后监听到消息如下：

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/tcptrace.png?raw=true)

因为通信已经进行了加密，所以拿到的是乱码。至此，验证成功。