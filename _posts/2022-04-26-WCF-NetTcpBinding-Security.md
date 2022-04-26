---                
layout: post            
title: "WCF使用NetTCPBinding安全研究"                
date:   2022-4-26 17:30:00                 
categories: "WCF"                
catalog: true                
tags:                 
    - WCF                
---      


        <security mode="Message/None/Transport/TransportWithCredential">
            <transport clientCredentialType="Basic/Certificate/Digest/None/Ntlm/Windows"
                        protectionLevel="None/Sign/EncryptAndSign" 
                        sslProtocols="Tls|Tls11|Tls12"/>
            <message algorithmSuite="Basic128/Basic192/Basic256/Basic128Rsa15/Basic256Rsa15/TripleDes/TripleDesRsa15/Basic128Sha256/Basic192Sha256/TripleDesSha256/Basic128Sha256Rsa15/Basic192Sha256Rsa15/Basic256Sha256Rsa15/TripleDesSha256Rsa15"
                    clientCredentialType="Certificate/IssuedToken/None/UserName/Windows" />
        </security>

## Security mode - Transport	
Transport security is provided using TLS over TCP or SPNego. The service may need to be configured with SSL certificates. It is possible to control the protection level with this mode.    

How to config SSL certificate if set mode to "Transport"



[security of netTcpBinding](https://docs.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/wcf/security-of-nettcpbinding)   
[transport of netTcpBinding](https://docs.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/wcf/transport-of-nettcpbinding)  
[WCF NetTcpBinding Security - how does it work?](https://stackoverflow.com/q/2536522/7352168)  
[Is SSL for WCF needed when using Transport Security?](https://stackoverflow.com/a/6114626/7352168)  
[Transport Security with Windows Authentication](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/transport-security-with-windows-authentication)  
