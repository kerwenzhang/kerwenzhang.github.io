---                
layout: post                
title: "TypeScript"                
date:   2019-7-4 20:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

## 介绍

TypeScript 是 JavaScript 的一个超集，扩展了 JavaScript 的语法，是由微软开发的自由和开源的编程语言。

## 安装

        npm install -g typescript
安装完成后我们可以使用 tsc -v 来查看版本号

        $ tsc -v
        Version 3.2.2
## Hello world

        var message:string="Hello World“
        console.log(message)
通常使用`.ts`作为TypeScript代码文件的扩展名.

## 转换成Jayavscript

        tsc test.ts

## 面向对象编程

        class Site{
          name():void{
            console.log("hello")
          }
        }
        var obj = new Site();
        obj.name();

## 数据类型

#### 任意类型 any
        let x:any =1;
        x='This is string'
#### 数字类型 number
        let decLiteral: number = 6;
#### 字符串类型 string
        let name: string = "Runoob";
        let years: number = 5;
        let words: string = `您好，今年是 ${ name } 发布 ${ years + 1} 周年`;
#### 布尔类型 boolean
        let flag: boolean = true;
#### 数组类型
        let arr: number[] = [1, 2];
#### 枚举 enum
        enum color{red,green,blue}
        let c : Color = Color.blue;
        console.log(c)
## 变量声明
        var [变量名] : [类型] = 值;
## 语句
### 条件语句
If 语句

        var num:number = 2 
        if(num > 0) { 
          console.log(num+" 是正数") 
        } else if(num < 0) { 
          console.log(num+" 是负数") 
        } else { 
          console.log(num+" 不是正数也不是负数") 
        }
Switch 语句

        var grade:string = "A"; 
          switch(grade) { 
          case "A": { 
            console.log("优"); 
            break; 
          } 
          default: { 
            console.log("非法输入"); 
            break;              
          } 
        }
### 循环
for 循环

        var num = 5;
        var i;
        var factorial = 1;
        for (i = num; i >= 1; i--) {
          factorial *= i;
        }
        console.log(factorial);
for...in 循环

        var j:any; 
        var n:any = "a b c" 
        
        for(j in n) {
          console.log(n[j])  
        }
while 循环
## 函数
        function add(x: number, y: number): number {
          return x + y;
        }
        console.log(add(1,2))
可选参数

        function buildName(firstName: string, lastName?: string) {
        if (lastName)
                return firstName + " " + lastName;
        else
                return firstName;
        }
        
        let result1 = buildName("Bob");  // 正确
默认参数

        function calculate(price:number,rate:number = 0.50) { 
          var discount = price * rate; 
          console.log("计算结果: ",discount); 
        } 
        calculate(1000) 
## 类
    class Car {     
      engine:string;  
      // 构造函数 
      constructor(engine:string) { 
        this.engine = engine 
      }   
      // 方法 
      disp():void { 
        console.log("发动机为 :   "+this.engine) 
      } 
    }
    var obj = new Car("Engine 1")
## 对象
对象是包含一组键值对的实例。 值可以是标量、函数、数组、对象等.

        var sites = { 
          site1:"Runoob", 
          site2:"Google" 
        }; 
        // 访问对象的值
        console.log(sites.site1) 
类型模板

        var sites = {
          site1: "Runoob",
          site2: "Google",
          sayHello: function () { } // 类型模板
        };
        sites.sayHello = function () {
          console.log("hello " + sites.site1);
        };
        sites.sayHello();