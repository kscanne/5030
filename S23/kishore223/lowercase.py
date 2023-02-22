import unittest

def lowercase_word(word, lang):
    if lang in ['tr', 'az']:
        return word.replace('I', 'ı').lower()
    elif lang == 'ga':
        vowels = set(['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'])
        for i in range(1, len(word)):
            if word[i-1] in ['n', 't'] and word[i] in vowels and word[i].isupper():
                return word[:i] + '-' + word[i:].lower()
        return word.lower()
    elif lang == 'el':
        if word.endswith('Σ'):
            return word[:-1] + 'ς'
        else:
            return word.lower()
    elif lang in ['zh', 'ja', 'th']:
        return word
    else:
        return word.lower()

word = input("Enter a word: ")
print("1.Type 'tr' for Turkish Language")
print("2.Type 'az' for Azerbaijani Language")
print("3.Type 'ga' for Irish Language")
print("4.Type 'zh' for Chinese Language(no changes)")
print("5.Type 'ja' for Japanese Language(no changes)")
print("6.Type 'th' for Thai Language(no changes)")
print("****** Note: If you type any other word, it will be just converted to lowercase. ******")

lang = input("Enter language code (BCP-47): ")

lowercased_word = lowercase_word(word, lang)
print(lowercased_word)

class TestLowercaseWord(unittest.TestCase):
    def test_turkish_lowercases_word(self):
        word = "IPHONE"
        lang = "tr"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "ıphone")
        
    def test_azerbaijani_lowercases_word(self):
        word = "MINI"
        lang = "az"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "mını")
        
    def test_irish_adds_hyphen_to_vowels(self):
        word = "tAcht"
        lang = "ga"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "t-acht")
        
    def test_chinese_does_not_change_word(self):
        word = "你好"
        lang = "zh"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "你好")
        
    def test_japanese_does_not_change_word(self):
        word = "こんにちは"
        lang = "ja"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "こんにちは")
        
    def test_thai_does_not_change_word(self):
        word = "สวัสดี"
        lang = "th"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "สวัสดี")
        
    def test_unsupported_language_lowercases_word(self):
        word = "Macbook"
        lang = "fr"
        result = lowercase_word(word, lang)
        self.assertEqual(result, "macbook")
        
if __name__ == '__main__':
    unittest.main()