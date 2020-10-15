---                
layout: post                
title: "找到指定端口占用程序" 
date:   2020-10-15 10:30:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

1.	Run CMD, input `netstat -ano|findstr "port_number"`, it will list the process using this port.  
2.	Input command `tasklist | find “process_id”` to get the process name.  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/port.png?raw=true) 

[https://stackoverflow.com/questions/61694720/issue-with-listening-at-an-endpoint-connecting-to-wcf-from-net-tcp-protocol](https://stackoverflow.com/questions/61694720/issue-with-listening-at-an-endpoint-connecting-to-wcf-from-net-tcp-protocol)