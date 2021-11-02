import unicodedata

class Word:

  def __init__(self, word, bcpCode, std=False):
    self._w = word
    self._l = bcpCode
    self._finalSigma = False
    self._standardIrishSpelling = std

  def setWord(self, w):
    self._w = w

  def getLang(self):
    if '-' in self._l:
      return self._l[0:self._l.find('-')]
    return self._l

  def irish(self):
    temp = self._w
    if len(self._w)>1:
      if (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
        temp = self._w[0]+'-'+temp[1:]
    return temp.lower()

  def turkish(self):
    temp = self._w
    temp = temp.replace('\u0049','\u0131')
    return temp.lower()

  def greek(self):
      temp = self._w
      if temp[-1]=='\u03a3':
        self._finalSigma = True
        temp = temp[:-1]+'\u03c2'
      return temp.lower()


  def azerbaijani(self):
    temp = self._w
    temp = temp.replace('\u0049','\u0131')
    return temp.lower()

  def noLower(self):
    return self._w

  def simpleLower(self):
    temp = self._w
    return temp.lower()


  def toLower(self):

    lan = self.getLang()
    lanDic = {"ga": self.irish(),
            "tr": self.azerbaijani(),
            "az": self.turkish(),
            "el": self.greek(),
            "zh": self.noLower(),
            "ja": self.noLower(),
            "th": self.noLower()}
    lower = lanDic.get(lan, self.simpleLower())
    return lower


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






