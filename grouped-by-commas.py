# https://www.codewars.com/kata/grouped-by-commas/train/python
# 2.7 accidentally 
# Python makes my cry :) 

import re
def group_by_commas(n):
    return ','.join(re.findall(r'\d{1,3}', str(n)[::-1])[::-1][::-1])[::-1] 

print(group_by_commas(35235235), '35,235,235')
