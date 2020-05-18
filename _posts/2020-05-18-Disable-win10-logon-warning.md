---                
layout: post                
title: "Disable Win10 logon warning message" 
date:   2020-05-18 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

在做Local build的时候需要切换语言之后重启机器。重启机器之后发现windows没有办法自动登录，加了自动登录也没起作用。 研究之后发现是因为IT在登录界面上加了一个warning信息，每次登录的时候需要点确认才能登录进去。 这个warning信息阻止了win10的自动登录。解决办法也很简单：
1. 开始菜单查找“secpol.msc”
2. 在Local Policies -> Security Options里找到下面这两个配置项：

    Interactive logon: Message text for users attempting to log on  
    Interactive logon: Message title for users...

将这两个配置项清空保存，重启就OK了。

[https://helpdeskgeek.com/how-to/add-a-message-to-the-logon-screen-for-users-in-windows/](https://helpdeskgeek.com/how-to/add-a-message-to-the-logon-screen-for-users-in-windows/)