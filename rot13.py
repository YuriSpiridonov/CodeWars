# https://www.codewars.com/kata/rot13/train/python

import re
def replacer(letter):
    if ord(letter) in range (65, 91):
        if ord(letter)+13 > 90:
            letter = chr(65+ord(letter)+12-90)
        else:
            letter = chr(ord(letter)+13)
    elif ord(letter) in range (97, 123):
        if ord(letter)+13 > 122:
            letter = chr(97+ord(letter)+12-122)
        else:
            letter = chr(ord(letter)+13)        
    return letter        
        
def rot13(message):
    message = re.sub(r'\w', lambda mo : replacer(mo.group()), message)
    return message
