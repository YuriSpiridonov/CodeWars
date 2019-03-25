# https://www.codewars.com/kata/filter-valid-romans/train/python

import re
def valid_romans(arr):
    returnNumbers = list()
    for number in arr:
        romanRegex = re.compile(r'''
        #(1k-4k) (900|400|-500+) (90|40|50 10<>80)(9| 4|5 1-3,6-8)
        ((M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))|
        ''', re.VERBOSE)
        mo = romanRegex.search(number)
        if len(mo.group()) == len(number) and len(mo.group()) > 0:
            returnNumbers.append(mo.group())
        else:
            continue
    return returnNumbers


print(valid_romans(["VI", 'XXIII','XXXIX', 'XLVIII','LIII', 'LXXXIX','XCVIII','C', 'CMXCIX', 'MMMMCMXCIX']))
print(valid_romans(["MMMCDLXVL", "MDLXXXVI", "DCLXII", "MMMMCLL", "MMDCCCLXXXIVCD"]))#, ["MDLXXXVI", "DCLXII"])
print(valid_romans(["MMMMCCCXXXII", "MMDCCCXXVCD", "MMCCCXLV", "DCCLXVIIICD", "MMMMCXII"]))#, ["MMMMCCCXXXII", "MMCCCXLV", "MMMMCXII"])
print(valid_romans(["DCCLIVI", "MDCCXXXVVI", "MDLXXVI", "MDVIL", "MCCLXIII"]))#, ["MDLXXVI", "MCCLXIII"])
print(valid_romans(["DV", "", "CLVIII", "MDCCCXXCD", "MDCLXVI", "MMMDCCCLXXXVI"]))#, ["DV", "CLVIII", "MDCLXVI", "MMMDCCCLXXXVI"])
print(valid_romans(["MMCDXVIII", "MMMCCXXXIV", "MMMMDCLXXXI", "MMMCMXIL", "MMMMCLXI"]))#, ["MMCDXVIII", "MMMCCXXXIV", "MMMMDCLXXXI", "MMMMCLXI"])
