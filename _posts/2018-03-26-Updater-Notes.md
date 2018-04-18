---     
layout: post     
title: "Updater work notes"     
date:   2018-3-26 14:30:00      
categories: "C#"     
catalog: true     
tags:      
    - C#     
---     
     
    
1. IIS enable net.tcp 协议   
Right click on application, manage application -> Advanced setting   
service change to "http,net.tcp"   
   
2. Database does not have privilege to write   
Modify database file and its folder's privilege setting   
   
3. Library project could not set config   
Refrence [C# library project 不支持](http://kerwenzhang.github.io/c%23/2018/03/15/C-library-config/)   
   
4. SQLite binary 版本不兼容, release, debug 加新的配置   
调用SQLite binary，有时会提示版本兼容问题，需要修改project的配置文件，在release和debug下加入以下配置：   
   
5. IIS does not need to set notify port   
在使用WCF service时，需要进行服务器地址配置，需要加端口号，但如果选择用IIS托管，可以省略端口号。IIS 可以自己管理。   
   
6. windows service install, use InstallUtil.exe   
打开VS2017 command 窗口   
InstallUtil.exe UpdateServiceAgent.exe   
InstallUtil.exe -u UpdateServiceAgent.exe   
   
7. NuGet package restore failed for project PCDCInterface: Unable to find version '1.0.0.3' of package 'Newtonsoft.Json'.   
Solution: PCDCInterface need the libraies of Json during compile, please copy 'packages' to the root of solution   
   
8. WPF ContextMenu MenuItem binding command does not work   
Solution: [Check this](https://stackoverflow.com/questions/3583507/wpf-binding-a-contextmenu-to-an-mvvm-command)   
    a. Create a proxy class   
    b. Add proxy binding to resource    
    c. Modify ContextMenu  
	
9. How to show text in Progress bar  

10. Button in DataGrid binding command does not work  

11. How to popup context menu when click left mouse  