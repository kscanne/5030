from utils import Word

if __name__=='__main__':
  f = open('tests.tsv')
  failed = False
  for test in f:
    test = test.rstrip('\n')
    testLine = test.split('\t')
    testWord = Word(testLine[0], testLine[1])
    lowerWord = testWord.toLowercase()
    if lowerWord != testLine[2]:
      failed = True
      print('Test case failed. Expected', testLine[2], 'when lowercasing', testLine[0],'in language',testLine[1],'but got',lowerWord)
  if not failed:
       print('All tests succeed!')
  
  f.close()