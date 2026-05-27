## HLR_Setup

**Description**  
这是 HLR 测试用例的 Setup procedure。

Story: CVBFTBATCH-10135 和 CVBFTBATCH-10677。

**Precondition**  
使用 domain administrator user 登录测试机器，建议使用 installer 推荐用户。

### Step 1

**Test Step Description**  
Installation

安装所有 Batch components（Batch、eProcedure 和 Material Manager），并激活产品。

按需重启机器。

**Expected Result**  
...

### Step 2

**Test Step Description**  
Collateral Configuration

将 Material Database 配置为 `Sample2_Materials`。

将 `HLR.zip` 下载到测试机器，并解压到任意位置（建议使用 batch share folder `FTBATCH_PROJECTS`）。

在解压后的 `HLR` 文件夹下创建 `logs`、`restart`、`journals` 文件夹。

在 FTSP 的 Batch Server 的 General Tab 中勾选 `Enable Factory eProcedure` 和 `Enable FactoryTalk Batch Material Manager`，并选择 `Computer hosting the FactoryTalk Batch Material`。如有需要，在 FTSP 中配置 collateral。

**Expected Result**  
...

### Step 3

**Test Step Description**  
Audit Configuration

确认已启用 Auditing：

- 在 FactoryTalk Administration Console 中，进入  
  `System > Policies > System Policies > Audit Policy > Audit changes to configuration and control system`  
  并设置为 `Enabled`。

Note：建议输入带有 TC 和 step number 关联特征的 Audit comments，以便后续可以更容易在 Diagnostic 中搜索并验证 Audit message。

**Expected Result**  

### Step 4

**Test Step Description**  
Create Shortcut

启动 FactoryTalk Administration Console，并创建一个新的 Application：`HLR_TEST`。

添加一个新的 FactoryTalk Linx server：`HLR_LINX`。

打开 Communication Setup，创建所需名称的 Shortcut，并配置指定的 IP 和 slot number。

**Expected Result**  
...

### Step 5

**Test Step Description**  
How to Clear Diagnostics Log

启动 FactoryTalk Administration Console：

- 选择 `Tool > FactoryTalk Diagnostics > Setup`
- 导航到 `Diagnostics Setup > Destination Setup > LocalLog`
- 点击 `Clear Log`（是否保存 log 可按需决定）

**Expected Result**  
...

### Step 6

**Test Step Description**  
How to configure Full Edit / View Only permission

启动 FactoryTalk Administration Console：

进入  
`Policies > Product Policies > Batch > Equipment Editor > Access Modes`

双击 `Access Modes`。

在指定 computer 上，为目标 users 或 groups 配置 `Full Edit / View Only` 为 `Allow`。

**Expected Result**  
...

### Step 7

**Test Step Description**  
How to configure Deploy Area Model permission

启动 FactoryTalk Administration Console：

进入  
`Policies > Product Policies > Batch > Feature Security`

双击 `Feature Security`。

在指定 computer 上，为目标 users 或 groups 配置 `Configure Runtime Area Model Deployment` 为 `Allow / Deny`。

**Expected Result**  
...

### Step 8

**Test Step Description**  
How to configure SAI permission

启动 FactoryTalk Administration Console：

进入  
`Policies > Product Policies > Batch > Equipment Editor > Feature Security`

双击 `Feature Security`。

在指定 computer 上，为目标 users 或 groups 配置 `Area Model : Secure` 为 `Allow / Deny`。

**Expected Result**  
...

---
