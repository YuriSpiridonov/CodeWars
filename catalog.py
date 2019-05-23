# https://www.codewars.com/kata/catalog/train/python

import re
def catalog(s, article):
    match = str()
    s = s.split('\r\n')
    regex = re.compile(r'([\w\s]*?'+article+'[\w\s]*?)</name><prx>(\d*\.?\d*?)</prx><qty>(\d*\.?\d*?)')
    for string in s:
        mo = regex.findall(string)
        if mo:
            for i in range(len(mo)):
                match += '{} > prx: ${} qty: {}\r\n'.format(mo[i][0],mo[i][1],mo[i][2])
        else:
            match = 'Nothing'
    return match.rstrip('\r\n')
