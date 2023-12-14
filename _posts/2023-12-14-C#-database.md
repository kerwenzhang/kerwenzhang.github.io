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

# Reference
[C# Database Connection: How to connect SQL Server (Example)](https://www.guru99.com/c-sharp-access-database.htm)  