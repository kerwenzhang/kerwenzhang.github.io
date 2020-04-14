---                
layout: post                
title: "Git clone LFS 错误" 
date:   2020-04-14 10:30:00                 
categories: "Git"                
catalog: true                
tags:                 
    - Git                
---      

在用Git去clone的时候遇到以下问题：

    Use git lfs logs last to view the log.
    error: external filter 'git-lfs filter-process' failed
    fatal: data/processed/career_builder/embedding.npy: smudge filter lfs failed
    warning: Clone succeeded, but checkout failed.

解决方案：

    // Skip smudge - We'll download binary files later in a faster batch
    git lfs install --skip-smudge

    // Do git clone here
    git clone ...

    // Fetch all the binary files in the new clone
    git lfs pull

    // Reinstate smudge
    git lfs install --force

[https://github.com/git-lfs/git-lfs/issues/911](https://github.com/git-lfs/git-lfs/issues/911)