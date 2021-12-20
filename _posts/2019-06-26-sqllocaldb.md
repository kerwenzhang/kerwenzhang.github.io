---                
layout: post                
title: "SQLLocalDB 命令行"                
date:   2019-6-26 10:30:00                 
categories: ".Net Core"                
catalog: true                
tags:                 
    - .Net Core                
---      

SqlLocalDB i                        //列出所有LocalDB实例  
SqlLocalDB create "MyDatabase"    //创建“Mydatabase数据库”，说明：创建后还没有启动数据库

SqlLocalDb info "MyDatabase"        //显示MyDatabase数据库信息

SqlLocalDB start "MyDatabase"      //启动MyDatabase数据库

SqlLocalDB stop "MyDatabase"      //停止MyDatabase数据库

SqlLocalDB delete "MyDatabase   //删除MyDatabase数据库