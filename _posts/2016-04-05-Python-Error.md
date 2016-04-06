---
layout: post
title: Python 错误信息
date:   2016-04-05 15:36:03
categories: [Python]
tags: [Pthon]
---

* content
{:toc}

错误1：

	import urllib.request
	response=urllib.request.urlopen("http://www.baidu.com/")
	html = response.read()
	html=html.decode('UTF-8')
	print(html)

在print时报以下错误：   

	UnicodeEncodeError: 'charmap' codec can't encode characters in position 70924-70950: character maps to <undefined>

解决办法   

我遇到这个问题是因为我用的win7是英文的操作系统，在用print输出时找不到对应的中文字符。
办法1： 将控制面板-> Regin and Language -> system locale改到中文，重启
办法2： 将要输出的东西保存到文件中，在保存的过程中需要转成UTF-8格式
	
	import urllib.request
	def WriteToFile(data):
		fo = open("C:\\test.txt","w", encoding="utf-8")
		fo.writelines(data)
		fo.close()
	
	response=urllib.request.urlopen("http://www.baidu.com/")
	html = response.read()
	html=html.decode('UTF-8')
	WriteToFile(html)
	
错误2：

	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(data)
	fo.close()

报以下错误：   

	TypeError:must be str,not bytes

解决办法   

	fo.writelines(data.decode('utf-8'))
	
更新