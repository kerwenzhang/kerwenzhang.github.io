---                                  
layout: post                                  
title: "How to create a IIS hosted WCF"                                  
date:   2018-10-30 14:00:00                                   
categories: "WCF"                                  
catalog: true                                  
tags:                                   
    - WCF                                  
---                        

## Create a new WCF Project
1. Open Visual Studio 2017 with Admin priviledage
2. File -> New -> Project
3. In "Visual C#" -> "WCF", select "WCF Service Library"
![open](https://raw.githubusercontent.com/kerwenzhang/kerwenzhang.github.io/master/_posts/image/per1.png)

## Host by IIS
1. Right click on solution, select "Add" -> "New project"  
2. Select "Visual C#" -> "Web" -> "Previous Versions" -> "WCF Service"  
![open2](https://raw.githubusercontent.com/kerwenzhang/kerwenzhang.github.io/master/_posts/image/per2.png)
3. Input project name and location, click "OK" button  
4. Delete "AppCode" and "AppData" folder   
5. Add WCF Service project in reference   
6. Modify svc file   
7. Add WCF configuration in Web.Config

## Setup IIS
1. Create a new application pool
2. Create new application under "Sites" -> "Default web site"
3. Modify folder access if you meet access deny issue.