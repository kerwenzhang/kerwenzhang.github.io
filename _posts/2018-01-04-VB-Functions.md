---
layout: post
title: "VBScript Functions"
date:   2018-1-4 13:50:00 
categories: "VB"
catalog: true
tags: 
    - VB
---


VBScript functions 介绍    
https://www.w3schools.com/asp/asp_ref_vbscript_functions.asp#string
 
 
Example to rename a File
    
    subFuns

    Private Sub subFuns
        Dim path,tests
        path="C:\Users\N0398326\Desktop\temp\20180103\Import Tool.exe"
        tests = Rename(path)
        MsgBox tests
    End Sub

    Private Function Rename(path)
        Dim index,fileName,filePath,renameFile,Fso
        Set Fso=WScript.CreateObject("Scripting.FileSystemObject")
        index=InStrRev(path,"\")
        fileName=Mid(path,index+1,len(path))
        filePath=Mid(path,1,index)
        If InStr(fileName, " ") > 0 Then
            renameFile=filePath+"test"
            'Fso.MoveFile path,renameFile
            Rename=renameFile
        else
            Rename=path
        End If
        'Fso.MoveFile renameFile,path
    End Function