l=input()
word=input()
res=[]

if l=="en" or l=="en-US" or l=="en-Latn" or l=="en-IE":
    res=word.lower()

elif l=="ga" or l=="ga-IE":
    if word[0] in ['n','t'] and word[1] in ['A','E','I','O','U']:
        res.append(word[0])
        res.append('-')
        for i in word[1:]:
            res.append(i.lower())
    else:
        res=word.lower()
elif l=="el":
    res=word.lower()
elif l=="tr" or l=="az":
    res=word.lower()
else:
    res=word
for i in res:
  print( i,end='')

