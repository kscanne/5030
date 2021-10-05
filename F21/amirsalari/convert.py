def convert(test_word):
    if(test_word[1] in ["en", "en-US", "en-IE", "en-Latn"]):
        lowercase_word = test_word[0].lower()
        return lowercase_word

    if(test_word[1] in ["tr", "az"]):
        lowercase_word = test_word[0]
        lowercase_word = lowercase_word.replace('\u0049', '\u0131')  # I ı
        lowercase_word = lowercase_word.replace('\u011E', '\u011F')  # Ğ ğ
        lowercase_word = lowercase_word.replace('\u00C7', '\u00E7')  # Ç ç
        lowercase_word = lowercase_word.replace('\u00D6', '\u00F6')  # Ö ö
        lowercase_word = lowercase_word.replace('\u00DC', '\u00FC')  # Ü ü
        lowercase_word = lowercase_word.replace('\u015E', '\u015F')  # Ş ş
        lowercase_word = lowercase_word.lower()
        return lowercase_word

    if(test_word[1] in ["ga", "ga-IE"]):
        lowercase_word = test_word[0]
        first = test_word[0][0]
        second = test_word[0][1]
        first_letters = ['n', 't']
        second_letters = ['A', 'E', 'I', 'O', 'U',
                          '\u00C1', '\u00C9', '\u00CD', '\u00D3', '\u00D5', '\u00DA']
        if (first in first_letters):
            '''Unicode	Upper   Unicode	    	Lower	Character Name
                00C1	Á	    00E1	        á	        A acute
                00C9	É	    00E9	        é	        E acute
                00CD	Í	    00ED	        í	        I acute
                00D3	Ó	    00F3	        ó	        O acute
                00D5	Õ	    00F5	        ó	        O acute
                00DA	Ú	    00FA	        ú	        U acute'''

            if(second in second_letters):
                lowercase_word = lowercase_word.lower()
                lowercase_word = lowercase_word[:1] + "-" + lowercase_word[1:]

                if(second == '\u00C1'):  # Á   á
                    lowercase_word[2] = '\u00E1'

                if(second == '\u00C9'):  # É   é
                    lowercase_word[2] = '\u00E9'

                if(second == '\u00CD'):  # Í   í
                    lowercase_word[2] = '\u00ED'

                if(second == '\u00DA'):  # Ú    ú
                    lowercase_word[2] = '\u00FA'

                if(second == '\u00D5'):  # Õ    ó
                    lowercase_word = lowercase_word[:2] + \
                        '\u00F5' + lowercase_word[3:]

                if(second == '\u00D3'):  # Ó    ó
                    lowercase_word = lowercase_word[:2] + \
                        '\u00F3' + lowercase_word[3:]
        else:
            lowercase_word = lowercase_word.lower()
        return lowercase_word

    if(test_word[1] in ["el"]):
        lowercase_word = test_word[0]
        if(lowercase_word[-1] == '\u03A3'):  # index -1 means last element in the array
            # if the char is Σ Greek Capital Letter Sigma
            lowercase_word = lowercase_word[:-1] + '\u03C2'

        lowercase_word = lowercase_word.lower()
        return lowercase_word

    if(test_word[1] in ["zh", "ja", "th", "zh-Hans"]):
        return test_word[0]


def open_file(file_name):
    f = open(file_name, encoding="utf-8")
    lines_text = []
    pieces_text = []
    for line in f:
        line = line.rstrip('\n')
        lines_text.append(line)
        pieces = line.split('\t')
        pieces_text.append(pieces)
    return pieces_text


def close_file(file_name):
    f = open(file_name, encoding="utf-8")
    f.close()


# print("Enter file path: ")  # tests.tsv

# file_path = input()
file_path = 'tests.tsv'
test_file = open_file(file_path)

for iteration, item in enumerate(test_file):
    if (item[2] != convert(item)):
        print("In Line: ", iteration, ",test case failed for: ",
              item, ". The correct lowercase word is: ", convert(item), "\n")

close_file(file_path)
