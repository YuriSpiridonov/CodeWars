# https://www.codewars.com/kata/convert-pascalcase-string-into-snake-case/train/python

import re    
def to_underscore(string):
    return '_'.join(re.findall(r'[A-Z][a-z0-9]*',string)).lower() if type(string) is str else str(string)
