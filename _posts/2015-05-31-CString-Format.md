---
layout: postlayout
title: "MFC中CString.Format使用方法"
date:   2013-12-23 00:18:23 
thumbimg: 1346208288725.jpg
categories: [MFC]
tags: [MFC, CString, Format]
---

<div id="cnblogs_post_body"><p>%c 单个字符<br />%d 十进制整数(int)<br />%ld 十进制整数(long)</p>
<p>%lu unsigned long<br />%f 十进制浮点数(float)<br />%lf 十进制浮点数(double)<br />%o 八进制数<br />%s 字符串<br />%u 无符号十进制数<br />%x 十六进制数</p>
<p>&nbsp;</p>
<p>int转换为CString：<br />　　CString str;<br />　　int number=15;<br />　　//str="15"<br />　　str.Format(_T("%d"),number);<br />　　//str=" 15"(前面有两个空格；4表示将占用4位，如果数字超过4位将输出所有数字，不会截断)<br />　　str.Format(_T("%4d"),number);<br />　　//str="0015"(.4表示将占用4位，如果数字超过4位将输出所有数字，不会截断)<br />　　str.Format(_T("%.4d"),number);<br />　　long转换为CString的方法与上面相似，只需要把%d改为%ld就可以了。</p>
<p>double转换为CString：<br />　　CString str;<br />　　double num=1.46;<br />　　//str="1.46"<br />　　str.Format(_T("%lf"),num);<br />　　//str="1.5"(.1表示小数点后留1位，小数点后超过1位则四舍五入)<br />　　str.Format(_T("%.1lf"),num);<br />　　//str="1.4600"<br />　　str.Format(_T("%.4f"),num);<br />　　//str=" 1.4600"(前面有1个空格)<br />　　str.Format(_T("%7.4f"),num);<br />　　float转换为CString的方法也同上面相似，将lf%改为f%就可以了。</p>
<p>将十进制数转换为八进制：<br />　　CString str;<br />　　int num=255;<br />　　//str="377"<br />　　str.Format(_T("%o"),num);<br />　　//str="00000377"<br />　　str.Format(_T("%.8o"),num);</p></div>

<p>Post Date: {{ page.date | date_to_string }}</p>

<a href="{{ site.baseurl }}/index.html">Go back</a>