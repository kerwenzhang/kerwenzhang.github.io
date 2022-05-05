---                
layout: post            
title: "SSL, HTTPS, TLS, HSTS 区别"                
date:   2022-4-26 13:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

## SSL
SSL(Secure Socket Layer 安全套接层)简而言之，它是一项标准技术，可确保互联网连接安全，保护两个系统之间发送的任何敏感数据，防止网络犯罪分子读取和修改任何传输信息。最初是由网景公司（Netscape）研发，起因是因为HTTP在传输数据时使用的是明文，是不安全的。为了解决这一隐患网景公司推出了SSL安全套接字协议层，SSL是基于HTTP之下，TCP/IP之上的一个协议层，是基于HTTP标准并对TCP传输数据时进行加密，所以HPPTS是HTTP+SSL/TCP的简称。  

## TLS
由于HTTPS的推出受到了很多人的欢迎，在SSL更新到3.0时，IETF对SSL3.0进行了标准化，并添加了少数机制，标准化后的IETF更名为TLS1.0(Transport Layer Security 安全传输层协议)，可以说TLS就是SSL的新版本3.1。可以说TLS是更为安全的升级版 SSL。  

## HSTS
HSTS(HTTP Strict Transport Security)是一套由互联网工程任务组发布的互联网安全策略机制。HSTS的作用是强制客户端（如浏览器）使用HTTPS与服务器创建连接。  
HSTS可以用来抵御SSL剥离攻击。SSL剥离攻击是中间人攻击的一种，由Moxie Marlinspike于2009年发明。SSL剥离的实施方法是阻止浏览器与服务器创建HTTPS连接。它的前提是用户很少直接在地址栏输入https://，用户总是通过点击链接或3xx重定向，从HTTP页面进入HTTPS页面。所以攻击者可以在用户访问HTTP页面时替换所有`https://`开头的链接为`http://`，达到阻止HTTPS的目的。  

In TLS, the client proposes and the server chooses. HSTS allows a server to force clients to use HTTPS for a particular domain.

## Reference
[SSL，HTTPS，TLS三者的区别](https://zhuanlan.zhihu.com/p/158711125)  
[HTTP Strict Transport Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)  
[Is there a HSTS equivalent for specifying TLS version?](https://security.stackexchange.com/questions/100093/is-there-a-hsts-equivalent-for-specifying-tls-version)