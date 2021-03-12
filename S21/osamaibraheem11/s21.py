import csv

def LowerCase(word,language): 
  if "en" in language:
    return word.lower()
  elif "tr" or "az" in language:
    return word.replace('I',"ı").lower()
  elif "ga" in language:
    return word[:1].lower()+"-"+word[1:].lower()
  elif "el" in language:
    if word.endswith('Σ'):
      return word.replace('Σ',"ς").lower()
    else:
      return word.replace('Σ',"σ").lower()
  else:
    word.lower()
read_tsv = csv.reader(open("tests.tsv"), delimiter="\t") 
for row in read_tsv: 
  word, language, answer = row
  LowerCaseWord = LowerCase(word,language) 
  if LowerCaseWord == answer: 
    print("Passed")
  else:
    print(f"Failed, this was expected output {row[2]}, this what you put out {LowerCaseWord} and lan was {row[1]}")