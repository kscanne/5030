import re


def to_lower(word, lang):
    case_insensitive_langs = r'(zh)|(ja)|(th)'
    if not re.compile(case_insensitive_langs).match(lang):
        results = language_select(word, lang)
    else:
        results = word

    return results

def language_select(word, lang):
    if re.compile("tr*").match(lang) or re.compile("az*").match(lang):
        updt_word = word.replace('I','\u0131')
    elif re.compile("ga*").match(lang):
        updt_word = re.sub(r'\b([nt])([AEI\u004FU\u00C1\u00C9\u00CD\u00D3\u00DA])', r'\1-\2', word)
    elif re.compile("el*").match(lang):
        updt_word = re.sub('.*\u0370\b', '\u03A3', word)
    else:
        updt_word = word

    return updt_word.lower()