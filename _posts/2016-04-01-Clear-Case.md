---
layout: post
title: Clear Case 常用操作
date:   2016-04-01 08:30:03
categories: "Clear Case"
catalog: true
tags: 
    - Clear Case
---



## Merge

#### Merge文件

在一个branch创建的文件Merge到另一个branch   
You have to merge the parent directory first, so that the file shows up in the directory in the destination branch. At this point the new file will have zero size. You can then merge the file itself. The easiest way to do both of these operations is via the Version Tree view - much less error-prone than doing it via the command line.   

#### Merge Folder

在一个branch创建了文件夹，然后删掉， 在另一个branch创建同名文件夹时会报错，提示在某个branch已经存在同名文件夹。  
先找到提示的branch\tag, 创建一个dynamic view，然后选择该文件夹的父节点， check out， 选择手动merge， 将文件夹的创建动作merge到最新的branch。  
注意一定要选择手动merge， 自动merge不会在新的branch上创建文件夹。   

## View相关

强制删除一个View   

	cleartool lsview -l theViewToRemove # get its uuid
	cleartool rmtag -view theViewToRemove
	cleartool unregister -view -uuid uuid_of_viewToRemove