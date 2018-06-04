---          
layout: post          
title: "WCF 双工通信"          
date:   2018-6-4 13:15:00           
categories: "WCF"          
catalog: true          
tags:           
    - WCF          
---          
          
        
        
双工（Duplex）模式的消息交换方式体现在消息交换过程中，参与的双方均可以向对方发送消息。基于双工MEP消息交换可以看成是多个基本模式下（比如请求-回复模式和单项模式）消息交换的组合。双工MEP又具有一些变体，比如典型的订阅-发布模式就可以看成是双工模式的一种表现形式。双工消息交换模式使服务端回调（Callback）客户端操作成为可能。      
    
# 请求过程中的回调    
    
这是一种比较典型的双工消息交换模式的表现形式，客户端在进行服务调用的时候，附加上一个回调对象；服务在对处理该处理中，通过客户端附加的回调对象（实际上是调用回调服务的代理对象）回调客户端的操作（该操作在客户端执行）。整个消息交换的过程实际上由两个基本的消息交换构成，其一是客户端正常的服务请求，其二则是服务端对客户端的回调。两者可以采用请求-回复模式，也可以采用单向（One-way）的MEP进行消息交换。    
    
Server:    
    
	public interface ICallback    
    {    
        [OperationContract(IsOneWay = true)]    
        void DisplayResult(double x, double y, double result);    
    }    
	    
	[ServiceContract( CallbackContract=typeof(ICallback))]    
    public interface IService1    
    {    
        [OperationContract(IsOneWay =true)]    
        void Add(double x, double y);    
    }       
	    
	public class Service1 : IService1    
    {    
        public void Add(double x, double y)    
        {    
            double result = x + y;    
            ICallback callback = OperationContext.Current.GetCallbackChannel<ICallback>();    
            callback.DisplayResult(x, y, result);    
        }    
    }    
	    
Client:     
    
	public class ServicesCallback : ServiceReference1.IService1Callback    
    {    
        public void DisplayResult(double x, double y, double result)    
        {    
            Console.WriteLine("x + y = {2} when x = {0} and y = {1}", x, y, result);    
        }    
    }    
	    
	class Program    
    {    
        static void Main(string[] args)    
        {    
            InstanceContext instanceContext = new InstanceContext(new ServicesCallback());    
            ServiceReference1.Service1Client client = new ServiceReference1.Service1Client(instanceContext);    
            client.Add(1.0, 2.1);    
            Console.WriteLine("End");    
            Console.Read();    
        }    
    }    
    
# 订阅-发布    
    
订阅-发布模式是双工模式的一个典型的变体。在这个模式下，消息交换的双方变成了订阅者和发布者，若干订阅者就某个主题向发布者申请订阅，发布者将所有的订阅者保存在一个订阅者列表中，在某个时刻将主题发送给该主题的所有订阅者。实际上基于订阅-发布模式的消息交换也可以看成是两个基本模式下消息交换的组合，申请订阅是一个单向模式的消息交换（如果订阅者行为得到订阅的回馈，该消息交换也可以采用请求-回复模式）；而主题发布也是一个基于单向模式的消息交换过程。    
    
Server:    
    
	public interface INotifyCallback    
    {    
        [OperationContract(IsOneWay = true)]    
        void NotifyCallback(string sender);    
    }    
	    
	[ServiceContract(CallbackContract = typeof(INotifyCallback))]    
    public interface IService1    
    {    
        [OperationContract(IsOneWay = true)]    
        void RegisterClient();    
    
        [OperationContract(IsOneWay = true)]    
        void GetString(int data);    
    }        
	    
	[ServiceBehavior(ConcurrencyMode = ConcurrencyMode.Multiple, InstanceContextMode = InstanceContextMode.Single)]    
    public class Service1 : IService1    
    {    
        private static List<INotifyCallback> clientCallbackList;    
        public Service1()    
        {    
            clientCallbackList = new List<INotifyCallback>();    
        }    
    
        public void RegisterClient()    
        {    
            INotifyCallback clientCallback = OperationContext.Current.GetCallbackChannel<INotifyCallback>();    
            OperationContext.Current.Channel.Closing += Channel_Closing;    
            clientCallbackList.Add(clientCallback);    
        }    
    
        private void Channel_Closing(object sender, EventArgs e)    
        {    
            lock (clientCallbackList)    
            {    
                clientCallbackList.Remove((INotifyCallback)sender);    
            }    
        }    
    
        public static void NotifyClient(string msg)    
        {    
            if (string.IsNullOrEmpty(msg))    
            {    
                return;    
            }    
    
            if (clientCallbackList == null)    
            {    
                return;    
            }    
    
            foreach (var item in clientCallbackList)    
            {    
                item.NotifyCallback(msg);    
            }    
        }    
    
        public void GetString(int data)    
        {    
            NotifyClient("You input " + data);    
        }    
    }    
	    
Client:    
    
	class NotifyClientCallback : ServiceReference1.IService1Callback    
    {    
        public void NotifyCallback(string sender)    
        {    
            Console.WriteLine(sender);    
        }    
    }    
	    
	class Program    
    {    
        static void Main(string[] args)    
        {    
            string serverNotifyAddress = "net.tcp://localhost/test/service.svc/tcp";    
                
            var binding = new NetTcpBinding();    
            var address = new EndpointAddress(serverNotifyAddress);    
            binding.Security.Mode = SecurityMode.None;    
            InstanceContext instanceContext = new InstanceContext(new NotifyClientCallback());    
            DuplexChannelFactory<ServiceReference1.IService1> factory = new DuplexChannelFactory<ServiceReference1.IService1>(instanceContext, binding, address);    
            var channel = factory.CreateChannel();    
            channel.RegisterClient();    
            channel.GetString(23);    
    
            Console.ReadKey();    
        }    
    }