import pandas as pd

fs = "\t"
table = str.maketrans('\t', fs)

fName = 'tests.csv'
file_read = pd.read_csv(fName, sep = '\t')

# f = open(fName,'r')
# with open(fName,'r') as tsv:
#     word_input = (col[1])
#     lang_input = (col[2])
#     exp_output = (col[3]);  

# try:
#   line = f.readline()
#   while line:
#     print(line.translate(table), end = "")
#     line = f.readline()

# except IOError:
#   print("Could not read file: " + fName)

# finally:
#   f.close()