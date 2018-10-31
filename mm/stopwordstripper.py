#Imports
import csv
import sys

#Main function.
def main():
    #load the tsv with unit tests.
    with open('cases_updated.tsv','rb') as tsvin, open ('cases_tested.tsv','wb') as tsvout:
        tsvin = csv.reader(tsvin,delimiter='\t')
        tsvout = csv.writer(tsvout,delimiter='\t')

        #Iterate through rows in cases.tsv.
        for row in tsvin:
            strippedline = stopwords(row[0],row[1])     
            tsvout.writerow([row[0],row[1],strippedline])
            #Use assert to check results.
            assert strippedline == row[2]

#Function to test for non-english characters.
def isenglish(stringin):
    try:
        stringin.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

#Function to test stop words in input string.
def stopwords(langcode,checkline): 
    #Load checkline into list.
    checkline = checkline.split()
    #Define stopdict (for loading in stop word dictionaries).
    stopdict = []
    largestopdict = []
    #Define stripped (checkline after going through selective stripping).
    strippedlist = []
    #Define englishlist final list.
    englishlist = []
    #Define dictionary (text file) to load based on langcode.
    if (langcode == "en"):
        with open("en.txt","r") as file:
            for line in file:
                line = line.strip()
                stopdict.append(line)
    elif (langcode == "fr"):
        with open("fr.txt","r") as file:
            for line in file:
                line = line.strip()
                stopdict.append(line)
    elif (langcode == "ga"):
        with open("ga.txt","r") as file:
            for line in file: 
                line = line.strip()
                stopdict.append(line)
    elif (langcode == "gd"):
        with open("gd.txt","r") as file:
            for line in file:
                line = line.strip()
                stopdict.append(line)
    elif (langcode == "gv"):
        with open("gv.txt","r") as file:
            for line in file:
                line = line.strip()
                stopdict.append(line)
    elif (langcode == "ru"):
        with open("ru.txt","r") as file:
            for line in file:
                line = line.strip()
                stopdict.append(line) 
    else:
        for item in checkline:
            strippedlist.append(item)
    #Add upper and lower case versions of each line in stopdict to largestopdict.
    for item in stopdict:
        if isenglish(item):
            for letter in range(len(item)):
                convertcase = item[:letter] + item[letter].swapcase() + item[(letter+1):]
                largestopdict.append(convertcase)
    #Add all capital letter version of each line in stopdict to largestopdict.
    for item in stopdict:
        if isenglish(item):
            largestopdict.append(item.upper())
    #Add the original items of stopdict to largestopdict.
    for item in stopdict:
        largestopdict.append(item) 
    #Check to see if any of the words are fully contained.
    for item in checkline:
        if not (item in string for string in largestopdict):
            strippedlist.append(item) 
        elif not (string in item for string in largestopdict):
            strippedlist.append(item)
        elif item not in largestopdict:
            strippedlist.append(item)
    if not strippedlist:
        strippedlist.append("") 
    strippedstr = " ".join(strippedlist)
    return strippedstr
if __name__ == "__main__":
    main()
