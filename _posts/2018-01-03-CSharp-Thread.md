---
layout: post
title: "C# 线程"
date:   2018-1-3 14:50:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



## 线程生命周期  

线程生命周期开始于 System.Threading.Thread 类的对象被创建时，结束于线程被终止或完成执行时。  
下面列出了线程生命周期中的各种状态：  
  
  未启动状态：   当线程实例被创建但 Start 方法未被调用时的状况。  
  就绪状态：     当线程准备好运行并等待 CPU 周期时的状况。  
  不可运行状态： 下面的几种情况下线程是不可运行的：  
    已经调用 Sleep 方法  
    已经调用 Wait 方法  
    通过 I/O 操作阻塞  
  死亡状态：     当线程已完成执行或已中止时的状况。  
  
## 主线程  

在 C# 中，System.Threading.Thread 类用于线程的工作。它允许创建并访问多线程应用程序中的单个线程。进程中第一个被执行的线程称为主线程。  
当 C# 程序开始执行时，主线程自动创建。使用 Thread 类创建的线程被主线程的子线程调用。您可以使用 Thread 类的 CurrentThread 属性访问线程。  
Example:

    static void Main(string[] args)
    {
        Thread th = Thread.CurrentThread;
        th.Name = "MainThread";
        Console.WriteLine("This is {0}", th.Name);
        Console.ReadKey();
    }
    
运行结果：

    This is MainThread
    
## 创建线程  

    static void Main(string[] args)
    {
        Thread t = new Thread(Child);
        t.Start();
        Console.WriteLine("This is main thread.");
        Console.ReadKey();
    }

    static void Child()
    {
        Console.WriteLine("This is in thread.");
    }
    
运行结果：

    This is main thread.
    This is in thread.
    
程序运行的结果不能保证哪个先输出，因为线程是由操作系统调度，每次哪个线程在前面可以不同   
## 线程管理

Sleep()方法：  

    static void Main(string[] args)
    {
        Thread t = new Thread(Child);
        t.Start();
        Console.WriteLine("This is main thread.");
        Console.ReadKey();
    }

    static void Child()
    {
        Console.WriteLine("This is in thread.");
        Thread.Sleep(1000);
        Console.WriteLine("Sleep 1 second.");
    }
    
## 传入参数

    static void Main(string[] args)
    {
        Thread t2 = new Thread(ChildWithParam);
        t2.Start("test");
        Console.ReadKey();
    }

    static void ChildWithParam(object str)
    {
        Console.WriteLine("Child with parameter: " + str.ToString());
    }
    
上面创建的线程是类型不安全的，那用什么样的方式执行带传入参数的线程的方法是类型安全的呢，答案就是创建一个自定义类，在类中定义一个作为传入参数的字段，将线程的主方法定义为一个类的实例方法。  

    static void Main(string[] args)
    {
        ThreadClass<string> testClass = new ThreadClass<string>("data");
        Thread t3 = new Thread(testClass.ThreadFun);
        t3.Start();
        Console.ReadKey();
    }
    
    class ThreadClass<T>
    {
        private T data;
        public ThreadClass(T data)
        {
            this.data = data;
        }

        public void ThreadFun()
        {
            Console.WriteLine("In thread class: " + this.data.ToString());
        }
    }
    
## 后台线程　　 

　　Thread类默认创建的是前台线程，所以我们前面创建的线程全部都是前台线程。只要有一个前台线程在运行，应用程序的进程就在运行。如果有多个前台线程在运行，而Main()方法（主线程）结束了，应用程序的进程就仍然是激活的，直到所有前台线程完成其任务为止。   
　　那后台线程呢？显然和前台线程相反。当主线程结束后，应用程序的进程就终止了，在所有前台线程结束后，后台线程就会被终止。   
　　在编码的时候我们可以设置Thread类的IsBackground的属性来确定该线程是前台线程还是后台线程。当IsBackground设置为False的时候，为前台线程，设置为Ture的时候为后台线程，下面我们举例来说明前台线程和后台线程的区别。首先我们创建一个前台线程。   

## 线程池

LR线程池  

## 线程同步

## Task类

## 线程异步