---                                  
layout: post                                  
title: "How to downlaod code using label in RTC"                                  
date:   2018-10-23 14:00:00                                   
categories: "Others"                                  
catalog: true                                  
tags:                                   
    - Others                                  
---                        
        
Take Updater R1 label 1.00.00.40 as example.    
    
First, need to create a new workspace    
1. In Team Artfacts window, CVB_CommonInstall, Source Control, select Stream "Updater R1"    
2. right click on "Updaer R1", select "New" -> "Repository WorkSpace"    
3. In the wizard, change "WorkSpace name", click -> next    
4. Keep "Private", select "Next"    
5. Click "Finish" button, Wait some while, popup "Load Repository Workspace" dialog    
6. Change Sandbox location, and select "Load component as root folder", click Next    
7. click "Finish" in next popup page.    
8. After download code complete, open this project    
    
9. In Team Artfacts window, My Repository WorkSpace, find the workspace you just created in step3, if could not find, right click, select refresh    
10. Select the workspace you created, right click, select "Open"    
11. In "Components" section, it list the current baseline, select "Replace With..." button    
12. In the coming wizard dialog, select "Component baseline", click "Next" button    
13. It will list all label which has labeled. Select "1.00.00.40" as example, click "Next" button    
14. Click "Finish" button, click "Save" button in "Repository WorkSpace" page.