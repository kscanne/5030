# pip install langdetect
# pip install translate
# pip install iso-639
# pip install pycountry

from langdetect import detect
from translate import Translator
from iso639 import languages
import pycountry 

usr = input('Type Word Here: ')
# usr_caps = usr.upper()
# print('Input: ', usr_caps)

lang_code = detect(usr)
lang_name = pycountry.languages.get(alpha_2 = lang_code)
print('Language Detected: ', lang_name.name, '[',lang_code,']')

trans = Translator(from_lang = lang_code, to_lang = "english")
conv_low = trans.translate(usr)
print('Lowercase Conversion: ', conv_low)