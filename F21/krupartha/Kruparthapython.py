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
        checks = 'AEIOU'
        for w in range(0, len(text)-1):
            if text[w] == 't' or text[w] == 'n':
                if text[w+1] in checks:
                    lowercase += text[w] + '-'
                else:
                    lowercase += text[w].lower()
            else:
                lowercase += text[w].lower()
            
        return lowercase + text[-1].lower()    
    
    
    
    def ga_ie(self, text):   # for a dialect of irish
        lowercase = "" 
        checks = 'AEIOUÁÉÍÓÚ'
        for w in range(0, len(text)-2):
            if text[w] == 't' or text[w] == 'n':
                if (text[w+1] + text[w+2]) in 'ÃB̃C̃D̃ẼẼF̃G̃H̃ĨJ̃K̃L̃M̃ÕP̃Q̃R̃S̃T̃ŨṼW̃X̃ỸZ̃':   
                    lowercase += text[w]
                else:
                    if text[w+1] in checks:
                        lowercase += text[w] + '-'
                    else:
                        lowercase += text[w].lower()
            else:
                lowercase += text[w].lower()
            
        if text[-2] == 't' or text[-2] == 'n':
            if text[-1] in checks:
                lowercase += text[-2] + '-'
            else:
                lowercase += text[-2].lower()
        else:       
            lowercase += text[-2].lower()        
         
        
        return lowercase + text[-1].lower()

    
    
    
    

def language(txt, lang_code):
    
    lang_code = lang_code
    text = txt 
     
    lang_direct = ['en', 'th', 'en-us', 'zh-hans', 'en-latn', 'en-ie']
    
    if [lang for lang in lang_direct if lang_code in lang]:        
        return obj.lc(text)
    elif lang_code == 'tr':
        return obj.tr(text)
    elif lang_code == 'el':
        return obj.el(text)
    elif lang_code == 'ga':
        return obj.ga(text)
    elif lang_code=='ga-ie': 
        return obj.ga_ie(text)
    else:
        return 'nothing selected in the list'

    
    
    
text_input = input("Enter text: ").strip()
lang_code = input("Enter language code: ").lower().strip()

obj = convertLowerCase()    


lowercase_text = language(text_input, lang_code)


print("Text in lowercase: {}".format(lowercase_text))    

