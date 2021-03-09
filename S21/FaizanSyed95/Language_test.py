import csv 

Vowels=['A','E','I','O','U','Á','É','Í','Ó','Ú']
Greek=['Π','Ό','Λ','Η','Σ']
Greek_again=['π','ό','λ','η','ς']


def Word_check(lang , word):
    LG=list(lang)
    
    if LG[0]=='z' and LG[1]=='h' or LG[0]=='J' and LG[1]=='a' or LG[0]=='t' and LG[1]=='h':
        return word
    
            
    elif LG[0]  == "e" and LG[1] == "n" :
            return word.lower()
        
    elif  LG[0]=='t' and LG[1]=='r' or LG[0]=='a' and LG[1]=='z'  :
            wordArray= list(word)     
            for i in range(len(wordArray)):   
                if wordArray[i] == "I":
                     wordArray[i] = "ı"
                     
            return ''.join(wordArray).lower()
        
    elif  LG[0]=='g' and LG[1]=='a' :
        wordArray = list(word)
        for j in range(len(Vowels)):
            if wordArray[0] == "t" or wordArray[0] == "n":
                if Vowels[j] in wordArray[1]:
                    wordArray.insert(1,'-')     
        
        return ''.join(wordArray).lower()
   
    elif LG[0]=='e' and LG[1]=='l':
        wordArray=list(word)        
        for i in range(len(wordArray)):
            for j in range(len(Greek)):
                if wordArray[i] == Greek[j]:
                    wordArray[i] = Greek_again[j]
                    
        return ''.join(wordArray)
        



file = open("C:/Users/Phaixan/Desktop/5030/S21/FaizanSyed95/tests.tsv",  encoding = "utf8")
read_tsv = csv.reader(file,delimiter="\t") #auto test by reading from the file
for row in read_tsv: # going through each row of tsv file
    W = Word_check(row[1],row[0])
    #print(W , row[2])
    if W == row[2]:
        print("Right")
    else:
        print("not right")




            