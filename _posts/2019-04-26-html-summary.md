---                                  
layout: post                                  
title: "Html 总结"                                  
date:   2019-04-26 9:00:00                                   
categories: "Web"                                  
catalog: true                                  
tags:                                   
    - Web                                  
---                        
    
## 常用VSCode插件  

1. Beautify
2. Html CSS Support
3. HTML Snippets
4. Open HTML in Default Browser
5. vscode-icons

Markdown插件：

1. markdownlint
2. Markdown Preview Enhanced

## Html常用标签

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

### 块元素
div, nav, dl, ol,ul,table,p, form,hr, h1-h6  
特征：

1. 能够识别宽高
2. margin和padding的上下左右均对其有效
3. 可以自动换行
4. 多个块状元素标签写在一起，默认排列方式为从上至下

### 行内元素
只占据它对应标签的边框所包含的空间。只能容纳文本或者其他内联元素。
a,br,img,input,span...  
特征：  

1. 设置宽高无效
2. 对margin仅设置左右方向有效，上下无效；padding设置上下左右都有效，即会撑大空间,
3. 行内元素尺寸由内含的内容决定
4. 不会自动进行换行

#### 行内块元素
行内块状元素综合了行内元素和块状元素的特性，但是各有取舍  
特征:

1. 不自动换行
2. 能够识别宽高
3. 默认排列方式为从左到右

#### 块级元素和内联元素之间的转换

1. Display  
    display:block;转换为块级元素。  
    display:inline;转换为行内元素。  
    display:inline-block;转换为行内块级元素。
2. float  
当把行内元素设置完float:left/right后，该行内元素的display属性会被赋予block值，且拥有浮动特性
3. position  

    当为行内元素进行定位时，position:absolute与position:fixed.都会使得原先的行内元素变为块级元素。

## 知识点
### 浮动float

浮动float的本意是什么呢？是：让文字像流水一样环绕浮动元素。
#### 特征

1. 包裹性  
block元素不指定width的话，默认是100%，一旦让该div浮动起来，立刻会像inline元素一样产生包裹性，宽度会跟随内容自适应。（这也是通常float元素需要手动指定width的原因）
2. 高度欺骗

#### 闭合浮动

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

ref 1: [https://www.jianshu.com/p/07eb19957991](https://www.jianshu.com/p/07eb19957991)  
ref 2: http://www.cnblogs.com/iyangyuan/archive/2013/03/27/2983813.html  
ref 3: https://www.zhangxinxu.com/wordpress/2010/01/css-float%E6%B5%AE%E5%8A%A8%E7%9A%84%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6%E3%80%81%E8%AF%A6%E8%A7%A3%E5%8F%8A%E6%8B%93%E5%B1%95%E4%B8%80/  
ref 4: https://www.zhangxinxu.com/wordpress/2010/01/css-float%E6%B5%AE%E5%8A%A8%E7%9A%84%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6%E3%80%81%E8%AF%A6%E8%A7%A3%E5%8F%8A%E6%8B%93%E5%B1%95%E4%BA%8C/
### height padding margin

