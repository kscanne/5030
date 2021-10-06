print("PSD ASSIGNMENT: CODE REVIEW")
print("Conversion of UPPERCASE into lowercase")
#List of languages are stored in languages 
languagesAvailable = ["ENGLISH", "TURKISH or AZERBAIJANI", "IRISH","GREEK"]

#Function to print the list of languages
def language_function():
    print("")
    print("Languages:")
    print(" 1."+languagesAvailable [0])
    print(" 2."+languagesAvailable [1])
    print(" 3."+languagesAvailable [2])
    print(" 4."+languagesAvailable [3])
    print("")
    select_function()
    
#Function to select a language from the list and store in inputVar
def select_function():
    inputVar = input("Please press a number to select the language from list above: ")

    if inputVar=="1":
        print("You selected "+languagesAvailable [0]+ " language")
        print("")
        inputVar = input("Please enter uppercase text to convert to lowercase : ")
	#Converted the user input to basic lower case
        inputVar=inputVar.lower()
        print("Lowercase Output : " + inputVar)
        process_function()
    

    if inputVar=="2":
        print("You selected "+languagesAvailable [1]+ " language")
        print("")  
        inputVar = input("Please enter uppercase text to convert to lowercase : ")
        str= inputVar

	#If "I" is found in the user input, replace it with "i"
	#Also, lower case other alphabets
        if str.find("I"):
            inputVar=inputVar.lower()
            inputVar=inputVar.replace('i','ı')
            print("Lowercase Output : " + inputVar)
            process_function()
	#If "I" not found, just lower case rest all alphabets
        else:
            inputVar=inputVar.lower()
            print("Lowercase Output : " + inputVar)
            process_function()            
    
    
    if inputVar=="3":
        print("You selected "+languagesAvailable [2]+ " language")
        print("")
        inputVar = input("Please enter uppercase text to convert to lowercase : ")
        str = inputVar
        f_letter = str[:1]
        s_letter = str[1:2]
	
	#If first letter is from the list below, followed by second letter from the list below, then store lowercase first letter in "beg_substr" and lowercase second letter in "endsubstr"
        if f_letter== "T" or f_letter== "t" or f_letter== "N" or f_letter== "n":
            if s_letter=="A" or s_letter=="I" or s_letter=="E" or s_letter=="O" or s_letter=="U" or s_letter=="Á" or s_letter=="É" or s_letter=="Í" or s_letter=="Ó"or s_letter=="Ú":
                str1 = inputVar.lower()
                str2 = "-"
                beg_substr = str1[:1]
                end_substr = str1[1:]
                my_str = beg_substr + str2 + end_substr
                print("Lowercase Output : " + my_str)
                process_function()
            else:
                inputVar=inputVar.lower()
                print("Lowercase Output : " + inputVar)
                process_function()
        else:
            inputVar=inputVar.lower()
            print("Lowercase Output : " + inputVar)
            process_function()
        

    if inputVar=="4":
        print("You selected "+languagesAvailable [3]+ " language")
        print("")
        inputVar = input("Please enter uppercase text to convert to lowercase : ")
	#Converted the user input to basic lower case
        inputVar=inputVar.lower()
        print("Lowercase Output : " + inputVar)
        process_function()
        
#Function to ask the user to continue or exit
def process_function():
    inputlist = ["Y", "y", "n", "N"]
    print("")
    str_input = input("Do you want to continue(Y/N)? Press Y to Continue, N to Exit: ")
    if str_input=="Y" or str_input=="y":
        language_function()
    else:
        quit()

language_function()
