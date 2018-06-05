---          
layout: post          
title: "在.NET环境中实现每日构建"          
date:   2018-6-5 13:15:00           
categories: "Others"          
catalog: true          
tags:           
    - Others          
---          
          
每日构建（Daily Build）也可称为持续集成（Continuous Integration），强调完全自动化的、可重复的创建过程，其中包括每天运行多次的自动化测试。每日构建的作用日益显得重要。它让开发者可以每天进行系统集成，从而减少了开发过程中的集成问题。

在.NET环境下建立每日构建可以使用一系列开源工具：
Nant: 完成代码的自动编译，自动运行测试工具。http://nant.sourceforge.net/builds/
NantContrib：自动从源码库中获取源代码。http://nantcontrib.sourceforge.net/nightly/builds/
NUnit2Report:将NUnit测试工具产生的XML报告转换为HTML报告形式。http://NUnit2Report.sourceforge.net
VSS：Visual Source Safe，微软源码管理工具
Draco.NET: 用于自动检测VSS中源代码变动情况，调用Nant完成自动编译

        
[在.NET环境中实现每日构建--NAnt篇](http://dragon.cnblogs.com/archive/2005/07/29/203189.html)
[在.NET环境中实现每日构建(Daily Build)--ccnet,MSBuild篇](http://hjf1223.cnblogs.com/archive/2006/04/13/374655.html)
[Jenkins+MSbuild+SVN实现dotnet持续集成 快速搭建持续集成环境](https://www.cnblogs.com/linJie1930906722/p/5966581.html)
[Build .NET Project with Jenkins](https://gist.github.com/yancyn/365a0ea446c4bab8af51)
[Integrate Jenkins and GitHub](https://www.automatetheplanet.com/integrate-jenkins-github/)
[Integrate Jenkins with MSBuild and NuGet](https://www.codeproject.com/Articles/878203/Integrate-Jenkins-with-MSBuild-and-NuGet)