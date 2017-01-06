---
layout: post
title: 设计模式
date:   2017-01-06 13:30:14
categories: "C#"
catalog: true
tags: 
    - C#
---



## 简单工厂模式

    class Parent {  virtual Function()=0;}
    class ChildA {}
    class ChildB {}
    
    class Factory
    {
        public Parent GetInstance(type)
        {
            if(type is A)
            {
                return new ChildA();
            }
            else
            {
                return new ChildB();
            }
        }
    }
    
    class Implement
    {
        public void GetInstance()
        {
            Factory fac = new Factory();
            Parent instance = fac.GetInstance(type);
            instance.Function();
        }
    }
    
## 工厂模式

工厂模式定义了一个创建对象的接口， 由子类决定要实例化的类是哪一个。 工厂方法让类把实例化推迟到子类。

    public abstract class Pizza
	{
        protected string name;
        public virtual string Bake()
		{
        }
    }
    
    public class Pizza_KindA : Pizza
    {
        name = "Kind A Pizza";
    }
    
    public class Pizza_KindB : Pizza
    {
        name = "Kind B Pizza";
    }
    
    public abstract class PizzaStore
	{
        public Pizza OrderPizza(string type)
		{
			Pizza pizza = CreatePizza(type);

			pizza.Bake();

			return pizza;
		}
        
        protected abstract Pizza CreatePizza(string type);
    }
    
    public class PizzaStoreI : PizzaStore
	{
        protected override Pizza CreatePizza(string type)
		{
			if(type.Equals("A"))
			{
				return new Pizza_KindA();
			}
            if(type.Equals("B"))
            {
                return new Pizza_KindB();
            }
			else return null;
		}
    }
    
    int main()
    {
        PizzaStore store = new PizzaStoreI();
        store.OrderPizza("A");
    }
