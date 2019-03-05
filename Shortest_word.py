# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    # your code here
    l= None
    lst=s.split(' ')
    for word in lst:
        if l == None or len(word) < l:
            l = len(word)
    return l # l: shortest word length
