import unicodedata

class Lang:
  def __init__(self):
    self._langCode = ''

  def getLang(self, givenLang):
    language = givenLang.split('-')[0]
    if len(language) < 2 or len(language) > 3:
      print("Invalid BCP-47 code")
    else:
      self._langCode = language

class Word:
  def __init__(self, word, bcpCode):
    self._word = word
    self._lang = bcpCode

  def toLower(self):
    # \u00c1 = A with Acute
    # \u00c9 = E with Acute
    # \u00cd = I with Acute
    # \u00d3 = O with Acute
    # \u00da = U with Acute
    # \u0131 = i with not dot
    # \u0370 = sigma
    # \u03a3 = lower ending sigma

    language = Lang()
    language.getLang(self._lang)
    if not language._langCode:
      return ''
    temp = self._word
    noChange = ['zh', 'ja', 'th']
    if language in noChange:
      return temp
    elif language=='ga':
      if len(self._word)>1:
        if (self._word[0]=='t' or self._word[0]=='n') and unicodedata.normalize('NFC', self._word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          temp = self._word[0]+'-'+temp[1:]
      return temp.lower()
    elif language=='tr' or language=='az':
      temp = self._word
      temp = temp.replace('\u0049','\u0131')
      return temp.lower()
    elif language=='el':
      if temp[-1]=='\u03a3':
        temp = temp[:-1]+'\u03c2'
      return temp.lower()
    else:
      return temp.lower()


if __name__=='__main__':
  f = open('tests.tsv')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
