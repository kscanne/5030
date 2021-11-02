import unicodedata

class Word:
  def __init__(input, word, bcpCode):
    input.word = word
    input.bcpCodeofLanguage = bcpCode
    
  def toLower(input):  
    language = input.bcpCodeofLanguage    
    if '-' in input.bcpCodeofLanguage:
      i = input.bcpCodeofLanguage.find('-')
      language = input.bcpCodeofLanguage[0:i]      
    if len(language)<2 or len(language)>3:
      print("Invalid BCP-47 code")
      return ''      
    tempVariable = input.word    
    if language=='zh' or language=='ja' or language=='th':
      return tempVariable
    elif language=='ga' or language=='gd':
      if len(input.word)>1:
        if (input.word[0]=='t' or input.word[0]=='n') and unicodedata.normalize('NFC', input.word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
          tempVariable = input.word[0]+'-'+tempVariable[1:]
      return tempVariable.lower()      
    elif language=='tr' or language=='az':
      tempVariable = input.word
      tempVariable = tempVariable.replace('\u0049','\u0131')
      return tempVariable.lower()      
    elif language=='el':
      if tempVariable[-1]=='\u03a3':
        tempVariable = tempVariable[:-1]+'\u03c2'
      return tempVariable.lower()   
    else:
      return tempVariable.lower()


if __name__=='__main__':
  f = open('tests.tsv', encoding="utf8")
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.toLower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()