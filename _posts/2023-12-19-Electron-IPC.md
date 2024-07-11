---      
layout: post      
title: "Electron IPC"      
date:   2023-12-19 10:59:00       
categories: "Electron"      
catalog: true      
tags:       
    - Electron      
---      
      
进程间通信 Inter-process communication (IPC)是在 Electron 中构建功能丰富的桌面应用程序的关键部分之一。Electron 的主进程和渲染进程有着清楚的分工并且不可互换。 这代表着无论是从渲染进程直接访问 Node.js 接口，亦或者是从主进程访问 HTML 文档对象模型 (DOM)，都是不可能的。  

解决这一问题的方法是使用进程间通信 (IPC)。进程使用 ipcMain 和 ipcRenderer 模块，通过开发人员定义的“通道”传递消息来进行通信。 这些通道是 任意 （您可以随意命名它们）和 双向 （您可以在两个模块中使用相同的通道名称）的。  

# 模式 1：渲染器进程到主进程（单向）
要将单向 IPC 消息从渲染器进程发送到主进程，您可以使用 `ipcRenderer.send` API 发送消息，然后使用 `ipcMain.on` API 接收。  

通常使用此模式**从 Web 内容调用主进程 API**。  
main.js  
创建一个监听器, 每当消息通过 set-title 通道传入时，找到附加到消息发送方的 `BrowserWindow` 实例，并在该实例上使用 `win.setTitle` API。  

    function createWindow () {
        const mainWindow = new BrowserWindow({
            webPreferences: {
                preload: path.join(__dirname, 'preload.js')
            }
        })

        ipcMain.on('set-title', (event, title) => {
            const webContents = event.sender
            const win = BrowserWindow.fromWebContents(webContents)
            win.setTitle(title)
        })

        mainWindow.loadFile('index.html')
    }

preload.js  
使用 ipcRenderer.send API将消息发送到main的监听器。  

    const { contextBridge, ipcRenderer } = require('electron/renderer')

    contextBridge.exposeInMainWorld('electronAPI', {
        setTitle: (title) => ipcRenderer.send('set-title', title)
    })

index.html  
添加一个由文本输入框和按钮  

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
            <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">
            <title>Hello World!</title>
        </head>
        <body>
            Title: <input id="title"/>
            <button id="btn" type="button">Set</button>
            <script src="./renderer.js"></script>
        </body>
    </html>

renderer.js  
在renderer.js 文件中添加几行代码，以利用从预加载脚本中暴露的 window.electronAPI 功能  

    const setButton = document.getElementById('btn')
    const titleInput = document.getElementById('title')
    setButton.addEventListener('click', () => {
        const title = titleInput.value
        window.electronAPI.setTitle(title)
    })

# 模式 2：渲染器进程到主进程（双向）
双向 IPC 的一个常见应用是从渲染器进程代码调用主进程模块并等待结果。这可以通过将 `ipcRenderer.invoke` 与 `ipcMain.handle` 搭配使用来完成。  
main.js  
使用 `ipcMain.handle` 监听事件  

    async function handleFileOpen () {
        const { canceled, filePaths } = await dialog.showOpenDialog({})
        if (!canceled) {
            return filePaths[0]
        }
    }

    app.whenReady().then(() => {
        ipcMain.handle('dialog:openFile', handleFileOpen)
        createWindow()
    })

preload.js  
使用`ipcRenderer.invoke`调用main里的监听器，并返回值

    const { contextBridge, ipcRenderer } = require('electron')

    contextBridge.exposeInMainWorld('electronAPI', {
        openFile: () => ipcRenderer.invoke('dialog:openFile')
    })

index.html  
用户界面包含一个 #btn 按钮元素，将用于触发我们的预加载 API，以及一个 #filePath 元素，将用于显示所选文件的路径。  

    <html>
        ...
        <body>
            <button type="button" id="btn">Open a File</button>
            File path: <strong id="filePath"></strong>
            <script src='./renderer.js'></script>
        </body>
    </html>

renderer.js  
监听 #btn 按钮的点击，并调用 `window.electronAPI.openFile()` API 来激活原生的打开文件对话框。 然后我们在 #filePath 元素中显示选中文件的路径。  

    const btn = document.getElementById('btn')
    const filePathElement = document.getElementById('filePath')

    btn.addEventListener('click', async () => {
        const filePath = await window.electronAPI.openFile()
        filePathElement.innerText = filePath
    })

# 模式 3：主进程到渲染器进程
将消息从主进程发送到渲染器进程时，需要指定是哪一个渲染器接收消息。 消息需要通过其 WebContents 实例发送到渲染器进程。 此 WebContents 实例包含一个 send 方法，其使用方式与 ipcRenderer.send 相同。  

main.js  
首先使用 Electron 的 Menu 模块在主进程中构建一个自定义菜单，该模块使用 `webContents.send` API 将 IPC 消息通过 update-counter 通道从主进程发送到目标渲染器。  

    const { app, BrowserWindow, Menu, ipcMain } = require('electron')
    const path = require('node:path')

    function createWindow () {
        const mainWindow = new BrowserWindow({
            webPreferences: {
            preload: path.join(__dirname, 'preload.js')
            }
        })

        const menu = Menu.buildFromTemplate([
            {
            label: app.name,
            submenu: [
                {
                click: () => mainWindow.webContents.send('update-counter', 1),
                label: 'Increment'
                },
                {
                click: () => mainWindow.webContents.send('update-counter', -1),
                label: 'Decrement'
                }
            ]
            }
        ])
        Menu.setApplicationMenu(menu)

        mainWindow.loadFile('index.html')
    }
    // ...

preload.js  
使用预加载脚本中的 contextBridge 和 ipcRenderer 模块向渲染器进程暴露 IPC 功能  

    const { contextBridge, ipcRenderer } = require('electron')

    contextBridge.exposeInMainWorld('electronAPI', {
        onUpdateCounter: (callback) => ipcRenderer.on('update-counter', (_event, value) => callback(value))
    })

加载预加载脚本后，渲染器进程应有权访问 window.electronAPI.onUpdateCounter() 监听器函数。  

index.html  

    <body>
        Current value: <strong id="counter">0</strong>
        <script src="./renderer.js"></script>
    </body>

renderer.js    
将回调传递给从preload脚本中暴露的 window.electronAPI.onUpdateCounter 函数。   

    const counter = document.getElementById('counter')

    window.electronAPI.onUpdateCounter((value) => {
        const oldValue = Number(counter.innerText)
        const newValue = oldValue + value
        counter.innerText = newValue.toString()
    })

# 模式 4：渲染器进程到渲染器进程
没有直接的方法可以使用 ipcMain 和 ipcRenderer 模块在 Electron 中的渲染器进程之间发送消息。 为此，您有两种选择：  

- 将主进程作为渲染器之间的消息代理。 这需要将消息从一个渲染器发送到主进程，然后主进程将消息转发到另一个渲染器。  
- 从主进程将一个 MessagePort 传递到两个渲染器。 这将允许在初始设置后渲染器之间直接进行通信。
# Reference
[Inter-Process Communication](https://www.electronjs.org/docs/latest/tutorial/ipc)    
[ipcMain](https://www.electronjs.org/docs/latest/api/ipc-main)  