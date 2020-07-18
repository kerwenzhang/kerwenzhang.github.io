---
layout: post
title: "C# 动态加载dll"
date:   2015-12-02 10:50:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



c#中通过反射可以方便的动态加载dll程序集，但是如果你需要对dll进行更新，却发现.net类库没有提供卸载dll程序集的方法。在.net 中，加入了应用程序域的概念，应用程序域是可以卸载的。也就是说，如果需要对动态加载的dll程序集进行更新，可以通过以下方法解决：     

新建一个应用程序域，在该应用程序域中动态加载DLL，然后可以卸载掉该应用程序域。该应用程序域被卸载的时候，相关资源也会被回收。  <br/>   
要想这样实现，就要让你程序的currentDomain和新建的newDomain之间进行通信，穿过应用程序域的边界。从网上找到了某大牛的解决方法，抄下来留给自己看吧： <br/>   

	using System; 
	using System.Collections.Generic; 
	using System.Text; 
	using System.Threading; 
	using System.Reflection; 
	namespace UnloadDll 
	{ 
		class Program 
		{ 
			static void Main(string[] args) 
			{ 
				string callingDomainName = AppDomain.CurrentDomain.FriendlyName;//Thread.GetDomain().FriendlyName; 
				Console.WriteLine(callingDomainName); 
				AppDomain ad = AppDomain.CreateDomain("DLL Unload test"); 
				ProxyObject obj = (ProxyObject)ad.CreateInstanceFromAndUnwrap(@"UnloadDll.exe", "UnloadDll.ProxyObject"); 
				obj.LoadAssembly(); 
				obj.Invoke("TestDll.Class1", "Test", "It's a test"); 
				AppDomain.Unload(ad); 
				obj = null; 
				Console.ReadLine(); 
			} 
		} 
		class ProxyObject : MarshalByRefObject 
		{ 
			Assembly assembly = null; 
			public void LoadAssembly() 
			{ 
				assembly = Assembly.LoadFile(@"TestDLL.dll");            
			} 
			public bool Invoke(string fullClassName, string methodName, params Object[] args) 
			{ 
				if(assembly == null) 
					return false; 
				Type tp = assembly.GetType(fullClassName); 
				if (tp == null) 
					return false; 
				MethodInfo method = tp.GetMethod(methodName); 
				if (method == null) 
					return false; 
				Object obj = Activator.CreateInstance(tp); 
				method.Invoke(obj, args); 
				return true;            
			} 
		} 
	} 
	
注意：<br/>   
1. 要想让一个对象能够穿过AppDomain边界，必须要继承MarshalByRefObject类，否则无法被其他AppDomain使用。<br/>   
2. 每个线程都有一个默认的AppDomain，可以通过Thread.GetDomain()来得到	<br/>   

Members must be resolvable at compile time to be called directly from C#. Otherwise you must use reflection or dynamic objects.<br/>   
Reflection<br/>   

	namespace ConsoleApplication1
	{
		using System;
		using System.Reflection;

		class Program
		{
			static void Main(string[] args)
			{
				var DLL = Assembly.LoadFile(@"C:\visual studio 2012\Projects\ConsoleApplication1\ConsoleApplication1\DLL.dll");

				foreach(Type type in DLL.GetExportedTypes())
				{
					var c = Activator.CreateInstance(type);
					type.InvokeMember("Output", BindingFlags.InvokeMethod, null, c, new object[] {@"Hello"});
				}

				Console.ReadLine();
			}
		}
	}

Dynamic (.NET 4.0)   

	namespace ConsoleApplication1
	{
		using System;
		using System.Reflection;

		class Program
		{
			static void Main(string[] args)
			{
				var DLL = Assembly.LoadFile(@"C:\visual studio 2012\Projects\ConsoleApplication1\ConsoleApplication1\DLL.dll");

				foreach(Type type in DLL.GetExportedTypes())
				{
					dynamic c = Activator.CreateInstance(type);
					c.Output(@"Hello");
				}

				Console.ReadLine();
			}
		}
	}
