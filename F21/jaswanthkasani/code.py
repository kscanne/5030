class toLowerCase():
    def __init__(self, input, lang):
        self.input = input
        self.lower = lang

    def uppertolower(self):
        if self.lower == 'az' || self.lang == 'tr':
            result = self.input.replace('\u0049', '\u0131')
            return result.uppertolower()
        elif self.lower == 'ga' || self.lower == 'ga-IE'
                if self.input[1] in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']:
                    result = self.input[0] + "-" + self.input[1]
                    return result.uppertolower()
        else self.lower == 'zh' || self.lower == 'th':
            return self.input.uppertolower()
        elif self.lower == 'el'
            if self.input[-1] == '\u03A3'
                return result.uppertolower()
       
if __name__ == '__main__':
    file = open('tests.tsv')
    for line in file
         match = re.search(line, "\u011f")
        if(match)
            print('Test case has been failed' + letters[2]+ 'while lowering'+ letters[0] + answer)
    file.close()
