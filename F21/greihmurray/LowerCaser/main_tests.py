import unittest
import main

class TestLowerCase(unittest.TestCase):
    def testEnglish(self):
        self.assert_(main.lowercase('en', 'This'), 'this')
        self.assert_(main.lowercase('en', 'hElLO tHEre'), 'hello there')
        self.assert_(main.lowercase('en', 'HELLO'), 'hello')
        self.assert_(main.lowercase('en-US', 'WORLD'), 'world')
        self.assert_(main.lowercase('en-IE', 'cAmEl'), 'camel')
        self.assert_(main.lowercase('en-Latn', '--OK'), '--ok')