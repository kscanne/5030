# -*- coding: utf-8 -*-

# test - lower module 
# Developers: Mahdi Rahbar
# License: -


import lower

def get_test_file(path = 'tests.tsv'):
    '''
        This function gets a path directory address as 
            the input, reads the data and returns a list 
            of values. 

        input: string - path of saved testing data 
        output: word - lang - lowered word 
    '''
    with open(path, encoding='utf-8') as f: 
        test_data = f.readlines()
    for i in range(len(test_data)):
        test_data[i] = test_data[i].strip().split()
    
    return test_data 

def evaluate(test_data):
    '''
        This function gets a list of test conditions 
            and perform the functions in the class one 
            by one and raise error in case of contradiction.

        input: list of lists 
        output: None
    '''
    for l in test_data:
        lower_obj = lower.Lower(l[0], l[1])
        output = lower_obj.call_lower()
        assert output == l[2], """
        The output value is not what expected,expected: {}, but received: {}""".format(l[2], output)

    print("The test has done successfuly!")



if __name__ == "__main__":
    test_data = get_test_file()
    evaluate(test_data)
