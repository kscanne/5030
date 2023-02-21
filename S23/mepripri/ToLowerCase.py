import csv

def splitLang(lang):
    lang=lang.split('-')
    return lang[0]

def toLower(s,lang):
    str=''
    first=0
    lang=splitLang(lang)
    if lang=='tr' or lang=='az':
        for i in s:
            if i=='I':
                str+=chr(305)
            else:
                str+=i.lower()
    elif lang=='ga':
        if (s[0]=='n' or s[0]=='t') and s[1] in ['A','E','I','O','U','Á','É','Í','Ó','Ú']:
            str+=s[0].lower()+'-'+s[1:].lower()
        else:
            str+=s.lower()
    elif lang=='el':
        if ord(s[-1])==931:
            str+=s[:-1].lower()
            str+=chr(962)
        else:
            str=str+s.lower()
    elif len(lang)!=2:
        str+='Invalid Language'
    else:
        str+=s.lower()
    return str
    

with open("tests.tsv") as file:
    read = csv.reader(file,delimiter="\t")
    for r in read:
        print("Word : ",r[0])
        print("Lowercase : ",toLower(r[0],r[1]),"\n")