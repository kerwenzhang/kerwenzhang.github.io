---                                  
layout: post                                  
title: "WCF Discovery UDP 广播调查"                                  
date:   2018-12-10 9:00:00                                   
categories: "WCF"                                  
catalog: true                                  
tags:                                   
    - WCF                                  
---                        
    
## Set TTL  

We were able to get WCF discovery working across networks. Basically we had to increase the TimeToLive in WCF to be more than the default of 1. Here is a more detailed explanation from our network consultant:  

The standard TTL for the WS-Discovery packets from WCF are 1. By increasing this to a larger number, and enabling sparse-dense PIM on the correct SVIs on layer 3 switch configured as a the RP, multicast routing allows the WS-Discovery protocol to traverse multiple subnets on a larger enterprise level. This will NOT work through NAT, firewall, etc – it will only work between actual routed subnets (though it should work through an IPsec encrypted VTI with properly configured IP and multicast routing protocols).  

[https://serverfault.com/a/619825](https://serverfault.com/a/619825)  

## Explain

This is not a firewall issue but normal behavior of WS-Discovery. WS-Discovery uses SOAP-over-UDP sent to multicast IP group (239.255.255.250). And multicast packets generally are not routed and stay within limits of local network. Thus DiscoveryClient cannot discover services on other network without external help.

You have two options:

Configure your routers to pass multicast IP traffic between each other. While it is fairly easy to achieve it may load your inter-network link unnecessarily and it also may require help from your ISP or you may need tunneling of some sort.
Set up what is known as "Discovery Proxy" on the network where discoverable services are. Discovery Proxy basically performs discovery locally and then uses HTTP to deliver discovery results to other networks. As Discovery Proxy has the same SOAP WSDL existing WS-Discovery clients may use it without any changes over internet.

[https://stackoverflow.com/questions/43406764/wcf-udp-discovery-on-other-network](https://stackoverflow.com/questions/43406764/wcf-udp-discovery-on-other-network)

## UDDI

[https://forums.asp.net/t/2034544.aspx?WCF+and+WS+Discovery+across+network+segments](https://forums.asp.net/t/2034544.aspx?WCF+and+WS+Discovery+across+network+segments)
[https://www.codeproject.com/Articles/32476/Integrating-WCF-Services-into-UDDI-based-enterpris](https://www.codeproject.com/Articles/32476/Integrating-WCF-Services-into-UDDI-based-enterpris)

## Explain

[https://stackoverflow.com/a/49947754/7352168](https://stackoverflow.com/a/49947754/7352168)

## UPnP

[https://support.videotec.com/hc/en-gb/articles/217116646-Discovery-methods-supported-by-ONVIF-devices](https://support.videotec.com/hc/en-gb/articles/217116646-Discovery-methods-supported-by-ONVIF-devices)

## UDP 单播、广播和多播

[UDP 单播、广播和多播](https://www.cnblogs.com/jingliming/p/4477264.html)

[UDP 多播实例](http://www.jarloo.com/c-udp-multicasting-tutorial/)

## WCF Discovery UDP 组播地址


239.255.255.250:3702

[NET 4.0 : Enabling WCF service for discovery (Discovery Part III)](https://developers.de/blogs/damir_dobric/archive/2008/11/27/net-4-0-enabling-wcf-service-for-discovery.aspx)