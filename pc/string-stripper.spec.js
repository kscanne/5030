var stringStripper = require('./string-stripper.js');
var util = require('./util.js');

var runTests = function (testFilePath) {
    var testCases = util.readTextFileToArray(testFilePath);

    testCases.forEach(function (testCase, index) {
        var [languageCode, input, expectedOutput] = util.extractTestCase(testCase);
        var actualOutput = stringStripper.stripStopWords(languageCode, input);
        
        util.assertEquals(
            actualOutput,
            expectedOutput,
            `Test ${index + 1} passed.`,
            `Test ${index+1} failed. Expected '${expectedOutput}' but got '${actualOutput}'.`
        );
    });
}

runTests('../tests/cases.tsv');