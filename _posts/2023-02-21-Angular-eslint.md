---
layout: post
title: 从tslint迁移到Angular-eslint
date:   2023-02-21 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

1. 安装eslint依赖，运行以下命令：

    ng add @angular-eslint/schematics@14

运行结果：

在root自动生成.eslintrc.json文件，默认使用@angular-eslinteslint插件。    
以下eslint相关的cli配置被添加至angular.json，  

    "cli": {
        "defaultCollection": "@angular-eslint/schematics"
    }

2. Run the convert-tslint-to-eslint schematic on a project
If you just have a single project in your workspace you can just run:

    ng g @angular-eslint/schematics:convert-tslint-to-eslint

The schematic will do the following for you:

Read your chosen project's tslint.json and use it to CREATE a .eslintrc.json at the root of the specific project which extends from the root config (if you do not already have a root config, it will also add one automatically for you).
The contents of this .eslintrc.json will be the closest possible equivalent to your tslint.json that the tooling can figure out.
You will want to pay close attention to the terminal output of the schematic as it runs, because it will let you know if it couldn't find an appropriate converter for a TSLint rule, or if it has installed any additional ESLint plugins to help you match up your new setup with your old one.
UPDATE the project's architect configuration in the angular.json to such that the lint "target" will invoke ESLint instead of TSLint.
UPDATE any instances of tslint:disable comments that are located within your TypeScript source files to their ESLint equivalent.
If you choose YES (the default) for the --remove-tslint-if-no-more-tslint-targets option, it will also automatically remove TSLint and Codelyzer from your workspace if you have no more usage of them left.

3. "@typescript-eslint/naming-convention": "off"

4. 检验是否可以使用

运行lint命令

    ng lint

5. ng lint --fix

6. 安装eslint插件


# Reference
[Angular ESLint](https://github.com/angular-eslint/angular-eslint#migrating-an-angular-cli-project-from-codelyzer-and-tslint)  
[Angular中迁移tslint至eslint的过程是怎样的呢](https://www.qycn.com/xzx/article/14457.html)  