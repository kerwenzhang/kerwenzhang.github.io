---                                  
layout: post                                  
title: "jQuery ajax 发送get请求"                                  
date:   2020-07-14 9:00:00                                   
categories: "Web"                                  
catalog: true                                  
tags:                                   
    - Web                                  
---                        
    
### Create Nodejs Server

server.js:  

        var http = require("http");
        var url = require("url");
        var fs = require('fs');

        http.createServer(function (req, res) {
        if (req.url.indexOf("/server.js") != 0) {
                var rootDir = 'C:\\Kerwen\\Learn\\Web\\MyWebLearning\\jQuery\\learn'
                fs.readFile(rootDir + req.url, function (err, data) {
                res.writeHead(200, {
                        'Content-Type': 'text/html',
                        'Content-Length': data.length
                });
                res.write(data);
                res.end();
                });
        } else {
                var urlPara = url.parse(req.url, true);
                var strName = urlPara.query.name;
                if (strName) {
                res.write('hello: ' + strName);
                } else {
                res.write("Args error");
                }
                res.end();
        }
        }).listen(8080);

在命令行里运行  

        node server.js

打开浏览器，输入   

        http://localhost:8080/server.js/?name=kerwen

进行测试， 返回 `hello: kerwen`  

### Create html

        <input type="text" id="namevalue"><br>
        <button id="btn16">Send</button>
        结果: <span id="resultid"></span>

### Create js scripts

    $(document).ready(function(){
        $("#btn16").on("click", function(){
                 $.get("server.js", {name:$("#namevalue").val()}, function(data){
                $("#resultid").text(data);
                });
         });
    });

打开浏览器，输入 `http://localhost:8080/index.html`  
输入名字，点击“Send”，会返回结果.    

这地方有个坑，运行html的时候必须保证html的地址和NodeJs的server地址一致。如果直接双击html运行，浏览器打开的html地址应该是类似`c:\..\index.html`，此时发送get请求会抛出一下异常：  

        'Access-Control-Allow-Origin' error  

根据jQuery的api文档描述：  

        Due to browser security restrictions, most "Ajax" requests are subject to the same origin policy; the request can not successfully retrieve data from a different domain, subdomain, port, or protocol.

我尝试将发送格式从`JSON`改成`JSONP`, 结果浏览器在解析返回结果时会抛出另外的异常：  

        Unexpected end of input jquery using ajax  

综上，get请求只能适用于同一domain。  

[https://api.jquery.com/jQuery.get/](https://api.jquery.com/jQuery.get/)  
[https://stackoverflow.com/questions/47523265/jquery-ajax-no-access-control-allow-origin-header-is-present-on-the-requested/47525511](https://stackoverflow.com/questions/47523265/jquery-ajax-no-access-control-allow-origin-header-is-present-on-the-requested/47525511)  
[https://stackoverflow.com/questions/29399996/unexpected-end-of-input-jquery-using-ajax](https://stackoverflow.com/questions/29399996/unexpected-end-of-input-jquery-using-ajax)   