---
layout: post
title: C#枚举类型生成tlb时自动加前缀
date:   2024-04-03 9:13:14
categories: "C#"
catalog: true
tags: 
    - C#
---

最近发现如果用C#生成COM接口，C#里写的枚举(enum)，在生成tlb时，会自动添加枚举名前缀。
# 实例  
1. 创建一个C# .net framework library, 取名EnumTest
2. 在类里面添加一个枚举

        namespace EnumTest
        {
            public class Class1
            {
                public enum enumDemo
                {
                    None = 0,
                    enumA = 1,
                    enumB = 2,
                    enumC = 3
                }
            }
        }
3. 将project属性设置为`Make Assembly COM-Visible`，并且`Register for COM interop`
4. 编译工程，在debug目录下会生成`EnumTest.dll`和`EnumTest.tlb`两个文件。tlb是COM注册时生成的接口定义文件。  
5. 使用`C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x86\oleview.exe`打开tlb文件。 菜单File->View TypeLib...， 选择我们刚才生成的`EnumTest.tlb`. 我们创建的枚举`enumDemo`显示如下：

        typedef [uuid(AAAFE7CA-E486-3D7C-96D7-4A69C9386581), version(1.0),
        custom(0F21F359-AB84-41E8-9A78-36D110E6D2F9, "EnumTest.Class1+enumDemo")
        ]
        enum {
            enumDemo_None = 0,
            enumDemo_enumA = 1,
            enumDemo_enumB = 2,
            enumDemo_enumC = 3
        } enumDemo;

可以发现，在每个枚举元素前自动添加了枚举名的前缀。  

这是由 .NET 枚举类型与 C 和 C++ 等语言中的 enum 关键字之间的显着不兼容性引起的。C/C++将枚举成员添加到全局命名空间。 这实际上是一个很大的问题，它经常迫使您在枚举成员名称上添加前缀，这样它们就不会与其他标识符发生冲突。 

最近批准的新 C++ 语言标准 (C++11) 实际上通过新的 enum class 关键字修复了这个问题。 其工作方式与 .NET 枚举相同，它们需要以其枚举类型名称作为前缀。 

类型库导出器无法做任何合理的事情。 但要在枚举成员前面加上其类型名称。不这样做将会引发标识符名称冲突的可怕后果。  

# 解决方案
要解决此问题，可以使用 oleview.exe 程序将类型库反编译为 .idl。 编辑 typedef 并使用 midl.exe 将其编译回 .tlb。 
具体操作如下：  
1. 使用`oleview.exe`打开tlb之后，菜单File-> Save as，将tlb保存为idl文件。
2. 使用文本编辑器打开`EnumTest.IDL`文件，找到我们定义的枚举

        enum {
            enumDemo_None = 0,
            enumDemo_enumA = 1,
            enumDemo_enumB = 2,
            enumDemo_enumC = 3
        } enumDemo;

    将其修改为：  

        enum enumDemo {
            None = 0,
            enumA = 1,
            enumB = 2,
            enumC = 3
        } enumDemo;

    注意枚举名称必须在 enum 关键字之后再放一遍。
3. 使用midl.exe 将idl文件转回tlb

        midl EnumTest.IDL /tlb EnumTest_new.tlb

4. 使用`oleview.exe`打开新的tlb

        typedef [uuid(AAAFE7CA-E486-3D7C-96D7-4A69C9386581), version(1.0),
        custom(0F21F359-AB84-41E8-9A78-36D110E6D2F9, "EnumTest.Class1+enumDemo")
        ]
        enum {
            None = 0,
            enumA = 1,
            enumB = 2,
            enumC = 3
        } enumDemo;

枚举成员变量就回到我们C#里定义的模样了。  


# Reference
[Why is the enum name added as a prefix to my constants](https://stackoverflow.com/a/9362480/7352168)   
[Interop: Remove prefix from C# Enums for COM](http://blogs.artinsoft.net/mrojas/archive/2010/05/17/interop-remove-prefix-from-c-enums-for-com.aspx)   
