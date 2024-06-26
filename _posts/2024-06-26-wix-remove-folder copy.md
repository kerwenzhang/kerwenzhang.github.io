---                
layout: post                
title: "TransactionOption"                
date:   2024-6-26 20:30:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      
TransactionOption用于指定组件请求的自动事务类型。有以下5个选项:

| Option | Value | Description1 | Description2 | Description3 |
|----------|----------|----------|----------|----------|
| Disabled    | 0   | 忽略当前上下文中的任何事务。   |此类的实例将不参与事务，但可以共享其调用者的上下文，即使其调用者配置为 NotSupported、Supported、Required 或 RequiresNew。|
| NotSupported    | 1   | 使用非受控事务在上下文中创建组件。   | 此类的实例将不会参与事务，并且仅当其调用者也配置为 NotSupported 时才会共享其调用者的上下文。 |NotSupported 指示容器不启动事务，也不联接现有事务。 由父容器启动的事务不影响已经配置为不支持事务的子容器。 例如，如果包配置为启动事务，而包中的 For 循环容器使用 NotSupported 选项，则在 For 循环中的任务失败时不回滚任何任务。  |
| Supported    | 2   | 如果事务存在，则共享该事务。   | 如果存在，此类的实例将参与其调用者的交易。 |Supported 指示容器不启动事务，但将联接由其父容器启动的任何事务。 例如，如果具有四个执行 SQL 任务的包启动了一个事务，而且所有这四个任务都使用 Supported 选项，则在其中任何一个任务失败时都会回滚执行 SQL 任务所执行的数据库更新。 如果包没有启动事务，则四个执行 SQL 任务将不绑定到该事务，而且除了回滚失败的任务所执行的更新外，不回滚任何其他数据库更新。  | 
| Required    | 3   | 如果事务存在，则共享该事务；如有必要，则创建新事务。   | 如果存在，则该类的实例将参与其调用者的交易。如果不存在，则将为其创建一个新的交易。 |  Required 指示该容器启动一个事务，除非已经存在由其父容器启动的事务。 如果事务已经存在，容器将联接该事务。 例如，如果没有配置为支持事务的包包括一个使用 Required 选项的序列容器，则该序列容器会启动其自己的事务。 如果包已经配置为使用 Required 选项，则序列容器将联接包事务。|
| RequiresNew    | 4   | 使用新事务创建组件，而与当前上下文的状态无关。   | 总是会为该类的实例创建新的交易 |


# Reference
[TransactionOption Enum](https://learn.microsoft.com/en-us/dotnet/api/system.enterpriseservices.transactionoption?view=netframework-4.8.1)  
[Integration Services 事务](https://learn.microsoft.com/zh-cn/sql/integration-services/integration-services-transactions?view=sql-server-ver16)  