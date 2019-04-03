# https://www.codewars.com/kata/validdate-regex/train/python
# as experiment ugly regex without comments

import re

valid_date = re.compile(r'''
\[
(
(12|10|[0][13578])\-([3][01]|20|10|[0-2][1-9])|
([0][2])\-([2][0-8]|10|[01][1-9])|
(11|[0][469])\-(30|20|10|[0-2][1-9])
)
\]
''', re.VERBOSE)

mo = valid_date.search('ignored [08-11] ignored')
mo1 = valid_date.search("[01-23]")

print(bool(mo))
print(bool(mo1))
