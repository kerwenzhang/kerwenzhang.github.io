---                
layout: post            
title: "FactoryTalk Batch入门3：Batch  Recipe Editor"                
date:   2022-6-20 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

FactoryTalk Batch 配方编辑器(Batch Recipe Editor)用于创建和配置主配方。 FactoryTalk Batch 配方编辑器可以使用表格`tables`、顺序功能图`sequential function charts` 或两者，以图形方式将程序信息组织到单元程序`unit procedures`、操作`operations`和阶段`phases`中。 配方的制定者可以使用编辑器用来创建或编辑配方（步骤序列）和公式值（参数、设定点值等）。  
所有配方均使用 `ISA S88.01` 标准进行配置和显示。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe0.png?raw=true)  

# 打开Recipe Editor
1. 开始菜单 > Rockwell Software > Recipe Editor，点击之后会显示一个空的Recipe Editor. 如果提示验证，点击Yes去验证该区域模型里所有的配方。   
2. 验证完成之后点Close关闭验证窗口。   
主窗体布局如下：       
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe1.png?raw=true)

![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe7.png?raw=true)  

    • 程序视图窗格`Procedure View pane`位于编辑器的左侧，包含当前配方组件的分层列表。 从列表中选择一个组件会在“配方构建”窗格`Recipe Construction pane`中显示相应的步骤。  
    • 配方构建窗格`Recipe Construction pane`位于编辑器的右侧，用于编辑主配方。 可以使用顺序功能图 (SFC) 或表格来编辑和查看配方结构。 

# 打开一个配方
1. 从文件菜单中，选择`Open Top Level`。 打开 [类型] 配方对话框。 类型是 BINARY。 （配方也可以存储为XML格式或者RDB格式。）  
2. 从选择要打开的配方列表中，选择 `CLS_FRENCHVANILLA`。 在右侧展示配方有关的信息。有两个复选框`Release Recipe as Step`和`Release Recipe to Production`。      
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe2.png?raw=true)
3. 点击Open.  
打开配方`CLS_FRENCHVANILLA`后，左侧过程视图显示的是配方结构，右侧显示的是配方结构的SFC版本。     

# 添加顺序步骤
1. 选择工具栏中的指针图标后，点击左侧过程视图中的 `CLS_SWEETCREAM_UP:1` 单元过程。将显示 `CLS_SWEETCREAM_OP:1` 操作。  
2. 点击 `CLS_SWEETCREAM_OP:1` 操作。显示该操作中的所有步骤。  
3. 选择OP底部的 ADD_MILK:1 STATE = COMPLETE 转换(transition)。   
4. 在配方构建工具箱中选择添加步骤(Add Step)。  
   新的步骤和转换将添加到所选转换下方，并打开“选择阶段”对话框。  
    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe3.png?raw=true)
5. 选择 XFR_OUT，然后选择 OK。新步骤定义为 XFR_OUT:1，步骤下方的转换定义为 XFR_OUT:1.STATE = COMPLETE。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe4.png?raw=true)    

# 添加并行步骤

1. 仍然在`CLS_SWEETCREAM_OP:1` 操作, 选择步骤  `TEMP_CTL:1`
1. 选择“添加并行”。将与所选步骤并行添加一个新步骤(Add Parallel)，并打开“选择阶段”对话框。
2. 选择 ADD_EGG，然后选择“确定”。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe5.png?raw=true)   

    新的步骤现在定义为 `ADD_EGG:2`，并且该步骤下方的转换自动重新定义为 `ADD_EGG:2.STATE = COMPLETE AND TEMP_CTL:1.STATE = COMPLETE AND ADD_CREAM:1.STATE = COMPLETE`，以反映新的并行结构。
    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe6.png?raw=true)  

 
# 分配步骤公式值
1. 仍在 `CLS_SWEETCREAM_OP:1` 中，选择 `ADD_EGG:2` 步骤。
2. 在工具栏中选择 `值输入`(`Value Entry`)。打开参数对话框，列出与该步骤相关的参数。这里唯一的参数是 `ADD_AMOUNT`。
3. 在 值(value) 框中键入 100，然后勾选 “显示(Display)”，这样值就会显示在 SFC 上。

    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe8.png?raw=true)  
4. 选择 “确定” 返回到 FactoryTalk Batch 配方编辑器窗口。接下来，修改 TEMP_CTL:1 的参数，以便操作员可以在批次运行时输入数值。
5. 选择 TEMP_CTL:1 步骤，然后选择 “值输入”。此时将打开 “参数值输入 / 报告限值输入” 对话框，其中列出了与该步骤相关的参数。共有两个参数：HOLD_TIME（保持时间）和 TEMP_SP（温度设定点）。您希望让操作员决定将混合物保持多长时间。
6. 对于 HOLD_TIME 参数，从 “来源” 列表中选择 “Operator（操作员）”，以指示在运行配方时由操作员输入该数值。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe9.png?raw=true)  
7. 点击OK返回FactoryTalk Batch Recipe 编辑窗口    

# 添加配方注释
配方注释功能可让您创建和编辑注释，以便在设计阶段和运行阶段查看。利用此功能，可将重要信息插入配方中，并将其与特定步骤、转换或整个配方关联。

1. 仍处于 CLS_SWEETCREAM_OP:1 操作界面时，选择 文本框工具（Text Box Tool）。此时光标将变为文本编辑工具样式。
2. 将光标移至 AGITATE:1 步骤的右侧并点击，SFC 图中将出现一个标有 C1 的文本框。
3. 选择 链接工具（Link），此时光标变为带加号（+）的样式，将其移回 C1 文本框。
4. 在文本框内任意位置点击并按住鼠标左键，将光标拖至 AGITATE:1 步骤。此时文本框下半部分将显示 AGITATE:1，表明该文本框已与此步骤关联。
5. 选择 选择工具（Selection Tool），双击文本框内部，输入以下内容：如果混合物开始分离，将搅拌速度降至 20 RPM。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe10.png?raw=true)   

# 添加连续循环
1. 在工具栏上选择 “向上” 两次，以导航至 CLS_SWEETCREAM_UP:1 单元程序。
2. 选择 转换工具。将指针放置在已标记为 CLS_SWEETCREAM_UP:1.STATE = COMPLETE 的现有转换右侧，然后点击添加一个未定义的转换。
3. 选择 链接工具 按钮。
4. 从标记为 CLS_SWEETCREAM_UP:1 的步骤开始，拖动指针至新创建的 TRUE 转换，释放鼠标以添加链接。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe11.png?raw=true)   
5. 从 TRUE 转换拖动指针至单元程序的最后一步（CLS_FRENCHVANILLA_UP:1），从而完成循环结构。 
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe12.png?raw=true)   
6. 选择 选择工具 按钮，然后双击新创建的 TRUE 转换。
7. 选择 常用表达式 文件夹。 
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe13.png?raw=true)   
8. 双击 Step.State = Complete。
9. 在对话框的上部，高亮显示表达式中的等号（=），然后选择 大于或小于 按钮。此时转换条件应变为 CLS_SWEETCREAM_UP:1.STATE <> COMPLETE。此转换确保 CLS_SWEETCREAM_UP:1 操作将持续运行，直到达到 COMPLETE 状态。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe14.png?raw=true)  
10. 选择 确定。

# 删除操作
从示例操作中删除顺序步骤：
1. 仍处于 CLS_SWEETCREAM_OP:1 操作时，选择 XFR_OUT:1 步骤。
2. 选择 删除步骤(Remove Step) 按钮。此时 XFR_OUT:1 步骤及其链接和后续转换将被移除，SFC（顺序功能图）会自动重新排列以适应删除的步骤。  

从示例操作中删除并行步骤：
1. 仍处于 CLS_SWEETCREAM_OP:1 操作时，选择 ADD_EGG:2 并行步骤。
2. 选择 删除步骤 工具。此时 ADD_EGG:2 并行步骤及其链接将被移除，后续转换会重新配置，SFC 会自动调整布局以适配删除的步骤。

# 验证配方
1. 选择 验证（Verify）按钮，系统将打开 “验证过程结果” 对话框。正常结果应显示：CLS_FRENCHVANILLA >> 配方验证已完成。
2. 选择 关闭（Close）按钮。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe15.png?raw=true)  