---
layout: post
title: "node-gyp 指定C++ standard"
date: 2024-11-19 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

最近给产品升级Nodejs版本，从Node 18升级到Node22，升级完之后发现Addon project编译不过去了，编译的时候会报很多语法错误，很多是跟C++的隐式转换有关。比如以下代码

        const LPSTR testStr = "Server-Group";

在老版本Node18的时候不会报错，但Node环境切到22，就会有error报出来，而且是静态error。

        error C2440: 'initializing': cannot convert from 'const char [xx]' to 'LPSTR'
        E0144	a value of type "const char *" cannot be used to initialize an entity of type "const LPSTR"
        Conversion from string literal loses const qualifier (see /Zc:strictStrings)

仔细对比了下node-gyp生成的vcxproj文件，发现C++ language仍然是14，但在编译命令中C++版本发生了变化。 从

        /Zc:__cplusplus -std:c++17

变成了  

        /Zc:__cplusplus -std:c++20 /Zm2000 

在微软的官方说明中，`/Zc:__cplusplus`会启用 `__cplusplus` 预处理器宏。检查代码是否符合指定的C++标准。这就难怪它报的是静态问题。  
默认是c++14； 当Node版本是18时，生成的vcxproj带的标准是C++17；当Node版本是22时，c++标准改成了20。


|/Zc:__cplusplus 选项|/std 选项|__cplusplus 值|  
|--|--|--|
|Zc:__cplusplus|/std:c++14（默认值）|201402L|
|Zc:__cplusplus|/std:c++17|201703L|
|Zc:__cplusplus|/std:c++20|202002L|

  
解决方案有两个。第一个是修改我们的代码，使其满足C++ 20标准。

        const LPSTR testStr	= const_cast<char*>("Server-Group");

第二个方法是修改node-gyp配置文件，降低C++的标准。node-gyp论坛里有个[帖子](https://github.com/nodejs/node-gyp/issues/1662)讨论怎么指定C++的版本。    
 
        binding.gyp:

        ['OS=="win"', {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "AdditionalOptions": [ "-std:c++17", ],
            },
          },
        }]

这个方法编译的时候会有warning： 

        cl : command line  warning D9025: overriding '/std:c++20' with '/std:c++17'

因为生成的vcxproj文件里其实是这样的：  

        /Zc:__cplusplus -std:c++20 /Zm2000 -std:c++17

这个方法并不推荐，因为我们降低了标准，并且这个问题早晚都得解决。  

这个问题其实还可以再挖一挖，node-gyp是怎么根据Node环境指定/zc编译选项的。  

# Reference
[/Zc:__cplusplus](https://learn.microsoft.com/zh-cn/cpp/build/reference/zc-cplusplus?view=msvc-170)    
[Is there any way to use C++17 on MSBuild?](https://github.com/nodejs/node-gyp/issues/1662)