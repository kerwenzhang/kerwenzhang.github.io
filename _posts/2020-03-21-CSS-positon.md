---                
layout: post                
title: "CSS定位中的子绝父相" 
date:   2020-03-21 10:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

position是CSS样式中一个样式，从英文意思理解就是位置，就是用来定位的。其样式下有几个属性，分别是absolute、relative、static(默认)、fixed等等

子绝父相的意思是在父类的position属性是relative的情况下，子类的position属性又是absolute的情况下，那么我们的子类这时其实不是在body中absolute而是在其父类的范围中absolute

### static定位  
默认值。没有定位，元素出现在正常的流中。意思是有关元素将按照它们在标记里出现的先后顺序出现在浏览器窗口里。  

### 相对定位relative
什么是相对定位？相对什么定位？相对自己文档流中的原始位置定位。它的特点是——不会脱离文档流。

也就是说，使用position:relative定位，其元素依旧在文档流中，他的位置可以使用 left、right、top、bottom、z-index等定位参数，但是，他的存在，还是会影响文档中紧跟在他周围的元素的。

### 固定定位

position:fixed 相对浏览器定位。它相对于浏览器的窗口进行定位。同时——它会脱离文档流  

### 绝对定位absolute
生成绝对定位的元素，相对于 除static 定位以外的第一个父元素进行定位。  
元素的位置通过 "left", "top", "right" 以及 "bottom" 属性进行规定。   

### 总结
position: relative;不会脱离文档流，position: fixed;position: absolute;会脱离文档流  
position: relative; 相对于自己在文档流中的初始位置偏移定位。  
position: fixed; 相对于浏览器窗口定位。  
position: absolute; 绝对定位是相对于最近的已定位祖先元素，如果元素没有已定位的祖先元素，那么它的位置会相对于文档定位。  


设置父元素相对定位，子元素绝对定位，那么子元素就是相对于这个父元素的位置来定位的。


[https://www.cnblogs.com/JNovice/p/9536910.html](https://www.cnblogs.com/JNovice/p/9536910.html)  
[https://www.jianshu.com/p/6c46d7800249](https://www.jianshu.com/p/6c46d7800249)  
[https://www.imooc.com/wenda/detail/311347](https://www.imooc.com/wenda/detail/311347)  
[https://blog.csdn.net/fungleo/article/details/50056111](https://blog.csdn.net/fungleo/article/details/50056111)

