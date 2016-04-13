---
layout: post
title: BeautifulSoup 笔记
date:   2016-04-13 15:52:03
categories: [Python]
tags: [BeautifulSoup]
---

* content
{:toc}

### 安装

	$ pip install beautifulsoup4

### import

	from bs4 import BeautifulSoup	

### 格式化html

	soup = BeautifulSoup(html_doc)
	print(soup.prettify())

### 获取所有文字内容:

	print(soup.get_text())

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .   

## Tag

Tag 对象与XML或HTML原生文档中的tag相同:   

	soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
	tag = soup.b
	type(tag)

	# <class 'bs4.element.Tag'>

### Name

每个tag都有自己的名字,通过 .name 来获取:   

	tag.name

	# u'b'

### Attributes

一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:   

	tag['class']

	# u'boldest'

## 遍历文档树

操作文档树最简单的方法就是告诉它你想获取的tag的name.如果想获取 <head> 标签,只要用 soup.head :   

	soup.head

	# <head><title>The Dormouse's story</title></head>

可以在文档树的tag中多次调用这个方法.下面的代码可以获取<body>标签中的第一个<b>标签:   

	soup.body.b

	# <b>The Dormouse's story</b>

如果想要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 find_all():   

	soup.find_all('a')

	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,

	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

## 搜索文档树

最简单的filter是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签:   

	soup.find_all('b')

	# [<b>The Dormouse's story</b>]

### 正则表达式

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到:   

	import re
	for tag in soup.find_all(re.compile("^b")):
		print(tag.name)

	# body

	# b

find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件.这里有几个例子:   

	soup.find_all("title")

	# [<title>The Dormouse's story</title>]

	soup.find_all("p", "title")

	# [<p class="title"><b>The Dormouse's story</b></p>]

	soup.find_all("a")

	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,

	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.find_all(id="link2")

	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

	import re
	soup.find(text=re.compile("sisters"))

	# u'Once upon a time there were three little sisters; and their names were\n'
	
	soup.find_all(href=re.compile("elsie"))

	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
	
	# 使用多个指定名字的参数可以同时过滤tag的多个属性:

	soup.find_all(href=re.compile("elsie"), id='link1')

	# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
	
	data_soup.find_all(attrs={"data-foo": "value"})

	# [<div data-foo="value">foo!</div>]

### 按CSS搜索

标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:   

	soup.find_all("a", class_="sister")

	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,

	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

tag的 class 属性是 多值属性 .按照CSS类名搜索tag时,可以分别搜索tag中的每个CSS类名:   

	css_soup = BeautifulSoup('<p class="body strikeout"></p>')
	css_soup.find_all("p", class_="strikeout")

	# [<p class="body strikeout"></p>]

### limit 参数

find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.   

	soup.find_all("a", limit=2)

	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,

	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
