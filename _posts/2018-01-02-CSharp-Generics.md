---
layout: post
title: "C# 泛型"
date:   2018-1-2 10:50:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



原文地址： https://www.cnblogs.com/yueyue184/p/5032156.html   

 我们在编写程序时，经常遇到两个模块的功能非常相似，只是一个是处理int数据，另一个是处理string数据，或者其他自定义的数据类型，但我们没有办法，只能分别写多个方法处理每个数据类型，因为方法的参数类型不同。有没有一种办法，在方法中传入通用的数据类型，这样不就可以合并代码了吗？泛型的出现就是专门解决这个问题的。读完本篇文章，你会对泛型有更深的了解。

为什么要使用泛型

为了了解这个问题，我们先看下面的代码，代码省略了一些内容，但功能是实现一个栈，这个栈只能处理int数据类型：

    public class Stack
    {

        private int[] m_item;

        public int Pop(){...}

        public void Push(int item){...}

        public Stack(int i)
        {

            this.m_item = new int[i];

        }

    }

上面代码运行的很好，但是，当我们需要一个栈来保存string类型时，该怎么办呢？很多人都会想到把上面的代码复制一份，把int改成string不就行了。当然，这样做本身是没有任何问题的，但一个优秀的程序是不会这样做的，因为他想到若以后再需要long、Node类型的栈该怎样做呢？还要再复制吗？优秀的程序员会想到用一个通用的数据类型object来实现这个栈：

    public class Stack
    {
        private object[] m_item;

        public object Pop(){...}

        public void Push(object item){...}

        public Stack(int i)
        {

            this.m_item = new[i];

        }
    }

这个栈写的不错，他非常灵活，可以接收任何数据类型，可以说是一劳永逸。但全面地讲，也不是没有缺陷的，主要表现在：

当Stack处理值类型时，会出现装箱、折箱操作，这将在托管堆上分配和回收大量的变量，若数据量大，则性能损失非常严重。    
在处理引用类型时，虽然没有装箱和折箱操作，但将用到数据类型的强制转换操作，增加处理器的负担。    
在数据类型的强制转换上还有更严重的问题（假设stack是Stack的一个实例）：  

    Node1 x = new Node1();
    stack.Push(x);
    Node2 y = (Node2)stack.Pop();

上面的代码在编译时是完全没问题的，但由于Push了一个Node1类型的数据，但在Pop时却要求转换为Node2类型，这将出现程序运行时的类型转换异常，但却逃离了编译器的检查。
 

针对object类型栈的问题，我们引入泛型，他可以优雅地解决这些问题。泛型用用一个通过的数据类型T来代替object，在类实例化时指定T的类型，运行时（Runtime）自动编译为本地代码，运行效率和代码质量都有很大提高，并且保证数据类型安全。

 

使用泛型 

下面是用泛型来重写上面的栈，用一个通用的数据类型T来作为一个占位符，等待在实例化时用一个实际的类型来代替。让我们来看看泛型的威力：

    public class Stack<T>
    {

        private T[] m_item;

        public T Pop(){...}

        public void Push(T item){...}

        public Stack(int i)

        {
            this.m_item = new T[i];
        }

    }

类的写法不变，只是引入了通用数据类型T就可以适用于任何数据类型，并且类型安全的。这个类的调用方法：

//实例化只能保存int类型的类

    Stack<int> a = new Stack<int>(100);
    a.Push(10);
    a.Push("8888"); //这一行编译不通过，因为类a只接收int类型的数据
    int x = a.Pop();

 

//实例化只能保存string类型的类

    Stack<string> b = new Stack<string>(100);

    b.Push(10);    //这一行编译不通过，因为类b只接收string类型的数据

    b.Push("8888");

    string y = b.Pop();

 

这个类和object实现的类有截然不同的区别：

1. 他是类型安全的。实例化了int类型的栈，就不能处理string类型的数据，其他数据类型也一样。

2. 无需装箱和折箱。这个类在实例化时，按照所传入的数据类型生成本地代码，本地代码数据类型已确定，所以无需装箱和折箱。

3. 无需类型转换。

 

泛型类实例化的理论

C#泛型类在编译时，先生成中间代码IL，通用类型T只是一个占位符。在实例化类时，根据用户指定的数据类型代替T并由即时编译器（JIT）生成本地代码，这个本地代码中已经使用了实际的数据类型，等同于用实际类型写的类，所以不同的封闭类的本地代码是不一样的。按照这个原理，我们可以这样认为：

泛型类的不同的封闭类是分别不同的数据类型。

例：Stack<int>和Stack<string>是两个完全没有任何关系的类，你可以把他看成类A和类B，这个解释对泛型类的静态成员的理解有很大帮助。

 