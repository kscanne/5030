import unicodedata

class Word:

  def __init__(self, word, language):
    self.word = word 
    self.lang = language
  
  def get_language(self):
    language = self.lang
    if '-' in self.lang:
      index = self.lang.find('-')
      language = self.lang[0:index]
      return language
    if not len(language)==2:
      raise ValueError("Invalid BCP-47 code")
 
  def change_to_lower(self):
    language=self.get_language()
    not_lower_list = ('zh','ja','th')
    Irish_vowels = ('AEIOU\u00c1\u00c9\u00cd\u00d3\u00da')
    if language in not_lower_list:
      return self.word
    elif ('ga') in language:
      if len(self.word)>1 and (self.word[0]=='t' or self.word[0]=='n') and unicodedata.normalize('NFC', self.word)[1] in Irish_vowels:
        self.word = self.word[0]+'-'+self.word[1:]
      return self.word.lower()
    elif language=='tr':
      self.word = self.word
      self.word = self.word.replace('\u0049','\u0131')
      return self.word.lower()
    elif language=='az':
      self.word = self.word
      self.word = self.word.replace('\u0049','\u0131')
      return self.word.lower()
    elif language=='el':
      if self.word[-1]=='\u03a3':
        self._finalSigma = True
        self.word = self.word[:-1]+'\u03c2'
      return self.word.lower()
    elif False and language=='gd':
      # specification doesn't ask for this language to be treated differently
      # so this will never be called
      if len(self.word)>1:
        if (self.word[0]=='t' or self.word[0]=='n') and self.word[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          self.word = self.word[0]+'-'+self.word[1:]
      return self.word.lower()
    else:
      return self.word.lower()
    
  def isLenited(self):
    language = self.lang
    if '-' in self.lang:
      i = self.lang.find('-')
      language = self.lang[0:i]
    if language == 'ga' or language == 'gd':
      if len(self.word) < 2:
        return False
      else:
        return self.word[0].lower() in 'bcdfgmpst' and self.word[1].lower()=='h'
    else:
      raise NotImplementedError('Method only available for Irish and Scottish Gaelic')

if __name__=='__main__':
  f = open('tests.tsv',encoding='utf-8')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    word = Word(pieces[0], pieces[1])
    answer = word.change_to_lower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
