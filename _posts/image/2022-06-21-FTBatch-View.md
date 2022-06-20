---                
layout: post            
title: "FactoryTalk Batch入门4：Batch View"                
date:   2022-6-21 14:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---      

FactoryTalk Batch View is used to initiate and control the batch process and to view running batches. It has a graphical user interface with easy to use windows and buttons and, like most of the FactoryTalk Batch components, is based primarily on input from ISA’s S88.01 Batch Control Standard.
Using the sample demo files installed with FactoryTalk Batch, this chapter takes you through the steps involved in running a batch, demonstrating the powerful simplicity and functionality of the FactoryTalk Batch solution.  

# Open FactoryTalk Batch View
1. Select Start > Rockwell Software > View. The FactoryTalk Batch View window opens to the Batch List view, which is one of the ten views accessible using the toolbar buttons.   
Tip: If none of the toolbar or command buttons are enabled, except the Login button, select the Login button and enter a FactoryTalk Security user name and password.
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view1.png?raw=true)

# Run a sample batch

1. Select the Add Batch command button. The Recipe List dialog box opens, listing the recipes that are released to production, which constitute the master recipe list for a facility.   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view2.png?raw=true)
2. Select the CLS_FRENCHVANILLA recipe, and then select OK. The Batch Creation dialog box opens. The Formula Values area displays the materials and amounts that are used in the recipe. The Unit Binding area indicates the units that you can choose to bind to the recipe.  
This recipe takes advantage of the powerful Dynamic Unit Allocation feature, which allows you to select which units in the area model to bind to the recipe and when that binding occurs. In this batch, you choose to bind the units as you create the batch. Later in this section you see how to bind units to a batch after the batch is created.    
3. Type TEST_1 in the Batch IDbox.  
4. From the Bound Unit list in the Unit Binding area, select WP_FREEZER2 as the FREEZER unit and WP_MIXER2 as the MIXER unit to bind to the recipe. When the batch is run, the recipe will bind to the units that you selected.  
5. Select Create. The batch is added to the Batch List.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view3.png?raw=true)
6. Select the TEST_1 batch, select the Start Batch command button, and then select Yes to confirm.  
7. If you configured a verification policy on the START command (see Create a sample signature template), the Command Signature dialog box opens.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view4.png?raw=true)

# Examine the batch
1. Select the Procedure as SFC button to examine the batch as it is running. The Procedure as SFC view displays the sequential function charts (SFCs) of the currently selected batch, where you can watch the batch execute its steps and transitions. An operator can command a batch using the command buttons.   
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view5.png?raw=true)
The Procedure as SFC window consists of four sections:  
• The Procedural Hierarchy displays the details of the entire batch. Dragging the split bar to the right reveals more of the batch details, such as State, Mode, Unit, and Key Parameters.  
• The Sequential Function Chart (SFC) displays for the step that is selected in the Procedural Hierarchy. You can view a different level of the SFC by double-clicking a step.  
• The Recipe Table displays the components of the procedural elements in the currently selected batch. You also can acccess the recipe table by clicking the Procedure as Table button.  
• The Auxiliary Index contains five tabs that display information regarding the recipe, prompts, parameters, reports and arbitration for the step that is selected in the Procedural Hierarchy or the SFC.  

# Bind a unit manually
When you create a batch, you can select units to bind to the recipe (which we did earlier in this chapter). You also have the ability to change the binding after the batch is created, which is helpful if a unit becomes unavailable between the time you create the batch and when you are ready to run the batch.  
1. In the Batch List view, create a batch of French Vanilla named TEST_2 and bind to the WP_MIXER1 and WP_FREEZER1 units.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view6.png?raw=true)
2. Select the TEST_2 batch, and then select the Procedure as SFC button. Notice that WP_MIXER1 and WP_FREEZER1 appear in the SFC to indicate that those phases will be used in the recipe.  
3. Select CLS_SWEETCREAM_UP:1 in the Procedural Hierarchy or SFC.  
4. Select the Bind command button, and then Yes to confirm the binding. The Manual Bind of Step dialog box opens listing the options you can
select for binding the unit.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view7.png?raw=true)

WP_MIXER2 does not appear in the list because the other unit procedures in the batch are bound to WP_FREEZER1, which is linked to WP_MIXER1. You want the FactoryTalk Batch Server to prompt the operator to select the unit to bind to the unit procedure as the batch runs. If you select First Available, the FactoryTalk Batch Server selects the unit to bind based on availability at the time equipment is needed.  
5. From the SelectUnit to bind to Unit Requirement list, select PROMPT, and then select OK. Notice that the SFC changes to MIXER. When the batch runs, the operator is prompted to select the mixer unit to bind to the recipe.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view8.png?raw=true)
6. Select CLS_TRANSFER_IN_UP:1 in the Procedural Hierarchy or SFC.  
7. Select the Bind command button, and then select Yes to confirm the binding. The Manual Bind of Step dialog box opens listing the options
you can select for binding the unit. Notice that WP_FREEZER1 and WP_FREEZER2 both appear in the list because the MIXER binding process was changed to Prompt.  
8. Select PROMPT from the Select Unit to bind to Unit Requirementlist, and then select OK.  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/Batch/view9.png?raw=true)
Notice that the SFC changes to FREEZER. When the batch is run, the operator is prompted to select the freezer unit to bind to the recipe.  

# respond to unacknowledged sample prompts
1. Select the Start Batch command button, and then select Yes to start the batch.  
The Unacknowledged Prompts button begins to flash yellow. You could address this request from the Batch List view but switch to the SFC view to see how the binding changes.  
2. Select the Procedure as SFC button. Notice that the first transition indicates BINDING, which means the FactoryTalk Batch Server is trying to acquire an equipment phase to run the CLS_SWEETCREAM unit procedure.  
3. Select the flashing Unacknowledged Prompts button. The Unacknowledged Prompts List opens indicating that the operator must select the unit to use as the MIXER.  
4. Double-click the TEST_2 batch. The Prompt to Bind Unit Requirement dialog box opens indicating that WP_MIXER1 and WP_MIXER2 are the mixers available to bind to the recipe.    
5. Select WP_MIXER2 from the Select Unit to bind to Unit Requirement list, and then select OK.  
6. Select the Procedure as SFC button and notice that the batch continues to run using WP_MIXER2. When the batch reaches the transition following the CLS_SWEETCREAM unit procedure, the Unacknowledged Prompts button starts to flash again.  
7. Select the flashing Unacknowledged Prompts button. The Batch List opens indicating that the operator must select the unit to use as the FREEZER.  
8. Double-click the TEST_2 batch. The Prompt to Bind Unit Requirement dialog box opens indicating that WP_FREEZER2 is the only freezer available to bind to the recipe. Because you selected WP_MIXER2, which is linked to WP_FREEZER2, that is the only option available to you.  
9. Select WP_FREEZER2 from the Select Unit to bind to Unit Requirement list, and then select OK. The batch should run to completion.  

# view the sample batch event journal
The FactoryTalk Batch Server gathers detailed data for every action that takes place during the execution of all batches and places the data within an electronic batch record. You can filter and view this data in the Event Journal window  
1. Select the Event Journal button. The Event Journal view opens.  
2. Select the Journal button. The Event Data Files dialog box opens.  
3. In the Event Data Files list, select the TEST_2 batch, and then select OK. The event data displays on the right side of the window.  
4. In the Filtering area, select Event Type from the Column 1 list.  
5. In the Filter 1 box, type COMMENT, and then select the Refresh button. The data is filtered to show the comment that you added to the TEST_2 batch. You must adjust the column headings to view the entire message as shown in this figure.  

# Control a phase manually
1. Select the Phase Control button. The Phase Control view opens and displays the process cell.  
2. Double-click the WEST_PARLOR icon to view the units within the WEST_PARLOR process cell.  
3. Select the WP_MIXER1 icon. A list of the phases in WP_MIXER1 displays in the Phases section. You may need to move the vertical split bars to the right or left so your window appears as shown.  
4. Select the WP_ADD_EGG_M1 icon, and then select the Acquire command button. Select Yes to confirm the acquisition of the phase.  
Notice the green operator (Opr) light, which indicates that the WP_ADD_EGG_M1 phase is now owned by the operator.  
5. Select the Start command button, and then select Yes to start the WP_ADD_EGG_M1 phase. The Phase Control dialog box opens.  
6. Type TEST_3 in the Batch ID box, and then select OK. After running for a few seconds, the Unacknowledged Prompts button on the toolbar starts flashing yellow and ADD_AMOUNT displays in the Unacknowledged Prompts list.  
7. Select the Acknowledge button. The Acknowledge dialog box opens showing the default value as 0. The allowable range of values is 0 to 5000.  
8. Type 40, and then select the Acknowledge button. The phase continues to run.  
As the phase runs, you can use the command buttons to Hold, Restart, Abort, Stop, Pause, Resume the phase.  
9. When the phase completes, select the Reset command button, and then select Yes to confirm the reset. You can run this phase as many times as necessary to test it. When you are done testing, release control back to FactoryTalk Batch so the phase can run as part of a recipe.  
10. Select the Release command button, and then select Yes to confirm the release.  

# Resolve arbitration issues
A procedure stops running if a phase is unable to acquire the needed equipment. The FactoryTalk Batch Server displays ACQUIRING1 on the SFC at the transition above that phase and that is where you begin your investigation to determine the cause of the arbitration issue.  
1. Select the Phase Control button. The Phase Control view opens and displays the process cell.  
2. Double-click the WEST_PARLOR icon, and then select the WP_MIXER1 icon. A list of the phases within WP_MIXER1 are displayed in the Phases section.  
3. Select the WP_XFR_OUT icon, and then select the Acquire command button. Select Yes to confirm the acquisition of the phase.  
4. Select the Batch List button to go to the Batch List view.  
5. Select the Add Batch command button, and then add a batch of CLS_FRENCHVANILLA, binding to WP_MIXER1 and WP_FREEZER1 with a batch ID of TEST_5.  
6. Start the batch, and then select the Procedure as SFC button. The batch stops processing when it reaches the XFR_OUT:1 phase.  
7. Select the XFR_OUT:1 phase in the Procedural Hierarchy view. In the SFC view, notice that the transition is stalled in ACQUIRING. In the Auxiliary Index view, select the Arbitration tab and notice that the phase needs WP_XFR_OUT_M1 and is owned by WP_XFR_OUT_M1.  
8. Select the Phase Summary button. The Phase Summary window opens and displays all the equipment phases and their associated status information. This window is useful when trying to determine the state of an equipment phase.  
9. Scroll down and notice that the WP_XFR_OUT_M1 phase is owned by the Operator.  
10. Select the Arbitration button. The Arbitration window opens to the phase that you selected in the SFC view. The operator uses this window to view current resource allocation information, acquire available resources, and release operator-owned resources. Notice again that this phase is owned by the operator.   
In this window the operator can acquire an equipment phase and then release it to resolve an arbitration issue.  
11. Select the Release command button to release the equipment phase. The batch runs to completion.  
12. Select the Batch List button to return to the Batch List view. Remove all batches from the batch list.  
