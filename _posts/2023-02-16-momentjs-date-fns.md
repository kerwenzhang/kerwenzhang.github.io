---
layout: post
title: 用date-fns替代momentjs
date:   2023-02-16 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

# Moment.js
Moment.js是一个（轻量级）的Javascript日期处理类库，使用它可以轻松解决前端开发中遇到的种种日期时间问题。  
Moment.js不依赖任何第三方库，支持字符串、Date、时间戳以及数组等格式，可以格式化日期时间，计算相对时间，获取特定时间后的日期时间等等。  
支持中文在内的多种语言。  

安装  

    npm install moment

fromNow() 时间间隔或相对时间  

    moment([2007, 0, 29]).fromNow();       // 16 years ago

calendar()  
日历时间显示相对于给定的 referenceTime 的时间（默认为现在），但与 moment#fromNow 略有不同。  
moment.calendar 会根据日期与 referenceTime 的日期（默认为今天）的接近程度，使用不同的字符串格式化日期。  


# date-fns
date-fns是另外一个比热门的JavaScript日期处理工具库，越来越多的人用它来替换Moment.js。它一样提供了大量的函数来操作日期。  
安装：  

    npm install date-fns --save

date-fns是使用纯函数构建的，并且可以再不改变传递日期实例的情况下保持不变。并且由于date-fns里面每一个方法都是一个文件，所以可以非常方便的只引入需要的部分，这相比于Moment.js可以更方便的降低打包体积。  
format()：格式化日期  

    console.log(format(new Date(), "yyyy-MM-dd HH:mm:ss", { locale: zhCN })); //  2021-08-10 11:42:31
    console.log(format(new Date(), "yyyy-MM-dd HH:mm:ss")); // 2021-08-10 11:38:44
    console.log(format(new Date(), "yyyy-MM-dd")); // 2021-08-10
    console.log(format(new Date(), "HH:mm:ss")); // 11:38:44


parseISO()：将字符串形式的日期转换成Date格式的日期  

    console.log(parseISO("2021-12-19")); // Sun Dec 19 2021 00:00:00 GMT+0800 (中国标准时间)

formatDistanceToNow   

    formatDistanceToNow(new Date(2007, 0, 29), { addSuffix: true })  // about 16 years ago

设置全局local:  

    import { setDefaultOptions } from 'date-fns';
    import { es } from 'date-fns/locale';
    setDefaultOptions({ locale: es })

动态改变:  

    import { setDefaultOptions } from 'date-fns';
    import * as Locales from 'date-fns/locale';
    const language = 'en';
    setDefaultOptions({ locale: Locales[language] })

# vs

        console.log(moment(new Date("Wed Feb 15 2023 16:41:55 GMT+080")).calendar());          // Last Wednesday at 11:21 PM
        console.log(formatRelative(new Date("Wed Feb 15 2023 16:41:55 GMT+080"), new Date()));  //Last Wednesday at 11:21 PM

        console.log(moment('2023-01-15 16:41:55').fromNow());      // a month ago
        console.log(formatDistanceToNow(new Date("2023-01-15 16:41:55"), { addSuffix: true }));  // about 1 month ago

Reference
[Moment.js和date-fns](https://blog.csdn.net/duola8789/article/details/90045485)  
[Moment.js 文档](http://momentjs.cn/docs/)  
[date-fns](https://date-fns.org/docs/Getting-Started)  

[https://stackoverflow.com/questions/47271803/moment-vs-date-fns-locale-date-formats](https://stackoverflow.com/questions/47271803/moment-vs-date-fns-locale-date-formats)    
[date-fns: how to define a default locale app-wide?](https://stackoverflow.com/questions/68002600/date-fns-how-to-define-a-default-locale-app-wide)  
[Add function to set locale globally](https://github.com/date-fns/date-fns/issues/816)