# https://www.codewars.com/kata/valid-parentheses/train/python

import re
def valid_parentheses(string):
    string = string.strip(' ')
    string = re.sub(r'\w+', '', string)
    while '()' in string:
        string = re.sub(r'\(\)', '' , string)
    return bool(len(string) == 0)
    
print(valid_parentheses(" wlaby(r(dr))ayhkm"),True)    
