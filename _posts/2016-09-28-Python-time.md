---
layout: post
title: Python 时间相关操作
date:   2016-09-28 16:45:14
categories: [Python]
tags: [time]
---

* content
{:toc}

## datetime
datetime是Python处理日期和时间的标准库。   

### 获取当前日期和时间

我们先看如何获取当前日期和时间：   

	>>> from datetime import datetime
	>>> now = datetime.now() # 获取当前datetime
	>>> print(now)
	2015-05-18 16:28:07.198690
	>>> print(type(now))
	

注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。   

如果仅导入import datetime，则必须引用全名datetime.datetime。   

datetime.now()返回当前日期和时间，其类型是datetime。   

### 获取指定日期和时间

要指定某个日期和时间，我们直接用参数构造一个datetime：   

	>>> from datetime import datetime
	>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
	>>> print(dt)
	2015-04-19 12:20:00
	
### datetime转换为timestamp

把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：   

	>>> from datetime import datetime
	>>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
	>>> dt.timestamp() # 把timestamp转换为datetime
	1429417200.0
	
注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。   

某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。   

### timestamp转换为datetime

要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：   

	>>> from datetime import datetime
	>>> t = 1429417200.0
	>>> print(datetime.fromtimestamp(t))
	2015-04-19 12:20:00
	
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。   

本地时间是指当前操作系统设定的时区。例如北京时区是东8区。   

### str转换为datetime

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：   

	>>> from datetime import datetime
	>>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
	>>> print(cday)
	2015-06-01 18:19:59
	
字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档。   

注意转换后的datetime是没有时区信息的。   

### datetime转换为str

如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：   

	>>> from datetime import datetime
	>>> now = datetime.now()
	>>> print(now.strftime('%a, %b %d %H:%M'))
	Mon, May 05 16:28
	
### datetime加减

对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：   

	>>> from datetime import datetime, timedelta
	>>> now = datetime.now()
	>>> now
	datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
	>>> now + timedelta(hours=10)
	datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
	>>> now - timedelta(days=1)
	datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
	>>> now + timedelta(days=2, hours=12)
	datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
	
可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。   

### 小结

datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。   

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。