---
layout: post
title: "pnpm 关掉 syslink"
date: 2024-09-12 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

相比于npm，pnpm 能显著提高包的下载速度。但如果查看node module文件夹，会发现很多module文件夹都带了link图标。这是因为pnpm使用了syslink，不管你有多少个project使用了这个module，pnpm只下载一份，然后用syslink将其连接到所需要的project中。    
可以使用命令`pnpm store path`来查看pnpm的缓存文件夹。  
Syslink能减少空间占用，这在多project的情况下带来的好处不言而喻。但在某些情况下，可能想禁掉syslink，将所有的module都完整下载下来，这也可以做到。在project root下新建一个`.npmrc`文件，在文件中添加以下配置：  

    node-linker=hoisted

删掉node modules，重新`pnpm install`  

注意: pnpm这个功能是从v7.13开始有的，如果你的pnpm版本过低，建议升级到7.13以上版本。  