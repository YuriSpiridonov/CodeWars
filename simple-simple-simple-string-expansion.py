# https://www.codewars.com/kata/simple-simple-simple-string-expansion/train/python

import re
def string_expansion(s):
    result = str()
    regex = re.compile(r'(\d)?([a-zA-Z]+)+')
    mo = regex.findall(s)
    print(mo)
    for item in mo:
        if len(item[1]) > 1:
            lst = list(item[1])
            for letter in lst:
                if item[0] == '': 
                    number = 1
                else:
                    number = item[0]
                letters = letter*int(number)
                result += ''.join(letters)
        else:
            if item[0] == '': 
                number = 1
            else:
                number = item[0]
            letters = item[1]*int(number)
            result += ''.join(letters)
    return result 
    
print(string_expansion('cvyb239bved2dv'))
print(string_expansion('3abc'),'aaabbbccc')
print(string_expansion('3D2a5d2f'),'DDDaadddddff')
print(string_expansion('0d0a0v0t0y'),'')
print(string_expansion('3d332f2a'),'dddffaa')
print(string_expansion('abcde'),'abcde')
