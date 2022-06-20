---                
layout: post            
title: "FactoryTalk Batch入门3：Batch  Recipe Editor"                
date:   2022-6-20 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

The FactoryTalk Batch Recipe Editor is used to create and configure master recipes. The FactoryTalk Batch Recipe Editor lets you use tables, sequential function charts, or both, to graphically organize procedural information into unit procedures, operations, and phases. This FactoryTalk Batch component is used primarily by recipe formulators to create or edit recipes (sequences of steps) and formula values (parameters, set point values, etc.).  
All recipes are configured and displayed using the ISA S88.01 Batch Control Standards, which define the Procedure, Unit Procedure, and Operation
(Phase) layers for the procedural model.  

# 打开Recipe Editor
Select Start > Rockwell Software > Recipe Editor. A blank FactoryTalk Batch Recipe Editor window displays.  
If a recipe verification box displays, select Yes to verify all the recipes in the Area Model’s recipe directory.  
3. When this is complete, select Close.    
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe1.png?raw=true)

The Procedure View pane occupies the left side of the FactoryTalk Batch Recipe Editor window and contains a hierarchical list of the current recipe components. Selecting a component from the list displays the corresponding step(s) in the Recipe Construction pane.   
• The Recipe Construction pane occupies the right side of the FactoryTalk Batch Recipe Editor window and is used to construct master recipes. The Recipe Construction pane allows you to construct and view recipe structures using a sequential function chart (SFC) or a table. Both the SFC View and the Table View can be displayed exclusively, or the Recipe Construction pane can be tiled to display both views at the same time. Selecting a component within either view will highlight the corresponding item in the Procedure View pane.  

# open a recipe
1. From the File menu, select Open Top Level. The Open [Type] Recipe dialog box opens. In this case [Type] is BINARY. (Other recipe storage types are XML and RDB.)  
2. From the Select the recipe to open list, select CLS_FRENCHVANILLA. In the right column, notice the information about the recipe and the Release Recipe as Step and Release Recipe To Production checkboxes.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe2.png?raw=true)
3. Select Open.  

The ISA S88.01 recipe structure of CLS_FRENCHVANILLA is displayed on the left side in the Procedure View pane. The SFC version of the CLS_FRENCHVANILLA recipe structure is displayed on the right side in the Recipe Construction pane.    

# Add a sequential step
1. With the Selection Tool selected, double-click the CLS_SWEETCREAM_UP:1 unit procedure in the Procedure View. The CLS_SWEETCREAM_OP:1 operation displays.  
2. Double-click the CLS_SWEETCREAM_OP:1 operation. The recipe steps within the operation display.  
3. Select the ADD_MILK:1 STATE = COMPLETE transition at the bottom of the operation.  
4. Select Add Step in the Recipe Construction Toolbox.   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe7.png?raw=true)  
A new step and transition are added below the selected transition and the Select Phase dialog box opens.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe3.png?raw=true)
5. Select XFR_OUT, and then select OK. The new step is defined as XFR_OUT:1 and the transition below the step is defined as XFR_OUT:1.STATE = COMPLETE.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe4.png?raw=true)  

# Add a parallel step
1. While still in the CLS_SWEETCREAM_OP:1 operation, select the TEMP_CTL:1 step.  
2. Select Add Parallel. A new step is added in parallel to the selected step and the Select Phase dialog box opens.  
3. Select ADD_EGG, and then select OK.   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe5.png?raw=true)  
The new step is now defined as ADD_EGG:2 and the transition below the step is automatically redefined as ADD_EGG:2.STATE = COMPLETE AND TEMP_CTL:1.STATE = COMPLETE AND ADD_CREAM:1.STATE = COMPLETE to reflect the new parallel structure.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/recipe6.png?raw=true)  

# Assign step formula values
1. While still in the CLS_SWEETCREAM_OP:1 operation, select the ADD_EGG:2 step.  
2. Select Value Entry. The Parameter Value Entry/Report Limit Entry dialog box opens listing the parameters associated with the step. The only parameter is ADD_AMOUNT.  
3. Type 100 in the Value box, and then select Display so the value displays on the SFC.  
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