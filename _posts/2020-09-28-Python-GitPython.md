---                
layout: post                
title: "GitPython" 
date:   2020-09-28 10:30:00                 
categories: "Python"                
catalog: true                
tags:                 
    - Python                
---      

`GitPython`是个开源的Python第三方库，我们可以用它方便的操作Git repository。  
安装：  

    pip install gitpython

我们可以用GitPython直接调用Git的命令：  

git log:  

    g = git.Git("C:/path/to/your/repo") 
    loginfo = g.log("--oneline", "f5035ce..f63d26b")
    print loginfo

git show:  

    from git import Repo

    # Suppose the current path is the root of the repository
    r = Repo('.')
    o = r.git.show('HEAD', pretty="", name_only=True)
    print(o)

### Read line by line

    for line in lines.splitlines():
        print(line)



[GitPython](https://gitpython.readthedocs.io/en/stable/index.html)    
[https://stackoverflow.com/questions/55176579/iterate-commits-b-w-2-specified-commits-in-gitpython](https://stackoverflow.com/questions/55176579/iterate-commits-b-w-2-specified-commits-in-gitpython)  
[https://stackoverflow.com/questions/64056275/how-to-list-all-changed-files-between-two-tags-in-gitpython](https://stackoverflow.com/questions/64056275/how-to-list-all-changed-files-between-two-tags-in-gitpython)  
[https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422153](https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422153)   