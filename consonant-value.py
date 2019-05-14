# https://www.codewars.com/kata/consonant-value/train/python

import re
def solve(s):
    dic = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 
    'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 
    'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
    regex = re.compile(r'[^aeiou]*')
    mo = regex.findall(s)
    lst = list()
    for element in mo:
        if element != '' and len(element) > 1:
            ele = list(element)
            for key, value in dic.items():         
                while key in ele:
                    ele[ele.index(key)] = value
            lst.append(sum(ele))
        elif element != '' and len(element) == 1:
            for key, value in dic.items():
                lst.append(value)
    return max(lst)
