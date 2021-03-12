"""
Code after making necessary changes marked by the partner
Code Review Task
Haris Alam Lodhi

"""
import pandas as pd
import re


def lowerCasing(word: str, lan: str):
    if (re.search('^en.*', lan)):
        return word.lower()

    if (re.search('^tr.*', lan) or re.search('^az.*', lan)):
        replace = word.replace('I', u"\u0131")
        return replace.lower()

    if (re.search('^ga.*', lan)):
        vowels = 'A,E,I,O,U,Á,É,Í,Ó,Ú'.split(',')
        if ((re.search('^[n,t].*', word)) and (word[1] in vowels)):
            return((word[0]+'-'+word[1:]).lower())
        else:
            return(word.lower())

    if (re.search('^el.*', lan)):
        if(re.search('Σ$', word)):
            replace = word.replace('Σ', u"\u03C2")
            return(replace.lower())
        else:
            return(word.lower())
    if (re.search('^zh.*', lan) or re.search('^ja.*', lan) or re.search("^th.*", lan)):
        return (word)



if __name__ == '__main__':
    test_passed = True
    try:
        test_data = pd.read_csv('tests.tsv', sep='\t')
        for row_data in test_data.index:
            extracted_data = test_data.iloc[row_data]
            word, lang, result = extracted_data
            processed_result = lowerCasing(word, lang)
            if result != processed_result:
                print("""Test failed for word '{}' the result is '{}' where the expected result was '{}' """.format(
                    word, processed_result, result))
                test_passed = False
            else:
                print("""Test Passed for word '{}' the result is '{}' where the expected result was '{}'""".format(
                    word, processed_result, result))
        if test_passed:
            print('Congratulations! All test cases have been passed')
        else:
            print("Failed! Not all test cases have been met")

    except Exception as e:
        print("File can not be opened because %s " % e)
