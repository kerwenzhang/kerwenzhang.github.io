---
layout: post
title: SQL 存储过程
date:   2023-02-15 9:13:14
categories: "SQL"
catalog: true
tags: 
    - SQL
---

# 什么是存储过程  
存储过程（stored procedure）是一组为了完成特定功能的sql语句集。经过编译以后存储在数据库中，存储过程可能包含程序流、逻辑流以及对数据库的查询。他可以接受参数。输出参数，返回单个或者多个结果集以及返回值。  

# 为什么使用存储过程  
1. 提高性能  
SQL语句在创建过程时进行分析和编译。 存储过程是预编译的，在首次运行一个存储过程时，查询优化器对其进行分析、优化，并给出最终被存在系统表中的存储计划，这样，在执行过程时便可节省此开销。  
2. 降低网络开销  
存储过程调用时只需用提供存储过程名和必要的参数信息，从而可降低网络的流量。  
3. 便于进行代码移植  
数据库专业人员可以随时对存储过程进行修改，但对应用程序源代码却毫无影响，从而极大的提高了程序的可移植性。  
4. 更强的安全性  
1）系统管理员可以对执行的某一个存储过程进行权限限制，避免非授权用户对数据的访问  
2）在通过网络调用过程时，只有对执行过程的调用是可见的。 因此，恶意用户无法看到表和数据库对象名称、嵌入自己的 Transact-SQL 语句或搜索关键数据。  
3）使用过程参数有助于避免 SQL 注入攻击。 因为参数输入被视作文字值而非可执行代码，所以，攻击者将命令插入过程内的 Transact-SQL 语句并损害安全性将更为困难。  
4）可以对过程进行加密，这有助于对源代码进行模糊处理。   

劣势：  
1. 存储过程需要专门的数据库开发人员进行维护，但实际情况是，往往由程序开发员人员兼职  
2. 设计逻辑变更，修改存储过程没有SQL灵活  

# 存储过程的种类  
1.用户指定以的存储过程，  
2.系统，默认的存储过程。  
3.扩展存储过程。（少见）  

# 存储过程的规则  
1、可以引用在同一存储过程中创建的对象，只要引用时已经创建了该对象即可。  
2、可以在存储过程内引用临时表。如果在存储过程内创建本地临时表,则临时表仅为该存储过程而存在;退出该存储过程后，临时表将消失  
3、如果执行的存储过程将调用另一个存储过程,则被调用的存储过程可以访问由第一个存储过程创建的所有对象，包括临时表在内。   
4、如果执行对远程Microsoft SOL Server 2008实例进行更改的远程存储过程，则不能回滚这些更改。远程存储过程不参与事务处理。   
5、存储过程中的参数的最大数目为2100。  
6、存储过程中的局部变量的最大数目仅受可用内存的限制  
7、根据可用内存的不同，存储过程最大可达128mb。  

# 语法

SQL Server Management Studio -> 找到database, 右键 New Query, 会弹出编辑窗口  
无参数:  

    create procedure GetBatchHis
    as
    begin
        select * from batchhis;
    end

点工具栏中的Execute，会在database > Programmability -> Stored Procedures 下生成procedure

    执行： exec GetBatchHis
    删除: drop procedure if exists GetBatchHis

有输入参数：

    create proc GetBatchHisWithParam(@BatchID varchar(255))
    As
        select count(UniqueID) from batchhis where BatchID=@BatchID
    Go

    执行： exec GetBatchHisWithParam @BatchID='STRAWBERRY'

有输出参数：

    create proc GetBatchHisWithOutParam
    @BatchID varchar(255),
    @Count int output
    As
        select @Count=count(UniqueID) from batchhis where BatchID=@BatchID
    Go

    执行: 
    declare @count1 int
    exec GetBatchHisWithOutParam @BatchID='STRAWBERRY', @count=@count1 output;
    print @count1

# Reference  
[SQL 存储过程](https://blog.csdn.net/paoe1612205661/article/details/127280048)  
[SQL总结（五）存储过程](https://www.cnblogs.com/yank/p/4235609.html)  
[SQL存储过程](https://www.jianshu.com/p/77c888044efd)  