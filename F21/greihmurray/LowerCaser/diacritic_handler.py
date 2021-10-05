import csv

#Opens csv file
diacritic_file = open('diacritics - Sheet1.csv', encoding='utf-8')
csvreader = csv.reader(diacritic_file)

lowercase_diacritics = []
uppercase_diacritics = []

#Reads all lines of diacritics - Sheet1.csv file and appends each character to appropriate list
for row in csvreader:
    uppercase_diacritics.append(row[0])
    lowercase_diacritics.append(row[1])

#closes csv file
diacritic_file.close()

#Checks to see if provided character is a lowercase diacritic
#Accepts one argument
#char - character to check
def isLowercaseDiacritic(char):
    if char in lowercase_diacritics:
        return True
    else:
        return False

#Checks to see if provided character is a uppercase diacritic
#Accepts one argument
#char - character to check
def isUppercaseDiacritic(char):
    if char in uppercase_diacritics:
        return True
    else:
        return False

#Checks to see if provided character is a diacritic
#Accepts one argument
#char - character to check
def isDiacritic(char):
    if char in lowercase_diacritics or char in uppercase_diacritics:
        return True
    else:
        return False

#Converts provided diacritic to its lowercase equivalent
#Accepts one argument
#char - character to check
def convertToLowercaseDiacritic(char):
    lowercase_char = lowercase_diacritics[uppercase_diacritics.index(char)]

    return lowercase_char

#Converts provided diacritic to its uppercase equivalent
#Accepts one argument
#char - character to check
def convertToUppercaseDiacritic(char):
    uppercase_char = uppercase_diacritics[lowercase_diacritics.index(char)]

    return uppercase_char