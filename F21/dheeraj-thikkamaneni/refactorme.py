#Dheeraj 
#Shirishma
#Vamshi
#Naveen


import unicodedata

class Word:

    def __init__(self, word, bcpCode, std=False):
        self.word = word
        self._language = bcpCode
        self._finalSigma = False
        self._standardIrishSpelling = std
        self.I = '\u0049'
        self.dotlessI='\u0131' 
        self.sigma1='\u03a3'  
        self.sigma2='\u03c2'
        self.checks='\u0041\u0045\u0049\u004F\u0055\u00c1\u00c9\u00cd\u00d3\u00da' 
        

        
        
    def noLowerCase(self):
        return self.word
    
    def irish(self):
        temp = self.word
        if len(self.word)>1:
            if (self.word[0]=='t' or self.word[0]=='n') and unicodedata.normalize('NFC', self.word)[1] in self.checks:
                temp = self.word[0]+'-'+self.word[1:]

        return temp.lower()
    
    def turkish(self): 
        temp = self.word
        temp = self.word.replace(self.I,self.dotlessI)
        return temp.lower()
    
        
    def greek(self):
        if self.word[-1]==self.sigma1:  
            self._finalSigma = True
            temp =self.word[:-1]+self.sigma2
        return temp.lower()
        
        
    def lowerCase(self):
        return self.word.lower()
        
    def isLenited(self):
        if self._language == 'gd'or self._language == 'ga':
            if len(self.word) < 2: 
                return False
            else:
                return self.word[0].lower() in 'bcdfgmpst' and self.word[1].lower()=='h'
        else:
            raise NotImplementedError('Method only available for Irish and Scottish Gaelic')

        
        
    def toLower(self):    
        language=self._language
        if '-' in self._language:
            i = self._language.find('-')
            language = self._language[0:i]
        if len(language)<2 or len(language)>3: 
            raise Exception("Invalid BCP-47 code")

        if language=='zh' or language=='ja' or language=='th':
            return w.noLowerCase()
        elif language=='ga':
            return w.irish()
        elif language=='tr'or language=='az':
            return w.turkish()
        elif language=='el':
            return w.greek()
        elif language == 'gd':
                return isLenited()
        else:
            return w.lowerCase()
        
        
        
        
if __name__=='__main__':
    file = open('tests.tsv', encoding='utf-8') 
    for line in file:
        line = line.rstrip('\n')
        pieces = line.split('\t')
        w = Word(pieces[0], pieces[1])
        answer = w.toLower()
        print(answer)
        if answer != pieces[2]:
            print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
    file.close()
