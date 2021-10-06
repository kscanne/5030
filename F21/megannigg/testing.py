from lowercase import lowercase  

import csv
tests = []
with open("tests.tsv") as file:
    test_file = csv.reader(file, delimiter="\t")
    for line in test_file:
        tests.append(line)

for test in tests:
    result =  ' Expected: '+test[2]+' Actual: '+lowercase(test[0],test[1])
    if lowercase(test[0],test[1]) == test[2]:
        print('Passed!'+result)
    else:
        print('Failed.'+result)

