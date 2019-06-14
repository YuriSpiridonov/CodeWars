# https://www.codewars.com/kata/weird-string-case/train/python

def CaSe(word):
    lst=list(word)
    for i in range(len(lst)):
        if i == 0 or i%2 == 0:
            lst[i] = lst[i].upper()
    return ''.join(lst)            
               
def to_weird_case(n):
    n = n.split(' ')
    for i in range(len(n)):
        n[i] = CaSe(n[i])
    return ' '.join(n)
