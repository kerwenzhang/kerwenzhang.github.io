---                
layout: post                
title: "C# debug application startup" 
date:   2020-01-06 15:00:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

    
Add

    System.Diagnostics.Debugger.Launch();

to `Application_Start`. You'll get a popup asking you if you want to debug the website, and if you click OK, you'll be taken to Visual Studio in debug mode, paused at that line.