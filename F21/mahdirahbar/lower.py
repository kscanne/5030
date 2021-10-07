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
        
        for i in range(len(self.word_list)):
            if (self.word_list[i][0].encode('utf-8') in self.irish_lower_decoded) and \
                (self.word_list[i][1].encode('utf-8') in self.irish_upper_decoded):
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
        char_dict = {'I':'ı'}

        for i in range(len(self.word_list)):            
            for key, value in char_dict.items():
                indexes = [i for i, ltr in enumerate(self.word_list[i]) if ltr == key]
                for l in indexes:
                    self.word_list[i] = self.word_list[i][:l].lower() + value + self.word_list[i][l+1:].lower()

        ## An alternative way is the following two lines of code!

        ## The following 2 lines of codes are a more general form of 
        ##      converting Turkish characters to lower case.
        # for i in range(len(self.word_list)):
        #     self.word_list[i] = self.word_list[i].lower()
        return self.word_to_str()

    def el_lower(self):
        '''
            This function process the words in Greek language and 
                convert them based on the rules in Greek. 

            input: - 
            output:  string
        '''
        exception_chars = {'Σ':'ς'}
        for i in range(len(self.word_list)):
            for key, value in exception_chars.items():
                if key == self.word_list[i][-1]:
                    self.word_list[i] = self.word_list[i][:-1].lower()+ value
                else:
                    self.word_list[i] = self.word_list[i].lower()

        return self.word_to_str()



    def word_to_str(self):
        '''
            Convert list of words to a continous string. 

            input: - 
            output: string
        '''
        return " ".join(self.word_list)

    def utf8_decoder(self, word):
        '''
            Returns the decoded word.
            input: - 
            output: string
        '''
        return word.decode('utf-8')

    def ga_util(self):
        '''
            Build the required utility for ga.
            input: - 
            output: None
        '''
        irish_upper = (u'A',u'E',u'I',u'U',u'Á',u'É',u'Í',u'Ó',u'Ú') # ,u'O'
        irish_exp = ('n','t')
        self.irish_upper_decoded = []
        for i in range(len(irish_upper)):
            self.irish_upper_decoded.append(irish_upper[i].encode('utf-8'))
        self.irish_lower_decoded = []
        for i in range(len(irish_exp)):
            self.irish_lower_decoded.append(irish_exp[i].encode('utf-8'))

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
        elif 'ga' in self.lang :
            # Irish 'ga'
            self.ga_util()
            return self.ga_lower()
        elif self.lang in ['tr', 'az']:
            return self.tr_lower()
        elif self.lang == 'el':
            return self.el_lower()
            # Greek 'el'
        elif any(lan in self.lang for lan in ['zh', 'ja', 'th', 'fa', 'ar']):
            return self.string
