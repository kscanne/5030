import unicodedata

class Word(object):

  def __init__(self, word, bcpCode):
    self._word = word
    self._language = bcpCode
    self._finalSigma = False

  def performIrishCheck(self):
    return ((self._word[0]=='t' or self._word[0]=='n') and unicodedata.normalize('NFC', self._word)[1] in 'AEIOUÁÉÍÓÚ')

  def toLower(self):
      return self._word.lower()

class IrishWord(Word):

  def __init__(self, word, bcpCode, std=False):
    Word.__init__(self, word, bcpCode)
    self._standardIrishSpelling = std

  def toLower(self):
    if len(self._word)>1:
        if (self.performIrishCheck()):
          self._word = self._word[0]+'-'+self._word[1:]
    return self._word.lower()

  def isLenited(self):
    language = self._language
    if '-' in self._language:
      i = self._language.find('-')
      language = self._language[0:i]
    if language == 'ga' or language == 'gd':
      if len(self._word) < 2:
        return False
      else:
        return self._word[0].lower() in 'bcdfgmpst' and self._word[1].lower()=='h'
    else:
      raise NotImplementedError('Method only available for Irish and Scottish Gaelic')

class GreekWord(Word):

  def __init__(self, word, bcpCode):
    Word.__init__(self, word, bcpCode)

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
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

def isInvalidLanguage(language):
    return (len(language)<2 or len(language)>3)

def languageCanBeIgnored(language):
    return (language=='zh' or language=='ja' or language=='th')

if __name__=='__main__':
  f = open('tests.tsv')
  for line in f:
    line = line.rstrip('\n')
    (word, language, result) = line.split('\t')
    
    if '-' in language:
      index = language.find('-')
      language = language[0:index]
    if (isInvalidLanguage(language)):
      raise InvalidLanguageException("Invalid BCP-47 code", )

    if (languageCanBeIgnored(language)):
      answer = word
    elif language=='ga':
      answer = IrishWord(word, language).toLower()   
    elif language=='tr':  
      answer = TurkishWord(word, language).toLower()   
    elif language=='az':
      answer = AzerbaijaniWord(word, language).toLower()
    elif language=='el':
      answer = GreekWord(word, language).toLower()  
    else:
      answer = Word(word, language).toLower()

    if answer != result:
      print('Test case failed. Expected', result, 'when lowercasing',word,'in language',language,'but got',answer)
  f.close()