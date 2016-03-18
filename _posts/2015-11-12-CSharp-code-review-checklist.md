---
layout: postlayout
title: "C# Code Review Checklist"
date:   2015-11-12 17:05:00 
categories: [C#]
tags: [C#]
---

1.Prefer the 'is' or 'as' operator to type casts. Try to avoid casting directly.  
	
	if(myObj is Class1)
	{
		// do something
	}

	string s = myObject as string;
	if(s != null)
	{
		// do something
	}
	
Bad: string s = (string)myObject;  

2.Prefer StringBuilder to string concatenation  
  String is used to save string data, StringBulder is used to string operation: Add, append, delete string.  
	
	StringBuilder sb = new StringBuilder(str1,50);
	sb.Append(str2);
	sb.Append(str3);
	sb.Append(str4);
	
3.Avoid using static classes as a miscellaneous bucket.  
4.Prefer 'enum' to static constants.   
5.Avoid using 'out' and 'ref' parameters on public methods, if possible.  
6.Always test delegates against null before raising events  
	
	public void RaiseEvent(ElementAddedEventArgs e)
	{
		if(Element_Added != null)
		{
			Element_Added(this, e);
		}
	}
	
7.Avoid using GC.Collect()  
8.Prefer 'foreach' to 'for' or 'do while'.  
9.Prefer XmlTextReader over XmlDocument or XPathDocument when parsing large XML documents for one time use.  
10.Limit visibility of types in the assembly. Not every class and method need to be public  
11.Prefer Try-Parse pattern if type supports it to void expensive exception handling  