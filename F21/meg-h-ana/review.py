import unicodedata
import csv

class WordConverter:

    def __init__(self, w, l):
        self._w = w
        self._l = l

    def toIrish(self):
        w = self._w
        if len(self._w)>1:
            if (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
                w = self._w[0]+'-'+w[1:]
        return w

    def toTurkish(self):
        w = self._w.replace('\u0049','\u0131')
        return w

    def toAzerbaijani(self):
        w = self._w.replace('\u0049','\u0131')
        return w

    def toGreek(self):
        w = self._w[:-1]+'\u03c2' if self._w[-1]=='\u03a3' else self._w
        return w

    def toLowerUtil(self, l):
        choose = {
            "zh": self._w,
            "ja": self._w,
            "th": self._w,
            "el": self.toGreek().lower(),
            "tr": self.toTurkish().lower(),
            "ga": self.toIrish().lower(),
            "az": self.toAzerbaijani().lower()
        }

        return choose.get(l, self._w.lower())


class Word:

    def __init__(self, w, l):
        self._w = w
        self._lang = l
        self.wc = WordConverter(w, l)

    def parseLanguage(self):

        if (len(self._lang)>2 and self._lang[2]!='-') or len(self._lang)<2:
            print("Incorrect language code")
            return ''

        return self._lang[0:2]

    def lowercase(self):
        language = self.parseLanguage()
        if len(language)==0:
            return ''
        return self.wc.toLowerUtil(language)

if __name__=='__main__':
    with open("tests.tsv") as file:
        test_file = csv.reader(file, delimiter="\t")
        for test in test_file:
            w = Word(test[0], test[1])
            actual = w.lowercase()
            if actual != test[2]:
                print("Tests Failed!!")
                print("Input:",test[0],"Language:",test[1])
                print("Expected:",test[2],"Fount:",actual)