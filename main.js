const { app, BrowserWindow, ipcMain } = require('electron')


app.on('ready',()=>{
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration:true,
            contextIsolation:false
        }
    })
    win.loadFile('./pages/login/login.html')
    ipcMain.on("message",(event, arg)=>{
        console.log(arg)
        event.sender.send('reply',"now from main") 
    })
})