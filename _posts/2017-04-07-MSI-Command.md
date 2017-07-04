---
layout: post
title: "MSI Commandline"
date:   2017-04-07 13:07:00 
categories: "Others"
catalog: true
tags: 
    - Others
    - MSI
---



## MSI 输出log

    /L*V "C:\package.log"
    
## Admin安装

    msiexec /a foo.msi TARGETDIR=C:\EXTRACT\ /qn /norestart /l*v admin_install.log