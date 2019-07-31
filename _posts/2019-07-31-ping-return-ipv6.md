---                
layout: post                
title: "ping 返回IPV6地址"                
date:   2019-7-31 14:30:00                 
categories: "Other"                
catalog: true                
tags:                 
    - Other                
---      

在ping一台局域网虚拟机时发现总是返回IPV6的地址  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/ping_ipv4.jpg?raw=true)

解决方案1：

在ping时添加一个 `-4` 后缀
![IMG](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/ping_ipv4_cmd.jpg?raw=true)

方案2： 

open an elevated Command Prompt, and execute 2 commands:  

    netsh interface ipv6 set prefix ::/96 60 3
    netsh interface ipv6 set prefix ::ffff:0:0/96 55 4

Reference:  
[https://theitbros.com/ping-returns-ipv6-address-ping-ipv4/](https://theitbros.com/ping-returns-ipv6-address-ping-ipv4/)