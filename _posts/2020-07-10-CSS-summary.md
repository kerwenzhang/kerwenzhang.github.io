---                                  
layout: post                                  
title: "Html 总结"                                  
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