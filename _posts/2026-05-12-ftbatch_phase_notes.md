---
layout: post
title: "FTBatch Phase学习笔记"
date: 2026-05-12 18:30:00
categories: "FTBatch"
catalog: true
tags:
  - FTBatch
---

# FTBatch Phase 学习笔记

本文主要整理 FTBatch 中几个最核心的概念：**Phase、Operation、Unit**，以及它们在 **FTBatch + PLC / PhaseManager** 架构中的关系。

---

## 1. 什么是 Phase？

在 **FTBatch / Batch 控制** 的语境里，**Phase（相位）** 是配方执行中的**最小可执行动作单元**，可以理解为“设备会做的一件标准动作”。

它不是泛泛的工艺阶段，而是在 **ISA-88 / FactoryTalk Batch** 里有明确含义的控制对象。

### 常见例子
- 加料（Add）
- 加热（Heat）
- 搅拌（Agitate）
- 转移（Transfer）
- 清洗（CIP）
- 保温（Hold）

### Phase 的典型特征
- 能被配方步骤调用
- 有状态，例如：
  - Idle
  - Running
  - Held
  - Complete
  - Aborted
- 能接收命令，例如：
  - Start
  - Hold
  - Restart
  - Stop
  - Abort
- 有参数，例如：
  - 温度设定值
  - 加料重量
  - 搅拌时间

### 一句话理解
**Phase 是批处理系统与底层控制系统之间的标准动作接口。**

配方层不会直接写“开哪个阀、停哪个泵、延时几秒”，而是调用更高层的工艺动作，例如：
- `Add Material`
- `Heat To Temperature`
- `Transfer Out`

这些动作最终由底层 PLC 或 PC 控制逻辑去实现。

---

## 2. Phase 是在 Batch 里实现，还是在 PLC 里实现？

### 短答案
通常来说，**Phase 的执行逻辑在 PLC 或 PC 控制层中实现，而 FTBatch 负责调度、下命令和监控状态。**

### FTBatch 负责什么？
- 执行配方
- 决定当前该调用哪个 Phase
- 给 Phase 下发命令
- 传递参数
- 读取状态和结果

### PLC / PC 控制层负责什么？
- 真正控制阀门、泵、电机、加热器
- 按工艺逻辑完成动作
- 返回状态、报警和完成信号

### 例子：加热到 80°C
假设配方里有一步：

- `Heat reactor to 80°C`

在 FTBatch 看来，这一步就是调用一个 Phase，例如：
- `HEAT`

并传入参数：
- `TargetTemp = 80`

#### FTBatch 做什么？
- 把参数传给 `HEAT`
- 发出 `Start`
- 等待其状态变为 `Running / Complete / Held / Aborted`

#### PLC 做什么？
PLC 中的 `HEAT` 逻辑会：
- 打开蒸汽阀或加热器
- 读取温度反馈
- 做超温保护、超时判断
- 达到目标温度后完成动作
- 把状态返回给 FTBatch

### 结论
**Phase 不是 Batch 自己直接执行的物理动作，而是由 Batch 调用底层控制层去执行。**

---

## 3. 为什么 FTBatch 不直接控制阀门和电机？

因为 **Batch 是工艺调度层，不是底层设备控制层**。

### 原因 1：降低复杂度
如果 FTBatch 直接操作每个阀门、泵和电机，那么每个配方都要写大量设备细节，维护会非常困难。

例如一个“加料”动作，底层可能涉及：
- 开阀门
- 启动泵
- 检查联锁
- 读取流量
- 达到目标后停泵
- 关闭阀门
- 故障处理

这些细节更适合留在控制层。

### 原因 2：便于复用
同一个“加料”动作可能被多个配方复用。

如果每个配方都写一遍底层点位逻辑，会重复且容易出错。  
如果封装成一个统一的 Phase，例如 `ADD_MATERIAL`，配方只需要调用它即可。

### 原因 3：安全与联锁应留在 PLC
例如：
- 电机互锁
- 阀门开闭顺序
- 温度 / 压力保护
- 紧急停机
- permissive 条件

这些逻辑应尽量在 PLC 中完成，因为 PLC 更适合实时控制和保护。

### 原因 4：配方描述的是工艺意图，不是控制细节
配方更关心的是：
- 加 20kg 原料 A
- 加热到 80°C
- 搅拌 10 分钟
- 转移到下游罐

而不是：
- 打开 V101
- 延时 2 秒
- 启动 P201
- 检查 LS102
- 再关闭 V103

### 一句话总结
**FTBatch 决定做什么，PLC 决定怎么做，而 Phase 就是两者之间的标准动作接口。**

---

## 4. Unit、Operation、Phase 三者是什么关系？

这些概念来自 **ISA-88 / FactoryTalk Batch**，它们描述了配方执行的层级结构。

### 最短定义
- **Unit**：设备单元，完成某类工艺任务的设备
- **Operation**：一个工艺阶段中的动作集合
- **Phase**：最小可执行动作，由控制层具体实现

### 层级关系
```text
Procedure
  └─ Unit Procedure
       └─ Operation
            └─ Phase
```

如果只聚焦这三个概念，可以理解为：

```text
Unit（设备）
  └─ 承载若干 Operation
       └─ 每个 Operation 由若干 Phase 构成
```

### 直观理解
- **Unit** = 配方在哪台设备上执行
- **Operation** = 一个工艺阶段
- **Phase** = 这个阶段中的具体动作

### 工厂例子
假设产品在一台反应釜中生产：

#### Unit
- `Reactor_101`

#### Operation 1：Charge
- `Add_A`
- `Add_B`

#### Operation 2：Heat
- `Heat_To_80`
- `Hold_10_Min`

#### Operation 3：React
- `Agitate`
- `Monitor_Reaction`

#### Operation 4：Transfer
- `Transfer_To_Tank`

其中，真正由控制系统直接执行的最小动作，通常就是 **Phase**。

---

## 5. FTBatch、PhaseManager 和 PLC 是怎么配合的？

### FTBatch
FTBatch 是批处理调度和配方执行层，负责：
- 执行 Recipe
- 按顺序调用 Operation / Phase
- 做设备仲裁
- 跟踪批次状态
- 记录执行过程

它不直接控制现场 IO。

### PhaseManager
PhaseManager 是 Rockwell Logix 中的一个**相位管理框架 / 对象模型**，用于在 PLC 中实现标准化的 Phase 接口。

它通常定义：
- Phase 状态
- Phase 命令
- 参数
- Owner / arbitration
- `Running / Held / Complete / Aborted` 等行为

简单说：

**PhaseManager 帮你在 PLC 里把 Phase 做成标准化、可被 Batch 调用的对象。**

### PLC
PLC 是真正执行控制逻辑的地方，负责：
- 开关阀门
- 启动电机
- 执行联锁保护
- 读取仪表反馈
- 完成实际工艺动作

---

## 6. 从系统角度看整体架构

```text
[Recipe / Batch Procedure]
           │
           ▼
   [FactoryTalk Batch Server]
           │
           │ 调度 Operation / Phase
           │ 下发命令、写参数、读状态
           ▼
   [PLC with PhaseManager]
           │
           │ Phase logic
           ▼
 [Valves / Pumps / Motors / Sensors]
```

这张图表达的是：

- **FTBatch** 负责配方调度
- **PhaseManager / PLC** 负责实现和执行 Phase
- **现场设备** 负责真正完成动作

---

## 7. 一个完整执行示例：Heat 到 80°C

### Step 1：配方调用 Phase
配方执行到加热步骤：

- Operation = Heat
- Phase = `HEAT`
- 参数 = `TargetTemp = 80`

### Step 2：FTBatch 下发命令
FTBatch：
- 给 `HEAT` 写入参数 `80`
- 发出 `Start`

### Step 3：PLC / PhaseManager 接收命令
PLC 中的 `HEAT` phase：
- 接收 `Start`
- 状态切换到 `Running`
- 开始执行加热逻辑
- 实时更新状态

### Step 4：现场设备执行
- 打开蒸汽阀
- 监测温度
- 达到 80°C
- 标记 `Complete`

### Step 5：状态返回给 FTBatch
PLC 将：
- `Running`
- `Complete`
- 或 `Fault`

返回给 FTBatch。

### Step 6：FTBatch 继续下一步
当 FTBatch 看到 `HEAT Complete` 后，就继续执行下一个 Phase。

---

## 8. Unit 在整体架构中的位置

更完整的 Batch 模型可以表示为：

```text
Recipe / Procedure
   │
   ▼
Unit Procedure
   │
   ├─ Unit: Reactor_101
   │    ├─ Operation: Charge
   │    │    ├─ Phase: Add_A
   │    │    └─ Phase: Add_B
   │    ├─ Operation: Heat
   │    │    └─ Phase: Heat_To_80
   │    └─ Operation: Transfer
   │         └─ Phase: Transfer_Out
   │
   ▼
FactoryTalk Batch Server
   ▼
PLC / PhaseManager
   ▼
Field Devices
```

这里可以看到：
- **Unit** 是 Batch 中的设备执行容器
- **Operation** 是工艺步骤分组
- **Phase** 是具体控制动作接口

---

## 9. 最后的三个总结

### 逻辑层次
```text
Procedure > Unit Procedure > Operation > Phase
```

### 系统层次
```text
FTBatch > PLC / PhaseManager > 现场设备
```

### 职责分工
```text
Batch 决定做什么
PLC 决定怎么做
```

---

## 10. 一个通俗比喻

如果把工厂批处理比作拍电影：

- **Recipe** = 剧本
- **FTBatch** = 导演
- **Unit** = 片场
- **Operation** = 一场戏
- **Phase** = 一个具体动作镜头
- **PLC / PhaseManager** = 现场执行团队
- **阀门 / 泵 / 电机** = 真正干活的设备

导演不会自己去搬灯、推摄像机；  
导演负责告诉现场团队“现在执行哪个动作”。  
FTBatch 和 PLC 的关系也是这样。