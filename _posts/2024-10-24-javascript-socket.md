---
layout: post
title: "JavaScript socket编程"
date: 2024-10-24 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---
Socket编程是一种网络通信的编程范式，它允许程序通过网络发送和接收数据。在Web开发中，尤其是在JavaScript中，Socket编程通常指的是使用WebSocket协议进行实时通信。WebSocket提供了一种在单个TCP连接上进行全双工通信的方式，使得客户端和服务器之间可以实时交换数据。    
在JavaScript中，通过HTML5引入的WebSocket API，开发者可以轻松地创建Socket连接。这种连接是持久的，意味着一旦建立，就可以在无需重新连接的情况下进行数据交换。这对于需要实时数据交互的应用，如在线聊天、实时监控等场景非常有用。   

# WebSocket vs HTTP
WebSocket与HTTP虽然都是应用层协议，但它们在设计哲学和使用场景上有很大的不同。HTTP是一个无状态的请求/响应协议，主要关注于资源的请求和传输。而WebSocket则是一个全双工的协议，设计之初就是为了保持一个持久的连接，并允许服务器和客户端之间自由地交换消息。  

在性能方面，WebSocket由于其持久连接的特性，减少了建立和关闭连接的开销，使得它在需要高频实时通信的应用中表现更为出色。相比之下，HTTP由于每次通信都需要建立新的连接，其性能在高并发场景下会受到限制。  

在易用性方面，WebSocket由于需要在客户端和服务器之间维持一个长时间的连接，其编程模型比HTTP复杂。但在现代Web开发中，许多框架和库已经封装好了WebSocket的复杂性，使得开发者可以更专注于业务逻辑的实现。  

# WebSocket的技术特性
## 实时性
WebSocket协议的一个核心特性就是实时性。它能够在客户端和服务器之间建立一个持久的连接，并允许双方以接近实时的方式交换数据。这种能力使得WebSocket在需要快速响应的应用场景中变得非常有价值，例如实时聊天、在线游戏、股票交易等。

实时性是通过WebSocket协议的全双工通信模型实现的。在这个模型中，服务器可以在任何时候向客户端发送数据，而无需客户端显式地请求。这种通信方式的效率和响应速度远远超过了传统的HTTP轮询或长轮询技术。

## 全双工通信
全双工通信意味着WebSocket连接可以在两个方向上同时进行数据传输。这与传统的HTTP协议不同，后者通常是单向的，即客户端发起请求，服务器响应请求。WebSocket的全双工通信特性极大地扩展了Web应用的可能性，使得开发者可以构建更为复杂和互动的实时Web应用。

# Reference
[JavaScript Socket编程与WebSocket应用实践](https://blog.csdn.net/weixin_36123300/article/details/142924302)  
[Socket.IO-Client 使用教程](https://blog.csdn.net/gitblog_00989/article/details/141210300)   
[从理解到精通"socket.io-client"包实时通讯](https://juejin.cn/post/7260324692506460197)  