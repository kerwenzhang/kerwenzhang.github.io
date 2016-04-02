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

### 编码注释：   

	# -*- coding:utf-8 -*-

### print

print带参数输出   

	int1=30
	int2=20
	str1="test"
	print("int1 is %d, int2 is %d, str1 is %s" %(int1,int2,str1))

%r可以输出任何一种格式   

	formater ="%r %r %r %r"
	print (formater % (1,2,3,4))
	print (formater % ("one", "two", "three", "four"))
	print (formater % (True, False, True, False))
	
input   
input用于获取用户的输入   

	s=input("提示信息")	

### 函数

参数   

	def function1(*args):
		arg1, arg2 = args
		print("arg1: %r, arg2: %r" % (arg1, arg2))


### import 文件
在一个文件中定义一个函数：
	def break_words(stuff):
		"""This function will break up words for us."""
		words = stuff.split(' ')
		return words
在另一个文件中可以通过import调用函数
	import xxx
	sentence ="All good things come to those who wait"
	words = function1.break_words(sentence)

调用
	help(function1.break_words)
可以得到模组帮助文档的方式，所谓帮助文档就是定义函数时放在 """ 之间的东西

### 文件读写操作：   

	fo = open(strFilePath,"r", encoding="utf-8")
	fileData = fo.readlines()
	
	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(newLinelists)	

获取一个文件夹下的指定格式文件   

	
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
		
