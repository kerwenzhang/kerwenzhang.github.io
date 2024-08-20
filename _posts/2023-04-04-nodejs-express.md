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


## nodemon
nodemon 能够监听项目文件变动，当代码被修改后， nodemon会自动帮我们重启项目，极大方便了开发和调试

安装：  

    npm install -g nodemon

使用：  
将启动命令修改为  

    nodemon app.js

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

# 路由  
在Express中，路由指的是客户端的请求与服务器处理函数之间的映射关系。
Express中的路由分3部分组成，分别是请求的类型、请求的UR地址、处理函数。  

    app.METHOD(PATH, HANDLER)

例子：  

    //匹配GET请求，且请求URL为 /
    app.get('/', function(req ,res) => {
        res.send('Hello World!')
    })

    //匹配POST请求，且请求URL为 /
    app.post('/', function(req, res) {
        res.send('Got a POST request')
    })

在Express中使用路由最简单的方式，就是把路由挂载到app上  

    const express = require('express')
    //创建Web服务器，命名为app
    const app = express()

    //挂载路由
    app.get('/', (req, res) => { res.send('Hello World!')})
    app.post('/', (req, res) => { res.send('Post Request')})

    //启动Web服务器‘
    app.listen(80, () => { console.log('server running at http://127.0.0.1')})

## 模块化路由
为了方便对路由进行模块化管理， Express不建议将路由直接挂在到app上，而是推荐将路由抽离为单独的模块。  
创建路由模块  

    var express = require('express')  //导入express
    var router = express.Router  //创建路由对象

    //挂载获取用户列表的路由
    router.get('/user/list', function(req, res) => {
        res.send('Get user list.')
    })
    //挂载添加用户的路由
    router.post('/user/add', function(req, res) => {
        res.send('Add new user.')
    })

    //向外导出路由对象
    module.exports =router

注册路由模块  

    const userRouter = require('./router/user.js')
    //使用app.use()注册路由模块
    app.use(userRouter)

## 为路由模块添加前缀
类似于托管静态资源时，为静态资源统一挂载访问前缀一样，路由模块添加前缀的方式也非常简单  

    const userRouter = require('./router/user.js')
    //使用app.use()注册路由模块，并添加统一的访问前缀 /api
    app.use('/api', userRouter)



# 静态文件  
为了提供诸如图像、CSS 文件和 JavaScript 文件之类的静态文件，请使用 Express 中的 `express.static` 内置中间件函数。

此函数特征如下：

    express.static(root, [options])

例如，通过如下代码就可以将 public 目录下的图片、CSS 文件、JavaScript 文件对外开放访问了：  

    app.use(express.static('public'))

现在，你就可以访问 public 目录中的所有文件了  
如果要使用多个静态资源目录，请多次调用 express.static 中间件函数：  

    app.use(express.static('public'))
    app.use(express.static('files'))

要为 express.static 函数提供的文件创建虚拟路径前缀（其中路径实际上并不存在于文件系统中），请为静态目录指定挂载路径，如下所示：  

    app.use('/static', express.static('public'))

现在，你就可以通过带有 /static 前缀地址来访问 public 目录中的文件了。

    http://localhost:3000/static/images/kitten.jpg
    http://localhost:3000/static/css/style.css  

提供给 express.static 函数的路径是相对于node进程的目录的。如果从另一个目录运行 express 应用程序，则使用要提供服务的目录的绝对路径更安全：  

    const path = require('path')
    app.use('/static', express.static(path.join(__dirname, 'public')))

# 中间件
中间件（Middleware），特指业务流程的中间处理环节。当一个请求到达Express服务器之后，可以连续调用多个中间件，从而对这次请求进行预处理。   
Express的中间件，本质上就是一个function处理函数， 一个最简单的中间件函数如下：  

    //常量mw所指向的就是一个中间件函数
    const mv = function(req, res, next) {
        console.log('这是一个最简单的中间件函数')
        //在当前中间件的业务处理完毕后，必须调用next()函数
        //表示把流转关系转交给下一个中间件或路由
        next()
    }

## 全局生效的中间件  
客户端发起的任何请求到达服务器之后，都会触发的中间件，叫做全局生效的中间件。  

通过调用app.use(中间件函数)，即可定义一个全局生效的中间件。

    //常量mv所指向的就是中间件函数
    const mv = function(req, res next) {
        console.log('这是一个最简单的中间件函数')
        next()
    }

    //全局生效的中间件
    app.use(mv)

定义多个全局中间件  
可以使用app.use()连续定义多个全局中间件，客户端请求到达服务器之后，会按照中间件定义的先后顺序依次进行调用。  


    //第一个全局中间件
    app.use(function(req, res, next) {
        console.log('调用了第一个全局中间件')
        next()
    })

    //第二个全局中间件
    app.use(function(req, res, next) {
        console.log('调用了第二个全局中间件')
        next()
    })

    //请求这个路由，会依次触发上述两个全局中间件
    app.get('/user', (req, res) => {
        res.send('Home.page.')
    })

## 局部生效的中间件
不使用app.use()定义的中间件，叫做局部生效的中间件。  

    //定义中间件函数 mv1
    const mv1 = function(req, res, next) {
        console.log('这是中间件函数')
        next()
    }

    //mv1这个中间件只在"当前路由中生效"，这种用法属于"局部生效的中间件"
    app.get('/', mv1, function(req, res) {
        res.send('Home.page.')
    })

    //mv1这个中间件不会影响下面这个路由
    app.get('/user', function(req, res) { res.send('User page.') })

定义多个局部中间件  
可以在路由中通过如下两种等价的方式，使用多个局部中间件

    app.get('/', mv1, mv2, (req, res) => { res.send('Home.page.') })
    app.get('/', [mv1, mv2], (req, res) => { res.send('Home.page') })

中间件注意事项：
+ 一定要在路由之前注册中间件
+ 执行完中间件的业务代码之后，不要忘记调用next()函数
+ 调用next()函数后不要再写额外的代码
+ 连续调用多个中间件时，多个中间件之间，共享req和res对象  

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

# Swagger
Swagger是一种规范，用于描述API的结构，功能和参数。它是一种开源工具，可通过该工具生成API文档，用于开发和测试。使用Swagger可以提供清晰的可视化API文档，可用于API交互的文档驱动开发，以及API的自动化测试和集成。Swagger已经成为API设计和开发中的必备工具。  

在Express中使用Swagger，需要以下步骤：  

安装Swagger

    npm install swagger-jsdoc swagger-ui-express --save



## 配置Swagger

    const express = require('express');
    const swaggerJsdoc = require('swagger-jsdoc');
    const swaggerUi = require('swagger-ui-express');

    const app = express();

    const options = {
        definition: {
            openapi: '3.0.0',
            info: {
                title: 'My API',
                version: '1.0.0'
            }
        },
        apis: ['./routes/*.js']
    };

    const swaggerSpec = swaggerJsdoc(options);

    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

其中，`options-definition`字段用于定义Swagger规范，`apis`字段用于指定使用Swagger规范的API文件路径，指定 swagger-jsdoc 去哪个路由下收集 swagger 注释  

## 创建路由
在根目录下创建routes文件夹，新建router.js, 添加路由信息

    const express = require('express');
    var router = express.Router();

    router.get('/users', (req, res) => {
        res.status(200).json({data: [{name: 'Tom', age: 20}, {name: 'Lucy', age: 22}]});
    });

    router.post('/users', (req, res) => {
        res.status(200).json({success: true});
    });

    module.exports = router;

## 添加Swagger说明
在router.js中定义Swagger  
具体可以参考[Swagger官网规范说明](https://swagger.io/specification/)或使用[Swagger Editor](https://editor.swagger.io/)进行编写。

    /**
    * @swagger
    * /api/users:
    *  get:
    *    summary: 获取所有用户信息
    *    responses:
    *      200:
    *        description: 成功获取所有用户信息
    * 
    *  post:
    *    summary: 创建用户
    *    parameters:
    *      - in: body
    *        name: user
    *        schema:
    *          type: object
    *          properties:
    *            name:
    *              type: string
    *            age:
    *              type: integer
    *    responses:
    *      200:
    *        description: 成功创建用户
    */

## 使用路由
在index.js中引用路由，并添加`/api`前缀  

    const router = require('./routes/router.js');
    app.use('/api',router);


## 返回json
在index.js中添加以下语句，返回json规范的swagger

    // 开放 swagger 相关接口，
    app.get('/swagger.json', function(req, res) {
        res.setHeader('Content-Type', 'application/json');
        res.send(swaggerSpec);
    });

## 封装
可以将所有swagger的配置从index.js中挪出来，单独放一个文件, 新建一个文件夹swagger，在该目录下创建config.js。将所有swagger相关配置都挪进去:

    const swaggerJsdoc = require('swagger-jsdoc');
    const swaggerUi = require('swagger-ui-express');

    exports.setSwagger = function(app) {
        const options = {
            definition:{
                openapi:'3.0.0',
                info:{
                    title:'My API',
                    version: '1.0.0'
                }
            },
            apis:['./routes/*.js']
        };

        const swaggerSpec = swaggerJsdoc(options);

        // 开放 swagger 相关接口，
        app.get('/swagger.json', function(req, res) {
            res.setHeader('Content-Type', 'application/json');
            res.send(swaggerSpec);
        });
        app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
    }

修改index.js

    const swagger = require('./swagger/config.js');
    swagger.setSwagger(app);



# Reference  
[node.js中express框架的使用](https://blog.csdn.net/weixin_54418006/article/details/123584850)  
[在Express中使用Swagger](https://www.cnblogs.com/biem/p/17426229.html)