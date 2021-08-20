---                
layout: post                
title: "SAFEARRAY的用法" 
date:   2021-08-20 14:30:00                 
categories: "MFC"                
catalog: true                
tags:                 
    - MFC                
---      

什么是SAFEARRAY呢？可以理解为一个数组，可以定义维数、长度、边界、元素类型等信息，差不多相当于C#中的List. 在编写COM组件时，需要一次传递很多的数据时，使用SAFEARRAY会很方便   
首先要知道，SafeArray也并不单独使用，而是将其再包装到VARIANT类型的变量中，然后才作为参数传送出去。  
一、要打包的数据和需要定义的变量  

	_variant_t vValue[4];
	vValue[0] = _bstr_t("CSDN");
	vValue[1] = _bstr_t("心中有道");
	vValue[2] = _bstr_t("博客");
	vValue[3] = _bstr_t("SAFEARRAY");
 
	SAFEARRAY *psaValue;
	SAFEARRAYBOUND rgsaBound[1];
	VARIANT vsaValue;

`SAFEARRAY`就是所谓的安全数组，`psaValue`是一个指向SAFEARRAY的指针，

## SAFEARRAYBOUND  
在VC中，`SAFEARRAYBOUND`的定义如下：  

	typedef struct tagSAFEARRAYBOUND
	{
		ULONG cElements;
		LONG lLbound;
	} 	SAFEARRAYBOUND;
 
	typedef struct tagSAFEARRAYBOUND *LPSAFEARRAYBOUND;

`SAFEARRAYBOUND`是一个结构体，里面有两个变量   
`ULONG cElements`表示的是元素的数目（更准确的说是在本维中的数目）    
`LONG lLbound`表示的是一个逻辑起点序号，实际访问内存的时候，安全数组会将程序指定的序号减去`lLbound`，比如你将其设置为`10000`, `a[10000]`这相当于`A[0]`，`a[999]`数组越界，所以在没有特殊要求的情况下，`lLbound`一般为`0`。  
还有一点，定义的时候是`SAFEARRAYBOUND rgsaBound[1]`  
`rgsaBound[1]`表示的是一位数组，二维数组要定义为`rgsaBound[2]`  

`VARIANT vsaValue` 这个就是最终要的得到的变量了，可以把这个变量作为参数传出去。

## 实现代码及函数、参数意义

	psaValue = SafeArrayCreate(VT_VARIANT, 1, rgsaBound); 
	for (long i = 0; i < 4; i++)
	{
		SafeArrayPutElement(psaValue, &i, &vValue[i]);
	}
 
	vsaValue.vt = VT_ARRAY | VT_VARIANT; 
	V_ARRAY(&vsaValue) = psaValue;

### 创建SAFEARRAY

	psaValue = SafeArrayCreate(VT_VARIANT, 1, rgsaBound);

第一个参数`VT_VARIANT`表示数组的类型，第二个参数表示创建数组的维数，本例中是一维，第三个参数是对这个数组各个维度的描述。
`SafeArrayCreate()`就是创建`SAFEARRAY`的函数，准确的说是在堆中创建了一个`SAFEARRAY`，也就是说在这个函数里面，调用了`new`或者`malloc()`之类的申请了一个空间。 

### 放置元素到数组中

    long demen[1];
	for (int i = 0; i < 4; i++)
	{
		demen[i] = i;
		SafeArrayPutElement(psaValue, demen, &vValue[i]);
	}

第一个参数是指向`SAFEARRAY`的指针；第二个参数是`long`型数组指针，表示`SAFEARRAY`元素的下标，即唯一确定一个`SAFEARRAY`元素；第三个参数就是要放置的那个值的指针了。   

### 指明vsaValue存放值得类型  

	vsaValue.vt = VT_ARRAY | VT_VARIANT;

在`VARIANT`的`vt`成员的值如果包含`VT_ARRAY`，那么它所封装的就是一个`SAFEARRAY`，它的`parray`成员即是指向`SAFEARRAY`的指针。
`VT_ARRAY`说明`vsaValue`封装的是一个`SAFEARRAY`，`VT_VARIANT`说明`SAFEARRAY`的元素是VARIANT类型。  

### 完成封装

	V_ARRAY(&vsaValue) = psaValue; //等价于vsaValue.parray = psaValue


## 参考

[SAFEARRAY基本用法详解](https://blog.csdn.net/u010204038/article/details/38085931)  
[SAFEARRAY](https://blog.csdn.net/qq_36196748/article/details/82424545)