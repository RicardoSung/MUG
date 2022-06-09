const { app, BrowserWindow, Notification  } = require('electron')

const path = require('path')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        //   webPreferences: {
        //     preload: path.join(__dirname, 'preload.js')
        //   }
    })

    win.loadFile('index.html')
}


const NOTIFICATION_TITLE = 'Basic Notification'
const NOTIFICATION_BODY = 'Notification from the Main process'

function showNotification() {
    new Notification({ title: NOTIFICATION_TITLE, body: NOTIFICATION_BODY }).show()
}

// app.whenReady().then(createWindow).then(showNotification)


/******
Create a Window for Windows
******/
// app.whenReady().then(() => {
//     createWindow()
//   })


/******
Create a Window for MacOS and Windows
******/
app.whenReady().then(() => {
    createWindow()
    showNotification()
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})


