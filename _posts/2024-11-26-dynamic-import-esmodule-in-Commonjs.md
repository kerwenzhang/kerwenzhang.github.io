---
layout: post
title: "Dynamic import ESModules in CommonJS"
date: 2024-11-26 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

今天在升级第三方module到最新,升完就发现问题了。我们的project用的是CommonJs，但一些第三方的module最新版本用了ESModule。比如`del`。 del 6.0还是用的CommonJs，之前的调用是这么写的：  

    del = require('del')
    del('path')

从7.0开始，del开始用ESModule。官方例子变成了这样  


    import {deleteAsync} from 'del';
    const deletedDirectoryPaths = await deleteAsync(['temp', 'public']);

升级del到8.0之后就报了以下错误:

    Error [ERR_REQUIRE_ESM]: require() of ES Module xxx\node_modules\del\index.js from xxx.js not supported.
    Instead change the require of index.js in xxx.js to a dynamic import() which is available in all CommonJS modules.

我们不能因为一个dev dependency就把整个module改成ESModule。好在CommonJS里能动态import ESModule。错误消息里也有相关提示。  

    const del = (...args) => import('del').then((mod) => mod.deleteAsync(...args));
    del('path)

以上写法对del还挺好用。但我在chai上遇到了另外一个问题。chai最新版本也只支持ESModule.  按照上面的写法

    const expect = (...args) => import('chai').then((mod) => mod.expect(...args));
    expect ('true').to.equal('false');

它会报以下错误

    TypeError: Cannot read properties of undefined (reading 'equal')

我能想到的解决方案有  
方案1  

    import('chai').then(chai => {
      expect = chai.expect;
      expect('true').to.equal('false');
      
    });

这样每个expect都得先动态import一下，放弃！  
方案2  

    const expectEqual = (arg1, arg2) => import('chai').then((mod) => mod.expect(arg1).to.equal(arg2));

好处是我只需要在文件开始地方声明一下，后边就可以无限用了。但需要为每一种expect都声明一下。`expect.to.be`，`expect.to.exist`