import unicodedata

class Word:

  def __init__(self, word, bcpCode):
    self.w = word
    self.l = bcpCode
    self._finalSigma = False

  def wordToLowerCase(self):
    language = self._l
    temp = self._w
    
    if '-' in self._l:
      i = self._l.find('-')
      language = self._l[0:i]
    if len(language)<2 or len(language)>3:
      print("Invalid BCP-47 code")
      return ''  

    if language=='zh' or language=='ja' or language=='th':
      return temp

    if language=='ga':
      if len(self._w)>1:
        if (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          temp = self._w[0]+'-'+temp[1:]
      return temp.lower()

    if language=='tr':      
      temp = temp.replace('\u0049','\u0131')
      return temp.lower()

    if language=='az':     
      temp = temp.replace('\u0049','\u0131')
      return temp.lower()

    if language=='el':
      if temp[-1]=='\u03a3':
        self._finalSigma = True
        temp = temp[:-1]+'\u03c2'
      return temp.lower()

    if False and language=='gd':
      if len(self._w)>1:
        if (self._w[0]=='t' or self._w[0]=='n') and self._w[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          temp = self._w[0]+'-'+temp[1:]
      return temp.lower()
    else:
      return temp.lower()

    

if __name__=='__main__':
  testFile = open('tests.tsv', encoding="utf-8")
  for line in testFile:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    wordToBeChecked = Word(pieces[0], pieces[1])
    answer = wordToBeChecked.wordToLowerCase()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)

  testFile.close()




