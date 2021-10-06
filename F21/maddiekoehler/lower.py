### A function that lowercases all letters in a word
###	parameters:
###		string: word
###		string: lang
###


def makeLower(word, lang):

	#Turkish or Azerbaijani special characters
	if 'tr' in lang or 'az' in lang:
		word = word.replace('I','ı')
		word = word.lower()

	#Irish special characters
	irishVowels = ['A','E','I','O','U','Á','É','Í','Ó','Ú']
	if 'ga' in lang and len(word)>1:
		if word[0] == 'n' or word[0] == 't':
			if word[1] in irishVowels:
				word = word[:1] + '-' + word[1:]
		word = word.lower()
	
	#Greek special characters
	if 'el' in lang:
		word = word.lower()
		if word[-1] == 'Σ':
			word = word[:-1]+'ς'


	#Chinese, Japanese, Thai words
	keepSame = ['zh','ja','th']
	if lang in keepSame:
		word = word	

	else:
		word = word.lower()
	

	return word

