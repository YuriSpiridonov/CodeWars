# https://www.codewars.com/kata/molecule-to-atoms/train/python

import re
def replacer(match):
    regex = re.compile(r'([A-Z][a-z]?)(\d+)?')
    mo = regex.findall(match)
    number = re.search(r'(?<=[\)\]\}])\d', match)
    match = ''
    for i in range(len(mo)):
        if number is None:
            match += mo[i][0]+mo[i][1]
            continue
        if mo[i][1].isdigit() is False:
            match += mo[i][0]+str(1*int(number.group()))
        else:
            match += mo[i][0]+str(int(mo[i][1])*int(number.group()))        
    return match
    
def parse_molecule(formula):
    moleculaDict = dict()
    formula = re.sub(r'\(.*?\)\d?', lambda mo: replacer(mo.group()), formula)
    formula = re.sub(r'\[.*?\]\d?', lambda mo: replacer(mo.group()), formula)
    formula = re.sub(r'\{.*?\}\d?', lambda mo: replacer(mo.group()), formula)
    regex = re.compile(r'([A-Z][a-z]?)(\d+)?')
    mo = regex.findall(formula)
    for element in mo:
        if element[0] in moleculaDict.keys():
            if element[1].isdigit() is False:
                moleculaDict[element[0]] += 1 
                continue
            moleculaDict[element[0]] += int(element[1])
        if element[1].isdigit() is False:
            moleculaDict[element[0]] = moleculaDict.get(element[0], 1)
            continue
        moleculaDict[element[0]] = moleculaDict.get(element[0], int(element[1]))
    return moleculaDict
