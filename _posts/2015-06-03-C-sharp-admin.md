---
layout: post
title: "C#程序以管理员权限运行"
date:   2015-06-03 10:19:00 
categories: "C#"
catalog: true
tags: 
    - C#
---



转自： &nbsp;<a target="_blank" href="http://www.cnblogs.com/Interkey/p/RunAsAdmin.html">Cosmic_Spy&nbsp;</a>&nbsp;&nbsp;<a target="_blank" href="http://www.cnblogs.com/Interkey/p/RunAsAdmin.html">http://www.cnblogs.com/Interkey/p/RunAsAdmin.html</a></p>   
<p>在Vista 和 Windows 7 及更新版本的操作系统，增加了 UAC(用户账户控制) 的安全机制，如果 UAC 被打开，用户即使以管理员权限登录，其应用程序默认情况下也无法对系统目录、系统注册表等可能影响系统正常运行的设置进行写操作。这个机制大大增强了系统的安全性，但对应用程序开发者来说，我们不能强迫用户去关闭UAC，但有时我们开发的应用程序又需要以 Administrator 的方式运行，如何实现这样的功能呢？</p>   

<p>下面演示 C# 程序如何实现提示用户以管理员权限运行。</p>   
<p>本例以WinForm程序演示，新建一项目生成后进行相应修改：</p>   
<p><strong>方法一：通过 System.Diagnostics.Process.Start() 方式启动：</strong></p>   
<p>实现方法： 修改默认生成的Program文件，修改后的代码如下：</p>   
<p>由于已经在代码上做了注释，所以不再详细说明；</p>   
<p><br>   
</p>   
<p><pre name="code" class="csharp">static class Program   
    {   
        [STAThread]   
        static void Main()   
        {            
            Application.EnableVisualStyles();   
            Application.SetCompatibleTextRenderingDefault(false);   

            /**   
             * 当前用户是管理员的时候，直接启动应用程序   
             * 如果不是管理员，则使用启动对象启动程序，以确保使用管理员身份运行   
             */   
            //获得当前登录的Windows用户标示   
            System.Security.Principal.WindowsIdentity identity = System.Security.Principal.WindowsIdentity.GetCurrent();   
            System.Security.Principal.WindowsPrincipal principal = new System.Security.Principal.WindowsPrincipal(identity);   
            //判断当前登录用户是否为管理员   
            if (principal.IsInRole(System.Security.Principal.WindowsBuiltInRole.Administrator))   
            {   
                //如果是管理员，则直接运行   
                Application.Run(new Form1());   
            }   
            else   
            {   
                //创建启动对象   
                System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();   
                startInfo.UseShellExecute = true;   
                startInfo.WorkingDirectory = Environment.CurrentDirectory;   
                startInfo.FileName = Application.ExecutablePath;   
                //设置启动动作,确保以管理员身份运行   
                startInfo.Verb = &quot;runas&quot;;   
                try   
                {   
                    System.Diagnostics.Process.Start(startInfo);   
                }   
                catch   
                {   
                    return;   
                }   
                //退出   
                Application.Exit();   
            }   
        }   
    }</pre><br>   
</p>   
<p>效果：由于是通过System.Diagnostics.Process.Start() 方式外部调用启动，所以直接通过VS运行时，是不会提示VS也需要管理员权限，只有程序本身需要管理员权限，与生成应用程序的程序不同。这点是和方法二实现的主要不同之处。</p>   
<p><span style="color:rgb(136,136,136)">本文地址：<a target="_blank" href="http://www.cnblogs.com/Interkey/p/RunAsAdmin.html"><span style="color:rgb(136,136,136)">http://www.cnblogs.com/Interkey/p/RunAsAdmin.html</span></a></span></p>   
<p><strong>方法二：通过添加应用程序清单文件：</strong></p>   
<p>在 项目 上 添加新项 选择“应用程序清单文件” 然后单击 添加 按钮</p>   
<p>添加后，默认打开<span style="font-family:Verdana,Arial,Helvetica,sans-serif; font-size:14px; line-height:25px; text-indent:28px">app.manifest文件，</span>将：</p>   
<p>&lt;requestedExecutionLevel&nbsp; level=&quot;<span style="background-color:yellow">asInvoker</span>&quot; uiAccess=&quot;false&quot; /&gt;</p>   
<p>修改为：</p>   
<p>&lt;requestedExecutionLevel level=&quot;<span style="color:red; background-color:yellow">requireAdministrator</span>&quot; uiAccess=&quot;false&quot; /&gt;</p>   
<p>然后打开 项目属性 ，将 应用程序 标签页中的 资源 中的 清单 修改为新建的 app.manifest。</p>   
<p>重新生成项目，再次打开程序时就会提示 需要以管理员权限运行。</p>   
<p>需要注意的是：如果在VS中 启动调试 的话，就会提示 此任务要求应用程序具有提升的权限。如下图：</p>   
<p><img width="525" height="264" title="提升权限" alt="提升权限" src="http://images.cnblogs.com/cnblogs_com/Interkey/497307/o_04.png"></p>   
<p>选择 使用其他凭据重新启动 即可。</p>   
<p><strong>方法三：直接修改程序文件的属性</strong></p>   
<p>右击程序文件，在弹出的属性对话框中的 兼容性 标签页中</p>   
<p>勾选“以管理员身份运行此程序”即可。</p>   
<p>&nbsp;<img width="439" height="585" title="设置权限等级" alt="设置权限等级" src="http://images.cnblogs.com/cnblogs_com/Interkey/497307/o_05.png"></p>   
<p>&nbsp;</p>   
<p>如果有兴趣还可以继续查看下面的链接：</p>   
<p><a target="_blank" href="http://www.cnblogs.com/Lemon_s/archive/2011/07/28/2119222.html">http://www.cnblogs.com/Lemon_s/archive/2011/07/28/2119222.html</a></p>   
<p><a target="_blank" href="http://www.cnblogs.com/shenchao/archive/2013/03/05/2944660.html">http://www.cnblogs.com/shenchao/archive/2013/03/05/2944660.html</a></p>   
<br>   
</div>   

