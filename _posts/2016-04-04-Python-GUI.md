---
layout: post
title: Python GUI 编程各种实现的对比
date:   2016-04-04 19:30:03
categories: "Python"
tags: 
    - Python
---

* content
{:toc}

从 Python 语言的诞生之日起，就有许多优秀的 GUI 工具集整合到 Python 当中，这些优秀的 GUI 工具集，使得 Python 也可以在图形界面编程领域当中大展身手，由于 Python 的流行，许多应用程序都是由 Python 结合那些优秀的 GUI 工具集编写的。下面分别介绍 Python GUI 编程的各种实现，下面的许多内容都是来自维基百科，这里就当做是一个没有技术色彩的整合吧。   

## Tkinter

简单介绍：   
是绑定了 Python 的 Tk GUI 工具集 ，就是Python 包装的Tcl代码，通过内嵌在 Python 解释器内部的 Tcl 解释器实现， Tkinter   
的调用转换成 Tcl 命令，然后交给 Tcl 解释器进行解释，实现 Python 的 GUI 界面。   
对比Tk和其它语言的绑定，比如 PerlTk ，是直接由 Tk 中的 C 库实现的。   

优点：   

历史最悠久， Python 事实上的标准 GUI ， Python 中使用 Tk GUI 工具集的标准接口，已经包括在标准的 Python Windows 安   
装中，著名的 IDLE 就是使用 Tkinter 实现 GUI 的创建的 GUI 简单，学起来和用起来也简单。   

## wxPython

简单介绍：   

Python 对跨平台的 GUI 工具集 wxWidgets （ C++ 编写）的包装，作为 Python 的一个 扩展模块实现。   

优点：   

比较流行的一个 Tkinter 的替代品，在 各种平台下都表现挺好。   

## PyGTK

简单介绍：   

一系列的 Python 对 GTK+ GUI 库的包装。   

优点：   

比较流行的一个 Tkinter 的替代品，许多 Gnome 下的著名应用程序的 GUI 都是使用 PyGTK 实现的，比如 BitTorrent ， GIMP   
和 Gedit 都有可选的实现，在 Windows 平台 似乎表现不太好，这点也无可厚非，毕竟使用的是 GTK 的 GUI 库。   

## PyQt

简单介绍：   

Python 对跨平台的 GUI 工具集 Qt 的包装实现了 440 个类以及 6000 个函数或者方法 ，PyQt 是作为 Python 的插件实现的。   

优点：   

比较流行的一个 Tkinter 的替代品，功能 非常强大，可以用Qt开发多美漂亮的界面，也就可以用PyQt开发多么漂亮的界面。   
跨平台的支持很好，不过在商业授权上似乎存在一些问题, 写商业程序需要购买商业版授权.   

## PySide

简单介绍：   

另一个 Python 对跨平台的 GUI 工具集 Qt 的包装，捆绑在 Python 当中，最初由 BoostC++ 库实现，后来迁移到 Shiboken。