const {Menu} = require('electron')

var template=[
    {
        label:'File',
        submenu:[
            {label:'New Database'},
            {label:'New Group'},
            {label:'New Item'},
            {label:'Open Database'},
            {label:'Open Group'},
            {label:'Open Item'},
            {label:'Export ...'},
            {label:'Exit'},
            {label:'Preference'},
        ]
    },
    {
        label:'Edit'
    }
]