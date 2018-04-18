---  
layout: post  
title: "C# library project 不支持 config"  
date:   2018-3-15 20:30:00   
categories: "C#"  
catalog: true  
tags:   
    - C#  
---  
  
 
You generally should not add an app.config file to a class library project; it won't be used without some painful bending and twisting on your part. It doesn't hurt the library project at all - it just won't do anything at all.

Instead, you configure the application which is using your library; so the configuration information required would go there. Each application that might use your library likely will have different requirements, so this actually makes logical sense, too.  

Different callers of the same library will, in general, use different configurations. This implies that the configuration must reside in the executable application, and not in the class library.

You may create an app.config within the class library project. It will contain default configurations for items you create within the library. For instance, it will contain connection strings if you create an Entity Framework model within the class library.

However, these settings will not be used by the executable application calling the library. Instead, these settings may be copied from the library.dll.config file into the app.config or web.config of the caller, so that they may be changed to be specific to the caller, and to the environment into which the caller is deployed.

This is how it has been with .NET since Day 1.
