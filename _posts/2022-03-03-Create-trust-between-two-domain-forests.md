---                
layout: post            
title: "Create trust between two domain forests"                
date:   2022-3-3 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

正常情况下一个domain的机器或者账号只能在本domain使用，拿到另外一个domain是不受信任的。因为产品需求，调查了下如何让两个domain能互相认证，domain1的账号也能在domain2内正常使用。  

# Prepare two domains

1. Prepare two domain servers, for example: the first one Windows Server 2016, the second one Windows Server 2019.   
Note: if you are using vm, please make sure they are cloned from different template. Two vms which clone from same template will share same SID even after you rename the computer. This will lead to error when create trust. Use the PSTool to get the SIDs of two servers, make sure they are different.   
2. Rename them:  
Windows Server 2016 -> DomainServer1  
Windows Server 2019 -> DomainServer2  
3. Upgrade DomainServer1 to domain server  
   - Go to Server Manager, select “Manage” -> “Add Roles and Features”  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/1.png?raw=true)

   - Use default option “Role-based or feature-based installation”.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/2.png?raw=true)

   - Use default option “Select a server from the server pool”.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/3.png?raw=true)

   - Select checkbox “Active Directory Domain Services”  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/4.png?raw=true)

   - Popup a confirm dialog, click “Add Features”  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/5.png?raw=true)

   - It will take few minutes to complete installation.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/6.png?raw=true)

   - After install complete, click “Promote this server to a domain controller”.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/7.png?raw=true)

   - Select option “Add a new forest”, change domain name to “Updater1.domain”.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/8.png?raw=true)

   - Input password and confirm  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/9.png?raw=true)

   - Will generate NetBIOS domain name automatically, keep default.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/10.png?raw=true)

   - Keep default setting, Next  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/11.png?raw=true)

   - Will run prerequisites check, if all passed, click “Install”.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/12.png?raw=true)

   - After reboot, check the full computer name and domain name.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/13.png?raw=true)  

4. Similar steps to upgrade DomainServer2 to domain server.  
    After complete:  
    DomainServer1.Updater1.domain(10.224.106.208)  
    DomainServer2.Updater2.domain(10.224.110.245)  

# Create trust between domains

1. Ping each other, make sure the two servers can ping each other successfully.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/14.png?raw=true)
2. Add second DNS Server  
    On DomainServer1:  
   - Go to Control Panel -> Network and Sharing Center  
   - Select your Ethernet connections, select property and config IPV4  
   - Input the second DNS ip address  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/15.png?raw=true)
    On DomainServer2, similar steps to config second DNS.  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/16.png?raw=true)
3. Create stub zone in DNS  
    On DomainServer1:  
   - Open Server Manager, Tools -> DNS  
 ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/17.png?raw=true)
   - Right click on “Forward Lookup Zones”, select “New Zone…”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/18.png?raw=true)
   - Select “Stub zone” and Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/19.png?raw=true)
   - Select “To all DNS … forest”, Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/20.png?raw=true)
   - Input domain name “Updater2.domain”.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/21.png?raw=true)
   - Input the ip address of Updater2.domain  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/22.png?raw=true)
   - Display below success dialog.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/23.png?raw=true)
   - You should be able to successful ping Updater2.domain now.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/24.png?raw=true)
  
    On DomainServer2, similar steps to config DNS.  

4. Create trust  
    On DomainServer1:  
   - Open “Server Manager”, select “Tools” -> “Active Directory Domains and Trusts”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/25.png?raw=true)
   - Right click on “Updater1.domain”, select “Properties”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/26.png?raw=true)
   - Go to “Trusts” tab, click “New Trust”.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/27.png?raw=true)
   - Input domain name: “Updater2.domain”, Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/28.png?raw=true)
   - Select “Forest trust”, Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/29.png?raw=true)
   - Select “Two-way”, Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/30.png?raw=true)
   - Select “Both this domain and the specified domain”, Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/31.png?raw=true)
   - Input the user name and password of Updater2.domain  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/32.png?raw=true)
   - Select “Forest-wide authentication”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/33.png?raw=true)
   - Select “Forest-wide authentication”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/34.png?raw=true)
   - Next  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/35.png?raw=true)
   - Select “Yes, confirm the outgoing trust”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/36.png?raw=true)
   - Select “Yes, confirm the incoming trust”  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/37.png?raw=true)
   - Should display below success dialog.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/38.png?raw=true)
   - Could see the trusts have been created in outgoing and incoming.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/39.png?raw=true)
   - Go to DomainServer2, could see the trusts have been created automatically.  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Domain/40.png?raw=true)
   
# Verify

1. Prepare two windows client machines: Test1 and Test2  
2. Test1 join Updater1.domain, Test2 join Updater2.domain  
3. On Test1 machine, sign out and use domain2 account to logon  

If could logon, we have created trust between two domain forests.  

# Reference  
  
[Trust Relationship Between Two Forest](https://www.youtube.com/watch?v=F7DgXAXNnC8&ab_channel=TechiJack)  
[Cannot create Trust Relationship](https://social.technet.microsoft.com/Forums/lync/en-US/cc46715e-b36c-4473-a1bf-3367d1344f62/cannot-create-trust-relationship?forum=winserverDS)  
[How to get SID by PSTool](https://docs.microsoft.com/en-us/sysinternals/downloads/psgetsid#:~:text=If%20you%20want%20to%20see,and%20an%20optional%20computer%20name)   
