
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
            if idx == 1 and (letter in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', "Ó"] or ord(letter) in [211]) and word[0] in ['n', 't'] and (len(word)-idx >= 2 and ord(word[idx+1]) != 771):
                lower_letter = "-"+letter.lower()
        elif language.startswith('el'):
            if letter == 'Σ' and idx == len(word)-1:
                lower_letter = 'ς'
        elif language.startswith(("zh", "th", "ja")):
            lower_letter = letter

        result += lower_letter

    return result


with open("tests.tsv", "r", encoding="utf-8") as f:
    tests = f.read().splitlines()

num_correct = 0
for test in tests:
    word, language, actual = test.split("\t")
    predicted = to_lowercase(word, language)
    if predicted != actual:
        print(f"COuldn't convert {word} in {language}!")
        print(f"Actual: {actual}")
        print(f"Predicted: {predicted}")
    else:
        num_correct += 1

print(f"Successfully completed {num_correct}/{len(tests)} tests")
