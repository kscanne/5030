import unicodedata

class Word:

    def __init__(self, word, language):
        self._word = word
        self._lang = language

    def parseLanguage(self):

        if (len(self._lang)>2 and self._lang[2]!='-') or len(self._lang)<2:
            print("Incorrect language code")
            return ''

        return self._lang[0:2]

    def setWord(self, w):
        self._word = w

    def irish(self):
        word = self._word
        if len(self._word)>1 and (self._word[0]=='t' or self._word[0]=='n') and unicodedata.normalize('NFC', self._word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
            word = self._word[0]+'-'+word[1:]
        return word.lower()

    def turkishOrAzerbaijani(self):
        return self._word.replace('\u0049','\u0131').lower()

    def greek(self):
        word = self._word[:-1]+'\u03c2' if self._word[-1]=='\u03a3' else self._word
        return word.lower()

    def toLowerUtil(self, language):
        select = {
            "ga": self.irish(),
            "tr": self.turkishOrAzerbaijani(),
            "az": self.turkishOrAzerbaijani(),
            "el": self.greek(),
            "zh": self._word,
            "ja": self._word,
            "th": self._word
        }

        return select.get(language, self._word.lower())

    def toLower(self):
        language = self.parseLanguage()
        if len(language)==0:
            return ''
        return self.toLowerUtil(language)

if __name__=='__main__':
    f = open('tests.tsv')
    for s in f:
        s = s.rstrip('\n')
        words = s.split('\t')
        w = Word(words[0], words[1])
        answer = w.toLower()
        if answer != words[2]:
            print("Test failed for Input:", words[0], "language:", words[1], "Expected:", words[2], "result:", answer)
    f.close()