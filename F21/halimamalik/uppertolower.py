
def lowercaseconverter(word,language): #method to convert uppercase to lowercase
    irish_capvowel = ['A','E','I','O','U',u"\u00C1", u"\u00C9",u"\u00CD",u"\u00D3",u"\u00DA"]
    langcode = language[0:2] 
    if langcode == 'tr' or langcode == 'az':
        lowerword = word.lower()
        output = lowerword.replace('i',u"\u0131")
        return output
    elif langcode == 'ga':
        if word[0] == 'n' or word[0] == 't':
            if word[1] in irish_capvowel:
                splitword = list(word.lower())
                splitword.insert(1, '-')
                output = ''.join(splitword)
                return output
            else:
                return word.lower()
        else:
            return word.lower()
    else:
        return word.lower()

if __name__=='__main__':
    with open('tests.tsv',  encoding="utf8") as f:
        row_list = []
        for row in f:
            stripped = row.strip()
            row_list = stripped.split()
            w = lowercaseconverter(row_list[0], row_list[1])
            if w != row_list[2]:
                print('Test case failed. Expected', row_list[2], 'when lowercasing',row_list[0], 'using language', row_list[1], 'but got',w)
            else:
                print('Test case passed')
            
    f.close()
