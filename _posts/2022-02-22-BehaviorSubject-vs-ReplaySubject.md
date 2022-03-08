---                
layout: post            
title: "Subject vs BehaviorSubject vs ReplaySubject"                
date:   2022-2-22 16:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---  

# Subject
A Subject is a special type of Observable that allows values to be multicasted to many Observers. Subjects are like EventEmitters.  
使用Subject时，订阅者只会获得订阅后发出的发布值。
Subject有三个子类：  

        BehaviorSubject  
        ReplaySubject  
        AsyncSubject  

# BehaviorSubject
A variant of Subject that requires an initial value and emits its current value whenever it is subscribed to.  
BehaviorSubject- 新订阅者在订阅后立即获得最后发布的值或初始值。BehaviorSubject会缓存最后一个值。订阅者将在初始订阅时获得最新值。如果没有上一个值的时候会发送默认值（如果有的话)。如果BehaviorSubject被初始化为null，那订阅者在订阅后会先收到null值。  

# ReplaySubject
A variant of Subject that "replays" old values to new subscribers by emitting them when they first subscribe.  
ReplaySubject可以缓存指定数量的值。新订阅者在订阅后立即获得所有先前发布的值。  
它有一个内部缓冲区，用于暂存接收到的指定数量的值。像Subject， ReplaySubject通过将值传递给其next函数来`observe`值。当它接收到一个值时，它将将该值存储一段时间，存储的时间长短由构造函数来决定。
当订阅ReplaySubject时，它将以先进先出 (FIFO) 的方式将缓冲区中的所有值发送给订阅者。
构造函数的参数：  

1. bufferSize- 这将确定缓冲区中存储了多少项目，默认为无限。
2. windowTime- 从缓冲区中删除值之前在缓冲区中保存值的时间量。
   
这两个参数可以同时存在。比如想缓冲最多 3 个值，且这些值小于 2 秒，就可以用`new ReplaySubject(3, 2000)`.

## 与 BehaviorSubject 的差异

在初始化ReplaySubject时，如果将buffer size设为1，即`new ReplaySubject(1)`，它的实际行为类似于BehaviorSubject。总是缓存最后一个值，如果初始值是null，直到第一个值时订阅者才会收到消息。这就省去了BehaviorSubject的null检查。


# Reference
[RxJS: How to not subscribe to initial value and/or undefined?](https://stackoverflow.com/questions/28314882/rxjs-how-to-not-subscribe-to-initial-value-and-or-undefined)   
[Subject vs BehaviorSubject vs ReplaySubject in Angular](https://stackoverflow.com/questions/43118769/subject-vs-behaviorsubject-vs-replaysubject-in-angular#:~:text=The%20ReplaySubject%20stored%20an%20arbitrary,values%20that%20are%20passed%20in.)  
[BehaviorSubject](https://rxjs.dev/api/index/class/BehaviorSubject)   
[ReplaySubject](https://rxjs.dev/api/index/class/ReplaySubject) 