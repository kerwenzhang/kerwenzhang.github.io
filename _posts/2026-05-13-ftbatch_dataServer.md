---                
layout: post                
title: "FTBatch Data Server 学习笔记"                
date:   2026-05-13 18:30:00                 
categories: "FTBatch"                
catalog: true                
tags:                 
    - FTBatch                
---   
# FTBatch Data Server 说明


## 1. 什么是 Data Server

在 FTBatch 中，**Data Server** 是 Batch Server 与底层控制系统、仿真系统或 Phase 执行层之间的通信桥梁。

它的核心作用是：
- 读 Phase 状态
- 写 Phase 命令
- 传递参数
- 读取完成/故障信息

可以理解为：
- **FTBatch**：上层调度者
- **Data Server**：通信桥梁
- **PLC / PC / Simulator**：实际执行者

---

## 2. FTBatch 常见 Data Server 类型总览

| Data Server | 主要连接对象 | 通信方式 | 典型用途 |
|---|---|---|---|
| Live Data | FactoryTalk 数据层 | FactoryTalk Live Data | 接入 FT 平台实时数据 |
| Logix5000 CIP | Logix PLC | CIP | 直接连接 Logix 控制器 |
| PC Phase OPC | PC 上的 phase 逻辑 | OPC | 连接 PC 侧实现的 Phase |
| Simulator OPC | 仿真系统 | OPC | 开发、测试、培训、演示 |
| InstructionBasedServer | 指令式 phase 实现 | 专用接口 | 特定批处理架构 |

---

## 3. 各类 Data Server 详细说明

### 3.1 Live Data

#### 定义
`Live Data` 是通过 **FactoryTalk Live Data** 机制访问实时数据的方式，更偏向 Rockwell FactoryTalk 平台内部的数据层。

#### 实际连接对象
它通常连接的是：
- PLC 标签
- HMI 标签
- 控制模块变量
- FactoryTalk 平台暴露的数据项

严格来说，Live Data 连接的不是抽象的 Phase 对象本身，而是**承载 Phase 状态、命令和参数的数据点**。

#### 适用场景
- 项目已经深度使用 FactoryTalk 平台
- 已经有 FactoryTalk Directory、shortcut、tag 管理
- 数据来源不只是单一 PLC 标签
- 历史项目沿用 FT 数据架构

#### 特点
**优点：**
- 与 FactoryTalk 平台集成度高
- 适合复用已有 FT 数据架构

**注意点：**
- 相比直连 PLC，多一层抽象
- 排障时可能需要同时检查 FT Directory、Live Data 服务、shortcut、数据映射等

#### 一句话理解
**Live Data = 通过 FactoryTalk 数据层访问 Batch 所需实时点位。**

---

### 3.2 Logix5000 CIP

#### 定义
`Logix5000 CIP` 是 FTBatch 直接通过 **CIP（Common Industrial Protocol）** 与 Logix 控制器通信的方式。

#### 实际连接对象
主要连接：
- ControlLogix / CompactLogix
- PLC 中的 tag
- PhaseManager 相关接口
- batch phase 的命令、状态、参数变量

#### 适用场景
- 底层是 Logix PLC
- Phase 在 PLC / PhaseManager 中实现
- 希望减少中间层，直接连接控制器

#### 特点
**优点：**
- 链路短，连接直接
- 对 Logix + PhaseManager 架构匹配度高
- 工程语义清晰，调试通常更直接

**限制：**
- 主要适用于 Logix 控制器
- 跨平台通用性不如 OPC

#### 一句话理解
**Logix5000 CIP = FTBatch 直接跟 Logix PLC 通信。**

---

### 3.3 PC Phase OPC

#### 定义
`PC Phase OPC` 指 FTBatch 通过 **OPC** 去连接**运行在 PC 上的 Phase 执行逻辑**。

这里的关键不是“OPC 连 PLC”，而是：
**OPC 连的是 PC 上的 phase 程序。**

#### OPC Server 是什么
可以把 **OPC Server** 理解成一个标准化的数据接口服务，它把设备或程序里的数据点暴露出来，供其他软件读写。

例如，它可以提供这些点位：
- `TRANSFER.Command`
- `TRANSFER.State`
- `TRANSFER.Param.Quantity`
- `TRANSFER.ErrorCode`

FTBatch 就通过 OPC 去读写这些点。

#### 什么是 PC 侧 phase logic
`PC 侧 phase logic` 是指：
**某个 Phase 的状态机和执行逻辑不是写在 PLC 里，而是写在运行于 PC 上的软件/服务里。**

例如一个 PC 程序可能负责：
- 接收 `Start / Hold / Abort`
- 维护 `Idle / Running / Complete / Aborted` 等状态
- 处理 phase 参数
- 判断何时完成、何时故障
- 与数据库、MES、第三方系统交互

#### Phase 怎么跑在 PC 上
所谓 “Phase 跑在 PC 上”，并不是 FTBatch 自动把 Phase 放到电脑里，而是：
**有人专门写了一个 PC 程序，让它作为 Phase 执行器。**

这个程序会：
- 接收 FTBatch 发来的命令
- 维护 Phase 状态机
- 执行业务或协调逻辑
- 再去调用 PLC、数据库或其他系统
- 最后把状态返回给 FTBatch

#### 一个典型 PC Phase 场景
例如 `TRANSFER` phase：
- FTBatch 通过 OPC 写入参数和 `Start`
- PC 上的 phase 程序收到命令后：
  - 查询数据库确认目标设备可用
  - 检查 MES 是否放行
  - 记录批次开始信息
  - 再命令 PLC 启动泵和阀门动作
- PLC 负责底层设备控制和联锁
- PC 程序监控 PLC 执行结果，并将 `Running / Complete / Aborted` 状态写回 OPC
- FTBatch 读取这些状态并继续配方

#### 适用场景
- 历史系统采用 PC-based phase 架构
- 某些 Phase 需要大量上层业务逻辑
- 需要与数据库、MES、API、第三方系统深度交互
- 仿真或测试环境

#### 特点
**优点：**
- 更适合处理数据库、接口、MES 等上层逻辑
- 与 IT 系统集成方便

**注意点：**
- 实时性和稳定性通常不如 PLC
- 架构更复杂，维护对象更多
- 关键联锁和底层设备保护仍应留在 PLC

#### 一句话理解
**PC Phase OPC = FTBatch 通过 OPC 连接一个运行在 PC 上的 Phase 程序。**

---

### 3.4 Simulator OPC

#### 定义
`Simulator OPC` 是用于仿真环境的 OPC Data Server。

它不连接真实生产设备，而是连接：
- 仿真器
- 模拟 phase
- 假数据源
- 测试控制环境

#### 适用场景
- 开发和调试
- FAT / SAT 前验证
- 培训操作员
- 演示或方案验证

#### 特点
**优点：**
- 不依赖真实设备
- 适合早期联调和培训

**注意点：**
- 无法完全替代现场真实环境
- 不能完全反映实际仪表、机械、网络和联锁行为

#### 一句话理解
**Simulator OPC = FTBatch 通过 OPC 连接仿真环境进行测试。**

---

### 3.5 InstructionBasedServer

#### 定义
`InstructionBasedServer` 是一种更偏专用架构的 Data Server，用于支持 **instruction-based** 的 phase / equipment 实现方式。

它不是最通用的那种数据通道，而更像是为某种特定批处理实现模式准备的接口。

#### instruction-based 是什么意思
可以简单理解为：
- Batch 发出标准化指令
- 底层按约定解释并执行这些指令
- 再返回统一状态和结果

它强调的是一种“按指令驱动”的交互方式，而不是单纯自由读写一组散点 tag。

#### 适用场景
- 项目明确采用 instruction-based 架构
- 特定模板或历史系统
- 需要标准化指令接口的场景

#### 特点
**优点：**
- 对 instruction-based 架构更匹配
- 接口规范化程度较高

**注意点：**
- 使用场景相对专门
- 需要明确理解底层实现模型

#### 一句话理解
**InstructionBasedServer = 为指令式 phase 架构准备的专用数据服务器。**

---

## 4. PLC Phase 与 PC Phase 的区别

同样一个 Phase（例如 `TRANSFER`），底层可以有两种典型实现方式。

### 4.1 纯 PLC Phase

#### 架构
```text
FTBatch
   ↓
Data Server（常见为 Logix5000 CIP）
   ↓
PLC 中的 Phase
   ↓
阀门 / 泵 / 仪表
```

#### 特点
- Phase 状态机在 PLC 中
- PLC 直接负责相位逻辑和设备控制
- 结构简单，实时性好
- 故障边界更清晰

#### 适合场景
- 设备控制型 Phase
- 需要实时联锁和稳定执行的场景
- 新建 Logix + PhaseManager 项目

### 4.2 PC Phase

#### 架构
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

#### 特点
- Phase 状态机在 PC 程序中
- PC 负责上层业务逻辑与流程协调
- PLC 负责底层设备动作与联锁
- 更适合集成数据库、MES、第三方系统
- 架构更复杂

#### 适合场景
- 业务协调型 Phase
- 历史系统
- 与 IT 系统深度集成的场景

### 4.3 一句话区分
- **纯 PLC Phase**：PLC 既是 phase 执行者，也是设备控制者
- **PC Phase**：PC 是 phase 协调者，PLC 是设备执行者

---

## 5. 为什么很多新项目更偏向 Logix5000 CIP / PLC Phase

当底层是 Logix PLC，且 Phase 在 PLC / PhaseManager 中实现时，很多项目会优先选 **Logix5000 CIP**，原因包括：

- 直接连接 PLC，链路更短
- 对 Logix 架构更原生
- 中间层更少
- 排障和维护更直接
- 更符合“控制留在控制层”的原则

相比之下，`Live Data` 更适合已深度依赖 FactoryTalk 数据层的项目，`PC Phase OPC` 更适合特定历史架构或业务协调场景。

---

## 6. 最简总结

如果只用一句话记住这几种 Data Server：

- **Live Data**：走 FactoryTalk 数据层
- **Logix5000 CIP**：直接连 Logix PLC
- **PC Phase OPC**：连运行在 PC 上的 Phase 程序
- **Simulator OPC**：连仿真环境
- **InstructionBasedServer**：连指令式 Phase 架构
