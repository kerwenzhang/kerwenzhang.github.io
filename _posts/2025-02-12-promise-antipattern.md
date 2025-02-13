---                
layout: post                
title: "Promise antipattern                
date:   2025-2-12 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

    function bad() {
        return new Promise(function(resolve) {
            getOtherPromise().then(function(result) {
                resolve(result.property.example);
            });
        })
    }

If the other promise is rejected, this will happen unnoticed instead of being propagated to the new promise (where it would get handled) - and the new promise stays forever pending, which can induce leaks.


    function good() {
        return getOtherPromise().then(function(result) {
            return result.property.example;
        })
    }



# Reference

[What is the explicit promise construction antipattern and how do I avoid it?](https://stackoverflow.com/questions/23803743/what-is-the-explicit-promise-construction-antipattern-and-how-do-i-avoid-it)  
[https://zhuanlan.zhihu.com/p/685103077](https://zhuanlan.zhihu.com/p/685103077)  
[谈谈使用promise时候的一些反模式](https://blog.csdn.net/kingppy/article/details/50487814)  
[ES6 Promise：模式与反模式](https://zhuanlan.zhihu.com/p/29783901)   
[Promise 反模式的坑](https://juejin.cn/post/7064826664168980488)  
[promises 很酷，但很多人并没有理解就在用了 ](https://www.sohu.com/a/127089996_463987)  