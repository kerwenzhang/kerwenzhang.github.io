---
layout: post
title: 代码整洁之道(Clean Code)学习笔记
date:   2016-11-22 14:50:14
categories: "Book"
catalog: true
tags: 
    - Book
---


## 什么是整洁代码

优雅和高效的代码。代码逻辑应当直接了当，叫缺陷难以隐藏；尽量减少依赖关系，使之便于维护；依据某种分层战略完善错误处理代码；性能调至最优，省得引诱别人做没规矩的优化，搞出一堆混乱来。<b>整洁的代码只做好一件事。</b>  

糟糕的代码想做太多事，它意图混乱、目的含混。整洁的代码力求集中。每个函数、每个类和每个模块都全神贯注于一事，完全不受四周细节的干扰和污染。  

整洁的代码简单直接。<b>整洁的代码如同优美的散文</b>。整洁的代码从不隐藏设计者的意图，充满了<b>干净利落的抽象</b>和<b>直截了当的控制语句</b>。  
消除重复和提高表达力， 只要铭记这两点，改进脏代码时就会大有不同。  

我们在写代码时，读与写花费时间的比例超过10:1. 写新代码时，我们一直在读旧代码。既然比例如此之高，我们就想让读的过程变得轻松，即便那会使得编写过程更难。  
这事概无例外。不读周边代码的话就没法写代码。编写代码的难度，取决于读周边代码的难度。想要干得快，想要早点做完，想要轻松写代码，先让代码易读吧。    

## 有意义的命名  

#### 名副其实  

变量、函数或类的名称应该已经答复了所有的大问题。它该告诉你，它为什么会存在，它做什么事，应该怎么用。<b>如果名称需要注释来补充，那就不算是名副其实。</b>  
代码示例：

    public List<int[]> getThem() 
    {
        List<int[]> list1 = new ArrayList<int[]>();
        for (int[] x: theList)
            if (x[0] == 4)
                list1.add(x);
        return list1;
    }

上面这段代码里面没有复杂的表达式。空格和缩进中规中矩。只用到三个变量和两个常量，但仍然难以说明这段代码要做什么事。  

问题不在于代码的简洁度，而是在于代码的<b><red>模糊度</red></b>： 即上下文在代码中未被明确体现的程度。 读懂上述代码，我们需要先了解以下几个问题：  
1. theList 中是什么类型的东西？  
2. theList 零下标条目的意义是什么？  
3. 值4的意义是什么？  
4. 我怎么使用返回的列表？  

问题的答案没体现在代码段中，可那就是它们应该在的地方。 

## 函数

#### 短小

函数的第一规则是要短小。第二条规则是<b>还要更短小</b>。  
if语句、else语句、while语句等，其中的代码块应该只有一行。该行大抵应该是一个函数调用语句。  
函数的缩进层级不该多于一层或两层。  

#### 只做一件事

<b><I> 函数应该做一件事。做好这件事。只做这一件事</I></b>  

如果函数只是做了该函数名下同一抽象层上的步骤，则函数只做了一件事。  

要判断函数是否不止做了一件事，还有一个方法，就是看<b>是否能再拆出一个函数，该函数不仅只是单纯地重新诠释其实现</b>。  

#### 每个函数一个抽象层级

<b>自顶向下读代码： 向下规则</b>   

程序就像是一系列To起头的段落, 每一段都描述当前抽象层级， 并引用位于下一抽象层级的后续To起头段落。  

<I>To include the setups and teardowns, we include setups, then we inlude the test page content, and then we include the teardowns.</I>  

<I>To include the setups, we include the suite setup if this is a suite, then we include the regular setup.</I>  

<I>To include the suite setup, we search the parent and add an include statement.</I>  

<I>To search the parent...</I>   

#### 函数参数

最理想的参数数量是零， 其次是一， 再次是二， 应尽量避免三。  

标识参数丑陋不堪。向函数传入布尔值显示的表明本函数不止做一件事。如果标识为true将会这样做， 标识为false则会那样做。  

<b>如果函数看来需要两个、三个或三个以上参数， 就说明其中一些参数应该封装为类了。</b>

#### 分隔指令与询问

函数要么做什么事，要么回答什么事， 但两者不可兼得。

#### 使用异常替代返回错误代码

    if (deletePage(page) == E_OK) 
    {
        if (registry.deleteReference(page.name) == E_OK) 
        {
            if (configKeys.deleteKey(page.name.makeKey()) == E_OK) 
            {
                logger.log("page deleted");
            } 
            else 
            {
                logger.log("configKey not deleted");
            }
        } 
        else 
        {
            logger.log("deleteReference from registry failed");
        }
    } 
    else 
    {
        logger.log("delete failed");
        return E_ERROR;
    }
    
如果使用异常替代返回错误码， 错误处理代码就能从主路径代码中分离出来，得到简化：  

    try 
    {
        deletePage(page);
        registry.deleteReference(page.name);
        configKeys.deleteKey(page.name.makeKey());
    }
    catch (Exception e) 
    {
        logger.log(e.getMessage());
    }

#### 抽离 Try/Catch 代码块

Try/Catch代码块会搞乱代码结构，把错误处理与正常流程混为一谈。最好把try和catch代码块的主体部分抽离出来，另外形成函数.  

    public void delete(Page page) 
    {
        try 
        {
            deletePageAndAllReferences(page);
        }
        catch (Exception e) 
        {
            logError(e);
        }
    }
    
    private void deletePageAndAllReferences(Page page) throws Exception 
    {
        deletePage(page);
        registry.deleteReference(page.name);
        configKeys.deleteKey(page.name.makeKey());
    }
    
    private void logError(Exception e) 
    {
        logger.log(e.getMessage());
    }
	
## 注释

注释的恰当用法是弥补我们在用代码表达意图时遭遇的失败。  
之所以贬低注释，是因为注释会撒谎。 <b>注释存在的时间越久， 就离其所描述的代码越远， 越来越变得全然错误。</b> 原因很简单， 程序员不能坚持维护注释。  

带有少量注释的简洁而有表达力的代码， 要比带有大量注释的零碎而复杂的代码像样得多。 与其花时间编写解释你搞出的糟糕的代码的注释， 不如花时间清洁那堆糟糕的代码。   

## 对象和数据结构

#### 德墨忒耳律

著名的德墨忒尔律认为， 模块不应该了解它所操作对象的内部情形。 类C的方法f只应该调用以下对象的方法：  
1） C  
2） 由f创建的对象  
3） 作为参数传递给f的对象  
4） 由C的实体变量持有的对象  

## 系统

软件系统应该将起始过程和起始过程之后的运行时逻辑分离开， 在起始过程中构建应用对象。  
将构造与使用分开的方法之一是将全部构造过程搬迁到main或被称之为main的模块中， 设计系统的其余部分时， 假设所有对象都已经正确构造和设置。  

## 迭进

简单设计的四条规则：  
1） 运行所有测试  
2） 不可重复  
3） 保证表达力  
4） 尽可能减少类和方法的数量  

重复是拥有良好设计系统的大敌。 它代表着额外的工作、额外的风险和额外且不必要的复杂度。  
<b>小规模复用可以大量降低系统复杂性。</b>  

代码应当清晰地表达其作者的意图，作者把代码写得越清晰， 其他人花在理解代码上的时间也就越少， 从而减少缺陷， 缩减维护成本。  
