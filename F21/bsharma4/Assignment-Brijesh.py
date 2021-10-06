# Upper to Lower case converter program - Python
# Supporting Languages - "ENGLISH", "TURKISH or AZERBAIJANI", "IRISH","GREEK"

# CODING STANDARDS:
# CamelCase Notation for variable names
# Function name: Camelcase notation with _ between two words for better readability
# Define general purpose of every variable or function in comments for reading purposes

languageSet = ["English", "Turkish or Azerbaijani", "Irish", "Greek"]  # Array for Language List

# Function to select from the List
def selectLanguage_Function():
    print("")
    print("Choose your Language from options below,")
    print("#Press 1 for "+languageSet[0])
    print("#Press 2 for "+languageSet[1])
    print("#Press 3 for "+languageSet[2])
    print("#Press 4 for "+languageSet[3])
    print("")
    converter_Function()

# Function controlling the Logic for each language
def converter_Function():
    inputString = input("Your Choice : ")

    if inputString=="1": # For ENGLISH
        print("You have selected - "+languageSet[0])
        print("")
        inputString = input("Enter String ---> ")
        inputString=inputString.lower()
        print("")
        print("Lowercase output ---> " + inputString)
        exit_Function()


    if inputString=="2": # For TURKISH OR AZERBAIJANI
        print("You have selected - "+languageSet[1])
        print("")
        inputString = input("Enter String ---> ")
        str= inputString
        if str.find("I"):
            inputString=inputString.lower()
            inputString=inputString.replace('i','ı')
            print("")
            print("Lowercase output ---> " + inputString)
            exit_Function()
        else:
            inputString=inputString.lower()
            print("")
            print("Lowercase output ---> " + inputString)
            exit_Function()


    if inputString=="3": # For IRISH
        print("You have selected - "+languageSet[2])
        print("")
        inputString = input("Enter String ---> ")
        str = inputString
        fLetter = str[:1]
        sLetter = str[1:2]
        if fLetter== "T" or fLetter== "t" or fLetter== "N" or fLetter== "n":
            if sLetter=="A" or sLetter=="I" or sLetter=="E" or sLetter=="O" or sLetter=="U" or sLetter=="Á" or sLetter=="É" or sLetter=="Í" or sLetter=="Ó"or sLetter=="Ú":
                str1 = inputString.lower()
                str2 = "-"
                begSubstr = str1[:1]
                endSubstr = str1[1:]
                finalStr = begSubstr + str2 + endSubstr
                print(finalStr)
                exit_Function()
            else:
                inputString=inputString.lower()
                print("")
                print("Lowercase output ---> " + inputString)
                exit_Function()
        else:
            inputString=inputString.lower()
            print("")
            print("Lowercase output ---> " + inputString)
            exit_Function()

    if inputString=="4": # For Greek
        print("You have selected - "+languageSet[3])
        print("")
        inputString = input("Enter String ---> ")
        inputString=inputString.lower()
        print("")
        print("Lowercase output ---> " + inputString)
        exit_Function()

    else:
        print("")
        print("Invalid input, Try again")
        print("")
        selectLanguage_Function()

# Exit Function
def exit_Function():
        inputList = ["Y", "N"]
        print("")
        strInput = input("Do you want to continue(Y/N)?, Press Y to Continue, N to Exit :")
        if strInput=="Y":
            selectLanguage_Function()
        elif strInput=="N":
            print("")
            print("!! THANK YOU !!")
            print("Exiting from the application")
            print("")
            quit()
        else :
          print("Incorrect Entry --> Press Y to Continue, N to Exit")
          exit_Function()

#main function
def main():
    print("--Basic UPPERCASE Into lowercase Converter--")
    print("")
    selectLanguage_Function()

main()



