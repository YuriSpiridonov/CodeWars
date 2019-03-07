# https://www.codewars.com/kata/find-the-odd-int/train/python

def find_it(seq):
    odd_dict = dict()
    for i in seq:
        if i not in odd_dict:
            odd_dict[i]= 1
        else:
            odd_dict[i]+=1
    for key, value in odd_dict.items():
        if value%2 > 0:
            return key
