---  
layout: post  
title: "Git SSL certificate issue"  
date:   2018-4-26 13:30:00   
categories: "Git"  
catalog: true  
tags:   
    - Git  
---  
  
 
[Reference](https://confluence.atlassian.com/bitbucketserverkb/ssl-certificate-problem-unable-to-get-local-issuer-certificate-816521128.html)  

在用TorToiseGit进行 Git Clone时，遇到错误提示：  

    GIT SSL certificate problem: unable to get local issuer certificate

Workaround：  

    git config --global http.sslVerify false
    
