---                
layout: post                
title: "HttpParams的使用方法"                
date:   2019-7-17 17:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      

## HttpParams
The Query parameters are added using the helper class `HttpParams`.  The `HttpParams` is passed as one of the argument to `HttpClient.get` method.

To use HttpParams, you need to import it first as shown below.


    import { HttpClient,HttpParams } from '@angular/common/http';
 
Then create an instance of the HttpParams class.

    const params = new HttpParams()
    .set('page', PageNo)
    .set('sort', SortOn);

And then call the `httpClient.get` method passing the params as the argument.


    return this.httpClient.get<repos[]>(
        this.baseURL + 'users/' + userName + '/repos',
        {params})

也可以用`.append`方法

    params = new HttpParams()
      .set('page', '2')
      .append('page', '3')
      .set('sort', 'name');
 
    console.log(params.toString()); //Returns page=2&page=3&sort=name

## HTTPParams is immutable

The HttpParams object is immutable. Everytime you call a set method on Params object, it will create and return a new instance of the Params.

For Example

The following code does not work

    let params = new HttpParams();

    params.set('page', PageNo);
    params.set('sort', SortOn);
 
Each call to set method does not add the options to the existing HttpParams instance, but creates a new instance from the existing instance and returns it.

To work around, you can use the code as follows

    Let params = new HttpParams()
        .set('page', PageNo)
        .set('sort', SortOn);
 
Or you can try this

    let params = new HttpParams();

    params=params.set('page', PageNo);
    params=params.set('sort', SortOn);
 
## Reference

[https://www.tektutorialshub.com/angular/angular-pass-url-parameters-query-strings/](https://www.tektutorialshub.com/angular/angular-pass-url-parameters-query-strings/)