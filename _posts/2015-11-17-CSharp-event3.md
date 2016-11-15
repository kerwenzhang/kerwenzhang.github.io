---
layout: post
title: "C# 事件(三)"
date:   2015-11-17 12:01:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



原文地址： http://www.cnblogs.com/wudiwushen/archive/2010/04/23/1717829.html<br/>   

今天是大白话系列之C#委托与事件讲解的大结局，也是我们最关心的，在日常的MES系统编程中到底怎样使用这样的利器，其实我们每天都在使用事件，一个窗体，一个按钮都包含这事件，只是很少用到自己写的委托和事件，说白了不知道如何下手，也不知道在什么样的场景下应用。<br/>   
<br/>   
用到事件的地方有很多，这次讲解就MES系统开发中我们经常应用的场景。<br/>   
一、通用控件场景<br/>   
通用控件有很多，这里举最常用的万能通用分页控件<br/>   
【注：】本分页控件，只是为了讲解使用，并非真分页控件，还是基于.net控件的分页<br/>   
我们先来看场景<br/>   
<br/>   
![Alt text](/img/3.jpg)   
<br/>   
我们所看到的这个分页控件就是这次讲解的主角，在日常的编程中，像这样功能我们用的做多，所以我们必须要把它抽象出来，不能每个页面都写分页逻辑吧。那我们想想到底怎样去实现这样的功能呢？怎样才能让页面知道我们按了控件的哪个按钮呢？这时候让我们联想一想委托与事件，一定要聚精会神，叮咚！有了，我们可以把这个控件想象成一个发布者，而各个页面就想象成订阅者，或者是观察者，当页面订阅了分页控件的事件后，自然就会相应了嘛？<br/>   
<br/>   
有了思路，我们就开始行动吧！<br/>   
<br/>   
第一步，我们编写发布者代码，也就是这个控件代码<br/>   

	//和我们上一讲讲的一样，我们先定义订阅者所感兴趣的对象，这里我们将它抽象成Action，也就是首页、下页、上页之类的动作

    public class PageChangeEventArgs : EventArgs   
    {   
        private string action = string.Empty;   
        public string Action   
        {   
            get   
            {   
                return this.action;   
            }   
            set   
            {   
                this.action = value;   
            }   
        }   

        public PageChangeEventArgs()   
        {   

        }        

        public PageChangeEventArgs(String paramAction)   
        {   
            this.Action = paramAction;   
        }   
    }   

    //发布者代码 也就是控件代码   
    public partial class UIPageControlsNavigator : System.Web.UI.UserControl   
    {   
        //这里我们声明一个页面改变的委托[注：命名一定要规范]   
        public delegate void PageChangeEventHandler(object sender, PageChangeEventArgs e);   
        //这里我们声明一个事件   
         public event PageChangeEventHandler PageChange;   
        //然后以个保护类型的OnPageChange方法   
         protected virtual void OnPageChange(PageChangeEventArgs e)   
        {   
            if (PageChange != null)   
            {   
                PageChange(this, e);   
            }   
        }   

        //这里就是上一讲中，具体的触发函数,这里变成了一个按钮触发事件   
         protected void lbtnFirst_Click(object sender, EventArgs e)   
        {   
            //这时候，订阅者关心的对象e，也就是触发的是“首页”这个按钮   
            OnPageChange(new PageChangeEventArgs("First"));   
        }   

        protected void lbtnPrevious_Click(object sender, EventArgs e)   
        {   
            //这时候，订阅者关心的对象e，也就是触发的是“下页”这个按钮   
            OnPageChange(new PageChangeEventArgs("Previous"));   
        }   

        protected void lbtnLast_Click(object sender, EventArgs e)   
        {   
            OnPageChange(new PageChangeEventArgs("Last"));   
        }   

        protected void lbtnNext_Click(object sender, EventArgs e)   
        {   
            OnPageChange(new PageChangeEventArgs("Next"));   
        }   

        protected void btnSearch_Click(object sender, EventArgs e)   
        {   
            if (IsNumber(txtSearchPageCount.Text))   
            {   
                OnPageChange(new PageChangeEventArgs("Search"));   
            }   
        }   

        protected void cmbPerPage_SelectedIndexChanged(object sender, EventArgs e)   
        {   
            OnPageChange(new PageChangeEventArgs("PageSizeChanged"));   
        }    
        
        ....   

        #region public void BindData(GridView myGridView, IList businessObjects, PageChangeEventArgs e)

        /// <summary>   
        /// 具体控件分页功能实现   
         /// </summary>   
        /// <param name="myGridView">当前Grid控件</param>   
        /// <param name="businessObjects">数据源</param>   
        /// <param name="e">事件对象</param>   
        public void BindData(GridView myGridView, IList businessObjects, PageChangeEventArgs e)   
        {   
            // 计算页面数   
            if (businessObjects == null)   
            {   
                this.RowCount = 0;   

            }   
            else   
            {   
                this.RowCount = businessObjects.Count;   
            }   

            double pageCount = (double)RowCount / this.PageSize;   
            this.PageCount = (int)Math.Ceiling(pageCount);   
            myGridView.DataSource = businessObjects;   
            myGridView.PageSize = this.PageSize;   
            switch (e.Action)   
            {   
                case "PageLoad":   
                    if (CurrentPage > 0)   
                    {   
                        myGridView.PageIndex = CurrentPage - 1;   
                    }    
                    break;   
                case "First":   
                    myGridView.PageIndex = 0;   
                    myGridView.EditIndex = -1;   
                    break;   
                case "Previous":   
                    myGridView.PageIndex--;   
                    myGridView.EditIndex = -1;   
                    break;   
                case "Next":   
                    myGridView.PageIndex++;   
                    myGridView.EditIndex = -1;   
                    break;   
                case "Last":   
                    myGridView.PageIndex = this.PageCount - 1;   
                    myGridView.EditIndex = -1;   
                    break;   
                case "PageSizeChanged":   
                    myGridView.PageIndex = 0;   
                    myGridView.EditIndex = -1;   
                    break;   
                case "Search":   
                    myGridView.PageIndex = int.Parse(txtSearchPageCount.Text) - 1;   
                    break;   
                case "Refresh":   
                    break;   
                default:   
                    myGridView.PageIndex = 0;   
                    break;   
            }   
            // 页数不够了，进行调整   
            if (myGridView.PageIndex >= this.PageCount)   
            {   
                myGridView.PageIndex = this.PageCount == 0 ? 0 : this.PageCount - 1;   
            }   
            myGridView.DataBind();   
            // 获取按钮的状态   
            this.GetButtonState(myGridView);   
        }   

        #endregion   

    }   

当然控件代码还不值这些，我这里就列举出我们委托事件需要的代码：<br/>   
<br/>   
然后我们看一下调用页面的代码，也就是观察者，本例中是角色页面RoleManage.aspx<br/>   

    //角色管理页面代码类   
    public partial class RoleManage : BasePage   
    {   
        protected void Page_Load(object sender, EventArgs e)   
        {   
            //在当前页面订阅控件的点击事件   
            this.myNavigator.PageChange += new PageChangeEventHandler(this.myNavigator_PageChange);   
            if (!Page.IsPostBack)   
            {   

            }   
        }   
        
        //具体的点击触发函数功能，这里就是控件的分页   
        private void myNavigator_PageChange(object sender, PageChangeEventArgs e)   
        {   
            this.GetAllRoles(e);   
        }   

        private void GetAllRoles(PageChangeEventArgs e)   
        {   
            try   
            {   
                //角色数据源   
                roles = roleService.GetAllRoles();   
                //调用控件的分页功能函数，这个封装在分页控件里可以，封装在通用的类库里也行   
                this.myNavigator.BindData(this.grdRole, roles, e);   
                
            }   
            catch (Exception myException)   
            {   
                return;   
            }   
        }   

	}

 其实原理很简单，当控件上按下下页或者其它按钮的时候，这时候因为角色管理页面已经订阅了这个事件，所以它会执行具体委托的那个实体函数，就这么简单<br/>   
<br/>   
大家了看了可能会头大，那就自己动手试着做一下，只有做了才能真正的体会到里面的奥妙，其实和我上一讲内容很相识，只是稍微有一点点的变化而已。<br/>   
<br/>   
 <br/>   
<br/>   
<br/>   
二、业务控件场景<br/>   
<br/>   
大家在做MES系统的时候，50%的时候是在复制黏贴，甚至有的时候有些逻辑老是复制到这里，然后复制到那里，当然起初的时候感觉很快，也不用动脑子ctrl+c,ctrl+v结束，但是到后来逻辑改了，那时候就像没头苍蝇似的，早就忘了到底有多少地方用到这些逻辑，所以往往到BUG发生的时候，才恍然大悟“哦！原来这里忘了改了！”等等。我并不反对大家ctrl+c,ctrl+v，但是在享受这样的快捷之后，腾出时间再来重构一下，看看这时候能否用是否能抽象呀？用设计模式？符不符合00的设计原则？不然你就是编10年的软件，又能得到什么样的提高！又扯远了。。。<br/>   
<br/>   
 <br/>   
<br/>   
接下来，我们具体来看场景：<br/>   
<br/>   
 <br/>   
<br/>   
 <br/>   
<br/>   
 这是一个工作流审批用户控件，做MES系统的其实经常会和这个打交道，然而我们把这个逻辑封装成一个控件，那我们在今后维护上将会减轻很多工作量<br/>   
<br/>   
这里我只介绍这控件技术上我们用到的委托和事件的代码<br/>   

	public partial class ApprovalResults : System.Web.UI.UserControl
	{
		//EventHandler是微软默认的委托，在本例中我们直接就用EventHandler来表示委托，当然它的参数是Sender,e
		public event EventHandler Preview;
		public event EventHandler Submit;
		public event EventHandler FMOK;
		public event EventHandler FMProgress;
		public event EventHandler FMSave;

		...
		//提交按钮事件
		protected void btnSubmit_Click(object sender, EventArgs e)
		{
			try
			{
				//触发我们定义的事件
				Submit(sender, e);
			}
			catch (Exception ex)
			{
				...
			}
		}  ...
	}

然后我们到订阅这个事件的页面上看一下代码<br/>   

    public partial class Preview : BasePage   
    {   
        protected void Page_Load(object sender, EventArgs e)   
        {   
            ...   
            //在次页面中订阅审批控件的提交按钮事件   
            ApprovalResults1.Submit += new EventHandler(ApprovalResults1_Submit);   
        }   
        
        //具体的提交事件功能函数   
        public void ApprovalResults1_Submit(object sender, EventArgs e)   
        {            
            try   
            {                
            }   
            catch (Exception ex)   
            {               
            }   
            finally   
            {             
            }   
        }   
    }   

这样我想大家都理解了，当审批控件点击提交按钮，其实访问的就是订阅者页面的功能函数。<br/>   
<br/>   
其实委托事件应用的场景还有很多，它就是观察者模式的提炼。<br/>   
<br/>   
到此委托与事件讲解的大白话系列到此完毕，我非常希望大家能看了我的文章后能有点收获。