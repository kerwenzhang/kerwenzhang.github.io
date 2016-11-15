---
layout: post
title: MFC中计算程序运行时间
date:   2016-05-10 17:00:14
categories: "MFC"
catalog: true
tags: 
    - MFC
---



在我们实际的编程工作中，经常要测量程序的运行时间，比如衡量算法的运行时间等等。在这里我收集了网上集中测量程序运行时间的方法。   
通过网上查阅资料，找到以下几种VC中求取程序运行时间的方法：   
方法一 利用GetTickCount函数(ms)   
代码：   

	CString str;         	  
	long t1=GetTickCount();//程序段开始前取得系统运行时间(ms)        
	。。。。。。//to do sth
	long t2=GetTickCount();//程序段结束后取得系统运行时间(ms)  
	str.Format("time:%dms",t2-t1);//前后之差即程序运行时间        
	AfxMessageBox(str); 
 
方法二利用C/C++计时函数(s)   
代码：   

	#include"time.h"

	clock_t   start,   finish;
	start =clock(); 
	finish = clock();
	printf("%f seconds\n",(double)(finish-start)/CLOCKS_PER_SEC); 
	
方法三  利用CTime类 获取系统时间   
代码：   

	CString str;
	//获取系统时间
	CTime tm;
	tm=CTime::GetCurrentTime();
	str=tm.Format("现在时间是%Y年%m月%d日  %X");
	AfxMessageBox(str);
	
方法四  利用GetLocalTime类获取系统时间   

	SYSTEMTIME st;
	CString strDate,strTime;
	GetLocalTime(&st);
	strDate.Format("M----",st.wYear,st.wMonth,st.wDay);
	strTime.Format("-:-:-",st.wHour,st.wMinute,st.wSecond);
	AfxMessageBox(strDate);
	AfxMessageBox(strTime);
 
方法五 利用API函数   

	BOOL QueryPerformanceCounter(
	  LARGE_INTEGER *lpPerformanceCount   // counter value
	);
	