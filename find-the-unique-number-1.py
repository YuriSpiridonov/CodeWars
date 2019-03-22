# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    n = max(arr)
    if arr.count(n) > 1:
        n = min(arr)
    return n
