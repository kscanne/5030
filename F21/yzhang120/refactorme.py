import unicodedata

class Word:

  def __init__(self, word, bcpCode):
    self._word = word
    self._language = bcpCode

  def getLang(self):
    return self._language[0:self._language.find('-')] if '-' in self._language else self._language

  def ga_rule(self):
    vowel = 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da'
    ga_word = self._word
    if len(ga_word)>1:
        if (ga_word [0] in ['t','n']) and unicodedata.normalize('NFC', ga_word)[1] in vowel:
          ga_word = ga_word[0]+'-'+ga_word[1:]
    return ga_word.lower()

  def tr_az_rule(self):
    I_code = '\u0049'
    latin_small_I_code = '\u0131'
    tr_az_word = self._word
    tr_az_word = tr_az_word.replace(I_code, latin_small_I_code)
    return tr_az_word.lower()

  def el_rule(self):
    upp_sigma_code = '\u03a3'
    greek_small_sigma_code = '\u03c2'
    el_word = self._word
    if el_word[-1] == upp_sigma_code:
        #self._finalSigma = True
        el_word = el_word[:-1] + greek_small_sigma_code
    return el_word.lower()

  def return_word(self):
    return self._word

  def toLower(self):
    language = self.getLang()

    rule = {"tr": self.tr_az_rule(),
            "az": self.tr_az_rule(),
            "ga": self.ga_rule(),
            "el": self.el_rule(),
            "th": self.return_word(),
            "zh": self.return_word(),
            "ja": self.return_word()
            }

    return rule.get(language,self._word.lower()) if len(language) == 2 else print("Invalid BCP-47 code")
    
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
