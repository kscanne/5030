# -*- coding: utf-8 -*-

# lower
# Developers: Mahdi Rahbar
# License: - 


import lower

if __name__ == "__main__":
    text = input("Please enter the sentence you want to lower case: \n\n")
    lang = input("Please enter your desired language short code (you can look up your desired language short code online - hint: English's short code is \'en\')\n")
    lower = lower.Lower(text, lang)
    print("Your chosen language is: ",lower.lang, "\nYour converted text is: ", lower.call_lower())

