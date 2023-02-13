import pandas as pd



def lowerCase(word, lang):
    word = word.strip()
    langStart = lang[:2]

    if "en" == langStart:
        lower_word = word.lower()
        return lower_word
    
    if "tr" == langStart or 'az' == langStart:
        
        if "I" in word:
            word_list = [*word]
            indices = [i for i, x in enumerate(word_list) if x == "I"]
            
            for x in indices:
                word_list[x] = 'ı'

            lower_word = combineToString(word_list)
            lower_word = lower_word.lower()
            return lower_word
        else:
            return word
        
    if "ga" == langStart:
        lowCase = word.lower()
        caps = ['A','E','I','O','U','Á','É','Í','Ó','Ú']
        if word[0] == 'n' or word[0] == 't':
            if word[1] in caps and word[2].isalpha(): #must check isalpha as Õ parses as `O`,`~`
                word_list2 = [*lowCase]
                word_list2.insert(1,'-')
                lower_word = combineToString(word_list2)
                return lower_word
            else:
                word = word.lower()
                return word
            
        else:
                word = word.lower()
                return word
        
    if "el" == langStart:
        if word[-1] == 'Σ':
            lower_word = word.lower()
            lower_word_list = [*lower_word]
            lower_word_list[-1] = 'ς'
            lower_word = combineToString(lower_word_list)
            return lower_word
    else:
        return word
    
def combineToString(char_list):
    new_word = ""
    for x in char_list:
        new_word += x
    return new_word

def test_main():

    test_cases = pd.read_csv('../5030/S23/thofstrand/tests.tsv',sep='\t',names=["word","lang","lower"])
    for i in range(len(test_cases)):
        #word_output = lowerCase(test_cases['word'][i],test_cases['lang'][i])
        #print(word_output)
        result = lowerCase(test_cases['word'][i],test_cases['lang'][i]) == test_cases['lower'][i]
        print(result)
        
  
            


if __name__ == '__main__':
    
    test_main()
