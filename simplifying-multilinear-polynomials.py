# https://www.codewars.com/kata/simplifying-multilinear-polynomials/train/python

import re
def simplify(poly):
    polyDict = dict()
    digitSortDict = dict()
    alphaSortDict = dict()
    lst = list()
    regex = re.compile(r'''
    ([+-])?(\d+)?([a-z]+)
    ''', re.VERBOSE)
    mo = regex.findall(poly)
    for element in mo:
        if element[0] == '+' or element[0] == '':
            if element[1] == '':
                polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) + 1
            else:
                polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) + int(element[1])
        else:
            if element[1] == '':
                polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) - 1
            else:
                polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) - int(element[1])
    for key in sorted(polyDict):
        alphaSortDict[key] = polyDict[key]
    for key in sorted(alphaSortDict, key=len):
        digitSortDict[key] = alphaSortDict[key]
    for key, value in digitSortDict.items():
        if value < -1:
            lst.append(str(value)+key)
        elif value == -1:
            lst.append('-'+key)
        elif value == 0:
            continue
        elif value == 1:
           lst.append('+'+key)
        else:
            lst.append('+'+str(value)+key)
    return ''.join(lst).lstrip('+') 
    
print(simplify("xzy+zby"))
print(simplify("-a+5ab+3a-c-2a"),"-c+5ab") 
print(simplify("-abc+3a+2ac"),"3a+2ac-abc")
