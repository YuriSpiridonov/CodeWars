# https://www.codewars.com/kata/uncollapse-digits/train/python

import re
def uncollapse(digits):
    regex = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|zero)')
    mo = regex.findall(digits)
    return ' '.join(mo)
