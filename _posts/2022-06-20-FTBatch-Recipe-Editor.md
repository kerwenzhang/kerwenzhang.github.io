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

# 打开Recipe Editor
1. 开始菜单 > Rockwell Software > Recipe Editor，点击之后会显示一个空的Recipe Editor. 如果提示验证，点击Yes去验证该区域模型里所有的配方。   
2. 验证完成之后点Close关闭验证窗口。   
主窗体布局如下：       
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe1.png?raw=true)

    • 程序视图窗格`Procedure View pane`位于编辑器的左侧，包含当前配方组件的分层列表。 从列表中选择一个组件会在“配方构建”窗格`Recipe Construction pane`中显示相应的步骤。  
    • 配方构建窗格`Recipe Construction pane`位于编辑器的右侧，用于构建主配方。 可以使用顺序功能图 (SFC) 或表格来构建和查看配方结构。 SFC 视图和表格视图都可以独占显示，或者配方构造窗格可以平铺以同时显示两个视图。   

# 打开一个配方
1. 从文件菜单中，选择`Open Top Level`。 打开 [类型] 配方对话框。 类型是 BINARY。 （配方也可以存储为XML格式或者RDB格式。）  
2. 从选择要打开的配方列表中，选择 `CLS_FRENCHVANILLA`。 在右侧展示配方有关的信息。有两个复选框`Release Recipe as Step`和`Release Recipe to Production`。<font color="red">暂时不知道是干嘛的，留作以后研究。</font>      
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe2.png?raw=true)
3. 点击Open.  
打开配方`CLS_FRENCHVANILLA`后，左侧过程视图显示的是配方结构，右侧显示的是配方结构的SFC版本。     

# 添加顺序步骤
1. 选择工具栏中的指针图标后，点击左侧过程视图中的 `CLS_SWEETCREAM_UP:1` 单元过程。将显示 `CLS_SWEETCREAM_OP:1` 操作。  
2. 点击 `CLS_SWEETCREAM_OP:1` 操作。显示改操作中的所有步骤。  
3. 选择OP底部的 ADD_MILK:1 STATE = COMPLETE 转换(transition)。   
4. 在配方构建工具箱中选择添加步骤。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe7.png?raw=true)  

    新的步骤和转换将添加到所选转换下方，并打开“选择阶段”对话框。  
    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe3.png?raw=true)
5. 选择 XFR_OUT，然后选择 OK。新步骤定义为 XFR_OUT:1，步骤下方的转换定义为 XFR_OUT:1.STATE = COMPLETE。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe4.png?raw=true)    

# 添加并行步骤

1. 选择“添加并行”。将与所选步骤并行添加一个新步骤(Add Parallel)，并打开“选择阶段”对话框。
2. 选择 ADD_EGG，然后选择“确定”。
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe5.png?raw=true)   

    新的步骤现在定义为 `ADD_EGG:2`，并且该步骤下方的转换自动重新定义为 `ADD_EGG:2.STATE = COMPLETE AND TEMP_CTL:1.STATE = COMPLETE AND ADD_CREAM:1.STATE = COMPLETE`，以反映新的并行结构。
    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe6.png?raw=true)  

# Assign step formula values
1. While still in the CLS_SWEETCREAM_OP:1 operation, select the ADD_EGG:2 step.  
2. Select Value Entry. The Parameter Value Entry/Report Limit Entry dialog box opens listing the parameters associated with the step. The only parameter is ADD_AMOUNT.  
3. Type 100 in the Value box, and then select Display so the value displays on the SFC.  
# 分配步骤公式值
1. 仍在 `CLS_SWEETCREAM_OP:1` 中，选择 `ADD_EGG:2` 步骤。
2. 在工具栏中选择 值输入(Value Entry)。打开参数对话框，列出与该步骤相关的参数。这里唯一的参数是 ADD_AMOUNT。
3. 在 值(value) 框中键入 100，然后勾选 “显示(Display)”，这样值就会显示在 SFC 上。

    ![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe8.png?raw=true)  
4. Select OK to return to the FactoryTalk Batch Recipe Editor window. Next, you decide to change the parameter for TEMP_CTL:1 so that the operator can enter the amount when the batch is run.  
5. Select the TEMP_CTL:1 step, and then select Value Entry. The Parameter Value Entry/Report Limits Entry dialog box opens listing the parameters associated with the step. There are two parameters: HOLD_TIME and TEMP_SP. You want the operator to decide how long to hold the mixture.  
6. From the Origin list for the HOLD_TIME parameter, select Operator to indicate that the operator enters the amount when the recipe is run.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe9.png?raw=true)  
7. Select OK to return to the FactoryTalk Batch Recipe Editor window    

# Add recipe comments
Recipe commenting provides you with a tool to create and edit comments for viewing at design and run time. With this feature, important information can be inserted into the recipe and associated with a step, transition, or entire recipe.  

1. While still in the CLS_SWEETCREAM_OP:1 operation, select Text Box Tool. The cursor changes to a text tool.  
2. Move the cursor to the right of the AGITATE:1 step and select. A text box labeled C1 is placed in the SFC.  
3. Select Link, and move the cursor (now a +) back to the C1 text box.  
4. Select anywhere in the box, hold the mouse button, and drag the cursor to the AGITATE:1 step. AGITATE:1 now appears in the bottom half of the text box indicating the C1 text box is associated with the AGITATE:1 step.  
5. Choose the Selection Tool and double-click inside the text box. Type Reduce the agitation speed to 20 RPM if the mixture begins to separate.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe10.png?raw=true)   

# Add a continuous loop
1. Select Go Up on the toolbar twice to move to the CLS_SWEETCREAM_UP:1 unit procedure.  
2. Select Transition Tool. Place the pointer to the right of the existing transition labeled CLS_SWEETCREAM_UP:1.STATE = COMPLETE, and then select to add an undefined transition.  
3. Select the Link Tool button.  
4. Select and drag the pointer from the step labeled CLS_SWEETCREAM_UP:1 to the new TRUE transition. Release the mouse button to add the link.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe11.png?raw=true)   
5. Select and drag the pointer from the TRUE transition to the last step of the unit procedure (CLS_FRENCHVANILLA_UP:1). This completes the loop structure.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe12.png?raw=true)   
6. Select the Selection Tool button, and then double-click the new TRUE transition.  
7. Select the Common Expressions folder.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe13.png?raw=true)   
8. Double-click Step.State = Complete.  
9. In the upper part of the dialog box, highlight = (equal sign) in the expression, and then select the GREATER THAN OR LESS THAN button. The transition should now read CLS_SWEETCREAM_UP:1.STATE <> COMPLETE. This transition makes sure that the CLS_SWEETCREAM_UP:1 operation will continue to run until it reaches a COMPLETE state.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe14.png?raw=true)  
10. Select OK.  

# Remove 
To remove a sequential step from the sample operation:  
1. While still in the CLS_SWEETCREAM_OP:1 operation, select the XFR_OUT:1 step.  
2. Select the Remove Step button. The XFR_OUT:1 step is removed, including its links and the following transition. The SFC automatically
rearranges to adjust for the removed step.    

To remove a parallel step from the sample operation:  
1. While still in the CLS_SWEETCREAM_OP:1 operation, select the ADD_EGG:2 parallel step.  
2. Select the Remove Step tool. The ADD_EGG:2 parallel step is removed, including its links, and the following transition is re-configured. The
SFC automatically rearranges to adjust for the removed step.  

# verify the recipe:  
1. Select the Verify button. The Verification Process Results dialog box opens. The result should be: CLS_FRENCHVANILLA >> Verification
of recipes has completed.  
2. Select Close.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe15.png?raw=true)  