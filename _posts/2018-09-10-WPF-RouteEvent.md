---                          
layout: post                          
title: "WPF 路由事件"                          
date:   2018-9-10 14:00:00                           
categories: "WPF"                          
catalog: true                          
tags:                           
    - WPF                          
---                
        
## 简单的事件模型    
    
事件的前身是消息，消息的本质就是一组数据记录要执行的操作，然后消息处理函数根据消息的数据执行相应的操作，那么在消息处理函数中就充斥这大量的判断或者switch，这样对于大型应用程序的开发带来了不少麻烦。为了简单的开发微软封装了一套简单的事件模型。以前了解过window form的应该都知道，当托一个按钮到窗体后然后双击按钮就可以在.cs代码自动生成有关事件的代码，这就是一个简单的事件模型.    
事件模型包括一下几个部分：    
    
事件的拥有者：就是按钮：button1    
事件：就是button1.Click，在Form1.cs中    
事件的处理器就是这个方法button1_Click    
订阅关系：也就是说事件和事件处理器如何建立联系的呢：    
    
	this.button1.Click += new System.EventHandler(this.button1_Click);    
	    
这里就建立了事件和事件处理器的联系，当然一个事件我们也可以定义多个处理器相应。    
最后一个响应者：就是窗体本身    
    
## 路由事件模型     
传统的简单事件模型中，在消息激发是将消息通过事件订阅的然后交给事件的响应者，事件的响应者使用事件的处理器来做出相应，这样就存在一个问题，用户控件内部的事件就不能被外界订阅，因为事件的宿主必须能够直接访问到事件的响应者。    
路由事件的事件拥有者和事件的响应者之间则没有直接的显式订阅关系，事件的拥有者则只负责激发事件，事件将由谁响应它并不知道，事件的响应者则有事件的监听器，针对事件进行监听，当有此类事件传递至此事件响应者就使用事件处理器来响应事件并决定此事件是否继续传递。比如像上一个程序中的，点击“点我”以后事件就开始激发了，然后事件就会在控件树上进行传递，事件的响应者安装了监听器，当监听到这个事件进行响应，并决定这个事件是否继续传递。    
如果当事件在某个节点处理以后，不想让它继续传递，可以把它标记为“已处理”，就会停止路由，所有的路由事件都共享一个公共的事件数据基类 RoutedEventArgs。RoutedEventArgs 定义了一个采用布尔值的 Handled 属性。把事件设为已处理只要把Handled属性设为true即可    
    
	<Window x:Class="RouteEventWpfDemo.MainWindow"    
			xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"    
			xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"    
			xmlns:d="http://schemas.microsoft.com/expression/blend/2008"    
			xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"    
			xmlns:local="clr-namespace:RouteEventWpfDemo"    
			mc:Ignorable="d"    
			Title="MainWindow" Height="450" Width="800">    
		<Grid x:Name="GridA">    
			<Grid x:Name="GridB">    
				<Grid x:Name="GridC">    
					<Button Canvas.Left="101" Canvas.Top="68" Content="Button" Height="23" Name="ButtonA" Width="75" />    
				</Grid>    
			</Grid>    
		</Grid>    
	</Window>    
    
	namespace RouteEventWpfDemo    
	{    
		/// <summary>    
		/// Interaction logic for MainWindow.xaml    
		/// </summary>    
		public partial class MainWindow : Window    
		{    
			public MainWindow()    
			{    
				InitializeComponent();    
				//为GridA添加Button.ClickEvent监听    
				this.GridA.AddHandler(Button.ClickEvent, new RoutedEventHandler(this.ButtonA_Click));    
				//为GridB添加Button.ClickEvent监听    
				this.GridB.AddHandler(Button.ClickEvent, new RoutedEventHandler(this.ButtonA_Click));    
				//为GridC添加Button.ClickEvent监听    
				this.GridC.AddHandler(Button.ClickEvent, new RoutedEventHandler(this.ButtonA_Click));    
			}    
    
			private void ButtonA_Click(object sender, RoutedEventArgs e)    
			{    
				MessageBox.Show(((Grid)sender).Name);    
				if (((Grid)sender).Name == "GridB")    
				{    
					e.Handled = true;    
				}    
			}    
		}    
	}    
	    
## 自定义路由事件    
自定义路由事件大体需要三个步骤：    
1、声明并注册路由事件    
2、为路由事件添加CLR事件包装    
3、创建可以激发路由事件的方法    
    
	<Window x:Class="RouteEventWpfDemo.MainWindow"    
			xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"    
			xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"    
			xmlns:d="http://schemas.microsoft.com/expression/blend/2008"    
			xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"    
			xmlns:local="clr-namespace:RouteEventWpfDemo"    
			local:TimeButton.ReportTime="ReportTimeHandler"    
			mc:Ignorable="d"    
			Title="MainWindow" Height="450" Width="800">    
		<Grid x:Name="GridA" local:TimeButton.ReportTime="ReportTimeHandler">    
			<Grid x:Name="GridB" local:TimeButton.ReportTime="ReportTimeHandler">    
				<Grid x:Name="GridC" local:TimeButton.ReportTime="ReportTimeHandler">    
					<StackPanel x:Name="StackPanelA" local:TimeButton.ReportTime="ReportTimeHandler">    
						<ListBox x:Name="listBox"/>    
						<local:TimeButton x:Name="btnTime" Content="时间"  local:TimeButton.ReportTime="ReportTimeHandler" />    
					</StackPanel>    
				</Grid>    
			</Grid>    
		</Grid>    
	</Window>    
	    
	namespace RouteEventWpfDemo    
	{    
		/// <summary>    
		/// Interaction logic for MainWindow.xaml    
		/// </summary>    
		public partial class MainWindow : Window    
		{    
			public MainWindow()    
			{    
				InitializeComponent();    
			}    
    
			private void ReportTimeHandler(object sender, ReportTimeEventArgs e)    
			{    
				FrameworkElement element = (FrameworkElement)sender;    
				string timeStr = e.ClickTime.ToString("HH:mm:ss");    
				string content = string.Format("{0}==>到达{1}", timeStr, element.Name);    
				this.listBox.Items.Add(content);    
			}    
		}    
		    
		public class ReportTimeEventArgs : RoutedEventArgs    
		{    
			public ReportTimeEventArgs(RoutedEvent routedEvent, object source)    
				: base(routedEvent, source)    
			{ }    
    
			/// <summary>    
			/// 记录点击时间    
			/// </summary>    
			public DateTime ClickTime { get; set; }    
		}    
		    
		public class TimeButton : Button    
		{    
			//声明并注册路由事件    
			/*    
			 * 1、第一个参数ReportTime 为路由事件的名称    
			 * 2、第二个参数是路由事件的策略，包括Bubble冒泡式，Tunnel隧道式，Direct直达式（和直接事件类似）    
			 * 3、第三个参数用于指定事件处理器的类型    
			 * 4、第四个参数用于指定事件的宿主是哪一种类型    
			 */    
			public static readonly RoutedEvent ReportTimeEvent = EventManager.RegisterRoutedEvent    
				("ReportTime", RoutingStrategy.Bubble, typeof(EventHandler<ReportTimeEventArgs>), typeof(TimeButton));    
    
			//CLR事件包装器    
			public event RoutedEventHandler ReportTime    
			{    
				add { this.AddHandler(ReportTimeEvent, value); }    
				remove { this.RemoveHandler(ReportTimeEvent, value); }    
			}    
    
			//激发路由事件，借用Click事件的激发方法    
			protected override void OnClick()    
			{    
				base.OnClick();    
    
				ReportTimeEventArgs args = new ReportTimeEventArgs(ReportTimeEvent, this);    
				args.ClickTime = DateTime.Now;    
				this.RaiseEvent(args);    
			}    
		}    
	}    
	    
当路由事件的路由策略被设置为Bulle（冒泡式）时，路由事件的消息会从事件的触发者开始向它的上级容器控件一层一层的往外传，直至最外层的容器控件；而将事件的路由策略设置为Tunnel（隧道式）时，效果刚好与冒泡式相反，从最外层容器一层一层往内传；对于直达式就不用多说了吧。     
    
简单事件模型通过事件订阅将事件的发布者与事件的订阅者紧密联系在一起，事件被触发时，事件发布者通过事件订阅将事件消息直接发送给事件订阅者，事件订阅者使用事件处理方法对事件的发生进行响应；而路由事件的发布者与响应者之间并不存在这种直接的订阅关系，事件的发布者只负责发布事件，而不用关心事件由谁来响应，因为事件发布者其实早就心知肚明，只有那些安装了事件侦听器的对象才会成为事件的响应者，至于谁愿意成为这个响应者他可不关心，而那些想侦听事件消息的对象只需要安装事件的侦听器，就可以侦听事件消息的达到，当事件消息到达时，使用事件处理方法进行响应。至于路由事件的消息采用何种方式来传递，取决于该路由事件采取何种路由策略。    
    
## 附加事件    
在wpf中还有一种事件附加事件，像前面说的路由事件它的事件宿主都是我们可以看到的界面元素，但是附加事件不具备显式在用户界面上的能力，比如一个文本框的改变，鼠标的按下，键盘的按下这些事件都是附加事件的例子    
还是上面的例子我们给他加上颜色改变事件    
    
	<Window x:Class="RouteEventWpfDemo.MainWindow"    
			xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"    
			xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"    
			xmlns:d="http://schemas.microsoft.com/expression/blend/2008"    
			xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"    
			xmlns:local="clr-namespace:RouteEventWpfDemo"    
			local:TimeButton.ReportTime="ReportTimeHandler"    
			mc:Ignorable="d"    
			Title="MainWindow" Height="450" Width="800">    
		<Grid x:Name="GridA" local:TimeButton.ReportTime="ReportTimeHandler">    
			<Grid x:Name="GridB" local:TimeButton.ReportTime="ReportTimeHandler">    
				<Grid x:Name="GridC" local:TimeButton.ReportTime="ReportTimeHandler">    
					<StackPanel x:Name="StackPanelA" local:TimeButton.ReportTime="ReportTimeHandler">    
						<ListBox x:Name="listBox"/>    
						<local:TimeButton x:Name="btnTime" Content="时间"  local:TimeButton.ReportTime="ReportTimeHandler" />    
					</StackPanel>    
				</Grid>    
			</Grid>    
		</Grid>    
	</Window>    
	    
	namespace RouteEventWpfDemo    
	{    
		/// <summary>    
		/// Interaction logic for MainWindow.xaml    
		/// </summary>    
		public partial class MainWindow : Window    
		{    
			public MainWindow()    
			{    
				InitializeComponent();    
				//btnTime添加路由事件监听    
				TimeButton.AddColorChangedHandler(this.btnTime, new RoutedEventHandler(this.ColorChangedHandler));    
			}    
    
			private void ReportTimeHandler(object sender, ReportTimeEventArgs e)    
			{    
				FrameworkElement element = (FrameworkElement)sender;    
				string timeStr = e.ClickTime.ToString("HH:mm:ss");    
				string content = string.Format("{0}==>到达{1}", timeStr, element.Name);    
				this.listBox.Items.Add(content);    
    
				if (element.Name == "btnTime")    
				{    
					this.btnTime.Color = "123";    
					//准备消息传给路由事件    
					RoutedEventArgs args = new RoutedEventArgs(TimeButton.ColorChangedEvent, this.btnTime);    
					//引发事件    
					this.btnTime.RaiseEvent(args);    
				}    
			}    
    
			private void ColorChangedHandler(object sender, RoutedEventArgs e)    
			{    
				MessageBox.Show((e.OriginalSource as TimeButton).Color);    
			}    
		}    
		    
		public class ReportTimeEventArgs : RoutedEventArgs    
		{    
			public ReportTimeEventArgs(RoutedEvent routedEvent, object source)    
				: base(routedEvent, source)    
			{ }    
    
			/// <summary>    
			/// 记录点击时间    
			/// </summary>    
			public DateTime ClickTime { get; set; }    
		}    
		    
		public class TimeButton : Button    
		{    
			//声明并注册路由事件    
			/*    
			 * 1、第一个参数ReportTime 为路由事件的名称    
			 * 2、第二个参数是路由事件的策略，包括Bubble冒泡式，Tunnel隧道式，Direct直达式（和直接事件类似）    
			 * 3、第三个参数用于指定事件处理器的类型    
			 * 4、第四个参数用于指定事件的宿主是哪一种类型    
			 */    
			public static readonly RoutedEvent ReportTimeEvent = EventManager.RegisterRoutedEvent    
				("ReportTime", RoutingStrategy.Bubble, typeof(EventHandler<ReportTimeEventArgs>), typeof(TimeButton));    
    
			//CLR事件包装器    
			public event RoutedEventHandler ReportTime    
			{    
				add { this.AddHandler(ReportTimeEvent, value); }    
				remove { this.RemoveHandler(ReportTimeEvent, value); }    
			}    
    
			//激发路由事件，借用Click事件的激发方法    
			protected override void OnClick()    
			{    
				base.OnClick();    
    
				ReportTimeEventArgs args = new ReportTimeEventArgs(ReportTimeEvent, this);    
				args.ClickTime = DateTime.Now;    
				this.RaiseEvent(args);    
			}    
    
			/// <summary>    
			/// 声明颜色属性    
			/// </summary>    
			public string Color { get; set; }    
    
			/// <summary>    
			/// 声明并注册颜色改变路由事件    
			/// </summary>    
			public static readonly RoutedEvent ColorChangedEvent = EventManager.RegisterRoutedEvent    
			  ("ColorChanged", RoutingStrategy.Bubble, typeof(EventHandler<ReportTimeEventArgs>), typeof(TimeButton));    
    
			/// <summary>    
			/// 添加颜色改变事件    
			/// </summary>    
			/// <param name="d"></param>    
			/// <param name="e"></param>    
			public static void AddColorChangedHandler(DependencyObject d, RoutedEventHandler e)    
			{    
				UIElement ui = (UIElement)d;    
				if (ui != null)    
				{    
					ui.AddHandler(TimeButton.ColorChangedEvent, e);    
				}    
			}    
    
			/// <summary>    
			/// 删除颜色改变事件    
			/// </summary>    
			/// <param name="d"></param>    
			/// <param name="e"></param>    
			public static void RemoveColorChangedHandler(DependencyObject d, RoutedEventHandler e)    
			{    
				UIElement ui = (UIElement)d;    
				if (ui != null)    
				{    
					ui.RemoveHandler(TimeButton.ColorChangedEvent, e);    
				}    
			}    
		}    
	}    
    
[WPF学习之路由事件](https://www.cnblogs.com/JerryWang1991/archive/2013/03/29/2981103.html)