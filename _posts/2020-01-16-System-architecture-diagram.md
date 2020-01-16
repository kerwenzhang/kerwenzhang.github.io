---                
layout: post                
title: "系统架构图" 
date:   2020-01-16 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

## 基本概念
### 什么是架构

架构就是对系统中的实体以及实体之间的关系所进行的抽象描述，是一系列的决策。  
架构是结构和愿景。  
系统架构是概念的体现，是对物/信息的功能与形式元素之间的对应情况所做的分配，是对元素之间的关系以及元素同周边环境之间的关系所做的定义。   


### 什么是架构图

系统架构图是为了抽象地表示软件系统的<font color="red"><strong>整体轮廓</font></strong>和各个组件之间的<font color="red"><strong>相互关系和约束边界</font></strong>，以及软件系统的<font color="red"><strong>物理部署</font></strong>和软件系统的演进方向的整体视图。  


### 架构图的作用

一图胜千言。要让干系人理解、遵循架构决策，就需要把架构信息传递出去。架构图就是一个很好的载体。那么，画架构图是为了：  

达成共识  
减少歧义  

## 构图分类

架构图的分类有很多，有一种比较流行的是4+1视图，分别为场景视图、逻辑视图、物理视图、处理流程视图和开发视图。  

### 场景视图

场景视图用于描述系统的参与者与功能用例间的关系，反映系统的最终需求和交互设计，通常由<strong>用例图</strong>表示。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system1.jpg?raw=true)

### 逻辑视图

逻辑视图用于描述系统软件功能拆解后的组件关系，组件约束和边界，反映系统整体组成与系统如何构建的过程，通常由UML的<strong>组件图和类图</strong>来表示。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system2.jpg?raw=true)

### 物理视图

物理视图用于描述系统软件到物理硬件的映射关系，反映出系统的组件是如何部署到一组可计算机器节点上，用于指导软件系统的部署实施过程。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system3.jpg?raw=true)


### 处理流程视图

处理流程视图用于描述系统软件组件之间的通信时序，数据的输入输出，反映系统的功能流程与数据流程,通常由<strong>时序图和流程图</strong>表示。   

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system4.jpg?raw=true)

### 开发视图

开发视图用于描述系统的模块划分和组成，以及细化到内部包的组成设计，服务于开发人员，反映系统开发实施过程。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system5.jpg?raw=true)


以上 5 种架构视图从不同角度表示一个软件系统的不同特征，组合到一起作为架构蓝图描述系统架构。  


## 怎样的架构图是好的架构图

在画出一个好的架构图之前， 首先应该要明确其受众，再想清楚要给他们传递什么信息 ，所以，不要为了画一个物理视图去画物理视图，为了画一个逻辑视图去画逻辑视图，而应该根据受众的不同，传递的信息的不同，用图准确地表达出来，最后的图可能就是在这样一些分类里。那么，画出的图好不好的一个直接标准就是：受众有没有准确接收到想传递的信息。   

明确这两点之后，从受众角度来说，一个好的架构图是不需要解释的，它应该是自描述的，并且要具备一致性和足够的准确性，能够与代码相呼应。  

## C4模型

C4 模型使用容器（应用程序、数据存储、微服务等）、组件和代码来描述一个软件系统的静态结构。这几种图比较容易画，也给出了画图要点，但最关键的是，我们认为，它明确指出了每种图可能的受众以及意义。  

### 语境图(System Context Diagram)

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system6.jpg?raw=true)

用途  

这样一个简单的图，可以告诉我们，要构建的系统是什么；它的用户是谁，谁会用它，它要如何融入已有的IT环境。这个图的受众可以是开发团队的内部人员、外部的技术或非技术人员。  

怎么画   

中间是自己的系统，周围是用户和其它与之相互作用的系统。这个图的关键就是梳理清楚待建设系统的用户和高层次的依赖，梳理清楚了画下来只需要几分钟时间。  

### 容器图(Container Diagram)

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system7.jpg?raw=true)

用途  

这个图的受众可以是团队内部或外部的开发人员，也可以是运维人员。用途可以罗列为：  

1. 展现了软件系统的整体形态  
2. 体现了高层次的技术决策  
3. 系统中的职责是如何分布的，容器间的是如何交互的  

怎么画  

用一个框图来表示，内部可能包括名称、技术选择、职责，以及这些框图之间的交互，如果涉及外部系统，最好明确边界。  


### 组件图(Component Diagram)

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system8.jpg?raw=true)

用途   

这个图主要是给内部开发人员看的，怎么去做代码的组织和构建。其用途有：  
描述了系统由哪些组件/服务组成  


### 类图(Code/Class Diagram)

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/system9.jpg?raw=true)
