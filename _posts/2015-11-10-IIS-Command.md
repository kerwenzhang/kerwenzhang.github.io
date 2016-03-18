---
layout: post
title: "Install IIS by commandline"
date:   2015-11-10 10:10:00 
categories: [IIS]
tags: [IIS, Commandline]
---
Install IIS by commandline:  
1. Open cmd window  
2. pkgmgr /norestart /iu:IIS-StaticContent;IIS-WebServerRole;IIS-WebServer;IIS-CommonHttpFeatures;IIS-DefaultDocument;IIS-ApplicationDevelopment;IIS-NetFxExtensibility;IIS-NetFxExtensibility45;IIS-ASPNET;IIS-ASPNET45;IIS-ISAPIExtensions;IIS-ISAPIFilter;NetFx4Extended-ASPNET45;IIS-Security;IIS-RequestFiltering;IIS-WebServerManagementTools;IIS-ManagementConsole;IIS-ManagementScriptingTools;IIS-ManagementService;IIS-IIS6ManagementCompatibility;IIS-Metabase;IIS-WMICompatibility;IIS-LegacyScripts;IIS-LegacySnapIn;IIS-WMICompatibility;WAS-WindowsActivationService;WAS-ProcessModel;WAS-NetFxEnvironment;WAS-ConfigurationAPI;WCF-HTTP-Activation  
/iu:后边跟的是IIS 组件，根据需要添加或者减少某个组件