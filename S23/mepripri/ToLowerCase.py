import csv

def splitLang(l):
    l=l.split('-')
    if len(l[0])==2:
        l=l[0]
    return l

def toLower(s,lang):
    str=''
    first=0
    lang=splitLang(lang)
    if lang=='tr' or lang=='az':
        for i in s:
            if ord(i)==73:
                str+=chr(305)
            else:
                str+=i.lower()
    elif lang=='ga':
        first=0
        for i in range(len(s)):
            if i==0:
                if (s[0]=='n' or s[0]=='t') and s[1] in ['A','E','I','O','U','Á','É','Í','Ó','Ú']:
                    str+=s[0].lower()+'-'+s[1].lower()
                    first=1
                else:
                    str+=s[i].lower()
            elif i==1 and first==1:
                continue
            else:
                str+=s[i].lower()
    elif lang=='el':
        if ord(s[-1])==931:
            str+=s[:-1].lower()
            str+=chr(962)
        else:
            str=str+s.lower()
    elif lang=='zh' or lang=='th' or lang=='ja' or lang=='en':
        str+=s.lower()
    else:
        str+='Invalid Language'
    return str


with open("tests.tsv") as file:
    read = csv.reader(file,delimiter="\t")
    for r in read:
        print("Word : ",r[0])
        print("Lowercase : ",toLower(r[0],r[1]),"\n")
