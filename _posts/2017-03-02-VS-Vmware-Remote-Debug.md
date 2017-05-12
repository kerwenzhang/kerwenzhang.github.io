---
layout: post
title: "Visual Studio + Vmware 远程调试"
date:   2017-03-02 10:30:00 
categories: "Others"
catalog: true
tags: 
    - Others
    - VS
---



配置：  
Visual Studio 2013 装在了host机上， 想remote debug Vmware机器中的程序。  
1. 将Vmware 的network 配置改为NAT   
2. 尝试在vmware中ping主机的ip， 应该能ping通  
3. 在host机上ping虚拟机， 如果ping不通，参考第4-9步  
4. 将host和vmware的防火墙都关闭  
5. 将vmware的ip改为自动获取  
6. host机上网络设置-》 本地连接 -》 属性 -》 将VmWare Bridge Protocol 设为Enable  
7. host机上网络设置-》 左侧 更改适配器设置 -》 将VMware Network Adapter Vmnet8设为Enable，并且将Vmnet8的ip设为自动获取  
8. host机上cmd -》　ipconfig， 查看Vmnet8的ip，应该和vmware的ip在同一个网段  
9. host机上ping虚拟机， 应该能ping通  
10. 将Remote debug的文件拷贝到虚拟机  
11. 右键点击 msvsmon.exe, run as Administrator    
12. 如果遇到连接失败Authentication问题， 菜单栏 Tools -> Options -> 将Windows认证改为No Authentication     
13. 勾选 Allow any user to debug    