---                
layout: post                
title: "如何限制Task的最大并发数量" 
date:   2019-12-10 16:40:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

    int maxConcurrency=10;
    var messages = new List<string>();
    using(SemaphoreSlim concurrencySemaphore = new SemaphoreSlim(maxConcurrency))
    {
        List<Task> tasks = new List<Task>();
        foreach(var msg in messages)
        {
            concurrencySemaphore.Wait();

            var t = Task.Factory.StartNew(() =>
            {
                try
                {
                    Process(msg);
                }
                finally
                {
                    concurrencySemaphore.Release();
                }
            });

            tasks.Add(t);
        }

        Task.WaitAll(tasks.ToArray());
    }