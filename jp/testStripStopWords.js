var stripFunction = require('./stripStopWords');

function runTests(){
	var passedTests=0;
	var failedTests=0;
	var testNumber=0;
	var fileSystem = require('fs');
	var testData = fileSystem.readFileSync('../tests/cases.tsv').toString().trim().split("\n");

	for(test in testData) {
    	testData[test] = testData[test].toString().split("\t");
    	if(runTest(testData[test],testNumber) == "Fail"){
    		failedTests++;
    	}
    	else if (runTest(testData[test],testNumber) == "Pass"){
    		passedTests++;
    	}
    	testNumber++;
	}

	console.log("Tests Passed: " + passedTests);
	console.log("Tests Failed: " + failedTests);
}

function runTest(testCase, testNumber){
	var output = stripFunction.strip_stopwords(testCase[0],testCase[1]);
	if (output != testCase[2]){
		console.log("Error for test " + testNumber + ": should have returned: " + testCase[2]);
		console.log("But instead returned: " + output);
		return "Fail";
	}
	else{
		return "Pass";
	}
}

runTests();