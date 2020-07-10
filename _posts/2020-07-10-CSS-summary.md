---                                  
layout: post                                  
title: "CSS 总结"                                  
date:   2020-07-10 9:00:00                                   
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


### css的引入方式

在HTML中引入CSS共有3种方式：   
（1）外部样式表； （2）内部样式表； （3）内联样式表；

#### 外部样式表
所谓的“外部样式表”，就是把CSS代码和HTML代码都单独放在不同文件中，然后在HTML文档head标签中使用link标签来引用CSS样式表。 当样式需要被应用到多个页面时，外部样式表是最理想的选择。  

    <link href="index.css" rel="stylesheet" type="text/css" />

#### 内部样式表
内部样式，指的就是把CSS代码和HTML代码放在同一个文件中.   

    <head>  
        <title></title>   
        <style type="text/css">
                p{
                    color:Red;
                }      
        </style>
    </head>

#### 内联样式表

是把CSS代码和HTML代码放在同一个文件中，在标签的style属性中定义.  

    <body>
        <p style="color:Red; ">段落</p>
    </body>

### id和class
#### 元素的id属性

id属性被赋予了标识页面元素的唯一身份。如果一个页面出现了多个相同id属性取值，CSS选择器或者JavaScript就会因为无法分辨要控制的元素而最终报错。  

    <body>
        <div id="first">TEST</div>
    </body>

#### 元素的class属性
class，顾名思义，就是“类”。它采用的思想跟其他C、Java等编程语言的“类”相似。我们可以为同一个页面的相同元素或者不同元素设置相同的class，然后使得相同的class具有相同的CSS样式。  
如果你要为两个元素或者两个以上元素定义相同的样式，建议使用class属性。  

    <body>
        <div class="first">TEST</div>
        <p class="first">TEST</p>
    </body>

### CSS选择器
#### 元素选择器

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css1.jpg?raw=true) 

#### id选择器
id名前面必须要加上前缀“#”，否则该选择器无法生效。id名前面加上“#”，表明这是一个id选择器。  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css2.jpg?raw=true) 

#### class选择器
class名前面必须要加上前缀“.”（英文点号），否则该选择器无法生效。类名前面加上“.”，表明这是一个class选择器。  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css3.jpg?raw=true) 

#### 子元素选择器
子元素选择器，就是选中某个元素下的子元素，然后对该子元素设置CSS样式。  
父元素与子元素必须用空格隔开，从而表示选中某个元素下的子元素。  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css4.jpg?raw=true) 

#### 群组选择器
群组选择器，就是同时对几个选择器进行相同的操作。  
对于群组选择器，两个选择器之间必须用“,”（英文逗号）隔开，不然群组选择器无法生效。  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css5.jpg?raw=true) 