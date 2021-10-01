import unicodedata


class Word:

  exceptionLanguages = ['tr', 'az', 'ga', 'el']
  unchangedLanguages = ['ja', 'zh', 'th']

  def __init__(self, word, bcp):
    self.word = word
    self.language = bcp
    # self._standardIrishSpelling = std

  def setWord(self, w):
    self.word = w

  def toLowercase(self):
    language = self.getLanguageFromBcp()
    self.checkInvalidBcp(language)
    tmp = self.word
    if language in self.unchangedLanguages:
        return tmp
    elif language in self.exceptionLanguages:
        if language == 'ga':
            if len(self.word) > 1:
                if (self.word[0] == 't' or self.word[0] == 'n') and unicodedata.normalize('NFC', self.word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
                    tmp = self.word[0]+'-'+tmp[1:]
        elif language == 'tr':
            tmp = self.word
            tmp = tmp.replace('\u0049', '\u0131')
        elif language=='az':
            tmp = self.word
            tmp = tmp.replace('\u0049','\u0131')
        elif language=='el':
            if tmp[-1]=='\u03a3':
                #self._finalSigma = True
                tmp = tmp[:-1]+'\u03c2'
    return tmp.lower()

  def getLanguageFromBcp(self):
      language = self.language
      if '-' in self.language:
            i = self.language.find('-')
            language = self.language[0:i]
      return language

  def checkInvalidBcp(self, language):
      if len(language) < 2 or len(language) > 3:
        print("Invalid BCP-47 code: ", language)
        raise ValueError('Invalid Bcp Code')

