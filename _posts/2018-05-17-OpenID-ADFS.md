---  
layout: post  
title: "OpenID 与 ADFS"  
date:   2018-5-17 13:30:00   
categories: "Others"  
catalog: true  
tags:   
    - Others  
---  
  


# Directory Services

目录服务器的主要功能是提供资源与地址的对应关系，比如你想找一台网上的共享打印机或主机时，你只需要知道名字就可以了，而不必去关心它真正的物理位置。而目录服务器帮助维护这样的资源-地址映射。  
目录服务是使目录中所有信息和资源发挥作用的服务，如用户和资源管理、基于目录的网络服务、基于网络的应用管理等！活动目录服务是将网络中的各种资源组合起来，进行集中管理，一方便网络资源的搜索，使企业可以轻松地管理复杂的网络环境。  

网络上，特别是互联网中有各型各类的主机。有各种各样的资源, 这些东西杂散在网络中,，需要有一定的机制来访问这些资源,，得到相关的服务， 于是就有了目录服务。  
DNS服务是典型的目录服务,即帮你做域名与IP地址之间的转换  
  
在WINDOWS体系中，AD(活动目录)功能强大，是符合工业标准的目录服务器。在UNIX或LINUX中，也有相应的目录服务器。   

# AD

活动目录（Active Directory）是面向Windows Standard Server、Windows Enterprise Server以及 Windows Datacenter Server的目录服务  
Active Directory存储了有关网络对象的信息，并且让管理员和用户能够轻松地查找和使用这些信息。Active Directory使用了一种结构化的数据存储方式，并以此作为基础对目录信息进行合乎逻辑的分层组织。  
活动目录(Active Directory)主要提供以下功能：  
1. 服务器及客户端计算机管理： 管理服务器及客户端计算机账户，所有服务器及客户端计算机加入域管理并实施组策略。  
2. 用户服务：管理用户域账户、用户信息、企业通讯录（与电子邮件系统集成）、用户组管理、用户身份认证、用户授权管理等，按省实施组管理策略。  
3. 资源管理：管理打印机、文件共享服务等网络资源。  
4. 桌面配置：系统管理员可以集中的配置各种桌面配置策略，如：用户使用域中资源权限限制、界面功能的限制、应用程序执行特征限制、网络连接限制、安全配置限制等。  
5. 应用系统支撑：支持财务、人事、电子邮件、企业信息门户、办公自动化、补丁管理、防病毒系统等各种应用系统。  


# ADFS

ADFS(Active Directory Federation Services) 活动目录联合服务  
联合身份验证（Federated Identity）是一种用户身份的验证方式，这种验证方式通过把用户身份的验证过程与被该用户访问的服务提供商（SP，Service Provider，如我们自己的站点）进行逻辑分离，在保证用户身份信息被隔离在用户所属系统的内部的同时，为受信任的服务提供商提供所需要的用户信息。
当服务提供商需要对用户的身份进行验证时，会将相关的验证过程转交给身份验证提供方（IdP，Identity Provider，如AvePoint域的 AD FS 验证服务），当用户经由身份验证提供方成功登录后，身份验证提供方会将用户的身份验证凭据和用户相关的信息返还给服务提供商，从而实现服务提供商对于用户身份的验证，以及对于用户信息获取。  
 
ADFS将活动目录拓展到Internet。要理解这一点，可以考虑一般活动目录设施的工作原理。当用户通过活动目录认证时，域控制器检查用户的证书。证明是合法用户后，用户就可以随意访问Windows网络的任何授权资源，而无需在每次访问不同服务器时重新认证。   
ADFS将同样的概念应用到Internet. 我们都知道Web应用访问位于SQL Server或其他类型后端资源上的后端数据。对后端资源的安全认证问题往往比较复杂。可以有很多不同的认证方法提供这样的认证。例如，用户可能通过RADIUS(远程拨入用户服务认证)服务器或者通过应用程序代码的一部分实现所有权认证机制。  
这些认证机制都可实现认证功能，但是也有一些不足之处。不足之一是账户管理。当应用仅被我们自己的员工访问时，账户管理并不是个大问题。但是，如果您的供应商、客户都使用该应用时，您会突然发现您需要为其他企业的员工建立新的用户账户。不足之二是维护问题。当其他企业的员工离职，雇佣新员工时，您需要删除旧的账户和创建新的账户。密码也是一个问题。一旦应用配置完成，您要不断的为那些甚至没有为您公司工作的人员重新修改密码。  


  
[Reference2](https://baike.baidu.com/item/ADFS/892989)  
[Reference3](https://blog.csdn.net/nista/article/details/49099921)


# oAuth   
OAUTH协议为用户资源的授权提供了一个安全的、开放而又简易的标准。与以往的授权方式不同之处是OAUTH的授权不会使第三方触及到用户的帐号信息（如用户名与密码），即第三方无需使用用户的用户名与密码就可以申请获得该用户资源的授权，因此OAUTH是安全的。oAuth是Open Authorization的简写。  
OAUTH协议为用户资源的授权提供了一个安全的、开放而又简易的标准。同时，任何第三方都可以使用OAUTH认证服务，任何服务提供商都可以实现自身的OAUTH认证服务，因而OAUTH是开放的。  

协议特点  
(1). 简单：不管是OAUTH服务提供者还是应用开发者，都很易于理解与使用；  
(2). 安全：没有涉及到用户密钥等信息，更安全更灵活；  
(3). 开放：任何服务提供商都可以实现OAUTH，任何软件开发商都可以使用OAUTH；  
  
[Reference4](https://baike.baidu.com/item/oAuth/7153134?fr=aladdin)  



# OpenID

OpenID 的创建基于这样一个概念：我们可以通过 URI （又叫 URL 或网站地址）来认证一个网站的唯一身份，同理，我们也可以通过这种方式来作为用户的身份认证。  
目前的网站都是依靠用户名和密码来登录认证，这就意味着大家在每个网站都需要注册用户名和密码，即便你使用的是同样的密码。如果使用 OpenID ，你的网站地址（URI）就是你的用户名，而你的密码安全的存储在一个 OpenID 服务网站上（你可以自己建立一个 OpenID 服务网站，也可以选择一个可信任的 OpenID 服务网站来完成注册）  

登录一个支持 OpenID 的网站非常简单（即便你是第一次访问这个网站也是一样）。只需要输入你注册号的 OpenID 用户名，然后你登录的网站会跳转到你的 OpenID 服务网站，在你的 OpenID 服务网站输入密码（或者其它需要填写的信息）验证通过后，你会回到登录的网站并且已经成功登录。  

除了一处注册，到处通行以外，OpenID 给所有支持 OpenID 的网站带来了价值—共享用户资源。用户可以清楚的控制哪些信息可以被共享，例如姓名、地址、电话号码等。
[Reference1](https://baike.baidu.com/item/OpenID/2267230?fr=aladdin)   

# OpenID Connect

OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows Clients to verify the identity of the End-User based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User in an interoperable and REST-like manner.  

# OpenID Connect VS OpenID 2.0

OpenID Connect performs many of the same tasks as OpenID 2.0, but does so in a way that is API-friendly, and usable by native and mobile applications. OpenID Connect defines optional mechanisms for robust signing and encryption. Whereas integration of OAuth 1.0a and OpenID 2.0 required an extension, in OpenID Connect, OAuth 2.0 capabilities are integrated with the protocol itself.   

# IETF  
国际互联网工程任务组（The Internet Engineering Task Force，简称 IETF） 成立于1985年底，是全球互联网最具权威的技术标准化组织，主要任务是负责互联网相关技术规范的研发和制定，当前绝大多数国际互联网技术标准出自IETF。  
IETF是一个由为互联网技术工程及发展做出贡献的专家自发参与和管理的国际民间机构。它汇集了与互联网架构演化和互联网稳定运作等业务相关的网络设计者、运营者和研究人员，并向所有对该行业感兴趣的人士开放。任何人都可以注册参加IETF的会议。  
IETF的主要任务是负责互联网相关技术标准的研发和制定，是国际互联网业界具有一定权威的网络相关技术研究团体。   
