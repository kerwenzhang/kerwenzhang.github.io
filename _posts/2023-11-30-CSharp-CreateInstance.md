---
layout: post
title: "C# Create Instance"
date: 2023-11-30 11:00:00
categories: "C#"
catalog: true
tags:
  - C#
---
 

For Late binding we have to use System.Reflection namespace, which allows us to programmatically access the types contained in any assembly. We will see how we can do late bindings in four easy steps..
+ We have Get IDispatch Interface using Type.GetTypeFromProgID("Project1.Class1")
+ We have to create instance using the type ID Activator.CreateInstance(objAddType)
+ We have to make array of arguments (if required)
+ Invoke the Method using objAddType.InvokeMember function.  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/latebinding.png?raw=true)  