# 3/11/2021 - Garrett Reed - Initial Creation - Alpha#
# Test will load test words and the expected results version will be console-only #
# Instructions: Go into garrett_lowercaser and comment out the last line before running this test code

import _csv
import garrett_lowercaser


# Pass test data into program one line at a time
def testRunner():

    with open("tests.tsv", encoding='utf-8') as test_file:
        rd = _csv.reader(test_file, delimiter="\t")
        for row in rd:
            word = row[0]
            lang = row[1]
            answer = row[2]
            match = garrett_lowercaser.langEntry2(lang)     # Uses the non-console language entry
            result = (garrett_lowercaser.wordProcess(match, word))   # Uses the test path
            if answer != result:
                print('Error - Expected "' + answer + '"')




# Run Code
testRunner()




