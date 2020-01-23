const electon = require('electron')

const path = require('path')
const url = require('url')
const images = require('./images')
const {app, BrowserWindow, ipcMain: ipc} = electon
let mainWindow
app.on('ready', _ =>{
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 725,
        resizable: false
    })
    mainWindow.setMenu(null)

    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'capture.html'),
        protocol:'file',
        slashes: true
    }))

    mainWindow.webContents.openDevTools()

    images.mkdir(images.getPicturesDir(app))

    mainWindow.on('close', _ =>{
        mainWindow = null
    })
})

ipc.on('image-captured', (evt, contents) => {
    images.save(images.getPicturesDir(app), contents, (err, imgPath) => {
        images.cache(imgPath)
    })
})

ipc.on('image-remove',(evt, index) => {
    images.rm(index, _ => {
        evt.sender.send('image-removed', index)
    })
})