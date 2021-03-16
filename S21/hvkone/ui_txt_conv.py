#---------------------------------
# DEPENDECIES
#---------------------------------
# pip install langdetect
from langdetect import detect

# pip install translate
from translate import Translator

# pip install pycountr
import pycountry

# pip install bcp47
from bcp47 import bcp47

# pip install langcodes
# pip install language_data
from langcodes import *


def convert_to_ascii(text):
    return " ".join(str(ord(char)) for char in text)
#---------------------------------
# START OF CODE
#---------------------------------
usr_word = input('Type Word (to be converted to lowercase): ')

usr_word_code = usr_word.encode(encoding = 'UTF-8',errors = 'strict')
print('UTF-8 Input: ', usr_word_code)

usr_asc = convert_to_ascii(usr_word)
print('ORIGINAL ASCII INPUT: ', usr_asc)
# Convert to lowercase using ASCII 
usr_asc_new = ''
for i in range(len(usr_word)):
    if(usr_word[i] >= 'A' and usr_word[i] <= 'Z'):
        usr_asc_new = usr_asc_new + chr((ord(usr_word[i]) + 32))
    else:
        usr_asc_new = usr_asc_new + usr_word[i]
usr_asc_new = convert_to_ascii(usr_asc_new)       
print('CONVERTED ASCII OUTPUT: ', usr_asc_new)

usr_lang = input('Type Language Code [en]: ')
usr_regn = input('Type Region Code [US]: ')

# CHECK FOR REGION INPUT
if len(usr_regn) == 0:
    print('No Region Was Selected')
    lang_code = usr_lang
else:
    lang_code = '-'.join([usr_lang,usr_regn])
    # print('Region Selected: ', usr_regn)

# DETERMINE LANGUAGE CODE WITH REGION
lang_code = standardize_tag(lang_code)
print('Language Code: ', lang_code)

# DETERMINE FULL LANGUAGE NAME
lang_name = Language.make(language = lang_code).display_name()
print('Language Name: ', lang_name)

#---------------------------------
# LANGUAGE CONDITIONALS
#---------------------------------

# IF GAELIC INPUT
if (lang_code[:] in ['ga','ga-IE']) and (usr_word.startswith('t') or usr_word.startswith('n')) and (usr_word[1] in ['A','E','I','O','U','Á','É','Í','Ó','Ú']): 
    conv_word = '-'.join([usr_word[0],usr_word[1:]])
    print('Hyphenated Lowercase Conversion: ', conv_word.lower())

# IF TURKISH INPUT
elif (lang_code[:] in ['tr']) and usr_word[:] in ['I']:
    # still working on conversion to Latin dotless i...
    conv_rep = usr_word.replace('I', ('c4b1'.decode('utf-8'))) # find uppercase letter and replace
    conv_word = conv_rep
    print('TURKISH Lowercase Conversion: ', conv_word.lower())

# IF GREEK INPUT
elif lang_code == 'el' and usr_word[:] in ['Π','Ό','Λ','Η','Σ']: 
    if usr_word[-1] in ['Σ']:
        conv_sig = usr_word.replace('Σ','ς')
    else:
        conv_sig = usr_word.replace('Σ','σ')
    conv_rep = usr_word.replace(['Π','π'] or ['Ό','ό'] or ['Λ','λ'] or ['Η','η']) # find uppercase letters and replace
    conv_word = conv_rep
    print('GREEK Lowercase Conversion: ', conv_word.lower())

# IF CHINESE and OTHER INPUT
elif lang_code[:] in ['zh','th']:
    conv_word = usr_word # letters are the same in both cases
    print('SYMBOL Lowercase Conversion: ', conv_word.lower())


else:
    conv_word = usr_word.lower()
    print('STANDARD Lowercase Conversion: ', conv_word)