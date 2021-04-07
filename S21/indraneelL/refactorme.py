import unicodedata

class BaseClass:
    CAPITAL_ACUTE_A = '\u00c1'
    CAPITAL_ACUTE_E = '\u00c9'
    CAPITAL_ACUTE_I = '\u00cd'
    CAPITAL_ACUTE_O = '\u00d3'
    CAPITAL_ACUTE_U = '\u00da'
    CAPITAL_I = '\u0049'
    DOTLESS_i = '\u0131'
    CAPITAL_SIGMA = '\u03a3'
    SMALL_SIGMA = '\u03c2'

    STANDARD_VOWELS = 'AEIOU' + CAPITAL_ACUTE_A + CAPITAL_ACUTE_E + CAPITAL_ACUTE_I + CAPITAL_ACUTE_O + CAPITAL_ACUTE_U

    def __init__(self,word):
        self.word = word

class CheckIrishWord(BaseClass):

    def process_word(self):
        temp = self.word
        if len(self.word)>1:
            if (self.word[0]=='t' or self.word[0]=='n') and unicodedata.normalize('NFC', self.word)[1] in self.STANDARD_VOWELS:
                temp = self.word[0]+'-'+temp[1:]
        return temp.lower()

class CheckTurkAndAzerWord(BaseClass):

    def process_word(self):
        temp = self.word
        temp = temp.replace(self.CAPITAL_I,self.DOTLESS_i)
        return temp.lower()

class CheckGreekWord(BaseClass):

    def process_word(self):
        temp = self.word
        if temp[-1]== self.CAPITAL_SIGMA:
            temp = temp[:-1]+ self.CAPITAL_SIGMA
        return temp.lower()

class Word:

    def __init__(self, word, lang):
        self._w = word
        self._l = lang

    def checkForLangCode(self):
        language = self._l
        if '-' in self._l:
            i = self._l.find('-')
            language = self._l[0:i]
        if language == "az" or language == "tr":
                language = "at"
        return language

    def switcherProcess(self,language):
        
        switcher = {
            "ga": CheckIrishWord(self._w).process_word(),
            "at": CheckTurkAndAzerWord(self._w).process_word(),
            "el": CheckGreekWord(self._w).process_word(),
        }

        return switcher.get(language, self._w.lower())

    def toLower(self):
        
        language = self.checkForLangCode()
        assert(len(language)==2 or len(language)==3), "Invalid BCP-47 code"
        return self.switcherProcess(language)

    def checkThePieces(self, answer, pieces):
        return answer != pieces[2]
    
if __name__=='__main__':
  f = open("tests.tsv",encoding="utf8")
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if w.checkThePieces(answer, pieces):
      raise Exception('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()