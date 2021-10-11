# -*- coding: utf-8 -*-

# myers test
# Developers: Mahdi Rahbar
# License: - 

import re 
import ast 
  
def is_triangle(a, b, c):
    error = 'error'
    scalene = 'scalene'
    isosceles = 'isosceles'
    equilateral = 'equilateral'
    input_num = [a,b,c]
    sorted_input = sorted(input_num)  

    if sorted_input[0]+sorted_input[1]< sorted_input[2]:
        print("InputError: The input lengths, can not compromise a triangle! Please enter another set of inputs!")
        return 'error'
    if sorted_input[0] == sorted_input[1] :
        if sorted_input[1] != sorted_input[2]: 
            return isosceles
        if sorted_input[1] == sorted_input[2]: 
            return equilateral
    if sorted_input[1] == sorted_input[2] :
        if sorted_input[0] != sorted_input[1]: 
            return isosceles
        if sorted_input[0] == sorted_input[1]: 
            return equilateral
    else: 
        return scalene

def test_is_triangle(a, b, c, actual_status):
    output_status = is_triangle(a, b, c)
    assert actual_status == output_status, \
            """The output status is not what expected. 
            Expected {}, but got {}.""".format(output_status,actual_status)
        
    



if __name__ == "__main__":
    with open('myers.tsv', encoding = 'utf-8') as f:
        test_data = f.read()
        test_data = test_data.strip('\n').split('\n')
        for i in range(len(test_data)):
            test_data[i] = test_data[i].split('\t')
            test_data[i][0] =  ast.literal_eval(test_data[i][0]) 
        for i in range(len(test_data)):
            test_is_triangle(*test_data[i][0].values(), test_data[i][1])


