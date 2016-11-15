---
layout: post
title: Python正则表达式
date:   2016-04-13 17:05:03
categories: "Python"
catalog: true
tags: 
    - Python
---

正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。

下图列出了Python支持的正则表达式元字符和语法：    
![Label](http://ww3.sinaimg.cn/mw690/6c02e057jw1f2v67sn7w9j20m71brnj0.jpg)     

## re模块

Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。   

### re.match函数

re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。   

	re.match(pattern, string, flags=0)


|| 参数 || 描述 ||   
|| pattern || 匹配的正则表达式 ||   
||string||要匹配的字符串。||   
||flags||标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。||   

匹配成功re.match方法返回一个匹配的对象，否则返回None。   
可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。   

||匹配对象方法||描述||   
||group(num=0)||匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。||   
||groups()||返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。||   

### re.search方法

re.search 扫描整个字符串并返回第一个成功的匹配。   
函数语法：   

	re.search(pattern, string, flags=0)

||参数||描述||   
||pattern||匹配的正则表达式||   
||string||要匹配的字符串。||   
||flags||标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。||   

匹配成功re.search方法返回一个匹配的对象，否则返回None。   

### re.match与re.search的区别

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
