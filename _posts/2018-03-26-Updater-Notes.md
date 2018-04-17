---  
layout: post  
title: "WFC lean notes"  
date:   2018-3-26 14:30:00   
categories: "C#"  
catalog: true  
tags:   
    - C#  
---  
  
 
1. IIS enable net.tcp 协议

2. Database does not have priviledge to write

3. Library project could not set config

4. SQLLite binary 版本不兼容, release, debug 加新的配置

5. IIS does not need to set notify port

6. windows service install, use InstallUtil.exe

7. NuGet package restore failed for project PCDCInterface: Unable to find version '1.0.0.3' of package 'Newtonsoft.Json'.
Solution: PCDCInterface need the libraies of Json during compile, please copy 'packages' to the root of solution

8. WPF ContextMenu MenuItem binding command does not work
Solution: [Check this](https://stackoverflow.com/questions/3583507/wpf-binding-a-contextmenu-to-an-mvvm-command)
    a. Create a proxy class
    b. Add proxy binding to resource
    c. Modify ContextMenu