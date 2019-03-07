# https://www.codewars.com/kata/string-ends-with/train/python

def solution(string, ending):
    string_rev=''.join(reversed(string))
    ending_rev=''.join(reversed(ending))
    if string_rev.startswith(ending_rev):
        return True
    else:
        return False
