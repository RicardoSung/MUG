const {ipcRenderer} = require("electron")

let signin = document.getElementsByClassName("submit_btn")[0];
let withoutsign = document.getElementsByClassName("without_login")[0];

window.addEventListener('DOMContentLoaded', () => {
    signin.addEventListener("click",()=>{
        alert(document.getElementsByClassName("input_box")[0].value);
    });

    withoutsign.addEventListener("click",()=>{
        window.location.href='../workspace/workspace.html';
    });
})
