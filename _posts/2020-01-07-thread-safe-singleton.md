---                
layout: post                
title: "线程安全的单例模式" 
date:   2020-01-07 19:30:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

## 普通单例模式

    public class Singleton
    {
        private static Singleton instance = null;

        private Singleton()
        {
        }

        public static Singleton Instance
        {
            get
            {
                if (instance == null)
                {
                    instance = new Singleton();
                }
                return instance;
            }
        }
    }

缺点：  
非线程安全  

## 简单线程安全

    public class Singleton
    {
        private static Singleton instance = null;
        private static readonly object padlock = new object();

        Singleton()
        {
        }

        public static Singleton Instance
        {
            get
            {
                lock (padlock)
                {
                    if (instance == null)
                    {
                        instance = new Singleton();
                    }
                    return instance;
                }
            }
        }
    }

优点：  
使用锁去控制类的实例化，保证了线程安全。  
缺点：  
性能受影响，每次获取实例都需要先加锁。  

## 双重检查  


    public class Singleton
    {
        private static Singleton instance = null;
        private static readonly object padlock = new object();

        Singleton()
        {
        }

        public static Singleton Instance
        {
            get
            {
                if (instance == null)
                {
                    lock (padlock)
                    {
                        if (instance == null)
                        {
                            instance = new Singleton();
                        }
                    }
                }
                return instance;
            }
        }
    }

通过双重检查，减少加锁带来的性能问题。   

## 不加锁版本

    public class Singleton
    {
        private static readonly Singleton instance = new Singleton();

        // Explicit static constructor to tell C# compiler
        // not to mark type as beforefieldinit
        static Singleton()
        {
        }

        private Singleton()
        {
        }

        public static Singleton Instance
        {
            get
            {
                return instance;
            }
        }
    }

## 使用 `Lazy<T>` type

    public sealed class Singleton
    {
        private static readonly Lazy<Singleton> lazy = new Lazy<Singleton>(() => new Singleton());

        public static Singleton Instance
        {
            get
            {
                return lazy.Value;
            }
        }

        private Singleton()
        {
        }
    }

[https://csharpindepth.com/articles/singleton](https://csharpindepth.com/articles/singleton)