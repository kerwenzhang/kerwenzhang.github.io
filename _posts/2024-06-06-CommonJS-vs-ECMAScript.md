---                
layout: post                
title: "CommonJS vs ECMAScript"                
date:   2024-6-6 20:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

# CommonJs
CommonJS(简称cjs)，为node.js打包javaScript的原始方法，使用require和imports（module.exports）语句定义模块  
在node.js中，每个文件都被视为一个单独的模块。模块的局部变量是私有的，只有exports出去的变量，才能被外界访问。  

默认情况下，node.js会将以下情形视为 cjs模块:  

+ 扩展名为.cjs的文件；
+ 扩展名为.js的文件，且离自己最近的package.json文件包含一个顶级字段“type”，其值为“commonjs”；
+ <font color="red">扩展名为.js的文件，且离自己最近的package.json文件不包含一个顶级字段“type”</font>(建议明确指定 type值，而不是不定义)；
+ 扩展名不为.mjs, .cjs, .json, .node, .js的文件，且离自己最近的package.json文件包含一个顶级字段“type”，其值为“module”，但是这些文件通过require引入。
# ESMAScript
ECMAScript模块(简称esm)，是ecma262标准下封装的JavaScript代码重用的官方标准格式。使用import和export语句定义模块  

默认情况下，node.js会将以下情形视为 esm 模块:

+ 扩展名为 .mjs 的文件；
+ 扩展名为.js的文件，且离自己最近的package.json文件包含一个顶级字段“type”，其值为“module”；

# 两者不同
-cjs只有在node.js环境使用。  
-esm在node.js和浏览器环境都可以使用  

+ esm使用import/export， 而cjs使用require/exports
+ cjs可以使用 __filename 或者 __dirname，process, 而esm不行，esm只能使用 import.meta.url
+ esm不支持本机模块。 但是可以改为通过 module.createRequire() or process.dlopen.加载
+ cjs使用 require.resolve， 而esm使用new URL(), import.meta.resolve
+ cjs可以通过环境变量指定的路径，去查找本机上对应位置的模块，而esm不行，
+ cjs 是在运行时确定，而esm则在静态编译时确定。
+ cjs可以同步执行，esm不行

# Reference
[CommonJS模块和ECMAScript模块](https://www.cnblogs.com/withheart/p/17861005.html)  
[CommonJS 与 Node.js 中的 ES 模块](https://blog.logrocket.com/commonjs-vs-es-modules-node-js/)  