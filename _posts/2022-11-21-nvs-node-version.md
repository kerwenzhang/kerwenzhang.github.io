---
layout: post
title: 使用NVS管理node版本
date:   2022-11-21 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

在开发过程中可能需要切换node的版本，目前有 nvm、n 等方案，我们推荐跨平台的 nvs。  
# 安装

访问 [nvs/releases](https://github.com/jasongin/nvs/releases) 下载最新版本的 nvs.msi，然后双击安装即可。 

# 使用  

`nvs ls-remote` 列出所有可用的nvs版本  
`nvs add <version>` 下载指定版本，如 nvs add 16、nvs add 16.14    
`nvs add lts`  安装最新的 LTS 版本  
`nvs ls` 查看已安装的版本  
`nvs use <version>` 切换到指定版本  
`nvs link <version>` 定默认的版本，关掉当前cmd窗口之后default仍然有效  
`nvs rm <version>` 删除指定版本  

node 会被下载到下边这个文件夹下

    %LOCALAPPDATA%\nvs\node\

 我们也可以从nodejs官网上直接下载某个特定版本的zip包，然后解压到这个文件夹下。  