---
layout: post
title: "C# 泛型"
date:   2018-1-2 10:50:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



原文地址： http://www.cnblogs.com/wudiwushen/archive/2010/04/20/1703368.html     

首先，我们还是先说说委托吧，从字面上理解，只要是中国人应该都知道这个意思，除非委托2个中文字不认识，举个例子，小明委托小张去买车票。   

首先是C#语法      

	public delegate void BugTicketEventHandler();   

delegate 是关键词，【注：EventHandler是一个声明委托的微软C#的命名标准，我的习惯是标准就要第一时间说，也就这个命名习惯要第一时间养成】     

完了，这就是委托，就这么简单，看看和我们一般的方法有什么区别呢？   

	public void BuyTicket()  
	{  
		//方法体  
	}   

区别知道了吧，在现实生活中，委托只是个命令，做事情是别人，而在程序世界里委托只是存储了各个方法的地址，而他自己也是什么也不做的。     

那我们就把刚才那个，小明委托小张去买车票的现实生活场景，怎么在程序世界里体现呢？     

代码     

	//小张类  

    public class MrZhang     
    {     
        //其实买车票的悲情人物是小张     
        public static void BuyTicket()     
        {     
            Console.WriteLine("NND,每次都让我去买票，鸡人呀！");     
        }     
    }     
  
    //小明类     
    class MrMing     
    {     
        //声明一个委托，其实就是个“命令”     
        public delegate void BugTicketEventHandler();     

        public static void Main(string[] args)     
        {   
            //这里就是具体阐述这个命令是干什么的，本例是MrZhang.BuyTicket“小张买车票”     
            BugTicketEventHandler myDelegate = new BugTicketEventHandler(MrZhang.BuyTicket);     
  
            //这时候委托被附上了具体的方法     
            myDelegate();     
            Console.ReadKey();     
        }     
    }    

	BugTicketEventHandler myDelegate = new BugTicketEventHandler(MrZhang.BuyTicket);   

这是委托的声明方法， BugTicketEventHandler(委托的方法);委托的方法必须要加上，因为委托的构造函数是不为空的。     

注：委托的参数和返回类型，都要和你要具体委托的方法要一致，例：     

	public delegate void BugTicketEventHandler();  

	public static void BuyTicket()  
	{  
		Console.WriteLine("NND,每次都让我去买票，鸡人呀！");  
	}    

同学们，看到这里可以先消化消化，休息一下，我们简单的讲一下委托链的概念：     

其实委托链也是相当的简单，在现实生活中，小明叫小张买完车票之后，可能接着又让他带张电影票，     

而我们程序世界里的表述为：    

	//小张类

    public class MrZhang   
    {   
        //其实买车票的悲情人物是小张   
        public static void BuyTicket()   
        {   
            Console.WriteLine("NND,每次都让我去买票，鸡人呀！");   
        }   

        public static void BuyMovieTicket()   
        {   
            Console.WriteLine("我去，自己泡妞，还要让我带电影票！");   
        }   
    }   

    //小明类   
    class MrMing   
    {   
        //声明一个委托，其实就是个“命令”   
        public delegate void BugTicketEventHandler();   

        public static void Main(string[] args)   
        {   
            //这里就是具体阐述这个命令是干什么的，本例是MrZhang.BuyTicket“小张买车票”   
            BugTicketEventHandler myDelegate = new BugTicketEventHandler(MrZhang.BuyTicket);   

            myDelegate += MrZhang.BuyMovieTicket;   
            //这时候委托被附上了具体的方法   
            myDelegate();   
            Console.ReadKey();   
        }   
    }    
 
其实，我们只是在程序中加了 myDelegate += MrZhang.BuyMovieTicket;<br/>   
这时这个委托就相当于要做2件事情，先是买车票，再是买电影票拉！<br/>