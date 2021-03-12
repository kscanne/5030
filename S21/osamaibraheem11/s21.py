import csv

irishVowels = ["A","E","I","O","U","Á","É","Í","Ó","Ú"]

def LowerCase(word,language): 
    if ('ga' == language or 'ga-IE' == language) and (word.startswith('n') or word.startswith('t')) and word[1:2] in irishVowels:
        return word[:1].lower()+"-"+word[1:].lower()
    elif ('tr' == language):
        return word.replace('I',"ı").lower()
    elif ("az" == language):
        return word.replace('I',"ı").lower()
    elif ('el' == language):
        if word.endswith('Σ'):
            return word[:-1].lower() + "ς"
        else:
            return word[:-1].lower() + "σ"
    else:
        return word.lower()
read_tsv = csv.reader(open("tests.tsv",encoding = "utf8" ), delimiter="\t") 
for row in read_tsv: 
  word, language, answer = row
  LowerCaseWord = LowerCase(word,language)
  if LowerCaseWord == answer: 
    print("Passed")
  else:
    print(f"Failed, this was expected output {row[2]}, this what you put out {LowerCaseWord} and lan was {row[1]}")