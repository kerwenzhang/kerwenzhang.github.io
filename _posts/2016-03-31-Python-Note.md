---
layout: post
title: Python学习笔记
date:   2016-03-31 16:30:03
categories: [Python]
tags: [Python]
---

* content
{:toc}

Python入门教程， 提供了很多的实例，但是基于Python2.0 的， 目前Python已经更新到Python3.5，里面的一些函数（如Print）已经不一样了。   
[笨办法学Python](http://www.jb51.net/shouce/Pythonbbf/latest/index.html)   

编码注释：   

	# -*- coding:utf-8 -*-

文件读写操作：   

	fo = open(strFilePath,"r", encoding="utf-8")
	fileData = fo.readlines()
	
	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(newLinelists)	

获取一个文件夹下的制定格式文件   

	
	''''' 

	#获取目录中指定的文件名 

	#>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 

	#>>>FileList=GetFileList(FindPath,FlagStr) # 

	'''  
	def GetFileList(FindPath,FlagStr=[]):  
		
		import os  
		FileList=[]  
		FileNames=os.listdir(FindPath)  
		if (len(FileNames)>0):  
		   for fn in FileNames:  
			   if (len(FlagStr)>0):  

				   #返回指定类型的文件名  

				   if (IsSubString(FlagStr,fn)):  
					   fullfilename=os.path.join(FindPath,fn)  
					   FileList.append(fullfilename)  
			   else:  

				   #默认直接返回所有文件名  

				   fullfilename=os.path.join(FindPath,fn)  
				   FileList.append(fullfilename)  
	  
		#对文件名排序  

		if (len(FileList)>0):  
			FileList.sort()  
	  
		return FileList  
		
