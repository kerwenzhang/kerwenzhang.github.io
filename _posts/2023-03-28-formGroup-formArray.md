---
layout: post
title: formGroup,formControl,formArray
date:   2023-03-28 9:13:14
categories: "Web"
catalog: true
tags: 
    - Web
---

Angular 提供了两种不同的方法来通过表单处理用户输入：响应式表单和模板驱动表单。 两者都从视图中捕获用户输入事件、验证用户输入、创建表单模型、修改数据模型，并提供跟踪这些更改的途径。  
+ 响应式表单  提供对底层表单对象模型直接、显式的访问。它们与模板驱动表单相比，更加健壮：它们的可扩展性、可复用性和可测试性都更高。如果表单是你的应用程序的关键部分，或者你已经在使用响应式表单来构建应用，那就使用响应式表单。

+ 模板驱动表单  依赖模板中的指令来创建和操作底层的对象模型。它们对于向应用添加一个简单的表单非常有用，比如电子邮件列表注册表单。它们很容易添加到应用中，但在扩展性方面不如响应式表单。如果你有可以只在模板中管理的非常基本的表单需求和逻辑，那么模板驱动表单就很合适。  


常用表单基础类  

+ FormControl  追踪单个表单控件的值和验证状态。
+ FormGroup	  追踪一个表单控件组的值和状态。
+ FormArray	追踪表单控件数组的值和状态。
+ ControlValueAccessor 在 Angular 的 FormControl 实例和内置 DOM 元素之间创建一个桥梁

# 响应式表单

## 添加基础表单控件
注册响应式表单模块

    import { ReactiveFormsModule } from '@angular/forms';

    @NgModule({
    imports: [
        // other imports ...
        ReactiveFormsModule
    ],
    })
    export class AppModule { }

生成新的 FormControl

    import { Component } from '@angular/core';
    import { FormControl } from '@angular/forms';

    @Component({
        selector: 'app-name-editor',
        templateUrl: './name-editor.component.html',
        styleUrls: ['./name-editor.component.css']
    })
    export class NameEditorComponent {
        name = new FormControl('');
    }

在模板中注册该控件  

    <label for="name">Name: </label>
    <input id="name" type="text" [formControl]="name">


## 把表单控件分组
单中通常会包含几个相互关联的控件。响应式表单提供了两种把多个相关控件分组到同一个输入表单中的方法。  
+ Form group 定义了一个带有一组控件的表单，你可以把它们放在一起管理。

+ Form array 定义了一个动态表单，你可以在运行时添加和删除控件。  


就像 FormControl 的实例能让你控制单个输入框所对应的控件一样，FormGroup 的实例也能跟踪一组 FormControl 实例（比如一个表单）的表单状态。当创建 FormGroup 时，其中的每个控件都会根据其名字进行跟踪。  


### 创建嵌套的表单组
表单组可以同时接受单个表单控件实例和其它表单组实例作为其子控件。这可以让复杂的表单模型更容易维护，并在逻辑上把它们分组到一起。  

### 更新部分数据模型

patchValue()

## 使用 FormBuilder 服务生成控件
当需要与多个表单打交道时，手动创建多个表单控件实例会非常繁琐。FormBuilder 服务提供了一些便捷方法来生成表单控件。FormBuilder 在幕后也使用同样的方式来创建和返回这些实例，只是用起来更简单。  

### 验证表单
Validators

### 创建动态表单
FormArray 是 FormGroup 之外的另一个选择，用于管理任意数量的匿名控件。像 FormGroup 实例一样，你也可以往 FormArray 中动态插入和移除控件，并且 FormArray 实例的值和验证状态也是根据它的子控件计算得来的。不过，你不需要为每个控件定义一个名字作为 key，因此，如果你事先不知道子控件的数量，这就是一个很好的选择。  

# Reference
[响应式表单](https://angular.cn/guide/reactive-forms)  
[创建表单之FormArray、FormGroup](https://blog.csdn.net/sungoodluck666/article/details/109334760)  
[Angular响应式表单之FormGroup](https://blog.tcs-y.com/2020/07/02/angular-reactive-form-formgroup/)  