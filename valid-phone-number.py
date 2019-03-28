# https://www.codewars.com/kata/valid-phone-number/train/python

import re
def validPhoneNumber(phoneNumber):
    regex = re.compile(r'^\(\d{3}\)\s\d{3}\-\d{4}$')
    mo = regex.match(phoneNumber)
    return bool(mo)
