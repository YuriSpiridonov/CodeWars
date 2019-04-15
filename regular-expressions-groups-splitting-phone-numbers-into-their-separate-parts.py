# https://www.codewars.com/kata/regular-expressions-groups-splitting-phone-numbers-into-their-separate-parts/train/python
# I wont comment that re. I will back in 1-2 week and comment.

import re

regex = re.compile(r'(?:\+|0{1,2}(?=[1-9]\d [1-9]\d )|(?=\d[1-9]\d |(?=[1-9]\d{5})))([1-9]\d(?= [1-9]\d ))? ?(^\d[1-9]\d|(?<=[1-9]\d )[1-9]\d)? ?([1-9]\d{5})$')

mo = regex.match("0090 70 500000")
mo1 = regex.match('+12 34 567890')
mo2 = regex.match('12 34 567890')
mo3 = regex.match('034 567890')
mo4 = regex.match('567890')

print(mo)
print(mo1)
print(mo2)
print(mo3)
print(mo4)
