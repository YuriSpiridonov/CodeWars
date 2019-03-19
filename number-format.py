# https://www.codewars.com/kata/number-format/train/python

import re
def number_format(n):
    regex = re.compile(r'-?\d')
    mo = regex.findall(str(n))
    lencount = len(mo)//3
    y = 3
    returnNumber = str()
    if len(mo)<=3:
        returnNumber = ''.join(mo)
        return returnNumber
    else:
        for x in range(lencount):
            mo.insert(-y,',')
            y+=4
    if mo[0]==',':
        mo.pop(0)
    returnNumber = ''.join(mo)
    return returnNumber
