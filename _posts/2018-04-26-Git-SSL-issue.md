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
    
Resolution:  
[Reference](https://www.cnblogs.com/chucklu/p/4056499.html)  
1. Use Puttygen to generate a new key:  
Parameter choose RSA, click "Generate" button, click blank area 

2. Click "Save private key" to save your private key

3. Copy public key and past to GitLab website server

4. Right click in an empty folder, select "TortoiseGit"-> "Clone"

5. In popup dialog, input your GitLab url,  check "Load Putty Key", select the private key you have saved

6. Click OK button

