---
layout: post
title: "FTBatch Data Server"
date: 2026-05-13 18:30:00
categories: "FTBatch"
catalog: true
tags:
  - FTBatch
---

# FTBatch：怎么理解几种 Data Server

FTBatch支持的Data Server有 `Live Data`、`Logix5000 CIP`、`PC Phase OPC`、`Simulator OPC`、`InstructionBasedServer`。

这篇就把我目前对这几种 Data Server 的理解整理一下，重点还是放在“它们在系统里分别扮演什么角色”上。

---

## 1. 先说最基本的：什么是 Data Server

在 FTBatch 里，**Data Server** 可以先理解成 Batch Server 和底层控制系统之间的通信桥梁。

它主要负责几件事：

- 读 Phase 状态
- 写 Phase 命令
- 传递参数
- 读取完成或故障信息

如果沿用前一篇的思路去理解，大致可以把它看成：

- **FTBatch**：上层调度者
- **Data Server**：中间通信层
- **PLC / PC / Simulator**：实际执行者

也就是说，Batch 并不是直接去控制现场设备，而是通过不同类型的 Data Server 和底层实现打交道。

---

## 2. 先有个整体印象：FTBatch 里常见的 Data Server

| Data Server | 主要连接对象 | 通信方式 | 典型用途 |
|---|---|---|---|
| Live Data | FactoryTalk 数据层 | FactoryTalk Live Data | 接入 FT 平台实时数据 |
| Logix5000 CIP | Logix PLC | CIP | 直接连接 Logix 控制器 |
| PC Phase OPC | PC 上的 phase 逻辑 | OPC | 连接 PC 侧实现的 Phase |
| Simulator OPC | 仿真系统 | OPC | 开发、测试、培训、演示 |
| InstructionBasedServer | 指令式 phase 实现 | 专用接口 | 特定批处理架构 |

如果先不抠细节，可以先这样记：

- **Live Data**：走 FactoryTalk 平台的数据层
- **Logix5000 CIP**：直接连 Logix PLC
- **PC Phase OPC**：连 PC 上的 Phase 程序
- **Simulator OPC**：连仿真环境
- **InstructionBasedServer**：连指令式实现

---

## 3. 逐个来看这几种 Data Server

## 3.1 Live Data

`Live Data` 是通过 **FactoryTalk Live Data** 机制访问实时数据的一种方式，更偏向 Rockwell FactoryTalk 平台内部的数据层。

它通常连的不是抽象的 Phase 本体，而是：

- PLC 标签
- HMI 标签
- 控制模块变量
- FactoryTalk 平台暴露出来的数据项

也就是说，FTBatch 真正读写的，还是那些承载了 Phase 状态、命令和参数的数据点。

我现在对它的理解更接近于：**先走 FactoryTalk 的数据层，再去拿底层数据**。

所以它比较适合这些场景：

- 项目本来就深度使用 FactoryTalk 平台
- 已经有 FactoryTalk Directory、shortcut、tag 管理
- 数据来源不只是单一 PLC 标签
- 历史项目本来就是按 FT 数据架构做的

它的好处是和 FactoryTalk 平台集成得比较深，已有的数据架构也容易复用；但代价是比起直连 PLC，会多一层抽象，排障时往往也要多看几层。

如果只用一句话记它，可以理解成：

**Live Data = 通过 FactoryTalk 数据层访问 Batch 所需实时点位。**

---

## 3.2 Logix5000 CIP

`Logix5000 CIP` 是 FTBatch 直接通过 **CIP（Common Industrial Protocol）** 跟 Logix 控制器通信的方式。

它主要连的是：

- ControlLogix / CompactLogix
- PLC 里的 tag
- PhaseManager 相关接口
- batch phase 的命令、状态和参数变量

如果底层本来就是 Logix PLC，Phase 也在 PLC / PhaseManager 里实现，那这条路通常是最直观的。因为它本质上就是：**FTBatch 直接去跟 Logix PLC 说话**。

这也是为什么很多新项目会优先选它：

- 链路更短
- 连接更直接
- 对 Logix + PhaseManager 架构匹配度高
- 调试和排障通常也更直接

它的限制也很明显：主要就是面向 Logix 控制器，跨平台通用性不如 OPC。

一句话概括就是：

**Logix5000 CIP = FTBatch 直接跟 Logix PLC 通信。**

---

## 3.3 PC Phase OPC

`PC Phase OPC` 是这几个名字里最容易让人误会的一个。

它指的是：**FTBatch 通过 OPC 去连接运行在 PC 上的 Phase 执行逻辑**。关键点不是“OPC 连 PLC”，而是：**OPC 连的是 PC 上的 phase 程序。**

这里面有两个容易混的概念。

第一个是 **OPC Server**。可以先把它理解成一个标准化的数据接口服务，它把设备或程序里的数据点暴露出来，供其他软件读写。比如它可以提供：

- `TRANSFER.Command`
- `TRANSFER.State`
- `TRANSFER.Param.Quantity`
- `TRANSFER.ErrorCode`

第二个是 **PC 侧 phase logic**。它的意思是，某个 Phase 的状态机和执行逻辑不是写在 PLC 里，而是写在运行于 PC 上的软件或服务里。这个程序会接收 FTBatch 发来的命令，维护 Phase 状态机，执行业务或协调逻辑，再去调用 PLC、数据库或其他系统，最后把状态返回给 FTBatch。

举个典型场景，比如一个 `TRANSFER` phase：

- FTBatch 通过 OPC 写入参数和 `Start`
- PC 上的 phase 程序收到命令后，先去查数据库、查 MES、记录批次信息
- 然后再命令 PLC 去启动泵和阀门动作
- PLC 负责底层设备控制和联锁
- PC 程序监控 PLC 执行结果，再把 `Running / Complete / Aborted` 等状态写回 OPC
- FTBatch 读取这些状态并继续配方

所以它比较适合这些情况：

- 历史系统本来就是 PC-based phase 架构
- 某些 Phase 需要大量上层业务逻辑
- 需要和数据库、MES、API、第三方系统深度集成

它的优点是更方便处理 IT/业务系统集成；缺点是实时性和稳定性通常不如 PLC，而且整体架构会更复杂。

一句话理解就是：

**PC Phase OPC = FTBatch 通过 OPC 连接一个运行在 PC 上的 Phase 程序。**

---

## 3.4 Simulator OPC

`Simulator OPC` 比较好理解，它本质上就是用于仿真环境的 OPC Data Server。

它不连真实生产设备，而是去连：

- 仿真器
- 模拟 phase
- 假数据源
- 测试控制环境

所以它特别适合：

- 开发和调试
- FAT / SAT 前验证
- 培训操作员
- 演示或方案验证

它的优点是不用依赖真实设备，早期联调和培训都很方便；但缺点也很明显：仿真环境再像，也不可能完全替代真实现场。

可以把它简单记成：

**Simulator OPC = FTBatch 通过 OPC 连接仿真环境进行测试。**

---

## 3.5 InstructionBasedServer

`InstructionBasedServer` 也是一个比较偏专用的 Data Server。它主要用于支持 **instruction-based** 的 phase / equipment 实现方式。

这个名字不太直观，但可以先简单理解成：

- Batch 发出标准化指令
- 底层按约定去解释和执行这些指令
- 再返回统一状态和结果

它强调的是一种“按指令驱动”的交互方式，而不是单纯自由读写一堆散点 tag。

所以它更适合这些场景：

- 项目明确采用 instruction-based 架构
- 特定模板或历史系统
- 需要标准化指令接口的场景

它的好处是接口规范化程度更高，但问题也在于使用场景相对专门，前提是你得先清楚底层实现模型到底是什么。

一句话理解就是：

**InstructionBasedServer = 为指令式 phase 架构准备的专用数据服务器。**

---

## 4. 顺便补一下：PLC Phase 和 PC Phase 到底差在哪？

理解 `PC Phase OPC` 时，顺手把 **PLC Phase** 和 **PC Phase** 的区别一起看掉，会更容易不混。

同样一个 Phase，比如 `TRANSFER`，底层其实可以有两种典型实现方式。

### 4.1 纯 PLC Phase

```text
FTBatch
   ↓
Data Server（常见为 Logix5000 CIP）
   ↓
PLC 中的 Phase
   ↓
阀门 / 泵 / 仪表
```

这种方式下：

- Phase 状态机在 PLC 中
- PLC 直接负责相位逻辑和设备控制
- 结构相对简单
- 实时性更好
- 故障边界也更清楚

它更适合设备控制型 Phase，以及那些强调实时联锁和稳定执行的场景。

### 4.2 PC Phase

```text
FTBatch
   ↓
PC Phase OPC
   ↓
OPC Server
   ↓
PC 上的 Phase 程序
   ↓
PLC（设备执行）
   ↓
阀门 / 泵 / 仪表
```

这种方式下：

- Phase 状态机在 PC 程序中
- PC 负责上层业务逻辑和流程协调
- PLC 负责底层设备动作和联锁
- 更适合集成数据库、MES、第三方系统
- 但整体架构也更复杂

它更适合历史系统，或者那些本身就带较多业务协调逻辑的场景。

如果只用一句话区分：

- **纯 PLC Phase**：PLC 既是 phase 执行者，也是设备控制者
- **PC Phase**：PC 是 phase 协调者，PLC 是设备执行者

---

## 5. 为什么很多新项目更偏向 Logix5000 CIP / PLC Phase

当底层是 Logix PLC，且 Phase 在 PLC / PhaseManager 中实现时，很多项目会优先选 **Logix5000 CIP**。

原因其实很朴素：

- 直接连接 PLC，链路更短
- 对 Logix 架构更原生
- 中间层更少
- 排障和维护更直接
- 更符合“控制尽量留在控制层”的原则

相比之下：

- `Live Data` 更适合已经深度依赖 FactoryTalk 数据层的项目
- `PC Phase OPC` 更适合历史架构，或者需要大量业务协调逻辑的场景

所以这也不是谁绝对更高级，而是谁更适合当前系统架构。

---

## 6. 最后收一下

如果只想先记住最核心的几点，我觉得下面这几句就够了：

- **Live Data**：走 FactoryTalk 数据层
- **Logix5000 CIP**：直接连 Logix PLC
- **PC Phase OPC**：连运行在 PC 上的 Phase 程序
- **Simulator OPC**：连仿真环境
- **InstructionBasedServer**：连指令式 Phase 架构

如果再进一步压缩成一句话，那就是：

**Data Server 的区别，本质上就是 FTBatch 到底通过哪种路径，去和底层的 Phase 实现打交道。**