# https://www.codewars.com/kata/create-four-letter-birding-codes-from-bird-names/train/python

import re
def bird_code(arr):
    birdCode = list()
    regex = re.compile(r'[a-zA-Z\']+')
    for birds in arr:
        mo = regex.findall(birds)
        if len(mo) == 1:
            birdCode.append(mo[0][:4].upper())
        elif len(mo) == 2:
            birdCode.append(mo[0][:2].upper() + mo[1][:2].upper())
        elif len(mo) == 3:
            birdCode.append(mo[0][0].upper() + mo[1][0].upper() + mo[2][:2].upper())
        else:
            birdCode.append(mo[0][0].upper() + mo[1][0].upper() + mo[2][0].upper() + mo[3][0].upper())
    return birdCode
