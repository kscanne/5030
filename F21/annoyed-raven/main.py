import csv

capitalized = []
lowercased = []
language_encoding = []

'''
This function opens the tsv file and seperates tests cases into three parts
the language encoding, Capitilazed input, and the suggested Lowercased result
'''
with open("tests.tsv", encoding="UTF-8") as language_tsv:
    language_tsv = csv.reader(language_tsv, delimiter="\t", quotechar='"')
    for row in language_tsv:
        transition = []
        for x in row:
            transition.append(x)
         
        capitalized.append(transition[0])
        language_encoding.append(transition[1])
        lowercased.append(transition[2])       
'''     an easy check to make sure tsv file was seperated correctly
        print(row)
        print(capitalized)
        print(language_encoding)
        print(lowercased)
'''  
# the storage lists of indexes for each occurence of a the specific dialact/language
Encoding_indexesEN= []
Encoding_indexesEN_US= []
Encoding_indexesEN_IE= []
Encoding_indexesEN_LATN= []
Encoding_indexesGA= []
Encoding_indexesGA_IE= []
Encoding_indexesTR= []
Encoding_indexesEL= []
Encoding_indexesZH_HANS= []
Encoding_indexesTH= []

#sorting of each occurance per dialect/language
for i in range(0, len(language_encoding)):
    if language_encoding[i] == "en":
        Encoding_indexesEN.append(i)
    elif language_encoding[i] == "en-US":
        Encoding_indexesEN_US.append(i)    
    elif language_encoding[i] == "en-IE":
        Encoding_indexesEN_IE.append(i)  
    elif language_encoding[i] == "en-Latn":
        Encoding_indexesEN_LATN.append(i)  
    elif language_encoding[i] == "ga":
        Encoding_indexesGA.append(i)  
    elif language_encoding[i] == "ga-IE":
        Encoding_indexesGA_IE.append(i)  
    elif language_encoding[i] == "tr":
        Encoding_indexesTR.append(i)  
    elif language_encoding[i] == "el":
        Encoding_indexesEL.append(i)  
    elif language_encoding[i] == "zh-Hans":
        Encoding_indexesZH_HANS.append(i)  
    elif language_encoding[i] == "th":
        Encoding_indexesTH.append(i)  


# final sorting and printing of words
# still missing exceptions
for j in Encoding_indexesEN:
    instance_en = []
    instance_en.append(capitalized[j].lower())
    print(instance_en)
for j in Encoding_indexesEN_US:
    instance_en_us = []
    instance_en_us.append(capitalized[j].lower())
    print(instance_en_us)
for j in Encoding_indexesEN_IE:
    instance_en_ie = []
    instance_en_ie.append(capitalized[j].lower())
    print(instance_en_ie)
for j in Encoding_indexesEN_LATN:
    instance_en_latn = []
    instance_en_latn.append(capitalized[j].lower())
    print(instance_en_latn)
for j in Encoding_indexesGA:
    instance_ga = []
    instance_ga.append(capitalized[j].lower())
    print(instance_ga)
for j in Encoding_indexesGA_IE:
    instance_ga_ie = []
    instance_ga_ie.append(capitalized[j].lower())
    print(instance_ga_ie)
for j in Encoding_indexesTR:
    instance_tr = []
    instance_tr.append(capitalized[j].lower())
    print(instance_tr)
for j in Encoding_indexesEL:
    instance_el = []
    instance_el.append(capitalized[j].lower())
    print(instance_el)
for j in Encoding_indexesZH_HANS:
    instance_zh_hans = []
    instance_zh_hans.append(capitalized[j].lower())
    print(instance_zh_hans)
for j in Encoding_indexesTH:
    instance_th = []
    instance_th.append(capitalized[j].lower())
    print(instance_th)