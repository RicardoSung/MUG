const { app } = require("electron")
const path = require('path')
var fs = require("fs")

let homeDir = path.dirname(app.getAppPath())

let settingJsonPath = homeDir + "/setting.json"

const defaultSetting = {};
//check if "setting.json" exists in the app path or create it.
function createAppSetting() {
    return new Promise((resolve, reject) => {
        fs.access(settingJsonPath, (err) => {
            if (err) {
                fs.appendFileSync(settingJsonPath, defaultSetting, 'utf-8', (err) => {
                    if (err) {
                        reject(false);
                    } else {
                        resolve(true);
                    }
                });
            } else {
                resolve(true);
            }
        })
    })
};

function jsonRead(fileDir, classname) {
    try {
        let jsonData = fs.readFile(fileDir, 'utf-8', (err, data) => { return data; });
        const jsonDataString = JSON.parse(jsonData.toString());
        return jsonDataString.classname;
    } catch (error) {
        console.log(error);
    }
}


function jsonModify(fileDir, classname, classdata) {
    try {
        let jsonData = fs.readFile(fileDir, 'utf-8', (err, data) => { return data; });
        var jsonDataString = JSON.parse(jsonData.toString());
        jsonDataString.classname = classdata;
        let jsonDataNew = JSON.stringify(jsonDataString, null, 2);
        fs.writeFile(fileDir, jsonDataNew, 'utf-8', (err) => {
            throw (err);
        });
    } catch (error) {
        console.log(error);
    }
}


export {createAppSetting, jsonRead, jsonModify};