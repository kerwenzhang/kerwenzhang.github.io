---
layout: post
title: "利用Process Monitor软件解决无法加载DLL文件的问题"
date:   2016-03-14 10:50:00 
categories: "C#, Others"
tags: 
    - ProMon
	- dll
	- C# 
	- Others
---

* content
{:toc}

Process Monitor一款系统进程监视软件，总体来说，Process Monitor相当于Filemon+Regmon，其中的Filemon专门用来监视系统 中的任何文件操作过程，而Regmon用来监视注册表的读写操作过程。 有了Process Monitor，使用者就可以对系统中的任何文件和 注册表操作同时进行监视和记录，通过注册表和文件读写的变化， 对于帮助诊断系统故障或是发现恶意软件、病毒或木马来说，非常 有用。 这是一个高级的 Windows系统和应用程序监视工具，由优秀的 Sysinternals开发，并且目前已并入微软旗下，可靠性自不用说。    

打开Process Monitor，添加过滤:    
Process Name is (Proces_name).exe  => click add   
patch ends with dll  => click add    
result is "NAME NOT FOUND"  => click add   

然后重启调试, 在bug出现前， 点"File-> Save"， 保存一下log， 可以选择csv格式   
继续调试，当bug出现后，再保存一份log， 对比两份log， 就可以发现究竟是哪个dll没有找到。   