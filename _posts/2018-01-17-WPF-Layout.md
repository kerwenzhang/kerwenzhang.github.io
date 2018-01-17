---  
layout: post  
title: "WFP布局"  
date:   2018-1-17 20:30:00   
categories: "WPF"  
catalog: true  
tags:   
    - WPF  
---  
  
  
## WFP布局  
WPF布局包括两个阶段：一个测量（measure）阶段和一个排列(arrange)阶段。在测量阶段，容器遍历所有子元素，并询问子元素它们所期望的大小。在排列阶段，容器在合适的位置放置子元素。  
  
#### Canvas   
Canvas面板是最轻量级的布局容器，它不会自动调整内部元素的排列和大小，不指定元素位置，元素将默认显示在画布的左上方。Canvas主要用来画图。  
Canvas默认不会自动裁剪超过自身范围的内容，即溢出的内容会显示在Canvas外面，这是因为Canvas的ClipToBounds属性默认值是false，我们可以显式地设置为true来裁剪多出的内容。  
  
	<Canvas Margin="10,10,10,10" Background="White" >  
         <Rectangle Name="rect" Canvas.Left="300" Canvas.Top="180" Fill="Black" Stroke="Red"  Width="200" Height="200"/>  
         <Ellipse  Name="el" Canvas.Left="160" Canvas.Top="150" Fill="Azure" Stroke="Green" Width="180" Height="180"/>  
     </Canvas>  
  
#### StackPanel   
StackPanel就是将子元素按照堆栈的形式一一排列，可以通过设置StackPanel的Orientation属性设置两种排列方式：横排（Horizontal，该值为默认值）和竖排（Vertical）。纵向的StackPanel每个元素默认宽度与面板一样宽，反之横向是高度和面板一样高。如果包含的元素超过了面板控件，它会被截断多出的内容。  
可以通过Orientation属性来设置StackPanel是横排（设置其值为Vertical）还是竖排（设置其值为Horizontal）。	   
  
	<StackPanel Margin="10,10,10,10" Background="Azure">  
        <Label>A Button Stack</Label>  
        <Button Content="Button 1"></Button>  
        <Button>Button 2</Button>  
        <Button>Button 3</Button>  
        <Button Content="Button 4"></Button>  
    </StackPanel>  
	  
#### WrapPanel   
WrapPanel面板在可能的空间中，一次以一行或一列的方式布置控件。  
默认情况下，WrapPanel.Orientation属性设置为Horizontal，控件从左向右进行排列，然后再在下一行中排列，但你可将WrapPanel.Orientation设置为Vertical，从而在多个列中放置元素。  
  
WrapPanel面板实际上用来控制用户界面中一小部分的布局细节，并非用于控制整个窗口布局。  
  
	<WrapPanel Margin="10" Background="Azure">  
        <Button VerticalAlignment="Top" Margin="5">Top Button</Button>  
        <Button MinHeight="50"> Tall Button 2</Button>  
        <Button VerticalAlignment="Bottom">Bottom Button</Button>  
        <Button>Stretch Button</Button>  
        <Button VerticalAlignment="Center">Center Button</Button>  
        <Button>Next Button</Button>  
    </WrapPanel>  
	  
#### DockPanel   
DockPanel面板定义一个区域，在此区域中，你可以使子元素通过锚点的形式进行排列。DockPanel类似于WinForm中Dock属性的功能。对于在DockPanel中的元素的停靠可以通过Panel.Dock的附加属性来设置，如果设置LastChildFill属性为true，则最后一个元素将填充剩余的所有空间。  
  
	<DockPanel Margin="10" Background="Azure" LastChildFill="True">  
        <Button DockPanel.Dock="Top" Background="Red">Top Button</Button>       
        <Button DockPanel.Dock="Left" Background="Gray">Left Button</Button>  
        <Button DockPanel.Dock="Right" Background="Green">Right Button</Button>  
        <Button DockPanel.Dock="Bottom"  Background="White">Bottom Button</Button>  
        <Button>Remaining Button</Button>  
    </DockPanel>  
	  
#### Grid   
Grid比起其他Panel，功能是最多最为复杂的布局控件。它由<Grid.ColumnDefinitions>列元素集合和<Grid.RowDefinitions>行元素集合两种元素组成。而放在Grid面板中的元素必须显式采用附加属性定义其所在行和列，否则元素均默认放置在第0行第0列。  
  
	<Grid Width="Auto" Height="Auto">  
        <Grid.RowDefinitions>  
            <RowDefinition Height="*"/>  
            <RowDefinition Height="Auto"/>  
        </Grid.RowDefinitions>  
        <Grid.ColumnDefinitions>  
            <ColumnDefinition Width="120"/>  
            <ColumnDefinition Width="150"/>  
            <ColumnDefinition Width="*"/>  
            <ColumnDefinition Width="2*"/>  
        </Grid.ColumnDefinitions>  
        <Rectangle Grid.Row="0" Grid.Column="0" Fill="Green" Margin="10,10,10,20"/>  
        <Rectangle Grid.Row="0" Grid.Column="1" Grid.ColumnSpan="2" Fill="Blue" Margin="10,10,10,20"/>  
        <Rectangle Grid.Row="0" Grid.Column="4" Fill="Orange"/>  
        <Button Grid.Row="1" Grid.Column="0">Button 2</Button>  
        <Rectangle Grid.Row="1" Grid.Column="1" Grid.ColumnSpan="3" Fill="Red"/>  
    </Grid>  
	  
定义Grid的列宽和行高可采用固定、自动和按比例三种方式定义。  
  
　　第一种：固定长度——宽度不够时，元素会被裁剪，单位是pixel;  
  
　　第二种：自动长度——自动匹配行中最宽元素的高度。  
  
　　第三种：比例长度——"*"表示占用剩余的全部宽度或高度，两行都是*，则将剩余高度平分。像上面的一个2*，一个*，表示前者2/3宽度。  
  
#### UniformGrid  
UniformGrid是Grid简化版本，不像Grid面板，UniformGrid不需要预先定义行集合和列集合，反而，通过简单设置Rows和Columns属性来设置尺寸。每个单元格始终具有相同的大小。UniformGrid每个单元格只能容纳一个元素，将自动按照在其内部的元素个数，自动创建行和列，并通过保存相同的行列数。  
  
	<UniformGrid>  
        <Ellipse Margin="10" Fill="Gray"/>  
        <Ellipse Margin="10" Fill="Gray"/>  
        <Ellipse Margin="10" Fill="Green"/>  
        <Ellipse Margin="10" Fill="Green"/>  
        <Ellipse Margin="10" Fill="Red"/>  
    </UniformGrid>  
	  
#### ScrollViewer  
通常用户界面中的内容比计算机屏幕的显示区域大的时候，可以利用ScrollViewer控件可以方便地使应用程序中的内容具备滚动功能。  
  
	<Grid>  
        <ScrollViewer HorizontalScrollBarVisibility="Visible" VerticalScrollBarVisibility="Auto">  
            <Rectangle Width="500" Height="400" Fill="Green"/>  
        </ScrollViewer>  
    </Grid>  
	  
## 综合运用  
  
	<Window x:Class="WPFLayoutDemo.MainWindow"  
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"  
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"  
        WindowStartupLocation="CenterScreen"  
        Title="布局综合运用实例" Height="400" Width="480">  
		<DockPanel Width="Auto" Height="Auto" LastChildFill="True">  
			<!--顶部菜单区域-->  
			<Menu Width="Auto" Height="20" Background="LightGray" DockPanel.Dock="Top">  
				<!--File菜单项-->  
				<MenuItem Header="文件">  
					<MenuItem Header="保存"/>  
					<Separator/>  
					<MenuItem Header="退出"/>  
				</MenuItem>  
				<!--About 菜单项-->  
				<MenuItem Header="帮助">  
					<MenuItem Header="关于本产品"/>  
				</MenuItem>  
			</Menu>  
  
			<!--状态栏-->  
			<StackPanel Width="Auto" Height="25" Background="LightGray" Orientation="Horizontal" DockPanel.Dock="Bottom">  
				<Label Width="Auto" Height="Auto" Content="状态栏" FontFamily="Arial" FontSize="12"/>  
			</StackPanel>  
			<!--Left-->  
			<StackPanel Width="130" Height="Auto" Background="Gray" DockPanel.Dock="Left">  
				<Button Margin="10" Width="Auto" Height="30" Content="导航栏"/>  
				<Button Margin="10" Width="Auto" Height="30" Content="导航栏"/>  
				<Button Margin="10" Width="Auto" Height="30" Content="导航栏"/>  
			</StackPanel>  
  
			<!--Right-->  
			<Grid Width="Auto" Height="Auto" Background="White">  
  
				<Grid.ColumnDefinitions>  
					<ColumnDefinition Width="*"/>  
					<ColumnDefinition Width="*"/>  
				</Grid.ColumnDefinitions>  
  
				<Grid.RowDefinitions>  
					<RowDefinition Height="*"/>  
					<RowDefinition Height="*"/>  
				</Grid.RowDefinitions>  
  
				<Rectangle Fill="Gray" Margin="10,10,10,10" Grid.Row="0" Grid.Column="0"/>  
				<Rectangle Fill="Gray" Margin="10,10,10,10" Grid.Row="0" Grid.Column="1"/>  
				<Rectangle Fill="Gray" Margin="10,10,10,10" Grid.Row="1" Grid.Column="0"/>  
				<Rectangle Fill="Gray" Margin="10,10,10,10" Grid.Row="1" Grid.Column="1"/>  
			</Grid>  
		</DockPanel>  
	     
	</Window>