---                
layout: post            
title: "FactoryTalk Batch入门1：启动Batch Server"                
date:   2022-6-8 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

FTBatch在安装的时候，会在安装目录(`C:\Program Files (x86)\Rockwell Software\Batch`)下创建一个名为`BATCHCTL`的共享文件夹，里面包含`SampleDemo1`和`SampleDemo2`两个Demo工程.   
我们以Demo1为例.在SampleDemo1文件夹下有五个文件夹

|文件夹名|说明|  
| --- | ----------- |
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
Batch Server只是一个Windows服务，在我们启动服务之前我们要做一些配置，这些配置是在FTBatch Equipment Editor里。<font color="red">为啥是在这？没太懂。。。</font>  
1. 点击开始菜单 > Rockwell Software > Equipment Editor  
2. 在主界面的菜单里选择 Options > Server Options.默认显示`Project Settings`Tab页  
3. 这里有几个关键配置项：Primary Journal,Error Logging, Equipment Database, Recipe Directory.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server9.png?raw=true)  
默认已经选择了DEMO1，可以保持不动。 点击右边的省略号，会弹出文件夹选择框，默认定位到`BATCHCTL`共享文件夹。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server10.png?raw=true)  

Equipment Databas路径我们选的是ice_cream1.cfg，这里边描述了做冰激凌所用的设备信息。  

4. Restart Control tab页里配置重启方式。<font color="red">这里指的是设备？还是Batch Server? 又或者整个生产线?</font>  
用户手册里把Restart Type改成了Warm Restart. 把Secondary Path配置到了Bin文件夹。不知道原因，先照着来吧。。。   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server11.png?raw=true)  

5. Batch Reporting tab页里默认是Leave Never (No Queue)，也不知道这几个选项有啥区别，再说再说。。。   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server12.png?raw=true)  

6. 点击OK保存，之后退出Equipment Editor

# 重建配方目录
Server配置完了之后需要重建一下配方<font color="red">???为啥</font>,可能是需要保证在Server启动前配方没有什么严重问题。  
重建配方需要用到Recipe Editor  
1. 点击开始菜单 > Rockwell Software > Recipe Editor， 一打开就要求我们验证当前加载的配方，选择Cancel。    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server13.png?raw=true)  

2. 选择菜单File > Rebuild Recipe Directory. 重建完成之后有如下提示  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server14.png?raw=true) 
点OK,弹出如下窗口，要求我们对刚才的修改加Comments，无视   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server15.png?raw=true) 
点Yes，验证我们的配方.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server16.png?raw=true) 
3. 检查完之后有如下提示，点Accept。   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server17.png?raw=true) 
同样弹出Audit comments窗口，无视无视。。。   
4. 点Close，关掉验证窗口  
5. File > Exit退出Recipe Editor.  

# 启动Batch Server
终于到了Server启动。。。   
1. 开始菜单 > Rockwell Software > Batch Service Manager，这界面风格无力吐槽。。。   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server18.png?raw=true) 
2. 确认机器名字是当前机器    
3. 服务列表里选FactoryTalk Batch Server，这是默认选项  
4. 因为产品没有激活，勾选 Allow Demo Mode，在Demo mode下，Server启动两个小时候自动停止。     
5. 下边有server的重启方式 Cold, Warm, Warm All，<font color="red">跟Equipment Editor里的restart配置有什么区别？</font>  
6. 点Start/Continue启动Server,大概一分钟左右变成这样      
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server19.png?raw=true) 
同时后边有弹出一个新的窗口，这是接下来要讲的模拟器，Server启动的时候因为我们选的Demo1，模拟器被自动调起来了。<font color="red">怎么做到的？</font>   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server20.png?raw=true) 
7. 在Server Details里可以看到一些Server的详细信息。`PCD Communications`tab页里显示的是与底层设备通信状态<font color="red">？？？</font>状态是`PHASES GOOD`    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server21.png?raw=true) 
8. 点击Start, 开始验证Tag，状态切成`IN PROGRESS`，一段时间后提示`COMPLETED`    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/server22.png?raw=true) 
9. 在Batch Service Manager界面上点Close，不会影响Server的运行状态。  

# 启动Batch阶段模拟器
1. 在启动Batch Server的时候模拟器就自动被调起来了，如果没有，开始菜单 > Rockwell Software > Simulator  
2. 标题栏上已经显示出当前运行的配方名字。如果没有运行，可以选择File > Open，定位到Program Files > Rockwell Software > Batch > SampleDemo1 > Recipes 选择ice_cream1.sim  
3. 最小化模拟器  