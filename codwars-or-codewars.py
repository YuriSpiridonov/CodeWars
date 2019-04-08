# https://www.codewars.com/kata/codwars-or-codewars/train/python
# I beat it! Finaly! one day I will oneline it! 
# REMINDER check re.compile's and clean them

import re

def find_codwars(url):
    greedyRegex = re.compile(r'''
    ^(|http://|https://|http://www.|https://www.)(?:.*[\w.])?
    \bcodwars\.com\b     
    (|/.*|\?.*)?$
    ''', re.VERBOSE)
    non_greedeRegex = re.compile(r'(|//).*\.?\bcodwars\.com?/[\w+]')
    if url.count('/') > 3:
        mo = non_greedeRegex.search(url)
    else:
        mo = greedyRegex.match(url)
    return bool(mo)
