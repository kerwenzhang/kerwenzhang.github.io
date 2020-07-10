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


### 文本样式

#### text-align
在CSS中，使用text-align属性控制文本的水平方向的对齐方式：左对齐、居中对齐、右对齐。  

    text-align: center      /* 文本居中对齐 */

#### line-height
line-height属性指的是行高，而不是行间距。  

    height: 30px;
    line-height: 30px;  /* line-height等于height, 实现垂直居中的效果 */

### 边框样式

要设置一个元素的边框必须要设置以下3个方面：  
（1）边框的宽度；  
（2）边框的外观（实线，或者虚线）；  
（3）边框的颜色；   
简洁的写法：  

    border:1px solid gray;  

### 背景样式
#### background-color

    div{
        background-color:red;
    }

color和background-color区别：   
color为元素文本颜色，background-color为元素背景颜色   

#### background-image

    div {
        background-image:url("../images/one piece.jpg") no-repeat;
    }

### 超链接样式

去除超链接下划线:  

    text-decoration:none;

定义超链接伪类:  

    a:link{CSS样式}     /* 定义a元素未访问时的样式 */
    a:visited{CSS样式}
    a:hover{CSS样式}
    a:actived{CSS样式}

### 图片
#### 水平对齐text-align
text-align一般只用在两个地方：文本水平对齐和图片水平对齐。也就是说，text-align只对文本和img标签有效，对其他标签无效。  

### CSS 盒子模型
在“CSS盒子模型”理论中，所有页面中的元素都可以看成一个盒子，并且占据着一定的页面空间。   
每个盒子都是由content（内容）、padding（内边距）、margin（外边距）和border（边框）这四个属性组成的。此外，在盒子模型中，还有宽度width和高度height两大辅助性属性。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css6.png?raw=true) 

可以使用margin来实现盒子的居中对齐：  

    margin: 0 auto;     /*居中对齐 */

### float布局
#### 正常文档流
在学习浮动布局之前，我们先来认识一下什么叫“正常文档流”。  
什么叫文档流？简单来说，就是元素在页面出现的先后顺序。  
那什么叫“正常文档流”呢？我们先来看一下正常文档流的简单定义：正常文档流，将窗体自上而下分成一行一行，块元素独占一行，相邻行内元素在每行中按从左到右地依次排列元素。  

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css7.jpg?raw=true) 
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css8.jpg?raw=true) 

因为div、p、hr都是块元素，因此独占一行。而span、i、img都是行内元素，因此如果两个行内元素相邻，就会会位于同一行，并且从左到右排列。  

#### 脱离正常文档流
所谓的脱离文档流就是指它所显示的位置和文档代码的顺序不一致了，比如可以用CSS控制div的显示位置，  
在CSS布局中，我们可以使用浮动或者定位这两种技术来实现“脱离正常文档流”，从而随心所欲地控制着页面的布局。   

#### 浮动float
在传统的印刷布局中，文本可以按照实际需要来围绕图片。一般把这种方式称为“文本环绕”。在网页设计中，应用了CSS的float属性的页面元素就像在印刷布局里被文字包围的图片一样。   
<font color="red">浮动元素会生成一个块级框，而不论它本身是何种元素。</font>   

#### 清除浮动clear

    clear: left/right/both

### 定位布局
浮动布局比较灵活，但是不容易控制。而定位布局的出现，使得用户精准定位页面中的任意元素成为可能，使得网页布局变得更加随心所欲。当然由于定位布局缺乏灵活性，也给空间大小和位置不确定的版面布局带来困惑。   
定位的方法有很多种，它们分别是固定定位（fixed）、相对定位（relative）、绝对定位（absolute）和静态定位（static）。  
#### 固定定位fixed
当元素的position属性设置为fixed时，这个元素就被固定了，被固定的元素不会随着滚动条的拖动而改变位置。在视野中，固定定位的元素的位置是不会改变的。  

    position:fixed;
    top:像素值;
    bottom;像素值;
    left:像素值;
    right:像素值;

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css9.jpg?raw=true) 

#### 相对定位relative
采用相对定位的元素，其位置是相对于它的原始位置计算而来的。相对定位是通过将元素从原来的位置向上、向下、向左或者向右移动来定位的。采用相对定位的元素会获得相应的空间。  

<font color="red">CSS相对定位元素的位置是相对于原始位置而言，而固定定位元素的位置是相对浏览器而言！ </font>   
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css10.jpg?raw=true) 

#### 绝对定位absolute
绝对定位在几种定位方法中使用最广泛，这种方法能够很精确地把元素移动到任意你想要的位置。  
一个元素变成了绝对定位元素，这个元素就完全脱离正常文档流了，绝对定位元素的前面或者后面的元素会认为这个元素并不存在，即这个元素浮于其他元素上面，它是独立出来的。  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css11.jpg?raw=true) 

#### 静态定位static
如果没有指定元素的position属性值，也就是默认情况下，元素是静态定位。  
只要是支持position属性的html对象都是默认为static。static是position属性的默认值，它表示块保留在原本应该在的位置，不会重新定位。  