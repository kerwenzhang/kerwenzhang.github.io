---
layout: post
title: Clear Case 常用操作
date:   2016-04-01 08:30:03
categories: "Others"
tags: 
    - Others
	- Clear Case
---

* content
{:toc}

## Merge

在一个branch创建的文件Merge到另一个branch   
You have to merge the parent directory first, so that the file shows up in the directory in the destination branch. At this point the new file will have zero size. You can then merge the file itself. The easiest way to do both of these operations is via the Version Tree view - much less error-prone than doing it via the command line.   

## View相关

强制删除一个View   

	cleartool lsview -l theViewToRemove # get its uuid
	cleartool rmtag -view theViewToRemove
	cleartool unregister -view -uuid uuid_of_viewToRemove