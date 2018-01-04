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
微软官方文档： https://docs.microsoft.com/zh-cn/dotnet/csharp/programming-guide/generics/    

C# 语言和公共语言运行时 (CLR) 的 2.0 版本中添加了泛型。 泛型将类型参数的概念引入 .NET Framework，这样就可以设计具有以下特征的类和方法：在客户端代码声明并初始化这些类和方法之前，这些类和方法会延迟指定一个或多个类型。 例如，通过使用泛型类型参数 T，可以编写其他客户端代码能够使用的单个类，而不会产生运行时转换或装箱操作的成本或风险

## 为什么要使用泛型

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

 

## 使用泛型 

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

微软官方提供的一个例子：

    // Declare the generic class.
    public class GenericList<T>
    {
        void Add(T input) { }
    }
    class TestGenericList
    {
        private class ExampleClass { }
        static void Main()
        {
            // Declare a list of type int.
            GenericList<int> list1 = new GenericList<int>();

            // Declare a list of type string.
            GenericList<string> list2 = new GenericList<string>();

            // Declare a list of type ExampleClass.
            GenericList<ExampleClass> list3 = new GenericList<ExampleClass>();
        }
    } 
 

这个类和object实现的类有截然不同的区别：

1. 他是类型安全的。实例化了int类型的栈，就不能处理string类型的数据，其他数据类型也一样。

2. 无需装箱和折箱。这个类在实例化时，按照所传入的数据类型生成本地代码，本地代码数据类型已确定，所以无需装箱和折箱。

3. 无需类型转换。

 
Example:

    class IntStack
    {
        private int[] members;
        private int point = 0;
        public IntStack(int count)
        {
            members = new int[count];
        }
        public bool Push(int data)
        {
            if(point < members.Count())
            {
                members[point] = data;
                point++;
                return true;
            }
            return false;
        }
        public bool Pop(ref int data)
        {
            if(point > 0)
            {
                data = members[point - 1];
                point--;
                return true;
            }
            data = -1;
            return false;
        }
        public void Display()
        {
            foreach(int data in members)
            {
                Console.WriteLine(data);
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            IntStack stack = new IntStack(10);
            int[] data = new int[] { 2, 43, 1, 7, 4, 8, 5, 67, 19, 30 };
            foreach(int temp in data)
            {
                stack.Push(temp);
            }
            stack.Display();
            Console.WriteLine("Begin to popup");
            for(int i = 0; i < data.Count(); i++)
            {
                int temp = -1;
                stack.Pop(ref temp);
                Console.WriteLine(temp);
            }
            Console.ReadKey();
        }
    }
 
改成泛型：

    class GenericStack<T>
    {
        private T[] members;
        private int point = 0;
        public GenericStack(int count)
        {
            members = new T[count];
        }
        public bool Push(T data)
        {
            if (point < members.Count())
            {
                members[point] = data;
                point++;
                return true;
            }
            return false;
        }
        public bool Pop(ref T data)
        {
            if (point > 0)
            {
                data = members[point - 1];
                point--;
                return true;
            }
            return false;
        }
        public void Display()
        {
            foreach (T data in members)
            {
                Console.WriteLine(data);
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            int[] data = new int[] { 2, 43, 1, 7, 4, 8, 5, 67, 19, 30 };

            GenericStack<int> stack2 = new GenericStack<int>(10);
            foreach (int temp in data)
            {
                stack2.Push(temp);
            }
            stack2.Display();
            Console.WriteLine("Begin to popup");
            for (int i = 0; i < data.Count(); i++)
            {
                int temp = -1;
                stack2.Pop(ref temp);
                Console.WriteLine(temp);
            }
            Console.ReadKey();
        }
    }
    
## 泛型约束  

定义泛型类时，可以对实例化类时用的参数类型施加限制。 这些限制称为约束。 通过使用 where 关键字指定约束。  

where T: struct	类型参数必须是值类型。 可以指定除 Nullable 以外的任何值类型。 有关详细信息，请参阅使用可以为 null 的类型。  
where T : class	类型参数必须是引用类型；这同样适用于所有类、接口、委托或数组类型。  
where T : new()	类型参数必须具有公共无参数构造函数。 与其他约束一起使用时，new() 约束必须最后指定。  
where T : <base class name>	类型参数必须是指定的基类或派生自指定的基类。  
where T : <interface name>	类型参数必须是指定的接口或实现指定的接口。 可指定多个接口约束。 约束接口也可以是泛型。  
where T : U	为 T 提供的类型参数必须是为 U 提供的参数或派生自为 U 提供的参数。  

例如：  

    public class GenericList<T> where T : Employee
    
    class EmployeeList<T> where T : Employee, IEmployee, System.IComparable<T>, new()
    
## 泛型方法

    static void Swap<T>(ref T data1, ref T data2)
    {
        T temp;
        temp = data1;
        data1 = data2;
        data2 = temp;
    }
    
    static void Main(string[] args)
    {
        int data1 = 2;
        int data2 = 3;
        Swap<int>(ref data1, ref data2);
    }