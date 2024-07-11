---
layout: post
title: Angular Flex-Layout
date:   2022-11-16 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

Angular Flex Layout 使用 Flexbox CSS + mediaQuery 提供了一个复杂的布局 API。布局引擎智能地自动将适当的 CSS 应用于浏览器视图层次结构的过程。这种自动化还解决了传统的、手动的、仅 CSS 的 Flexbox CSS 应用程序遇到的许多复杂性和变通方法。    
Flex Layout的真正强大之处在于它的响应引擎。响应式 API使开发人员能够轻松地为不同的视口大小和显示设备指定不同的布局、大小和可见性。  

# 安装

    npm i -s @angular/flex-layout @angular/cdk

需要在应用的模块中导入 Layout 模块。  
app.module.ts  

    import { FlexLayoutModule } from '@angular/flex-layout';
    ...

    @NgModule({
        ...
        imports: [ FlexLayoutModule ],
        ...
    });

配置完成后，就可以在 HTML 标签中使用 Angular Layout 属性进行 flex 布局：

    <div fxLayout="row" fxLayoutAlign="space-between">
    </div>

[Flex-layout演示网址](https://tburleson-layouts-demos.firebaseapp.com/#/docs)  

# Guide
Angular Layout 功能提供了智能的语法指令，使开发人员能够使用 Flexbox 和 CSS Grid 轻松直观地创建响应式和自适应布局。  
flex-container的结构如下图  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/flex1.jpg?raw=true) 
在 flex 容器中默认存在两条轴，水平主轴(main axis) 和垂直的交叉轴(cross axis)，这是默认的设置  
在容器中的每个单元块被称之为 flex item，每个项目占据的主轴空间为 (main size), 占据的交叉轴的空间为 (cross size)。  
这里需要强调，不能先入为主认为宽度就是 main size，高度就是 cross size，这个还要取决于你主轴的方向，如果你垂直方向是主轴，那么项目的高度就是 main size。  

以下API可以用在容器container上  

| HTML | API | 允许的值 | 说明|
| --- | ----------- | --------| --------|
| fxLayout | direction [wrap] | row, column, row-reverse, column-reverse | 决定主轴的方向(即项目的排列方向) |  
| fxLayoutAlign | main-axis, cross-axis | main-axis: start, center, end, space-around, space-between, space-evenly; cross-axis: start, center, end, stretch, space-between, space-around, baseline | 子容器应在主轴和横轴上对齐（可选）|  
| fxLayoutGap | %, px, vw, vh| N/A |指定 flexbox 容器（例如，嵌套在 fxLayout 容器中）内子项的边距间隙 |  


flex-direction: 决定主轴的方向(即项目的排列方向)  

    .container {
        flex-direction: row | row-reverse | column | column-reverse;
    }

flex-wrap: 决定容器内项目是否可换行  

    .container {
        flex-wrap: nowrap | wrap | wrap-reverse;
    }

flex-flow: flex-direction 和 flex-wrap 的简写形式  

justify-content：定义了项目在主轴的对齐方式。

    .container {
        justify-content: flex-start | flex-end | center | space-between | space-around;
    }

space-between：两端对齐，项目之间的间隔相等，即剩余空间等分成间隙。  
space-around：每个项目两侧的间隔相等，所以项目之间的间隔比项目与边缘的间隔大一倍。  

align-items: 定义了项目在交叉轴上的对齐方式  

    .container {
        align-items: flex-start | flex-end | center | baseline | stretch;
    }

以下API可以用在元素element上  

| HTML | 允许的值 | 说明|
| --- | ----------- | --------| --------|
| fxFlex | "", px, %, vw, vh, grow, shrink, basis | 应用于 fxLayout 容器中的元素，并标识flexbox容器流中该元素的大小调整。 |  
| fxFlexOrder | int | 用于已排序的fxLayout容器中的元素，并标识元素的位置顺序 |  
| fxFlexFill, fxFill | N/A | fxFlexFill不接受任何参数，并使用以下内联 CSS 样式填充其宿主元素 margin:0, width:100%, height:100%, min-width:100%, min-height:100%  | 	 

flex  
默认0 1 auto，flex属性是flex-grow，flex-shrink与flex-basis三个属性的简写，用于定义项目放大，缩小与宽度。

flex-grow 定义项目的放大比例

    .item {
        flex-grow: <number>;
    }

默认值为 0，即如果存在剩余空间，也不放大  


flex-shrink    
用于决定项目在空间不足时是否缩小，默认是1，即空间不足时大家一起等比缩小；注意，即便设置了固定宽度，也会缩小。权重比width属性高    

在同一时间，flex-shrink 和 flex-grow 只有一个能起作用，这其中的道理细想起来也很浅显：空间足够时，flex-grow 就有发挥的余地，而空间不足时，flex-shrink 就能起作用。  

flex-basis   
flex-basis: 定义了在分配多余空间之前，项目占据的主轴空间，浏览器根据这个属性，计算主轴是否有多余空间 当主轴为水平方向的时候，当设置了 flex-basis，项目的宽度设置值会失效，即如果设置了flex-basis，权重会比width属性高，会覆盖width属性。
flex-basis 需要跟 flex-grow 和 flex-shrink 配合使用才能发挥效果。  



以下API可以用在任何元素上：  

| HTML | 允许的值 | 说明|
| --- | ----------- | --------| --------|
| fxHide | TRUE, FALSE, 0, "" | 显示/隐藏托管元素。fxHide 逻辑默认隐藏一个元素 |   
| fxShow | TRUE, FALSE, 0, "" | 显示/隐藏托管元素。fxShow 逻辑默认显示一个元素 |   

以下代指屏幕的大小，可以与指令结合起来使用

| breakpoint | mediaQuery |  
| xs	| 'screen and (max-width: 599px)'|  
| sm	| 'screen and (min-width: 600px) and (max-width: 959px)'|  
| md	| 'screen and (min-width: 960px) and (max-width: 1279px)'|  
| lg	| 'screen and (min-width: 1280px) and (max-width: 1919px)'|  
| xl	| 'screen and (min-width: 1920px) and (max-width: 5000px)'|  
| lt-sm	| 'screen and (max-width: 599px)'|  
| lt-md	| 'screen and (max-width: 959px)'|  
| lt-lg	| 'screen and (max-width: 1279px)'|  
| lt-xl	| 'screen and (max-width: 1919px)'|  
| gt-xs	| 'screen and (min-width: 600px)'|  
| gt-sm	| 'screen and (min-width: 960px)'|  
| gt-md	| 'screen and (min-width: 1280px)'|  
| gt-lg	| 'screen and (min-width: 1920px)'|  


# Reference
[Angular Layout](https://github.com/angular/flex-layout/wiki)  
[Flex布局详解](https://zhuanlan.zhihu.com/p/367346487)    
[Flex布局详解](https://zhuanlan.zhihu.com/p/359561226)    
[Flex布局总结](https://blog.csdn.net/tsfx051435adsl/article/details/86075602)  