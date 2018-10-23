---                              
layout: post                              
title: "Updater R1 经验教训"                              
date:   2018-10-22 14:00:00                               
categories: "Others"                              
catalog: true                              
tags:                               
    - Others                              
---                    
    
1. 性能检测没有检测异常情况（网络连接不上，Server连接不上）  
2. 测试机不足，导致开发机占用  
3. 非Admin情况的测试  
4. 不管计划的多合理，总是能把最后的deadline吃净。在一些关键节点（first build，IC build）之前总会发现一些bug，导致build的时间不断向后推迟，最终会把所有的冗余时间给用掉。 分析原因，其一，每个人都不是full time在这个项目上，每个人都有其他的工作，Updater的job完成之后就把注意力转移到其他工作上了，而在关键节点之前，所有人的注意力，精力都重新回到Updater上，更容易集中发现问题。 其二，测试覆盖不够    
措施：  
a. 关键节点加大提前量  
b. 责任人pay more attention  
c. 测试范围design，case 要更细致的review  
