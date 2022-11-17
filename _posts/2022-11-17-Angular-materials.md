---
layout: post
title: Angular Material
date:   2022-11-17 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

Angular Material是Angular JS开发人员的UI组件库。  
# 安装
在使用Material之前，建议安装最新的nodejs，安装最新的Angular，否则你可能会遇到因为版本不匹配造成的各种不兼容问题。

    npm install -g @angular/cli 

Material： 

    ng add @angular/material@latest

会有一些命令提示，按默认  
运行工程`ng serve --open`, 如果遇到以下error

    An unhandled exception occurred: ENOENT: no such file or directory, lstat '...\@angular'

Ctrl + C结束编译，修改`Angular.json`文件。但更建议把环境都升到最新，升到最新之后这个问题就消失了。  

    "styles": [
        "./node_modules/@angular/material/prebuilt-themes/indigo-pink.css",
        "src/styles.scss"
    ],

在`app.module.ts`里引入material模块  

    import { MatSlideToggleModule } from '@angular/material/slide-toggle';

    @NgModule ({
        imports: [
            MatSlideToggleModule,
        ]
    })

修改app.component.html  

    <mat-slide-toggle>Toggle me!</mat-slide-toggle>

# Reference
[Angular Material API](https://material.angular.cn/components/categories)
