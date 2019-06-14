# https://www.codewars.com/kata/odd-even-string-sort/train/python

def sort_my_string(S):
    s = list(S)
    even = list()
    odd = list()
    for i in range(len(s)):
        if i == 0 or i%2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    return ''.join(even)+' '+''.join(odd)
