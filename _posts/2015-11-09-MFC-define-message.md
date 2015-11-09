---
layout: postlayout
title: "MFC中自定义消息"
date:   2015-11-09 8:41:00 
categories: [MFC]
tags: [MFC,Message]
---

原文地址:http://www.cnblogs.com/xulei/archive/2007/11/22/968170.html

消息映射、循环机制是Windows程序运行的基本方式。VC++ MFC 中有许多现成的消息句柄，可当我们需要完成其它的任务，需要自定义消息，
就遇到了一些困难。在MFC ClassWizard中不允许添加用户自定义消息，所以我们必须手动在程序中添加相应代码，以便可以象处理其它消息一样处理自定义消息。

自定义消息的步骤如下：
（1）建立Single Document的MFC Application，工程名为：MyMessage
（2）自定义消息：
### 第一步：定义消息
在Resource.h中添加如下代码：
		//推荐用户自定义消息至少是WM_USER+100，因为很多新控件也要使用WM_USER消息。
		#define WM_MY_MESSAGE (WM_USER+100)
### 第二步：声明消息处理函数
选择CMainFrame类中添加消息处理函数
在MainFrm.h文件中，类CMainFrame内，声明消息处理函数，代码如下:
		protect:
		fx_msg LRESULT OnMyMessage(WPARAM wParam, LPARAM lParam); 
### 第三步：实现消息处理函数
在MainFrm.cpp文件中添加如下代码：
		LRESULT CMainFrame::OnMyMessage(WPARAM wParam, LPARAM lParam)
		{
			//TODO: Add your message handle code
			return 0;
		}
### 第四步：添加消息映射
在CMainFrame类的消息块中，使用ON_MESSAGE宏指令将消息映射到消息处理函数中

		BEGIN_MESSAGE_MAP(CMainFrame, CFrameWnd)
			ON_WM_CREATE()
			ON_MESSAGE(WM_MY_MESSAGE,OnMyMessage)
			//ON_REGISTERED_MESSAGE (WM_MY_MESSAGE,OnMyMessage)
		END_MESSAGE_MAP()
如果用户需要一个定义整个系统唯一的消息,可以调用SDK函数RegisterWindowMessage定义消息:
在Resource.h中将代码

		#define WM_MY_MESSAGE (WM_USER+100)
替换为：

		static UINT WM_MY_MESSAGE=RegisterWindowMessage(_T("User"));
并使用ON_REGISTERED_MESSAGE宏指令取代ON_MESSAGE宏指令,其余步骤同上。
注：如果仍然使用ON_MESSAGE宏指令，compile可以通过，但是无法响应消息。
当需要使用自定义消息时,可以在相应类中的函数中调用函数PostMessage或SendMessage发送消息PoseMessage(WM_MY_MESSAGE,O,O)。