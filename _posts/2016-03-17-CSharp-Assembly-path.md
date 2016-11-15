---
layout: post
title: "c# 用代码来设置程序的PrivatePath"
date:   2016-03-17 15:30:00 
categories: "C#"
catalog: true
tags: 
    - C#
---




原文地址：http://blog.csdn.net/sweety820/article/details/25218691   

有时候我们想让程序的exe文件和dll文件分开在不同目录，这时候可以有４种方法   

### app.config中配置

	<runtime>  
		<gcConcurrent enabled="true" />  
		<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">  
			<publisherPolicy apply="yes" />  
			<probing privatePath="32;64" />  
		</assemblyBinding>  
	</runtime>  

### AppendPrivatePath

AppDomain.CurrentDomain.AppendPrivatePath来设置    

	AppDomain.CurrentDomain.AppendPrivatePath( strRelatedDirectory );

### PrivateBinPath

new AppDomainSetup().PrivateBinPath 来设置    

	if (AppDomain.CurrentDomain.IsDefaultAppDomain())  
	{  
		string appName = AppDomain.CurrentDomain.FriendlyName;  
		var currentAssembly = Assembly.GetExecutingAssembly();  
		AppDomainSetup setup = new AppDomainSetup();  
		setup.ApplicationBase = System.Environment.CurrentDirectory;  
		setup.PrivateBinPath = "Libs";  
		setup.ConfigurationFile = setup.ApplicationBase +  

             string.Format("\\Config\\{0}.config", appName);     

		AppDomain newDomain = AppDomain.CreateDomain("NewAppDomain", null, setup);  
		int ret = newDomain.ExecuteAssemblyByName(currentAssembly.FullName, e.Args);  
		AppDomain.Unload(newDomain);  
		Environment.ExitCode = ret;  
		Environment.Exit(0);  
		return;  
	}

可有时候又不想把他放在config文件上，只想用代码来实现，第二中方法发现已经过期，第三种方法MSDN语焉不详的，网上也没有什么资料，目前就用第四种方法    

### AssemblyResolve事件

AppDomain有个AssemblyResolve事件，加载dll失败的时候触发，可以在这个事件里面处理    

	AppDomain.CurrentDomain.AssemblyResolve += CurrentDomain_AssemblyResolve;  
	
	
	static System.Reflection.Assembly CurrentDomain_AssemblyResolve(object sender, ResolveEventArgs args)  
	{  

        string path = System.IO.Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"Libs\");     
        path = System.IO.Path.Combine(path, args.Name.Split(',')[0]);     
        path = String.Format(@"{0}.dll", path);     
        return System.Reflection.Assembly.LoadFrom(path);     
    }  