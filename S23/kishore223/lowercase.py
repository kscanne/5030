def lowercase_word(word, lang):
    if lang in ['tr', 'az']:
        return word.replace('I', 'ı').lower()
    elif lang == 'ga':
        vowels = set(['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'])
        for i in range(1, len(word)):
            if word[i-1] in ['n', 't'] and word[i] in vowels and word[i].isupper():
                return word[:i] + '-' + word[i:].lower()
        return word.lower()
    elif lang == 'el':
        if word.endswith('Σ'):
            return word[:-1] + 'ς'
        else:
            return word.lower()
    elif lang in ['zh', 'ja', 'th']:
        return word
    else:
        return word.lower()

word = input("Enter a word: ")

print("1.Type 'tr' for Turkish Language")
print("2.Type 'az' for Azerbaijani Language")
print("3.Type 'ga' for Irish Language")
print("4.Type 'zh' for Chinese Language(no changes)")
print("5.Type 'ja' for Japanese Language(no changes)")
print("6.Type 'th' for Thai Language(no changes)")
print("****** Note: If you type any other word or character, it will be just converted to lowercase. ******")

lang = input("Enter language code (BCP-47): ")

lowercased_word = lowercase_word(word, lang)
print(lowercased_word)