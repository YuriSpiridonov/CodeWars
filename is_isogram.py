# https://www.codewars.com/kata/isograms/train/python

def is_isogram(string): 
    count= dict()
    for character in string.lower():
        count.setdefault(character, 0)
        count[character]+=1
    if  len(count) == 0 or max(count.values()) == 1:
        return True
    else:
        return False 
