import unicodedata

class Word:

  def __init__(self, word, bcpCode):
    self._word = word
    self._lang = Language(bcpCode).getLanguage()
    self._langType = Language(bcpCode).getLanguageType()

  def setWord(self, word):
    self._word = word

  def toLower(self):
    language = self._lang
    languageType = self._langType
    temp = self._word

    if languageType == "asian":
      return AsianWord(temp, language).toLower()
    elif languageType == "gaelic":
      return GaelicWord(temp, language).toLower()
    elif languageType == "greek":
      return GreekWord(temp, language).toLower()
    elif languageType == "turkic":
      return TurkicWord(temp, language).toLower()

    return temp.lower()


class AsianWord(Word):
  def toLower(self):
    return self._word


class GaelicWord(Word):
  def __init__(self, word, bcpCode, std=False):
      super().__init__(word, bcpCode)
      self._standardIrishSpelling = std

  def toLower(self):
    temp = self._word
    gaelicVowels = 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da'
    beginningTN = 'tn'

    if self._lang =='ga':
      if len(self._word)>1:
        if (self._word[0] in beginningTN) and (unicodedata.normalize('NFC', self._word)[1] in gaelicVowels):
          temp = self._word[0]+'-'+temp[1:]
      return temp.lower()

  def isLenited(self):
    gaelicConsonants = 'bcdfgmpst'
    h = 'h'

    if len(self._word) < 2:
      return False
    else:
      return self._word[0].lower() in gaelicConsonants and self._word[1].lower() == h


class GreekWord(Word):
  def __init__(self, word, bcpCode, std=False):
      super().__init__(word, bcpCode, std=std)
      self._finalSigma = False

  def toLower(self):
    temp = self._word
    capitalSigma = '\u03a3'
    endingSigma = '\u03c2'


    if temp[-1] == capitalSigma:
      self._finalSigma = True
      temp = temp[:-1] + endingSigma
    return temp.lower()  

class TurkicWord(Word):
  def toLower(self):
    capitalI = '\u0049'
    dotlessI = '\u0131'
    temp = self._word
    temp = temp.replace(capitalI, dotlessI)
    return temp.lower()


class Language:
  def __init__(self, bcpCode):
    self._lang = bcpCode
    self.setLanguage(bcpCode)

    self._langType = "default"
    self.setLanguageType()
  
  def setLanguage(self, bcpCode):
    temp = bcpCode
    if '-' in bcpCode:
      i = bcpCode.find('-')
      temp = bcpCode[0:i]
    if len(temp)<2 or len(temp)>3:
      raise ValueError("Invalid BCP-47 code")
    self._lang = temp
  
  def getLanguage(self):
    return self._lang

  def setLanguageType(self):
    if self._lang == "zh" or self._lang == "ja" or self._lang == "th":
      self._langType = "asian"
    elif self._lang == "ga" or self._lang == "gd":
      self._langType = "gaelic"
    elif self._lang == "el":
      self._langType == "greek"
    elif self._lang == "az" or self._lang == "tr":
      self._langType = "turkic"
    else:
      self._langType = "default"

  def getLanguageType(self):
    return self._langType


if __name__=='__main__':
  f = open('tests.tsv',encoding='utf-8')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
