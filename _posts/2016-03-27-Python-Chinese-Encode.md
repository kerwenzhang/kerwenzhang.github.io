---
layout: post
title: Python3 读取中文
date:   2016-03-27 19:00:03
categories: [Python]
tags: [Python]
---

* content
{:toc}

Python在读取带有中文的文本时，经常会报以下错误：   

	UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position xx: illegal multibyte sequence

去网上查找相关资料，发现很多解决方案都是在用 decode, encode方式，但测试发现对Python3不适用。 这也是Python3 不向下兼容带来的一个问题，很多参考资料已经不能用了。后来发现Python3 可以用一种更为简单的方式实现中文字符的解码：   

## 读取

	fo = open(strFilePath,"r", encoding="utf-8")
	fileData = fo.readlines()
	fo.close()
	
## 保存

	fo = open(filePath,"w", encoding="utf-8")
	fo.writelines(newLinelists)
	fo.close()