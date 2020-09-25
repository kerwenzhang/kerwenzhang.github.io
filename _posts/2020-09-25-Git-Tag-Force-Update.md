---                
layout: post                
title: "Git 解决 would clobber existing tag 问题" 
date:   2020-09-25 10:30:00                 
categories: "Git"                
catalog: true                
tags:                 
    - Git                
---      

在用Git去更新代码的时候有遇到下面的问题：  

    > git pull --tags origin master
    From https://github.com/MY/REPO
    * branch            master     -> FETCH_HEAD
    ! [rejected]        latest     -> latest  (would clobber existing tag)
    9428765..935da94  master     -> origin/master

原因是我删了原有的一个tag，然后重新创建了一个相同名字的。  
解决方案：  

    git fetch --tags -f

强制刷新一下本地的tags

[https://stackoverflow.com/questions/58031165/how-to-get-rid-of-would-clobber-existing-tag](https://stackoverflow.com/questions/58031165/how-to-get-rid-of-would-clobber-existing-tag)