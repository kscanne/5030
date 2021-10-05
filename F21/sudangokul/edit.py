from langdetect import detect
word = input("Please Enter your Own String : ")
lang1= detect(word) 
print("given string language is = ",lang1)
print("code  laguage\nenglish (en)\nTurkish (tr)\nAzerbaijani (az)\nIrish (ga)\nhindi  (hi)\nchinese   (zh)\ngreek  (el)\nJapanese  (ja)\nthai  (th)\nSpanish  (es)\nrussian  (ru)") 
lang= input("Enter the Correct language = ",)  
p=[]
if lang=='tr' or lang=='az':
    for i in word:
        if i=='I':
           p.append('\u0131')
        elif i>='A' and i<='Z':
            p.append(i.lower())
elif lang=='ga' or lang=='ga-IE':
    if((word[0]=='n' or word[0]=='t') and (word[1]=='A' or word[1]=='E' or word[1]=='I' or word[1]=='O' or word[1]=='U' or word[1]=='\u00C1' or word[1]=='\u00C9' or word[1]=='\u00CD' or word[1]=='\u00D3' or word[1]=='\u00DA')):
        p.append(word[0])
        p.append('-')
        if(word[1]=='\u00C1' ):
            p.append('\u00E1')
        elif(word[1]=='\u00C9'):
            p.append('\u00E9')
        elif(word[1]=='\u00CD'):
            p.append('\u00ED')
        elif(word[1]=='\u00D3'):
            p.append('\u00F3')
        elif(word[1]=='\u00DA'):
            p.append('\u00FA')
        elif(word[1]>='A' or word[1]=='E' or word[1]=='I' or word[1]=='O' or word[1]=='U' ):
            p.append(word[1].lower())
        c=word[2:]
        for i in c:
            if i>='A' and i<='Z':
                p.append(i.lower())
            elif(i=='\u00C1'):
                p.append('\u00E1')
            elif(i=='\u00C9'):
                p.append('\u00E9')
            elif(i=='\u00CD'):
                p.append('\u00ED')
            elif(i=='\u00D3'):
                p.append('\u00F3')
            elif(i=='\u00DA'):
                p.append('\u00FA')
            else:
                p.append(i)
    else:
        for i in word:
            if i>='A' and i<='Z':
                p.append(i.lower())
            elif(i=='\u00C1'):
                p.append('\u00E1')
            elif(i=='\u00C9'):
                p.append('\u00E9')
            elif(i=='\u00CD'):
                p.append('\u00ED')
            elif(i=='\u00D3'):
                p.append('\u00F3')
            elif(i=='\u00DA'):
                p.append('\u00FA')
            elif(i=='\u00D5'):
                p.append('\u00F5')
            else:
                p.append(i)
elif lang=='el':
    if word[-1]=='\u03A3':
        c=word[:-1]
        x='\u03C2'
    else:
        c=word
        x=''
    for i in c:
        if(i=='\u03A0'):
            p.append('\u03C0')
        elif(i=='\u03A3'):
            p.append('\u03C3')
        elif(i=='\u0397'):
            p.append('\u03B7')
        elif(i=='\u039B'):
            p.append('\u03BB')
        elif(i=='\u038C'):
            p.append('\u03CC')
    p.append(x)
elif lang=='en' or lang=='en-US' or lang=='en-IE' or lang=='en-Latn':
    for i in word:
        if i>='A' or i<='Z':
            p.append(i.lower())
        else:
            p.append(i)
else:
    for i in word:
        p.append(i)
for i in p:
    print(i,end='')

