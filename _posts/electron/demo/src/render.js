const electron = require('electron')
const ipc = electron.ipcRenderer

document.getElementById('start').addEventListener('click', _=>{
    ipc.send('start')
})

ipc.on('Response',(evt, msg) =>{
    document.getElementById('msg').innerHTML = msg
})