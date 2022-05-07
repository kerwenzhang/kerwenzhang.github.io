---                
layout: post            
title: "Dell笔记本插3.5mm耳机后耳麦不好用"                
date:   2022-5-6 16:30:00                 
categories: "Other"                
catalog: true                
tags:                 
    - Other                
---      

最近发现自己的Dell笔记本插3.5mm耳机之后耳麦不工作，默认使用的是笔记本的耳麦。一番查找之后找到了解决方案：  
1. 开始菜单，找到`MaxxAudioPro`，如果是Dell笔记本且没有装，可以试着装一下这个软件    
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic1.png?raw=true)
2. 打开这个软件之后，如果你没有插耳机，第一个图标是音响的模样，意思是用的笔记本自带的外放。  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic2.png?raw=true)
3. 插上耳机之后，就变成这样了  
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic3.png?raw=true)
4. 点第一个图标，修改输出设备，改成耳机headset
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic4.png?raw=true)

测试：
1. 右下角声音图标，右键选择声音
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic5.png?raw=true)
2. 在Recording选项卡里可以看到耳机的耳麦已经被激活
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic6.png?raw=true)
3. 离笔记本远一点对着耳机的耳麦说话可以看到效果。  
4. 拔掉3.5mm耳机之后会发现 Jack Mic被disable了
   ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/mic7.png?raw=true)
   
# Reference
[耳机连戴尔电脑耳机麦克风不识别？保姆级讲师一对一解答！](https://www.bilibili.com/video/BV1d44y1v7xo?spm_id_from=333.999.0.0)  
