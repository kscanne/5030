# pip install langdetect
# pip install translate

from langdetect import detect
from translate import Translator

usr = input('Type Word Here: ')
# usr_caps = usr.upper()
# print('Input: ', usr_caps)

lang = detect(usr)
print('Language Detected: ', lang)

trans = Translator(from_lang = lang, to_lang = "english")
conv_low = trans.translate(usr)
print('Lowercase Conversion: ', conv_low)