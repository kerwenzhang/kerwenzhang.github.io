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

# WebSocket的起源和演变
WebSocket协议的起源可以追溯到早期的Web应用中对于实时通信的需求。最初，开发者们依赖于轮询（`polling`）和长轮询（`long polling`）等技术来模拟服务器推送的能力。然而，这些方法在大规模应用中效率低下，且延迟较高，这促使了WebSocket协议的诞生。  

WebSocket的演变始于HTML5规范的制定，它提供了一种在单个TCP连接上进行全双工通信的机制。这种新的协议使得客户端和服务器之间可以进行双向数据传输，无需像HTTP那样进行重复的连接建立和销毁，大大提高了效率。  

在WebSocket出现之前，开发者们常使用iframe或者Flash来实现类似的功能，但这些方法要么不被现代浏览器支持，要么存在安全和性能问题。因此，WebSocket的推出，可以说是对Web实时通信需求的一次革命性的响应。  

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

# WebSocket协议细节

##  协议帧结构
WebSocket协议的数据传输是基于帧（`frame`）的。每个帧携带了一部分数据，这些数据可以是文本、二进制或者控制帧。控制帧用于管理WebSocket连接，例如关闭连接或发送ping和pong消息以保持连接活跃。  

帧结构的设计使得WebSocket可以高效地传输数据，同时还能进行必要的控制。帧的类型、数据负载长度、掩码键（masking key）等信息都包含在帧的头部中，这样接收方就可以正确地解析和处理数据。  

## 控制帧和数据帧
WebSocket协议区分了控制帧和数据帧。控制帧用于控制WebSocket连接的状态，包括打开连接、关闭连接、发送ping和pong消息等。数据帧则用于传输实际的业务数据。  

控制帧的类型包括`CONNECT`、`DISCONNECT`、`PING`、`PONG`和`SUBSCRIBE`等。这些帧通常不包含有效载荷数据，或者只包含少量的数据。数据帧的类型为`MESSAGE`，它用于传输应用数据，可以是文本格式也可以是二进制格式。  

# WebSocket API的基本使用
## 创建WebSocket连接
要开始使用WebSocket API，首先需要创建一个WebSocket连接。这通常涉及创建一个新的 WebSocket 对象，并指定要连接的服务器的URL。以下是一个简单的示例：

    var socket = new WebSocket('ws://***/socket');

这里，我们创建了一个新的WebSocket对象 socket ，并将其连接到 *** 服务器上的 /socket 路径。这个URL必须是以 ws:// 或 wss:// 开头的URI。 ws:// 用于非加密连接，而 wss:// 用于加密连接，类似于HTTPS。

## 发送和接收数据
一旦WebSocket连接被创建，我们就可以使用 send 方法发送数据，以及监听 message 事件来接收数据。下面的代码展示了如何发送文本消息和如何处理接收到的消息：

    // 发送文本消息
    socket.send('Hello, server!');
    
    // 监听接收消息事件
    socket.onmessage = function(event) {
      var data = event.data; // 接收到的数据
      console.log('Message from server ', data);
    };

在这个示例中，我们发送了一个简单的字符串 'Hello, server!' 到服务器，并在接收到消息时，通过 message 事件的回调函数打印出消息内容。  

# Reference
[JavaScript Socket编程与WebSocket应用实践](https://blog.csdn.net/weixin_36123300/article/details/142924302)  
[Socket.IO-Client 使用教程](https://blog.csdn.net/gitblog_00989/article/details/141210300)   
[从理解到精通"socket.io-client"包实时通讯](https://juejin.cn/post/7260324692506460197)  