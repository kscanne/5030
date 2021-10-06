def lowercase(word, language):

#Turkish or Azerbaijani uses lowercase i with out a dot    
    if 'tr' in language or 'az' in language:
        word = word.replace('I','ı')
        word = word.lower()
        
#Irish rule: when converting uppercase vowels to lowercase, the vowel must be proceded by a dash
    elif 'ga' in language:
        if len(word)>1:
            if word[0] in 'tn' and word[1] in 'AEIOUÁÉÍÓÚ':
                word = word[0] + '-'+ word[1:]
        word = word.lower()
 
#Greek and uppercase sigma at the end of a word gets converted to a small letter final sigma
    elif 'el' in language:
        if word[-1] == 'Σ':
                word = word[:-1]+'ς'
        word = word.lower()

#chinese and japanese do not have lowercase values
    elif 'zh' in language or 'ja' in language or 'th' in language:
        word = word

#lower case for all other languages
    else:
        word = word.lower()


    return word
