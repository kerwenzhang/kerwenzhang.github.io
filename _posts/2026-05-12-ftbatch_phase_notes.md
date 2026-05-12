---
layout: post
title: "FTBatch：怎么理解 Phase、Operation 和 Unit"
date: 2026-05-12 18:30:00

categories: "FTBatch"
catalog: true
tags:
  - FTBatch
---

# FTBatch：怎么理解 Phase、Operation 和 Unit

最近在补 FTBatch产品知识，发现最容易把人绕进去的，反而不是软件界面怎么点，而是几个最基础的词：**Phase、Operation、Unit**。

单看字面都不难，但一放到 Batch、PLC、PhaseManager 这些上下文里，就特别容易混。这篇主要是把我目前对这几个概念的理解顺一遍。

---

## 1. 先从最核心的 Phase 说起

在 **FTBatch / Batch 控制** 的语境里，**Phase（相位）** 可以先理解成配方执行里的**最小动作单元**。它不是那种很宽泛的“工艺阶段”，而是 **ISA-88 / FactoryTalk Batch** 里一个比较明确的控制对象。

常见的动作包括：
- 加料（Add）
- 加热（Heat）
- 搅拌（Agitate）
- 转移（Transfer）
- 清洗（CIP）
- 保温（Hold）

从工程实现的角度看，一个 Phase 通常会有：
- 能被配方步骤调用
- 自己的状态，比如 Idle、Running、Held、Complete、Aborted
- 能接收命令，比如 Start、Hold、Restart、Stop、Abort
- 一些参数，比如温度设定值、加料重量、搅拌时间

可以把 **Phase** 理解成一个“被 Batch 调用的标准动作”。配方层不会直接写“开哪个阀、停哪个泵、延时几秒”，而是调用更高层的工艺动作，比如 `Add Material`、`Heat To Temperature`、`Transfer Out`，然后由底层 PLC 或 PC 控制逻辑去实现。

所以对我来说，**Phase 更像是 Batch 和控制层之间约定好的一层动作接口**。



---

## 2. Phase 是在 FTBatch 里执行，还是在 PLC 里执行？

我刚开始接触 FTBatch 时，一个很自然的误解就是：既然配方里直接能看到 Phase，那它是不是就在 Batch 里运行？

更准确的说法是：**Phase 的执行逻辑通常在 PLC 或 PC 控制层中实现，而 FTBatch 负责调度、下命令和看状态。**

FTBatch 主要做的是：
- 执行配方
- 决定当前该调用哪个 Phase
- 给 Phase 下发命令
- 传递参数
- 读取状态和结果

PLC / PC 控制层主要做的是：
- 真正控制阀门、泵、电机、加热器
- 按工艺逻辑完成动作
- 返回状态、报警和完成信号

拿“加热到 80°C”这个动作举个例子。假设配方里有一步 `Heat reactor to 80°C`，在 FTBatch 看来，这一步就是调用一个叫 `HEAT` 的 Phase，并把参数 `TargetTemp = 80` 传下去。接下来，FTBatch 会发出 `Start`，然后等待这个 Phase 的状态变化，比如 `Running`、`Complete`、`Held` 或 `Aborted`。

而 PLC 侧的 `HEAT` 逻辑才是真正干活的那一层。它会去打开蒸汽阀或加热器、读取温度反馈、处理超温保护和超时判断，最后在达到条件后把结果返回给 FTBatch。

最关键的一点是：**Phase 不是 Batch 自己直接去执行的物理动作，而是 Batch 调用底层控制层去执行。**



---

## 3. 为什么 FTBatch 不直接去控制阀门和电机？

这里其实就是一个分层问题：**Batch 是工艺调度层，不是底层设备控制层**。

如果 FTBatch 直接去操作每一个阀门、泵和电机，系统很快就会变得很难维护。比如一个看起来很简单的“加料”动作，底层实际可能要处理开阀门、启动泵、检查联锁、读取流量、达到目标后停泵、关闭阀门、故障处理等一整套细节。这些事情本来就更适合放在控制层，而不是塞进配方里。

另外一个很现实的问题是复用。如果每个配方都自己去写一遍底层点位逻辑，不仅重复，而且很容易出错。相反，如果把它封装成一个统一的 Phase，比如 `ADD_MATERIAL`，那不同配方只要调用这个动作就行了。

再往下说，像电机互锁、阀门开闭顺序、温度压力保护、紧急停机、permissive 条件这些东西，本来也更适合留在 PLC。毕竟 PLC 更擅长做实时控制和设备保护。

还有一点我觉得挺重要：**配方描述的应该是工艺意图，而不是控制细节**。

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

所以说到底，还是这句话：**FTBatch 决定做什么，PLC 决定怎么做，而 Phase 就是两者之间的标准动作接口。**



---

## 4. Unit、Operation、Phase 到底怎么区分？

上面把 Phase 单独拎出来说完，再回头看 **Unit、Operation、Phase** 这三个词，关系就清楚一些了。它们本质上是在描述配方执行的不同层级。

可以先这样记：
- **Unit**：设备单元，完成某类工艺任务的设备
- **Operation**：一个工艺阶段中的动作集合
- **Phase**：最小可执行动作，由控制层具体实现

层级关系大致是：

```text
Procedure
  └─ Unit Procedure
       └─ Operation
            └─ Phase
```

如果只聚焦这三个概念，也可以简单理解成：

```text
Unit（设备）
  └─ 承载若干 Operation
       └─ 每个 Operation 由若干 Phase 构成
```

换成更直白的话：
- **Unit** = 配方在哪台设备上执行
- **Operation** = 一个工艺阶段
- **Phase** = 这个阶段里的具体动作

比如产品在一台反应釜中生产，`Reactor_101` 是 Unit，`Charge`、`Heat`、`React`、`Transfer` 可以看成不同的 Operation，而其中真正由控制系统直接执行的最小动作，通常就是 **Phase**。


---

## 5. 放到系统里看：FTBatch、PhaseManager 和 PLC 分别在干什么？

如果只看术语，还是会有点抽象。放到实际系统里看，就容易理解多了。

- **FTBatch** 是批处理调度和配方执行层，负责执行 Recipe、按顺序调用 Operation / Phase、做设备仲裁、跟踪批次状态和记录执行过程。
- **PhaseManager** 不是一个独立运行的软件，更像是 Rockwell 在 Logix 里提供的一套相位管理框架，用来在 PLC 中实现标准化的 Phase 接口。
- **PLC** 则是真正执行控制逻辑的地方，

---

## 6. 从系统角度看一眼整体架构

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

这张图表达的事情其实很简单：

- **FTBatch** 负责配方调度

- **PhaseManager / PLC** 负责实现和执行 Phase
- **现场设备** 负责真正完成动作


---

## 7. 用一个简单例子把前面的东西串起来

还是拿“加热到 80°C”这个动作举例。

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

## 8. 再补一张图：Unit 在整体结构里的位置

如果把 Unit 也一起放进来，完整一点的 Batch 模型大概是这样：

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

## 9. 最后收一下

如果只想先记住最核心的几点，我觉得下面这三条就够了。

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

## 10. 最后用一个不那么严谨但挺好记的比喻

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