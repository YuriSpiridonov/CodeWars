# https://www.codewars.com/kata/help-the-bookseller/train/python

import re
def stock_list(listOfArt, listOfCat):
    total = dict()
    string = str()
    for letter in listOfCat:
        regex = re.compile(r'^('+letter+').*\s(\d+)')
        for code in listOfArt:
            mo = regex.findall(code)
            if mo:
                total[mo[0][0]] = total.get(mo[0][0], 0) + int(mo[0][1])
            else:
                total[letter] = total.get(letter, 0)
    for key, value in total.items():
        string += f'({key} : {value}) - '
    return string.rstrip(' - ')            
                
    
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["Q","A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")    
