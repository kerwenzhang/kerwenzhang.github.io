---                
layout: post                
title: "WPF中的视觉树和逻辑树"                
date:   2018-7-9 13:50:00                 
categories: "WPF"                
catalog: true                
tags:                 
    - WPF                
---      
  
## 可视化树  
  
可视化树代表你界面上所有的渲染在屏幕上的元素。可视化树用于渲染，事件路由，定位资源（如果该元素没有逻辑父元素）等等等等。向上或者向下遍历可视化树可以简单的使用VisualTreeHelper和简单的递归方法。  
然后，还是有个小别扭让它变得复杂。任何承继自ContentElement的东西都可以在UI上显示，但其实并不在可视化树中。WPF会假定这些元素也在可视化树中，来保持事件路由的一致性，但这只是个幻觉。VisualTreeHelper对ContentElement对象不起作用，因为ContentElement不是继承自Visual或者Visual3D.  
内容元素(继承自ContentElement的类)不是可视化树的一部分；他们不是继承自Visual而且没有可视化表示。为了显示在UI上，ContentElement必须寄宿在一个Visual主体上，通常是一个FrameworkElement。你可以认为主体类似于一个可以选择如何展示该ContentElement的浏览器。一旦一个Content被显示主体捕获，这个Content就可以加入到一个特定的和可视化树相关的树处理过程中。  
这意味着你永远没办法仅仅使用VisualTreeHelper来遍历可视化树。如果你把一个ContentElement传递给VisualTreeHelper的GetParent或者GetChild方法，会抛出一个异常。因为ContentElement不是Visual或者Visual3D的子类，你只能沿着逻辑树查找ContentElement的父元素，直到找到一个Visual对象。  
  
	DependencyObject FindVisualTreeRoot (DependencyObject initial)  
	{  
		DependencyObject current = initial;  
		DependencyObject result = initial;  
	   
	   
		While(current !=null)  
		{  
			result = current;  
			if(current is Visual || current is Visual3D)  
			{  
				current = VisualTreeHelper.GetParent(current);  
			}  
			else  
			{  
				current = LogicalTreeHelper.GetParent(current);  
			}  
		}  
		return result;  
	}  
  
## 逻辑树  
  
逻辑树表示UI的核心结构。和XAML文件中定义的元素近乎相等，排除掉内部生成的那些用来帮助渲染的可视化元素。WPF用逻辑树来决定依赖属性，值继承，资源解决方案等。  
逻辑树用起来不像可视化树那么简单。对于新手来说，逻辑树可以包含类型对象，这一点和可视化树不同，可视化树只包含Dependancy子类的实例。遍历逻辑树时，要记住逻辑树的叶子可以是任何类型。由于LogicTreeHelper只对DependencyObject有效，遍历逻辑树时需要非常小心，最好做类型检查。看个例子：  
  
	void WalkDownLogicalTree(object current)  
	{  
		DoSomethingWithObjectInLogicalTree(current);  
	   
	   
		DependencyObject depObj = current as DependencyObject;  
	   
	   
		if(depObj != null)  
		{  
			foreach(object logicalChild in LogicalTreeHelper.GetChildren(depObj))  
				WalkDownLogicalTree(logicalChild);  
		}  
	}  
  
一个给定的Window/Page/Control会有一棵视觉树，但是可以有几个逻辑树。这些逻辑树互相不相连。可以仅仅使用LogicalTreeHelper来在几棵逻辑树之间遍历。  
  
并不是所有的逻辑树结点都可以扩展为视觉树结点。只有从System.Windows.Media.Visual和System.Windows.Media.Visual3D继承的元素才能被视觉树包含。  
  
WPF中提供了遍历逻辑树和视觉树的辅助类：System.Windows.LogicalTreeHelper和System.Windows.Media.VisualTreeHelper。注意遍历的位置，逻辑树可以在类的构造函数中遍历。但是，视觉树必须在经过至少一次的布局后才能形成。所以它不能在构造函数遍历。通常是在OnContentRendered进行，这个函数为在布局发生后被调用。  
其实每个Tree结点元素本身也包含了遍历的方法。比如，Visual类包含了三个保护成员方法VisualParent、VisualChildrenCount、GetVisualChild。通过它们可以访问Visual的父元素和子元素。而对于FrameworkElement，它通常定义了一个公共的Parent属性表示其逻辑父元素。特定的FrameworkElement子类用不同的方式暴露了它的逻辑子元素。比如部分子元素是Children Collection，有是有时Content属性  
  
## 打印视觉树和逻辑树  
  
xaml代码：  
  
	<Window x:Class="WpfApplication1.MainWindow"  
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
        Title="MainWindow" Height="350" Width="525"  
        Loaded="Window_Loaded_1">  
		<Grid>  
			<Button Content="button" Margin="179,131,206,150"></Button>  
		</Grid>  
	</Window>  
	  
后台cs代码：  
  
	private void Window_Loaded_1(object sender, RoutedEventArgs e)  
	{  
		StringBuilder tree = new StringBuilder();  
		PrintVisualTree(this, 0, tree);  
		Console.WriteLine("VisualTree:");  
		Console.WriteLine(tree.ToString());  
  
		tree.Clear();  
		PrintLogicalTree(this, 0, tree);  
		Console.WriteLine("LogicalTree:");  
		Console.WriteLine(tree.ToString());  
	}  
  
	public void PrintVisualTree(DependencyObject obj, int level, StringBuilder tree)  
	{  
		tree.AppendLine(new string(' ', level) + obj);  
		for (int i = 0; i < VisualTreeHelper.GetChildrenCount(obj); i++)  
		{  
			PrintVisualTree(VisualTreeHelper.GetChild(obj, i), level + 1, tree);  
		}  
	}  
  
	public void PrintLogicalTree(DependencyObject obj, int level, StringBuilder tree)  
	{  
		tree.AppendLine(new string(' ', level) + obj);  
		foreach (var v in LogicalTreeHelper.GetChildren(obj))  
		{  
			if (v is DependencyObject)  
			{  
				PrintLogicalTree(v as DependencyObject, level + 1, tree);  
			}  
		}  
	}  
   
输出：  
  
	VisualTree:  
	WpfApplication1.MainWindow  
	 System.Windows.Controls.Border  
	  System.Windows.Documents.AdornerDecorator  
	   System.Windows.Controls.ContentPresenter  
		System.Windows.Controls.Grid  
		 System.Windows.Controls.Button: button  
		  Microsoft.Windows.Themes.ButtonChrome  
		   System.Windows.Controls.ContentPresenter  
			System.Windows.Controls.TextBlock  
	   System.Windows.Documents.AdornerLayer  
	   
	LogicalTree:  
	WpfApplication1.MainWindow  
	 System.Windows.Controls.Grid  
	  System.Windows.Controls.Button: button  
  
