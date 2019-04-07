# https://www.codewars.com/kata/regexp-basics-is-it-ipv4-address/train/python

import re
def ipv4_address(address):
    regex = re.compile(r'''
    #      200-249   | 250-255 | 100-109| 0-99 110-199
    \b([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\.
    ([2]([0-4][0-9]|[5][0-5])|(10[0-9]|[1]?[1-9]?[0-9]))\b    
    ''', re.VERBOSE)
    mo = regex.match(address)
    if mo is None:
        return False
    elif  mo.group() == address:    
        return (bool(mo))
    else:
        return False
