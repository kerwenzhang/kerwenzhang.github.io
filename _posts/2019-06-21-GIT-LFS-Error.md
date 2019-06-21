---                
layout: post                
title: "GIT error: Encountered 7 file(s) that should have been pointers, but weren't"                
date:   2019-6-21 9:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      
  
最近公司开始转用GitLab做代码存储， 在使用的过程中遇到以下问题：
1. Clone一个代码库
2. 不修改任何东西，直接在git bash里面 `git status`， 发现有几个dll文件显示modified
3. 使用`Git checkout .` 弹出以下提示

        Encountered 7 file(s) that should have been pointers, but weren't:  
        ...  
        ...  

解决方法：

    git rm --cached -r .

    git reset --hard

    git rm .gitattributes

    git reset .

    git checkout .