---                  
layout: post                  
title: "WPF 使用 Converter"                  
date:   2018-7-10 15:50:00                   
categories: "WPF"                  
catalog: true                  
tags:                   
    - WPF                  
---        
    
[WPF 绑定中Converter的应用](https://blog.csdn.net/u012046379/article/details/50948047)  
  
在WPF 经常用到绑定，如果绑定的源数据和目标属性是同类型的则不需要转换, 如果是不同类型的数据我们要怎么做呢？比如有一个文本框，一个按钮，我一个文本框里输入一个的数字用来代表颜色，1表示“红色”，2 表示“绿色”,3表示“蓝色”。我输入对应的数字，按钮的文字显示对应颜色。    
显然这个不是同类型的数据：文本框的数据是String类型，而按钮的文字颜色是Brush类型，这个时候我们就需要用到转换器（converter）来告诉我们的banding怎么转换我们的数据。首先定义一个转换器（类）,命名为NumberToColor，要想实现转换的功能，必须实现IValueConverter接口中的Convert和ConvertBack两个函数。Convert函数是把我们的数据来源转换为目标数据的方法，这里就是把文本框里的string类型转换为Brush类型。我们这样实现Convert函数，(参数value就是数据来源的值，这里就是文本框中的数据，返回值就是Brush)  
  
	public class NumberToColor : IValueConverter  
    {  
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)  
        {  
            int colorValue = System.Convert.ToInt32(value);  
            switch (colorValue)  
            {  
                case 1:              //red  
                    return new SolidColorBrush(Colors.Red);  
  
                case 2:               //green  
                    return new SolidColorBrush(Colors.Green);  
                case 3:               //blue  
                    return new SolidColorBrush(Colors.Blue);  
  
            }  
            return new SolidColorBrush(Colors.LawnGreen);  
        }  
  
        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)  
        {  
            throw new NotImplementedException();  
        }  
    }  
	  
在xaml代码，显示一个文本框和一个按钮，并把按钮的前景色绑定到文本框的文本属性上，使用自定义的Number2Color转换器，运行程序  你修改文本框中的值，会看到按钮颜色发生变化。  
  
	<Window x:Class="WpfApp1.MainWindow"  
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"  
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"  
        xmlns:local="clr-namespace:WpfApp1"  
        mc:Ignorable="d"  
        Title="MainWindow" Height="450" Width="800">  
		<Window.Resources>  
			<local:NumberToColor x:Key="N2C"/>  
		</Window.Resources>  
		  
		<Grid>  
			<Grid.RowDefinitions>  
				<RowDefinition Height="50"/>  
				<RowDefinition Height="50"/>  
				<RowDefinition Height="30"/>  
				<RowDefinition Height="50"/>  
				<RowDefinition/>  
			</Grid.RowDefinitions>  
			  
			<TextBox x:Name="colorText" Text="1"  BorderBrush="Gray" BorderThickness="2" Width="200" Grid.Row="1"/>  
			<Button x:Name="testBtn" Content="Test" Width="100" Grid.Row="3" FontSize="25" Foreground="{Binding Path=Text,ElementName=colorText, Converter={StaticResource N2C}}"/>  
		</Grid>  
	</Window>  
	  
如果想实现按钮的文字颜色发生改变，文本框中的文字也对应改变。添加3个按钮，点击按钮的时候改变“测试”按钮的文字颜色。  
将绑定设置为双向绑定，我们为绑定增加属性：Mode=TwoWay， 在ConvertBack中增加转换方法  
  
	public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)  
	{  
		SolidColorBrush sb = (SolidColorBrush)value;  
		Color c = sb.Color;  
		if (c == Colors.Red)  
		{  
			return 1;  
		}  
		else if (c == Colors.Green)  
		{  
			return 2;  
		}  
		else if (c == Colors.Blue)  
		{  
			return 3;  
		}  
		return 0;  
	}  
	  
xaml:  
  
	<TextBox x:Name="colorText" Text="1"  BorderBrush="Gray" BorderThickness="2" Width="200" Grid.Row="1"/>  
	<Button x:Name="testBtn" Content="Test" Width="100" Grid.Row="3" FontSize="25" Foreground="{Binding Path=Text,ElementName=colorText, Converter={StaticResource N2C}, Mode=TwoWay}"/>  
	<StackPanel Orientation="Horizontal">  
		<Button Content="Red" Width="100" Foreground="Red" Click="btnClick"/>  
		<Button Content="Green" Width="100" Foreground="Green" Click="btnClick"/>  
		<Button Content="Blue" Width="100" Foreground="Blue" Click="btnClick"/>  
	</StackPanel>  
	  
button 事件：  
  
	private void btnClick(object sender, RoutedEventArgs e)  
	{  
		testBtn.Foreground = ((Button)sender).Foreground;  
	}