import unicodedata

class Word(object):

  def __init__(self, word, bcpCode):
    self._word = word
    self._language = bcpCode

  def toLower(self):
      return self._word.lower()

class IrishWord(Word):

  def __init__(self, word, bcpCode, std=False):
    Word.__init__(self, word, bcpCode)
    self._standardIrishSpelling = std

  def specialCase(self):
    return ((self._word[0] in 'tn') and unicodedata.normalize('NFC', self._word)[1] in 'AEIOUÁÉÍÓÚ')

  def toLower(self):
    if len(self._word)>1:
        if (self.specialCase()):
          self._word = self._word[0]+'-'+self._word[1:]
    return self._word.lower()

  def isLenited(self):
    language = self._language
    if '-' in self._language:
      index = self._language.find('-')
      language = self._language[0:index]
    if language == 'ga' or language == 'gd':
      if len(self._word) < 2:
        return False
      else:
        return self._word[0].lower() in 'bcdfgmpst' and self._word[1].lower()=='h'
    else:
      raise InvalidMethodException('Method only available for Irish and Scottish Gaelic')

class GreekWord(Word):

  def __init__(self, word, bcpCode):
    Word.__init__(self, word, bcpCode)
    self._finalSigma = False

  def toLower(self):
    if self._word[-1]=='Σ':
        self._finalSigma = True
        self._word = self._word[:-1]+'ς'
    return self._word.lower()

class TurkishWord(Word):

  def __init__(self, word, bcpCode):
    Word.__init__(self, word, bcpCode)

  def toLower(self):
    self._word = self._word.replace('I','ı')
    return self._word.lower()

class AzerbaijaniWord(Word):

  def __init__(self, word, bcpCode):
    Word.__init__(self, word, bcpCode)

  def toLower(self):
    self._word = self._word.replace('I','ı')
    return self._word.lower()

class InvalidLanguageException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidMethodException(Exception):
    def __init__(self, message):            
        super().__init__(message)

class Language:

  def __init__(self, bcpCode):
    self._language = bcpCode
    self._skipLanguageList = ['zh', 'ja', 'th']

  def getLanguage(self):
    return self._language

  def getBaseLanguage(self):
    language = self._language
    if '-' in language:
      index = language.find('-')
      language = language[0:index]
    return language

  def isInvalidLanguage(self):
    baselanguage = self.getBaseLanguage()    
    return (len(baselanguage)<2 or len(baselanguage)>3)

  def languageCanBeIgnored(self):
      language = self.getBaseLanguage()
      return (language in self._skipLanguageList)

if __name__=='__main__':
  f = open('tests.tsv')
  for line in f:
    line = line.rstrip('\n')
    (word, bcpCode, result) = line.split('\t')
    
    language = Language(bcpCode)
    if (language.isInvalidLanguage()):
      raise InvalidLanguageException("Invalid BCP-47 code")

    baseLanguage = language.getBaseLanguage()
    if (language.languageCanBeIgnored()):
      answer = word.lower()
    elif baseLanguage=='ga':
      answer = IrishWord(word, baseLanguage).toLower()   
    elif baseLanguage=='tr':  
      answer = TurkishWord(word, baseLanguage).toLower()   
    elif baseLanguage=='az':
      answer = AzerbaijaniWord(word, baseLanguage).toLower()
    elif baseLanguage=='el':
      answer = GreekWord(word, baseLanguage).toLower()  
    else:
      answer = Word(word, baseLanguage).toLower()

    if answer != result:
      print('Test case failed. Expected', result, 'when lowercasing',word,'in language',baseLanguage,'but got',answer)
  f.close()