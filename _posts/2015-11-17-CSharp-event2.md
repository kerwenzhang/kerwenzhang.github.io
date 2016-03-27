---
layout: post
title: "C# 事件(二)"
date:   2015-11-17 11:54:00 
categories: [C#]
tags: [C#]
---

* content
{:toc}

原文地址： http://www.cnblogs.com/wudiwushen/archive/2010/04/21/1717378.html<br/><br/>   

为什么我们在日常的编程活动中遇到这么多sender,EventArgs e 参数：<br/>   

	void Page_Load(object sender, EventArgs e)
	{	
	}
	
	protected void btnSearch_Click(object sender, ImageClickEventArgs e)
	{
	}
	
	protected void grdBill_RowDataBound(object sender, GridViewRowEventArgs e)
	{          
	}

那他们到底表示什么呢？<br/>   
在回答上面的问题之前，我们先搞懂 .Net Framework的编码规范：<br/>   
<br/>   
一、委托类型的名称都应该以EventHandler结束。 <br/>   
二、委托的原型定义：有一个void返回值，并接受两个输入参数：一个Object 类型，一个 EventArgs类型(或继承自EventArgs)。 <br/>   
三、事件的命名为 委托去掉 EventHandler之后剩余的部分。 <br/>   
四、继承自EventArgs的类型应该以EventArgs结尾。<br/>   
<br/>   
这就是微软编码的规范，当然这不仅仅是规则，而是在这种规则下使程序有更大的灵活性，那我们就继续重构第三讲的例子，让他符合微软的规范。<br/>   

    //所有订阅者【Subscriber】感兴趣的对象，也就是e,都要继承微软的EventArgs   
    //本例中订阅者【也称观察者】MrMing，MrZhang他们感兴趣的e对象，就是杂志【magazine】   
    public class PubEventArgs : EventArgs   
    {   
        public readonly string magazineName;   
        public PubEventArgs()   
        {   

		
        }   
        public PubEventArgs (string magazineName)   
        {   
           this.magazineName = magazineName;   
        }   
    }   

    //发布者（Publiser)   
    public class Publisher   
    {   
        //声明一个出版的委托   
        //这里多了一个参数sender,它所代表的就是Subject，也就是监视对象，本例中就是Publisher   
        public delegate void PublishEventHander(object sender ,PubEventArgs e);   
        //在委托的机制下我们建立以个出版事件   
        public event PublishEventHander Publish;   

        //声明一个可重写的OnPublish的保护函数   
        protected virtual void OnPublish(PubEventArgs e)   
        {   
            if (Publish != null)   
            {   
                //Sender = this，也就是Publisher   
                this.Publish(this, e);   
            }   
        }   

        //事件必须要在方法里去触发   
        public void issue(string magazineName)   
        {   
            OnPublish(new PubEventArgs(magazineName));   
        }   
    }   

    //Subscriber 订阅者   
    public class MrMing   
    {   
        //对事件感兴趣的事情   
        public static void Receive(object sender,PubEventArgs e)   
        {   
            Console.WriteLine("嘎嘎，我已经收到最新一期的《"+e.magazineName+"》啦！！");   
        }   
    }   

    public class MrZhang   
    {   
        //对事件感兴趣的事情   
        public static void Receive(object sender, PubEventArgs e)   
        {   
            Console.WriteLine("幼稚，这么大了，还看《火影忍者》，SB小明！");   
            Console.WriteLine("这个我定的《"+e.magazineName+"》，哇哈哈！");   
        }   
    }   

    class Story   
    {   
        public static void Main(string[] args)   
        {   
            //实例化一个出版社   
            Publisher publisher = new Publisher();   

            Console.Write("请输入要发行的杂志：");   
            string name = Console.ReadLine();   

            if (name == "火影忍者")   
            {   
                //给这个出火影忍者的事件注册感兴趣的订阅者，此例中是小明   
                publisher.Publish += new Publisher.PublishEventHander(MrMing.Receive);   
                //发布者在这里触发出版火影忍者的事件   
                publisher.issue("火影忍者");   
            }   
            else   
            {   
                //给这个出火影忍者的事件注册感兴趣的订阅者，此例中是小明[另一种事件注册方式]   
                publisher.Publish += MrZhang.Receive;   
                publisher.issue("环球日报");   
            }   
            Console.ReadKey();   
        }   
    }   

输入火影忍者后，触发小明订阅的事件<br/>   
<br/>   
通过例子我再做一次说明，其实我们不用把Sender,e想的过于可怕<br/>   
<br/>   
一、委托声明原型中的Object类型的参数代表了Subject，也就是监视对象，在本例中是 Publisher(出版社)。。 <br/>   
二、EventArgs 对象包含了Observer所感兴趣的数据，在本例中是杂志。<br/>   
<br/>    
<br/>   
好了，我们接着讲我们的委托与事件，其实如果大家对设计模式精通的话，其实他们关联的是观察者（Observer）模式，这里我就不再描述什么是观察者模式了，只是简单讲一下他们的关联：<br/>   
<br/>   
在C#的event中，委托充当了抽象的Observer接口，而提供事件的对象充当了目标对象。委托是比抽象Observer接口更为松耦合的设计。<br/>   
<br/>   
如果看不懂的话也没关系，当大家OO达到一定程度了，自然而然就会明白。<br/>   
<br/>   
最后我们来看一个我们日常最最常用的观察者模式：<br/>   
<br/>   
场景：当我们用信用卡刷完钱的时候，我们就会接收到手机短信，或者是电子邮件，其实这就是Observer pattern<br/>   

    //---本例场景为当用户从银行账号里取出钱后，马上通知电子邮件和发手机短信---   
    //本例中的订阅者，也就是观察者是电子邮件与手机   
    //发布者，也就是被监视对象是银行账号   


    //Obverser电子邮件，手机关心的对象e ,分别是邮件地址、手机号码、取款金额   
    public class UserEventArgs : EventArgs   
    {   
        public readonly string emailAddress;   
        public readonly string mobilePhone;   
        public readonly string amount;   
        public UserEventArgs(string emailAddress, string mobilePhone,string amount)   
        {   
            this.emailAddress = emailAddress;   
            this.mobilePhone = mobilePhone;   
            this.amount = amount;   
        }   
    }   

    //发布者，也就是被监视的对象-银行账号   
    class BankAccount   
    {   
        //声明一个处理银行交易的委托   
        public delegate void ProcessTranEventHandler(object sender, UserEventArgs e);   
        //声明一个事件   
        public event ProcessTranEventHandler ProcessTran;   

        protected virtual void OnProcessTran(UserEventArgs e)   
        {   
            if (ProcessTran != null)   
            {   
                ProcessTran(this, e);   
            }   
        }   

        public void Prcess(UserEventArgs e)   
        {   
            OnProcessTran(e);   
        }   
    }   

    //观察者Email   
    class Email   
    {   
        public static void SendEmail(object sender, UserEventArgs e)   
        {   
            Console.WriteLine("向用户邮箱" + e.emailAddress + "发送邮件:您在"+System.DateTime.Now.ToString()+"取款金额为"+e.amount);   
        }   
    }   

    //观察者手机   
    class Mobile   
    {   
        public static void SendNotification(object sender, UserEventArgs e)   
        {   
            Console.WriteLine("向用户手机" + e.mobilePhone + "发送短信:您在" + System.DateTime.Now.ToString() + "取款金额为" + e.amount);   
        }   
    }   

    //订阅系统，实现银行系统订阅几个Observer，实现与客户端的松耦合   
    class SubscribSystem   
    {   
        public SubscribSystem()   
        {   
 
        }   

        public SubscribSystem(BankAccount bankAccount, UserEventArgs e)   
        {   
            //现在我们在银行账户订阅2个，分别是电子邮件和手机短信   
            bankAccount.ProcessTran += new BankAccount.ProcessTranEventHandler(Email.SendEmail);   
            bankAccount.ProcessTran += new BankAccount.ProcessTranEventHandler(Mobile.SendNotification);   
            bankAccount.Prcess(e);   
        }   
    }   

    class Client   
    {   
        public static void Main(string[] args)   
        {   
            Console.Write("请输入您要取款的金额：");   
            string amount = Console.ReadLine();   
            Console.WriteLine("交易成功，请取磁卡。");   
            //初始化e   
            UserEventArgs user = new UserEventArgs("jinjiangbo2008@163.com", "18868789776",amount);   
            //初始化订阅系统   
            SubscribSystem subject = new SubscribSystem(new BankAccount(), user);   
            Console.ReadKey();   
        }   
    }   

网上还有个热水器烧水的OBSERVER PATTERN 也是蛮经典的，大家可以看看。<br/>   
<br/>   
下一讲我们要讲讲，在我们的日常的MES系统开发中，到底在什么场景用到委托事件，毕竟我们学了这样的技术，我们必须要用起来，这才有价值嘛！<br/>   
<br/>   
呵呵！下讲，将会更加精彩！