import sys
import csv
import unicodedata

#CemilCan edition
def check_language(lang):
    supported_languages = ["en", "en-US", "en-IE", "en-Latn", "ga", "ga-IE", "tr", "el", "zh-Hans", "th", "zh", "az", "ja"]
    if lang in supported_languages:
        return True
    else:
        return False

def normalizeWord(word):
    word = unicodedata.normalize('NFC', word)
    return word

def lowerCase(word, lang):
    
    word = word
    
    if '-' in lang:
        lang = lang[0:2]
    
    if lang == "th" or lang == "zh" or lang == "ja":
        return word
    elif lang == "tr" or lang == "az":
        word = word.replace("\u0049", "\u0131")
        word = word.lower()
        return word
    elif lang == "ga":
        word = unicodedata.normalize('NFC', word)
        irish_vowels = ["A","E","I","O","U","\u00C1","\u00C9","\u00CD","\u00D3","\u00DA"]
        if (word[0] == 'n' or word[0] == 't') and word[1] in irish_vowels:
            word = word[0] + '-' + word[1:]
        word = word.lower()
        return word
    elif lang == "el":
        if word[-1] == "\u03A3":
            word = word[:-1] + "\u03C2"
        word = word.lower()
        return word
    else:
        word = word.lower()
        return word

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lowercase.py [directory]")
    
    file = open(sys.argv[1], encoding="utf8")
    read_tsv = csv.reader(file, delimiter="\t")
    for row in read_tsv:
        if check_language(row[1]):
            normalized_word = normalizeWord(row[0]) 
            lowercase_word = lowerCase(normalized_word, row[1])
            if lowercase_word !=  normalizeWord(row[2]):
                print('Lowercasing unsuccessful, expected:', row[2], ", Got:", lowercase_word)
            else:
                print("Lowercasing successful:", row[0], "->", lowercase_word)
        else:
            print(row[1], ", language not supported")
    file.close()

if __name__ == "__main__":
    main()