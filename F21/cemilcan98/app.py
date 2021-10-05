def toLowerCase(i):
    if(i[1] in ["en", "en-US", "en-IE", "en-Latn"]):
        y = i[0].lower()
        return y

    # Checking for the special letters in Turkish and Azeri 
    if(i[1] == "tr" or i[1] == "az"):
        y = i[0]
        y = y.replace('\u011E', '\u011F')
        y = y.replace('\u00C7', '\u00E7')
        y = y.replace('\u00D6', '\u00F6')
        y = y.replace('\u00D3', '\u00FC')
        y = y.replace('\u015E', '\u015F')  
        y = y.replace('\u0049', '\u0131')  # I to ı
        y = y.lower()

        return y

    # Checking for the special cases in Irish
    if(i[1] == "ga" or i[1] == "ga-IE"):
        y = i[0]
        first = i[0][0]
        second = i[0][1]
        first_letters = ['n', 't']
        second_letters = ['A', 'E', 'I', 'O', 'U',
                          '\u00C1', '\u00C9', '\u00CD', '\u00D3', '\u00D3']
        upper_diff_letters = ['\u00C1', '\u00C9',
                              '\u00CD', '\u00D3', '\u00DA']

        lower_diff_letters = ['\u00E1', '\u00E9',
                              '\u00ED', '\u00F3', '\u00FA']

        if (first in first_letters):
            if(second in second_letters):
                y = y.lower()
                y = y[:1] + "-" + y[1:]
                if(second == '\u00C1'):
                    y[2] = '\u00E1'
                if(second == '\u00C9'):
                    y[2] = '\u00E9'
                if(second == '\u00CD'):
                    y[2] = '\u00ED'
                if(second == '\u00DA'):
                    y[2] = '\u00FA'
                if(second == '\u00D3'):
                    y = y[:2] + '\u00F3' + y[3:]
        else:
            y = y.lower()
        return y

    # Greek Cases
    if(i[1] == "el"):
        y = i[0]
        if(y[-1] == '\u03A3'):
            y = y[:-1] + '\u03C2'
        y = y.lower()
        return y

    if(i[1] in ["zh", "ja", "th", "zh-Hans"]):
        y = i[0]
        return y


def open_file(file_name):
    f = open(file_name, encoding="utf8")
    lines_text = []
    pieces_text = []
    for line in f:
        line = line.rstrip('\n')
        lines_text.append(line)
        pieces = line.split('\t')
        pieces_text.append(pieces)
    return pieces_text


def close_file(file_name):
    f = open(file_name, encoding="utf8")
    f.close()


y = open_file('tests.tsv')
for k in y:
    if (k[2] != toLowerCase(k)):
        print("Failed test: ", k)
