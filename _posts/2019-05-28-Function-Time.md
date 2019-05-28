---                                  
layout: post                                  
title: "C# 计算函数执行时间"                                  
date:   2019-05-28 9:00:00                                   
categories: "C#"                                  
catalog: true                                  
tags:                                   
    - C#                                  
---                        
    

    var watch = System.Diagnostics.Stopwatch.StartNew();

    // your code

    watch.Stop();
    var elapsedMs = watch.ElapsedMilliseconds;