# This module mainly solves lowering a word and also can process some special
# cases for languages: tr, az, ga, el.
# author: Zhen Guo
# Date: 3/4/2021

from abc import abstractmethod
import re


class StrategyInterface(object):
    @abstractmethod
    def process(self, word: str, language: str) -> str:
        """:abstract strategy interface for processing word lowering
        """
        pass


class BaseStrategy(StrategyInterface):
    """:Base strategy class for word lowering
    """
    def process(self, word: str, language: str) -> str:
        return word.lower()


class SpecialStrategy(StrategyInterface):
    """class used to special process for word lowering
    """

    def process(self, word: str, language: str) -> str:
        proc_word = word
        if language in ('tr', 'az'):
            proc_word = re.sub(r'I', 'ı', word)
        if language == 'ga' and re.match(r'[n,t][A,E,I,O,U,Á,É,Í,Ó,Ú]', word):
            proc_word = word[0] + '-' + word[1:]
        if language == 'el':
            proc_word = re.sub(r'Σ', 'σ', re.sub(r'Σ$', 'ς', word))
        return proc_word


class WordLower(object):
    def __init__(self):
        self._base_strategy = BaseStrategy
        self._special_strategies = [SpecialStrategy]

    def process(self, word: str, language: str) -> str:
        """ It's the main method for external use
        :param word: input word we want to lower
        :param language: word related language
        :return: word after lowering
        """
        if not word:
            return
        for strategy in self._special_strategies:
            word = strategy().process(word, language)
        return self._base_strategy().process(word, language)

    def add_strategy(self, new_strategy: StrategyInterface):
        """
         It's mainly used to extend new and special strategy
        :param new_strategy: input word we want to lower
        """
        self._special_strategies.append(new_strategy)


if __name__ == "__main__":
    wl = WordLower()
    print(wl.process('tAcht', 'ga'))
    print(wl.process('nÓg', 'ga'))
    print(wl.process('ΠΣΛΗΣ', 'el'))
    print(wl.process(None, 'el'))
