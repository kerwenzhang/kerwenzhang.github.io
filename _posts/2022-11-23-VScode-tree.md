---
layout: post
title: VSCode增加文件树目录缩进
date:   2022-11-23 9:13:14
categories: "Others"
catalog: true
tags: 
    - Others
---

Go to File > Preference > Settings and choose:

Workbench › Tree: Indent

Controls tree indentation in pixels.

or (in your settings.json enter this directly)

    "workbench.tree.indent": 20

you can add colorized tree indent guides to make the explorer file structure more obvious.  

    {                                         // in settings.json
    "workbench.colorCustomizations": {
        "tree.indentGuidesStroke": "#00ff00"
    }