import csv


def wordlower(word,lan):

    word=word

    lan=lan

    if(lan=='en'):
        for letter in word:
            letter=word.lower()
        print(letter)


    if(lan=='tr' or lan=='az'):

        for letter in word:
            if (letter=='i' or letter=='I'):
                letter=word.replace('I',"ı").lower()
                print(letter)
            else:
                print(letter.lower(),end='')


    if(lan=='ga'):
        leng=len(word)

        if(word[0]=='n' or word[0]=='t'):
            if(word[1]==a or word[1]==E or word[1]==I or word[1]==O or word[1]==U or word[1]==Á or word[1]==Í or word[1]==Ó or word[1]==Ú):

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

    if(lan=='th' or lan=='zh'):
        for letter in word:
            letter=word.lower()
        print(letter)






