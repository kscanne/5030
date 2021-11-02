import unicodedata
# Mysterious hard-coded Unicode escapes
tr_upper_I = "\u0049"
tr_lower_I = "\u0131"
el_upper_sigma = "\u03a3"
el_lower_sigma = "\u03c2"
ga_upper_A = "\u00c1"
ga_upper_E = "\u00c9"
ga_upper_I = "\u00cd"
ga_upper_O = "\u00d3"
ga_upper_U = "\u00da"


class Word:

    def __init__(self, word, bcpCode, std=False):
        self._word = word
        self._language = bcpCode
        self._finalSigma = False
        self._standardIrishSpelling = std
        # Unnecessary code (Fowler: Remove Dead Code, Remove Setting Method)

    def setWord(self, word):
        self._word = word

    def getLanguage(self):
        # Required “parsing” of the BPC-47 string is hard-coded
        if '-' in self._language:
            return self._language[0:self._language.find('-')]
        return self._language

    def toLower(self):
        language = self.getLanguage()
        # Long lines of code made up of Boolean expressions (Fowler: Decompose Conditional)
        if len(language) != 2:
            print("Invalid BCP-47 code")
            # Awkward error handling in case of an invalid language code
            raise ValueError("Invalid BCP-47 code")
        # Removing nested if-elif and adding dictionary mapping (there is not switch case in python)
        language_dictionary = {
            'ga': self.irishLowering,
            'tr': self.vowelChange,
            'az': self.vowelChange,
            'el': self.greekLowering,
            'zh': self.noChange,
            'ja': self.noChange,
            'th': self.noChange
        }

        if language not in language_dictionary.keys():
            return self.regularLowering()
        else:
            return language_dictionary[language]()

    def isLenited(self):
        language = self.getLanguage()
        if language == 'ga' or language == 'gd':
            if len(self.temp) < 2:
                raise ValueError("Length of parameters is less than 2")
            else:
                return self.temp[0].lower() in 'bcdfgmpst' and self.temp[1].lower() == 'h'
        else:
            raise NotImplementedError(
                'Method only available for Irish and Scottish Gaelic')

    def regularLowering(self):
        return self._word.lower()

    def noChange(self):
        return self._word

    def irishLowering(self):
        if len(self._word) > 1:
            if (self._word[0] == 't' or self._word[0] == 'n') and unicodedata.normalize('NFC', self._word)[1] in ['A', 'E', 'I', 'O', 'U', ga_upper_A, ga_upper_E, ga_upper_I, ga_upper_O, ga_upper_U]:
                self._word = self._word[0]+'-'+ self._word[1:]
        return self._word.lower()

    def greekLowering(self):
        if self._word[-1] == el_upper_sigma:
            self._finalSigma = True
            self._word = self._word[:-1] + el_lower_sigma
        return self._word.lower()

    def vowelChange(self):
        self._word = self._word.replace(tr_upper_I, tr_lower_I)
        return self._word.lower()


if __name__ == '__main__':
    file = open('tests.tsv', encoding='UTF-8')
    for line in file:
        line = line.rstrip('\n')
        pieces = line.split('\t')
        word = Word(pieces[0], pieces[1])
        answer = word.toLower()
        if answer != pieces[2]:
            print('Test case failed. Expected',
                  pieces[2], 'when lowercasing', pieces[0], 'in language', pieces[1], 'but got', answer)
    file.close()
