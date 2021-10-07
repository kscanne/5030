class convertLowerCase():

    def lc(self, text):   # methid that converts languages without any special cases 
        return text.lower()       
    
    def tr(self, text):   # for turkish
        lowercase = ""
        turkish_dict = {'I':'ı', 'İ':'i'}
        for word in text:
            if word == 'I' or word == 'İ':
                lowercase += turkish_dict[word]
            else:
                lowercase += word.lower()
        return lowercase            
    
    
    def el(self, text):   # for greek
        lowercase = ""
        if text[-1] == 'Σ':
            lowercase += text[0:-1].lower()+'ς'
        else:
            lowercase += text.lower()
        return lowercase     
        
        
    def ga(self, text):   # for irish 
        lowercase = "" 
        checks = 'AEIOUÁÉÍÓÚ'
        checks2 = 'ÃẼĨÕŨ'
        
        if text[0] == 't' or text[0] == 'n':
            if text[1]+text[2] in checks2:
                lowercase += text.lower()
            elif text[1] in checks:
                lowercase += text[0] + '-' + text[1:].lower()
            else:
                lowercase += text.lower()    
        else:
            lowercase += text.lower()
            
        return lowercase    
 
    

def language(txt, lang_code):
    
    lang_code = lang_code
    text = txt 
     
    lang_direct = ['en', 'th', 'en-us', 'zh-hans', 'en-latn', 'en-ie', 'ja']
    
    if [lang for lang in lang_direct if lang_code in lang]:        
        return obj.lc(text)
    elif lang_code == 'tr' or lang_code == 'az:
        return obj.tr(text)
    elif lang_code == 'el':
        return obj.el(text)
    elif lang_code == 'ga' or lang_code == 'ga-ie':
        return obj.ga(text)
    else:
        return 'nothing selected in the list'

     
text_input = input("Enter text: ").strip()
lang_code = input("Enter language code: ").lower().strip()

obj = convertLowerCase()    

lowercase_text = language(text_input, lang_code)

print("Text in lowercase: {}".format(lowercase_text))    












# test case code
# first run the above code first so that the test-case code can access the methods mentioned. 
# mention the file path of the tests.tsv to thats located in your computer in order to read the file.
# an object has been created for the class, execute the testcase code.


import pandas as pd

class convertLowerCaseTest():
    
    data = pd.read_csv('tests.tsv', delimiter = '\t')   # mention the tsv file path to read the values
    test_data = [list(row) for row in data.values]

    for i in test_data:
        text = i[0]
        lang_code = i[1].lower()
        
        print('input: ' + text)
        print('lang: ' + i[1])
        
        lowercase_text = language(text, lang_code)
        
        print("Your scenario: " + lowercase_text)
        print("Actual scenario: " + i[2])
        print('\n')
        
objt = convertLowerCaseTest()   
