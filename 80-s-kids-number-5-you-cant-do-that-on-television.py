# https://www.codewars.com/kata/80-s-kids-number-5-you-cant-do-that-on-television/train/python

import re
def bucket_of(said):
    wetRegex = re.compile(r'(water)(\w+)?|(wet)(\w+)?|(wash)(\w+)?', re.I)
    wetMO = wetRegex.search(said)
    slimeRegex = re.compile(r'(I don\'t know)|(slime)',re.I)
    slimeMO = slimeRegex.search(said)
    if wetMO == None and slimeMO == None:
        return 'air'
    elif  wetMO != None and slimeMO != None:
        return 'sludge'
    elif wetMO != None:
        return 'water'
    elif slimeMO != None:
        return 'slime'
    else:
        return 'air'
