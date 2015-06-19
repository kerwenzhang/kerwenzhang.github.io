---
layout: postlayout
title: "MFC ActiveX新增属性页 控件不响应"
date:   2015-05-31 00:18:23 
categories: [MFC]
tags: [MFC, Activex]
---

<div id="cnblogs_post_body"><p>在Activex中可以添加自定义的属性页，在新的属性页上添加一个button控件，设置好响应函数后，测试时发现点击button没有响应。</p>
<p>对比之前的主属性页发现，新增属性页的属性&ldquo;Disabled&rdquo; 被设为true， 改为false后，新属性页控件能正常使用。</p></div>

<p>Post Date: {{ page.date | date_to_string }}</p>