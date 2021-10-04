import csv

diacritic_file = open('diacritics - Sheet1.csv', encoding='utf-8')
csvreader = csv.reader(diacritic_file)

lowercase_diacritics = []
uppercase_diacritics = []

for row in csvreader:
    uppercase_diacritics.append(row[0])
    lowercase_diacritics.append(row[1])

diacritic_file.close()

def isLowercaseDiacritic(char):
    if char in lowercase_diacritics:
        return True
    else:
        return False

def isUppercaseDiacritic(char):
    if char in uppercase_diacritics:
        return True
    else:
        return False

def isDiacritic(char):
    if char in lowercase_diacritics or char in uppercase_diacritics:
        return True
    else:
        return False

def convertToLowercaseDiacritic(char):
    lowercase_char = lowercase_diacritics[uppercase_diacritics.index(char)]

    return lowercase_char

def convertToUppercaseDiacritic(char):
    uppercase_char = uppercase_diacritics[lowercase_diacritics.index(char)]

    return uppercase_char