

# Create a function that takes an input string and a language as arguments
# Use conditionals to create special logic based on language
# Use string manipulation to implement special lowercasing rules
# Default to standard python lowercasing function


def lowercase_me(word, language):
    
    if language == "ga":

        if word.isupper():
            return word.lower()
        
        if ("A" in word and not word.startswith("A")):
            return word.replace("A", "-a", 1).lower()

    elif language == "ga-IE":

        # this character won't lowercase. returns none. So I'm using a placeholder
        if "Õ" in word:
            return word.replace("Õ", "!@#!@#!@#").lower().replace("!@#!@#!@#", "õ")
        
        if ("Ó" in word and not word.startswith("Ó")):
            return word.replace("Ó", "-ó").lower()

    elif language == "tr":
        
        if "I" in word:
            return word.lower.replace("i", "ı")

    elif language == "el":
        return word.lower()

    elif language == "zh-Hans":
        return word.lower()

    elif language == "th":
        return word.lower()
    else:
        return word.lower()


if __name__ == "__main__":

    file = open("tests.tsv")

    for count, value in enumerate(file):
        codex = value.rstrip('\n').split('\t')
        
        result = lowercase_me(codex[0], codex[1])

        if result != codex[2]:
            print('TEST FAILURE at line' + str(count) + '. Expected ' + codex[2] + '. Found ' + result + ' for language ' + codex[1])
        else:
            print('Test Passed for line ' + str(count))

    file.close()