---                                  
layout: post                                  
title: "JavaScript 总结"                                  
date:   2020-07-11 9:00:00                                   
categories: "Web"                                  
catalog: true                                  
tags:                                   
    - Web                                  
---                        
    
[HTML](https://blog.csdn.net/wuyxinu/article/details/103515157)      
[CSS](https://blog.csdn.net/wuyxinu/article/details/103583618)    
[JS](https://blog.csdn.net/wuyxinu/article/details/103642800)    
[JS-下](https://blog.csdn.net/wuyxinu/article/details/103646041)   
[jQuery](https://blog.csdn.net/wuyxinu/article/details/103669718)   
[Node.js + Gulp](https://blog.csdn.net/wuyxinu/article/details/103774211)   

HTML是网页的结构，CSS是网页的外观，而JavaScript是页面的行为。  

### 数据类型
JavaScript数据类型有2大分类：一是“基本数据类型”，二是“特殊数据类型”。

其中，基本数据类型包括以下3种： 

（1）数字型（Number型）：如整型84，浮点型3.14；  
（2）字符串型（String型）：如"绿叶学习网"；  
（3）布尔型（Boolean型）：true或fasle；  

特殊数据类型有3种：

（1）空值（null型）；  
（2）未定义值（undefined型）；  
（3）转义字符；  

### typeof运算符
ypeof运算符用于返回它的操作数当前所容纳的数据的类型，这对于判断一个变量是否已被定义特别有用。

例如：typeof(1)返回值是number，typeof("javascript")返回值是string。  

### 类型转换

1. 字符串型转换为数值型    

    parseInt()  //将字符串型转换为整型
    parseFloat()  //将字符串型转换为浮点型

2. 数值型转换为字符串型
    	
    .toString()

### 函数
在JavaScript中，使用函数前，必须用function关键字来定义函数。

### 字符串对象
1. length属性  
我们可以通过length属性来获取字符串的长度。  

    字符串名.length

2. match()  
使用match()方法可以从字符串内索引指定的值，或者找到一个或多个正则表达式的匹配。  

    stringObject.match(字符串)    //匹配字符串;
    stringObject.match(正则表达式)  //匹配正则表达式

3. indexOf()  
使用indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。   

    stringObject.indexOf(字符串)

4. replace()  
replace()方法常常用于在字符串中用一些字符替换另一些字符，或者替换一个与正则表达式匹配的子串。  

    stringObject.replace(原字符,替换字符)   
    stringObject.replace(正则表达式,替换字符)  //匹配正则表达式

5. charAt()  
使用charAt()方法来获取字符串中的某一个字符  

    stringObject.charAt(n)

6. 连接字符串  
使用concat()方法来连接2个或多个字符串。  

    字符串1.concat(字符串2,字符串3,…,字符串n);

7. split()  
使用split()方法把一个字符串分割成字符串数组。  

    字符串.split(分割符)

8. substring()  
使用substring()方法来提取字符串中的某一部分字符串。  

    字符串.substring(开始位置,结束位置)

### 日期对象
