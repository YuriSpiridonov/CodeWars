# https://www.codewars.com/kata/mod4-regex/train/python

import re

class Mod:
    mod4 = re.compile(r"""
    .*\[                                 # any char before [
    [-+]?                                # - or + before number
    \d*                                  # digits before pattern
    (?:[13579][26]\]|[02468][048]\])|    # pattern for numbers divisible by 4
    .*\[                                 # any char before [
    [-+]?                                # - or + before number
    [048]\]                              # pattern for 0 4 and 8 only
    """, re.VERBOSE)
