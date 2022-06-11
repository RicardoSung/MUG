const { dialog } = require('electron')

// class file_op{

//     constructor(){

//     }


function   file_open(){
    dialog.showOpenDialog(
        {
            properties: ['openFile'],
            title: 'Select a file or files...',
            filters: [
                { name: 'Images', extensions: ['jpg', 'png'] },
                { name: 'Movies', extensions: ['mp4', 'avi'] },
                { name: 'All Files', extensions: ['*'] }
            ]
        }
    ).then(result => {
        if (result.canceled) {
            console.log('Dialog was canceled')
        } else {
            const file = result.filePaths[0]
        }
    }
    )}
// }

module.exports = file_open;