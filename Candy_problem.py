# https://www.codewars.com/kata/candy-problem/train/python

def candies(s):
    number = int()
    for i in range(len(s)):
        if len(s)>1 and s is not None:
            number += max(s)-s[i]
            continue
        else:
            return -1
    if not s:
        return -1
    else:    
        return number
