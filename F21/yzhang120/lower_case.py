import pandas as pd

def lower_general(input_string):
    return input_string.lower()

def lower_null(input_string):
    return input_string

def lower_tr_az(input_string):
    output_string = ''
    for char in input_string:
        if char != 'I':
            output_string += char.lower()
        else:
            output_string += u"\u0131"
    return output_string

def lower_ga(input_string):
    Irish_vowel = 'AEIOUÁÉÍÓÚ'
    if input_string[0] in 'nt' and input_string[1] in Irish_vowel:
        output_string = input_string[0] + '-' + input_string[1:].lower()
    else:
        output_string = input_string.lower()
    return output_string

def get_lowercase(word, language):
    if language in ('tr', 'az'):
        output = lower_tr_az(word)
    elif language in ('ga', 'ga-IE'):
        output = lower_ga(word)
    elif language in ('zh', 'zh-Hans', 'zh-CN', 'zh-HK' 'ja', 'jp-JP', 'th', 'ko-KR'):
        output = lower_null(word)
    else:
        output = lower_general(word)
    return output

if __name__ == "__main__":
    test = pd.read_csv('tests.tsv', sep='\t', header=None)
    for i in range(len(test)):
        if test.iloc[i,2] == get_lowercase(test.iloc[i,0], test.iloc[i,1]):
            print('Correct!')
        else:
            print(f'{test.iloc[i,0]} in {test.iloc[i,1]} should be transformed to {test.iloc[i,2]} rather than {get_lowercase(test.iloc[i,0], test.iloc[i,1])}')
