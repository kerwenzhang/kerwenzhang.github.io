---
layout: post
title: "[转]C++回调函数(callback)的使用"
date:   2015-05-31 00:18:23
categories: [C++]
tags: [Callback]
---

* content
{:toc}


原文地址：http://blog.sina.com.cn/s/blog_6568e7880100p77y.html     


## 什么是回调函数(callback)  

模块A有一个函数foo，他向模块B传递foo的地址，然后在B里面发生某种事件（event）时，通过从A里面传递过来的foo的地址调用foo，通知A发生了什么事情，让A作出相应反应。 那么我们就把foo称为回调函数。     
  
例子：     
回调函数是个很有用，也很重要的概念。当发生某种事件时，系统或其他函数将会自动调用您定义的一段函数。回调函数在windows编程使用的场合很多， 比如Hook回调函数：MouseProc,GetMsgProc连同EnumWindows,DrawState的回调函数等等，更有很多系统级的回调 过程。本文不准备介绍这些函数和过程，而是谈谈实现自己的回调函数的一些经验。     
之所以产生使用回调函数这个想法，是因为现在使用VC和Delphi混合编程，用VC写的一个DLL程式进行一些时间比较长的异步工作，工作完成之后，需 要通知使用DLL的应用程式：某些事件已完成,请处理事件的后续部分。开始想过使用同步对象，文档影射，消息等实现DLL函数到应用程式的通知，后来突 然想到可不能够在应用程式端先写一个函数，等需要处理后续事宜的时候，在DLL里直接调用这个函数即可。     
于是就动手，写了个回调函数的原形。在VC和 Delphi里都进行了测试     

## 一：声明回调函数类型。  

vc版     

	typedef int (WINAPI *PFCALLBACK)(int Param1,int Param2) ;  

Delph版     

	PFCALLBACK = function(Param1:integer;Param2:integer):integer;stdcall;  

实际上是声明了一个返回值为int,传入参数为两个int的指向函数的指针。     
由于C++和PASCAL编译器对参数入栈和函数返回的处理有可能不一致，把函数类型用WINAPI(WINAPI宏展开就是__stdcall)或stdcall统一修饰。     

## 二：声明回调函数原形  

声明函数原形     
vc版     

	int WINAPI CBFunc(int Param1,int Param2)；  

Delphi版     

	function CBFunc(Param1,Param2:integer):integer;stdcall;  

以上函数为全局函数，假如要使用一个类里的函数作为回调函数原形，把该类函数声明为静态函数即可。 [Page]     
  
## 三： 回调函数调用调用者  

调用回调函数的函数我把他放到了DLL里，这是个很简单的VC生成的WIN32 DLL.并使用DEF文档输出其函数名 TestCallBack。实现如下：     

	PFCALLBACKgCallBack=0;  
	void WINAPI TestCallBack(PFCALLBACK Func)  
	{  
		if(Func==NULL)return;  
		gCallBack=Func;  
		DWORD ThreadID=0;  
		HANDLE hThread = CreateThread(NULL,NULL,Thread1,LPVOID(0),&amp;ThreadID );  
		return;  
	}  

此函数的工作把传入的 PFCALLBACK Func参数保存起来等待使用，并且启动一个线程。声明了一个函数指针PFCALLBACK gCallBack保存传入的函数地址。     

## 四： 回调函数怎样被使用：  

TestCallBack函数被调用后，启动了一个线程，作为演示，线程人为的进行了延时处理，并且把线程运行的过程打印在屏幕上.     
本段线程的代码也在DLL工程里实现     

	ULONGWINAPI Thread1(LPVOID Param)  
	{  
		TCHAR Buffer[256];  
		HDC hDC = GetDC(HWND_DESKTOP);  
		int Step=1;  
		MSG Msg; [Page]  
		DWORD StartTick;  
		//一个延时循环  
		for(;Step&lt;200;Step++)  
		{  
			StartTick = GetTickCount();  
  
			for(;GetTickCount()-StartTick&lt;10;)  
			{  
				if(PeekMessage(&amp;Msg,NULL,0,0,PM_NOREMOVE) )  
				{  
					TranslateMessage(&amp;Msg);  
					DispatchMessage(&amp;Msg);  
				}  
			}                  
  
			sprintf(Buffer,/"Running d/",Step);  
			if(hDC!=NULL)  
				TextOut(hDC,30,50,Buffer,strlen(Buffer));  
		}  
  
		(*gCallback)(Step,1);  
  
		::ReleaseDC (HWND_DESKTOP,hDC);  
		return 0;  
	}  

## 五：万事具备  

使用vc和Delphi各建立了一个工程，编写回调函数的实现部分     
VC版     

	int WINAPI CBFunc(int Param1,int Param2)  
	{  
		int res= Param1+Param2;  
		TCHAR Buffer[256]=/"/";  
		sprintf(Buffer,/"callback result = %d/",res);  
		MessageBox(NULL,Buffer,/"Testing/",MB_OK);//演示回调函数被调用  
		return res;[Page]  
	}  

Delphi版     

	function CBFunc(Param1,Param2:integer):integer;  
	begin  
		result:= Param1+Param2;  
		TForm1.Edit1.Text:=inttostr(result);/ /演示回调函数被调用  
	end;  
  
使用静态连接的方法连接DLL里的出口函数 TestCallBack,在工程里添加 Button( 对于Delphi的工程，还需要在Form1上放一个Edit控件，默认名为Edit1)。     
响应ButtonClick事件调用 TestCallBack     
TestCallBack(CBFunc) //函数的参数CBFunc为回调函数的地址     
函数调用创建线程后立即返回，应用程式能够同时干别的事情去了。现在能够看到屏幕上不停的显示字符串，表示dll里创建的线程运行正常。一会之后，线程延 时部分结束结束，vc的应用程式弹出MessageBox,表示回调函数被调用并显示根据Param1，Param2运算的结果，Delphi的程式 edit控件里的文本则被改写成Param1，Param2 的运算结果。     
可见使用回调函数的编程模式，能够根据不同的需求传递不同的回调函数地址，或定义各种回调函数的原形（同时也需要改变使用回调函数的参数和返回值约 定），实现多种回调事件处理，能够使程式的控制灵活多变，也是一种高效率的，清楚的程式模块之间的耦合方式。在一些异步或复杂的程式系统里尤其有用 -- 您能够在一个模块（如DLL）里专心实现模块核心的业务流程和技术功能，外围的扩展的功能只给出一个回调函数的接口，通过调用其他模块传递过来的回调函数 地址的方式，将后续处理无缝地交给另一个模块，随他按自定义的方式处理。     
本文的例子使用了在DLL里的多线程延时后调用回调函数的方式，只是为了突出一下回调函数的效果，其实只要是在本进程之内，都能够随您高兴能够把函数地址传递来传递去，当成回调函数使用。     
这样的编程模式原理很简单单一：就是把函数也看成一个指针一个地址来调用，没有什么别的复杂的东西，仅仅是编程里的一个小技巧。至于回调函数模式究竟能为您带来多少好处，就看您是否使用，怎样使用这种编程模式了。     
另外的解释：cdxiaogan     
msdn上这么说的：     
有关函数指针的知识     
使用例子能够很好地说明函数指针的用法。首先，看一看 Win32 API 中的 EnumWindows 函数：     

	Declare Function EnumWindows lib /"user32/" _  
	(ByVal lpEnumFunc as Long, _  
	ByVal lParam as Long ) As Long  

EnumWindows 是个枚举函数，他能够列出系统中每一个打开的窗口的句柄。EnumWindows 的工作方式是重复地调用传递给他的第一个参数（lpEnumFunc，函数指针）。每当 EnumWindows 调用函数，EnumWindows 都传递一个打开窗口的句柄。     
在代码中调用 EnumWindows 时，能够将一个自定义函数作为第一个参数传递给他，用来处理一系列的值。例如，能够编写一个函数将任何的值添加到一个列表框中，将 hWnd 值转换为窗口的名字，连同其他任何操作！     
为了表明传递的参数是个自定义函数，在函数名称的前面要加上 AddressOf 关键字。第二个参数能够是合适的任何值。例如，假如要把 MyProc 作为函数参数，能够按下面的方式调用 EnumWindows：     

	x = EnumWindows(AddressOf MyProc, 5)  

在调用过程时指定的自定义函数被称为回调函数。回调函数（通常简称为&ldquo;回调&rdquo;）能够对过程提供的数据执行指定的操作。     
回调函数的参数集必须具备规定的形式，这是由使用回调函数的 API 决定的。关于需要什么参数，怎样调用他们，请参阅 API 文档。     
回复人：zcchm     
我谈一下自己对回调函数的一点理解, 不对的地方请指教.     
我刚开始接触回调时, 也是一团雾水.很多人解释这个问题时, 总是拿API来举例子, 本来菜鸟最惧怕的就是API, ^_^. 回调跟API没有必然联系.     
其实回调就是一种利用函数指针进行函数调用的过程.     
  
为什么要用回调呢?比如我要写一个子模块给您用, 来接收远程socket发来的命令.当我接收到命令后, 需要调用您的主模块的函数, 来进行相应的处理.但是我不知道您要用哪个函数来处理这个命令,我也不知道您的主模块是什么.cpp或.h, 或说, 我根本不用关心您在主模块里怎么处理他, 也不应该关心用什么函数处理他...... 怎么办?     
  
  
  
## 使用回调.  

我在我的模块里先定义回调函数类型, 连同回调函数指针.     

	typedef void (CALLBACK *cbkSendCmdToMain) (AnsiString sCmd);  
	cbkSendCmdToMainSendCmdToMain;  

这样SendCmdToMain就是个指向拥有一个AnsiString形参, 返回值为void的函数指针.     
这样, 在我接收到命令时, 就能够调用这个函数啦.     

	...  
	SendCmdToMain(sCommand);  
	...  

但是这样还不够, 我得给一个接口函数(比如Init), 让您在主模块里调用Init来注册这个回调函数.     
在您的主模块里, 可能这样     

	void CALLBACK YourSendCmdFun(AnsiString sCmd);//声明  
	...  
	void CALLBACK YourSendCmdFun(AnsiString sCmd);//定义  
	{  
		ShowMessage(sCmd);  
	}  
	...  

调用Init函数向我的模块注册回调.可能这样:     

	Init(YourSendCmdFun, ...);  

这样, 预期目的就达到了.     
  
需要注意一点, 回调函数一般都要声明为全局的. 假如要在类里使用回调函数, 前面需要加上 static, 其实也相当于全局的.     

  


Post Date: {{ page.date | date_to_string }}  
