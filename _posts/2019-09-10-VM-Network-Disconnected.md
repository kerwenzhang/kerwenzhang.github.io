---                
layout: post                
title: "the tcp/ip netbios helper service was successfully sent a stop control"                
date:   2019-9-10 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

在注册表中有一下info信息

    The TCP/IP NetBIOS Helper service was successfully sent a stop control. The reason specified was: 0x40030011 [Operating System: Network Connectivity (Planned)]__

解决方法：

goto Device Manager -> Network Adapter -> unselect checkbox "Allow the computer to turn off this device to save power" in Power Management tab.
[reference1](https://answers.microsoft.com/en-us/windows/forum/windows_7-networking/network-randomly-drops-the-tcpip-netbios-helper/a5e0a261-8344-45b2-af3a-75a45332a2ed)