---                
layout: post                
title: "TypeScript 学习"                
date:   2020-7-17 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

[https://ts.xcatliu.com/](https://ts.xcatliu.com/)

TypeScript 是 JavaScript 的一个超集，主要提供了类型系统和对 ES6 的支持，它由 Microsoft 开发，代码开源于 GitHub 上。  

### 安装

    npm install -g typescript

以上命令会在全局环境下安装 tsc 命令，安装完成之后，我们就可以在任何地方执行 tsc 命令了。  
约定使用 TypeScript 编写的文件以 .ts 为后缀，用 TypeScript 编写 React 时，以 .tsx 为后缀。  

    function sayHello(person: string) {
        return 'Hello, ' + person;
    }
    let user = 'Tom';
    console.log(sayHello(user));

    // 编译
    tsc hello.ts

### 数据类型
1. 基本数据类型

        let isDone: boolean = false;    //布尔值
        let decLiteral: number = 6;     //数值
        let myName: string = 'Tom';     //字符串
        // 模板字符串
        let sentence: string = `Hello, my name is ${myName}.`;

2. 空值  
    JavaScript 没有空值（Void）的概念，在 TypeScript 中，可以用 void 表示没有任何返回值的函数：  

        function alertName(): void {
            alert('My name is Tom');
        }

3. 任意值  
如果是一个普通类型，在赋值过程中改变类型是不被允许的, 但如果是 any 类型，则允许被赋值为任意类型。    

        let myFavoriteNumber: any = 'seven';
        myFavoriteNumber = 7;

变量如果在声明的时候，未指定其类型，那么它会被识别为任意值类型：  

4. 数组  

        let fibonacci: number[] = [1, 1, 2, 3, 5];
        // 用 any 表示数组中允许出现任意类型：
        let list: any[] = ['xcatliu', 25, { website: 'http://xcatliu.com' }];

5. 函数  
一个函数有输入和输出，要在 TypeScript 中对其进行约束，需要把输入和输出都考虑到，其中函数声明的类型定义较简单：  

        function sum(x: number, y: number): number {
            return x + y;
        }

用`?`表示可选参数：  

        function buildName(firstName: string, lastName?: string) {
            if (lastName) {
                return firstName + ' ' + lastName;
            } else {
                return firstName;
            }
        }
        let tom = buildName('Tom');

需要注意的是，可选参数必须接在必需参数后面。换句话说，可选参数后面不允许再出现必需参数.  
参数默认值:  

        function buildName(firstName: string, lastName: string = 'Cat') {
            return firstName + ' ' + lastName;
        }
        let tom = buildName('Tom');

### 元组
数组合并了相同类型的对象，而元组（Tuple）合并了不同类型的对象。    
定义一对值分别为 string 和 number 的元组：   

    let tom: [string, number] = ['Tom', 25];    

### 枚举
枚举（Enum）类型用于取值被限定在一定范围内的场景，比如一周只能有七天，颜色限定为红绿蓝等。  

    enum Days {Sun, Mon, Tue, Wed, Thu, Fri, Sat};

    console.log(Days["Sun"] === 0); // true
    console.log(Days["Mon"] === 1); // true
    console.log(Days["Tue"] === 2); // true
    console.log(Days["Sat"] === 6); // true

