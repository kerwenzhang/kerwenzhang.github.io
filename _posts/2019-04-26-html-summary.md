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
#### 块元素: 
div, nav, dl, ol,ul,table,p, form,hr, h1-h6  
特征：
1. 能够识别宽高
2. margin和padding的上下左右均对其有效
3. 可以自动换行
4. 多个块状元素标签写在一起，默认排列方式为从上至下

#### 行内元素
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
### 浮动

### height padding margin

