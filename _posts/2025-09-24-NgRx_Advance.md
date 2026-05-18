---                
layout: post                
title: "NgRx学习笔记：进阶篇"                
date:   2025-9-24 18:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      




这一篇继续整理 NgRx 里更常用的进阶内容。  
默认你已经看过前一篇基础篇，至少对 Action、Reducer、Selector、Effect 这几个核心概念有基本认识。

基础篇解决的是“NgRx 到底在做什么”，这一篇更偏向“项目里通常会怎么用”。

很多内容单独看都不难，难的是把它们放回真实项目里理解。

这一篇就按项目里最常见的四块内容来整理：

- Store
- Selectors
- Effects
- Entity

# Store



NgRx Store 是整个状态管理体系的中心。  
它负责统一保存应用状态，并规定状态只能通过明确的流程发生变化。

可以把 Store 理解成：

> 应用中一个统一的数据仓库。

当组件越来越多、页面之间共享的数据越来越复杂时，把状态集中放进 Store，会比各个组件自己维护更容易追踪，也更容易维护。


Store 更适合放这类状态：

- 多个组件共享的数据
- 页面切换后仍要保留的数据
- 需要从后端加载的数据
- 会被多个动作共同修改的数据
- 希望能够统一追踪变化过程的数据

如果只是组件内部的临时 UI 状态，比如：

- 弹窗是否打开
- 输入框当前内容
- hover 状态
- 一个局部 tab 的切换状态

通常没必要放进 Store。

---

## 初始化 Store

先看怎么初始化一个 Store：

    ng generate store State --root --state-path store --module app.module.ts --state-interface AppState

常见参数含义：

- `--root`：创建根 Store
- `--state-path`：指定状态文件目录
- `--module`：注册到哪个模块
- `--state-interface`：指定全局状态接口名称

生成后通常会有类似结构。


`app.module.ts`

```ts
@NgModule({
    imports: [
        StoreModule.forRoot(reducers, { metaReducers }),
        StoreDevtoolsModule.instrument()
    ],
})
export class AppModule {}
```

`src/app/store/index.ts`

```ts
import { ActionReducerMap } from '@ngrx/store';

export interface AppState {
}

export const reducers: ActionReducerMap<AppState> = {
};
```

这里的核心思想其实很直接：


- `AppState` 描述整个应用状态长什么样
- `reducers` 决定每一块状态交给哪个 reducer 管理

---

## MetaReducer

初始化完 Store 之后，接下来可以看一个经常在项目里碰到的概念：MetaReducer。

MetaReducer 可以理解成：


> 在 Action 到 Reducer 之间再加一层统一处理逻辑。

它常见的用途有：

- 打日志
- 统一错误处理
- 清空状态
- 状态持久化
- 仅开发环境下输出调试信息

MetaReducer 本质上是一个函数。  
它接收一个 reducer，再返回一个新的 reducer。

例如一个简单的日志 MetaReducer：

```ts
import { ActionReducer, MetaReducer } from '@ngrx/store';
import { isDevMode } from '@angular/core';

export function logger(reducer: ActionReducer<AppState>): ActionReducer<AppState> {
    return function(state, action) {
        const nextState = reducer(state, action);
        console.log('last state:', state);
        console.log('action:', action);
        console.log('next state:', nextState);
        return nextState;
    };
}

export const metaReducers: MetaReducer<AppState>[] =
    isDevMode() ? [logger] : [];
```

这样每次 dispatch action 时，都能看到：


- 旧状态
- 当前 action
- 新状态

对学习和排查问题都很有帮助。


---

## root state 与 feature state

再往下就是 Store 的组织方式。  
在 NgRx 中，整个应用状态本质上是一个大对象，这个大对象通常会被拆成两类状态：


- **root state**：应用启动时就存在的全局状态
- **feature state**：某个功能模块单独挂载的状态

### 1. root state

通过 `StoreModule.forRoot()` 注册的是根状态：

```ts
import { NgModule } from '@angular/core';
import { StoreModule } from '@ngrx/store';
import { scoreboardReducer } from './reducers/scoreboard.reducer';

@NgModule({
    imports: [
        StoreModule.forRoot({ game: scoreboardReducer })
    ],
})
export class AppModule {}
```

这表示应用启动后，Store 中立刻有一块 `game` 状态。

例如：

```ts
{
    game: {
        home: 0,
        away: 0
    }
}
```

适合放在 root state 的，一般是：

- 应用启动就要用的数据
- 全局共享的数据
- 整个应用生命周期都常驻的数据

---

### 2. feature state

通过 `StoreModule.forFeature()` 注册的是特性状态。

例如先让根 Store 为空：

```ts
@NgModule({
    imports: [
        StoreModule.forRoot({})
    ],
})
export class AppModule {}
```

在某个功能模块中注册自己的状态：

`scoreboard.reducer.ts`

```ts
export const scoreboardFeatureKey = 'game';
```

`scoreboard.module.ts`

```ts
import { NgModule } from '@angular/core';
import { StoreModule } from '@ngrx/store';
import {
    scoreboardFeatureKey,
    scoreboardReducer
} from './reducers/scoreboard.reducer';

@NgModule({
    imports: [
        StoreModule.forFeature(scoreboardFeatureKey, scoreboardReducer)
    ],
})
export class ScoreboardModule {}
```

再把这个模块引入到 `AppModule`：

```ts
import { NgModule } from '@angular/core';
import { StoreModule } from '@ngrx/store';
import { ScoreboardModule } from './scoreboard/scoreboard.module';

@NgModule({
    imports: [
        StoreModule.forRoot({}),
        ScoreboardModule
    ],
})
export class AppModule {}
```

这样最终 Store 就会扩展出：

```ts
{
    game: {
        home: 0,
        away: 0
    }
}
```

### root state 与 feature state 的区别

可以简单理解为：


- `forRoot()`：定义应用级别的基础状态
- `forFeature()`：给某个具体业务模块挂载自己的状态

在中大型项目里，通常会把大多数业务状态拆成 feature state，这样结构会更清晰，也更便于维护。

Store 这一部分更偏向“状态怎么组织”。  
接下来再看 Selectors，也就是“状态怎么读”。

# Selectors



前面已经知道 Selector 是“从状态中取数据”的工具。  
到了进阶场景里，它的价值会更明显。


它的作用不只是“取值”，还包括：

- 组合多个状态片段
- 生成派生数据
- 屏蔽状态结构细节
- 通过记忆化提升性能
- 统一组件的数据读取入口

---

## 创建基础 Selector

先看最基础的 selector 写法。

可以通过命令生成 selector：


    ng g selector store/selectors/counter

示例：

```ts
import { createFeatureSelector, createSelector } from '@ngrx/store';
import { counterFeatureKey, State } from '../reducers/counter.reducer';

export const selectFeatureCounter =
    createFeatureSelector<State>(counterFeatureKey);

export const selectCount = createSelector(
    selectFeatureCounter,
    (state: State) => state.count
);
```

组件中使用：

```ts
import { select, Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import { AppState } from './store';
import { selectCount } from './store/selectors/counter.selectors';

export class AppComponent {
    count$: Observable<number>;

    constructor(private store: Store<AppState>) {
        this.count$ = this.store.pipe(select(selectCount));
    }
}
```

这样组件只关心自己要什么数据，不用关心这个数据在状态树的第几层。


---

## 组合多个状态


`createSelector` 可以接收多个 selector，一起生成新的派生数据。

例如状态中有：

- 当前选中的用户 `selectedUser`
- 全部图书 `allBooks`

我们希望得到“当前用户相关的图书”。

```ts
import { createSelector } from '@ngrx/store';

export interface User {
    id: number;
    name: string;
}

export interface Book {
    id: number;
    userId: number;
    name: string;
}

export interface AppState {
    selectedUser: User | null;
    allBooks: Book[];
}

export const selectSelectedUser = (state: AppState) => state.selectedUser;
export const selectAllBooks = (state: AppState) => state.allBooks;

export const selectVisibleBooks = createSelector(
    selectSelectedUser,
    selectAllBooks,
    (selectedUser, allBooks) => {
        if (!selectedUser) {
            return allBooks;
        }

        return allBooks.filter(book => book.userId === selectedUser.id);
    }
);
```

这样做有几个好处：


- 组件里不需要自己写过滤逻辑
- 业务规则集中在 selector 中
- 更容易复用
- 更容易测试

---

## 记忆化（Memoization）


`createSelector` 的一个很重要特性是：

> 它会缓存上一次计算结果。

如果输入没变，就直接返回上一次结果，而不会重新执行计算逻辑。

这就是 **Memoization**。

例如：

```ts
import { createSelector } from '@ngrx/store';

interface State {
    counter1: number;
    counter2: number;
}

export const selectCounter1 = (state: State) => state.counter1;
export const selectCounter2 = (state: State) => state.counter2;

export const selectTotal = createSelector(
    selectCounter1,
    selectCounter2,
    (counter1, counter2) => counter1 + counter2
);
```

使用时：

```ts
let state = { counter1: 3, counter2: 4 };

selectTotal(state); // 结果 7
selectTotal(state); // 直接复用缓存结果 7

state = { ...state, counter2: 5 };

selectTotal(state); // 重新计算，结果 8
```

它特别适合：

- 列表过滤
- 总数统计
- 聚合计算
- 昂贵的数据转换

---

## 释放缓存


Selector 的缓存会一直保留在内存中。  
在少数情况下，如果你明确希望释放缓存，可以调用 `release()`。

```ts
selectTotal(state);
selectTotal.release();
```

这不是最常用的功能，不过了解它有助于理解 selector 的工作方式。


---

## Selectors 与 CQRS

NgRx 很强调“读”和“写”的分离：

- Reducer 负责写入状态
- Selector 负责读取状态

这和 CQRS（Command Query Responsibility Segregation）的思想很接近：

- Command：写
- Query：读

所以可以简单记成：

> Reducer 负责“怎么改”，Selector 负责“怎么读”。

如果说 Selector 解决的是“怎么把状态读出来”，那 Effects 解决的就是“异步逻辑放在哪里”。

# Effects



如果说 Reducer 负责**纯粹的状态变化**，那 Effects 负责的就是：


- API 请求
- 延迟任务
- 路由跳转
- 打日志
- 访问浏览器对象
- 其他副作用

它的核心目标是：

> 把异步逻辑和副作用从组件中拆出去。

这样组件就可以更专注于展示数据和 dispatch action。


---

## 一个简单的 Effect 示例

先看一个最小的 effect 例子。

先在页面上加一个按钮：


```html
<button (click)="delayAdd()">Delay add</button>
```

定义 action：

```ts
import { createActionGroup, emptyProps, props } from '@ngrx/store';

export const CounterActions = createActionGroup({
    source: 'Counter',
    events: {
        'Increment': props<{ count: number }>(),
        'Decrement': emptyProps(),
        'Delay Add': emptyProps()
    }
});
```

组件中 dispatch：

```ts
delayAdd() {
    this.store.dispatch(CounterActions.delayAdd());
}
```

创建 effect：

    ng g effect store/effects/counter --root --module ../../app.module.ts

修改 `counter.effects.ts`：

```ts
import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { map, mergeMap, timer } from 'rxjs';
import { CounterActions } from '../actions/counter.actions';

@Injectable()
export class CounterEffects {
    delayAdd$ = createEffect(() =>
        this.actions$.pipe(
            ofType(CounterActions.delayAdd),
            mergeMap(() =>
                timer(2000).pipe(
                    map(() => CounterActions.increment({ count: 10 }))
                )
            )
        )
    );

    constructor(private actions$: Actions) {}
}
```

这个 effect 的流程就是：

1. 监听 `Delay Add`
2. 等待 2 秒
3. dispatch 一个 `Increment({ count: 10 })`

---

## Effects 与组件内副作用的对比

很多 Angular 项目里，组件会直接注入 service 并发请求。  
这样当然也能工作，但项目一大，组件就很容易变重。


例如组件可能同时负责：

- 发请求
- 处理 loading
- 处理错误
- 更新列表
- 写订阅逻辑

这时组件的职责就会越来越混乱。


Effects 的思路是：

- 组件只 dispatch action
- Effect 处理异步逻辑
- Reducer 更新状态
- Selector 把结果提供给组件

例如电影列表示例中，组件只表达“我要加载电影”：

```ts
ngOnInit() {
    this.store.dispatch(loadMovies());
}
```

真正请求 API 的逻辑放在 effect 中：

```ts
loadMovies$ = createEffect(() =>
    this.actions$.pipe(
        ofType(loadMovies),
        exhaustMap(() =>
            this.moviesService.getAll().pipe(
                map(movies => moviesLoadedSuccess({ movies })),
                catchError(() => EMPTY)
            )
        )
    )
);
```

这样组件会轻很多，也更容易测试。


---

## 注册方式


### 1. NgModule 方式

在传统模块化 Angular 中：

```ts
EffectsModule.forRoot([CounterEffects])
```

或者：

```ts
EffectsModule.forFeature([FeatureEffects])
```

---

### 2. Standalone 方式

如果项目使用 standalone API：

```ts
import { provideEffects } from '@ngrx/effects';

bootstrapApplication(AppComponent, {
    providers: [
        provideEffects([MoviesEffects])
    ]
});
```

feature 级别也可以在路由里注册：

```ts
import { Route } from '@angular/router';
import { provideEffects } from '@ngrx/effects';

export const routes: Route[] = [
    {
        path: '',
        providers: [
            provideEffects([MoviesEffects])
        ]
    }
];
```

---

## 在 Action 中携带数据


有时候 effect 不只是关心 action 类型，还需要额外参数。  
这时就可以通过 `props` 传值。


例如登录：

```ts
import { createAction, props } from '@ngrx/store';
import { Credentials } from '../models/user';

export const login = createAction(
    '[Login Page] Login',
    props<{ credentials: Credentials }>()
);
```

effect 中使用：

```ts
login$ = createEffect(() =>
    this.actions$.pipe(
        ofType(login),
        exhaustMap(action =>
            this.authService.login(action.credentials).pipe(
                map(user => loginSuccess({ user }))
            )
        )
    )
);
```

---

## 从 Store 中读取额外状态


有时 effect 处理逻辑还需要结合当前 Store 状态。  
这时可以配合 `concatLatestFrom` 使用。

```ts
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { concatLatestFrom } from '@ngrx/operators';

addBookToCollectionSuccess$ = createEffect(
    () =>
        this.actions$.pipe(
            ofType(CollectionApiActions.addBookSuccess),
            concatLatestFrom(() =>
                this.store.select(fromBooks.getCollectionBookIds)
            ),
            tap(([_action, bookCollection]) => {
                if (bookCollection.length === 1) {
                    window.alert('恭喜你添加了第一本书！');
                } else {
                    window.alert('你已添加第 ' + bookCollection.length + ' 本书');
                }
            })
        ),
    { dispatch: false }
);
```

如果 effect 只是做副作用，不再 dispatch 新 action，就加上：


```ts
{ dispatch: false }
```

---

## 不依赖 Action 的 Effect


虽然大多数 effect 都是监听 action，但本质上 effect 也是 Observable 流。  
所以它也可以监听别的可观察源。

例如监听页面点击：

```ts
import { Injectable } from '@angular/core';
import { createEffect } from '@ngrx/effects';
import { fromEvent } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class UserActivityEffects {
    trackUserActivity$ = createEffect(
        () =>
            fromEvent(document, 'click').pipe(
                tap(event => this.analyticsService.track(event))
            ),
        { dispatch: false }
    );

    constructor(private analyticsService: AnalyticsService) {}
}
```

这类写法不算最常见，但它能帮助理解：

> Effect 本质上是“响应流中的事件并执行副作用”的地方，不一定只能响应 action。

Effects 解决的是副作用的问题，Entity 解决的则是另一类很常见的问题：**列表型数据怎么管理得更顺手**。

# Entity



在 NgRx 里，当你需要管理**一组同类型数据**时，比如：

- 用户列表
- 商品列表
- 文章列表
- 评论列表

如果完全手写 state、reducer、selector，通常会出现很多重复代码。  
例如你可能要自己处理：

- 列表新增
- 列表更新
- 列表删除
- 按 id 查找单条数据
- 维护有序数组
- 避免重复项

这时候就可以使用 **NgRx Entity**。

先用一句话概括：


> NgRx Entity 是一套专门用来管理“集合型状态”的工具。

它帮你把“列表数据的增删改查”这类高频操作标准化了。

---

## 为什么需要 Entity？

先看一个很常见的列表状态写法：

```ts
export interface UserState {
    users: User[];
    selectedUserId: number | null;
}
```

这种写法当然可以用，但数据量一大、操作一多，就会遇到一些问题：


### 1. 按 id 查找效率不高

如果你要找 id 为 `3` 的用户，通常要写：

```ts
const user = state.users.find(user => user.id === 3);
```

每次都要遍历数组。

### 2. 更新某一项代码比较繁琐

比如更新某个用户名称，往往要写一堆 `map`：

```ts
users: state.users.map(user =>
    user.id === updatedUser.id ? updatedUser : user
)
```

### 3. 很多集合操作逻辑重复

不同模块里都在重复写：

- add one
- add many
- update one
- remove one
- remove many

而这些逻辑其实都是套路化的。

---

## Entity 的核心思想

NgRx Entity 推荐把集合状态整理成下面这种结构：

```ts
{
    ids: [1, 2, 3],
    entities: {
        1: { id: 1, name: 'Tom' },
        2: { id: 2, name: 'Jerry' },
        3: { id: 3, name: 'Alice' }
    }
}
```

这是一种“**字典 + id 数组**”的结构：

- `ids`：保存顺序
- `entities`：按 id 存放实体对象，方便快速查找

这样设计有两个直接好处：

### 1. 查找快

```ts
const user = state.entities[2];
```

不需要遍历数组。

### 2. 增删改统一

EntityAdapter 已经把常见操作封装好了。


---

## Entity 中几个最核心的概念

### 1. EntityState

`EntityState<T>` 是 NgRx Entity 提供的标准集合状态接口。

例如：

```ts
import { EntityState } from '@ngrx/entity';

export interface User {
    id: number;
    name: string;
}

export interface UserState extends EntityState<User> {
    selectedUserId: number | null;
    loading: boolean;
}
```

这里的意思是：

- `UserState` 继承了 Entity 的标准结构
- 同时还能额外加自己的业务字段

所以最终 state 不只是 `ids` 和 `entities`，还可以有：

- `selectedUserId`
- `loading`
- `error`
- `loaded`

这里有个很重要的点：


> Entity 只是帮你管理集合结构，不会限制你扩展自己的业务状态。

---

### 2. EntityAdapter

`EntityAdapter` 可以理解成一个“集合操作工具箱”。

它会帮你生成很多常用方法，比如：

- `addOne`
- `addMany`
- `setAll`
- `updateOne`
- `updateMany`
- `removeOne`
- `removeMany`
- `removeAll`
- `upsertOne`
- `upsertMany`

你不需要每次都自己手写数组操作。

---

### 3. getInitialState

它用于生成初始状态。

例如：

```ts
const initialState: UserState = adapter.getInitialState({
    selectedUserId: null,
    loading: false
});
```

它会自动补上：

- `ids: []`
- `entities: {}`

再加上你自己的额外字段。

---

## 一个完整的 Entity 示例

下面用“文章列表”做一个最小示例。

假设每篇文章长这样：

```ts
export interface Article {
    id: number;
    title: string;
    content: string;
}
```

---

## 1. 定义 State 与 Adapter

创建 `article.reducer.ts`：

```ts
import { createReducer, on } from '@ngrx/store';
import {
    EntityState,
    EntityAdapter,
    createEntityAdapter
} from '@ngrx/entity';
import * as ArticleActions from './article.actions';

export interface Article {
    id: number;
    title: string;
    content: string;
}

export interface ArticleState extends EntityState<Article> {
    selectedArticleId: number | null;
    loading: boolean;
}

export const adapter: EntityAdapter<Article> =
    createEntityAdapter<Article>();

export const initialState: ArticleState = adapter.getInitialState({
    selectedArticleId: null,
    loading: false
});

export const articleReducer = createReducer(
    initialState,

    on(ArticleActions.loadArticlesSuccess, (state, { articles }) =>
        adapter.setAll(articles, {
            ...state,
            loading: false
        })
    ),

    on(ArticleActions.addArticleSuccess, (state, { article }) =>
        adapter.addOne(article, state)
    ),

    on(ArticleActions.updateArticleSuccess, (state, { update }) =>
        adapter.updateOne(update, state)
    ),

    on(ArticleActions.deleteArticleSuccess, (state, { id }) =>
        adapter.removeOne(id, state)
    ),

    on(ArticleActions.selectArticle, (state, { id }) => ({
        ...state,
        selectedArticleId: id
    }))
);
```

这个 reducer 的重点不在语法，而是要看出 Entity 带来的简化：


- 加一篇文章：`adapter.addOne`
- 批量设置文章：`adapter.setAll`
- 更新一篇文章：`adapter.updateOne`
- 删除一篇文章：`adapter.removeOne`

相比自己手写数组处理，代码会整洁很多。

---

## 2. 定义 Actions

`article.actions.ts`：

```ts
import { createAction, props } from '@ngrx/store';
import { Update } from '@ngrx/entity';
import { Article } from './article.reducer';

export const loadArticlesSuccess = createAction(
    '[Article API] Load Articles Success',
    props<{ articles: Article[] }>()
);

export const addArticleSuccess = createAction(
    '[Article API] Add Article Success',
    props<{ article: Article }>()
);

export const updateArticleSuccess = createAction(
    '[Article API] Update Article Success',
    props<{ update: Update<Article> }>()
);

export const deleteArticleSuccess = createAction(
    '[Article API] Delete Article Success',
    props<{ id: number }>()
);

export const selectArticle = createAction(
    '[Article Page] Select Article',
    props<{ id: number }>()
);
```

这里有个值得注意的地方：


更新时使用的是 `Update<T>`：

```ts
{
    id: 1,
    changes: {
        title: '新标题'
    }
}
```

这表示：

- 哪条数据要更新
- 具体改哪些字段

这比直接传整个对象更灵活。

---

## 3. 使用 Adapter 自动生成 Selectors

NgRx Entity 很方便的一点是：  
它可以直接帮你生成一组常用 selector。


`article.selectors.ts`：

```ts
import { createFeatureSelector, createSelector } from '@ngrx/store';
import { adapter, ArticleState } from './article.reducer';

export const selectArticleState =
    createFeatureSelector<ArticleState>('articles');

const {
    selectIds,
    selectEntities,
    selectAll,
    selectTotal
} = adapter.getSelectors(selectArticleState);

export const selectArticleIds = selectIds;
export const selectArticleEntities = selectEntities;
export const selectAllArticles = selectAll;
export const selectArticleTotal = selectTotal;

export const selectSelectedArticleId = createSelector(
    selectArticleState,
    state => state.selectedArticleId
);

export const selectCurrentArticle = createSelector(
    selectArticleEntities,
    selectSelectedArticleId,
    (entities, selectedId) =>
        selectedId !== null ? entities[selectedId] ?? null : null
);
```

这里自动得到的几个 selector 很常用：

- `selectIds`：所有 id
- `selectEntities`：实体字典
- `selectAll`：数组形式的全部数据
- `selectTotal`：总数

这意味着：

> state 内部虽然是 `ids + entities` 结构，但组件依然可以很方便地拿到普通数组。

所以不用太担心 Entity 会让组件使用起来变复杂。


---

## 4. 组件中如何使用

例如：

```ts
export class ArticleListComponent {
    articles$ = this.store.select(selectAllArticles);
    total$ = this.store.select(selectArticleTotal);
    currentArticle$ = this.store.select(selectCurrentArticle);

    constructor(private store: Store) {}

    selectArticle(id: number) {
        this.store.dispatch(selectArticle({ id }));
    }
}
```

组件并不需要知道底层是 `entities` 还是数组。  
它只通过 selector 拿自己想要的数据。

这也是 NgRx 的一个核心思路：


> 组件只消费数据，不关心状态内部实现细节。

---

## EntityAdapter 常见方法整理

下面把常用方法简单过一遍。


### 1. addOne

新增一条数据：

```ts
adapter.addOne(article, state)
```

### 2. addMany

新增多条数据：

```ts
adapter.addMany(articles, state)
```

### 3. setAll

用新数据整体替换旧集合：

```ts
adapter.setAll(articles, state)
```

适合“重新加载整个列表”的场景。

### 4. updateOne

更新单条数据：

```ts
adapter.updateOne(
    {
        id: 1,
        changes: { title: '新标题' }
    },
    state
)
```

### 5. upsertOne

如果存在就更新，不存在就新增：

```ts
adapter.upsertOne(article, state)
```

### 6. removeOne

删除单条数据：

```ts
adapter.removeOne(id, state)
```

### 7. removeAll

清空整个集合：

```ts
adapter.removeAll(state)
```

---

## 自定义主键 selectId

默认情况下，Entity 会把 `id` 当作主键。  
但有些数据的唯一标识不是 `id`，比如是 `uuid` 或 `code`。

这时可以在创建 adapter 时指定：

```ts
export interface Product {
    code: string;
    name: string;
}

export const productAdapter = createEntityAdapter<Product>({
    selectId: (product) => product.code
});
```

这样 Entity 就会把 `code` 作为唯一标识。

---

## 排序 sortComparer

有些时候你希望集合始终保持某种顺序，比如按名称排序、按时间排序。  
这时可以使用 `sortComparer`。

```ts
export const articleAdapter = createEntityAdapter<Article>({
    sortComparer: (a, b) => a.title.localeCompare(b.title)
});
```

这样 `selectAll` 返回的数据就会按 `title` 排序。

再比如按创建时间倒序：

```ts
sortComparer: (a, b) => b.createdAt - a.createdAt
```

所以：

- `entities` 负责快速查找
- `ids` 负责顺序维护
- `sortComparer` 负责定义顺序规则

---

## Entity 特别适合哪些场景？

Entity 特别适合下面这些情况：

### 1. 管理列表型数据

例如：

- 用户列表
- 商品列表
- 订单列表
- 评论列表

### 2. 经常根据 id 查单条数据

比如详情页、编辑页、选中项场景。

### 3. 需要频繁增删改

如果这个集合操作很多，Entity 能明显减少样板代码。

### 4. 需要统一列表状态结构

大型项目里，不同模块都用类似的集合结构，会更规范。

---

## Entity 不一定适合哪些场景？

虽然 Entity 很方便，但也不是所有状态都要用它。

例如这些情况，可能没必要：

### 1. 非集合型状态

比如：

- 当前主题色
- 登录状态
- loading 开关
- 表单草稿

### 2. 很简单、一次性的小数组

如果只是一个很短的小列表，而且几乎不会修改，用普通数组就够了。

### 3. 明显是树形或高度嵌套结构

Entity 更擅长“扁平集合”。  
如果是复杂树结构，可能需要先做 normalize，或者用更合适的建模方式。

---

## Entity 与普通数组 state 的对比

### 普通数组写法

```ts
interface State {
    articles: Article[];
}
```

优点：

- 直观
- 上手简单

缺点：

- 按 id 查找不方便
- 更新/删除要手写数组逻辑
- 重复代码多

### Entity 写法

```ts
interface State extends EntityState<Article> {
    selectedArticleId: number | null;
}
```

优点：

- 标准化
- 查找高效
- 增删改代码少
- selector 可复用性强

缺点：

- 初学时会觉得比数组多一层抽象
- 需要理解 `ids + entities` 结构

所以也可以这样记：


> 如果只是简单列表，数组就够。  
> 如果是“真正需要管理”的集合，Entity 往往更合适。

---

## Entity 和后端 API 的配合

在真实项目里，一个典型流程通常是：

1. 组件 dispatch `loadArticles`
2. Effect 调 API
3. API 返回文章数组
4. dispatch `loadArticlesSuccess({ articles })`
5. reducer 中用 `adapter.setAll(articles, state)`

例如：

```ts
loadArticles$ = createEffect(() =>
    this.actions$.pipe(
        ofType(loadArticles),
        exhaustMap(() =>
            this.articleService.getAll().pipe(
                map(articles => loadArticlesSuccess({ articles }))
            )
        )
    )
);
```

然后 reducer：

```ts
on(loadArticlesSuccess, (state, { articles }) =>
    adapter.setAll(articles, {
        ...state,
        loading: false
    })
)
```

这样整个列表管理流程会非常清晰：


- Effect 负责拿数据
- Entity 负责存集合
- Selector 负责读集合

---

## 一句话理解 Entity

如果看了很多代码还是有点绕，可以先只记住这句话：


> NgRx Entity = 用标准方式管理“按 id 组织的列表数据”。

它做的事情本质上就是：

- 帮你规范 state 结构
- 帮你减少 reducer 样板代码
- 帮你快速生成常用 selector
- 让列表数据管理更统一

---

## Entity 小结

Entity 里最重要的几个点可以总结为：


- `EntityState<T>`：标准集合状态结构
- `createEntityAdapter()`：创建集合适配器
- `adapter.getInitialState()`：生成初始状态
- `adapter.addOne / updateOne / removeOne / setAll`：简化 reducer
- `adapter.getSelectors()`：快速生成 selector

如果你项目里有大量“列表型业务状态”，那 Entity 基本是非常值得掌握的。

---

# 小结


到这里，NgRx 里几个常见的进阶主题基本都过了一遍：


- Store
- MetaReducer
- root state / feature state
- Selectors
- Effects
- Entity

如果把最开始的 Counter 示例看作“入门骨架”，那这些进阶内容就是把骨架往真实项目的方向继续搭起来。


最后再用一句话把它们串起来：


- **Store**：统一保存状态
- **Reducer**：根据 Action 计算新状态
- **Selector**：从状态中读取数据
- **Effect**：处理异步和副作用
- **Entity**：更高效地管理列表型数据

---

---

# Demo 3：Undo / Redo


Undo / Redo 这类场景很适合用来理解状态管理，因为它天然要求你保留历史状态、能够回退、也能够重做。  
如果只靠组件里的临时变量去拼，很快就会变得混乱；但如果状态变化是可追踪的，这类需求会清晰很多。

这一部分我准备单独再整理一个示例，放到后面继续补充。

# Reference

[NgRx](https://ngrx.io/docs)  
[Angular与NgRx状态管理: 最佳实践解析](https://www.jianshu.com/p/7a966d2e791d)  
[Level Up Your NgRx Skills With 10 Time-Tested Best Practices](https://angularexperts.io/blog/level-up-your-ng-rx-skills-with-10-time-tested-best-practices)  
[NgRx — Best Practices for Enterprise Angular Applications](https://wesleygrimes.com/angular/2018/05/30/ngrx-best-practices-for-enterprise-angular-applications)  
[Simplify State Management with NgRx in Angular | NgRx Guide](https://codezup.com/simplifying-state-management-ngrx-angular-guide/)   
[Angular Ngrx Undo Redo Demo](https://stackblitz.com/edit/angular-ngrx-undo-redo-demo?file=README.md)  

