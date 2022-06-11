const { Menu, dialog } = require('electron')

const file_open = require('./File_Op.js') 

// import {file_open} from "./File_Op.js"

var template = [
    {
        label: 'File',
        submenu: [
            { label: 'New Database' },
            { label: 'New Group' },
            { label: 'New Item' },
            {
                label: 'Open Database'
            },
            { label: 'Open Group' },
            { label: 'Open Item', 
            //When click "Open Item" in "File" Menu, pop up a file select window.
                click: async()=>{file_open()}
            },
            { label: 'Export ...' },
            { label: 'Exit' },
            { label: 'Preference' },
        ]
    },
    {
        label: 'Edit',
        submenu: [
            { label: 'Undo' },
            { label: 'Redo' },
            { label: 'Cut' },
            { label: 'Copy' },
            { label: 'Paste' },
            { label: 'Delete' },
            { label: 'Select All' },
            { label: 'Search' },
            { label: 'Advanced Search' },
        ]
    }
]

var m = Menu.buildFromTemplate(template)

Menu.setApplicationMenu(m)
