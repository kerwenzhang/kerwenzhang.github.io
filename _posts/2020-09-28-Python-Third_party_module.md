---                
layout: post                
title: "Python指定third-party module安装目录" 
date:   2020-09-28 10:30:00                 
categories: "Python"                
catalog: true                
tags:                 
    - Python                
---      

最近尝试用Python写个小程序，需要调用第三方的Module。第三方的Module正常情况下都需要先进行安装，才能使用。但是我不想在每个运行的机器上安装这个module。最终在`StackOverflow`上找到了解决方案：   

    pip install --target=d:\somewhere\other\than\the\default package_name

当引用第三方库时需要手动指定一下Module的位置：  

    import sys
    sys.path.append("/path/to/your/tweepy/directory")
    from git import Repo

注意这里用的是反斜杠  

[Installing GitPython](https://gitpython.readthedocs.io/en/stable/intro.html)  
[Use a library locally instead of installing it](https://stackoverflow.com/questions/9059699/python-use-a-library-locally-instead-of-installing-it)  
[mport Python modules without installing](https://www.tutorialspoint.com/How-we-can-import-Python-modules-without-installing#:~:text=If%20you%20are%20not%20able,%2F'%20%3E%3E%3E%20sys.)  