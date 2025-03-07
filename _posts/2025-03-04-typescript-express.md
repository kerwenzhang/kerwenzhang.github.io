---                
layout: post                
title: "Typescript + express"                
date:   2025-3-4 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

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


# Reference

[How to set up TypeScript with Node.js and Express](https://blog.logrocket.com/how-to-set-up-node-typescript-express/)      
[express+typescript](https://blog.csdn.net/longyvfengyun/article/details/139771745)  