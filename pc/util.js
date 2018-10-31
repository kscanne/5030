var fs = require('fs');

exports.readTextFileToArray = function (path) {
    if (fs.existsSync(path)) {
        var buf = fs.readFileSync(path);
        return buf.toString().split("\n");
    }
    throw new Error("Not a valid language code");
}

exports.assertEquals = function (actualOutput, expectedOutput, successMsg, errorMsg) {
    if (actualOutput === expectedOutput) {
        // console.log(successMsg);
    } else {
        console.error(errorMsg)
    }
}