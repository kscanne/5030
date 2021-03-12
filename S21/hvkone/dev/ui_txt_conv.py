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
if lang_code == 'ga' and (usr_word.startswith('t') or usr_word.startswith('n')) and usr_word[1] in ['A','E','I','O','U','Á','É','Í','Ó','Ú']:
    conv_word = '-'.join([usr_word[0],usr_word[1:]])
    print('Hyphenated Lowercase Conversion: ', conv_word.lower())
else:
    conv_word = usr_word_code.lower()
    print('Lowercase Conversion: ', conv_word)
