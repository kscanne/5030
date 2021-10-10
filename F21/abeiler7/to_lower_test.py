import unittest
import pandas as pd
import to_lowercase as lc

class TestToLower(unittest.TestCase):
    def test_something(self):
        test_cases = pd.read_csv("./tests.tsv", sep='\t', header=None)
        for idx, row in test_cases.iterrows():
            self.assertEqual(lc.to_lower(row[0], row[1]), row[2])


if __name__ == '__main__':
    unittest.main()
