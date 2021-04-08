import unicodedata


class CheckBCP_47:
    def LanguageCheck(self):
        language = self._language
        if '-' in self._language:
            index = self._language.find('-')
            language = self._language[0:index]
        if len(language) != 2:
            print("Invalid BCP-47 code")
            return ''
        else:
            return language


class Word(CheckBCP_47):

    def __init__(self, word, bcpCode):
        self._word = word
        self._language = bcpCode

    def toLower(self):
        language = CheckBCP_47.LanguageCheck(self)
        temp = self._word
        
        #for Asian Languages
        if language == 'zh' or language == 'ja' or language == 'th':
            return temp
        
        #for Irish and Scottish language
        if language == 'ga' or language == 'gd':
            if len(self._word) > 1:
                if (self._word[0] == 't' or self._word[0] == 'n') and unicodedata.normalize('NFC', self._word)[1] in 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da':
                    temp = self._word[0]+'-'+temp[1:]
            return temp.lower()
        
        #for Turkish languages
        if language == 'tr' or language == 'az':
            temp = self._word
            temp = temp.replace('\u0049', '\u0131')
            return temp.lower()
        
        #for Greek language
        if language == 'el':
            if temp[-1] == '\u03a3':
                temp = temp[:-1]+'\u03c2'
            return temp.lower()
        else:
            return temp.lower()

    def isLenited(self):
        language = CheckBCP_47.LanguageCheck(self)
        if language == 'ga' or language == 'gd':
            if len(self._word) < 2:
                return False
            else:
                return self._word[0].lower() in 'bcdfgmpst' and self._word[1].lower() == 'h'
        else:
            raise NotImplementedError(
                'Method only available for Irish and Scottish Gaelic')


if __name__ == '__main__':
    f = open('tests.tsv')
    for line in f:
        line = line.rstrip('\n')
        pieces = line.split('\t')
        w = Word(pieces[0], pieces[1])
        answer = w.toLower()
        if answer != pieces[2]:
            print('Test case failed. Expected',
                  pieces[2], 'when lowercasing', pieces[0], 'in language', pieces[1], 'but got', answer)
    f.close()
