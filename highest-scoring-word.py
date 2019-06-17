# https://www.codewars.com/kata/highest-scoring-word/train/python

def high(x):
    lst = sorted(x.split(), key = len, reverse=True)
    dct = dict()
    for word in lst:
        dct[word] = 0
        value = 0
        letter_list = list(word)
        for letter in letter_list:
            value += ord(letter)-96
        dct[word] = value
    for key, value in dct.items():
        return max(dct, key=dct.get)
