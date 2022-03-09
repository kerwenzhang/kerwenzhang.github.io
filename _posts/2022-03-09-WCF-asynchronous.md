---                
layout: post            
title: "WCF 异步操作"                
date:   2022-3-9 21:00:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      

C#虽然已经用了好多年了，但是从来没有系统的学习过，有很多新的语言特性也没有用过。找到官方的文档，从头到尾过一遍。。。   

# 疑问

1. WCF Service接收到的每次请求是开启一个新线程还是在主线程里执行？需不需要自己开一个线程？
2. WCF如果一个请求需要较长时间，该怎么设计？异步？跨线程怎么处理？
3. 异步 vs 双工callback？


# Reference：  
