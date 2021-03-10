fs="\t"
table = str.maketrans('\t', fs)
fName = 'tests.tsv'
f = open(fName,'r')

try:
  line = f.readline()
  while line:
    print(line.translate(table), end = "")
    line = f.readline()

except IOError:
  print("Could not read file: " + fName)

finally:
  f.close()