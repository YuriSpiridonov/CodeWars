# https://www.codewars.com/kata/molecule-to-atoms/train/python
# all wrong check after resolve!

import re
def parse_molecule (formula):
    moleculaDict = dict()
    regex = re.compile(r'''
    ([A-Z][a-z]?)(\d)?#((?<=\))\d)?((?<=\])\d)?
    ''',re.VERBOSE)
    mo = regex.findall(formula)
    print(mo)
    bracketsRegex = re.compile(r'''
    \(([A-Z][a-z]?)
    ''',re.VERBOSE)
    mo2 =  bracketsRegex.findall(formula)
    bracketsRegex2 = re.compile(r'''
    \[(.*)\](\d)
    ''',re.VERBOSE)
    mo3 =  bracketsRegex2.search(formula)
    print(mo2)
    for i in range(1,len(mo)+1):
        if mo[-i][1] == '':
            mo[-i] = (mo[-i][0], 1)
            continue
        else:
            continue
    for i in range(1,len(mo)+1):    
        if mo2:
            print(mo2.group(2))
            if mo[-i][0] in mo2.group():
                print(mo[-i][0])
                mo[-i] = (mo[-i][0], int(mo[-i][1])*int(mo2.group(2)))
                moleculaDict[mo[-i][0]] = 0+int(mo[-i][1])*int(mo2.group(2))
    for element in mo:
        moleculaDict[element[0]] = moleculaDict.get(element[0], element[1])
        if element[1]:
            moleculaDict[element[0]] = int(element[1])
            
    
        
print(parse_molecule("K4[ON(SO3)2]2"))#, {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")
#print(parse_molecule("H2O"))    
#print(parse_molecule("Mg(OH)2"))#, {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
