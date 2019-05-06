# https://www.codewars.com/kata/first-non-repeating-character/train/python

def first_non_repeating_letter(string):
    if len(string) == 0: return ''
    for i in range(len(string)):
        counter = string.lower().count(string.lower()[i])
        if counter == 1:
            return string[i]
    return ''
    
print(first_non_repeating_letter('HM.v7uwm:iNFDm3Dn3n5OGD2Fit3h:aiZzcDPdAA7CG33ab9wOIbB'))    
