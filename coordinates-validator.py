# https://www.codewars.com/kata/coordinates-validator/train/python

import re 
def is_valid_coordinates(coordinates):
    regex = re.compile(r'''
    
    (\-?(90|[0-8]?[0-9])\.?(\d+)?)                         # 1st coord: -? 0-90.0123456789
    (\,\s)                                                 # sep , (with space)
    (\-?(180|1[0-7][0-9]|[0-9]?[0-9])(\.?(\d+)?))$         # 2nd coord: -? 0-180.0123456789
    
    ''', re.VERBOSE)
    mo = regex.match(coordinates)
    if mo != None:
        return True
    else:
        return False 
    
    
print(is_valid_coordinates("-8, 25"))
print(is_valid_coordinates("4, -3"))
print(is_valid_coordinates("224.53525235, 23.45235"))
print(is_valid_coordinates("04, -223.234235"))
print(is_valid_coordinates("43.91343345, 143"))
print(is_valid_coordinates("23.234, - 23.4234"))
print(is_valid_coordinates("2342.43536, 34.324236"))
print(is_valid_coordinates("N23.43345, E32.6457"))
print(is_valid_coordinates("99.234, 12.324"))
print(is_valid_coordinates("6.325624, 43.34345.345"))
print(is_valid_coordinates("0, 1,2"))
print(is_valid_coordinates("0.342q0832, 1.2324"))
print(is_valid_coordinates("23.245, 1e1"))
