---
layout: post
title: "C# 操作SQL数据库"
date: 2023-12-14 9:00:00
categories: "C#"
catalog: true
tags:
  - C#
---

# 数据库基本操作

C# 中的 SqlCommand 允许用户查询数据库并发送SQL命令。 SQL命令由SQL连接对象指定。 最常见的有两种方法，用于查询结果的 `ExecuteReader` 方法和用于插入、更新和删除命令的 `ExecuteNonQuery` 方法。 
在正式开始前，先在SQL Server里创建一个Demodb数据库。在Demodb里创建一个demotb的表。表里只有两列TutorialID和TutorialName。插入两行测试数据.
|TutorialID|TutorialName|
|--|--|
|1|C#|
|2|ASP.NET|

使用Visual Studio，创建一个winForm应用程序`DemoApplication`
## 连接数据库
1. 在form上添加一个Connect button
2. 在click事件里添加代码

        private void buttonConnect_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection cnn;
            connetionString = @"Data Source=xxxx;Initial Catalog=Demodb;Trusted_Connection=Yes;";
            cnn = new SqlConnection(connetionString);
            cnn.Open();
            MessageBox.Show("Connection Open  !");
            cnn.Close();
        }

## 读取数据
读取数据需要用到SqlCommand，SqlCommand用于执行数据库的读写操作。  
SqlDataReader 用于获取 SQL 查询命令返回的数据， 获取到数据后我们可以使用dataReader.Read()按行读取所有数据。  

    private void buttonConnect_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=F3JW9G3;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlCommand command;
        SqlDataReader dataReader;
        String sql, output = "";
        sql = "Select TutorialID, TutorialName from demotb";
        command = new SqlCommand(sql, cnn);
        dataReader = command.ExecuteReader();

        while(dataReader.Read())
        {
            output += dataReader.GetValue(0) + " - " + dataReader.GetValue(1) + "\n";
        }


        MessageBox.Show(output);
        dataReader.Close();
        command.Dispose();
        cnn.Close();
    }

最后注意关闭所有SQL连接。  

## 插入数据  
插入数据需要用到SqlDataAdapter  

    private void buttonWrite_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=xxxx;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlDataAdapter adapter = new SqlDataAdapter();
        string sql = "Insert into demotb (TutorialID, TutorialName) values(3, '"+ "VB.NET" + "')";

        adapter.InsertCommand = new SqlCommand(sql, cnn);
        adapter.InsertCommand.ExecuteNonQuery();

        MessageBox.Show("Success to write database");
        cnn.Close();
    }

## 更新数据库

    private void buttonUpdate_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=F3JW9G3;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlDataAdapter adapter = new SqlDataAdapter();
        string sql = "Update demotb set TutorialName ='" + "C#.NET"+"' where TutorialID=3";

        adapter.UpdateCommand = new SqlCommand(sql, cnn);
        adapter.UpdateCommand.ExecuteNonQuery();

        MessageBox.Show("Success to update database");
        cnn.Close();
    }

## 删除  

    private void buttonDelete_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=xxxx;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlDataAdapter adapter = new SqlDataAdapter();
        string sql = "Delete demotb where TutorialID=3";

        adapter.DeleteCommand = new SqlCommand(sql, cnn);
        adapter.DeleteCommand.ExecuteNonQuery();

        MessageBox.Show("Success to delete database");
        cnn.Close();
    }

# ADODB
## OLEDB, ADODB, ADO.NET
Oledb（Object Linking and Embedding DB）和 ODBC 都是与数据库通信的标准. OLEDB 是 Microsoft设计的标准，它定义了一组用于访问数据库的 API（应用程序接口）函数。它其实是一个 COM（组件对象模型）API，是 ODBC的一种高级替代者和继承者。通常，OLEDB 用于创建特定于数据库的驱动程序（称为提供程序），该驱动程序可由更高级别的数据访问库（如 ADO 或 ADO.NET）实现。   

ADODB （ActiveX Data Objects DB）是 OLEDB 上的 API 层, 由 Microsoft 于 1996 年推出, 它基于 COM。适用于基于 MS 的数据库（如 Sql Server），提供一致的 API 和优化。ADODB 是 OLEDB 使用者。它与 OLEDB 通信，而 OLEDB 提供程序又直接与数据库或数据库服务器通信。  

ADO.Net 是基于 .Net 的数据库连接, 它是 .NET Framework 的一个组件， 是ADODB的升级/替换。ADO.NET 内置了对 SQL Server、OleDB 和 ODBC 的支持. ADO.Net 现在使用 System.Data.SqlClient 库为MS 的数据库提供服务。

### ADODB vs ADO.NET
 ADO（和 ADO.NET 都是用于Microsoft环境中数据访问的技术，但它们在体系结构、功能和编程模型方面有很大不同。  
1. 结构  
  ADO：它遵循连接的体系结构模型，其中与数据库建立连接，并直接通过连接访问和操作数据。  
  ADO.NET：它遵循断开连接的体系结构模型，其中数据从数据库中检索，存储在 DataSet（或其他数据容器）中，并与数据库断开连接。可以在本地操作数据，并在必要时对数据库进行更改。  
2. 数据访问组件
  ADO：它使用 Recordset 和 Connection 等对象来管理数据访问和检索。  
  ADO.NET：它使用 DataSet、DataTable、DataReader 和 DataAdapter 作为主要数据访问组件。DataSet 表示具有多个 DataTable 的数据的内存中缓存，DataAdapter 促进了数据库和 DataSet 之间的通信。  
3. 可扩展性和性能  
  ADO：对于大型数据集，它的效率可能较低，因为它需要与数据库的持续连接，这可能会影响性能。  
  ADO.NET：其断开连接的特性允许提高可扩展性和性能。数据可以获取一次，然后在本地操作，而无需连续的数据库连接。  
4. 语言独立性  
  ADO：它主要设计用于基于 COM 的语言，如 VB6 和 VBScript，但它也可以与其他语言一起使用。  
  ADO.NET：它基于 .NET Framework 构建，与语言无关，可以从各种 .NET 语言（如 C#、VB.NET 和 F#）访问。  
5. 安全性和性能优化  
  ADO：它提供有限的内置安全功能和优化选项。  
  ADO.NET：它提供了改进的安全措施，例如防止 SQL 注入的参数化查询，以及连接池和异步数据访问等性能优化技术。  

# Reference
[C# Database Connection: How to connect SQL Server (Example)](https://www.guru99.com/c-sharp-access-database.htm)  
[ADO 和 ADO.NET 之间的差异](https://net-informations.com/faq/ado/ado-difference.htm)  