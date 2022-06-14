---                
layout: post            
title: "FactoryTalk Batch入门2：Equipment Editor"                
date:   2022-6-14 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

# Equipment Editor 简介
FactoryTalk Batch Equipment Editor 是用于配置设备和相关功能以生成设施区域模型的组件。 FactoryTalk Batch Equipment Editor 中定义的组件与设施中的过程连接设备 (PCD) 交互。
如 ISA S88.01标准中所述，工厂的区域模型分为以下物理组件：
• 处理单元 Process Cell
• 单元 Unit
• 阶段 Phase
• 控制模块 Control Module
要构建区域模型，需要先建立这些组件。 除了区域模型之外，FactoryTalk Batch Equipment Editor 还允许指定通信功能、枚举集enumeration sets、数据服务器、FactoryTalk Event Archiver 功能以及配置 FactoryTalk Batch Server 选项

# 操作
1. 打开Equipment Editor：点击开始菜单 > Rockwell Software > Equipment Editor. 默认打开空白的页面。在主窗体左侧是类视图 Classes View，右侧是设计视图 Design View。  
2. 打开示例的区域模型。点击菜单 File > Open, 选择ice_cream1.cfg, 左侧类视图里显示名为`PARLOR`的处理单元类，右侧设计视图里为处理单元实例`WEST_PARLOR`.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip1.png?raw=true)

在类视图里显示的是在当前区域模型里已经存在的cell类，Unit类，Phase类以及操作顺序类(operation sequence classes)，列头显示的是当前的level是cell/unit还是phase，双击或者右键一个图标会打开编辑窗口。<font color="red">双击打开编辑窗口这个设定还挺奇怪的</font>    
design视图里是用来构建整个区域模型，并且显示当前level的布局。双击一个图标可以进到下一个level,左侧的类视图会显示对应level的类，右键打开编辑窗口。  
可以在设计视图里把完整路径页显示出来。View -》 Location Bar  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip2.png?raw=true)  

使用工具栏里的向上向下箭头在不同层级之间切换。  

# Phase Class
阶段类(Phase class) 是一个可重用的面向过程的功能模块，比如加热，搅拌，添加。把一个阶段类添加到设计视图里，就生成了一个阶段实例(Phase instance).  
一个phase class描述的是配方里都做了什么，但不具体描述怎么做。比如冰激凌配方里有个phase class 是加牛奶(ADD_MILK)，ADD_MILK只是描述加牛奶这个动作，但没有加牛奶这个过程的具体描述。   

右键ADD_MILK，弹出编辑窗口，在General页里可以编辑名字  
Parameters页里包含跟这个phase class相关的参数，通过这些参数，Batch可以向PCD发送数据<font color="red">这个是跟设备挂钩的吗？</font>      
Reports页里包含这个class的report参数，通过这些参数PCD可以向Batch发送数据。   
Message页里包含跟这个class相干的消息，主要用来troubleshooting  
如果在General页上勾选`Control Strategy`，会出现新的Tab页，用来添加控制策略。<font color="red">没懂</font>   

