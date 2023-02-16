print("")
print("**************************************************************WELCOME TO THE UTILITY*********************************************")
print("****************************************************Convert UPPERCASE Into lowercase*********************************************")
print("*********************************************************************************************************************************")
print("")
# Creating an array for Langauge List, In future more langauges can get added to array.
languageList = ["ENGLISH", "TURKISH or AZERBAIJANI", "IRISH","GREEK"]

# Function to select from the List
def language_Function():
    print("")
    print("****************************************************************PLEASE SELECT LANGAUGE **********************************")
    print("********* 1."+languageList[0])
    print("********* 2."+languageList[1])
    print("********* 3."+languageList[2])
    print("********* 4."+languageList[3])
    print("")
    print("************************************************ NOTE: USE THE SERIAL NUMBER TO SELECT A LANGAUGE************************")
    print("-------------------------------------------------For example : Press 1 for English---------------------------------------")
    print("")
    select_Function()
    
# Logic for each langauge, In future more langauges can be added and their logic can be written.
def select_Function():
    inputString = input("ENTER OPTION FROM ABOVE LIST --->")
    
    if inputString=="1": # For ENGLISH
        print("************************************ ******** LANGAUGE SELECTED IS - "+languageList[0]+" ********************************************" )
        print("")
        inputString = input("PLEASE ENTER TEXT ---> ")
        inputString=inputString.lower() 
        print("")
        print("LOWERCASE OUTPUT ---> " + inputString)
        exit_Function()
    
    
    if inputString=="2": # For TURKISH OR AZERBAIJANI
        print("********************** LANGAUGE SELECTED IS - "+languageList[1])
        print("")  
        inputString = input("PLEASE ENTER TEXT ---> ")
        str= inputString
        if str.find("I"):
            inputString=inputString.lower()
            inputString=inputString.replace('i','ı')
            print("")
            print("LOWERCASE OUTPUT ---> " + inputString)
            exit_Function()
        else:
            inputString=inputString.lower()
            print("")
            print("LOWERCASE OUTPUT ---> " + inputString)
            exit_Function()            
    
    
    if inputString=="3": # For IRISH
        print("********************** LANGAUGE SELECTED IS - "+languageList[2])
        print("")
        inputString = input("PLEASE ENTER TEXT ---> ")
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
                print("LOWERCASE OUTPUT ---> " + inputString)
                exit_Function()
        else:
            inputString=inputString.lower()
            print("")
            print("LOWERCASE OUTPUT ---> " + inputString)
            exit_Function()
        
    if inputString=="4": # For Greek
        print("********************** LANGAUGE SELECTED IS - "+languageList[3])
        print("")
        inputString = input("PLEASE ENTER TEXT ---> ")
        inputString=inputString.lower()
        print("")
        print("LOWERCASE OUTPUT ---> " + inputString)
        exit_Function()
        
    else:
        print("")
        print("**************************************** INCORRECT INPUT ********************************************")
        print("")
        language_Function()
        
# Exit Function
def exit_Function():
        inputList = ["Y", "N"]
        print("")
        strInput = input("************************ Do you want to continue(Y/N)**, Press Y to Contiue, N to Exit :")
        if strInput=="Y":
            language_Function()
        elif strInput=="N":
            print("")
            print("******************************!! THANK YOU !!****************************************************")
            print("******************************Exiting from the application***************************************")
            print("")
            quit()
        else :
          print("Incorrect Entry --> Press Y to Contiue, N to Exit")
          exit_Function()

language_Function()

    
    
    
