#Testing for makeLower function

from lower import makeLower

import csv
tests = []
with open("tests.tsv") as file:
        test_file = csv.reader(file, delimiter="\t")
        for line in test_file:
                tests.append(line)
for test in tests:
        expected = test[2]
        actual = makeLower(test[0], test[1])
        if actual == expected:
                print("Pass", "  Expected:", expected, "  Actual:", actual)
        else:
                print("Fail", "  Expected:", expected, "  Actual:", actual)
