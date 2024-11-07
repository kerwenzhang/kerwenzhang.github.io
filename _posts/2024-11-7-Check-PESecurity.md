---
layout: post
title: "怎么检查exe是否enable了SAFESEH"
date: 2024-11-07 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

1. 克隆这个repo [PESecurity](https://github.com/NetSPI/PESecurity)   
2. 开一个powershell窗口，导入该模块

        Import-Module .\Get-PESecurity.psm1

3. 在Powershell里调用该模块检查文件PE属性

        Get-PESecurity -file C:\Windows\System32\kernel32.dll
        Get-PESecurity -directory C:\Windows\System32\

# Reference
[PESecurity](https://github.com/NetSPI/PESecurity)    