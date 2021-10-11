---                
layout: post                
title: "如何在VMware Workstations上安装windows11" 
date:   2021-10-11 15:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

Windows 11 已经于 10月4日正式发布，在VMware Workstations 15.5.2 上安装时会提示没有满足最小安装需求

    This PC doesn't meet the minimum system requirements to install this version of Windows. For more informaiton, visit https://aka.ms/WindowsSysReq


![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/win11.png?raw=true)  


解决方法：
1. 按Shift+F10，调出 cmd窗口  
2. 输入regedit，调出注册表窗口  
3. 定位到HKEY_LOCAL_MACHINE\SYSTEM\SETUP，创建子健LabConfig  
4. 定位到LabConfig, 在右边新建以下四个 DWORD 值, Data都是1  

    BypassTPMCheck
    BypassCPUCheck
    BypassRAMCheck
    BypassSecureBootCheck

5. 关掉注册表和cmd窗口，然后关掉windows安装错误提示窗口  
6. 回到Install Now界面，重新选择edition  

## 参考
[How to Fix Cannot Install Windows 11 on VMware Workstation | Windows 11 VMware Not Meet Requirements](https://www.youtube.com/watch?v=sCLJYNI77Bk&ab_channel=TeeVee)  