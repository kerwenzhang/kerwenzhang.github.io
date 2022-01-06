---                
layout: post            
title: "IEnumerable<T> IActionResult ActionResult<T> "                
date:   2022-1-6 17:30:00                 
categories: ".Net Core"                
catalog: true                
tags:                 
    - .Net Core                
---      
在 ASP.NET Core 中有三种返回 数据 和 HTTP状态码 的方式   
# IEnumerable
IEnumerable<T>只能返回数据，附带不了http状态码   

    [HttpGet]
    public IEnumerable<Author> Get()
    {
        return authors;
    }

在 `ASP.NET Core 3.0` 开始，你不仅可以定义同步形式的 `IEnumerable<Author>`方法，也可以定义异步形式的 `IAsyncEnumerable<T>`方法，后者的不同点在于它是一个异步模式的集合，好处就是 不阻塞 当前的调用线程   

    [HttpGet]
    public async IAsyncEnumerable<Author> Get()
    {
        var authors = await GetAuthors();
        await foreach (var author in authors)
        {
                yield return author;
        }
    }

# IActionResult
IActionResult 实例可以将 数据 + Http状态码 一同带给前端  

    [HttpGet]
    public IActionResult Get()
    {
        if (authors == null)
            return NotFound("No records");

        return Ok(authors);
    }

上面的代码有 Ok，NotFound 两个方法，对应着 OKResult，NotFoundResult， Http Code 对应着 200，404。  

# ActionResult<T>
`ActionResult<T>` 是在 `ASP.NET Core 2.1` 中被引入的，它的作用就是包装了前面这种模式，怎么理解呢？ 就是即可以返回 `IActionResult` ，也可以返回指定类型  

    [HttpGet]
    public ActionResult<IEnumerable<Author>> Get()
    {
        if (authors == null)
            return NotFound("No records");
        return authors;
    }

异步方法：  

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Author>>> Get()
    {
        var data = await GetAuthors();
        if (data == null)
                return NotFound("No record");
        return data;
    }


[如何在 Core Web API 中以三种方式返回数据](https://segmentfault.com/a/1190000039068169)    
