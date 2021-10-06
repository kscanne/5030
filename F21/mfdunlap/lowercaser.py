import csv
import unicodedata

#---------------------------------------------------------------------#
#                         LOWERCASE FUNCTION                          #
#---------------------------------------------------------------------#
def lowercase(word, language):
    """
    Function that turns a word into its lowercase version.

    Returns the lowercase version of word in accordance to
    the specifications of language.

    word        a string of a word
    language    the language word is written in
    """

    # Get base language to determine language rules
    base_language = language[:2]

    # Base language is Chinese (zh), Japanese (ja), or Thai (th)
    if (base_language == "zh" or base_language == "ja" or base_language == "th"):
        return word
    
    # Base language is Turkish (tr) or Azerbaijani (az)
    elif (base_language == "tr" or base_language == "az"):

        # Replace capitalized I to dotless i (ı)
        if (word.find("I") != -1):
            word = word.replace("I", "ı")
        return word.lower()
    
    # Base language is Irish (ga)
    elif (base_language == "ga"):
        recode = False

        # Normalize utf-8 characters to simplest unicode entities
        if (not unicodedata.is_normalized('NFC', word)):
            recode = True
            word = unicodedata.normalize('NFC', word).encode('utf-8','ignore').decode('utf-8')

        # Place hypen between 1st and 2nd char if the first char is 'n' or 't' and the second is an gaelic vowel
        if (word[0] in "nt" and word[1] in "AEIOUÁÉÍÓÚ"):
            word = word.lower()
            return word[0] + "-" + word[1:]

        # Denormalize utf-8 characters if they were normalized earlier in the code
        if recode:
            word = unicodedata.normalize('NFD', word).encode('utf-8','ignore').decode('utf-8')
            
        return word.lower()

    # Base language is modern Greek (el)
    elif (base_language == "el"):

        # Replace uppercase Σ at the end of a word with special lowercase sigma (ς)
        if (word.endswith("Σ")):
            word = word.lower()
            word = word[:-1] + "ς"
            return word
        
        return word.lower()
            
    # Default behavior for all other base languages
    return word.lower()


#---------------------------------------------------------------------#
#                                TESTS                                #
#---------------------------------------------------------------------#
if __name__ == "__main__":

    # Verify that test.tsv file cases work properly
    with open("tests.tsv", encoding="utf-8") as tsv_file:
        csv_file = csv.reader(tsv_file, delimiter="\t")
        line = 1

        print("****** TEST CASES GIVEN BY DR. SCANNELL ******")
        for row in csv_file:

            # Pull information from the .tsv file
            word = row[0]
            language = row[1]
            lowercase_correct = row[2]

            # Convert the word to its lowercase form 
            answer = lowercase(word,language)

            if (line == 19):
                print("\n****** TEST CASES GIVEN BY MAYA DUNLAP ******")
            
            # Print whether the answer was correctly converted
            if answer == lowercase_correct:
                print(f"Ex {line}:  {word} was correctly changed to {lowercase_correct}.")
            else:
                print(f"Ex {line}:  ERROR! {word} was incorrectly changed to {lowercase(word,language)} instead of {lowercase_correct}.")
            
            line += 1