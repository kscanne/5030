with open("F18/data/list.txt", "r") as f:
    languages = f.read().splitlines()
print(languages)


def to_lowercase(word: str, language: str):
    """
    word: str, the string to be converted to lowercase
    language: str, the language of the string, in BCP 47 format
    """
    result = ""

    for idx, letter in enumerate(word):
        lower_letter = letter.lower()
        if language == 'tr' or language == 'az':
            if letter == 'I':
                lower_letter = 'ı'
        elif language.startswith(('gd', 'gv', 'ga')):
            if idx == 1 and letter in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú'] and word[0] in ['n', 't']:
                lower_letter = "-"+letter.lower()
        elif language.startswith('el'):
            if letter == 'Σ' and idx == len(word)-1:
                lower_letter = 'ς'
        elif language.startswith(("zh", "th", "ja")):
            lower_letter = letter

        result += lower_letter

    return result


with open("S23/b-sai/tests.tsv", "r", encoding="utf-8") as f:
    tests = f.read().splitlines()
for test in tests:
    word, language, expected = test.split("\t")
    predicted = to_lowercase(word, language)
    if predicted != expected:
        print(f"Failed to convert {word} to lowercase in {language}!")
        print(f"Expected: {expected}")
        print(f"Actual: {predicted}")
