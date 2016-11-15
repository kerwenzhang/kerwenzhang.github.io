---
layout: post
title: Python 爬虫入门笔记
date:   2016-04-04 19:36:03
categories: "Python"
catalog: true
tags: 
    - Python
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

## urllib

在Python中，我们使用urllib这个组件来抓取网页。   
urllib是Python的一个获取URLs(Uniform Resource Locators)的组件。   
它以urlopen函数的形式提供了一个非常简单的接口。   
官方文档在这： https://docs.python.org/3/library/urllib.html   
最简单的urllib2的应用代码只需要四行。   

	import urllib2  
	response = urllib2.urlopen('http://www.baidu.com/')  
	html = response.read()  
	print html  

Python 3.x中urllib2被整合到了urllib中，用urllib.request替代。在3.x中代码如下：   

	import urllib.request	 
	response=urllib.request.urlopen("http://www.baidu.com/")
	html = response.read()
	html=html.decode('UTF-8')
	Print(html)
	
用Python简单处理URL   
如果要抓取百度上面搜索关键词为Jecvay Notes的网页, 则代码如下   

	import urllib
	import urllib.request
	 
	data={}
	data['word']='Jecvay Notes'
	 
	url_values=urllib.parse.urlencode(data)
	url="http://www.baidu.com/s?"
	full_url=url+url_values
	 
	data=urllib.request.urlopen(full_url).read()
	data=data.decode('UTF-8')
	print(data)

data是一个字典, 然后通过urllib.parse.urlencode()来将data转换为 ‘word=Jecvay+Notes’的字符串, 最后和url合并为full_url,    

## Python的队列和集合

在爬虫程序中, 用到了广度优先搜索(BFS)算法. 这个算法用到的数据结构就是队列.   
Python的List功能已经足够完成队列的功能,但是List用来完成队列功能其实是低效率的, 因为List在队首使用 pop(0) 和 insert() 都是效率比较低的, Python官方建议使用collection.deque来高效的完成队列任务.   

	from collections import deque
	queue = deque(["Eric","John","Michael"])
	queue.append("Terry")
	queue.append("Graham")
	print(queue.popleft())
	print(queue.popleft())
	print(queue)

在爬虫程序中, 为了不重复爬那些已经爬过的网站, 我们需要把爬过的页面的url放进集合中, 在每一次要爬某一个url之前, 先看看集合里面是否已经存在. 如果已经存在, 我们就跳过这个url; 如果不存在, 我们先把url放入集合中, 然后再去爬这个页面.   
Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 一般用来测试是否已经包含了某元素, 或者用来对众多元素们去重.    

	basket ={'apple', 'orange','apple','pear','orange'}
	print(basket)
	print('orange' in basket)
	print('crabgrass' in basket)

	emptySet = set()

## 正则表达式

在爬虫程序中, 爬回来的数据是一个字符串, 字符串的内容是页面的html代码. 我们要从字符串中, 提取出页面提到过的所有url. 这就要求爬虫程序要有简单的字符串处理能力, 而正则表达式可以很轻松的完成这一任务.   

爬虫Ver 1.0   

	import re
	import urllib.request
	import urllib
	 
	from collections import deque
	 
	queue = deque()
	visited = set()
	 
	url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
	 
	queue.append(url)
	cnt = 0
	 
	while queue:
	  url = queue.popleft()  # 队首元素出队
	  visited |= {url}  # 标记为已访问
	 
	  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
	  cnt += 1
	  urlop = urllib.request.urlopen(url)
	  if 'html' not in urlop.getheader('Content-Type'):
		continue
	 
	  # 避免程序异常中止, 用try..catch处理异常

	  try:
		data = urlop.read().decode('utf-8')
	  except:
		continue
	 
	  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列

	  linkre = re.compile('href=\"(.+?)\"')
	  for x in linkre.findall(data):
		if 'http' in x and x not in visited:
		  queue.append(x)
		  print('加入队列 --->  ' + x)
		  
## 超时跳过

urlop = urllib.request.urlopen(url, timeout = 2)   
当发生超时, 程序因为exception中断. 于是把这一句也放在try .. except 结构里, 问题解决.   

## 伪装浏览器

在 GET 的时候将 User-Agent 添加到header里   

	import urllib.request
	import http.cookiejar
	 
	# head: dict of header

	def makeMyOpener(head = {
		'Connection': 'Keep-Alive',
		'Accept': 'text/html, application/xhtml+xml, */*',
		'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
	}):
		cj = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
		header = []
		for key, value in head.items():
			elem = (key, value)
			header.append(elem)
		opener.addheaders = header
		return opener
	 
	oper = makeMyOpener()
	uop = oper.open('http://www.baidu.com/', timeout = 1000)
	data = uop.read()
	print(data)

保存抓回来的报文   

	def saveFile(data):
		save_path = 'D:\\temp.out'
		f_obj = open(save_path, 'wb') # wb 表示打开方式
		f_obj.write(data)
		f_obj.close()
	 
	# 这里省略爬虫代码

	# ...
	 
	# 爬到的数据放到 dat 变量里

	# 将 dat 变量保存到 D 盘下

	saveFile(dat)
	
使用 Requests 库来代替 urllib, 用 BeautifulSoup 来代替 re 模块.   
官方文档:   
http://docs.python-requests.org/en/latest/   
http://www.crummy.com/software/BeautifulSoup/   

在 Windows 下如果安装了 Python3, 那么在 cmd 下直接可以通过 pip 来安装这两个模块, 命令如下:   

	pip install requests
	pip install beautifulsoup4
	
参考资料：   
http://blog.csdn.net/column/details/why-bug.html   
http://python.jobbole.com/77821/   
https://jecvay.com/2014/09/python3-web-bug-series1.html   
http://cuiqingcai.com/category/technique/python