import locale
import re

## read the file and iterate through every line
class WordConvert:
    def readTestFile(self):
        textFile = open("tests.tsv", "r")
        while textFile:
            line = textFile.readline()
            if line == "" or line == '\n':
                break
            word, lang, _  = line.split('\t')
            self.methodToProcessText(word,lang)
        textFile.close()

    def makeWordsLower(self,word):
        print(word.lower())

    def methodToProcessText(self, text, lang):
        # using regex check for the language and do functionalities
        word = text
        if re.findall("\A[n,t][AEIOUÁÉÍÓÚ]",text) and re.match("^ga.*",lang):
            word = re.sub(r'(^[n,t])([AEIOUÁÉÍÓÚ])', r'\1-\2',text)
        elif re.match("^tr.*", lang):
            word = text.replace("I","ı")
        self.makeWordsLower(word.lower())

wordConvert = WordConvert()
wordConvert.readTestFile()