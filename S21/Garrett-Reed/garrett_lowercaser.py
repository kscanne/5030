# 3/6/2021 - Garrett Reed - Initial Creation - Alpha#
# Alpha version will be console-only #

# Function to drive process
def wordCaseDriver():
    wordProcess(langEntry(), wordEntry())


def langEntry():
    userLang = input("Please select a language (en, en-US, en-IE, en-Latn, tr, az, ga, ga-IE, el, zh-Hans, ja, th): ")
    langList = ["en", "en-US", "en-IE", "en-Latn", "tr", "az", "ga", "ga-IE", "el", "zh-Hans", "ja", "th"]
    try:
        match = langList.index(userLang)
    except:
        print("Error - Unknown Language")
        quit()
    return match


# Accepts language codes directly instead of through the console
def langEntry2(lang):
    userLang = lang
    langList = ["en", "en-US", "en-IE", "en-Latn", "tr", "az", "ga", "ga-IE", "el", "zh-Hans", "ja", "th"]
    try:
        match = langList.index(userLang)
    except:
        print("Error - Unknown Language")
        quit()
    return match


def wordEntry():
    userWord = input("Please enter the word to make lowercase: ")
    if len(userWord) < 1:
        print("Error - No word provided")
        quit()
    return userWord


def outputLowercase(convertedWord):
    print(convertedWord)
    return convertedWord


# Sends words down correct logic path
def wordProcess(match, userWord):
    if match == 0 or match == 1 or match == 2 or match == 3:
        testMarker = enConverter(userWord)
        return testMarker
    elif match == 4 or match == 5:
        testMarker = trAzConverter(userWord)
        return testMarker
    elif match == 6 or match == 7:
        testMarker = gaConverter(userWord)
        return testMarker
    elif match == 8:
        testMarker = elConverter(userWord)
        return testMarker
    elif match == 9 or match == 10 or match == 11:
        # These languages do not have lowercase characters, so they can be printed directly
        testMarker = outputLowercase(userWord)
        return testMarker

def enConverter(userWordPre):
    convertedText = userWordPre.casefold()
    testMarker = outputLowercase(convertedText)
    return testMarker


def trAzConverter(userWordPre):
    wordAsList = list(userWordPre)
    convertedTextList = []
    # Apply special rule for lowercase i without a dot
    for x in wordAsList:
        if x == "I":
            convertedTextList.append(u"\u0131")
        else:
            convertedTextList.append(x.casefold())
    # Make a single string from list and print it
    convertedText = "".join(convertedTextList)
    testMarker = outputLowercase(convertedText)
    return testMarker


def gaConverter(userWordPre):
    wordAsList = list(userWordPre)
    convertedTextList = []
    gaUpperVowels = ["A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]
    # Apply special rule that checks first two letters of the word
    if wordAsList[0] == "n" or wordAsList[0] == "t":
        if wordAsList[1] in gaUpperVowels:
            convertedTextList.append(wordAsList[0])
            convertedTextList.append("-")
    else:
        convertedTextList.append(wordAsList[0])
    # Convert remaining list to lowercase starting with second character of user input
    for i in range(1, len(wordAsList)):
        convertedTextList.append(wordAsList[i])
    # Make a single string from list and print it
    convertedText = "".join(convertedTextList)
    convertedText = convertedText.casefold()
    testMarker = outputLowercase(convertedText)
    return testMarker
    print(testMarker)


def elConverter(userWordPre):
    wordAsList = list(userWordPre)
    convertedTextList = []
    # Find last letter and if it is sigma, use the special final lower sigma
    if wordAsList[-1] == "Σ":
        finalCharacter = u"\u03C2"
    else:
        finalCharacter = wordAsList[-1].casefold()

    for i in range(0, len(wordAsList)-1):
        convertedTextList.append(wordAsList[i])
    convertedText = "".join(convertedTextList)
    convertedText = convertedText.casefold()
    convertedText = convertedText + finalCharacter
    testMarker = outputLowercase(convertedText)
    return testMarker


# Run Program
wordCaseDriver()