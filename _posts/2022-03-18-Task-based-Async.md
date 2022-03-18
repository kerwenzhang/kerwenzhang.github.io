---                
layout: post            
title: "基于事件的异步模式(TAP)该怎么写"                
date:   2022-3-18 15:30:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

# 三种异步模式
.NET 提供了执行异步操作的三种模式：  

基于任务的异步模式 (TAP) ，该模式使用单一方法表示异步操作的开始和完成。 TAP 是在 .NET Framework 4 中引入的。 这是在 .NET 中进行异步编程的推荐方法。 C# 中的 async 和 await 关键词为 TAP 添加了语言支持。   

基于事件的异步模式 (EAP)，是提供异步行为的基于事件的旧模型。 这种模式需要后缀为 Async 的方法，以及一个或多个事件、事件处理程序委托类型和 EventArg 派生类型。 EAP 是在 .NET Framework 2.0 中引入的。 建议新开发中不再使用这种模式。  

异步编程模型 (APM) 模式（也称为 IAsyncResult 模式），这是使用 IAsyncResult 接口提供异步行为的旧模型。 在这种模式下，同步操作需要 Begin 和 End 方法（例如，BeginWrite 和 EndWrite以实现异步写入操作）。 不建议新的开发使用此模式。   

# TAP

基于任务的异步模式 Task-based asynchronous pattern (TAP)是基于 System.Threading.Tasks.Task 命名空间中的 System.Threading.Tasks.Task 和 System.Threading.Tasks 类型，这些类型用于表示任意异步操作。  

使用回调或事件来实现异步编程时，编写的代码不直观， APM 需要 Begin 和 End 方法。 EAP 需要后缀为 Async 的方法，以及一个或多个事件、事件处理程序委托类型和 EventArg 派生类型。这样很容易把代码搞得一团糟。TAP使用单个方法表示异步操作的开始和完成。 这与异步编程模型（APM 或 IAsyncResult）模式和基于事件的异步模式 (EAP) 形成对比。它让编写异步代码变得容易和优雅。通过使用async/await关键字，可以像写同步代码那样编写异步代码，所有的回调和事件处理都交给编译器和运行时帮你处理了。

TAP 方法返回 System.Threading.Tasks.Task 或 System.Threading.Tasks.Task<TResult>，具体取决于相应同步方法返回的是 void 还是类型 TResult。  
TAP 方法的参数中不能添加 out 或 ref 参数，需要返回的所有数据应该由 TResult返回。  
一个典型的TAP 函数包括以下元素：  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/tap1.png?raw=true)  

async是一个专门给编译器的提示，意思是该函数的实现可能会出现await。

        Task<int> DelayAndCalculate1(int a, int b)
        {
            return Task.Delay(1000).ContinueWith(t => a + b);
        }

        async Task<int> DelayAndCalculate2(int a, int b)
        {
            await Task.Delay(1000);
            return a + b;
        }

这两个函数（不算函数名的不同），在函数声明上是完全没有区别的。只是其中一个在实现中使用了await，所以C#语法要求我们必须在标示async。  
另外interface的定义中不能写async，因为如上所述，async不是函数声明，而其实编译函数实现的提示。
其实真正重要的是await（和其他异步的实现，如例子中的DelayAndCalculate1），有没有async反而确实不重要。 
而await是一个标记，它告诉编译器生成一个等待器来等待可等待类型实例的运行结果。一个await对应一个等待器 ，任务的等待器类型是TaskAwaiter/TaskAwaiter<TResult>。  

await task等效于task.GetAwaiter().GetResult()。  
task.GetAwaiter() 返回TaskAwaiter/TaskAwaiter<TResult>  

        async Task<int> ComplexWorkFlow()
        {
            Task<int> task1 = DoTask1();
            Task<int> task2 = DoTask2();
            Task<int> task3 = DoTask3UseResultOfTask1(await task1);
            Task<int> task4 = DoTask4UseResultOfTask2(await task2);
            return await DoTask5(await task3, await task4);
        }

task1和task2可以并行执行，task3和task4可以并行执行（事实上更好的写法可以让task1->task3完全并行与task2->task4）。核心思路就是只有当某个task的执行结果需要被使用的时候才解开这个task的值（等它执行完毕）。  


## Task.Run vs Task<TResult>.Factory.StartNew


## ContinueWith



## Cancellation 


## WhenAll


# Reference

[基于任务的异步模式](https://docs.microsoft.com/zh-cn/dotnet/standard/asynchronous-programming-patterns/task-based-asynchronous-pattern-tap)  
[Asynchronous Programming in .NET – Task-based Asynchronous Pattern (TAP)](https://www.codeproject.com/Articles/1246939/Asynchronous-Programming-in-NET-Task-based-Asynchr#_articleTop)  
[Introduction to Task-Based Asynchronous Pattern in C# 4.5: Part I](https://www.c-sharpcorner.com/UploadFile/DipalChoksi/introduction-to-task-based-asynchronous-pattern-in-C-Sharp-4-5-part-i/)  
[c#中为什么async方法里必须还要有await？](https://www.zhihu.com/question/58922017)  
[C# TAP 异步编程 二 、await运算符已经可等待类型Awaitable](https://www.cnblogs.com/cdaniu/p/15703901.html)  
[C# Async / Await - Make your app more responsive and faster with asynchronous programming](https://www.youtube.com/watch?v=2moh18sh5p4&ab_channel=IAmTimCorey)  
[C# Advanced Async - Getting progress reports, cancelling tasks, and more](https://www.youtube.com/watch?v=ZTKGRJy5P2M&ab_channel=IAmTimCorey)  