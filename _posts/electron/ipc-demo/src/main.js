console.log("main");

const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require("path");
const url=require("url");
const countdown = require('./countdown')
const ipc = electron.ipcMain

let mainWindow

app.on('ready', _ =>{
    mainWindow = new BrowserWindow({
        height:400,
        width:400,
        webPreferences:{
            nodeIntegration:true
        }
    })


    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname,'countdown.html'),
        protocol:'file',
        slashes:true
    }))


    mainWindow.on('closed',_=>{
        console.log('closed!')
        mainWindow=null
    })
})

ipc.on('countdown-start', _ =>{
    countdown(count => {
        mainWindow.webContents.send('countdown',count)
    })
})