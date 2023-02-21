#!/usr/bin/env python
# coding: utf-8

# In[4]:


import unicodedata

def lc (word, language):

    # Check if language is Chinese, Japanese, or Thai, and return original word unchanged.
    if language.startswith("zh") or language.startswith("ja") or language.startswith("th"):
        return word

    # Check if language is Turkish or Azerbaijani and replace 'I' with 'ı'.
    if language.startswith("tr") or language.startswith("az"):
        return word.replace("I", "ı")

    # Check if language is Irish and insert hyphen in specific cases.
    if language.startswith("ga"):
        if word.startswith("n"):
            next_letter = word[1:2]
            if next_letter in ("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"):
                return "n-" + word[1:].lower()
        elif word.startswith("t"):
            next_letter = word[1:2]
            if next_letter in ("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"):
                return "t-" + word[1:].lower()

    # Check if language is modern Greek and handle final sigma.
    if language.startswith("el"):
        if word.endswith("Σ") or word.endswith("ς"):
            return word[:-1] + "ς"

    # Check if language is English and handle en-Latn
    if language.startswith("en") and language.endswith("-Latn"):
        return word.lower()

    # Check if language is Thai and handle th
    if language == "th":
        return word

    # For all other cases, simply use the built-in lower() method.
    return word.lower()

with open('tests.tsv', encoding="utf8") as f:
      for line in f:
        word, language, expected = line.strip().split('\t')
        actual = lc(word, language)
        #actual = actual.islower()
        if actual != expected:
            print(f'Test case failed. Expected "{expected}" when lowercasing "{word}" in language "{language}" but got "{actual}".')
            
#Testing            
assert lc ("你好", "zh-CN") == "你好", "Test case failed"
print("passed")

assert lc("WORLD", "eng") == "world", "Test case failed"
print("passed")

assert lc ("HELLO-WORLD", "en") == "hello world", "Test case failed"
print("passed")

assert lc("官话", "zh-Hans") == "官话", "Test case failed"
print("passed")

assert lc("nÕg", "ga-IE") == "nõg", "Test case failed"
print("passed")


# In[ ]:




