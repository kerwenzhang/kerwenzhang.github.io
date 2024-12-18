---                
layout: post                
title: "WCF 安全设置"                
date:   2019-6-20 16:30:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      
  
WCF服务的安全性包括两个主要要求： 传输安全和授权. 传输安全包括身份验证（验证服务和客户端的标识）、保密性（消息加密）和完整性（进行数字签名以检测是否存在篡改）。 授权是控制对资源的访问，例如仅允许特权用户读取文件。

## 基本知识
安全依赖于凭据 。 凭据用于证明实体是否属实。 例如，服务的客户端发出声明的标识，和凭据用于证明该声明以某种方式。 在典型方案中，会发生凭据交换。 首先，某服务将对其标识发出声明，并使用凭据向客户端证明该标识。 同样，客户端也将对某标识发出声明，并向该服务出具凭据。 如果双方都信任对方的凭据，则可以建立安全上下文 ，在此上下文中，将以保密方式对所有消息进行交换，并且所有消息都将进行签名以保护其完整性。

如果客户端和服务计算机都位于需要二者登录到网络的 Windows 域中，则凭据将由 Windows 基础结构来提供。在 Windows 系统上，授权的工作方式是将每个计算机和用户分配到一个角色和组的集合中。  

Internet 环境并没有一个控制器来管理随时登录的成百上千万的用户， 而是在其凭据中最常采用 X.509 证书（也称为安全套接字层 (SSL) 证书）的形式。 这些证书通常由证书颁发机构 颁发，证书颁发机构可以是担保证书以及将向其颁发证书的人员的真实性的第三方公司。 若要在 Internet 上公开服务，还必须提供这样一个受信任的证书来对服务进行身份验证。

## 传输安全性

传输安全性包含三项主要安全功能：完整性、保密性和身份验证。 完整性是检测消息是否被篡改的能力。 保密性是能够保留一条消息的预期接收者以外的任何人无法读取这通过加密技术来实现。 身份验证是能够验证已声明的标识。 将这三项功能结合在一起，有助于确保消息安全地从一个点到达另一个点。WCF采用两种不同的机制来解决这三个涉及到传输安全的问题，我们一般将它们称为不同的安全模式，即Transport安全模式和Message安全模式。    

在WCF可以将传输安全模式设置成以下几种：  
1. None - 不设置任何安全模式  
2. Message - 使用 SOAP 消息安全提供安全性。  
使用 Ws-security （和其他规范），将对 SOAP 正文进行加密和签名。 Message模式不依赖于传输协议。服务端需要指定服务端证书，用来加密服务端和客户端相互传送的消息。  
消息模式通过在每条消息中都包含安全数据来提供安全保障。 使用 XML 和 SOAP 安全标头时，每条消息中都包含确保消息的完整性和保密性所需要的凭据及其他数据。 每条消息都包含安全数据时，由于必须逐一处理每条消息，因此将导致性能下降。  
消息安全相对于传输安全的一个优势就是：更为灵活。 即，安全要求不由传输协议确定。 您可以使用任何类型的客户端凭据来保证消息的安全 

3. Transport - 使用 TLS over TCP 或 SPNego 提供传输安全性。   
此服务可能需要使用 SSL 证书进行配置。 可以通过此模式来控制保护级别。  
当选择传输模式来保证安全时，您要选择使用该协议所指示的机制。 例如，如果您选择 WSHttpBinding 类并将其安全模式设置为“传输”，则您要选择基于 HTTP 的 SSL (HTTPS) 作为安全机制。 传输模式的好处在于它比消息模式更为高效，原因是其安全是在相对较低的级别进行集成的。 使用传输模式时，必须根据传输规范实现安全机制，这样消息才能通过传输在各点之间安全流动。  
一般说来，传输安全的主要优点是它提供了较高的吞吐量，而无论您使用哪种传输协议。 但是，它确实有两个限制：第一种是传输机制决定了用于对用户进行身份验证的凭据类型。 只有当服务需要与其他要求不同类型凭据的服务交互操作时，这才是一个缺点。 第二个限制是，因为安全不是在消息级应用的，所以安全是逐个跃点实现的，而不是以端对端方式实现的。 

4. TransportWithMessageCredential - 传输安全性与消息安全性结合使用。传输安全用于有效确保每条消息的保密性和完整性。 同时，每条消息都包含其凭据数据，这使得可以对消息进行身份验证。   
使用 TLS over TCP 或 SPNego 提供传输安全性，传输安全性可确保完整性、保密性和服务器身份验证。 SOAP 消息安全性提供客户端身份验证。 

## Transport安全模式   

### SSL, TLS和HTTPS

SSL（Secure Sockets Layer）最初是由Netscape公司开发的一种安全协议，应用于Netscape浏览器以解决与Web服务器之间的安全传输问题。SSL先后经历了三个主要的版本，即1.0、2.0和3.0。之后SSL被IETF （Internet Engineering Task Force）接管，正是根名为TLS（Transport Layer Security）。可以这么说，SSL是TLS的前身，TLS 1.0相当于SSL 3.1。  
TLS/SSL本身是和具体的网络传输协议无关的，既可以用于HTTP，也可以用于TCP。  

HTTPS（Hypertext Transfer Protocol Secure）则是将HTTP和TLS/SSL两者结合起来。在一般情况下，HTTPS通常采用443端口进行通信。对于WCF来说，所以基于HTTP协议的绑定的Transport安全都是通过HTTPS来实现的。而NetTcpBinding和NetNamedPipeBinding也提供了对TLS/SSL的支持，一般我们将TLS/SSL在TCP上的应用称为SSL Over TCP。  

TLS/SSL帮助我们解决两个问题：客户端对服务端的验证，以及通过对传输层传输的数据段（Segment）进行加密确保消息的机密性。  

优点：  
高性能。虽然TLS/SSL在正式进行消息交换之前需要通过协商建立一个安全的连接，但是这个协商过程完全通过传输层协议来完成。而且这种安全模式还可以充分利用网络适配器的硬件加速，这样就可以减少CPU时间，进而提供性能。  

缺点：  
1. Transport安全模式依赖于具体的传输协议；  
2. 它只能提供基于点对点（Point-to-Point）的安全传输保障，即客户端之间连接服务的场景。如果在客户端的服务端之间的网络需要一些用于消息路由的中间结点，Transport安全模式则没有了用武之地。  
3. 在Transport安全模式下，意味着我们不得不在传输层而不能在应用层解决对客户端的认证，这就决定了可供选择的认证方式不如Message模式多。   
由于上述的这些局限（主要还是只能提供点对点的安全传输保障），决定了Intranet是Transport安全模式主要的应用环境。

## Message安全模式

Transport安全模式将安全传输策略应用到传输层的数据段，进而间接地实现基于消息的安全传输。而Message模式则直接将安全策略的目标对象对准消息本身，通过对消息进行签名、加密实现消息安全传输。所以Message安全模式不会因底层是HTTP或者TCP传输协议而采用不同的安全机制，并且能够提供从消息最初发送端到最终接收端之间的安全传输，即端到端（End-To-End）安全传输。Message模式下的安全协议是一种应用层协议，我们可以在应用层上实现对客户端的验证，因而具有更多的认证解决方案的选择。  

优点： 
1. 由于Message安全模式是通过在应用层通过对消息实施加密、签名等安全机制实现的，所以这是一种于具体传输协议无关的安全机制，不会因底层采用的是TCP或者HTTP而有所不同。较之Transport安全，这种基于应用层实现的安全机制在认证方式上具有更多的选择；  
2. 由于Message安全模式下各种安全机制都是直接应用在消息（SOAP）级别的，无论消息路由的路径有多复杂，都能够保证消息的安全传输。所以，不同于Transport安全模式只能提供点对点（Point-to-Point）的安全，Message安全模式能够提供端到端（End-to-End）安全；  
3. 由于Message安全模式是对WS-Security、WS-Trust、WS-SecureConversation和WS-SecurityPolicy这四个WS-*规范的实现，所有具有很好的互操作性，能够提供跨平台的支持。  

缺点：
性能  

## 凭证
认证是确定被认证方的真实身份和他或她申明（Claim）的身份是否相符的行为。认证方需要被认证方提供相应的身份证明材料，以鉴定本身的身份是否与声称的身份相符。在计算机的语言中，这里的身份证明有一个专有的名称，即“凭证（Credential）”，或者用户凭证（User Credential）、认证凭证（Authentication Credential）。  
WCF支持一系列不同类型的用户凭证，以满足不同认证需求。  

### 用户名/密码认证

如果你选择了用户名/密码凭证，WCF为你提供了三种认证模式：  
 
1. 将用户名映射为Windows帐号，采用Windows认证；  
2. 采用ASP.NET的成员资格（Membership）模块  
3. 通过继承UserNamePasswordValidator，实现自定义认证。  

### Windows认证  
集成Windows认证（IWA：Integrated Windows Authentication）是仅次于用户名/密码的认证方式。尤其是在基于Windows活动目录（AD：Active Directory）的Intranet应用来说，Windows认证更是成为首选。    
Windows是实现单点登录（SSO：Single Sign-On）最理想的方式。无论是采用域（Domain）模式还是工作组（Workgroup）模式，只要你以Windows帐号和密码登录到某一台机器，你就会得到一个凭证。在当前会话超时之前，你就可以携带该Windows凭证，自动登录到集成了Windows认证方式的所有应用，而无须频繁地输入相同的Windows帐号和密码。如果登录帐号不具有操作目标应用的权限，在一般情况下，你好可以通过重新输入Windows帐号和相应的密码（如果当前用户具有多个Windows帐号）以另外一个身份（该身份具有对目标应用进行操作的访问权限）对目标应用进行操作。  

Windows具有两种不同的认证协议，即NTLM（NT LAN Manager）和Kerberos。  

### X.509证书  
对于消息交换来说，通过非对称的方式对消息进行加密是能够确保消息的机密性。具体的做法是：消息的发送方采用接收方的公钥进行加密，接收方通过自己的私钥进行解密。由于私钥仅供接收方所有，所有其他人不能对密文进行解密。  

## ProtectionLevel 
ProtectionLevel 属性出现在多个特性类（如 ServiceContractAttribute 和 OperationContractAttribute 类）中。 保护级别是一个值，它指定了支持服务的消息（或消息部分）是进行签名、签名并加密，还是未经签名或加密即发送。
## 凭据类型

### 传输凭据类型
None	指定客户端不需要提供任何凭据。 这相当于匿名客户端。  
Basic	为客户端指定基本身份验证。   
摘要	为客户端指定摘要式身份验证。   
Ntlm	指定 NT LAN Manager (NTLM) 身份验证。   
Windows	指定 Windows 身份验证。   
证书	使用 X.509 证书执行客户端身份验证。  
Password	用户必须提供用户名和密码。 使用 Windows 身份验证或其他自定义解决方案验证用户名/密码对。  

### 消息客户端凭据类型

None	指定客户端不需要提供凭据。 这相当于匿名客户端。  
Windows	允许在使用 Windows 凭据建立的安全上下文中交换 SOAP 消息。  
用户名	允许服务可以要求使用用户名凭据对客户端进行身份验证。 请注意，WCF 不允许使用用户名称，例如生成签名或加密数据的任何加密操作。 WCF 可确保传输的安全性时使用用户名凭据。  
证书	允许服务可以要求使用 X.509 证书对客户端进行身份验证。  
已颁发的令牌	根据安全策略配置的自定义令牌类型。 默认令牌类型为安全断言标记语言 (SAML)。 令牌由安全令牌服务颁发。 有关详细信息，请参阅联合身份验证和颁发令牌。


## 业界级安全规范
#### 公钥基础结构

公钥基础结构 (PKI) 是一种由数字证书、证书颁发机构以及其他注册机构所组成的系统，旨在通过使用公钥加密对电子事务中所涉及的各方进行检验和身份验证。 有关详细信息，请参阅Windows Server 2008 R2 证书服务。

#### Kerberos 协议
Kerberos 协议是一种规范，用于创建一种安全机制来对 Windows 域上的用户进行身份验证。 它允许用户建立针对域中的其他实体的安全上下文。 Windows 2000 及版本更高的平台默认情况下使用 Kerberos 协议。 在创建将与 intranet 客户端进行交互的服务时，理解系统的机制非常有用。 此外，由于Web 服务安全 Kerberos 绑定的广泛发布，可以使用 Kerberos 协议与 Internet 客户端通信 （即 Kerberos 协议是可互操作）。 有关如何在 Windows 中实现 Kerberos 协议的详细信息，请参阅Microsoft Kerberos。

#### X.509 证书
X.509 证书是安全应用程序中使用的主要凭据形式。 有关详细信息 X.509 证书请参阅X.509 公钥证书。 X.509 证书存储在证书存储区中。 运行 Windows 的计算机有多种证书存储区，每一种都针对不同的用途。 有关不同存储区的详细信息，请参阅证书存储区。

## 传输安全方案
使用 WCF 传输安全的常见方案包括：
1. 使用 Windows 确保传输安全。 WCF 客户端和服务部署在 Windows 域 （或 Windows 林） 中。 消息包含个人数据，因此要求客户端和服务相互进行身份验证，要求实现消息完整性和消息保密性。 此外，还需要有已发生特定事务的证明，例如，消息的接收方应记录签名信息。
2. 使用 UserName 和 HTTPS 确保传输安全。 WCF 客户端和服务需要一些开发，以便通过 Internet 工作。 客户端凭据根据数据库（其中的内容为用户名/密码对）进行身份验证。 服务是用受信任的安全套接字层 (SSL) 证书部署在一个 HTTPS 地址的。 由于消息是通过 Internet 传输的，因此，客户端和服务需要相互进行身份验证，并且必须在传输过程中保持消息的保密性和完整性。
3. 使用证书确保传输安全。 WCF 客户端和服务需要一些开发，以便通过公共 internet 工作。 客户端和服务都具有可用于确保消息安全的证书。 客户端和服务通过 Internet 进行相互通信，执行要求消息完整性、保密性和相互身份验证的重要事务。

Reference:  
[Microsoft doc](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/securing-services)     
[WCF安全系列 二 - netTCPBinding绑定之Transport安全模式](https://www.cnblogs.com/chnking/archive/2008/10/07/1305891.html)    
[WCF安全系列 三 - netTCPBinding绑定之Message安全模式](http://www.cnblogs.com/chnking/archive/2008/10/15/1312120.html)   

[WCF安全之X509证书](https://www.cnblogs.com/viter/archive/2009/07/02/x509.html)   

[常用安全方案](https://docs.microsoft.com/zh-cn/dotnet/framework/wcf/feature-details/common-security-scenarios)   

[WCF安全系列 - 从两种安全模式谈起](https://www.cnblogs.com/artech/archive/2011/05/22/authentication_01.html)  
[WCF安全系列认证与凭证：用户名/密码认证与Windows认证](https://www.cnblogs.com/artech/archive/2011/05/23/authentication_021.html)  
[WCF安全系列认证与凭证：X.509证书](https://www.cnblogs.com/artech/archive/2011/05/23/authentication_022.html)  