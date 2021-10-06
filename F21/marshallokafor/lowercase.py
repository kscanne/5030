
#This Python code converts upper case words to lowercase

# List of  languages with applicable lower case rules
languagesRules = {
    "tr":  ["lowercase", "dotless_I"],
    "az":  ["lowercase", "dotless_I"],
    "ga":  ["second_letter_hyphen", "lowercase"],
    "el":  ["replace_sigma", "lowercase"],
    "zh":  ["no_upper_and_lower_cases"],
    "ja":  ["no_upper_and_lower_cases"],
    "th":  ["no_upper_and_lower_cases"]
}

# Rules to carry out the conversion from upper case to lower case based on the dictionary defined above
def applyWordRule(word, rule):

    if rule == "lowercase":
        # replace letter 'i' with 'ı'
        return word.lower()

    if rule == "dotless_I":

        # replace letter 'i' with 'ı'
        return word.replace('i', 'ı')

    if rule == "second_letter_hyphen":

        # get first letter of word
        firstCharacter = word[0]

        # check if the letter of word is lowercase n or t
        if firstCharacter == "n" or firstCharacter == "t":
            # get second character of the word
            secondCharacter = word[1]

            # check  if second character is an uppercase irish vowel
            if secondCharacter.isupper and secondCharacter in ("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"):
                # convert word to lowercase and insert - as the second character
                return word[:1]+"-"+word[1:]
        return word

    if rule == "replace_sigma":
        # Change all Σ characters to σ unless if Σ is the last character
        wordWithoutLastCharacter = word[:-1].replace('Σ', 'σ')
        lastCharacter = word[-1:]

        # check if the last character of word is Σ
        if lastCharacter == "Σ":
            lastCharacter = "ς"
        return wordWithoutLastCharacter+lastCharacter

    if rule == "no_upper_and_lower_cases":
        # return the original string unchanged
        return word

# Function that does the conversion
def wordToLowercase(language, word):
    language = language.split("-")[0]
    # Check if language exists in available language rules
    if language in languagesRules:
        # Get language and apply language rules
        languageRules = languagesRules[language]
        for rule in languageRules:
            word = applyWordRule(word, rule)

        return word
    else:
        return word.lower()

# Function that reads the test file
def testFile(filePath):

    file = open(filePath, encoding = "utf-8")

    for fileLine in file:
        # Get line of file and covert it to a list
        row = fileLine.split("\n")[0].split("\t")

        word = row[0].strip()
        language = row[1].strip()
        expectedLowercasedWord = row[2].strip()
        lowercasedWord = wordToLowercase(language, word).strip()

        if lowercasedWord != expectedLowercasedWord:
            print( "\033[91m" + "Test Failed  for " + language + " word " + word +
                " Expected " + expectedLowercasedWord + " but got " + lowercasedWord  + "\033[0m")
            break   
        else: 
            print("\033[92m" +"Word: " + word, "\t \tLanguage: " + language,  "\t Expectation: " +
            expectedLowercasedWord,  "\t  Result: " + lowercasedWord  + "\033[0m")
    file.close()


# Load the Test file
testFile("tests.tsv")