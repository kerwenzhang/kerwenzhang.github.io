---
layout: post
title: Notepad++配置Python开发环境
date:   2016-03-27 18:54:03
categories: "Python"
catalog: true
tags: 
    - Python
---

* content
{:toc}

## 安装Python

我选择了32位的2.7版本。https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi   

安装的时候可以修改安装路径到D盘，然后注意一点是可以将最后一项“配置环境变量”勾选上（默认是不选择的），这样就不用手动配置环境变量了。   

## 配置Notepad++

1. Notepad++ ->"运行"菜单->"运行"按钮   

2. 在弹出的窗口内输入以下命令：   

	cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT

然后点击“保存”，随意取一个名字，比如“RunPython”，为方便，配置一下快捷键（比如 Ctrl + F5），点OK即可。之后运行Python文件只要按配置的快捷键或者在运行菜单上点“RunPython”即可。   
注意不要跟已有的快捷键冲突。查看已有的快捷键，可以点击"运行"菜单->"管理快捷键"按钮 查看   

## 命令解释

	cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
	
cmd /k python： 表示打开Cmd窗口，运行/k后边的命令，并且执行完毕后保留窗口。此处即python（因为在环境变量里已经添加了Python目录，所以这里不用指定Python程序的目录，就可直接找到）   

$(FULL_CURRENT_PATH) ：Notepad++的宏定义，表示当前文件的完整路径。   

& 用来连接多条命令   

ECHO：换行   

PAUSE： 表示运行结束后暂停（cmd中显示“请按任意键继续. . .”），等待一个按键继续   

EXIT： 表示“按任意键继续. . .”后，关闭命令行窗口。   

## Notepad++宏定义的含义

可以参考Notepad++自带的帮助文档。   

点击“？”菜单->“帮助”按钮（或者Shift+F1快捷键）->在打开的页面中点击右面的“Commands”，可以查看到各个宏定义的含义   


	FULL_CURRENT_PATH

　　	the fully qualified path to the current document.   

	CURRENT_DIRECTORY

　　	The directory the current document resides in.   

	FILE_NAME

　　	The filename of the document, without the directory.   

	NAME_PART

　　	The filename without the extension.   

	EXT_PART
	　　The extension of the current document.
	NPP_DIRECTORY
	　　The directory that contains the notepad++.exe executable that is currently running.
	CURRENT_WORD
	　　The currently selected text in the document.
	CURRENT_LINE
	　　The current line number that is selected in the document (0 based index, the first line is 0).
	CURRENT_COLUMN
	　　The current column the cursor resides in (0 based index, the first position on the line is 0).
	
## 测试

创建一个测试文件，保存为DemoRun.py。   

	import platform;
	   
	print "Just for demo how to do python development under windows:";
	print "Current python version info is %s"%(platform.python_version());
	print "uname=",platform.uname();
	
Ctrl + F5执行，看是否能输出结果。   

## 问题

1. 当Python脚本需要创建文件或目录时，执行脚本，发现在脚本所在的目录下没有生成的文件或目录，查找一下的话，发现生成的文件在Notepad++的安装目录下。比如下面的脚本，想在脚本所在的目录下，创建一个子目录“testdir”   

	# create directory

	import os
	CurPath = os.path.abspath('.')
	print CurPath
	JoinPath = os.path.join( CurPath, 'testdir')
	print JoinPath
	os.mkdir( JoinPath )

发现在脚本所在的目录下没有，而在“D:\Program Files (x86)\Notepad++”下却生成了一个“testdir”文件夹。   

2. 原因何在呢？使用下面的代码打印当前工作目录：   

	import os
	print os.getcwd()
	
显示的是Notepad++的安装目录，因此确定是工作目录的问题。改进后的命令行是：   

	cmd /k cd "(CURRENT_DIRECTORY)" &  python "(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT

该命令行的含义是：首先cd 到该要执行的Python脚本所在的目录（CURRENT_DIRECTORY），在该目录下，执行 python程序，这样工作目录就由默认的Notepad++的安装目录，改为了该要执行的Python脚本所在的目录。   

3. 修改命令行   

想要将原来的命令行修改为改进后的命令行，发现Notepad++并没有提供修改的功能   

	cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
	->

	cmd /k cd "(CURRENT_DIRECTORY)" &  python "(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
	
想要修改，有2种办法   

（1）点击"运行"菜单->"管理快捷键"按钮后，删除原来的快捷键，然后重新建一遍。   

（2）修改shortcuts.xml。注意shortcuts.xml的路径有可能为“C:\Users\XXX\AppData\Roaming\Notepad++”下的shortcuts.xml，而并不是“D:\Program Files (x86)\Notepad++”下的shortcuts.xml   

4. 但是这样还有一个问题，就是如果Python脚本所在的目录和Notepad++的安装目录不再一个分区，那么改进后的命令行失效。比如，Notepad++安装在D盘，要执行的脚本在E盘，那么运行下面的测试脚本：   

	import os
	print os.getcwd()

打印当前工作目录仍旧是“D:\Program Files (x86)\Notepad++”。   

这个问题没有解决。