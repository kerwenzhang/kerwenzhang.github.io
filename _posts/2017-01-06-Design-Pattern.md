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


## 抽象工厂模式

抽象工厂模式提供一个接口， 用于创建相关或依赖对象的家族， 而不需要明确指定具体类。

    //两种抽象产品：水果、蔬菜
    public interface Fruit
    {
    }
    public interface Veggie
    {
    }
    
    //四种具体产品：北方水果，热带水果，北方蔬菜，热带蔬菜
    /北方水果
    public class NorthernFruit implements Fruit
    {
        private String name;
        public NorthernFruit(String name)
        {
        }
    }
    //热带水果
    public class TropicalFruit implements Fruit
    {
        private String name;
        public TropicalFruit(String name)
        {
        }
    }
    
    //北方蔬菜
    public class NorthernVeggie implements Veggie
    {
        private String name;
        public NorthernVeggie(String name)
        {
        }    
    }
    //热带蔬菜
    public class TropicalVeggie implements Veggie
    {
        private String name;
        public TropicalVeggie(String name)
        {
        }   
    }
    
    //抽象工厂角色
    public interface Gardener
    {
        public Fruit createFruit(String name);
        public Veggie createVeggie(String name);
    }
    
    //具体工厂角色：北方工厂
    public class NorthernGardener implements Gardener
    {
        public Fruit createFruit(String name)
        {
            return new NorthernFruit(name);
        }
        public Veggie createVeggie(String name)
        {
            return new NorthernVeggie(name);
        }
    }
    //热带工厂
    public class TropicalGardener implements Gardener
    {
        public Fruit createFruit(String name)
        {
            return new TropicalFruit(name);
        }
        public Veggie createVeggie(String name)
        {
            return new TropicalVeggie(name);
        }
    }
    
    int main()
    {
        NorthernGardener north = new NorthernGardener();
        north.createFruit();
        north.createVeggie();
    }
    
