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
        self.assert_(main.lowercase('en', 'KASIM'), 'kasim')
    def testTurkish(self):
        self.assert_(main.lowercase('tr', 'KASIM'), 'kasım')
    def testIrish(self):
        self.assert_(main.lowercase('ga', 'tAcht'), 't-acht')
        self.assert_(main.lowercase('ga', 'tACHt'), 't-acht')
        self.assert_(main.lowercase('ga', 'TACHT'), 't-acht')
        self.assert_(main.lowercase('ga', 'nAthair'), 'n-athair')
        self.assert_(main.lowercase('ga', 'nATHAIR'), 'n-athair')
        self.assert_(main.lowercase('ga', 'NATHAIR'), 'nathair')
        self.assert_(main.lowercase('ga-IE', 'nÓg'), 'n-óg')
        self.assert_(main.lowercase('ga-IE', 'nÕg'), 'nóg') #FAILED
        self.assert_(main.lowercase('ga-IE', 'nÕg'), 'nóg') #FAILED
    def testGreek(self):
        self.assert_(main.lowercase('el', 'ΠΟΛΗΣ'), 'πόλης')
    def testChinese(self):
        self.assert_(main.lowercase('zh-HANS', '官话'), '官话')
    def testThai(self):
        self.assert_(main.lowercase('th', 'ภาษาไทย'), 'ภาษาไทย')