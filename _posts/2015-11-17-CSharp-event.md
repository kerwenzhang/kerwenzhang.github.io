---
layout: post
title: "C# 事件(一)"
date:   2015-11-17 11:07:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



原文地址： http://www.cnblogs.com/wudiwushen/archive/2010/04/20/1703763.html<br/>   

<br/>   
什么是事件？EVENT？点击事件？加载事件？一连串的模糊的概念冲击着我们弱小的脑袋<br/>   
<br/>   
那我们首先来看一下比较正统的感念吧：<br/>   
<br/>   
事件是类在发生其关注的事情时用来提供通知的一种方式。<br/>   
<br/>   
事件的发生一般都牵扯2个角色<br/>   
<br/>   
事件发行者（Publisher）:一个事件的发行者，也称作是发送者（sender），其实就是个对象，这个对象会自行维护本身的状态信息，当本身状态信息变动时，便触发一个事件，并通知说有的事件订阅者。<br/>   
<br/>   
事件订阅者（Subscriber）:对事件感兴趣的对象，也称为Receiver，可以注册感兴趣的事件，在事件发行者触发一个事件后，会自动执行这段代码。<br/>   
<br/>   
为了更好的让大家理解上面的概念，我先什么都不讲，我们先来看一段简单的代码：<br/>   

	//发布者（Publiser)

    public class Publisher   
    {   
        //声明一个出版的委托   
        public delegate void PublishEventHander();   
        //在委托的机制下我们建立以个出版事件   
        public event PublishEventHander OnPublish;   
        //事件必须要在方法里去触发，出版社发布新书方法   
        public void issue()   
        {   
            //如果有人注册了这个事件，也就是这个事件不是空   
            if (OnPublish != null)   
            {   
                Console.WriteLine("最新一期的《火影忍者》今天出版哦！");   
                OnPublish();   
            }   
        }   
    }   

    //Subscriber 订阅者，无赖小明   
    public class MrMing   
    {   
        //对事件感兴趣的事情，这里指对出版社的书感兴趣   
        public static void Receive()   
        {   
            Console.WriteLine("嘎嘎，我已经收到最新一期的《火影忍者》啦！！");       
        }   
    }   
    
    //Subscriber 订阅者，悲情人物小张   
    public class MrZhang   
    {   
        //对事件感兴趣的事情   
        public static void Receive()   
        {   
            Console.WriteLine("幼稚，这么大了，还看《火影忍者》，SB小明！");   
        }   
    }   

    class Story   
    {   
        public static void Main(string[] args)   
        {   
            //实例化一个出版社   
            Publisher publisher = new Publisher();   

            //给这个出火影忍者的事件注册感兴趣的订阅者，此例中是小明   
            publisher.OnPublish += new Publisher.PublishEventHander(MrMing.Receive);   
            //另一种事件注册方式   
            //publisher.OnPublish += MrMing.Receive;   

            //发布者在这里触发出版火影忍者的事件   
            publisher.issue();   

            Console.ReadKey();   
        }   
    }   

如果童靴们，从上到下仔细看一边的话，我想应该知道什么是发布者，什么是订阅者了吧，那至于事件呢<br/>   
<br/>   
我们先看这句<br/>   

	publisher.OnPublish += new Publisher.PublishEventHander(MrMing.Receive);

这就是小明向出版社订阅他喜欢看的火影忍者，小张没有订阅所以小张没有收到书，<br/>    
<br/>   
我们再仔细看看这个赋值语句，是不是似曾相识过呢？是的就是我们在上一讲，在讲委托声明的时候，简直就是一个眸子里刻出来的嘛<br/>   
<br/>   
委托赋值：<br/>   

	BugTicketEventHandler myDelegate = new BugTicketEventHandler(MrZhang.BuyTicket);

所以，大家不要对事件有什么好怕的，其实事件的本质就是一个委托链，<br/>   
<br/>   
我们看一下事件的声明：<br/>   

	//声明一个出版的委托
	public delegate void PublishEventHander();
	//在委托的机制下我们建立以个出版事件
	public event PublishEventHander OnPublish;

在我们使用事件的时候，必须要声明对应的委托，而触发事件，其实就是在使用委托链。