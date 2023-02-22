
def to_lowercase(word: str, language: str):
    """
    word: str, the string to be converted to lowercase
    language: str, the language of the string, in BCP 47 format
    """
    result = ""
    
    if language.startswith(("zh", "th", "ja")):
        return word.lower()

    for idx, letter in enumerate(word):

        lower_letter = letter.lower()
        if language == 'tr' or language == 'az':
            if letter == 'I':
                lower_letter = 'ı'
        elif language.startswith(('gd', 'gv', 'ga')):
            is_2nd_letter = idx == 1
            is_exception_letter = letter in [
                'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', "Ó"]
            is_letter_o_latin = ord(letter) in [211]
            is_beginning_exception = word[0] in ['n', 't']
            is_not_last = len(word)-idx > 1
            if is_2nd_letter and (is_exception_letter or is_letter_o_latin) and is_beginning_exception and (is_not_last and ord(word[idx+1]) != 771):
                lower_letter = "-"+letter.lower()
        elif language.startswith('el'):
            if letter == 'Σ' and idx == len(word)-1:
                lower_letter = 'ς'

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
