---
layout: postlayout
title: "Visual Studio 统计代码行数"
date:   2015-07-27 17:13:00 
categories: [MFC]
tags: [MFC]
---
  遇到Visual Studio 统计代码行数问题。在VS的高级版本(Premium以上)带有Code Metirc功能。<br />
  但是都是统计各个工程的，没有一个总计，搞得人很头大。不知道微软怎么设计的。所以在网上找了一个简易方案，修改了一下，统计算是比较准确了。下面是表达式：<br />
  <br />
  ^:b*[^:b\*#/]+.*$  <br />
  <br />
  VS的搜索表达式没有兼容很多通用的表达式的内容，所以如果你想修改的话，要参照其规定。<br />
  [链接地址如下]: (http://msdn.microsoft.com/zh-cn/library/2k3te2cs(v=vs.80).aspx)<br />
