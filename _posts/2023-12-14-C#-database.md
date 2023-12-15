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

## 准备工作
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
            connetionString = @"Data Source=localhost;Initial Catalog=Demodb;Trusted_Connection=Yes;";
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
        connetionString = @"Data Source=localhost;Initial Catalog=Demodb;Trusted_Connection=Yes;";
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
        connetionString = @"Data Source=localhost;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlDataAdapter adapter = new SqlDataAdapter();
        string sql = "Insert into demotb (TutorialID, TutorialName) values(3, '"+ "VB.NET" + "')";

        adapter.InsertCommand = new SqlCommand(sql, cnn);
        adapter.InsertCommand.ExecuteNonQuery();

        MessageBox.Show("Success to write database");
        cnn.Close();
    }

## 更新数据

    private void buttonUpdate_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=localhost;Initial Catalog=Demodb;Trusted_Connection=Yes;";
        cnn = new SqlConnection(connetionString);
        cnn.Open();

        SqlDataAdapter adapter = new SqlDataAdapter();
        string sql = "Update demotb set TutorialName ='" + "C#.NET"+"' where TutorialID=3";

        adapter.UpdateCommand = new SqlCommand(sql, cnn);
        adapter.UpdateCommand.ExecuteNonQuery();

        MessageBox.Show("Success to update database");
        cnn.Close();
    }

## 删除数据  

    private void buttonDelete_Click(object sender, EventArgs e)
    {
        string connetionString;
        SqlConnection cnn;
        connetionString = @"Data Source=localhost;Initial Catalog=Demodb;Trusted_Connection=Yes;";
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
 ADO和 ADO.NET 都是用于Microsoft环境中数据访问的技术，但它们在体系结构、功能和编程模型方面有很大不同。  
1. 结构  
  ADO：它遵循连接的体系结构模型，与数据库建立连接，并直接通过连接访问和操作数据。  
  ADO.NET：它遵循断开连接的体系结构模型，从数据库中检索数据，将其存储在 DataSet（或其他数据容器）中，然后断开数据库连接。用户可以在本地操作数据，并在必要时对数据库进行更改。  
2. 数据访问组件
  ADO：使用 Recordset 和 Connection 等来访问和检索数据。  
  ADO.NET：使用 DataSet、DataTable、DataReader 和 DataAdapter 作为主要数据访问组件。DataSet 具有多个 DataTable，是数据在内存中的缓存，DataAdapter 方便了数据库和 DataSet 之间的通信。  
3. 可扩展性和性能  
  ADO：对于大型数据集，它的效率可能较低，因为它需要与数据库的持续连接，这可能会影响性能。  
  ADO.NET：其断开连接的特性允许提高可扩展性和性能。数据可以获取一次，然后在本地操作，而无需连续的数据库连接。  
4. 语言独立性  
  ADO：它主要设计用于基于 COM 的语言，如 VB6 和 VBScript，但它也可以与其他语言一起使用。  
  ADO.NET：它基于 .NET Framework 构建，与语言无关，可以从各种 .NET 语言（如 C#、VB.NET 和 F#）访问。  
5. 安全性和性能优化  
  ADO：它提供有限的内置安全功能和优化选项。  
  ADO.NET：它提供了改进的安全措施，例如防止 SQL 注入的参数化查询，以及连接池和异步数据访问等性能优化技术。  


## 实例
添加ADODB引用  
  在Reference上右键- Add Reference - 在COM tab页上搜索data，选择 `Microsoft ActiveX Data Objects 6.1 Library`
   ![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/db.png?raw=true)  
## 连接数据库
在form里新加一个button ADO Connect， 添加事件  

    private void buttonAdoConnect_Click(object sender, EventArgs e)
    {
        string str = "Provider=MSOLEDBSQL;Server=localhost;Database=Demodb;Trusted_Connection=Yes;";
        ADODB.Connection conn;
        conn = new ADODB.Connection();
        conn.Open(str, "", "", -1);  // connection Open
        MessageBox.Show("Success to connect database using ADODB");
        conn.Close();
    }
      
## 读取数据
在form里新加一个button ADO Read，添加事件  

    private void buttonAdoRead_Click(object sender, EventArgs e)
    {
        string str = "Provider=MSOLEDBSQL;Server=localhost;Database=Demodb;Trusted_Connection=Yes;";

        Connection conn = new Connection();
        Recordset rs = new Recordset();

        conn.Open(str);  // connection Open
                          
        rs.ActiveConnection = conn;
        rs.CursorLocation = CursorLocationEnum.adUseClient;
        rs.CursorType = CursorTypeEnum.adOpenForwardOnly;
        rs.LockType = LockTypeEnum.adLockReadOnly;
        rs.CacheSize = 500;

        string SQLQuery = "Select * from demotb";
        //* Execute query and get recordset
        rs.Open(SQLQuery, conn, CursorTypeEnum.adOpenUnspecified, LockTypeEnum.adLockUnspecified, (int)CommandTypeEnum.adCmdUnknown);

        rs.MoveFirst();
        string output = string.Empty;
        while(!rs.EOF)
        {
            string id = rs.Fields["TutorialID"].Value.ToString();
            string name = rs.Fields["TutorialName"].Value.ToString();
            output += id + " - " + name + "\n";

            rs.MoveNext();
        }

        rs.ActiveConnection = null;
        conn.Close();
        MessageBox.Show(output);
    }


## 插入数据  
在form里新加一个button ADO Write，添加事件   

    private void buttonAdoWrite_Click(object sender, EventArgs e)
    {
        string str = "Provider=MSOLEDBSQL;Server=localhost;Database=Demodb;Trusted_Connection=Yes;";

        ADODB.Connection conn = new Connection();
        
        conn.Open(str);  // connection Open

        ADODB.Command cmdInsert = new Command();
        cmdInsert.ActiveConnection = conn;

        cmdInsert.CommandText = "Insert into Demotb(TutorialID, TutorialName) VALUES(?,?)";
        cmdInsert.CommandType = CommandTypeEnum.adCmdText;

        ADODB.Parameter paramId = cmdInsert.CreateParameter(
            "TutorialID",
            DataTypeEnum.adVarChar,
            ParameterDirectionEnum.adParamInput,
            10,
            "3");
        cmdInsert.Parameters.Append(paramId);
        ADODB.Parameter paramName = cmdInsert.CreateParameter(
            "TutorialName",
            DataTypeEnum.adVarChar,
            ParameterDirectionEnum.adParamInput,
            10,
            "VB.Net");
        cmdInsert.Parameters.Append(paramName);
        object nRecrodsAffected = Type.Missing;
        object oParams = Type.Missing;
        cmdInsert.Execute(out nRecrodsAffected, ref oParams, (int)ExecuteOptionEnum.adExecuteNoRecords);

        conn.Close();
        MessageBox.Show("Success to write database");
    } 

## 更新数据
在form里新加一个button ADO Update，添加事件  

    private void buttonAdoUpdate_Click(object sender, EventArgs e)
    {
        string str = "Provider=MSOLEDBSQL;Server=localhost;Database=Demodb;Trusted_Connection=Yes;";

        ADODB.Connection conn = new Connection();

        conn.Open(str);  // connection Open

        ADODB.Command cmdInsert = new Command();
        cmdInsert.ActiveConnection = conn;

        //"Update demotb set TutorialName ='" + "C#NET"+"' where TutorialID=3"
        cmdInsert.CommandText = "Update Demotb set TutorialName = 'C#Net' where TutorialID='3'";
        cmdInsert.CommandType = CommandTypeEnum.adCmdText;
        
        object nRecrodsAffected = Type.Missing;
        object oParams = Type.Missing;
        cmdInsert.Execute(out nRecrodsAffected, ref oParams, (int)ExecuteOptionEnum.adExecuteNoRecords);

        conn.Close();
        MessageBox.Show("Success to update database");
    }

## 删除数据
在form里新加一个button ADO Delete，添加事件  

    private void buttonAdoDelete_Click(object sender, EventArgs e)
    {
        string str = "Provider=MSOLEDBSQL;Server=localhost;Database=Demodb;Trusted_Connection=Yes;";

        ADODB.Connection conn = new Connection();

        conn.Open(str);  // connection Open

        string command = "Delete from Demotb where TutorialID='3'";
        object nRecrodsAffected = Type.Missing;
        conn.Execute(command, out nRecrodsAffected, 0);

        conn.Close();
        MessageBox.Show("Success to DELETE data");
    }

# ADO.NET
ADO.NET 是一组向 .NET Framework 程序员公开数据访问服务的类。 ADO.NET 为创建分布式数据共享应用程序提供了一组丰富的组件, 提供对诸如 SQL Server 和 XML 这样的数据源以及通过 OLE DB 和 ODBC 公开的数据源的一致访问。ADO.NET 类位于 System.Data.dll 中，并与 System.Xml.dll 中的 XML 类集成。  

以前，数据处理主要依赖于基于连接的双层模型。 随着数据处理越来越多地使用多层体系结构，程序员正在向断开方法转换，以便为他们的应用程序提供更好的可伸缩性。  

ADO.NET 用于访问和操作数据的两个主要组件是 .NET Framework 数据提供程序(data providers)和 DataSet。  

**.NET Framework data providers** 是专门为数据操作以及快速、只进、只读访问数据而设计的组件。 data providers包括四个核心对象：    

|对象|说明|
|--|--|
|Connection|建立与特定数据源的连接。|
|Command|对数据源执行命令。 使用 Command 对象可以访问用于返回数据、修改数据、运行存储过程以及发送或检索参数信息的数据库命令。|
|DataReader|从数据源中读取只进且只读的数据流。DataReader 可从数据源提供高性能的数据流。|
|DataAdapter|DataAdapter 在 DataSet 对象和数据源之间起到桥梁作用。 DataAdapter 使用 Command 对象在数据源中执行 SQL 命令以向 DataSet 中加载数据，并将对 DataSet 中数据的更改协调回数据源。|

除了核心类之外，.NET Framework data providers还包含以下类。
+ Transaction  
  将命令登记在数据源处的事务中。 ADO.NET 还使用 System.Transactions 命名空间中的类提供对事务的支持。  
+ CommandBuilder  
  一个帮助器对象，它自动生成 DataAdapter 的命令属性或从存储过程中派生参数信息，并填充 Parameters 对象的 Command 集合。   
+ ConnectionStringBuilder  
  一个帮助器对象，它提供一种用于创建和管理由 Connection 对象使用的连接字符串的内容的简单方法。   
+ Parameter  
  定义命令和存储过程的输入、输出和返回值参数。   

**ADO.NET DataSet** 是专门为独立于任何数据源的数据访问而设计的。 因此，它可以用于多种不同的数据源，用于 XML 数据，或用于管理应用程序本地的数据。DataSet 对象对于支持 ADO.NET 中的断开连接的分布式数据方案起到至关重要的作用。 DataSet 是数据驻留在内存中的表示形式，不管数据源是什么，它都可提供一致的关系编程模型。 DataSet 包含一个或多个 DataTable 对象的集合，这些对象由数据行和数据列以及有关 DataTable 对象中数据的主键、外键、约束和关系信息组成。

DataReader 还是 DataSet?  
当你决定应用程序是应该使用 DataReader还是 DataSet时，请考虑应用程序所需的功能类型。 使用 DataSet 可执行以下操作：

+ 在应用程序中将数据缓存在本地，以便可以对数据进行处理。 如果只需要读取查询结果，则 DataReader 是更好的选择。  
+ 在层间或从 XML Web services 对数据进行远程处理。  
+ 与数据进行动态交互，例如绑定到 Windows 窗体控件或组合并关联来自多个源的数据。
+ 对数据执行大量的处理，而不需要与数据源保持打开的连接，从而将该连接释放给其他客户端使用。

如果不需要 DataSet 所提供的功能，则可以通过使用 DataReader 以只进、只读方式返回数据，从而提高应用程序的性能。 虽然 DataAdapter 使用 DataReader 来填充 DataSet 的内容，但使用 DataReader 可以提升性能，因为这样可以节省 DataSet 所使用的内存，并将省去创建 DataSet 并填充其内容所需的处理。  

## SQL Server数据类型映射 

[MS Link](https://learn.microsoft.com/zh-cn/dotnet/framework/data/adonet/sql-server-data-type-mappings)

## 连接池
连接到数据源可能需要很长时间。 连接到数据库服务器通常由几个需要很长时间的步骤组成。 必须建立物理通道（例如套接字或命名管道），必须与服务器进行初次握手，必须分析连接字符串信息，必须由服务器对连接进行身份验证，必须运行检查以便在当前事务中登记，等等。实际上，大多数应用程序仅使用一个或几个不同的连接配置。 这意味着在执行应用程序期间，许多相同的连接将反复地打开和关闭。  
为了最大程度地降低打开连接的成本，ADO.NET 使用一种称为“连接池”的优化技术，这种技术可最大程度地降低重复打开和关闭连接所造成的成本。  
连接池通过为每个给定的连接配置保留一组活动连接来管理连接。每当用户在连接上调用 Open 时，池进程就会查找池中可用的连接。 如果某个池连接可用，会将该连接返回给调用者，而不是打开新连接。 应用程序在该连接上调用 Close 时，池进程会将连接返回到活动连接池集中，而不是关闭连接。 连接返回到池中之后，即可在下一个 Open 调用中重复使用。    
只有配置相同的连接可以建立池连接。 ADO.NET 会同时保留多个池，每个池对应一种配置。在初次打开连接时，将根据完全匹配算法创建连接池，该算法将池与连接中的连接字符串关联。 每个连接池都与一个不同的连接字符串相关联。 打开新连接时，如果连接字符串并非与现有池完全匹配，将创建一个新池。 按进程、应用程序域、连接字符串以及 Windows 标识（在使用集成的安全性时）来建立池连接。 连接字符串还必须是完全匹配的；按不同顺序为同一连接提供的关键字将分到单独的池中。  


    using (SqlConnection connection = new SqlConnection(  
      "Integrated Security=SSPI;Initial Catalog=Northwind"))  
        {  
            connection.Open();
            // Pool A is created.  
        }  
      
    using (SqlConnection connection = new SqlConnection(  
      "Integrated Security=SSPI;Initial Catalog=pubs"))  
        {  
            connection.Open();
            // Pool B is created because the connection strings differ.  
        }  
      
    using (SqlConnection connection = new SqlConnection(  
      "Integrated Security=SSPI;Initial Catalog=Northwind"))  
        {  
            connection.Open();
            // The connection string matches pool A.  
        }


如果空闲时间达到大约 4-8 分钟，或池进程检测到与服务器的连接已断开，连接池进程会将该连接从池中移除。 注意，只有在尝试与服务器进行通信之后才能检测到断开的连接。 如果发现某连接不再连接到服务器，则会将其标记为无效。 无效连接只有在关闭或重新建立后，才会从连接池中移除。  

# 事务

# 存储过程


# 异步

# Reference
[C# Database Connection: How to connect SQL Server (Example)](https://www.guru99.com/c-sharp-access-database.htm)  
[ADO 和 ADO.NET 之间的差异](https://net-informations.com/faq/ado/ado-difference.htm)  
[ADODB Connection in .NET Application Using C#](https://www.c-sharpcorner.com/UploadFile/9a81a4/adodb-connection-in-net-application-using-C-Sharp/)  
[C# (CSharp) ADODB.Command示例](https://www.cnblogs.com/lothar/p/15781452.html)   
[Asynchronous Programming](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/asynchronous-programming)  