---
layout: post
title: "WPF 数据绑定"
date: 2023-07-31 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

# 属性绑定

1. 新建一个 WPF .net framework 工程
2. 为 MainWindow 新建一个 View model， 新建一个 class， 取名 MainWindowViewModel.cs
3. ViewModel 继承INotifyPropertyChanged接口，用于事件的触发  

        internal class MainWindowViewModel : INotifyPropertyChanged
        {
            public event PropertyChangedEventHandler PropertyChanged;
            protected void OnPropertyChanged([CallerMemberName] string name = null)
            {
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
            }
        }

4. 将页面与 ViewModel 关联起来, 有两种方式，一种是修改页面 xaml，一种是修改代码 xaml.cs, [参考](https://www.cnblogs.com/Boundless-Learn/p/16817947.html), 我选择修改代码 `MainWindow.xaml.cs`.

        MainWindowViewModel vm;
        public MainWindow()
        {
          InitializeComponent();
          vm = new MainWindowViewModel();
          this.DataContext = vm;
        }

5. 修改页面，添加一个 textbox， 一个 button，

        <TextBox Height="30" Width="300" Margin="10" Name="ServerName" Text="{Binding ServerName}" TextChanged="SqlServerNameTextbox_TextChanged"/>
        <Button Height="50" Width="100" Margin="10" IsEnabled="{Binding IsButtonEnabled}" Background="White">Next</Button>

6. TextBox的Text绑定属性ServerName，button的isEnabled绑定属性IsButtonEnabled, 当 ServerName 为空时，disable button， 不为空时，enable button。修改 xaml.cs 添加 text change 事件  

        private void SqlServerNameTextbox_TextChanged(object sender, TextChangedEventArgs e)
        {
            vm.HandleSqlNameTextChanged((sender as TextBox).Text);
        }


7. 修改ViewModel, 添加属性  

        private string serverName = "";
        public string ServerName
        {
            get
            {
                return serverName;
            }
            set
            {
                serverName = value;
                OnPropertyChanged();
            }
        }

        public bool isButtonEnabled = false;
        public bool IsButtonEnabled
        {
            get
            {
                return isButtonEnabled;
            }
            set
            {
                isButtonEnabled = value;
                OnPropertyChanged("IsButtonEnabled");

            }
        }

8. 添加Text Change事件处理  

        public void HandleSqlNameTextChanged(string currentText)
        {
            ServerName = currentText;
            if (string.IsNullOrEmpty(ServerName))
            {
                IsButtonEnabled = false;
            }
            else
            {
                IsButtonEnabled = true;
            }
        }

# Command
如果你的Next button已经绑定了Command，官方的建议是使用CanExecute，而不是直接enable/disable button。   
1. 在xaml中新建一个textbox和button   

        <TextBox Height="30" Width="300" Margin="10" Name="ComputerName" Text="{Binding ComputerName}" TextChanged="ComputerName_TextChanged"/>
        <Button Height="50" Width="100" Margin="10" Command="{Binding TestCommand}" Background="White">Test</Button>

2. xaml.cs中添加事件  

        private void ComputerName_TextChanged(object sender, TextChangedEventArgs e)
        {
            vm.HandleComputerNameTextChanged(((TextBox)sender).Text);
        }

3. View Model中添加属性，button Command 及事件处理, 当ComputerName发生改变时，通过`RaiseCanExecuteChanged`触发button Command的`CanExecute`    

        private string computerName = "";
        public string ComputerName
        {
            get
            {
                return computerName;
            }
            set
            {
                computerName = value;
                OnPropertyChanged();
            }
        }

        internal void HandleComputerNameTextChanged(string text)
        {
            ComputerName = text;
            TestCommand.RaiseCanExecuteChanged(); 
        }

        public ICommand _testCommand;
        public virtual ICommand TestCommand
        {
            get
            {

                if (_testCommand == null)
                {

                    _testCommand = new DelegateCommand(
                        () =>
                        {
                            MessageBox.Show("test");
                        },
                        // can execute
                        () => canGotoNext());
                }
                return _testCommand;
            }
        }

        public virtual bool canGotoNext()
        {
            if (string.IsNullOrEmpty(ComputerName))
            {
                return false;
            } else
            {                
                return true;
            }
        }