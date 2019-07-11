---                
layout: post                
title: "VS Code中配置保存*.ts文件自动编译成*.js文件"                
date:   2019-7-10 15:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

1. 使用下边的命令全局安装typescript （如已安装请忽略）

    npm i -g typescript 

2. 使用cd到达你指定的项目下，使用下列命令进行初始化，创建tsconfig.json文件

    tsc -init

”target” : 编译为何种规范，一般设置为 ES5 或者 ES2016/2017
“outdir” : 输出目录
“alwaysStrict” ： 打开严格模式 (‘use strict’)

3. 打开tsconfig.json文件修改和删除相应配置（如果想快速修改配置，请复制下列配置）

    {
        "compilerOptions": {
        "target": "es5",
        "noImplicitAny": false,
        "module": "amd",
        "removeComments": false,
        "sourceMap": false,
        "outDir": "build"//你要生成js的目录,可自由命名
        }
    }

4.  当编写好一个ts文件的时候，按下 Ctrl+shift+B 快捷键会进行编译，初次编译会选择编译模式（自行编写.ts文件测试），选择监视模式，这样就会自动生成一个对应的js文件。