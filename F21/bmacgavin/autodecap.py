import csv  # Needed to read .tsv file
from unicodedata import normalize   # Needed for cases involving unicode data of different forms


def language_identifier(row):
    """
    Checks language of potentially convertible word, and sends to specific language function.
    row: word / language / correct version
    return: corrected word following proper language conventions
    """
    if "en" in row[1]:
        return english_rules(row[0])
    if "ga" in row[1]:
        return gaelic_rules(row[0])
    if "tr" in row[1] or "az" in row[1]:
        return oguz_rules(row[0])
    if "el" in row[1]:
        return greek_rules(row[0])
    if "zh" in row[1] or "ja" in row[1] or "th" in row[1]:
        return row[0]


def english_rules(word):
    """
    Runs word through the English language to correct capitalization.
    word: single string
    return: corrected word following proper language conventions
    """
    if not word.islower():
        return word.lower()
    return word


def gaelic_rules(word):
    """
    Runs word through the Gaelic (Irish) language to correct capitalization.
    Special Case: for words starting with "n" or "t", add a hyphen to word
    word: single string
    return: corrected word following proper language conventions
    """
    upper_vowels = "AEIOUÁÉÍÓÚ"
    if len(word) != len(normalize("NFC", word)):
        norm_word = normalize("NFC", word)
        if word.startswith(("n", "t")) and norm_word[1] in upper_vowels:
            return norm_word[0] + "-" + normalize("NFD", norm_word[1:].lower())
        if not norm_word.islower():
            return normalize("NFD", norm_word.lower())
        return normalize(norm_word)
    else:
        if word.startswith(("n", "t")) and word[1] in upper_vowels:
            return word[0] + "-" + word[1:].lower()
        if not word.islower():
            return word.lower()
        return word


def oguz_rules(word):
    """
    Runs word through the Oguz branch languages (Turkish/Armenian) to correct capitalization.
    Special Case: for words with "I", replace with special character "ı"
    word: single string
    return: corrected word following proper language conventions
    """
    if "I" in word:
        new = word.replace("I", "ı")
        if not new.islower():
            return new.lower()
        return new
    if not word.islower():
        return word.lower()
    return word


def greek_rules(word):
    """
    Runs word through the modern Greek language to correct capitalization.
    Special Case: for words ending in "Σ", lowercase to "ς" instead of "σ"
    word: single string
    return: corrected word following proper language conventions
    """
    if not word.islower():
        return word.lower()
    return word


if __name__ == '__main__':
    with open("tests.tsv", encoding="utf8") as file:
        tsv_file = csv.reader(file, delimiter="\t")

        counter = 0
        print(f"\n***************************")
        print(f"*** Standard Test Cases ***")
        print(f"***************************")
        for row in tsv_file:
            if counter < 18:
                convert = language_identifier(row)
                if convert == row[2]:
                    print(f"Success! {convert}")
                else:
                    print(f"Error: {convert}")
                    print({convert})

            if counter == 18:
                print(f"\n************************")
                print(f"*** Other Test Cases ***")
                print(f"************************")

            if 18 <= counter < 27:
                convert = language_identifier(row)
                if convert == row[2]:
                    print(f"Success! {convert}")
                else:
                    print(f"Error: {convert}")

            if counter == 27:
                print(f"\n************************")
                print(f"*** Kevin Test Cases ***")
                print(f"************************")

            if counter >= 27:
                convert = language_identifier(row)
                if convert == row[2]:
                    print(f"Success! {convert}")
                else:
                    print(f"Error: {convert}")

            counter += 1
