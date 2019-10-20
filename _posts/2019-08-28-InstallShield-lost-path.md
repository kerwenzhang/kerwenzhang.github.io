---                
layout: post                
title: "InstallShield升级后Merge Module路径丢失"                
date:   2019-8-15 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

最近在把InstallShield从2014 升级到2015， 升级后打开安装工程文件，编译时提示找不到merge module。   
查看发现自己添加的merge module都找不到路径了。  
解决办法：  
InstallShield会将merge module的search path记录在注册表

    HKEY_CURRENT_USER\Software\InstallShield\Version\Professional\Project Settings\MMSearchPath  

升级2015后，需要将2014注册表中自定义的search path拷贝到2015注册表中。注意不要改变2015中原有的search path。    
