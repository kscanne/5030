# pip install python-bcp47
# pip install bcp47
from bcp47 import bcp47

# pip install langcodes
# pip install language_data
from langcodes import *



#------------------------------------
# START OF CODE
#------------------------------------
usr_word = input('Type Word (to be converted to lowercase): ')
usr_lang = input('Type Language Code [en]: ')
usr_regn = input('Type Region Code [US]: ')

# CHECK FOR REGION INPUT
if len(usr_regn) == 0:
    print('No Region Was Selected')
    lang_code = usr_lang
else:
    lang_code = '-'.join([usr_lang,usr_regn])

# DETERMINE LANGUAGE CODE WITH REGION
lang_code = standardize_tag(lang_code)
print('Language Code: ', lang_code)

# DETERMINE FULL LANGUAGE NAME
lang_name = Language.make(language = lang_code).display_name()
print('Language Name: ', lang_name)

# lang_tags = bcp47(lang_code)

# IF GAELIC INPUT
if lang_code == 'ga' and (usr_word.startswith('t') or usr_word.startswith('n')) and usr_word[1] in ['A','E','I','O','U']:
    conv_word = '-'.join([usr_word[0],usr_word[1:]])
    print('Hyphenated Lowercase Conversion: ', conv_word.lower())
else:
    conv_word = usr_word.lower()
    print('Lowercase Conversion: ', conv_word)

