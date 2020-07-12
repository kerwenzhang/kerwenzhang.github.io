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
创建日期对象必须使用“new语句”。  

    var 日期对象名 = new Date();
    var 日期对象名 = new Date(日期字符串);

常用方法:  

    getFullYear()	//返回一个表示年份的4位数字
    getMonth()	//返回值是0（一月）到11（十二月）之间的一个整数
    getDate()	//返回值是1~31之间的一个整数
    getHours()	//返回值是0~23之间的一个整数，来表示小时数
    getMinutes()	//返回值是0~59之间的一个整数，来表示分钟数
    getSeconds()	//返回值是0~59之间的一个整数，来表示秒数
    
将日期时间转换为字符串:  

    toString()	//将日期时间转换为普通字符串
    toUTCString()	//将日期时间转换为世界时间（UTC）格式的字符串
    toLocaleString()	//将日期时间转换为本地时间格式的字符串

### 数组对象
#### 创建数组
在JavaScript中，创建数组共有3种方法：  

    var myArr = new Array();

    var myArr = new Array(3);
    myArr[0]="HTML";
    myArr[1]="CSS";
    myArr[2]="JavaScript";

    var myArr = new Array(1,2,3,4);

#### 常用方法

    slice()	//获取数组中的某段数组元素
    push()	//在数组末尾添加元素
    pop()	//删除数组最后一个元素
    toString()	//将数组转换为字符串
    join()	//将数组元素连接成字符串
    concat()	//多个数组连接为字符串
    sort()	//数组元素正向排序
    reverse()	//数组元素反向排序
    
### 数值对象

    max(x,y)	//返回x和y中的最大值
    min(x,y)	//返回x和y中的最小值
    pow(x,y)	//返回x的y次幂
    abs(x)	//返回数的绝对值
    round(x)	//把数四舍五入为最接近的整数
    random()	//返回0~1之间的随机数
    ceil(x)	//对一个数进行上舍入
    floor(x)	//对一个数进行下舍入

### 窗口对象
在JavaScript中，一个浏览器窗口就是一个window对象。window对象主要用来控制由窗口弹出的对话框、打开窗口或关闭窗口、控制窗口的大小和位置等等。  

1. 打开窗口   

        window.open(URL, 窗口名称, 参数);

URL：指的是打开窗口的地址，窗口名称：指的是window对象的名称，可以是a标签或form标签中target属性值。如果指定的名称是一个已经存在的窗口名称，则返回对该窗口的引用，而不会再新打开一个窗口。    
参数：对打开的窗口进行属性设置。  

    // 打开一个指定位置的窗口：
    window.open("www.google.com","","top=200,left=200"); 
    // 打开一个指定大小的窗口：
    window.open("www.google.com","","width=200,height=200");
    // 打开一个固定大小的窗口：    	
    window.open("www.google.com","","width=200,height=200,resizable");

其他常用方法：  

    open()、close()	//打开窗口、关闭窗口
    resizeBy()、resizeTo()	//改变窗口大小
    moveBy()、moveTo()	//移动窗口
    setTimeout()、clearTimeout()	//设置或取消“一次性”执行的定时器
    setInterval()、clearInterval()	//设置或取消“重复性”执行的定时器

2. 窗口历史   
history对象属性：  

        current	//当前窗口的URL
        next	//历史列表中的下一个URL
        previous	//历史列表中的前一个URL
        length	//历史列表的长度，用于判断列表中的入口数目

history对象方法:  

    go()	//进入指定的网页
    back()	//返回上一页
    forward()	//进入下一页

常见的“上一页”与“下一页”实现代码如下：  

    <a href="javascript:window.history.forward();">下一页</a>
    <a href="javascript:window.history.back();">上一页</a>

