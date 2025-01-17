---
layout: post
title: "C# 各个版本的新特性"
date:   2018-1-2 14:50:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



微软官方地址： https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/    
中文版：　https://docs.microsoft.com/zh-cn/dotnet/csharp/whats-new/    

 
## C# 2.0 版  VS2005

泛型

分部类型 （partial)

匿名方法 (在 C# 3.0 及更高版本中，Lambda 表达式取代匿名方法)

可以为 null 的类型

迭代器

协变和逆变

## C# 3.0 版 VS2008

自动实现属性

    class Customer
    {
        public double TotalPurchases { get; set; }
        ...
    }
    
    Customer cust1 = new Customer ()
    cust1.TotalPurchases += 499.99;

匿名类型

    var v = new { Amount = 108, Message = "Hello" };  
    
匿名类型通常用在查询表达式的 select 子句中，以便返回源序列中每个对象的属性子集。   

查询表达式

查询表达式必须以 from 子句开头，且必须以 select 或 group 子句结尾。

    int[] scores = { 90, 71, 82, 93, 75, 82 };
    IEnumerable<int> scoreQuery =
        from score in scores
        where score > 80
        orderby score descending
        select score;
        
    foreach(int testScore in scoreQuery)
    {
        Console.WriteLine(testScore);
    }
    
    IEnumerable<int> scoreQuery2 = scores.Where(c => c > 80);
    foreach(int testScore in scoreQuery2)
    {
        Console.WriteLine(testScore);
    }

Lambda 表达式

http://kerwenzhang.github.io/c%23/2016/11/16/CSharp-Lambda/  

表达式树

扩展方法

## C# 4.0 版 VS2010

动态绑定

名为/可选自变量

泛型协变和逆变

嵌入互操作类型

## C# 5.0 版 VS2012

异步成员

调用方信息特性

## C# 6.0 VS2015

只读自动属性：  可以创建只能在构造函数中设置的只读自动属性。  
自动属性初始值设定项：
可以编写初始化表达式来设置自动属性的初始值。  
Expression-bodied 函数成员：
可以使用 lambda 表达式创建单行方法。  
using static：
可以将单个类的所有方法导入当前命名空间。  
Null - 条件运算符：
可以简洁、安全地访问对象的成员，同时仍能使用 null 条件运算符检查 null。  
字符串内插：
可以使用内联表达式（而不是位置参数）编写字符串格式设置表达式。  
异常筛选器：
可以基于异常或其他程序状态的属性捕获表达式。  
nameof 表达式：
可以让编译器生成符号的字符串表示形式。  
Catch 和 Finally 块中的 Await：
可以在先前不允许使用 await 表达式的位置使用它们。  
索引初始值设定项：
可以为关联容器及序列容器创建初始化表达式。  
集合初始值设定项的扩展方法：
除成员方法以外，集合初始值设定项还可以依赖可访问的扩展方法。  
改进了重载解析：
先前生成了不明确的方法调用的某些构造现在可以正确解析。  

## C# 7.0 VS2017

out 变量
可以将 out 值内联作为参数声明到使用这些参数的方法中。  
元组
可以创建包含多个公共字段的轻量级未命名类型。 编译器和 IDE 工具可理解这些类型的语义。  
放弃
放弃是指在不关心所赋予的值时，赋值中使用的临时只写变量。 在对元组和用户定义类型进行解构，以及在使用 out 参数调用方法时，它们特别有用。  
模式匹配
可以基于任意类型和这些类型的成员的值创建分支逻辑。  
ref 局部变量和返回结果
方法参数和局部变量可以是对其他存储的引用。  
本地函数
可以将函数嵌套在其他函数内，以限制其范围和可见性。  
更多的 expression-bodied 成员
可使用表达式创作的成员列表有所增长。  
throw 表达式
可以在之前因为 throw 是语句而不被允许的代码构造中引发异常。  
通用的异步返回类型
使用 async 修饰符声明的方法可以返回除 Task 和 Task<T> 以外的其他类型。   
数字文本语法改进
新令牌可提高数值常量的可读性。   