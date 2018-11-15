---                                  
layout: post                                  
title: "VM虚拟机局域网搭建"                                  
date:   2018-11-15 14:00:00                                   
categories: "Others"                                  
catalog: true                                  
tags:                                   
    - Others                                  
---                        
    

## vmnet0  

vmnet0，实际上就是一个虚拟的网桥，这个网桥有很若干个端口，一个端口用于连接你的Host，一个端口用于连接你的虚拟机，他们的位置是对等的，谁也不是谁的网关。所以在Bridged模式下，你可以让虚拟机成为一台和你的Host相同地位的机器。 

## vmnet1  

vmnet1，这是一个Host-Only网络模式，这是用于建立一个与世隔绝的网络环境所用到的，其中vmnet1也是一个虚拟的交换机，交换机的一个 端口连接到你的Host上，另外一个端口连接到虚拟的DHCP服务器上（实际上是vmware的一个组件），另外剩下的端口就是连虚拟机了。  
虚拟网卡 “VMWare Virtual Ethernet Adapter for VMnet1”作为虚拟机的网关接口，为虚拟机提供服务。在虚拟机启动之后，如果你用ipconfig命令，你会很清楚的看到，你的默认网关就是指向 “VMWare Virtual Ethernet Adapter for VMnet1”网卡的地址的。（实际上它并不能提供路由，这是VMware设计使然，它是干了除了提供路由之外的一些事情——实际上是我也不知道它干了什 么事情），这里没有提供路由主要表现在没有提供NAT服务，使得虚拟机不可以访问Host-Only模式所指定的网段之外的地址。    

## vmnet8  

vmnet8，这是一个NAT方式，最简单的组网方式了，从主机的“VMWare Virtual Ethernet Adapter for VMnet8”虚拟网卡出来，连接到vmnet8虚拟交换机，虚拟交换机的另外的口连接到虚拟的NAT服务器（这也是一个Vmware组件），还有一个口 连接到虚拟DHCP服务器，其他的口连虚拟机，  
虚拟机的网关即是“VMWare Virtual Ethernet Adapter for VMnet8”网卡所在的机器，废话，这肯定就是你的Host机器啦。同样，用ipconfig也可以看出来，你的虚拟机的默认网关也指向了你的 “VMWare Virtual Ethernet Adapter for VMnet8”虚拟网卡地址。相比之下，可以看出来，NAT组网方式和Host-Only方式，区别就在于是否多了一个NAT服务。   

## 用NAT组局域网  

1. 查看VM主机网络配置: 编辑->虚拟网络编辑器->NAT设置。 记录下网关的IP地址  

2. 配置宿主机VMnet8 ip: 使用静态IP， 修改网关IP地址， DNS地址与网关IP保持一致  

3. 配置虚拟机，经虚拟机网络设置为NAT方式  

4. 配置虚拟机ip, 将IP设置为静态IP， 保证宿主机和虚拟机的IP地址在同一地址段。网关和DNS地址与宿主保持一致。  

5. 关掉虚拟机防火墙  


    
[https://blog.csdn.net/qq_26182959/article/details/78459831](https://blog.csdn.net/qq_26182959/article/details/78459831)