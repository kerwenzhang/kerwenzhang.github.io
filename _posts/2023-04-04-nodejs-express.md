---
layout: post
title: nodejs express
date:   2023-04-04 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

# Express基础
新建一个文件夹demo

## 初始化项目

    npm init --yes

## npm安装EXPRESS

    npm install express --save

## 创建项目app.js

    const http = require("http");
    const express= require("express");      //Express框架
    let app=express();                      //app全称application，它是一个网站程序
    let server = http.createServer(app);    //通过http模块创建了一个服务器server


## 监听端口

    //服务器是要运行在某一个端口上面
    server.listen(8888,()=>{
        console.log("服务器启动成功");
    });

## 启动程序
package.json

    {
        "name": "expressdemo01",
        "version": "1.0.0",
        "main": "app.js",
        "license": "MIT",
        "author": "张三",
        "scripts": {
            "start": "node app.js"
        },
        "dependencies": {
            "express": "^4.16.4"
        }
    }

在控制台执行:

    npm run start


# 处理请求

## 处理get请求

    app.get("/",(req,resp)=>{
        resp.send("Hello, this is message get from server!");
    });

    app.get("/def",(req,resp)=>{
        resp.send("Get request from /def");
    })

浏览器访问`http://localhost:8888`和`http://localhost:8888/def`


## VSCode
点击VSCode侧边栏上的Run and Debug, 创建一个新的launch.json, 选择nodejs，保持默认设置

    {
        "version": "0.2.0",
        "configurations": [
            {
                "type": "node",
                "request": "launch",
                "name": "Launch Program",
                "skipFiles": [
                    "<node_internals>/**"
                ],
                "program": "${workspaceFolder}\\app.js"
            }
        ]
    }

点击 Start Debug(F5)

# 模块化编程
## 独立的js文件
创建新的`add.js`

    exports.add = function(a, b){
        return (a+b);
    }

app.js中引入这个模块

    const addObj = require('./add.js');
    const url = require("url");

    app.get("/calculate/add",(req, resp)=> {
        var params = url.parse(req.url, true).query;
        resp.send("result: "+ addObj.add(parseInt(params.a), parseInt(params.b)));
    })

输入url：  
http://localhost:8888/calculate/add?a=1&b=2

## 独立模块
创建新的`sub.js`

    function factory(){
        this.sub = function(a,b){
            return (a-b);
        }
    };

    module.exports = factory;

`app.js`中引入这个模块

    const Sub = require('./sub.js');
    subIns = new Sub();

    app.get("/calculate/sub",(req, resp)=> {
        var params = url.parse(req.url, true).query;
        resp.send("result: "+ subIns.sub(parseInt(params.a), parseInt(params.b)));
    })

## 发布包
创建独立的模块： 
和demo同级新建一个文件夹mult， 初始化项目

    npm init --yes

修改package.json中的name: kerwen_mult  
新建index.js  

    function factory(){
        this.mul = function(a,b){
            return (a*b);
        }
    };

    module.exports = factory;

新建一个readme.md  
访问 [npm官网](https://www.npmjs.com/) 网站注册一个账号  
在mult下运行命令`npm adduser`登录刚才创建的npm账号  
用`npm publish`发布包  
发布成功之后在npm官网能搜索到自己刚刚创建的包
回到demo工程，安装自己刚才发布的包

    npm install kerwen_mult

在app.js中引用：  

    const mul=require('kerwen_mult');
    mulIns = new mul();

    app.get("/calculate/mul",(req, resp)=> {
        var params = url.parse(req.url, true).query;
        resp.send("result: "+ mulIns.mul(parseInt(params.a), parseInt(params.b)));
    })

在网页中输入`http://localhost:8888/calculate/mul?a=2&b=3`


