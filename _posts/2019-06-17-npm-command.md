---                                  
layout: post                                  
title: "npm 命令行"                                  
date:   2019-06-17 9:00:00                                   
categories: "Web"                                  
catalog: true                                  
tags:                                   
    - Web                                  
---                        
    
1. npm init可自动创建package.json文件
2. npm install  
   自动将package.json中的模块安装到node-modules文件夹下

3. 将所有module升到最新版本

        npm i -g npm-check-updates
        ncu -u
        npm install

4. 提升安装速度 

        npm install --prefer-offline --no-audit --progress=false