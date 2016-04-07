---
layout: post
title: 用GitPython实现Git自动化上传代码
date:   2016-04-06 16:52:03
categories: [Python]
tags: [GitPython]
---

* content
{:toc}

最近一直在学习Python，最好的学习方法莫过于实践。 想来想去，自己首先想到的是把Git代码上传实现自动化。   
由于自己的博客是建在Github上，所以每次更新，添加文章都需要在git bash里面运行下面的代码：   

	Git add .
	Git commit -m "comments"
	Git push origin master

之后还需要输入用户名和密码，每一次更新都需要做这一套动作，很烦呐！   

然后就查到了这个库 GitPython，它满足了我目前所有的需求   
先贴官方文档：   
[http://gitpython.readthedocs.org/en/stable/index.html](http://gitpython.readthedocs.org/en/stable/index.html)   

## 安装

在命令行里面直接运行：   

	pip install gitpython

The first step is to create a git.Repo object to represent your repository.	   
第一步：   
先创建一个git.Repo的对象来指定你本地的代码仓库   

	from git import Repo

	path ="your repository directory"
	repo = Repo(path)
	assert not repo.bare

path是我的仓库根目录，它下面包含一个.git的隐藏文件夹   

检查仓库状态   

	print(repo.is_dirty())

与远程服务器上的文件进行比对，如果不同则返回True   

获取未上传的文件列表   

	fileList = repo.untracked_files

注意这个只会打印出你未上传的新文件，如果你只是更新了某个原先已经存在的文件，则repo.is_dirty()应该返回True   

origins = repo.remotes   
origin = origins.pop()   

GitCommandError: 'git push --porcelain prigin' returned with exit code 128   

GitDB   
官方文档：   
[http://gitdb.readthedocs.org/en/latest/index.html](http://gitdb.readthedocs.org/en/latest/index.html)   

## 安装

在命令行里面直接运行：   

	pip install gitdb