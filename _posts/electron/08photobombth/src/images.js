const path = require('path')
const fs = require('fs')

const logError = err => err && console.error(err)

let images = []

function FormatDateTime() {
    now = new Date();
    year = "" + now.getFullYear();
    month = "" + (now.getMonth() + 1); if (month.length == 1) { month = "0" + month; }
    day = "" + now.getDate(); if (day.length == 1) { day = "0" + day; }
    hour = "" + now.getHours(); if (hour.length == 1) { hour = "0" + hour; }
    minute = "" + now.getMinutes(); if (minute.length == 1) { minute = "0" + minute; }
    second = "" + now.getSeconds(); if (second.length == 1) { second = "0" + second; }
    return year + "-" + month + "-" + day + "-" + hour + "-" + minute + "-" + second;
  }


exports.save = (picturesPath, contents, done) => {
    const base64Data = contents.replace(/^data:image\/png;base64,/, '')
    const imgPath = path.join(picturesPath, FormatDateTime() +'.png')
    fs.writeFile(imgPath, base64Data, {encoding: 'base64'}, err => {
        if(err) return logError(err)

        done(null, imgPath)
    })
}

exports.getPicturesDir = app => {
    return path.join(app.getPath('pictures'), 'photobombth')
}

exports.mkdir = picturesPath => {
    fs.stat(picturesPath, (err, stats) => {
        if(err && err.code !== 'ENOENT')
            return logError(err)
        else if (err || !stats.isDirectory())
            fs.mkdir(picturesPath, logError)
    })
}

exports.rm = (index, done) => {
    fs.unlink(images[index], err => {
        if(err) return logError(err)

        images.splice(index, 1)
        done()
    })
}

exports.cache = imgPath => {
    images = images.concat([imgPath])
    return images
}

exports.getFromCache = index => {
    return images[index]
}