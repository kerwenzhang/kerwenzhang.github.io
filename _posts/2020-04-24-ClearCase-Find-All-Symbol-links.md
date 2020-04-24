---                
layout: post                
title: "How to find all Symbolic links under a ClearCase Vob" 
date:   2020-04-24 10:30:00                 
categories: "Git"                
catalog: true                
tags:                 
    - Git                
---      

最近一直在做code迁移，发现ClearCase里面有很多Symbolic link，这些link是无法直接迁移到GitLab里。 首先要解决的是怎么发现所有的Symbolic link：

    cleartool ls -l -r <folder> | findstr /C:"symbolic link" >> SymbolicFiles.txt

Folder 必须是个VOB名或者VOB下的子Folder

[https://adventuresinscm.wordpress.com/2017/08/01/clearcase-windows-quick-tip-find-all-symbolic-links/](https://adventuresinscm.wordpress.com/2017/08/01/clearcase-windows-quick-tip-find-all-symbolic-links/)