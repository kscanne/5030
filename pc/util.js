var fs = require('fs');

exports.readTextFileToArray = function (path) {
    if (fs.existsSync(path)) {
        var buf = fs.readFileSync(path);
        return buf.toString().split("\n");
    }
    console.error('File not found');
    return [];
}

exports.extractTestCase = function (testCase) {
    var test = testCase.split('\t');
    languageCode = test[0] || "";
    input = test[1] || "";
    expectedOutput = test[2] || "";
    return [languageCode, input, expectedOutput];
}

exports.assertEquals = function (actualOutput, expectedOutput, successMsg, errorMsg) {
    if (actualOutput === expectedOutput) {
        console.log(successMsg);
    } else {
        console.error(errorMsg)
    }
}