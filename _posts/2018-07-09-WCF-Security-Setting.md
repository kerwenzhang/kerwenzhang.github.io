---                
layout: post                
title: "WCF Security Setting"                
date:   2018-7-9 16:30:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      
  
在NetTcpBinding中可以将安全模式设置成以下几种：
None - 不设置任何安全模式
Message - 使用 SOAP 消息安全提供安全性。 默认情况下，将对 SOAP 正文进行加密和签名。 Message模式不依赖于传输协议。服务端需要指定服务端证书，用来加密服务端和客户端相互传送的消息。
Transport - 使用 TLS over TCP 或 SPNego 提供传输安全性。 此服务可能需要使用 SSL 证书进行配置。 可以通过此模式来控制保护级别。
TransportWithMessageCredential - 传输安全性与消息安全性结合使用。 使用 TLS over TCP 或 SPNego 提供传输安全性，传输安全性可确保完整性、保密性和服务器身份验证。 SOAP 消息安全性提供客户端身份验证。 

  
[WCF安全系列 二 - netTCPBinding绑定之Transport安全模式](https://www.cnblogs.com/chnking/archive/2008/10/07/1305891.html)
[WCF安全系列 三 - netTCPBinding绑定之Message安全模式](http://www.cnblogs.com/chnking/archive/2008/10/15/1312120.html)