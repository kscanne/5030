import unicodedata


class Word:
    def __init__(self, word, bcp_code):
        self.wc = word
        self.lang = bcp_code


class Strategy(object):
    def __init__(self, word: Word):
        self.word = word
    """
    strategy interface
    """
    def process(self):
        pass


class StrategyBase(Strategy):
    def process(self) -> str:
        """
        strategy of only lower process
        :return:
        """
        return self.word.wc.lower()


class StrategyKeep(Strategy):
    def process(self) -> str:
        """
        strategy of input word same to output word
        :return:
        """
        return self.word.wc


class StrategyVowel(Strategy):
    """
    strategy of processing to vowel cases
    """
    def process(self) -> str:
        vowels = 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da'
        temp = self.word.wc
        if len(temp) > 1 and (self.word.wc[0] in ['t', 'n']) and \
                unicodedata.normalize('NFC', self.word.wc)[1] in vowels:
            temp = self.word.wc[0] + '-' + temp[1:]
        return temp.lower()


class StrategyCharReplace(Strategy):
    def process(self) -> str:
        """
        strategy of replacing single char
        :return:
        """
        temp = self.word.wc
        temp = temp.replace('\u0049', '\u0131')
        return temp.lower()


class StrategyTrail(Strategy):
    """
    strategy of processing trail char
    """
    def process(self):
        temp = self.word.wc
        if temp[-1] == '\u03a3':
            temp = temp[:-1] + '\u03c2'
        return temp.lower()


class WordProcess(object):
    def __init__(self, word: Word):
        self.word = word
        self.strategy_dict = {'en': StrategyBase, 'zh': StrategyKeep, 'ja': StrategyKeep,
                              'th': StrategyKeep, 'ga': StrategyVowel, 'tr': StrategyCharReplace,
                              'az': StrategyCharReplace, 'el': StrategyTrail}

    def to_lower(self):
        language = self.convert_lang()
        if language in self.strategy_dict:
            specific_strategy = self.strategy_dict[language]
        else:
            specific_strategy = StrategyBase  # default strategy
        return specific_strategy(self.word).process()

    def convert_lang(self) -> str:
        """
        convert one language with '-'. If not, directly return itself
        :return: language code after converting
        """
        language = self.word.lang
        if '-' in self.word.lang:
            i = self.word.lang.find('-')
            language = self.word.lang[0:i]
        if len(language) != 2:
            raise ValueError("Invalid BCP-47 code")
        return language


if __name__ == '__main__':
    f = open('tests.tsv')
    for line in f:
        line = line.rstrip('\n')
        pieces = line.split('\t')
        w = Word(pieces[0], pieces[1])
        answer = WordProcess(w).to_lower()
        if answer != pieces[2]:
            print(f"""Test case failed. Expected {pieces[2]}, when lowercasing {pieces[0]} in language {pieces[1]}, 
            but got {answer}""")
    f.close()
