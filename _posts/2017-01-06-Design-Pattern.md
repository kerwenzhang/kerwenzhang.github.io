---
layout: post
title: 设计模式
date:   2017-01-06 13:30:14
categories: "Design Pattern"
catalog: true
tags: 
    - Design Pattern
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
    
## 策略模式(Strategy)

定义了算法家族， 分别封装起来， 让它们之间可以互相替换。 从概念上来看， 所有这些算法完成的都是相同的工作， 只是实现不同， 它可以以相同的方式调用所有的算法， 减少了各种算法类与使用算法类之间的耦合。 此模式让算法的变化， 不会影响到使用算法的客户。  

当不同的行为堆砌在一个类中时， 就很难避免使用条件语句来选择合适的行为。 将这些行为封装在一个个独立的Strategy类中， 可以在使用这些行为的类中消除条件语句。  

在实践中， 我们可以用它来封装几乎任何类型的规则， 只要在分析过程中听到需要在不同时间应用不同的业务规则， 就可以考虑使用策略模式处理这种变化的可能性。  

    abstract class CashBase
    {
        public abstract double acceptCash(double money);
    }
    
    class CashNormal : CashBase        // 正常销售
    {
        public override double acceptCash(double money)
        {
            return money;
        } 
    }
    
    class CashRebate : CashBase    // 打折促销
    {
        private double moneyRebate = 1d;
        public CashRebate(string moneyRebate)
        {
            this.moneyRebate = double.Parse(moneyRebate);
        }

        public override double acceptCash(double money)
        {
            return money * moneyRebate;
        } 
    }
    
    class CashReturn : CashBase    // 返利
    {
        private double moneyCondition = 0.0d;
        private double moneyReturn = 0.0d;
        
        public CashReturn(string moneyCondition,string moneyReturn)
        {
            this.moneyCondition = double.Parse(moneyCondition);
            this.moneyReturn = double.Parse(moneyReturn);
        }

        public override double acceptCash(double money)
        {
            double result = money;
            if (money >= moneyCondition)
                result=money- Math.Floor(money / moneyCondition) * moneyReturn;
                
            return result;
        } 
    }
    
    //收费策略Context
    class CashContext
    {
        private CashBase cs;

        public CashContext(CashBase csuper)
        {
            this.cs = csuper;
        }

        //得到现金促销计算结果（利用了多态机制，不同的策略行为导致不同的结果）
        public double GetResult(double money)
        {
            return cs.acceptCash(money);
        }
    }
    
    int main()
    {
        CashContext cc = null;
        switch (type)
        {
            case "正常收费":
                cc = new CashContext(new CashNormal());
                break;
            case "满300返100":
                cc = new CashContext(new CashReturn("300", "100"));
                break;
            case "打8折":
                cc = new CashContext(new CashRebate("0.8"));
                break;
        }
        double result = cc.GetResult(100);
    }
    
策略模式将选择的时机移到了客户端，可以通过和工厂模式结合实现优化：  

    ...
    //收费策略与工厂结合
    class CashContext
    {
        CashSuper cs = null;

        //根据条件返回相应的对象
        public CashContext(string type)
        {
            switch (type)
            {
                case "正常收费":
                    CashNormal cs0 = new CashNormal();
                    cs = cs0;
                    break;
                case "满300返100":
                    CashReturn cr1 = new CashReturn("300", "100");
                    cs = cr1;
                    break;
                case "打8折":
                    CashRebate cr2 = new CashRebate("0.8");
                    cs = cr2;
                    break;
            }
        }

        public double GetResult(double money)
        {
            return cs.acceptCash(money);
        }
    }
    
    int main()
    {
        CashContext csuper = new CashContext(type);
        double totalPrices = csuper.GetResult(100);
    }
    
## 装饰模式(Decorate)

动态的给一个对象添加一些额外的职责， 就增加功能来说， 装饰模式比生成子类更为灵活。  
装饰模式是为已有功能动态地添加更多功能的一种方式。   
当系统需要新功能的时候， 是向旧的类中添加新的代码。 这些新加的代码通常装饰了原有类的核心职责或主要行为。 在主类中添加新的字段， 新的方法和逻辑， 会增加了主类的复杂度。 而这些新加入的东西仅仅是为了满足一些只在某种特定情况下会执行的特殊行为的需要。 而装饰模式提供了一个非常好的解决方案， 它把每个要装饰的功能放在单独的类中，并让这个类包装它所要装饰的对象。  

    class Person
    {
        public Person()
        { }

        private string name;
        public Person(string name)
        {
            this.name = name;
        }

        public virtual void Show()
        {
            Console.WriteLine("装扮的{0}", name);
        }
    }
    
    class Finery : Person
    {
        protected Person component;

        //打扮
        public void Decorate(Person component)
        {
            this.component = component;
        }

        public override void Show()
        {
            if (component != null)
            {
                component.Show();
            }
        }
    }
    
    class TShirts : Finery
    {
        public override void Show()
        {
            Console.Write("大T恤 ");
            base.Show();
        }
    }

    class BigTrouser : Finery
    {
        public override void Show()
        {
            Console.Write("垮裤 ");
            base.Show();
        }
    }
    
    int main()
    {
        Person person = new Person("小菜");
        
        BigTrouser trouser = new BigTrouser();
        TShirts tShirt = new TShirts();
        
        trouser.Decorate(person);
        tShirt.Decorate(trouser);
        tShirt.Show();
    }
    
## 代理模式(Proxy)

为其他对象提供一种代理以控制对这个对象的访问。  
代理模式其实就是在访问对象时引入一定程度的间接性，因为这种间接性， 可以附加多种用途。  

    class SchoolGirl
    {
        private string name;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }
    }
    
    //送礼物
    interface GiveGift
    {
        void GiveDolls();
        void GiveFlowers();
        void GiveChocolate();
    }
    
    // 追求者
    class Pursuit : GiveGift
    {
        SchoolGirl mm;
        public Pursuit(SchoolGirl mm)
        {
            this.mm = mm;
        }
        public void GiveDolls()
        {
            Console.WriteLine(mm.Name + " 送你洋娃娃");
        }

        public void GiveFlowers()
        {
            Console.WriteLine(mm.Name + " 送你鲜花");
        }

        public void GiveChocolate()
        {
            Console.WriteLine(mm.Name + " 送你巧克力");
        }
    }
    
    // 代理者
    class Proxy : GiveGift
    {
        Pursuit gg;
        public Proxy(SchoolGirl mm)
        {
            gg = new Pursuit(mm);
        }


        public void GiveDolls()
        {
            gg.GiveDolls();
        }

        public void GiveFlowers()
        {
            gg.GiveFlowers();
        }

        public void GiveChocolate()
        {
            gg.GiveChocolate();
        }
    }
    
    int Main(string[] args)
    {
        SchoolGirl jiaojiao = new SchoolGirl();
        jiaojiao.Name = "李娇娇";

        Proxy daili = new Proxy(jiaojiao);

        daili.GiveDolls();
        daili.GiveFlowers();
        daili.GiveChocolate();
    }
    
用途：  
远程代理， 也就是为一个对象在不同的地址空间提供局部代表。 这样可以隐藏一个对象存在于不同地址空间的事实。  
虚拟代理， 是根据需要创建开销很大的对象。 通过它来存放实例化需要很长时间的真实对象。  
安全代理， 用来控制真实对象访问时的权限。  
智能指引， 是指当调用真实的对象时， 代理处理另外一些事。  

## 原型模式

用原型实例指定创建对象的种类， 并且通过拷贝这些原型创建新的对象。  
原型模式其实就是从一个对象再创建另外一个可定制的对象， 而且不需知道任何创建的细节。  
一般在初始化的信息不发生变化的情况下， 克隆是最好的办法。 这既隐藏了对象创建的细节， 又对性能是大大的提高。  

浅复制：  

    //简历
    class Resume : ICloneable
    {
        private string name;
        private string sex;
        private string age;

        private WorkExperience work;

        public Resume(string name)
        {
            this.name = name;
            work = new WorkExperience();
        }

        //设置个人信息
        public void SetPersonalInfo(string sex, string age)
        {
            this.sex = sex;
            this.age = age;
        }
        //设置工作经历
        public void SetWorkExperience(string workDate, string company)
        {
            work.WorkDate = workDate;
            work.Company = company;
        }

        public Object Clone()
        {
            return (Object)this.MemberwiseClone();
        }

    }

    //工作经历
    class WorkExperience
    {
        private string workDate;
        public string WorkDate
        {
            get { return workDate; }
            set { workDate = value; }
        }
        private string company;
        public string Company
        {
            get { return company; }
            set { company = value; }
        }
    }
    
    int main()
    {
        Resume a = new Resume("大鸟");
        a.SetPersonalInfo("男", "29");
        a.SetWorkExperience("1998-2000", "XX公司");

        Resume b = (Resume)a.Clone();
        b.SetWorkExperience("1998-2006", "YY企业");
    }
    
深复制：  

    //简历
    class Resume : ICloneable
    {
        private string name;
        private string sex;
        private string age;

        private WorkExperience work;

        public Resume(string name)
        {
            this.name = name;
            work = new WorkExperience();
        }

        private Resume(WorkExperience work)
        {
            this.work = (WorkExperience)work.Clone();
        }

        //设置个人信息
        public void SetPersonalInfo(string sex, string age)
        {
            this.sex = sex;
            this.age = age;
        }
        //设置工作经历
        public void SetWorkExperience(string workDate, string company)
        {
            work.WorkDate = workDate;
            work.Company = company;
        }

        public Object Clone()
        {
            Resume obj = new Resume(this.work);

            obj.name = this.name;
            obj.sex = this.sex;
            obj.age = this.age;


            return obj;
        }

    }

    //工作经历
    class WorkExperience : ICloneable
    {
        private string workDate;
        public string WorkDate
        {
            get { return workDate; }
            set { workDate = value; }
        }
        private string company;
        public string Company
        {
            get { return company; }
            set { company = value; }
        }

        public Object Clone()
        {
            return (Object)this.MemberwiseClone();
        }
    }
    
    static void Main(string[] args)
    {
        Resume a = new Resume("大鸟");
        a.SetPersonalInfo("男", "29");
        a.SetWorkExperience("1998-2000", "XX公司");

        Resume b = (Resume)a.Clone();
        b.SetWorkExperience("1998-2006", "YY企业");
    }
    
## 模板方法

定义一个操作中的算法的骨架， 而将一些步骤延迟到子类中。 模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。  
模板方法模式是通过把不变行为搬移到超类， 去除子类中的重复代码来体现它的优势。