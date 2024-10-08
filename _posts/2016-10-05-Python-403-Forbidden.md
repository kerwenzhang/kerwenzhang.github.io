---
layout: post
title: "Python爬虫 HTTP Error 403: Forbidden"
date:   2016-10-05 10:09:14
categories: "Python"
catalog: true
tags: 
    - Python
---





问题:   

 urllib.request.urlopen() 方法经常会被用来打开一个网页的源代码,然后会去分析这个页面源代码,但是对于有的网站使用这种方法时会抛出"HTTP Error 403: Forbidden"异常   
例如 执行下面的语句时   

	<span style="font-size:14px;"> urllib.request.urlopen("http://blog.csdn.net/eric_sunah/article/details/11099295")</span>  
 
会出现以下异常:   

	"Python"  
	<span style="color:#FF0000;">  File "D:\Python32\lib\urllib\request.py", line 475, in open  
		response = meth(req, response)  
	  File "D:\Python32\lib\urllib\request.py", line 587, in http_response  
		'http', request, response, code, msg, hdrs)  
	  File "D:\Python32\lib\urllib\request.py", line 513, in error  
		return self._call_chain(*args)  
	  File "D:\Python32\lib\urllib\request.py", line 447, in _call_chain  
		result = func(*args)  
	  File "D:\Python32\lib\urllib\request.py", line 595, in http_error_default  
		raise HTTPError(req.full_url, code, msg, hdrs, fp)  
	urllib.error.HTTPError: HTTP Error 403: Forbidden</span>  
	
分析:   
之所以出现上面的异常,是因为如果用 urllib.request.urlopen 方式打开一个URL,服务器端只会收到一个单纯的对于该页面访问的请求,但是服务器并不知道发送这个请求使用的浏览器,操作系统,硬件平台等信息,而缺失这些信息的请求往往都是非正常的访问,例如爬虫.   
有些网站为了防止这种非正常的访问,会验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)   
所以可以尝试在请求中加入UserAgent的信息   
方案:   
对于Python 3.x来说,在请求中添加UserAgent的信息非常简单,代码如下   

	"Python"  

	#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误  

    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询  

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}     
    req = urllib.request.Request(url=chaper_url, headers=headers)     
    urllib.request.urlopen(req).read()     
 
将urllib.request.urlopen.read() 替换成上面的代码后,对于出现问题的页面就可以就正常访问