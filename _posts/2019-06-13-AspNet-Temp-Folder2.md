---                                  
layout: post                                  
title: "Temporary ASP.Net Files folder 权限更改"                                  
date:   2019-06-13 9:00:00                                   
categories: "C#"                                  
catalog: true                                  
tags:                                   
    - C#                                  
---                        
    
最近在做DFS相关的一些工作，发现在ASP.NET临时文件夹中产生了一些临时文件，而且文件夹的权限中，除了IIS_IUSRS外，还多了application pool用户，权限还是special.  
![iis1](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/iis1.png?raw=true)

对比了一下其他产品，发现在Application pool -> Advanced Settings 里面有些不同。
![iis2](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/iis2.png?raw=true)

尝试把 Identity改成 NetworkService，重启IIS 之后，再次查看临时文件夹，发现application pool的账户权限就没有了。只剩下了IIS_IUSRS 账户。

查阅微软的[官方文档](https://docs.microsoft.com/en-us/iis/manage/configuring-security/application-pool-identities )，发现微软是故意这样做的。
在IIS 7.5 以前，application pool的Identity默认是Network Service。 IIS 7.5以后，出于安全的考虑，Identity的默认值改成ApplicaPoolIdentity。 临时文件夹的权限里面也会相应的增加application pool账户。