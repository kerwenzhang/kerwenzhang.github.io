---                                  
layout: post                                  
title: "CEF shutdown"                                  
date:   2023-06-07 9:00:00                                   
categories: "CEF"                                  
catalog: true                                  
tags:                                   
    - CEF                                  
---                        

CVBCOMMCRT-3410

Root Cause:
1. We use C# winForm to create a instance of ChromiumWebBrower, the Application Exit event will be hooked in browser's static constructor. So Cef.Shutdown() will be called when application exit. This usually happens on main thread. [](https://github.com/cefsharp/CefSharp/blob/cefsharp/96/CefSharp.WinForms/ChromiumWebBrowser.cs#L254)
2. When call print, Trend control will call Microsoft API PrintDocument.Print() to save print data to file. This API will finally create a `StatusDialog ` using `Application.Run(dialog);`. When run complete, application will call 'RaiseExit' in dispose. That's leading to the CEF hook is called. As the print thread is not the main UI thread, so the CEF shutdown will crash.

Reference:
[ProductDocument source code](https://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/CommonUI/System/Drawing/Printing/PrintDocument@cs/1/PrintDocument@cs)  
[PrintController source code](https://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/CommonUI/System/Drawing/Printing/PrintController@cs/1/PrintController@cs)   
[printcontrollerwithstatusdialog and StatusDialog source code](http://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/WinForms/Managed/System/WinForms/Printing/PrintControllerWithStatusDialog@cs/1/PrintControllerWithStatusDialog@cs)  

[Application.cs source code](https://www.dotnetframework.org/default.aspx/4@0/4@0/DEVDIV_TFS/Dev10/Releases/RTMRel/ndp/fx/src/WinForms/Managed/System/WinForms/Application@cs/1305376/Application@cs)  



Solution:
Based on CEfSharp offical (http://cefsharp.github.io/api/87.1.x/html/P_CefSharp_CefSharpSettings_ShutdownOnExit.htm), considering we are handling CEF shutdown manually when FTView exit, we should set this property as false to disable hook application exit event 


[https://www.dotnetframework.org/default.aspx/4@0/4@0/DEVDIV_TFS/Dev10/Releases/RTMRel/ndp/fx/src/WinForms/Managed/System/WinForms/Application@cs/1305376/Application@cs](https://www.dotnetframework.org/default.aspx/4@0/4@0/DEVDIV_TFS/Dev10/Releases/RTMRel/ndp/fx/src/WinForms/Managed/System/WinForms/Application@cs/1305376/Application@cs)  


        private static void RaiseExit() { 
            if (eventHandlers != null) {
                Delegate exit = eventHandlers[EVENT_APPLICATIONEXIT];
                if (exit != null)
                    ((EventHandler)exit)(null, EventArgs.Empty); 
            }
        } 



[CefSharpSettings.ShutdownOnExit Property](http://cefsharp.github.io/api/87.1.x/html/P_CefSharp_CefSharpSettings_ShutdownOnExit.htm)  
[cef thread](https://github.com/TV-Rename/tvrename/issues/870)  
[ChromiumWebBrowser static constructor](https://github.com/cefsharp/CefSharp/blob/cefsharp/96/CefSharp.WinForms/ChromiumWebBrowser.cs#L254)  
[Application.ApplicationExit Event](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.application.applicationexit?view=windowsdesktop-7.0)  
[ApplicationContext Class](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.applicationcontext?view=windowsdesktop-7.0)  
[Application.Run](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.application.run?view=windowsdesktop-7.0)  


        if (new LoginForm().ShowDialog() == DialogResult.OK)
        {
            Application.Run(new MainForm());
        }

[https://stackoverflow.com/a/2315170](https://stackoverflow.com/a/2315170)

[ProductDocument source code](https://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/CommonUI/System/Drawing/Printing/PrintDocument@cs/1/PrintDocument@cs)  
[PrintController source code](https://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/CommonUI/System/Drawing/Printing/PrintController@cs/1/PrintController@cs)   
[printcontrollerwithstatusdialog and StatusDialog source code](http://www.dotnetframework.org/default.aspx/DotNET/DotNET/8@0/untmp/whidbey/REDBITS/ndp/fx/src/WinForms/Managed/System/WinForms/Printing/PrintControllerWithStatusDialog@cs/1/PrintControllerWithStatusDialog@cs)  

[Application.cs source code](https://www.dotnetframework.org/default.aspx/4@0/4@0/DEVDIV_TFS/Dev10/Releases/RTMRel/ndp/fx/src/WinForms/Managed/System/WinForms/Application@cs/1305376/Application@cs)  