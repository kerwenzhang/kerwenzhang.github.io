---                
layout: post                
title: "Jenkins调用Powershell脚本时报NativeCommandError" 
date:   2020-07-07 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

在用Jenkins 调用一个powershell脚本时，输出的log里面有以下奇怪的error信息

    + CategoryInfo          : NotSpecified: (:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError

后来Google了一下，发现是Powershell本身的一个bug。我在Powershell脚本里面调用了PSEXEC这么一个exe，而PSEXEC在执行的过程中除了输出正常的log信息外，还会向STDERR里写信息。而Powershell在处理STDERR的时候抛出了异常，但这个异常其实并不影响脚本的正常运行，只是在log里面会有一堆恼人的error。
解决方案是在调用Powershell脚本时，将STDERR信息重定向到nul

    powershell test.ps1 2>nul

这样修改其实是把所有的STDERR给屏蔽掉了，有一定的风险。  

[Reference1](https://stackoverflow.com/questions/18380227/psexec-throws-error-messages-but-works-without-any-problems)   
[Reference2](https://stackoverflow.com/questions/1394084/ignoring-an-errorlevel-0-in-windows-powershell-ise/1416933#1416933)   
[Reference3](https://stackoverflow.com/questions/1394084/ignoring-an-errorlevel-0-in-windows-powershell-ise/11826589#11826589)   
[Reference4](https://stackoverflow.com/questions/10666101/lastexitcode-0-but-false-in-powershell-redirecting-stderr-to-stdout-gives/10666208#10666208)    