---                
layout: post                
title: "HTML Margin 与 padding 的区别" 
date:   2021-09-30 15:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

边距又分为外边距（margin）和内边距（padding）  
margin和padding是在html中的盒模型的基础上出现的，margin是盒子的外边距，即盒子与盒子之间的距离，而padding是内边距，是盒子的边与盒子内部元素的距离。  
 
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/css6.png?raw=true)  


## padding
padding 是内填充  
注意：设置padding后会撑大容器的大小  
padding 值不能为负数  
用padding时，最好给自身加上box-sizing：border-box；（固定边框）  

## Margin
Margin是外边距，上下外边距会叠加  
可以设置负值，会向相反方向移动；  
用margin时，最好给父级元素加上overflow：hidden；（溢出隐藏）  

margin是用来隔开元素与元素的间距；padding是用来隔开元素与内容的间隔。margin用于布局分开元素使元素与元素互不相干；padding用于元素与内容之间的间隔，让内容（文字）与（包裹）元素之间有一段“呼吸距离”。  

## 参考
[HTML之margin和padding的区别](https://blog.csdn.net/qq_44829555/article/details/90405269)  
[HTML中margin与padding的区别！](https://www.douban.com/group/topic/55124068/)  
[HTML中的padding和margin](https://www.cnblogs.com/wykid/p/8191025.html)
