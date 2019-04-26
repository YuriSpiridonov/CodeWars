# https://www.codewars.com/kata/float-or-integer-verifier/train/python

import re
def i_or_f(arr):
    regex = re.compile(r'''
    ^[+-]?(
    (\d*\.?(\d+)?)              #digits 1, 1.0, .1
    (\.?[eE][+-]?\d*)?          #digits 1E1, 1e+1
    )$
    ''', re.VERBOSE)
    return bool(regex.match(arr))
