# https://www.codewars.com/kata/add-commas-to-a-number-1/train/python

import re
def commas(num):
    num = round(num,3) 
    regex = re.compile(r'(-?\d+)(\.\d+)?')
    mo = regex.findall(str(num))
    lst = list(mo[0][0])
    lencount = len(lst)//3
    y = 3
    returnNumber = str()
    if len(lst)<=3:
        returnNumber = ''.join(lst)
    else:
        for x in range(lencount):
            lst.insert(-y,',')
            y+=4
    if lst[0]==',':
        lst.pop(0)
    if lst[0]=='-' and  lst[1]==',':
        lst.pop(1)    
    returnNumber = ''.join(lst)
    if mo[0][1] != '.0':
        returnNumber += ''.join(mo[0][1])
    return returnNumber
