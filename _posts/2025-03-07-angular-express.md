---                
layout: post                
title: "Host Angular with express"                
date:   2025-3-7 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

# 创建一个Angular工程

    ng new client

# 创建一个express工程

    mkdir server
    cd server
    npm init

安装必要的依赖

    npm install express typescript ts-node @types/node @types/express --save-dev

+ `Express`：适用于 Node.js 的极简且灵活的 Web 应用程序框架。
+ `TypeScript`：JavaScript 的超集，添加了静态类型和高级语言功能。
+ `ts-node`：适用于 Node.js 的 TypeScript 执行环境。
+ `@types/express`：适用于 Express 的 TypeScript 声明文件。

在server根目录下创建一个`tsconfig.json`文件, 配置TypeScript  

    {
        "compilerOptions": {
            "target": "es6",
            "module": "commonjs",
            "outDir": "./dist",
            "strict": true,
            "esModuleInterop": true,
            "skipLibCheck": true,
            "forceConsistentCasingInFileNames": true
        },
        "include": ["src/**/*.ts"],
        "exclude": ["node_modules"]
    }

此配置指定 TypeScript 编译器的输出目录、模块系统和其他选项。  

创建src目录，在src下创建index.ts文件  

    import express from 'express';

    const app = express();
    const port = 3000;

    app.get('/hello', (req, res) => {
        res.send('Hello World!');
    });

    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
    });

修改package.json，添加编译脚本

    "scripts": {
        "start": "ts-node src/index.ts",
        "build": "tsc",
        "serve": "node dist/index.js"
    }

# Host Angular project
为了使用 express 为 Angular 应用程序提供服务，我们将使用 express 的static功能来提供静态文件。以下代码应位于任何 app.get 或类似代码之前。

    // Uses the static content located in client
    app.use(express.static('../client/dist/client/browser', {}));

在所有已定义request请求之后加一个*用来实现捕获其余文件请求。

    app.use('*', (req, res) => {
        res.sendFile('index.html', { root: '../client/dist/client/browser' });
    });

整个index.ts文件如下  

    import express from 'express';

    const app = express();
    const port = 3000;
    app.use(express.static(`${__dirname}/../../client/dist/client/browser`));

    app.get('/hello', (req, res) => {
        res.send('Hello World!');
    });

    app.use('*', (req, res) => {
        res.sendFile('index.html', { root: '../client/dist/client/browser' });
    });

    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
    });

用命令行ng build编译client，之后在server目录下运行`npm run start`  

# Reference

[Hosting an Angular application with express](https://medium.com/medialesson/hosting-an-angular-application-with-express-31237756722f)      
[Build a Simple Web App with Express & Angular](https://www.geeksforgeeks.org/build-a-simple-web-app-with-express-angular/)    
[Deploy angular app in node server — express static](https://sidhu-dreamer.medium.com/deploy-angular-app-in-node-server-express-static-rest-api-method-in-the-same-port-2c8b5a39ebce)  