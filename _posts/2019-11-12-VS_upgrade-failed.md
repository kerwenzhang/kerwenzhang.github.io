---                
layout: post                
title: "VisualStudio 升级过程中提示root node is not in the package collection.
" 
date:   2019-11-12 15:30:00                 
categories: "VS"                
catalog: true                
tags:                 
    - VS                
---      

升级Visual Studio 2017 到 15.9.16版本时，冒出以下提示：  

    Setup operation failed: The root node "Microsoft.VisualStudio.Product.Professional,version=15.0.26403.7" is not in the package collection.

解决方案：  
Please follow the cleanup steps and retry your VS install

See if you have this file on your machine: "%programfiles(x86)%\Microsoft Visual Studio\Installer\resources\app\layout\InstallCleanup.exe"
If so, please launch it from an admin command prompt with a -full param:

    InstallCleanup.exe -full

If not, please manually delete the "%programfiles(x86)%\Microsoft Visual Studio\Installer” folder
Relaunch the newly downloaded vs_enterprise.exe (or vs_professional.exe or vs_community.exe…)
Allow the first step to install the installer
Once the installer comes up and you can see workload choices (.net desktop and the like), close it
Go launch the same InstallCleanup.exe to clean up old build of VS

Then relaunch vs_enterprise.exe and install VS
