# https://www.codewars.com/kata/compare-section-numbers/train/python

def compare(s1, s2):
    s1 = s1.split('.')
    s2 = s2.split('.')
    if len(s1) < len(s2):
        while len(s1) != len(s2):
            s1.append('0')
    elif len(s1) > len(s2):
        while len(s1) != len(s2):
            s2.append('0')
    for i in range(len(s1)):
        if int(s1[i]) == int(s2[i]):
            if i == len(s1)-1:
                return 0 
            else:
                continue
        elif int(s1[i]) < int(s2[i]):
            return -1
        elif int(s1[i]) > int(s2[i]):
            return 1
