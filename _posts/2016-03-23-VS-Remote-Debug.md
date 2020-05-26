---
layout: post
title: "Visual Studio 远程调试"
date:   2016-03-23 11:30:00 
categories: "VS"
catalog: true
tags: 
    - VS
---



第一步：将vs工具里的Remote Debugger文件夹拷贝到目标机器。大致的目录应该是：C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\Remote Debugger，或者从开始菜单那里可以找到它的快捷方式   

第二步：在测试机上打开Remote Debugger文件夹，如果要调试的程序是32位的就运行X86里面的msvsmon.exe，如果是64位的就运行X64里面的msvsmon.exe。   

运行后会出现一个远程调试监视器的界面   

第三步： 用VS 打开程序源码，用快捷键Ctrl + Alt + P 打开附加进程窗体。   

第四步： 点击“浏览” 按钮，选择你要调试的测试机名字   

第五步： 点击“刷新”， 选择你要测试的应用程序名字，点击“附加”
