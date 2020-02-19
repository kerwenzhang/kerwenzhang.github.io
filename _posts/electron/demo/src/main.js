const electron = require("electron")
const path = require("path")
const url = require("url")
const countdown = require("./countdown")

const {app, BrowserWindow, ipcMain:ipc} = electron;

let win

app.on('ready', _=>{
    win = new BrowserWindow({
        width:700,
        height:500,
        resizable:false
    })

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }))

    win.setMenu(null)
    win.on('closed', ()=>{
        win = null
    })

    countdown(count => {
        console.log("in main.js " + count)
    })
})

ipc.on('start', _ =>{
    console.log("get message from render")
    win.webContents.send('Response', "message from main")
})

