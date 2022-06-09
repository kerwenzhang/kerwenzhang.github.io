---                
layout: post            
title: "FactoryTalk Batch实操1：启动Batch Server"                
date:   2022-6-8 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

FTBatch在安装的时候，会在安装目录(`C:\Program Files (x86)\Rockwell Software\Batch`)下创建一个名为`BATCHCTL`的共享文件夹，里面包含`SampleDemo1`和`SampleDemo2`两个Demo工程.   
我们以Demo1为例.在SampleDemo1文件夹下有五个文件夹
|文件夹名|说明|  
|---|---|  
|instructions||  
|journals||  
|logs|日志，失败的时候可以先检查这里边的log输出|  
|recipes|存储配方|  
|restart||  

在运行实例工程前，需要做以下准备工作:  
1. 在FTSP里添加配置Security账户  
2. 配置Batch Server运行Demo1工程  
3. 验证配方  

# 添加Security账户  
1. 开始菜单 -> Rockwell Software > FactoryTalk Administration Console.   
2. Directory框弹出，选择Network，如果是remote到另外要给Directory Server上，需要输入用户名和密码。因为我把FTSP和Batch装到了一台机器上，所以就自动登录了。   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server1.png?raw=true)
3. 登录之后到Admin console主界面，在左侧树里面找到`Users and Groups`并展开，右键`Users`，选择添加新的`FactoryTalk User`  
  ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server2.png?raw=true)
4. 在General tab页上输入以下信息  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server3.png?raw=true)  
5. 同样的方式在创建一个ENG账户  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server4.png?raw=true)  

# 配置Security policy
接下来对我们的账户进行权限的设定。  
1. 在Admin Console中，依次展开System > Policies > Product Policies > Batch > Equipment Editor > Access Modes  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server5.png?raw=true)  
2. 右键选择属性，点击`Full Edit`右边的...,点击`Add`添加账户  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server6.png?raw=true)  
3. 在`Filter Users`里勾选`Show all`，选中ENG,直接点OK  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server7.png?raw=true)  
4. 回到上一个界面之后，发现ENG账户已经加进来了,点OK关掉`Full Edit`的设置。    
5. 类似的操作，在`View Only`里添加OPER账户  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server8.png?raw=true)  

# 配置 Batch Server

# 重建配方目录

# 启动Batch Server

# 启动Batch阶段模拟器