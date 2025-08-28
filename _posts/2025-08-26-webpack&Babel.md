---                
layout: post                
title: "使用Webpack和Babel将ES Modules代码转换为CommonJS代码"                
date:   2025-8-26 18:30:00                 
categories: "web"                
catalog: true                
tags:                 
    - web                
---      

在现代的JavaScript开发中，使用ES Modules（ESM）已经成为一种常见的模块化方案。然而，有些情况下，我们可能需要将ES Modules代码转换为CommonJS（CJS）代码，以便在旧版本的Node.js或其他环境中使用。Webpack和Babel是两个非常强大的工具，可以帮助我们实现这个转换过程。

1. 安装依赖

    npm install webpack webpack-cli babel-loader @babel/core @babel/preset-env --save-dev

2. 创建Webpack配置文件  
在项目根目录下创建一个名为webpack.config.js的文件，并添加以下内容  

    module.exports = {
        entry: './src/index.js',
        output: {
            filename: 'bundle.js',
            path: __dirname + '/dist',
        },
        module: {
            rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                loader: 'babel-loader',
                options: {
                    presets: [
                    ['@babel/preset-env', { modules: 'commonjs' }],
                    ],
                },
                },
            },
            ],
        },
    };

在上述配置中，我们指定了入口文件为`src/index.js`，输出文件为`dist/bundle.js`。同时，我们使用了`babel-loader`来处理JavaScript文件，并将`@babel/preset-env`的modules选项设置为`commonjs`，以将ES Modules代码转换为CommonJS代码。

3. 创建Babel配置文件
在项目根目录下创建一个名为.babelrc的文件，并添加以下内容：  

    {
        "presets": [
            ["@babel/preset-env", { "modules": false }]
        ]
    }

在上述配置中，我们将@babel/preset-env的modules选项设置为false，以确保Babel不会对ES Modules进行转换。  

4. 在src目录下，创建add.js

    export const add = (a,b) => {
        return a + b;
    }

5. 在src目录下，创建index.js

    import { add } from './add'

    console.log(add(1,2)); 

  注意我们用的是ESModule语法import，而不是require

6. 在package.json中添加新的命令行：

    "build": "webpack"

7. 运行命令行npm run build，生成dist/bundle.js  


# Reference
使用Webpack和Babel将ES Modules代码转换为CommonJS代码的配置）](https://juejin.cn/post/7280436213886779433)