# -*- coding: utf-8 -*-

# lower
# Developers: Mahdi Rahbar
# License: -

from langdetect import detect, DetectorFactory

class Lower: 
    def __init__(self, string, lang):
        self.string = string 
        self.lang = lang 
        self.detected_lang = self.lang_detector()
        self.word_list = self.string_splitter(string)

    def string_splitter(self, string):
        '''
            This method splits the given string and returns 
                a list of words.

            input: string 
            output: a list of words. 
        '''
        return string.split(" ")

    def lang_detector(self):
        '''
            Using an non-deterministic approach to recognize 
                the used language.

            input: string 
            output: a string showing the language.
        '''
        DetectorFactory.seed = 0 
        return detect(self.string)

    def ga_lower(self):
        '''
            This function process the words in Irish language and 
                convert them based on the rules in Irish. 

            input: - 
            output: returns the fianl string
        '''
        irish_upper = ('A','E','I','O','U','Á','É','Í','Ó','Ú')
        irish_exp = ('n','t')
        for i in range(len(self.word_list)):
            if (self.word_list[i][0] in irish_exp) and \
                (self.word_list[i][1] in irish_upper):
                self.word_list[i] =  self.word_list[i][0].lower() + \
                                     '-' + self.word_list[i][1:].lower()
            else: 
                self.word_list[i] = self.word_list[i].lower()
        return self.word_to_str()
        

    def tr_lower(self):
        '''
            This function process the words in Turkish language and 
                convert them based on the rules in Turkish. 

            input: - 
            output:  string
        '''
        pass

    def el_lower(self):
        '''
            This function process the words in Greek language and 
                convert them based on the rules in Greek. 

            input: - 
            output:  string
        '''
        pass

    def word_to_str(self):
        '''
            Convert list of words to a continous string. 

            input: - 
            output: string
        '''
        return " ".join(self.word_list)


    def call_lower(self):
        '''
            Calls different lower functions based on the given 
                input language.

            input: - 
            output: returns the fianl string
        '''

        if 'en' in self.lang:
            # English 'en'
            return self.string.lower()
        elif self.lang == 'ga':
            # Irish 'ga'
            return self.ga_lower()
        elif self.lang == 'tr' or 'az':
            return self.tr_lower()
        elif self.lang == 'el':
            return self.el_lower()
            # Greek 'el'
        elif self.lang == 'zh' or 'ja' or 'th' or 'fa' or 'ar':
            return self.string
