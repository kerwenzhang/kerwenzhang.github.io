---                
layout: post                
title: "TypeScript"                
date:   2024-5-29 20:30:00                 
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

#### 元组
数组合并了相同类型的对象，而元组（Tuple）合并了不同类型的对象。    
定义一对值分别为 string 和 number 的元组：   

        let tom: [string, number] = ['Tom', 25];   

#### 枚举 enum

        enum color{red,green,blue}
        let c : Color = Color.blue;
        console.log(c)

#### 空值  
JavaScript 没有空值（Void）的概念，在 TypeScript 中，可以用 void 表示没有任何返回值的函数：  

        function alertName(): void {
            alert('My name is Tom');
        }

#### Null 和 Undefined
在 TypeScript 中，可以使用 `null` 和 `undefined` 来定义这两个原始数据类型：

        let u: undefined = undefined;
        let n: null = null;

与 `void` 的区别是，`undefined` 和 `null` 是所有类型的子类型。也就是说 `undefined` 类型的变量，可以赋值给 `number` 类型的变量：

        // 这样不会报错
        let num: number = undefined;
        // 这样也不会报错
        let u: undefined;
        let num: number = u;

而 `void` 类型的变量不能赋值给 `number` 类型的变量：

        let u: void;
        let num: number = u;

        // Type 'void' is not assignable to type 'number'.

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

        var num:number = 5; 
        var factorial:number = 1; 
        
        while(num >=1) { 
          factorial = factorial * num; 
          num--; 
        } 
        console.log("5 的阶乘为："+factorial);

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

需要注意的是，可选参数必须接在必需参数后面。换句话说，可选参数后面不允许再出现必需参数.   

默认参数

        function calculate(price:number, rate:number = 0.50) { 
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
        
## 模块

项目中可以将代码拆分为多个文件，多个文件可以互相加载，并通过export和import关键字完成模块功能的交换。 模块是在其自身的作用域里执行，并不是在全局作用域，这意味着定义在模块里面的变量、函数和类等在模块外部是不可见的，除非明确地使用 export 导出它们。类似地，我们必须通过 import 导入其他模块导出的变量、函数、类等。


        export class Mail {
                title:string;
                content:string;

                constructor(title:string,content:string){
                        this.title = title;
                        this.content = content;
                }
        }

        import {Mail} from './Mail';
        let mail = new Mail('邮箱标题','邮箱内容');
        mail.content;