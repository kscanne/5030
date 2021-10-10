"""
Author: Lorenzo Pappone
This is the main file for running lowercase tests
"""

from utils import Word

if __name__=='__main__':
  f = open('tests2.tsv')
  # clear results file
  open("testPassed.tsv", "w").close()
  failed = False
  for test in f:
    test = test.rstrip('\n')
    testLine = test.split('\t')
    testWord = Word(testLine[0], testLine[1])
    lowerWord = testWord.toLowercase()
    if lowerWord != testLine[2]:
      failed = True
      print('Error: test case failed\n. Expected outcome', testLine[2], '\nInput', testLine[0],'\nLanguage',testLine[1],'\nActual outcome',lowerWord)
    else:
        with open("testPassed.tsv", "a") as f:
          f.write(test + " passed\n")
  if not failed:
       print('All tests succeed!')

  
  f.close()