---                
layout: post                
title: "VBScript拷贝长路径文件" 
date:   2020-11-6 10:30:00                 
categories: "Others"                
catalog: true                
tags:                 
    - Others                
---      

在用VBScript进行文件拷贝时，发现文件路径太长导致拷贝失败。可以尝试使用文件的短路径进行解决。

    Dim tempDir,soucerDir,fso,shortPath

    tempDir = "C:\toFolder"
    soucerDir = "\\server\looooongfilepath"
    set fso=CreateObject("Scripting.FileSystemObject")
    shortPath = fso.GetFolder(soucerDir).ShortPath

    fso.CopyFolder shortPath, tempDir

[https://social.technet.microsoft.com/Forums/scriptcenter/en-US/874d303f-f201-4fee-ad47-4f7c8979434f/vbscript-unable-to-copy-files-exceeding-260-chars-in-path?forum=ITCG#c21fb909-939a-440d-85a6-60cc6d09cc45](https://social.technet.microsoft.com/Forums/scriptcenter/en-US/874d303f-f201-4fee-ad47-4f7c8979434f/vbscript-unable-to-copy-files-exceeding-260-chars-in-path?forum=ITCG#c21fb909-939a-440d-85a6-60cc6d09cc45)