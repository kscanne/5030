import csv
import re

irishVowels = ["A","E","I","O","U","Á","É","Í","Ó","Ú"]

def wordlower(word,lan):

    if(lan=='en'):
      print(word.lower())

    if(lan=='tr' or lan=='az'):

        for letter in word:
            if (letter=='i' or letter=='I'):
                letter=re.sub(r'[Ii]','ı',word)
                print(letter.lower(),end='')
            else:
                print(letter.lower(),end='')

    if(lan=='ga' or 'ga-IE'):
        if(word[0]=='n' or word[0]=='t'):
            if(word[1] in irishVowels):
                for letter in word:
                    member = ['-']
                    word.insert(1,member)
                    print(word.lower(),end='')
            else:
                print(word.lower()，end='')

    if(lan=='el'):
        leng=len(word)
        if((word[len(word)-1])=='∑'):
            for letter in word:
                letter=word.replace('Σ',"ς").lower()
                print(letter)
        else:
            print(word.lower(), end='')

    if(lan=='th' or 'zh' or 'ja'):
        print=(word.lower())
