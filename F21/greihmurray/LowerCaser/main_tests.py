import unittest
import main

class TestLowerCase(unittest.TestCase):
    def testEnglish(self):
        self.assertTrue(main.lowercase('en', 'This'), 'this')
        self.assertTrue(main.lowercase('en', 'hElLO tHEre'), 'hello there')
        self.assertTrue(main.lowercase('en', 'HELLO'), 'hello')
        self.assertTrue(main.lowercase('en-US', 'WORLD'), 'world')
        self.assertTrue(main.lowercase('en-IE', 'cAmEl'), 'camel')
        self.assertTrue(main.lowercase('en-Latn', '--OK'), '--ok')
        self.assertTrue(main.lowercase('en', 'KASIM'), 'kasim')
    def testTurkish(self):
        self.assertTrue(main.lowercase('tr', 'KASIM'), 'kasım')
        self.assertTrue(main.lowercase('tr', 'MERHABA'), 'merhaba')
        self.assertTrue(main.lowercase('tr', 'ORADA'), 'orada')
        self.assertTrue(main.lowercase('tr', 'GENEL'), 'genel')
        self.assertTrue(main.lowercase('tr', 'KELIME'), 'kelıme')
    def testIrish(self):
        self.assertTrue(main.lowercase('ga', 'tAcht'), 't-acht')
        self.assertTrue(main.lowercase('ga', 'tACHt'), 't-acht')
        self.assertTrue(main.lowercase('ga', 'TACHT'), 't-acht')
        self.assertTrue(main.lowercase('ga', 'nAthair'), 'n-athair')
        self.assertTrue(main.lowercase('ga', 'nATHAIR'), 'n-athair')
        self.assertTrue(main.lowercase('ga', 'NATHAIR'), 'nathair')
        self.assertTrue(main.lowercase('ga-IE', 'nÓg'), 'n-óg')
        self.assertTrue(main.lowercase('ga-IE', 'nÕg'), 'nóg')
        self.assertTrue(main.lowercase('ga-IE', 'nÕg'), 'nóg')
    def testGreek(self):
        self.assertTrue(main.lowercase('el', 'ΠΟΛΗΣ'), 'πόλης')
        self.assertTrue(main.lowercase('el', 'ΓΕΙΑ ΣΑΣ'), 'γεια σας')
        self.assertTrue(main.lowercase('el', 'ΕΚΕΙ'), 'εκεί')
        self.assertTrue(main.lowercase('el', 'ΓΕΝΙΚΟΣ'), 'γενικός')
        self.assertTrue(main.lowercase('el', 'ΚΕΝΟΜΠΙ'), 'kenobi')
    def testChinese(self):
        self.assertTrue(main.lowercase('zh-HANS', '官话'), '官话')
        self.assertTrue(main.lowercase('zh', '你好'), '你好')
        self.assertTrue(main.lowercase('zh', '那裡'), '那裡')
        self.assertTrue(main.lowercase('zh-HANS', '一般的'), '一般的')
        self.assertTrue(main.lowercase('zh', '克諾比'), '克諾比')
    def testThai(self):
        self.assertTrue(main.lowercase('th', 'ภาษาไทย'), 'ภาษาไทย')
        self.assertTrue(main.lowercase('th', 'สวัสดี'), 'สวัสดี')
        self.assertTrue(main.lowercase('th', 'ที่นั่น'), 'ที่นั่น')
        self.assertTrue(main.lowercase('th', 'ทั่วไป'), 'ทั่วไป')
        self.assertTrue(main.lowercase('th', 'คำ'), 'คำ')
    def testJapanese(self):
        self.assertTrue(main.lowercase('ja', 'こんにちは'), 'こんにちは')
        self.assertTrue(main.lowercase('ja', 'そこの'), 'そこの')
        self.assertTrue(main.lowercase('ja', '全般的'), '全般的')
        self.assertTrue(main.lowercase('ja', 'ケノービ'), 'ケノービ')
        self.assertTrue(main.lowercase('ja', '言葉'), '言葉')
    def testAzerbaijani(self):
        self.assertTrue(main.lowercase('az', 'SALAM'), 'salam')
        self.assertTrue(main.lowercase('az', 'VAR'), 'var')
        self.assertTrue(main.lowercase('az', 'UMUMI'), 'umumı')
        self.assertTrue(main.lowercase('az', 'DUNYA'), 'dunya')
        self.assertTrue(main.lowercase('az', 'DEDI'), 'dedı')