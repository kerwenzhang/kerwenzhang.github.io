---
layout: post
title: "Batch 中 Recipe、Equipment 和 Device 的关系"
date: 2026-05-13 20:30:00
categories: "FTBatch"
catalog: true
tags:
  - FTBatch
---

# Rockwell FactoryTalk Batch 中 Recipe、Equipment 和 Device 的关系

在使用 Rockwell FactoryTalk Batch（FTBatch）时，最容易混淆的几个概念就是 **Recipe**、**Equipment** 和 **Device**。  
这几个词看起来都和“设备、执行、控制”有关，但它们处在不同层级，承担的职责并不相同。

可以先记住一句话：

> **Recipe 定义做什么，Equipment 定义在哪做，Device 定义怎么做。**

从执行链路上看，通常可以理解为：

> **Recipe → Equipment → Device**

---

## 一、Recipe：定义工艺逻辑

在 FTBatch 中，Recipe 的职责是定义一批产品如何被生产出来。  
它描述的是工艺过程，而不是具体某个阀门怎么开、某台泵怎么启停。

一个典型的 Recipe，通常会包含：

- 生产步骤的顺序
- 每个步骤的工艺参数
- 需要调用哪些操作动作
- 对设备资源的要求

在 ISA-88 的结构里，Recipe 往往按以下层级组织：

- Procedure
- Unit Procedure
- Operation
- Phase

其中，真正和底层执行发生连接的，通常是 **Phase**。

例如，一个配方可以定义为：

1. 向反应釜加入纯水 100 kg
2. 加热到 70℃
3. 搅拌 15 分钟
4. 排料到下一容器

这里表达的是生产意图和工艺顺序，而不是现场控制细节。

---

## 二、Equipment：定义设备能力模型

在 FTBatch 里，Equipment 不只是设备列表，更重要的是：**按照 ISA-88 建立的设备能力模型**。  
它把设备组织成可供 Recipe 调用和调度的结构。

常见层级包括：

- Process Cell
- Unit
- Equipment Module
- Control Module

其中最关键的通常是 **Unit**，因为 Recipe 往往是在某个 Unit 上运行的。

例如工厂中有两个反应釜：

- Reactor_01
- Reactor_02

从 FTBatch 的角度看，它们是两个可供配方选择和分配的 **Unit**。

此外，Equipment 还要定义这个 Unit 具备哪些可执行能力。  
例如，一个反应釜 Unit 下面可以配置这些 Phase：

- CHARGE
- HEAT
- AGITATE
- TRANSFER_OUT

这些 Phase 代表该设备具备的工艺执行能力，Recipe 在运行时正是通过调用这些能力完成步骤。

---

## 三、Recipe 和 Equipment 如何关联

理解这部分时，最关键的一点是：

> **Recipe 不直接绑定具体物理设备，而是依赖设备模型中的 Unit 和 Phase 来执行。**

这种联系通常体现在三个方面。

### 1. Recipe 的结构要和 Equipment 模型匹配

Recipe 中定义的 Unit Procedure、Operation、Phase，必须能在设备模型中找到对应的执行对象。

例如，一个配方步骤写的是：

- Charge Material
- Heat to Setpoint
- Agitate for Time

那么对应的设备 Unit 中，就应存在类似的 Phase，例如：

- CHARGE
- HEAT
- AGITATE

否则步骤无法真正落地执行。

### 2. 运行时通过 Unit 分配建立执行关系

Recipe 设计阶段描述的是“需要什么设备能力”；  
真正运行时，Batch Engine 会把它分配到某一个具体可用的 Unit 上。

例如：

- Recipe 需要一个 Reactor 类型的 Unit
- Equipment Model 中有 Reactor_01 和 Reactor_02
- 调度时系统把这批生产分配给 Reactor_01

此时，Recipe 和具体 Equipment 的运行关系才真正建立。

### 3. Phase 是 Recipe 与设备执行之间的桥梁

Recipe 步骤，例如“加水 100 kg”，在执行时通常会调用某个 Unit 下的 `CHARGE` Phase。  
这个 Phase 再把动作交给控制器逻辑去完成。

因此可以这样理解：

- Recipe 说的是工艺步骤
- Equipment 提供的是可调用的 Phase
- Phase 把工艺动作转换成可执行控制逻辑

---

## 四、为什么 Unit 下的 Phase 不能随便定义

Unit 下的 Phase 不是随便命名、随便增加的。  
在 FTBatch 中，Phase 不是纯文档概念，而是**可执行对象**，最终要落到控制器逻辑里。

这意味着一个 Phase 至少要满足两点：

- 工艺上有意义
- 控制上有实现

例如这些定义通常是合理的：

- CHARGE
- HEAT
- AGITATE
- TRANSFER
- CIP

因为它们代表的是工艺动作，底层可以由 PLC 或 PhaseManager 逻辑实现。

相反，如果只是随意定义一些没有实际控制逻辑支撑的名字，即使在 Equipment 中存在，也不能真正执行。

### Phase 不是按单个设备点来定义

Phase 一般不是一个阀门一个 Phase，也不是一个电机一个 Phase。  
更常见的做法是：**一个 Phase 代表一个对工艺有意义的操作**，而这个操作底层会调动多个 device。

例如：

- `CHARGE` 可能涉及阀门、泵、流量计或称重模块
- `HEAT` 可能涉及蒸汽阀、温度回路和温度反馈
- `AGITATE` 可能涉及搅拌电机和运行状态监视

因此，Phase 既不能脱离 PLC 和设备能力随意定义，也不适合直接细化成单个设备动作。  
更合理的方式是：**按工艺上可复用、控制上可实现的操作能力来定义。**

---

## 五、Recipe 绑定 Unit 后，可执行动作为什么是有限的

当一个 Recipe 绑定到某个 Equipment Unit 后，它能调用的动作并不是无限的，而是受这个 Unit 已实现能力的约束。

也就是说，Recipe 不是想写什么动作就能写什么动作，而是必须从这个 Unit 已提供的能力集合中选择。

例如，一个 Unit 如果只定义并实现了这些 Phase：

- CHARGE
- AGITATE
- TRANSFER_OUT

那么 Recipe 就可以基于这些能力去编排步骤；  
但不能凭空再调用：

- HEAT
- VACUUM_DRY
- PRESSURIZE

除非这个 Unit 的设备模型和 PLC 逻辑里已经具备并实现了这些能力。

换句话说：

> **Recipe 的可选动作集合，本质上由 Unit 的能力边界决定。**

这也是 Batch 系统能够进行设备分配和执行管理的基础。  
系统必须知道每个 Unit 能做什么，才能判断某个 Recipe 是否能在该 Unit 上运行。

---

## 六、Device：底层物理实现

如果说 Equipment 是逻辑模型，那么 Device 就是物理实现层。

这里的 Device 可以理解为：

- 控制器中的程序对象
- PLC 里的相位逻辑
- 阀门、泵、电机、仪表
- 实际 I/O 点
- PID 回路、称重模块、温控模块等

在工程实现里，Device 才是真正“动起来”的那一层。

例如：

- 开阀门
- 启动泵
- 读取流量计
- 调节蒸汽阀
- 采集温度反馈

这些都属于 Device 层面的动作。

---

## 七、Equipment 和 Device 如何关联

Equipment 和 Device 的关系，不能简单理解成“一条配置项直接把一个 Equipment 对应到一个 Device”。  
更准确的说法是：

> **Equipment 通过控制器中的 Phase 逻辑、模块逻辑或控制对象，间接驱动底层 Device。**

以一个反应釜为例：

在 Equipment Model 中，可能定义的是：

- Reactor_01（Unit）
- Charge Module
- Heat Module
- Agitate Module

而在控制器和现场层面，真正存在的是：

- 进料阀 XV101
- 加料泵 P101
- 蒸汽调节阀 TV201
- 搅拌电机 M301
- 温度变送器 TT401

FTBatch 本身通常不会直接逐个控制现场 I/O。  
Batch 系统调用的是 Unit 下的 Phase，而 Phase 背后一般由 PLC 或控制器逻辑实现。

因此，Equipment 到 Device 的关系通常可以概括为：

> **Equipment → Phase / Module Logic → Device**

---

## 八、一个简单例子

下面用一个简单的生产过程，把三者关系串起来。

### Recipe

配方 `Recipe_A`：

1. 向反应釜加纯水 100 kg
2. 加热到 70℃
3. 搅拌 15 分钟
4. 排料到缓存罐

### Equipment

设备模型中有一个 Unit：

- `Reactor_01`

它具备以下 Phase：

- `CHARGE`
- `HEAT`
- `AGITATE`
- `TRANSFER_OUT`

### Device

现场和 PLC 层面存在这些对象：

- 进水阀 `XV-101`
- 进水泵 `P-101`
- 蒸汽调节阀 `TV-201`
- 搅拌电机 `M-301`
- 出料阀 `XV-401`
- 温度变送器 `TT-201`

### 执行关系

实际运行时的链路大致如下：

- Recipe 步骤“加纯水 100 kg”  
  → 调用 `Reactor_01.CHARGE`

- `CHARGE` Phase 在 PLC 中执行  
  → 打开 `XV-101`  
  → 启动 `P-101`  
  → 读取流量或重量信号  
  → 达到目标后停止加料

- Recipe 步骤“加热到 70℃”  
  → 调用 `Reactor_01.HEAT`

- `HEAT` Phase 在 PLC 中执行  
  → 调节 `TV-201`  
  → 读取 `TT-201` 温度反馈  
  → 达到设定值后进入完成状态

- Recipe 步骤“搅拌 15 分钟”  
  → 调用 `Reactor_01.AGITATE`

- `AGITATE` Phase 在 PLC 中执行  
  → 启动 `M-301`  
  → 计时 15 分钟  
  → 停止搅拌

这样一来，三者之间的职责就比较清楚了：

- **Recipe 负责组织过程**
- **Equipment 负责提供执行能力**
- **Device 负责完成具体控制动作**

---

## 九、总结

理解 FTBatch 中 Recipe、Equipment 和 Device 的关系，可以抓住这样一条主线：

> **Recipe 定义工艺，Equipment 承载工艺，Device 实现控制。**

再进一步看：

- Recipe 通过 **Unit / Phase** 使用 Equipment
- Unit 下的 Phase 必须对应真实可实现的设备能力，不能随意定义
- Recipe 绑定某个 Unit 后，可调用的动作受该 Unit 已实现能力限制
- Equipment 通常通过 **Phase 逻辑 / PLC 程序** 间接驱动 Device

如果把整个系统看成一条完整链路，那么最常见的理解方式就是：

> **Recipe → Unit / Phase → PLC Logic → Device**