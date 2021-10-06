class LowerCase:
    def __init__(self, word, bcpCode):
        self.word = word
        self.l = bcpCode

    def wordLower(self):
        self.l=self.l[:2]
        if self.l == 'tr' or self.l == 'az':
            temp = self.word.replace('\u0049', '\u0131')
            return temp.lower()
        elif self.l == 'ga':
            if self.word[0] == 't' or self.word[0] == 'n' and  self.word[1] in ['A', 'E', 'I', 'O', 'U','\u00c1','\u00c9','\u00cd','\u00d3','\u00da']:
                temp = self.word[0] + "-" + self.word[1:]
                return temp.lower()
            else:
                return self.word.lower()
        elif self.l == 'el':
            if self.word[-1] == '\u03A3':
                word = self.word[:-1] + '\u03c2'
            self.word.lower()
        elif self.l == 'zh' or self.l == 'th' or self.l == 'ja':
            return self.word
        else:
            return self.word.lower()
if _name_ == '_main_':
    f = open('tests.tsv')
    for line in f:
        line = line.rstrip('\n')
        words = line.split('\t')
        l = LowerCase(words[0], words[1])
        answer = wordLower()
        if answer != words[2]:
            print('Test case failed. Expected' + words[2]+ 'but got' + answer + 'while converting'+words[0]+'in'+words[1])
        else:
            print("Test case passed")
    f.close()

