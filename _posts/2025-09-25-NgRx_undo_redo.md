---                
layout: post                
title: "NgRx学习笔记：undo/redo"                
date:   2025-9-25 18:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      


# Undo / Redo


Undo / Redo 这类场景很适合用来理解状态管理，因为它天然要求你保留历史状态、能够回退、也能够重做。  
如果只靠组件里的临时变量去拼，很快就会变得混乱；但如果状态变化是可追踪的，这类需求会清晰很多。

参考 [Angular Ngrx Undo Redo Demo](https://stackblitz.com/edit/angular-ngrx-undo-redo-demo?file=README.md) 这个示例，Undo / Redo 最常见的实现方式其实很直接：**不要只存当前状态，而是把状态拆成 past、present、future 三部分。**


## 1. 为什么普通 state 不够

假设页面上有一个计数器，用户可以不断点击加一、减一。

如果我们的 store 里只有这样一个结构：

- `count: 0`

那么每次 dispatch action 后，旧值都会被新值覆盖。  
此时你当然能拿到“当前值”，但你已经丢失了“上一步是什么”，自然也就没法真正实现 undo。

所以，Undo / Redo 往往不会直接把状态写成一个扁平对象，而会包装成一个历史记录结构。

## 2. 常见的数据结构

比较经典的写法如下：

- `past`：过去的状态数组
- `present`：当前状态
- `future`：被撤销后、可用于重做的状态数组

也就是：

- `past: State[]`
- `present: State`
- `future: State[]`

可以把它理解成下面这个模型：

- 用户做了一次正常编辑：把旧的 `present` 推入 `past`，再生成新的 `present`
- 用户点击 undo：从 `past` 取出最近一次状态作为新的 `present`，原来的 `present` 放进 `future`
- 用户点击 redo：从 `future` 取出最近一次状态作为新的 `present`，原来的 `present` 放回 `past`

这样状态怎么流转就一目了然了。


## 3. 状态变化过程

比如初始状态为：

- `past = []`
- `present = 0`
- `future = []`

用户连续执行两次加一后：

- 第一次加一后：`past = [0]`，`present = 1`，`future = []`
- 第二次加一后：`past = [0, 1]`，`present = 2`，`future = []`

这时如果执行 undo：

- `past = [0]`
- `present = 1`
- `future = [2]`

再执行一次 undo：

- `past = []`
- `present = 0`
- `future = [2, 1]`

如果此时执行 redo：

- `past = [0]`
- `present = 1`
- `future = [2]`

所以这里的关键不在于“把操作反着做一遍”，而在于**在历史状态之间切换**。


## 4. 在 NgRx 里怎么写

放到 NgRx 里，这件事其实还是老套路：action 描述意图，reducer 负责状态变化。


### action 负责描述意图

一般会有这几类 action：


- 普通业务 action，例如 `add`, `subtract`, `updateText`
- 历史控制 action，例如 `undo`, `redo`
- 有时还会补充 `reset` 或 `clearHistory`

普通业务 action 表示“我要修改状态”；  
而 `undo` / `redo` 表示“我要在历史记录里前进或后退”。

### reducer 负责维护 past / present / future

真正的核心还是 reducer。  
因为 reducer 本来就是纯函数，用来维护历史状态很合适。


对于一次**普通修改**，通常逻辑是：

1. 把当前 `present` 放进 `past`
2. 基于 action 计算新的 `present`
3. 清空 `future`

这里“清空 future”非常重要。  
原因是：如果用户已经 undo 回到了旧状态，然后又做了一次新的编辑，那么原先那条 redo 分支就不再成立了。

对于一次 **undo**，通常逻辑是：

1. 如果 `past` 为空，则保持不变
2. 取出 `past` 最后一个元素作为新的 `present`
3. 把旧的 `present` 放到 `future` 前面或后面（取决于你的实现方式）

对于一次 **redo**，则相反：

1. 如果 `future` 为空，则保持不变
2. 取出 `future` 中最近的一个状态作为新的 `present`
3. 把旧的 `present` 放回 `past`

## 5. 完整 demo：一个支持 undo/redo 的 Counter

下面用一个最简单的计数器例子来看。  
目标很简单：


- 点击 `+1` 修改当前值
- 点击 `-1` 修改当前值
- 点击 `Undo` 回到上一步
- 点击 `Redo` 恢复被撤销的那一步

这个例子虽然小，但结构是完整的：


- action
- state
- reducer
- selector
- component
- Store 注册

如果只是想看核心思路，重点看 reducer 就够了；  
如果想自己搭一个最小示例，下面这套结构可以直接照着写。



### actions

```ts actions.ts
import { createAction } from '@ngrx/store';

export const increment = createAction('[Counter] Increment');
export const decrement = createAction('[Counter] Decrement');
export const undo = createAction('[Counter] Undo');
export const redo = createAction('[Counter] Redo');
```

这里把 action 分成两类：

- `increment` / `decrement`：正常业务操作
- `undo` / `redo`：历史控制操作

### state

```ts state.ts
export interface CounterState {
  count: number;
}

export interface HistoryState<T> {
  past: T[];
  present: T;
  future: T[];
}

export const initialState: HistoryState<CounterState> = {
  past: [],
  present: { count: 0 },
  future: []
};
```

这里的关键是，不直接存一个 `count`，而是把真正的业务状态 `CounterState` 包进 `HistoryState<T>` 里。


### reducer

```ts reducer.ts
import { createReducer, on } from '@ngrx/store';
import { decrement, increment, redo, undo } from './actions';
import { CounterState, HistoryState, initialState } from './state';

function applyNewPresent(
  state: HistoryState<CounterState>,
  newPresent: CounterState
): HistoryState<CounterState> {
  return {
    past: [...state.past, state.present],
    present: newPresent,
    future: []
  };
}

export const counterReducer = createReducer(
  initialState,

  on(increment, (state) =>
    applyNewPresent(state, {
      count: state.present.count + 1
    })
  ),

  on(decrement, (state) =>
    applyNewPresent(state, {
      count: state.present.count - 1
    })
  ),

  on(undo, (state) => {
    if (state.past.length === 0) {
      return state;
    }

    const previous = state.past[state.past.length - 1];

    return {
      past: state.past.slice(0, -1),
      present: previous,
      future: [state.present, ...state.future]
    };
  }),

  on(redo, (state) => {
    if (state.future.length === 0) {
      return state;
    }

    const next = state.future[0];

    return {
      past: [...state.past, state.present],
      present: next,
      future: state.future.slice(1)
    };
  })
);
```

这个 reducer 就是整个例子的核心。


#### 普通修改

以 `increment` 为例：

1. 先把当前 `present` 放进 `past`
2. 计算新的 `present`
3. 清空 `future`

这里要清空 `future`，因为用户一旦在 undo 之后又做了新修改，原来的 redo 路径就不成立了。


#### undo

- 如果 `past` 为空，直接返回当前 state
- 否则取出 `past` 最后一个状态作为新的 `present`
- 当前的 `present` 放入 `future`

#### redo

- 如果 `future` 为空，直接返回当前 state
- 否则取出 `future` 第一个状态作为新的 `present`
- 当前的 `present` 放回 `past`

### selectors

```ts selectors.ts
import { createFeatureSelector, createSelector } from '@ngrx/store';
import { HistoryState, CounterState } from './state';

export const selectCounterHistory =
  createFeatureSelector<HistoryState<CounterState>>('counter');

export const selectCount = createSelector(
  selectCounterHistory,
  (state) => state.present.count
);

export const selectCanUndo = createSelector(
  selectCounterHistory,
  (state) => state.past.length > 0
);

export const selectCanRedo = createSelector(
  selectCounterHistory,
  (state) => state.future.length > 0
);
```

这里更推荐通过 selector 暴露 `canUndo`、`canRedo`，不要让组件自己去判断 `past.length` 或 `future.length`，这样会更清爽一点。


### Store 注册

如果还是传统的 NgModule 写法，可以这样注册：


```ts app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { StoreModule } from '@ngrx/store';
import { AppComponent } from './app.component';
import { counterReducer } from './store/reducer';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    StoreModule.forRoot({
      counter: counterReducer
    })
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

这里的 `counter` 就是 feature key，要和 selector 里 `createFeatureSelector('counter')` 对应起来。

如果项目已经在用 standalone API，也可以在 `app.config.ts` 或 `main.ts` 里通过 `provideStore` 注册，思路是一样的，这里就不展开了。


### component


```ts app.component.ts
import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { decrement, increment, redo, undo } from './store/actions';
import {
  selectCanRedo,
  selectCanUndo,
  selectCount
} from './store/selectors';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  count$ = this.store.select(selectCount);
  canUndo$ = this.store.select(selectCanUndo);
  canRedo$ = this.store.select(selectCanRedo);

  constructor(private store: Store) {}

  increment(): void {
    this.store.dispatch(increment());
  }

  decrement(): void {
    this.store.dispatch(decrement());
  }

  undo(): void {
    this.store.dispatch(undo());
  }

  redo(): void {
    this.store.dispatch(redo());
  }
}
```

```html app.component.html
<h2>Count: {{ count$ | async }}</h2>

<button (click)="decrement()">-1</button>
<button (click)="increment()">+1</button>
<button (click)="undo()" [disabled]="!(canUndo$ | async)">Undo</button>
<button (click)="redo()" [disabled]="!(canRedo$ | async)">Redo</button>
```

组件本身基本不处理状态逻辑：


- 只负责展示 `count`
- 根据 selector 决定按钮是否可点
- 点击按钮时 dispatch 对应 action

这也是 NgRx 比较顺手的一种写法：**组件只处理交互，状态变化统一交给 store。**


### 状态流转示例

假设初始值是 `0`：

1. 点击两次 `+1`
   - `past = [{count: 0}, {count: 1}]`
   - `present = {count: 2}`
   - `future = []`

2. 点击一次 `Undo`
   - `past = [{count: 0}]`
   - `present = {count: 1}`
   - `future = [{count: 2}]`

3. 点击一次 `Redo`
   - `past = [{count: 0}, {count: 1}]`
   - `present = {count: 2}`
   - `future = []`

如果配合 NgRx DevTools 去看，这个过程会更直观。


### 再往前走一步：把 undo/redo 逻辑抽出来

上面的 demo 已经够用了，不过它有个特点：**undo / redo 的逻辑和业务 reducer 写在一起。**

学习阶段这么写完全没问题，胜在直观。  
但如果项目里不止一个 feature 需要撤销/重做，很快就会出现重复代码。

这种情况下，通常会把它抽成一个高阶 reducer，或者单独的包装函数。

下面是一个偏思路型的写法：


```ts undo-redo.ts
export interface HistoryState<T> {
  past: T[];
  present: T;
  future: T[];
}

export function wrapWithHistory<T>(
  reducer: (state: T | undefined, action: any) => T,
  initialPresent: T
) {
  const initialState: HistoryState<T> = {
    past: [],
    present: initialPresent,
    future: []
  };

  return function historyReducer(
    state: HistoryState<T> = initialState,
    action: any
  ): HistoryState<T> {
    switch (action.type) {
      case '[History] Undo': {
        if (state.past.length === 0) {
          return state;
        }

        const previous = state.past[state.past.length - 1];
        return {
          past: state.past.slice(0, -1),
          present: previous,
          future: [state.present, ...state.future]
        };
      }

      case '[History] Redo': {
        if (state.future.length === 0) {
          return state;
        }

        const next = state.future[0];
        return {
          past: [...state.past, state.present],
          present: next,
          future: state.future.slice(1)
        };
      }

      default: {
        const newPresent = reducer(state.present, action);

        if (newPresent === state.present) {
          return state;
        }

        return {
          past: [...state.past, state.present],
          present: newPresent,
          future: []
        };
      }
    }
  };
}
```

这个版本主要是为了说明思路，不一定要原样照搬。  
核心意思就三点：


- 业务 reducer 只关心“当前状态如何变化”
- 历史包装器统一维护 `past / present / future`
- `undo` / `redo` 变成可复用能力，而不是每个 feature 各写一套

如果后面还想继续写进阶一点的内容，这一块其实完全可以单独展开成一篇。


### 这个 demo 的价值

这个写法虽然简单，但已经把核心模式交代清楚了：


- 普通 action 改变业务状态
- undo / redo 改变历史指针
- `past / present / future` 负责保存完整上下文

真正项目里，你可以把 `count` 换成：

- 表单内容
- 画布节点数据
- 富文本内容
- 可视化编辑器中的布局配置

模式本身没变，变的只是 `present` 里面装的业务数据。


### 还可以继续优化什么

在真实项目里，这个 demo 往往还会继续演进：

- 限制 `past` 最大长度，例如只保留最近 20 步
- 只让特定 action 进入历史记录
- 抽一个通用的 `undoRedoReducer` 包装器
- 对大对象使用更细粒度的历史记录策略

所以它既适合拿来入门，也适合作为后面继续封装的起点。


## 6. 这个例子能说明什么

这个例子不只是演示了怎么做 undo / redo，它其实也把 NgRx 里几个很核心的点带出来了。


### 状态是可追踪的

每一步变化都是 action 驱动的，历史记录也明确放在 store 里。  
相比“组件里自己记一个 previousValue”，这种方式更容易维护。


### reducer 逻辑是集中的

撤销、重做、普通修改，规则都放在 reducer 里统一处理，而不是散落在组件事件里。  
这样业务一旦复杂起来，状态怎么变的还是能看得清。


### 很适合配合 DevTools 看状态流

如果配合 NgRx DevTools 去看，会很直观：


- 触发了什么 action
- 当前 `present` 是什么
- `past` / `future` 怎么变化

拿它来理解 NgRx 的状态流很合适。


## 7. 实战里比较容易踩的点

Undo / Redo 看起来不复杂，但放到真实业务里，还是有一些地方要提前想清楚。


### 7.1 不是所有状态都值得记录历史

比如：

- 临时 loading 状态
- 接口错误提示
- hover / panel 开关这类瞬时 UI 状态
- 当前 tab 是否展开
- 某个弹窗是否显示

这些通常不适合放进 undo / redo 历史。  
真正适合记录的，往往是用户“有意编辑”的那部分数据，比如：

- 表单内容
- 画布元素位置
- 文档内容
- 布局配置

一个比较实用的判断标准是：**如果用户会期待“撤销这次编辑”，那它才值得进入历史。**


### 7.2 明确历史粒度

例如文本编辑：

- 是每输入一个字符就记录一次？
- 还是每失焦一次记录一次？
- 还是点击保存草稿前统一记录一次？

粒度太细，历史会膨胀得很快；  
粒度太粗，用户又会觉得 undo 不够自然。

实际项目里更常见的做法是：


- 高频输入先在本地缓冲
- 在某个提交时机统一进入历史
- 或者做节流 / 防抖后再记历史

### 7.3 给历史记录设上限


实际项目中，常见做法是只保留最近 N 步，例如 20 步、50 步。  
这样既能满足大多数撤销场景，也能避免内存占用持续增长。

例如 `past` 在追加时可以裁剪：

```ts reducer.ts
const nextPast = [...state.past, state.present].slice(-20);
```

然后把返回值改成：

```ts reducer.ts
return {
  past: nextPast,
  present: newPresent,
  future: []
};
```

这样就只保留最近 20 次历史。

### 7.4 只让需要的 action 进入历史


并不是所有 action 都应该自动进入 `past`。  
比如下面这些 action，往往不应该计入历史：

- `loadSuccess`
- `loadFailure`
- `toggleLoading`
- `selectTab`
- `hoverNode`

而下面这些 action 更适合进入历史：

- `updateField`
- `moveNode`
- `resizePanel`
- `changeColor`
- `deleteItem`

也就是说，**undo/redo 关心的是“用户编辑结果”，不是所有系统状态变化。**


### 7.5 避免把大对象完整复制太多次

如果 `present` 是一个很大的对象，每次都完整拷贝并压入 `past`，成本可能会比较高。  
这时要考虑：

- 是否只记录关键子树
- 是否拆成多个 feature，各自维护历史
- 是否记录 patch / diff，而不是完整快照
- 是否只对编辑器区域启用 undo/redo，而不是整个全局 store

这也是为什么很多复杂应用不会直接对“整个 AppState”做 undo/redo，而是只对某个 feature state 做。

### 7.6 在 selector 里暴露 canUndo / canRedo

这点不大，但挺实用。


不要在组件里这样写：

- `history.past.length > 0`
- `history.future.length > 0`

更推荐：

- 在 selector 里定义 `selectCanUndo`
- 在 selector 里定义 `selectCanRedo`

这样做有几个直接好处：


- 组件更简洁
- 更利于测试
- 如果将来判断条件变化，不需要改每个组件

### 7.7 新编辑发生后要清空 future

这是实现 undo/redo 时最容易漏掉的地方之一。

假设用户执行了：

1. `0 -> 1 -> 2`
2. undo 回到 `1`
3. 然后又执行一次新的编辑，变成 `10`

这时原本的 `2` 已经不应该再出现在 redo 链路中，所以必须清空 `future`。  
否则 redo 的语义会变得混乱。

### 7.8 尽量让 reducer 保持纯净


Undo / Redo 特别适合放在 reducer 中实现，就是因为 reducer 本身要求：

- 输入确定
- 输出确定
- 无副作用

这样历史切换会比较容易推导，也更容易测试。  
反过来，如果把 undo / redo 逻辑拆到组件事件里，或者散在多个 service 里，后面通常会越来越乱。


### 7.9 配合 DevTools 调试

NgRx DevTools 在这个场景下很好用。  
你可以很直观地看到：


- 每次 dispatch 了什么 action
- `present` 如何变化
- `past` 和 `future` 如何移动

不管是学习还是排查问题，都很方便。


### 7.10 先从 feature 级别开始，不要一上来做全局撤销


如果项目真的需要 undo/redo，建议先问清楚：

- 到底是哪一块业务需要撤销？
- 是整个页面，还是某个编辑区域？
- 用户预期撤销的是哪类操作？

大多数情况下，**对某个 feature 做局部 undo/redo** 会比“让全局所有状态都支持撤销”更现实，也更容易维护。


## 8. 小结

Undo / Redo 很适合拿来练习 NgRx，因为它把状态管理里几个最核心的问题都摆出来了：


- 状态如何建模
- 状态变化如何追踪
- reducer 如何保持纯函数
- 为什么不可变更新很重要

从实现上说，关键并不复杂：**用 `past / present / future` 包装原始 state，在 reducer 里统一处理普通操作、undo 和 redo。**  
把这个模式想明白之后，后面不管是做表单编辑器、流程编排器，还是更复杂的画布类应用，思路都会顺很多。


# Reference


[NgRx](https://ngrx.io/docs)  
[Angular与NgRx状态管理: 最佳实践解析](https://www.jianshu.com/p/7a966d2e791d)  
[Level Up Your NgRx Skills With 10 Time-Tested Best Practices](https://angularexperts.io/blog/level-up-your-ng-rx-skills-with-10-time-tested-best-practices)  
[NgRx — Best Practices for Enterprise Angular Applications](https://wesleygrimes.com/angular/2018/05/30/ngrx-best-practices-for-enterprise-angular-applications)  
[Simplify State Management with NgRx in Angular | NgRx Guide](https://codezup.com/simplifying-state-management-ngrx-angular-guide/)   
[Angular Ngrx Undo Redo Demo](https://stackblitz.com/edit/angular-ngrx-undo-redo-demo?file=README.md)  

