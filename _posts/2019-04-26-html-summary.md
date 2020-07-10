---                                  
layout: post                                  
title: "Html 总结"                                  
date:   2019-04-26 9:00:00                                   
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


# 常用VSCode插件  

1. Beautify
2. Html CSS Support
3. HTML Snippets
4. Open HTML in Default Browser
5. vscode-icons

Markdown插件：

1. markdownlint
2. Markdown Preview Enhanced

# Html常用标签

基本框架：

    <html>
        <head>
            <meta charset="utf-8"/>
            <title>页面名称</title>
            <link rel="stylesheet" type="text/css" href="文件路径"/>
            <style>样式</style>
            <script>js脚本</script>
        </head>
        <body>
            <div>
                <p></p>
            </div>
        </body>
    </html>

1. 链接 a
2. 特殊字符：
3. 换行元素 br
4. 分隔线元素 hr

## 块元素
div, nav, dl, ol,ul,table,p, form,hr, h1-h6    
特征：

1. 能够识别宽高
2. margin和padding的上下左右均对其有效
3. 可以自动换行
4. 多个块状元素标签写在一起，默认排列方式为从上至下

## 行内元素
只占据它对应标签的边框所包含的空间。只能容纳文本或者其他内联元素。  
a,br,img,input,span...  
特征：  

1. 设置宽高无效
2. 对margin仅设置左右方向有效，上下无效；padding设置上下左右都有效，即会撑大空间,
3. 行内元素尺寸由内含的内容决定
4. 不会自动进行换行

## 行内块元素
行内块状元素综合了行内元素和块状元素的特性，但是各有取舍  
特征:

1. 不自动换行
2. 能够识别宽高
3. 默认排列方式为从左到右

## 块级元素和内联元素之间的转换

1. Display  
    display:block;转换为块级元素。  
    display:inline;转换为行内元素。  
    display:inline-block;转换为行内块级元素。
2. float  
当把行内元素设置完float:left/right后，该行内元素的display属性会被赋予block值，且拥有浮动特性
3. position  

    当为行内元素进行定位时，position:absolute与position:fixed.都会使得原先的行内元素变为块级元素。

# 知识点
## 浮动float

浮动float的本意是什么呢？是：让文字像流水一样环绕浮动元素。
### 特征

1. 包裹性  
block元素不指定width的话，默认是100%，一旦让该div浮动起来，立刻会像inline元素一样产生包裹性，宽度会跟随内容自适应。（这也是通常float元素需要手动指定width的原因）
2. 高度欺骗

### 闭合浮动

1. 增加一个清除浮动的子元素  

        <div style="border:4px solid blue;">
            <div style="width:200px;border:4px solid red;float:left;">
                我是浮动元素1
            </div>
            <div style="width:200px;border:4px solid yellow;float:left;">
                我是浮动元素2
            </div>
            <div style="clear:both;"></div>  //加上空白div节点来闭合浮动
        </div>
        <div style="border:4px solid gray;">我是页脚</div>

2. 父元素设置 overflow:hidden

        <div style="border:4px solid blue;overflow:hidden;">
            <div style="width:200px;border:4px solid red;float:left;">
                我是浮动元素1
            </div>
            <div style="width:200px;border:4px solid yellow;float:left;">
                我是浮动元素2
            </div>
        </div>
        <div style="border:4px solid gray;">我是页脚</div>

3. 用:after伪元素，思路是用:after元素在div后面插入一个隐藏文本”.”，隐藏文本用clear来实现闭合浮动

        .clearfix:after {
            clear: both;
            content: ".";   //你头可以改成其他任意文本如“abc”
            display: block;
            height: 0;      //高度为0且hidden让该文本彻底隐藏
            visibility: hidden;
        }
        .clearfix {
            *zoom: 1;
        }

ref 1: [CSS浮动float详解](https://www.jianshu.com/p/07eb19957991)  
ref 2: [CSS浮动(float,clear)通俗讲解](http://www.cnblogs.com/iyangyuan/archive/2013/03/27/2983813.html)  
ref 3: [CSS float浮动的深入研究、详解及拓展(一)](https://www.zhangxinxu.com/wordpress/2010/01/css-float%E6%B5%AE%E5%8A%A8%E7%9A%84%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6%E3%80%81%E8%AF%A6%E8%A7%A3%E5%8F%8A%E6%8B%93%E5%B1%95%E4%B8%80/)  
ref 4: [CSS float浮动的深入研究、详解及拓展(一)](https://www.zhangxinxu.com/wordpress/2010/01/css-float%E6%B5%AE%E5%8A%A8%E7%9A%84%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6%E3%80%81%E8%AF%A6%E8%A7%A3%E5%8F%8A%E6%8B%93%E5%B1%95%E4%BA%8C/)   
ref 5: [那些年我们一起清除过的浮动](http://www.iyunlu.com/view/css-xhtml/55.html)

## padding margin border

margin是指从自身边框到另一个容器边框之间的距离，就是容器外距离。  
padding是指自身边框到自身内部另一个容器边框之间的距离，就是容器内距离。
![border](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/border.jpg?raw=true)

## position

### 相对定位 relative
定位是相对于自身位置定位（设置偏移量的时候，会相对于自身所在的位置偏移）。  
设置了 relative 的元素仍然处在文档流中，元素的宽高不变，设置偏移量也不会影响其他元素的位置。  
最外层容器设置为 relative 定位，在没有设置宽度的情况下，宽度是整个浏览器的宽度。  
相对定位元素经常被用来作为绝对定位元素的容器块。

### 绝对定位 absolute
元素的位置相对于浏览器窗口，是固定位置。即使窗口是滚动的它也不会移动。  
绝对定位是相对于离元素最近的设置了绝对或相对定位的父元素决定的，如果没有父元素设置绝对或相对定位，则元素相对于根元素即 html 元素定位。  
设置了 absolute 的元素脱了了文档流，元素在没有设置宽度的情况下，宽度由元素里面的内容决定。  
脱离后原来的位置相当于是空的，下面的元素会来占据位置。

## 权重

| *选择器* | *表达式或示例* | *权重值* |  
|ID选择器|#aaa|100|  
|类选择器|.aaa|10|  
|标签选择器|h1|1|  
|属性选择器|[title]|10|
|通配符选择器|*|0|  
|各种伪类选择器|如:link， :visited， :hover|10|  
|各种伪元素|::first-letter,::first-line,::after,::before,::selection|1|

## 伪类 伪元素
css引入伪类和伪元素概念是为了格式化文档树以外的信息。也就是说，伪类和伪元素是用来修饰不在文档树中的部分，比如，一句话中的第一个字母，或者是列表中的第一个元素。  
CSS3规范中的要求使用双冒号(::)表示伪元素，以此来区分伪元素和伪类.
![class](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/class.png?raw=true)

![item](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/item.png?raw=true)