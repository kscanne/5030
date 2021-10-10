import re
import unicodedata


def to_lower(word, lang):
    case_insensitive_langs = r'(zh)|(ja)|(th)'
    if not re.compile(case_insensitive_langs).match(lang):
        results = language_select(word, lang)
    else:
        results = word

    return results

def language_select(word, lang):
    # \u00C1 = A with Acute
    # \u00C9 = E with Acute
    # \u00CD = I with Acute
    # \u00D3 = O with Acute
    # \u00DA = U with Acute
    irish_regexp = r'\b([nt])([\u00C1\u00C9\u00CD\u00D3\u00DA])'

    updt_word = word
    if re.compile("tr*").match(lang) or re.compile("az*").match(lang):
        updt_word = word.replace('I','\u0131') #\u0131 = i with not dot
    elif re.compile("ga*").match(lang):
        if re.search(irish_regexp, word):
            updt_word = re.sub(irish_regexp, r'\1-\2', word)
        elif re.search(r'\b([nt])([AEIOU])', word):
            if len(word) > 2 and unicodedata.combining(word[2]) != 0:
                if re.match(r'[\u00C1\u00C9\u00CD\u00D3\u00DA]', unicodedata.normalize('NFC', word[1]+word[2])):
                    updt_word = word[:2] + '-' + word[3:]
            else:
                updt_word = re.sub(r'\b([nt])([AEIOU])', r'\1-\2', word)
    elif re.compile("el*").match(lang):
        updt_word = re.sub('.*\u0370\b', '\u03A3', word) # \u0370 = Σ, \u03A3 = ς

    return updt_word.lower()