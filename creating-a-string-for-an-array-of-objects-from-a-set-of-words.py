# https://www.codewars.com/kata/creating-a-string-for-an-array-of-objects-from-a-set-of-words/train/python

import re
def words_to_object(s):
    fullStr = str()
    regex = re.compile(r'(\S+)\s(\S+)') # list of tuples (key, value)
    mo = regex.findall(s)
    for i in range(len(mo)):
        partStr = ''.join("{name : '"+mo[i][0]+"', id : '"+mo[i][1]+"'}")
        fullStr= fullStr + partStr  + ', ' 
    fullStr = '[' + fullStr[:-2] + ']'
    return fullStr
