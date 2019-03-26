# https://www.codewars.com/kata/split-strings/train/python

import re
def solution(s):
    if len(s)%2 != 0:
        s+='_'
    regex = re.compile(r'\w\w')
    mo = regex.findall(s)
    return mo
