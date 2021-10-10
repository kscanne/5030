#%%
import pandas as pd
from json import loads

# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True 
    else: 
        return False

# Funtion returns triangle type
def traingle_type(a,b,c):
    if is_valid_triangle(a,b,c):
        if a == b == c:
            return "equilateral"
        elif a==b or b==c or c==a:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "error"

if __name__ == "__main__":

    df = pd.read_csv("myers.tsv", sep='\t', header=None)
    for (i,output) in zip(df.iloc[:,0],df.iloc[:,1]):
        print("Function Output: " +
              traingle_type(loads(i)['a'],loads(i)['b'],loads(i)['c']) +
              "\tExpected: " + output
            )
        
# %%
