# https://www.codewars.com/kata/regexp-basics-parsing-mana-cost/train/python
# not good solution

import re
def parse_mana_cost(mana):
    manaDict = dict()
    if mana == '0' or len(mana) == 0:
        return manaDict
    elif '\n' in mana:
        return None
    regex = re.compile(r'''
    ([0-9]*)
    ([wWuUbBrRgG]*)
    ''',re.VERBOSE)
    mo = regex.findall(mana)
    if bool(mo[0][0]) == False and bool(mo[0][1]) == False:
        return None
    elif len(mana) != len(mo[0][0])+len(mo[0][1]):
        return None
    if len(mo[0][0]) > 0 and int(mo[0][0]) != 0:
        manaDict['*'] = int(mo[0][0])
    lettersList = list(mo[0][1])
    for letter in lettersList:
        if letter.lower() in manaDict:
            manaDict[letter.lower()] += 1
        else:
            manaDict[letter.lower()] = 1
    return manaDict
