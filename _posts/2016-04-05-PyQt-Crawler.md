---
layout: post
title: PyQt 爬虫入门笔记
date:   2016-04-04 19:36:03
categories: [Python]
tags: [PyQt]
---

* content
{:toc}

## 基础介绍

抓取网页的过程其实和读者平时使用IE浏览器浏览网页的道理是一样的。   
比如说你在浏览器的地址栏中输入    www.baidu.com    这个地址。   
打开网页的过程其实就是浏览器作为一个浏览的“客户端”，向服务器端发送了 一次请求，把服务器端的文件“抓”到本地，再进行解释、展现。   
HTML是一种标记语言，用标签标记内容并加以解析和区分。   
浏览器的功能是将获取到的HTML代码进行解析，然后将原始的代码转变成我们直接看到的网站页面。   

爬虫最主要的处理对象就是URL，它根据URL地址取得所需要的文件内容，然后对它 进行进一步的处理。   


参考资料：   
http://blog.csdn.net/column/details/why-bug.html   
http://python.jobbole.com/77821/