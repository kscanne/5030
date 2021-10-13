def Lower(word,language):
    l=language[:2].lower()
    if l in ['tr','az']:
        i=l.find('I')
        word=word[0:i]+'ı'+word[i:]
        return word.lower()
    elif l == 'ga':
        if word[0] == 't' or word[0] == 'n' :
            if word[1] in ['A', 'E', 'I', 'O', 'U','Á','É','Í','Ó','Ú']:
                word = word[0] + "-" + word[1:]
                return word.lower()
            else:
                return word.lower()
    elif l == 'el':
        if word[-1] == 'Σ':
            word = word[:-1] + 'ς'
        word.lower()
    elif l in ['zh','th','ja']:
        return word
    else:
        return word.lower()
res=Lower("HELLO","en")
print(res)