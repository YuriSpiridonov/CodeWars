# https://www.codewars.com/kata/regex-password-validation/train/python

regex=r"^(?=.{6,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?!.*[\s#$%&\'()*+,-./:;<=>?!@[\\\]^_`{|}~]).*$"

import re

regex = re.compile(r"^(?=.{6,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?!.*[\s#$%&\'()*+,-./:;<=>?!@[\\\]^_`{|}~]).*$")
mo = regex.search('q8q\\0b6PZuV 22')
print(bool(mo))

# False
