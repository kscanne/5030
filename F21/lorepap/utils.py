"""
Author: Lorenzo Pappone
This is the library for lowercase task
"""

import unicodedata


class Word:

  exceptionLanguages = ['tr', 'az', 'ga', 'el']
  unchangedLanguages = ['ja', 'zh', 'th']

  def __init__(self, word, bcp):
    self.word = word
    self.language = bcp

  def toLowercase(self):
    """
    Lowercase input word (self.word) according to language variable (self.language).
    @param: Word object to access to the word variable (self.word)
    @return: word string in its lowercase version
    """

    language = self.getLanguageFromBcp()
    self.checkInvalidBcp(language)
    tmp = self.word
    if language in self.unchangedLanguages:
        return tmp
    elif language in self.exceptionLanguages:
        if language == 'ga':
            if len(self.word) > 1:
                if (self.word[0] == 't' or self.word[0] == 'n') and unicodedata.normalize('NFC', self.word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
                    tmp = self.word[0]+'-'+tmp[1:]
        elif language == 'tr':
            tmp = self.word
            tmp = tmp.replace('\u0049', '\u0131')
        elif language=='az':
            tmp = self.word
            tmp = tmp.replace('\u0049','\u0131')
        elif language=='el':
            # Sigma character
            if tmp[-1]=='\u03a3':
                tmp = tmp[:-1]+'\u03c2'
    return tmp.lower()

  def getLanguageFromBcp(self):
      """
      Get the code from BCP code
      """
      language = self.language
      if '-' in self.language:
            i = self.language.find('-')
            language = self.language[0:i]
      return language

  def checkInvalidBcp(self, language):
      """
      Check if the BCP code provided is invalid
      """
      if len(language) < 2 or len(language) > 3:
        print("Invalid BCP-47 code: ", language)
