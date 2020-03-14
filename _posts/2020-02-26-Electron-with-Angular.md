---                
layout: post                
title: "Electron with Angular" 
date:   2020-02-26 10:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      
If you have already have a web application(eg. Agnualr), this is how to integrate web application with Electron.  

## Create new Angular project  

1.	Create new folder “Angular” and open with VSCode  
2.	Open new terminal in VSCode and install the latest version of the Angular CLI globally:  

        npm i -g @angular/cli

3.	Navigate to your work folder and let’s create our new Angular app, called my-app:  

        ng new my-app
        cd my-app

4.	Run following command to start web service  

        npm start

5.	Open web browser and input http://localhost:4200/   
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/electron1.png?raw=true)

## Integrate with Electron

1.	Install latest electron  

        npm i -D electron@latest

Note: It may take 10+ minutes to install electron, depends on network performance.  
2.	Create new main.js file under my-app folder. This file will be the entry point for our Electron app and will contain the main API for the desktop app   

        const {app, BrowserWindow} =require("electron")
        const path = require("path")
        const url = require("url")

        let win;

        function CreateWindow(){
            win = new BrowserWindow({
                width: 800,
                height: 600
            })

            win.loadURL(
                url.format({
                    pathname: path.join(__dirname, '/dist/index.html'),
                    protocol: "file",
                    slashes: true
                })
            )

            win.setMenu(null)

            win.on("close", () => {
                win = null
            })
        }

        app.on("ready", CreateWindow);

        app.on("window-all-closed", () => {
            if(process.platform !== "darwin"){
                app.quit();
            }
        })

        app.on("activate", ()=> {
            if(win === null){
                CreateWindow();
            }
        })

3.	Modify package.json file, add electron main entry  

        "name": "my-app",
        "version": "0.0.0",
        "main": "main.js",

4.	Add new scripts  

        "scripts": {
            "electron": "ng build --base-href ./ && electron .",

5.	Modify angular.json file  

        "architect": {
                "build": {
                "builder": "@angular-devkit/build-angular:browser",
                "options": {
                    "outputPath": "dist",

6.	Running app  

        Npm run electron 
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/electron2.png?raw=true)

[reference](https://alligator.io/angular/electron/)