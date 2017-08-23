---
layout: post
title: Python文件与文件夹的操作
date:   2016-09-22 13:53:14
categories: "Python"
catalog: true
tags: 
    - Python
---



python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。   

导入的方法是:   

	import os   
	import shutil   

### 取得当前目录

	s = os.getcwd()   

### 更改当前目录

	os.chdir( "C:\\123")   

### 路径名分解

分解为目录名和文件名两部分   

	fpath , fname = os.path.split( "你要分解的路径")
	
	
	>>> a,b=os.path.split("c:\\dir1\\dir2\\file.txt")
	>>> print a
	c:\dir1\dir2
	>>> print b
	file.txt
	
分解文件名的扩展名   

	fpathandname , fext = os.path.splitext( "你要分解的路径")
	

	>>> a,b=os.path.splitext("c:\\dir1\\dir2\\file.txt")
	>>> print a
	c:\dir1\dir2\file
	>>> print b
	.txt

### 路径（目录或文件）是否存在

	b = os.path.exists( "你要判断的路径")

	
	>>> os.path.exists ("C:\\") #该路径存在
	True
	>>> os.path.exists ("C:\\123\\") #该路径不存在
	False
	>>> os.path.exists ("C:\\123.txt") #该文件不存在
	False
	>>> os.path.exists ("C:\\test.txt")  #该文件存在
	True

### 判断一个路径是否存在
	
	b = os.path.isdir( "你要判断的路径")	
	
### 判断是否是绝对路径
	
	os.path.isabs()
	
### 判断一个路径是否有需要的文件

	b = os.path.isfile( "你要判断的路径")

### 获取某目录中的文件及子目录的列表

	L = os.listdir( "你要判断的路径")
	
	>>> os.listdir("C:\\")   #这里包括隐藏文件也显示出来了

获取指定目录下的所有子目录的列表   

	
	def getDirList( p ):
		p = str( p )
		if p=="":
			return [ ]
		p = p.replace( "/","\\")
		if p[ -1] != "\\":
			p = p+"\\"
		a = os.listdir( p )
		b = [ x   for x in a if os.path.isdir( p + x ) ]
		return b
	 
	getDirList( "C:\\" )
	
获取指定目录下所有文件的列表   

	
	def getFileList( p ):
		p = str( p )
		if p=="":
			return [ ]
		p = p.replace( "/","\\")
		if p[ -1] != "\\":
			p = p+"\\"
		a = os.listdir( p )
		b = [ x   for x in a if os.path.isfile( p + x ) ]
		return b
	 
	getFileList( "C:\\" )

### 创建目录

	os.makedirs( path )   # path 是"要创建的子目录"
	
创建多级目录   

	os.makedirs（r“c：\python\test”）
	
创建以时间命名文件夹名   

	import os
	import time

	folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
	os.makedirs(r'%s/%s'%(os.getcwd(),folder))
	
### 删除目录

只能删除空目录   

	os.rmdir( path )   # path: "要删除的子目录"
	
删除多个目录   

	os.removedirs（r“c：\python”）

空目录、有内容的目录都可以删   

	
	shutil.rmtree("dir")    

### 创建空文件

	os.mknod("test.txt")        
	
### 删除文件

	os.remove(   filename )   # filename: "要删除的文件名"
	
### 重命名文件（目录）

	os.rename( oldfileName, newFilename)
	
### 获取文件大小

	os.path.getsize（filename）
	
### 打开文件

	fp = open("test.txt",w)     直接打开一个文件，如果文件不存在则创建文件

关于open 模式：   

w     以写方式打开，   
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)   
r+     以读写模式打开   
w+     以读写模式打开 (参见 w )   
a+     以读写模式打开 (参见 a )   
rb     以二进制读模式打开   
wb     以二进制写模式打开 (参见 w )   
ab     以二进制追加模式打开 (参见 a )   
rb+    以二进制读写模式打开 (参见 r+ )   
wb+    以二进制读写模式打开 (参见 w+ )   
ab+    以二进制读写模式打开 (参见 a+ )   

读取文件：

    def read_file():
        try:
            f = open("Student.txt", "r")
            for str in f.readlines():
                # do something
            f.close()
        except Exception:
            print("Could not read file.")
            
写文件：
    
    def Save_file(str):
        try:
            f=open("student.txt","a")
            f.write(str + "\n")
            f.close()
        except Exception:
            print("Could not save file.")
            

### 按时间排序目录下的文件

排序可以通过list.sort来巧妙的实现：   

	import os

	DIR = "/home/serho/workspace/lisp"

	def compare(x, y):
		stat_x = os.stat(DIR + "/" + x)
		stat_y = os.stat(DIR + "/" + y)
		if stat_x.st_ctime < stat_y.st_ctime:
			return -1
		elif stat_x.st_ctime > stat_y.st_ctime:
			return 1
		else:
			return 0

	iterms = os.listdir(DIR)

	iterms.sort(compare)

	for iterm in iterms:
		print iterm

