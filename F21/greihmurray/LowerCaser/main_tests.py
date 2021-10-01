import unittest
import main

class TestLowerCase(unittest.TestCase):
    def testEnglish(self):
        self.assert_(main.lowercase('en', 'This'), 'this')
        self.assert_(main.lowercase('en', 'hElLO tHEre'), 'hello there')