---                
layout: post                
title: "Map Pipe Subscirbe"                
date:   2019-8-30 10:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

## Map

Map’s job is to transform things  
map is a pretty simple operator. It takes a projection function, and applies it to each value that comes from the source observable.  

    x => `Hello ${x}!` // projection function

    // It's used like this:
    of('World').pipe(map(x => `Hello ${x}!`));


In this example, the observable returned by `of('World’)` is the source observable, and the single value `'World'` is going to be `pipe`'d through to `map`’s projection function.  
The projection function will receive 'World' as its input parameter x, and will create the string Hello World!.  
map wraps the project function in an observable, which then emits the string value Hello World!. Remember, <strong>operators always return observables.</strong>  

## Pipe

Unlike map, which is an operator, pipe is a method on Observable which is used for composing operators. pipe was introduced to RxJS in v5.5 that looked like this:   

    of(1,2,3).map(x => x + 1).filter(x => x > 2);

and turn it into this

    of(1,2,3).pipe(
      map(x => x + 1),
      filter(x => x > 2)
    );



[reference1](https://blog.angularindepth.com/reading-the-rxjs-6-sources-map-and-pipe-94d51fec71c2)  