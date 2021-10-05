import diacritic_handler

#General handler for lowercasing input text
#Accepts two arguments
#lang - chosen language
#text - text to convert to lowercase
def lowercase(lang, text):
    lower_case_text = ''
    langs_to_ignore = ['zh', 'ja', 'th'] #list of languages to ignore/return provided string

    base_lang = lang[0:2] #gets first two characters of selected language (Base of language)

    #Handles turkish and azerbeijan
    if base_lang == 'tr' or base_lang == 'az':
        if 'I' in text:
            lower_case_text = text.replace('I', 'ı')
            lower_case_text = lower_case_text.lower()
        else:
            lower_case_text = text.lower()
    #Handles Irish
    elif base_lang == 'ga':
        irish_vowels = ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'] #List of standard irish vowels
        words = text.split(' ') #If multiple words, will allow for processing of each word properly

        for word in words:
            #If word starts with n or t then checks for vowels/diacritics and handles accordingly
            if word[0:1] == 'n' or word[0:1] == 't':
                if word[1:2] in irish_vowels:
                    lower_case_text += word[0:1] + '-' + word[1:].lower()
                elif diacritic_handler.isUppercaseDiacritic(word[1:2]):
                    lower_case_text += word[0:1] + '-' + diacritic_handler.convertToLowercaseDiacritic(word[1:2]) + word[2:]
                else:
                    lower_case_text += word.lower()
            else:
                lower_case_text += word.lower()
    #Handles greek, uses lowercase_greek method
    elif base_lang == 'el':
        words = text.split(' ')

        for word in words:
            if word[-1] == 'Σ':
                word = word.replace('Σ', 'ς')
            lower_case_text += lowercase_greek(word)
    #Ensures return of base text with no changes
    elif base_lang in langs_to_ignore:
        lower_case_text = text
    #Defaults to handling text by english rules
    else:
        lower_case_text = text.lower()

    return lower_case_text

#Used to convert greek text to lowercase (Native lower() method was inaccurate)
#Accepts one argument
#char - character to convert
def lowercase_greek(word):
    greek_letters_uppercase = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
    greek_letters_lowercase = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
    lowercase_word = ''

    for char in word:
        #If the letter is final sigma, does not attempt to change at all
        if char == 'ς':
            lowercase_word += char
        else:
            lowercase_word += greek_letters_lowercase[greek_letters_uppercase.index(char)]

    return lowercase_word

#General main method, meant to execute on run, will take input from user and perform basic validation before calling lowercase method
if __name__ == '__main__':
    language = ''
    text = ''
    while True:
        if len(language) < 2:
            language = input('Enter desired language: ').strip()
            if len(language) < 2:
                print('Please enter a language')
                continue
        if not text:
            text = input('Input text to convert to lowercase: ').strip()
            if not text:
                print('Please enter text to convert to lowercase')
                continue
        lower_case_text = lowercase(language, text)

        print('Lower case text: ', '\n', lower_case_text)

        language = ''
        text = ''