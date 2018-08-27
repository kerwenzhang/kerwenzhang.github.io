---                      
layout: post                      
title: "Html 基本标签"                      
date:   2018-8-27 10:00:00                       
categories: "Html"                      
catalog: true                      
tags:                       
    - Html                      
---            
        
#### 标题
HTML 标题（Heading）是通过&lt;h1&gt; - &lt;h6&gt; 标签来定义的.

	<h1>这是一个标题</h1>
	<h2>这是一个标题</h2>
	<h3>这是一个标题</h3>
	
#### 段落

HTML 段落是通过标签 &lt;p&gt; 来定义的.

#### 链接

HTML 链接是通过标签 &lt;a&gt; 来定义的.

#### span

<span> 用于对文档中的行内元素进行组合。  
<span> 标签没有固定的格式表现。当对它应用样式时，它才会产生视觉上的变化。如果不对 <span> 应用样式，那么 <span> 元素中的文本与其他文本不会任何视觉上的差异。  
<span> 标签提供了一种将文本的一部分或者文档的一部分独立出来的方式。  

## 全局属性

#### class

	<element class="classname">
	
class 属性定义了元素的类名。  
class 属性通常用于指向样式表的类。但是，它也可以用于 JavaScript 中（通过 HTML DOM）, 来修改 HTML 元素的类名。  
如需为一个元素规定多个类，用空格分隔类名。 &lt;span class="left important"&gt;. HTML 元素允许使用多个类。  
