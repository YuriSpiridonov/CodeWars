# https://www.codewars.com/kata/count-the-smiley-faces/train/python

import re
def count_smileys(arr):
    counter = 0
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        smiles = re.compile(r'(:(\)|D|\~D|\-D|\~\)))|(;(\)|D|\~D|\-D|\~\)))')
        mo = smiles.findall(arr[i])
        if len(mo) == 0:
            continue
        elif len(mo[0][0]) >0 or  len(mo[0][2]) >0:
            counter+=1
    return counter
