---                              
layout: post                              
title: "开机启动程序"                              
date:   2018-9-18 14:00:00                               
categories: "Others"                              
catalog: true                              
tags:                               
    - Others                              
---                    
    
如果想开机用户登录后运行程序，可以放在Startup里面或者注册表里面：    
start >> all programs >> right-click startup >> open >> right click batch file >> create shortcut >> drag shortcut to startup folder.    
或者    
    
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run    
    
Here you can create a string. As name you can choose anything and the data is the full path to your file.    
    
如果想开机就启动程序，不需要用户登录，可以通过Task Scheduler的方式来实现    
    
Log in with an Administrator account    
Click on start and type “Task Scheduler” and hit return    
Click on “Task Scheduler Library”    
Click on “Create New Task” on the right hand side of the screen and set the parameters as follows:    
a. Set the user account to SYSTEM    
b. Choose "Run with highest privileges"    
c. Choose the OS for Windows7    
Click on “Triggers” tab and then click on “New…” Choose “At Startup” from the drop down menu, click Enabled and hit OK    
Click on the “Actions tab” and then click on “New…” If you are running a .bat file use cmd full path as the program(c:\widnows\system32\cmd.exe). Then input "/c <your bat file path>" In the Add arguments field    
Click on “OK” then on “OK” on the create task panel and it will now be scheduled.    
Add the .bat script to the place specified in your task event.    
Enjoy.