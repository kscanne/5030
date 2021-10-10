import pandas as pd
from unicodedata import normalize

## To Lowercase Function
def _to_lower(word, language):
    lang = language[0:language.find('-')] if '-' in language else language
    if lang == 'tr' or lang == 'az':
        return word.replace('I','ı').lower() # '\u0049','\u0131'
    elif lang == 'ga':
        irish_vowels = ['A','E','I','O','U','Á','É','Í','Ó','Ú'] # 'AEIOU\u00c1\u00c9\u00cd\u00d3\u00da'
        norm_word = normalize('NFC',word)
        if word[0]=='t' or word[0]=='n' and normalize('NFC',norm_word[1]) in irish_vowels:
            return (word[0]+'-'+word[1:]).lower()
        else:
            return word.lower()
    elif lang == 'el': # python .lower() already supports greek lowercase
        '''if word[-1] == 'Σ':
            return word.replace('Σ','ς')'''
        return word.lower()
    elif lang == 'zh' or lang == 'ja' or lang == 'th':
        return word
    else:
        return word.lower()

#'nÕg' == 'nÕg' # Test

if __name__ == "__main__":

    # Load Test
    df = pd.read_csv("tests.tsv", sep='\t', header=None)
    df.columns =['word','lang','expected_lower_case']

    # Cover word to lower
    output = []
    for (w,l) in zip(df.iloc[:, 0],df.iloc[:, 1]):
        output.append(_to_lower(w,l))
    df['function_output'] = output

    # Returns true/false 
    correct = []
    for (x,y) in zip(df.iloc[:, 2],df.iloc[:, 3]):
        correct.append(str(x==y))
    df['correct'] = correct

    # Outputs result
    df.to_csv("Output Result.tsv",  sep='\t', encoding='utf-8', index=False)
