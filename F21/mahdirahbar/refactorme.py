import unicodedata
import re

class Word:

  def __init__(self, word, language, std=False):
    self._w = word
    self.language = language
    self._lang = self.get_lang(language) 
    self._finalSigma = False
    self._standardIrishSpelling = std
    self.dispatch_table ={'ga':self.ga_lower,
                  'tr':self.tr_lower,
                  'az':self.az_lower,
                  'el':self.el_lower,
                  "zh":self.just_return,
                  'ja':self.just_return,
                  'th':self.just_return}
    # OLD EXPERIMENTAL CODE for dealing with vowel harmony
    # self._numVowels = 0
    # for c in word:
    #   if c in 'aeiouAEIOU':
    #   self._numVowels += 1
  def get_lang(self,lang): 
      lang = re.findall(r"(^\w*)-*",lang)[0]
      return lang

  def toLower(self):
    if len(self._lang)<2 or len(self._lang)>3:
      print("Invalid BCP-47 code")
      return ''
    return self.get_func()

  def isLenited(self):
    self._lang = self._l
    if '-' in self._l:
      i = self._l.find('-')
      self._lang = self._l[0:i]
    if self._lang == 'ga' or self._lang == 'gd':
      if len(self._w) < 2:
        return False
      else:
        return self._w[0].lower() in 'bcdfgmpst' and self._w[1].lower()=='h'
    else:
      raise NotImplementedError('Method only available for Irish and Scottish Gaelic')
  
  def get_func(self):
    if self._lang in self.dispatch_table.keys():
      return self.dispatch_table[self._lang]()
    else:
      return self._w.lower()

  def just_return(self):
    return self._w

  def ga_lower(self):
    temp = self._w
    if len(self._w)>1:
      if (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
        temp = self._w[0]+'-'+temp[1:]
    return temp.lower()

  def el_lower(self):
    temp = self._w
    if temp[-1]=='\u03a3':
      self._finalSigma = True
      temp = temp[:-1]+'\u03c2'
    return temp.lower()

  def tr_lower(self):
    temp = self._w
    temp = temp.replace('\u0049','\u0131')
    return temp.lower()

  def az_lower(self):
    temp = self._w
    temp = temp.replace('\u0049','\u0131')
    return temp.lower()

    
if __name__=='__main__':
  f = open('tests.tsv', encoding = 'utf8')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
