import unicodedata

class Word:

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

  def setWord(self, w):
    self._w = w

  def getLang(self):
    if '-' in self._l:
      return self._l[0:self._l.find('-')]
    return self._l

  def toLower(self):
    language = self._l
    if '-' in self._l:
      i = self._l.find('-')
      language = self._l[0:i]
    if len(language)<2 or len(language)>3:
      print("Invalid BCP-47 code")
      return ''
    temp = self._w
    if language=='zh':
      return temp
    elif language=='ja':
      return temp
    elif language=='ga':
      if len(self._w)>1:
        if (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          temp = self._w[0]+'-'+temp[1:]
      return temp.lower()
    elif language=='tr':
      temp = self._w
      temp = temp.replace('\u0049','\u0131')
      return temp.lower()
    elif language=='az':
      temp = self._w
      temp = temp.replace('\u0049','\u0131')
      return temp.lower()
    elif language=='th':
      return temp
    elif language=='el':
      if temp[-1]=='\u03a3':
        self._finalSigma = True
        temp = temp[:-1]+'\u03c2'
      return temp.lower()
    elif False and language=='gd':
      # specification doesn't ask for this language to be treated differently
      # so this will never be called
      if len(self._w)>1:
        if (self._w[0]=='t' or self._w[0]=='n') and self._w[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          temp = self._w[0]+'-'+temp[1:]
      return temp.lower()
    else:
      return temp.lower()

  def isLenited(self):
    language = self._l
    if '-' in self._l:
      i = self._l.find('-')
      language = self._l[0:i]
    if language == 'ga' or language == 'gd':
      if len(self._w) < 2:
        return False
      else:
        return self._w[0].lower() in 'bcdfgmpst' and self._w[1].lower()=='h'
    else:
      raise NotImplementedError('Method only available for Irish and Scottish Gaelic')

if __name__=='__main__':
  f = open('tests.tsv', encoding='utf-8')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
