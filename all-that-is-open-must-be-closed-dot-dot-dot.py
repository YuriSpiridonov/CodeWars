# https://www.codewars.com/kata/all-that-is-open-must-be-closed-dot-dot-dot/train/python
# 2.7

import re
def is_balanced(source, caps):
    source = re.sub(r'[a-zA-Z0-9\s!?,]', '', source)       
    while len(source) > 1:
        length = len(source)
        source = re.sub(r'\(\)|\[\]|\{\}|\-\-|@@', '', source)
        if length == len(source):
            break    
    if caps == '' or len(source) == 0:
        return True
    else:
        return False 
