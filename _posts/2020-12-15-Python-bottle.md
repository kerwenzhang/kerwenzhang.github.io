---                
layout: post                
title: "Python动态生成html页面" 
date:   2020-12-15 10:30:00                 
categories: "Python"                
catalog: true                
tags:                 
    - Python                
---      

使用bottle的template生成 html页面，可以传入参数：

    from bottle import template
    def WriteHtmlReport(htmlPath):    
        template_demo="""
        <html>
            <body>
                Hi { {Author} }
            </body>
        </html>
        """
        htmlTemp = template(template_demo, Author="Test")
        with open(htmlPath, 'wb') as f:
            f.write(htmlTemp.encode('utf-8'))

支持`for`循环:

    template_demo="""
    <html>
        <body>
            % for file in commit.CommitFiles:
                { {file} }</br>
            %end
        </body>
    </html>    
    """
    htmlTemp = template(template_demo, commit=commit)
    with open(htmlPath, 'wb') as f:
        f.write(htmlTemp.encode('utf-8'))

支持`if`语句:

    template_demo="""
    <html>
        <body>
            <font color={ {"green" if BuildResult=="SUCCESS" else "red"} }> { {BuildResult} }</font>
        </body>
    </html>    
    """
    htmlTemp = template(template_demo, BuildResult="SUCCESS")
    with open(htmlPath, 'wb') as f:
        f.write(htmlTemp.encode('utf-8'))


[Bottle API](http://www.bottlepy.org/docs/dev/stpl.html#template-functions)  
[Python利用bottle来动态生成本地html页面](https://www.jianshu.com/p/d8a52e854675)  
[https://www.cnblogs.com/fhkankan/p/12978622.html](https://www.cnblogs.com/fhkankan/p/12978622.html)  