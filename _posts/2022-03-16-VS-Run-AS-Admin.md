---                
layout: post            
title: "总是以Admin权限打开Visual Studio工程"                
date:   2022-3-16 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

平时用Visual Studio打开工程，默认是以普通用户权限运行的。在有些情况下可能需要以Admin权限打开，比如需要attach到IIS的process的时候，普通用户权限就不够用了。  
方法一： 右键Visual Studio，以Admin权限运行然后再打开工程，这样偶尔用也还可以。如果天天这样操作就很麻烦，所以希望找另外一个方法，打开所有Visual Studio工程时都以Admin权限打开。  
方法二： 
1. 定位到Visual Studio exe所在位置   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/vs1.png?raw=true)

2. 右键，troubleshoot compatibility
3. 选择 troubleshoot program
4. 勾选 The program requires additional permissions
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/vs2.png?raw=true)
5. 点Test program，会以Admin权限运行Visual Studio
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/vs3.png?raw=true)
6. 点Next，选择Yes,save these settings for this program
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/vs4.png?raw=true)
7. Close
