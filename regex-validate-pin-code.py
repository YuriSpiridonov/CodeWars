# https://www.codewars.com/kata/regex-validate-pin-code/train/python
# simple kata after the break

import re
def validate_pin(pin):
    regex = re.compile(r'\b\d{4}\b|\b\d{6}\b')
    mo = regex.match(pin)
    if mo:
        return True
    else:
        return False
