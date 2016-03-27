---
layout: post
title: ---
date:   2016-03-27 11:54:03
categories: [layout: post]
tags: [title:] ["MFC中CString.Format使用方法"]
---

* content
{:toc}

thumbimg: 1346208288725.jpg   
categories: [MFC]   
tags: [MFC, CString, Format]   
---   

* content   
{:toc}   

%c 单个字符     
%d 十进制整数(int)     
%ld 十进制整数(long)     

%lu unsigned long     
%f 十进制浮点数(float)     
%lf 十进制浮点数(double)     
%o 八进制数     
%s 字符串     
%u 无符号十进制数     
%x 十六进制数     

### int转换为CString：  

	CString str;
	int number=15;  
	str.Format(_T("%d"),number); //str="15"  
	str.Format(_T("%4d"),number); //str=" 15"(前面有两个空格；4表示将占用4位，如果数字超过4位将输出所有数字，不会截断)  
	str.Format(_T("%.4d"),number); //str="0015"(.4表示将占用4位，如果数字超过4位将输出所有数字，不会截断)  
	
	long转换为CString的方法与上面相似，只需要把%d改为%ld就可以了。

### double转换为CString：  

	CString str;  
	double num=1.46;  
	str.Format(_T("%lf"),num); //str="1.46"  
	str.Format(_T("%.1lf"),num); //str="1.5"(.1表示小数点后留1位，小数点后超过1位则四舍五入)  
	str.Format(_T("%.4f"),num); //str="1.4600"  
	str.Format(_T("%7.4f"),num); //str=" 1.4600"(前面有1个空格)  
	
	float转换为CString的方法也同上面相似，将lf%改为f%就可以了。

### 将十进制数转换为八进制：

	CString str;  
	int num=255;  
	str.Format(_T("%o"),num); //str="377"  
	str.Format(_T("%.8o"),num); //str="00000377"  

### bool转换为CString

	CString cs_tmp;
	cs_tmp = m_Bool1 ? "1" : "0";
	或者
	CString cs_tmp;
	cs_tmp = m_Bool1 ? "TRUE" : "FALSE";