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

## 如何占用一个端口
这个听起来有点无厘头，更多的是用来测试用。  
当指定端口被占用时，需要提示给用户。在进行测试的时候，需要先把指定端口占住。找到一个小工具`PortListener`  
下载地址：  
[http://www.rjlsoftware.com/software/utility/portlistener/download.shtml](http://www.rjlsoftware.com/software/utility/portlistener/download.shtml)

[https://stackoverflow.com/questions/61694720/issue-with-listening-at-an-endpoint-connecting-to-wcf-from-net-tcp-protocol](https://stackoverflow.com/questions/61694720/issue-with-listening-at-an-endpoint-connecting-to-wcf-from-net-tcp-protocol)