---                
layout: post                
title: "搭建Squid代理服务器" 
date:   2021-05-10 22:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

## Install Ubuntu
从官网上下载最新的Ubuntu，我下载的版本是 20.04.2.0 LTS  
[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)  
用VM workstations安装  

## 安装squid  
运行Ubuntu 命令行工具`Terminal`， 执行以下命令  

    sudo apt-get install squid3

之后使用以下命令检查安装好的squid  

    squid3 -v

![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Proxy0.png?raw=true)  

## squid配置
squid默认配置文件为 `/etc/squid/squid.conf ` 默认为 `readonly`  
通过命令行使用以下命令进行编辑  

    sudo gedit /etc/squid/squid.conf   

在squid.conf的默认配置中，拒绝了所有的外部代理请求。这时候如果使用该代理，会返回错误页面    
所以要想让其他主机使用squid代理，需要在 `http_access deny all` 前面添加我们自定义的规则。  
或者直接将最后一句修改为`http_access allow all`  
修改完之后重启服务  

    service squid restart 

## 配置其他机器使用代理
首先获取Ubuntu的ip地址  
下载 `net-tools`  

    sudo apt-get install net-tools

输入命令  

    ifconfig

其中inet之后的就是ip地址  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Proxy1.png?raw=true)

在Win10上设置全局代理  
Setting -> Network & Internet -> Proxy  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Proxy2.png?raw=true)
端口默认`3128`  

## 验证
在客户机上打开浏览器，`F12` 切换到`Network` Tab, 输入任意网址， 检查`Remote Address`  
在未使用Proxy之前  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Proxy3.png?raw=true)

使用全局Proxy之后  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Proxy4.png?raw=true)

## 如何查看应用程序的网络访问

[使用squid搭建代理服务器](https://www.hawu.me/operation/852)  
[Ubuntu设置squid代理](https://www.cnblogs.com/antoon/p/4496904.html)  
[ubuntu16.04安装squid 且配置代理验证](https://blog.csdn.net/wto882dim/article/details/88905394)  