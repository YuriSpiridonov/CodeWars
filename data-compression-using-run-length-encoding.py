# https://www.codewars.com/kata/data-compression-using-run-length-encoding/train/python

def encode(string):
    decoded = dict()
    result = str()
    for letter in string:
        if bool(decoded) == False or letter in decoded.keys():
            decoded[letter] = decoded.get(letter, 0)+1
        elif letter not in decoded.keys():
            for key, value in decoded.items():
                result += str(decoded[key])+key 
            decoded.clear()
            decoded[letter] = decoded.get(letter, 0)+1
    if bool(decoded) != False:
        for key, value in decoded.items():
                result += str(decoded[key])+key    
    return result

import re
def decode(string): 
    string = re.sub(r'(\d+)(\w)', lambda mo : mo.group(2)*int(mo.group(1)), string)
    return string
