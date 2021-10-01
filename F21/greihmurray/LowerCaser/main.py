def lowercase(lang, text):
    lower_case_text = ''

    if lang[0:2] == 'en':
        lower_case_text = text.lower()

    return lower_case_text

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