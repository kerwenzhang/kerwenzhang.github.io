---                
layout: post                
title: "JavaScript异步编程"                
date:   2025-1-15 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

异步编程是一种编程方式，它允许程序在等待某些操作完成的同时，继续执行其他任务。这种编程方式可以显著提高程序的执行效率，特别是在处理 I/O 密集型任务（如网络请求、文件读写等）时表现出色。  

在 JavaScript 中，异步编程的实现主要依赖于事件循环（Event Loop）、回调函数（Callback Functions）、Promise 对象以及 async/await 语法糖等机制。这些机制相互配合，共同构成了 JavaScript 异步编程的完整体系。

# 回调函数 Callback
回调函数是 JavaScript 中实现异步操作的一种基本方式。它将回调函数作为参数传递给异步函数，在异步操作完成后被调用。通过回调函数，我们可以将异步操作的结果传递给后续代码进行处理。  
回调函数的优点是简单易懂，但在实际应用中，过多的回调函数嵌套会导致代码难以维护，这种情况被称为“回调地狱”。

    function fetchData(url, callback) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                callback(null, data);
            })
            .catch(error => {
                callback(error);
            });
    }

    fetchData('http://www.google.com', (error, data) => {
        if(error) {
            console.error('Request failed: ', error)
        } else {
            console.log('Request succeed: ', data);
        }
    })


# Promise
为了解决回调地狱的问题，ES6 引入了 Promise 对象。Promise 是一种表示异步操作最终完成或失败的对象，它提供了更清晰的异步编程方式。  
Promise 对象有三种状态， Promise 对象的状态只能从 pending 转变为 fulfilled 或 rejected，且一旦状态改变就不会再变。
+ pending（进行中）
+ fulfilled/resolve（已成功）
+ rejected（已失败）  

    
Promise 对象提供了 then() 和 catch() 方法来处理异步操作的结果。  
then() 方法用于处理成功的情况，  
catch() 方法用于处理失败的情况。  
通过链式调用 then() 和 catch() 方法，我们可以避免回调地狱，使代码更加简洁易读。

一个Promise函数的结构如下列代码如下：

    const promise = new Promise((resolve, reject) => {
        resolve('a');
    });

    promise
        .then((arg) => { console.log('execute resolve, param: ', arg)})
        .catch((arg) => { console.log('execute reject, param: ', arg)})
        .finally(()=>{ console.log('End of promise')});

如果我们需要嵌套执行异步代码，相比于回调函数来说，Promise的执行方式如下列代码所示：

    const promise2 = new Promise((resolve, reject) => {
        resolve(1);
    })
    promise2.then((value) => {
        console.log(value);
        return value * 2;
    }).then((value)=>{
        console.log(value);
        return value * 2;
    }).then((value)=>{
        console.log(value);
        return value * 2;
    }).catch((err)=>{
        console.log(err);
    })

Promise 对象的优点是代码更加简洁易读，但仍需要一定的学习成本。  

    function fetchData(url) {
        return fetch(url);
    }

    fetchData('https://www.google.com')
        .then(response => response.text())
        .then(data => {
            console.log('Request succeed: ', data);
        })
        .catch(error => {
            console.error('Request failed: ', error);
        })

## Promise本身是同步，then的内容是异步

    let p = new Promise((resolve,reject) => {
        console.log("promise本身是同步");
        resolve("then是异步");
    }).then((res) => {
        console.log(res);
    })
    console.log("想不到吧");

最终输出

    promise本身是同步
    想不到吧
    then是异步

## 使用Promise封装异步操作

在下面例子中，validateUrl函数返回一个Promise对象，用于封装异步操作。请求完成后调用resolve或reject方法，Promise对象的then方法和catch方法用于处理异步操作的结果或错误。

    function validateUrl(url) {
        return new Promise(function (resolve, reject) {
            if (url === "https://www.google.com") {
                resolve("Validate url");
            } else {
                reject("Invalid url");
            }
        });
    }

    validateUrl("https://www.google.com")
        .then(function (data) {
            console.log("Request succeed: ", data);
        })
        .catch((error) => {
            console.error("Request failed: ", error);
        });

## Promise.then
then()这个方法是Promise实现了Thenable方法所具有的，该方法接受两个参数：  
.then 的第一个参数是一个函数，该函数将在 promise resolved 且接收到结果后执行。  
.then 的第二个参数也是一个函数，该函数将在 promise rejected 且接收到 error 信息后执行   

    let promise = new Promise((resolve, reject) => {
        let success = true; // 模拟一个成功或失败的条件
        if (success) {
            resolve("操作成功");
        } else {
            reject("操作失败");
        }
    });

    promise.then(
        (result) => {
            console.log("成功:", result);
        },
        (error) => {
            console.log("失败:", error);
        }
    );

由于Promise只能改变一次状态，因此then()方法的两个函数参数实现是互斥的，我们可以省略其中一个参数从而更加关注另外一种状态改变的参数。  
由于Promise的.then方法也会返回一个Promise对象，且前面的then方法中回调函数的返回值会作为后面then方法回调的参数。由此可以通过then的链式调用取代回调函数嵌套，避免了回调地狱，让代码更加扁平化。 


    // 链式调用 Promise
    task1()
        .then(task2)
        .then(task3)
        .then(() => {
            console.log('All tasks completed');
        })
        .catch((error) => {
            console.log('An error occurred:', error);
        });


# async/await
为了进一步简化异步编程，ES7 引入了 async/await 语法糖。async/await 是基于 Promise 对象的语法糖，它使得异步代码看起来更像同步代码，从而提高了代码的可读性和可维护性。

async 函数是一个返回 Promise 对象的函数，它内部的代码可以使用 await 关键字来等待 Promise 对象的结果。await 关键字只能在 async 函数内部使用。

async/await 的优点是代码更加简洁易读，且错误处理更加方便。它是目前 JavaScript 中最推荐的异步编程方式。  

    async function fetchData(url){
        try{
            const response = await fetch(url);
            const data = await response.text();
            return data;
        } catch(error) {
            throw error;
        }
    }

    (async() => {
        try{
            const data = await fetchData('https://www.google.com');
            console.log('Request succeed: ', data);
        } catch(error) {
            console.error('Request failed: ', error);
        }
    })();

Example 2

    async function mysw1(){
        return 1;
    }
    console.log("sw1: ",mysw1());  

    async function mysw2(){
        return new Promise((resolve, reject) =>{
            resolve(1);
        });
    }
    console.log("sw2: ",mysw2())  

    async function mysw3(){
        await 1;
    }
    console.log("sw3: ",mysw3());  

    async function mysw4(){
        let a = await 1;
        console.log(a);
    }
    console.log("sw4: ", mysw4(4));

    async function mysw5(){
        let a = await new Promise((resolve)=>{
            resolve(1);
        });
        console.log(a);
    }
    console.log("sw5: ",mysw5());

    async function  mysw6() {
        let a = await new Promise((resolve)=>{
            resolve(1);
        });
        console.log(a);
        return a;
    }
    console.log("sw6: ",mysw6())

    async function  mysw7() {
        let a = await new Promise((resolve)=>{
            resolve(1);
        });
        console.log(a);
        return a;
    }
    mysw7().then((res)=>{
        console.log("sw7: ", res);
    })

Example3:  
使用async/await后，契约连锁会变得很简单：  
不使用async/await关键字  

    function fetchData(url: string): Promise<string> {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve(`Data from ${url}`);
            }, 1000);
        });
    }

    function processData() {
        fetchData('https://api.example.com/data1')
            .then(data1 => {
                console.log(data1);
                return fetchData('https://api.example.com/data2');
            })
            .then(data2 => {
                console.log(data2);
                return fetchData('https://api.example.com/data3');
            })
            .then(data3 => {
                console.log(data3);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    processData();

使用async/await优化后  

    async function fetchData(url: string): Promise<string> {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve(`Data from ${url}`);
            }, 1000);
        });
    }

    async function processData() {
        try {
            const data1 = await fetchData('https://api.example.com/data1');
            console.log(data1);

            const data2 = await fetchData('https://api.example.com/data2');
            console.log(data2);

            const data3 = await fetchData('https://api.example.com/data3');
            console.log(data3);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    processData();


# 同步如何调用异步

    (async() => {
            try{
                const data = await fetchData('https://www.google.com');
                console.log('Request succeed: ', data);
            } catch(error) {
                console.error('Request failed: ', error);
            }
        })();


异步如何调用同步


# Reference

[JavaScript 异步编程：探索未来编程的无限可能](https://www.jianshu.com/p/0bc52c4db2dc)  
[js四种异步方法（回调函数、Promise、Generator、async/await）](https://www.cnblogs.com/sxww-zyt/p/16665196.html)  