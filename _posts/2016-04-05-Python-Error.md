---
layout: post
title: Python 错误信息
date:   2016-04-05 15:36:03
categories: [Python]
tags: [Pthon]
---

* content
{:toc}

	import urllib.request
	from bs4 import BeautifulSoup

	get = urllib.request.urlopen("https://www.website.com/")
	html = get.read()

	soup = BeautifulSoup(html)

	print(soup)

在print时报以下错误：   

	UnicodeEncodeError: 'charmap' codec can't encode characters in position 70924-70950: character maps to <undefined>

解决办法   

	print(soup		)
	
	

	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(data)
	fo.close()

报以下错误：   

	TypeError:must be str,not bytes

解决办法   

	fo.writelines(data.decode('utf-8'))