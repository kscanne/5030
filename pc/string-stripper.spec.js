var stringStripper = require('./string-stripper.js');
var util = require('./util.js');

var extractTestCase = function (testCase) {
    var test = testCase.trim().split('\t');
    languageCode = (test[0] || "").trim();
    input = (test[1] || "").trim();
    expectedOutput = (test[2] || "").trim();
    return [languageCode, input, expectedOutput];
}

var runTests = function (testFilePath) {
    var testCases = util.readTextFileToArray(testFilePath);
    var passCount = 0;
    var failCount = 0;

    testCases.forEach(function (testCase, index) {
        var [languageCode, input, expectedOutput] = extractTestCase(testCase);
        var actualOutput = stringStripper.stripStopWords(languageCode, input);
        
        result = util.assertEquals(
            actualOutput,
            expectedOutput,
            `Test ${index + 1} passed.`,
            `Test ${index+1} failed. Expected '${expectedOutput}' but got '${actualOutput}'.`
        );
        if (result) {
            passCount++;
        } else {
            failCount++;
        }
    });
    console.log(`\n[=====> Pass ${passCount} tests.\n[=====> Fail ${failCount} tests.`)
}

runTests('../tests/cases.tsv');