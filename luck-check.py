# https://www.codewars.com/kata/luck-check/train/python

def luck_check(string):
    left  = 0
    right = 0
    if len(string)%2 != 0:
        for integer in string[:int(len(string)/2)]:
            left  += int(integer)
        for integer in string[int(len(string)/2)+1:]: 
            right += int(integer)
    else:
        for integer in string[:int(len(string)/2)]:
            left  += int(integer)
        for integer in string[int(len(string)/2):]: 
            right += int(integer)
    if left == right:
        return True
    else:
        return False
