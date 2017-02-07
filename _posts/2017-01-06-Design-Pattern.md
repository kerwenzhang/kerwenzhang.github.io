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

## 外观模式(Facade)

为子系统中的一组接口提供一个一致的界面， 此模式定义了一个高层接口， 这个接口使得这一子系统更加容易使用。  

用途：  
在设计初期阶段， 应该要有意识的将不同的两个层分离。 层与层之间建立外观Facade， 这样可以为复杂的子系统提供一个简单的接口， 使得耦合大大降低。  
在开发阶段， 子系统旺旺因为不断的重构演化而变得越来越复杂。增加外观Facade可以提供一个简单的接口， 减少它们之间的依赖。  
在维护一个遗留的大型系统时， 可能这个系统已经非常难以维护和扩展了， 为新系统开发一个外观Facade类， 来提供遗留代码的比较清晰简单的接口， 让新系统与Facade对象交互。  

    //股票1
    class Stock1
    {
        public void Sell()
        {
            Console.WriteLine(" 股票1卖出");
        }
        public void Buy()
        {
            Console.WriteLine(" 股票1买入");
        }
    }
    
    //国债1
    class NationalDebt1
    {
        public void Sell()
        {
            Console.WriteLine(" 国债1卖出");
        }
        public void Buy()
        {
            Console.WriteLine(" 国债1买入");
        }
    }

    //房地产1
    class Realty1
    {
        public void Sell()
        {
            Console.WriteLine(" 房产1卖出");
        }
        public void Buy()
        {
            Console.WriteLine(" 房产1买入");
        }
    }
    
    class Fund
    {
        Stock1 gu1;
        NationalDebt1 nd1;
        Realty1 rt1;

        public Fund()
        {
            gu1 = new Stock1();
            nd1 = new NationalDebt1();
            rt1 = new Realty1();
        }

        public void BuyFund()
        {
            gu1.Buy();
            nd1.Buy();
            rt1.Buy();
        }

        public void SellFund()
        {
            gu1.Sell();
            nd1.Sell();
            rt1.Sell();
        }
    }
    
    int Main(string[] args)
    {

        Fund jijin = new Fund();

        jijin.BuyFund();
        jijin.SellFund();
    }
    
## 建造者模式（Builder）

将一个复杂对象的构建与它的表示分离， 使得同样的构建过程可以创建不同的表示。  
主要是用于创建一些复杂的对象， 这些对象内部构建间的建造顺序通常是稳定的， 但对象内部的构建通常面临着复杂的变化。  
建造者模式的好处就是使得建造代码与表示代码分离，由于建造者隐藏了该产品是如何组装的， 所以若需要改变一个产品的内部表示， 只需要再定义一个具体的建造者就可以了  
建造者模式是在当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时适用的模式。  


    abstract class PersonBuilder
    {
        protected Graphics g;
        protected Pen p;

        public PersonBuilder(Graphics g, Pen p)
        {
            this.g = g;
            this.p = p;
        }

        public abstract void BuildHead();
        public abstract void BuildBody();
        public abstract void BuildArmLeft();
        ...
    }

    class PersonThinBuilder : PersonBuilder
    {
        public PersonThinBuilder(Graphics g, Pen p)
            : base(g, p)
        { }

        public override void BuildHead()
        {
            g.DrawEllipse(p, 50, 20, 30, 30);
        }

        public override void BuildBody()
        {
            g.DrawRectangle(p, 60, 50, 10, 50);
        }

        public override void BuildArmLeft()
        {
            g.DrawLine(p, 60, 50, 40, 100);
        }
        ...
    }

    class PersonFatBuilder : PersonBuilder
    {
        public PersonFatBuilder(Graphics g, Pen p)
            : base(g, p)
        { }

        public override void BuildHead()
        {
            g.DrawEllipse(p, 50, 20, 30, 30);
        }

        public override void BuildBody()
        {
            g.DrawEllipse(p, 45, 50,40, 50);
        }

        public override void BuildArmLeft()
        {
            g.DrawLine(p, 50, 50, 30, 100);
        }
        ....
    }

    class PersonDirector
    {
        private PersonBuilder pb;
        public PersonDirector(PersonBuilder pb)
        {
            this.pb = pb;
        }

        public void CreatePerson()
        {
            pb.BuildHead();
            pb.BuildBody();
            pb.BuildArmLeft();
            ...
        }
    }
    
    int main()
    {
        PersonThinBuilder ptb = new PersonThinBuilder(pictureBox1.CreateGraphics(), new pen());
        PersonDirector pdThin = new PersonDirector(ptb);
        pdThin.CreatePerson();

        PersonFatBuilder pfb = new PersonFatBuilder(pictureBox2.CreateGraphics(), new pen());
        PersonDirector pdFat = new PersonDirector(pfb);
        pdFat.CreatePerson();
    }
    

## 观察者模式(Observer)

观察者模式定义了一种一对多的依赖关系， 让多个观察者对象同时监听某一个主题对象。 这个主题对象在状态发生变化时， 会通知所有观察者对象， 使它们能够自动更新自己。  
当一个抽象模型有两个方面， 其中一方面依赖于另一方面， 这时用观察者模式可以将这两者封装在独立的对象中使它们各自独立的改变和复用。  
观察者模式所做的工作其实就是在解除耦合。 让耦合的双方都依赖于抽象， 而不是依赖于具体。 从而使得各自的变化都不会影响另一边的变化。  

    //通知者接口
    interface Subject
    {
        void Notify();
        string SubjectState
        {
            get;
            set;
        }
    }

    //事件处理程序的委托
    delegate void EventHandler();

    class Secretary : Subject
    {
        //声明一事件Update，类型为委托EventHandler
        public event EventHandler Update;

        private string action;

        public void Notify()
        {
            Update();
        }
        public string SubjectState
        {
            get { return action; }
            set { action = value; }
        }
    }

    class Boss : Subject
    {
        //声明一事件Update，类型为委托EventHandler
        public event EventHandler Update;

        private string action;

        public void Notify()
        {
            Update();
        }
        public string SubjectState
        {
            get { return action; }
            set { action = value; }
        }
    }

    //看股票的同事
    class StockObserver
    {
        private string name;
        private Subject sub;
        public StockObserver(string name, Subject sub)
        {
            this.name = name;
            this.sub = sub;
        }

        //关闭股票行情
        public void CloseStockMarket()
        {
            Console.WriteLine("{0} {1} 关闭股票行情，继续工作！", sub.SubjectState, name);
        }
    }

    //看NBA的同事
    class NBAObserver
    {
        private string name;
        private Subject sub;
        public NBAObserver(string name, Subject sub)
        {
            this.name = name;
            this.sub = sub;
        }

        //关闭NBA直播
        public void CloseNBADirectSeeding()
        {
            Console.WriteLine("{0} {1} 关闭NBA直播，继续工作！", sub.SubjectState, name);
        }
    }
    
    int main()
    {
        //老板胡汉三
        Boss huhansan = new Boss();

        //看股票的同事
        StockObserver tongshi1 = new StockObserver("魏关姹", huhansan);
        //看NBA的同事
        NBAObserver tongshi2 = new NBAObserver("易管查", huhansan);

        huhansan.Update += new EventHandler(tongshi1.CloseStockMarket);
        huhansan.Update += new EventHandler(tongshi2.CloseNBADirectSeeding);

        //老板回来
        huhansan.SubjectState = "我胡汉三回来了！";
        //发出通知
        huhansan.Notify();
    }
    
## 状态模式(State)

当一个对象的内在状态改变时允许改变其行为， 这个对象看起来像是改变了其类。  
状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况。 把状态的判断逻辑转移到表示不同状态的一系列类当中， 可以把复杂的判断逻辑简化。  
状态模式的好处是将与特定状态相关的行为局部化， 并且将不同状态的行为分割开来。  
当一个对象的行为取决于它的状态， 并且它必须在运行时刻根据状态改变它的行为时， 就可以考虑使用状态模式了。  

    //抽象状态
    public abstract class State
    {
        public abstract void WriteProgram(Work w);
    }

    //上午工作状态
    public class ForenoonState : State
    {
        public override void WriteProgram(Work w)
        {
            if (w.Hour < 12)
            {
                Console.WriteLine("当前时间：{0}点 上午工作，精神百倍", w.Hour);
            }
            else
            {
                w.SetState(new NoonState());
                w.WriteProgram();
            }
        }
    }

    //中午工作状态
    public class NoonState : State
    {
        public override void WriteProgram(Work w)
        {
            if (w.Hour < 13)
            {
                Console.WriteLine("当前时间：{0}点 饿了，午饭；犯困，午休。", w.Hour);
            }
            else
            {
                w.SetState(new AfternoonState());
                w.WriteProgram();
            }
        }
    }

    //下午工作状态
    public class AfternoonState : State
    {
        public override void WriteProgram(Work w)
        {
            if (w.Hour < 17)
            {
                Console.WriteLine("当前时间：{0}点 下午状态还不错，继续努力", w.Hour);
            }
            else
            {
                w.SetState(new EveningState());
                w.WriteProgram();
            }
        }
    }
    ...
    
    //工作
    public class Work
    {
        private State current;
        public Work()
        {
            current = new ForenoonState();
        }

        private double hour;
        public double Hour
        {
            get { return hour; }
            set { hour = value; }
        }

        private bool finish = false;
        public bool TaskFinished
        {
            get { return finish; }
            set { finish = value; }
        }


        public void SetState(State s)
        {
            current = s;
        }

        public void WriteProgram()
        {
            current.WriteProgram(this);
        }
    }
    
    static void Main(string[] args)
    {
        //紧急项目
        Work emergencyProjects = new Work();
        emergencyProjects.Hour = 9;
        emergencyProjects.WriteProgram();
        emergencyProjects.Hour = 10;
        emergencyProjects.WriteProgram();
        ...
    }
    
## 适配器模式(Adapter)

将一个类的接口转换成客户希望的另外一个接口。 适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。  
系统的数据和行为都正确， 但接口不符时， 我们应该考虑用适配器， 目的是使控制范围之外的一个原有对象与某个接口匹配。 适配器模式主要应用于希望复用一些现存的类， 但是接口又与复用环境要求不一致的情况。  

    //篮球运动员
    abstract class Player
    {
        protected string name;
        public Player(string name)
        {
            this.name = name;
        }

        public abstract void Attack();
        public abstract void Defense();
    }

    //前锋
    class Forwards : Player
    {
        public Forwards(string name)
            : base(name)
        {
        }

        public override void Attack()
        {
            Console.WriteLine("前锋 {0} 进攻", name);
        }

        public override void Defense()
        {
            Console.WriteLine("前锋 {0} 防守", name);
        }
    }
    
    //外籍中锋
    class ForeignCenter
    {
        private string name;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public void 进攻()
        {
            Console.WriteLine("外籍中锋 {0} 进攻", name);
        }

        public void 防守()
        {
            Console.WriteLine("外籍中锋 {0} 防守", name);
        }
    }

    //翻译者
    class Translator : Player
    {
        private ForeignCenter wjzf = new ForeignCenter();

        public Translator(string name)
            : base(name)
        {
            wjzf.Name = name;
        }

        public override void Attack()
        {
            wjzf.进攻();
        }

        public override void Defense()
        {
            wjzf.防守();
        }
    }
    
    static void Main(string[] args)
    {
        Player b = new Forwards("巴蒂尔");
        b.Attack();
        
        Player ym = new Translator("姚明");
        ym.Attack();
        ym.Defense();

        Console.Read();
    }
    
## 备忘录模式(Memento)

在不破坏封装性的前提下， 捕获一个对象的内部状态， 并在该对象之外保存这个状态。 这样以后就可将该对象恢复到原先保存的状态。  
Memento模式比较适用于功能比较复杂的， 但需要维护或记录属性历史的类， 或者需要保存的属性只是众多属性中的一小部分时， Originator可以根据保存的Memento信息还原到前一状态。  

    class GameRole
    {
        //生命力
        private int vit;
        public int Vitality
        {
            get { return vit; }
            set { vit = value; }
        }

        //攻击力
        private int atk;
        public int Attack
        {
            get { return atk; }
            set { atk = value; }
        }

        //防御力
        private int def;
        public int Defense
        {
            get { return def; }
            set { def = value; }
        }

        //状态显示
        public void StateDisplay()
        {
            Console.WriteLine("角色当前状态：");
            Console.WriteLine("体力：{0}", this.vit);
            Console.WriteLine("攻击力：{0}", this.atk);
            Console.WriteLine("防御力：{0}", this.def);
            Console.WriteLine("");
        }

        //保存角色状态
        public RoleStateMemento SaveState()
        {
            return (new RoleStateMemento(vit, atk, def));
        }

        //恢复角色状态
        public void RecoveryState(RoleStateMemento memento)
        {
            this.vit = memento.Vitality;
            this.atk = memento.Attack;
            this.def = memento.Defense;
        }


        //获得初始状态
        public void GetInitState()
        {
            this.vit = 100;
            this.atk = 100;
            this.def = 100;
        }

        //战斗
        public void Fight()
        {
            this.vit = 0;
            this.atk = 0;
            this.def = 0;
        }
    }

    //角色状态存储箱
    class RoleStateMemento
    {
        private int vit;
        private int atk;
        private int def;

        public RoleStateMemento(int vit, int atk, int def)
        {
            this.vit = vit;
            this.atk = atk;
            this.def = def;
        }

        //生命力
        public int Vitality
        {
            get { return vit; }
            set { vit = value; }
        }

        //攻击力
        public int Attack
        {
            get { return atk; }
            set { atk = value; }
        }

        //防御力
        public int Defense
        {
            get { return def; }
            set { def = value; }
        }
    }

    //角色状态管理者
    class RoleStateCaretaker
    {
        private RoleStateMemento memento;

        public RoleStateMemento Memento
        {
            get { return memento; }
            set { memento = value; }
        }
    }
    
    static void Main(string[] args)
    {
        //大战Boss前
        GameRole lixiaoyao = new GameRole();
        lixiaoyao.GetInitState();
        lixiaoyao.StateDisplay();

        //保存进度
        RoleStateCaretaker stateAdmin = new RoleStateCaretaker();
        stateAdmin.Memento = lixiaoyao.SaveState();

        //大战Boss时，损耗严重
        lixiaoyao.Fight();
        lixiaoyao.StateDisplay();

        //恢复之前状态
        lixiaoyao.RecoveryState(stateAdmin.Memento);

        lixiaoyao.StateDisplay();

        Console.Read();

    }
    
## 组合模式（Composite）

将对象组合成属性结构以表示‘部分-整体’的层次结构。 组合模式使得用户对单个对象和组合对象的使用具有一致性。  
如果发现需求中是体现部分与整体层次的结构时， 以及希望用户可以忽略组合对象与单个对象的不同， 统一地使用组合结构中的所有对象时， 就应该考虑用组合模式了。  

    abstract class Component
    {
        protected string name;

        public Component(string name)
        {
            this.name = name;
        }

        public abstract void Add(Component c);
        public abstract void Remove(Component c);
        public abstract void Display(int depth);
    }

    class Composite : Component
    {
        private List<Component> children = new List<Component>();

        public Composite(string name)
            : base(name)
        { }

        public override void Add(Component c)
        {
            children.Add(c);
        }

        public override void Remove(Component c)
        {
            children.Remove(c);
        }

        public override void Display(int depth)
        {
            Console.WriteLine(new String('-', depth) + name);

            foreach (Component component in children)
            {
                component.Display(depth + 2);
            }
        }
    }

    class Leaf : Component
    {
        public Leaf(string name)
            : base(name)
        { }

        public override void Add(Component c)
        {
            Console.WriteLine("Cannot add to a leaf");
        }

        public override void Remove(Component c)
        {
            Console.WriteLine("Cannot remove from a leaf");
        }

        public override void Display(int depth)
        {
            Console.WriteLine(new String('-', depth) + name);
        }
    }
    
    static void Main(string[] args)
    {
        Composite root = new Composite("root");
        root.Add(new Leaf("Leaf A"));
        root.Add(new Leaf("Leaf B"));

        Composite comp = new Composite("Composite X");
        comp.Add(new Leaf("Leaf XA"));
        comp.Add(new Leaf("Leaf XB"));

        root.Add(comp);

        Composite comp2 = new Composite("Composite XY");
        comp2.Add(new Leaf("Leaf XYA"));
        comp2.Add(new Leaf("Leaf XYB"));

        comp.Add(comp2);

        root.Add(new Leaf("Leaf C"));

        Leaf leaf = new Leaf("Leaf D");
        root.Add(leaf);
        root.Remove(leaf);

        root.Display(1);

        Console.Read();
    }
    
