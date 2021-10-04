import diacritic_handler

def lowercase(lang, text):
    lower_case_text = ''
    langs_to_ignore = ['zh', 'ja', 'th']

    base_lang = lang[0:2]

    if base_lang == 'tr' or base_lang == 'az':
        if 'I' in text:
            lower_case_text = text.replace('I', 'ı')
            lower_case_text = lower_case_text.lower()
    elif base_lang == 'ga':
        irish_vowels = ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']
        words = text.split(' ')

        for word in words:
            if word[0:1] == 'n' or word[0:1] == 't':
                if word[1:2] in irish_vowels:
                    lower_case_text += word[0:1] + '-' + word[1:].lower()
                elif diacritic_handler.isUppercaseDiacritic(word[1:2]):
                    lower_case_text += word[0:1] + '-' + diacritic_handler.convertToLowercaseDiacritic(word[1:2]) + word[2:]
                else:
                    lower_case_text += word.lower()
            else:
                lower_case_text += word.lower()
    elif base_lang == 'el':
        words = text.split(' ')

        for word in words:
            if word[-1] == 'Σ':
                word = word.replace('Σ', 'ς')
            lower_case_text += lowercase_greek(word)
    elif base_lang in langs_to_ignore:
        lower_case_text = text
    else:
        lower_case_text = text.lower()

    return lower_case_text

def lowercase_greek(word):
    greek_letters_uppercase = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
    greek_letters_lowercase = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
    lowercase_word = ''

    for char in word:
        if char == 'ς':
            lowercase_word += char
        else:
            lowercase_word += greek_letters_lowercase[greek_letters_uppercase.index(char)]

    return lowercase_word

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