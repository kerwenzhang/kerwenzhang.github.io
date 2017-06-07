---
layout: post
title: "C# string 特殊的引用类型"
date:   2017-06-06 16:48:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



## String的不变性

    string str1 = "ab";
    string str2 = str1;
    str1 = "abc";
    Console.WriteLine("str1 is {0},str2 is {1}", str1, str2);
    Console.Read();

输出结果：

    //str1 is abc,str2 is ab
    
    
string最为显著的一个特点就是它具有恒定不变性：我们一旦创建了一个string，在managed heap 上为他分配了一块连续的内存空间，我们将不能以任何方式对这个string进行修改使之变长、变短、改变格式。所有对这个string进行各项操作（比如调用ToUpper获得大写格式的string）而返回的string，实际上另一个重新创建的string，其本身并不会产生任何变化。   

string   对象是不可变的（只读），因为一旦创建了该对象，就不能修改该对象的值。有的时候看来似乎修改了，实际是string经过了特殊处理，每次改变值时都会建立一个新的string对象，变量会指向这个新的对象，而原来的还是指向原来的对象，所以不会改变。这也是string效率低下的原因。  

String的不变，并非说string不能改变，而是其值不能改变。  

在例子中str1="ab",这时在内存中就将“ab”存下来，如果再创建字符串对象，其值也等于“ab”，str2="ab",则并非再重新分配内存空间，而是将之前保存的“ab”的地址赋给str2的引用，这就能印证例子2中的结果。而当str1="abc"其值发生改变时，这时检查内存，发现不存在此字符串，则重新分配内存空间，存储“abc”，并将其地址赋给str1，而str2依然指向“ab”的地址。可以印证例子1中的结果。  