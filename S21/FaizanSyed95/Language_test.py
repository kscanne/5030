import csv 

Vowels=['A','E','I','O','U','Á','É','Í','Ó','Ú']
GreekCapital=['Π','Ό','Λ','Η','Σ']
GreekSmall=['π','ό','λ','η','ς']


def Word_check(language , word):   #Function which has two inputs as string for checking the word and language
    Letter=list(language)   #converting string into list for detecting index values
    
    #Condition for detecting Chinese, Thai and Japanese 
    if Letter[0]=='z' and Letter[1]=='h' or Letter[0]=='J' and Letter[1]=='a' or Letter[0]=='t' and Letter[1]=='h':
        return word
    
    #Condition for All English        
    elif Letter[0]  == "e" and Letter[1] == "n" :
            return word.lower()
    
    #Condition for Turksih and Azerbhaijani
    elif  Letter[0]=='t' and Letter[1]=='r' or Letter[0]=='a' and Letter[1]=='z'  :
            wordArray= list(word)     
            for i in range(len(wordArray)):   
                if wordArray[i] == "I":
                     wordArray[i] = "ı"
                     
            return ''.join(wordArray).lower()
    
    #Condition for Irish    
    elif  Letter[0]=='g' and Letter[1]=='a' :
        wordArray = list(word)
        for j in range(len(Vowels)):
            if wordArray[0] == "t" or wordArray[0] == "n":
                if Vowels[j] in wordArray[1]:
                    wordArray.insert(1,'-')     
        
        return ''.join(wordArray).lower()
   
    #Condition for Greek 
    elif Letter[0]=='e' and Letter[1]=='l':
        wordArray=list(word)        
        for i in range(len(wordArray)):
            for j in range(len(GreekCapital)):
                if wordArray[i] == GreekCapital[j]:
                    wordArray[i] = GreekSmall[j]
                    
        return ''.join(wordArray)
        


#Openning and reading the test file
file = open("C:/Users/Phaixan/Desktop/5030/S21/FaizanSyed95/tests.tsv",  encoding = "utf8")
read_tsv = csv.reader(file,delimiter="\t") #auto test by reading from the file
for row in read_tsv: # going through each row of tsv file
    W = Word_check(row[1],row[0])
    #print(W , row[2])
    if W == row[2]:
        print("Word Match")
    else:
        print("No Match")




            