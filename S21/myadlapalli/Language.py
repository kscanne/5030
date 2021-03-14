NO_CHANGE_LANGS = ['zh', 'ja', 'th']
TURKISH_LANGS = ['tr', 'az']

IRISH = 'ga'
IRISH_VOWELS = ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']

GREEK = 'el'


def toLower(sentence, lang):
    sentence = sentence.strip()
    result = ''
    lang = lang.split('-')[0]

    # Languages with no change
    if lang in NO_CHANGE_LANGS:
        return sentence

    words = sentence.split(" ")
    # print(words)

    for word in words:
        result += ' ' + wordToLower(word, lang)

    return result.strip()

def wordToLower(word, lang):
    result = ''
    # Languages with no change
    if lang in NO_CHANGE_LANGS:
        return word

    # Irish
    if lang == IRISH:
        if len(word) > 1 and word[0] in ('t', 'n') and word[1] in IRISH_VOWELS:
            result = word[0] + '-' + word[1:].lower()
        else:
            result = word.lower()
        return result

    # Greek
    elif lang == GREEK:
        if word[-1] == 'Σ':
            result = word[:-1].lower() + str(u"\u03C2")
        else:
            result = word.lower()
        return result

    # Turkish
    elif lang in TURKISH_LANGS:
        for ch in word:
            if ch == 'I':
                result += str(u"\u0131")
            else:
                result += ch.lower()
        return result

    else:
        result = word.lower()

    return result.lower()


if __name__ == "__main__":
    r=open("tests.tsv",encoding="utf-8")
    for line in r.readlines():
        word,lang,exp=line.split('\t')
        exp=exp.strip("\n")
        actual=toLower(word,lang)
        if exp==actual:
            print("passed expected: {0} actual: {1}".format(exp,actual))
        else:
            print(repr("failed expected: {0} actual: {1}".format(exp,actual)))
  
