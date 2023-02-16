import csv

#function converts word to lower case and provides special rules for irish and turkish since they are not covered by the book
def toLower(input_string : str, language: str) -> str:
  irish_vowels = "AEIOUÁÉÍÓÚ"
  tilda_ord = 771
#the following condition for irish uses a conditional lamda function which looks for the following rules 
# - include a hyphen if the first alphabet is T or N and its followed by an irish vowel. It also checks for 
# ord 771 since that means that there is a tild on the second alphabet since that could be achieved by either a singular unicode or by 2 unicodes
# this is the reason we only check at postion[2] since if there is a tilda at [2] it means there can't be a vowel at [1]

  if(language.find("ga") + 1):
    irish_lower = lambda input_string : (input_string[0] + "-" + input_string[1:]).lower() \
                if (input_string[0] == "t" or input_string[0] == "n") and irish_vowels.find(input_string[1]) + 1 \
                and ord(input_string[2]) != tilda_ord  \
                else input_string.lower()

    return irish_lower(input_string)

# Turkish and Azerbaijani follow similar rules to standard covertion with just a different i
  elif((language.find("tr") + 1) or (language.find("az") + 1)):
    return input_string.lower().replace("i", "ı")

  else:
    return input_string.lower()

# Basic Testing
with open("tests.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
      assert toLower(line[0], line[1]) == line[2], "Test Failed for the word " + line[0] 
    print("All the test cases where successful!!")