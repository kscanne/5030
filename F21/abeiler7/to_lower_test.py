import unittest
import pandas as pd
import to_lowercase as lc

class TestToLower(unittest.TestCase):
    global test_cases;
    test_cases = pd.read_csv("./F21/abeiler7/tests.tsv", sep='\t', header=None)

    def test_something(self):
        for idx, row in test_cases.iterrows():
            #print(row[0])
            self.assertEqual(lc.to_lower(row[0]), row[2]) # add assertion here


if __name__ == '__main__':
    unittest.main()
