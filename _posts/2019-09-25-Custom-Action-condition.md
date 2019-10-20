---                
layout: post                
title: "Custom Action condition"                
date:   2019-9-12 15:30:00                 
categories: "MSI"                
catalog: true                
tags:                 
    - MSI                
---      


Modify & Repair  

    Installed AND Not REMOVE

Only Install  

    NOT Installed AND NOT PATCH

initial installation only:

    NOT Installed    

Uninstall

    REMOVE

Install and repair

    NOT REMOVE

initial install or when repair is selected

    NOT Installed OR MaintenanceMode="Modify"

[InstallShield Condition](https://resources.flexera.com/web/pdf/archive/IS-CHS-Common-MSI-Conditions.pdf)