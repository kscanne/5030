

# 1. Create a function that takes an input string and a language as arguments
# 2. Use conditionals to create special logic based on language
# 3. Use string manipulation to implement special lowercasing rules
# 4. Default to standard python lowercasing function


def lowercase_me(word, language):
    
    if language.startswith("ga"):

        # this character returns none when passed to the lower() method.
        # I'm using a placeholder and then swapping back
        if "Õ" in word or chr(771) in word:
            return word.replace("Õ", "!@#!@#!@#").lower().replace("!@#!@#!@#", "õ")

        if (word.startswith("n") or word.startswith("t")) and (word[1] in ['A','E','I','O','U','Á','É','Í','Ó','Ú']) :
            return (word[:1] + "-" + word[1:]).lower()         

        return word.lower()

    elif language == "tr":
        
        if "I" in word:
            return word.lower().replace("i", "ı")

    elif language in ["el", "zh-hans", "th"]:
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