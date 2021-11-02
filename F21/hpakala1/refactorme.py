import unicodedata

class UniCodeCharacter:
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

class BaseClass(UniCodeCharacter):
    def __init__(self,word):
        self.word = word

class Word(BaseClass):

    def __init__(self, word, lang):
        self._word = word
        self._lang = lang

    def checkForLangCode(self):
        language = self._lang
        if '-' in self._lang:
            i = self._lang.find('-')
            language = self._lang[0:i]
        if language == "az" or language == "tr":
                language = "at"
        return language

    def processForIrishWords(self):
        irishWord = self._word
        if len(self._word)>1:
            if (self._word[0]=='t' or self._word[0]=='n') and unicodedata.normalize('NFC', self._word)[1] in self.STANDARD_VOWELS:
                irishWord = self._word[0]+'-'+irishWord[1:]
        return irishWord.lower()

    def processForTurkishWord(self):
        turkishWord = self._word
        turkishWord = turkishWord.replace(self.CAPITAL_I,self.DOTLESS_i)
        return turkishWord.lower()

    def processForGreekWord(self):
        greekWord = self._word
        if greekWord[-1]== self.CAPITAL_SIGMA:
            greekWord = greekWord[:-1]+ self.CAPITAL_SIGMA
        return greekWord.lower()

    def switcherProcess(self,language):
        
        switcher = {
            "ga": self.processForIrishWords(),
            "at": self.processForTurkishWord(),
            "el": self.processForGreekWord(),
        }

        ## switch with default value, default value is converting to 
        return switcher.get(language, self._word.lower())

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