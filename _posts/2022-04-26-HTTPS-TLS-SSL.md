---                
layout: post            
title: "HTTPS, TLS, SSL三者区别"                
date:   2022-4-26 13:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

SSL(Secure Socket Layer 安全套接层)简而言之，它是一项标准技术，可确保互联网连接安全，保护两个系统之间发送的任何敏感数据，防止网络犯罪分子读取和修改任何传输信息。最初是由网景公司（Netscape）研发，起因是因为HTTP在传输数据时使用的是明文，是不安全的。为了解决这一隐患网景公司推出了SSL安全套接字协议层，SSL是基于HTTP之下，TCP/IP之上的一个协议层，是基于HTTP标准并对TCP传输数据时进行加密，所以HPPTS是HTTP+SSL/TCP的简称。  

由于HTTPS的推出受到了很多人的欢迎，在SSL更新到3.0时，IETF对SSL3.0进行了标准化，并添加了少数机制，标准化后的IETF更名为TLS1.0(Transport Layer Security 安全传输层协议)，可以说TLS就是SSL的新版本3.1。可以说TLS是更为安全的升级版 SSL。

[SSL，HTTPS，TLS三者的区别](https://zhuanlan.zhihu.com/p/158711125)