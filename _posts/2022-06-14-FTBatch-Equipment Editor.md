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
一个phase class描述的是配方里都做了什么，但不具体描述怎么做。比如冰激凌配方里有个phase class 是加牛奶(ADD_MILK)，ADD_MILK只是描述加牛奶这个动作，但没有怎么加的具体描述。   

右键ADD_MILK，弹出编辑窗口，在General页里可以编辑名字  
Parameters页里包含跟这个phase class相关的参数，通过这些参数，Batch可以向PCD发送数据<font color="red">这个是跟设备挂钩的吗？</font>      
Reports页里包含这个class的report参数，通过这些参数PCD可以向Batch发送数据。   
Message页里包含跟这个class相干的消息，主要用来troubleshooting  
如果在General页上勾选`Control Strategy`，会出现新的Tab页，用来添加控制策略。<font color="red">没懂</font>   

## Create Phase Class
1. 菜单Class -> New Phase Class,弹出创建页面  
2. Name修改成ADD_WATER,可以在图标列里选择一个合适的图标。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip3.png?raw=true)  
3. 在Paramter Tab页，添加一个新的参数,点击Apply  
Name: ADD_AMOUNT  
Default:  50  
Enum/E.U. :  KG  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip4.png?raw=true)  
4. 在Reports Tab页添加一个新的Report，点击Apply  
Name: AMOUNT_ADDED  
Enum/E.U. : KG  
5. 点OK，新的Phase类会在左侧类面板上出现。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip5.png?raw=true)  

## Create Phase
当一个Phase类被添加到一个Unit的时候，它就变成了一个Phase实例。 一个unit里只能有一个phase类的实例。当需要在多个unit里使用同一个phase时，在unit之间共享该phase，或者创建多个phase实例并且取不同的名字。    
如果在使用`material-enabled phase classes`, 则可以在一个unit里创建多个同一phase class的实例。  

## 查看Phase的设定  
1. 右键点击WP_ADD_CREAM_M1，弹出编辑窗口。  
2. 在General页上，可以配置Name，设备ID，Data Server名字，Auto Download/Auto Upload  
3. Arbitration(仲裁)页<font color="red">不知道这个页面是做什么的</font>  
4. Cross Invocation(交叉调用)页，<font color="red">跟Batch View和ActiveX控件有关，但不知道具体作用</font>   
5. Tag页显示Phase定义的所有tag点<font color="red">从哪来的？</font>。  
6. Parameter Limit Tags页，<font color="red">没懂</font>。  
7. Report Limit Tags页，<font color="red">没懂</font>。  
8.  Containers页，material-enabled phases才会有。   
9. 点Cancel   

## 查看Batch Tags
Batch 使用Phase tag来连接PCD中的phase logic。 Phase logic是指挥工厂中真实设备的实时命令(real-time commands)  
1. 右键WP_AGITATE_M1,弹出编辑窗口  
2. 选择Tags页， 列出跟该phase相关的所有phase tags。  
3. 选中`COMMAND`Tag，双击，弹出编辑窗口。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip6.png?raw=true)  
在`Item Name` 里是tag的地址，这是在PCD中定义的。这里我们使用的是模拟器中Tag(OPC_SIM).
4. 点Cancel，不修改任何设定。  

## 创建一个Phase
1. 在左侧选择`ADD_WATER` phase类，鼠标移到右侧设计视图时，鼠标形状发生变化，在空白区域点一下左键就会创建一个实例，弹出编辑窗口。  
2. Data Server选择OPC_SIM（默认）  
3. 把名字修改成WP_ADD_WATER_M1，正常情况下还需要配置tag点，但我们用的模拟器，所以不需要。  
4. 点OK. 一个新的Phase就创建成功了。  

# 签名模板
## 创建一个模板

1. 菜单选择Edit -> Signature Templates弹出编辑窗口。  
2. 点New Template按钮，创建一个新的Template  
3. 将名字修改为CommandsTemplate,点OK,新创建的模板已经添加进去了。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip7.png?raw=true)  
4. `Signoffs Required` 选择1 (this is the number of signatures that must be obtained for this signature template).  
5. 切到Signoffs页，在`Template Name` 里选择`CommandsTemplate`  
6. `Signoff`列表选择1 (this represents the Signoff you are going to configure.)  
7. 在`Meaning`里输入Authorizes commands.  
8. `Comment`选Optional.  
9. `Security Permissions`点Add按钮添加用户，选择ShowAll，点选OPER，点击OK  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip8.png?raw=true)  
10. 点OK，保存模板  

## 使用签名模板
1. 在Edit菜单里选Command Policies，弹出编辑窗口.  
2. 勾选Start，弹出模板选择窗口.  
3. 我们只创建了一个模板，所以它被默认选中了，点OK  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/equip9.png?raw=true)  
4. 点 OK退出.  
5. 点File -> Save 保存，弹出Comments窗口，无视     

## 在配方里使用签名模板
在 Edit 菜单里选 `Recipe Approvals Configuration` 