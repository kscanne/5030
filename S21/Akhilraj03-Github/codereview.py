## Main Code for Lower case Conversion for all Languages dynamically

## Defining a Funtion to convert the Upper case letters to Lower case letters with word and langauge variables

def UpperCaseToLowerCaseConverter(word,language):
	word=word
	language=language
		
		## Lower Case Convertion language of English and other languages extensions of english

		if(language=='english' or language=='en' or language=='en-US' or language=='en-Latn' or language=='en-Latin' or language=='en-IE' or language=='English'):
			for letter in word:
				letter=word.lower() 		## Convert Each letter to lower case letter
			string=letter
			print(string)				## Printing word output
			print(string.islower()) 		## Checking whether the coversion for English is Sucessful or not
		
		## Lower Case Conversion for Turkish & Azerbaijani languages

		if(language=='turkish' or language=='tr' or language=='azerbaijani' or language=='az' or language=='Turkish' or language=='Azerbaijani'):
			
            string = ""
            for letter in word:
                string += letter 
				if(letter=='i' or letter=='I'):
					I=u"\u0131"
					print(I,end='')
				else:
					print(letter.lower(),end='')

		    print(string.islower())		
			
		## Lower Case Conversion for Greek language

        if(language=='greek' or language=='el' or language=='Greek'):
            length = len(word) - 1
			for i in range(length):
				if(word[i]=='Σ'):
					I=u"\u03A3"
					print(I,end='')
				else:
					print(word[i].lower(),end='')
			if(word[-1]=='Σ'):
				I=u"\u03C2"
				print(I,end='')

			string=word
			print(string.islower())

		## Lower Case Conversion language of Irish and it's other language extension of Irish

		if(language=='irish' or language=='ga' or language=='ga-IE' or language=='Irish'):
			 
			 if (word[0]=='n' or word[0]=='t'):
			 	if(word[1]=='A' or word[1]=='E' or word[1]=='I' or word[1]=='O' or word[1]=='U' or word[1]=='Á' or word[1]=='É' or word[1]=='Í' or word[1]=='Ó' or word[1]=='Ú'):
					print(word[0].lower()+'-'+word[1].lower(),end='')
					print(word[2:].lower())
			else:
				print(word.lower())
			string=word
			print(string.islower())

		## Lower Case Conversion for Thai language

		if(language=='th' or language=='thai' or language=='Thai'):
			for letter in word:
				letter=word.lower()
			string=letter
			print(string)
			print(string.islower())

		## Lower Case Conversion for Chinese language

		if(language=='chinese' or language=='zh-Hans' or language=='Chinese'):
			for letter in word:
                letter=word.lower()
			string=letter
            print(string)
            print(string.islower())

		## Lower Case Conversion for Japanese language

		if(language=='japanese' or language=='ja' or language=='Japanese'):
            for letter in word:
                letter=word.lower()
			string=letter
            print(string)
            print(string.islower())

		## Lower Case Conversion for Mongolian language

		if(language=='Mongolian' or language=='mn' or language=='mn-Cyrl' or language=='mongolian'):
            for letter in word:
                letter=word.lower()
			string=letter
            print(string)
			print(string.islower())
