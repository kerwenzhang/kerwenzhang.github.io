---      
layout: post      
title: "VB6 functions to C#"      
date:   2024-1-18 10:59:00       
categories: "C#"      
catalog: true      
tags:       
    - C#      
---      
      


    VB             C#

    UBound()     = yourArray.GetUpperBound(0) or yourArray.Length for one-dimesional arrays
    LBound()     = yourArray.GetLowerBound(0)
    IsNothing()  = Object.ReferenceEquals(obj,null)
    Chr()        = Convert.ToChar()
    Len()        = "string".Length
    UCase()      = "string".ToUpper()
    LCase()      = "string".ToLower()
    Left()       = "string".Substring(0, length)
    Right()      = "string".Substring("string".Length - desiredLength)
    RTrim()      = "string".TrimEnd()
    LTrim()      = "string".TrimStart()
    Trim()       = "string".Trim()
    Mid()        = "string".Substring(start, length)
    Replace()    = "string".Replace()
    Split()      = "string".Split()
    Join()       = String.Join()
    MsgBox()     = MessageBox.Show()
    IIF()        = (boolean_condition ? "true" : "false")

InStr 返回第二个字符串在第一个字符串中出现的位置，如果没有，则返回0
instr（1，＂abcdef＂，＂j＂）返回结果为0， 1表示从第一个字符串的第一个字符开始查找， 与C#不同的是，VB6的开始Index为1， C#，VB.NET初始index是0   

Mid函数是用来提取字符串中的一部分字符的。它的基本语法：

    Mid(要提取的字符串, 起始位置, 需要提取的字符数)

注意起始位置从1开始  

        VB          C#

        CLng        Convert.ToInt64()
        

# Reference
[https://stackoverflow.com/a/1722914/7352168](https://stackoverflow.com/a/1722914/7352168)   

[Integral numeric types (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types)  
[Redim Preserve in C#?]()

[https://www.codemag.com/article/1807091/Prepare-Visual-Basic-for-Conversion-to-C](https://www.codemag.com/article/1807091/Prepare-Visual-Basic-for-Conversion-to-C)