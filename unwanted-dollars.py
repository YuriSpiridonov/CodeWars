# https://www.codewars.com/kata/unwanted-dollars/train/python

import re
def money_value(s):
    try:
        return float(re.sub(r'[\s$]', '', s))
    except:
        return 0.0
