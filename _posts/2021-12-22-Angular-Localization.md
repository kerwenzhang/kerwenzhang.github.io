---                
layout: post            
title: "Angular本地化"                
date:   2021-12-22 17:30:00                 
categories: "web"                
catalog: true                
tags:                 
    - web                
---      

Angular本地化有两种方式，一种是Angular官网推荐的`i18n`标记，另外一种是`ngx-translate`

# Angular
## Angular/localize
要利用 Angular 的本地化功能，请用 Angular CLI 将 @angular/localize 包添加到你的项目中。  

    ng add @angular/localize

Angular 提供了以下内置的数据转换管道。数据转换管道会使用 LOCALE_ID 标记来根据每个语言环境的规则来格式化数据。  

    DatePipe ：格式化日期值。
    CurrencyPipe ：将数字转换为货币字符串。
    DecimalPipe ：将数字转换为十进制数字字符串。
    PercentPipe ：将数字转换为百分比字符串。

## 添加 i18n 标记
标记要翻译的文本  
使用 `i18n` 属性标记要翻译的组件模板中的静态文本消息。将它放在每个元素标签上，并带有要翻译的固定文本。  
例如，以下 `<h1>` 标记显示简单的英语问候语 `Hello World！`。  

    <h1>Hello World!</h1>

要将问候语标记为待翻译，请将 `i18n` 属性添加到 `<h1>` 标记。  

    <h1 i18n>Hello World!</h1>

## 提取源语言文件
要提取源语言文件，请打开终端窗口，切换到应用程序项目的根目录，然后运行以下 CLI 命令：  

    ng extract-i18n

`extract-i18n` 命令使用 `XML` 在项目的根目录中创建一个名为 `messages.xlf` 的源语言文件。
要在 `src/locale` 目录中创建文件，请在选项中指定输出路径。以下示例就在选项中指定了输出路径。  

    ng extract-i18n --output-path src/locale

要创建法语翻译文件，请执行以下步骤：  
1. 制作 `messages.xlf` 源语言文件的副本。  
2. 将副本放在 `src/locale` 文件夹中。  
3. 将副本重命名为 `messages.fr.xlf` 以进行法语 ( fr ) 翻译。将此翻译文件发送给翻译人员。  

Angular需要为每个语言环境构建应用程序的可分发文件的副本。  
合并翻译后，可使用“服务器的语言检测功能”或不同的子目录来提供应用程序的每个可分发副本。  

# ngx-translate
Angular官网的方式需要构建不同的语言版本，并且没法自由切换语言。  
另一种方式是用开源库 `ngx-translate`。  



[Angular 国际化](https://angular.cn/guide/i18n-overview)  
[angular6.x 国际化解决方案 ngx-translate](https://www.jianshu.com/p/9c3834b9feed)  
[Why ngx-translate exists if we already have built-in Angular2+ i18n](https://github.com/ngx-translate/core/issues/495)