---
layout: post
title: "C# Form.Close VS Form.Dispose"
date:   2015-11-24 09:43:00 
categories: "C#"
tags: 
    - C#
---

* content
{:toc}

Form.Close() sends the proper windows messages to shut down the win32 window. During that process, if the form was not shown modally, Dispose is called on the form. Disposing the form frees up the unmanaged resources that the form is holding onto.     

If you do a form1.Show() or Application.Run(new Form1()), Dispose will be called when Close() is called.     

However, if you do form1.ShowDialog() to show the form modally, the form will not be disposed, and you'll need to call form1.Dispose() yourself. I believe this is the only time you should worry about disposing the form yourself.  