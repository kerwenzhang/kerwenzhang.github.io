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

## urllib2

在Python中，我们使用urllib2这个组件来抓取网页。   
urllib2是Python的一个获取URLs(Uniform Resource Locators)的组件。   
它以urlopen函数的形式提供了一个非常简单的接口。   
最简单的urllib2的应用代码只需要四行。   

	import urllib2  
	response = urllib2.urlopen('http://www.baidu.com/')  
	html = response.read()  
	print html  

Python 3.x中urllib2被整合到了urllib中，用urllib.request替代。在3.x中代码如下：   

	import urllib.request
	response = urllib.request.urlopen('http://www.baidu.com/')
	html = response.read()
	print (html)

在HTTP请求时，允许你做额外的两件事。   
1.发送data表单数据   
有时候你希望发送一些数据到URL(通常URL与CGI[通用网关接口]脚本，或其他WEB应用程序挂接)。   
在HTTP中,这个经常使用熟知的POST请求发送。   
一般的HTML表单，data需要编码成标准形式。然后做为data参数传到Request对象。   

	import urllib.parse
	import urllib.request

	url = 'http://www.someserver.com/register.cgi' 

	value ={'name':'WHY',
			'location':'SDU',
			'language':'Python'}

	data = urllib.parse.urlencode(value)
	binary_data = data.encode('utf-8')

	req = urllib.request.Request(url,binary_data)
	response = urllib.request.urlopen(req)
	the_page = response.read()

参考资料：   
http://blog.csdn.net/column/details/why-bug.html   
http://python.jobbole.com/77821/