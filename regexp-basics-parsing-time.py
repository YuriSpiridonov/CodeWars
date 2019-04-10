# https://www.codewars.com/kata/regexp-basics-parsing-time/train/python

import re
def to_seconds(time):
    regex = re.compile(r'\A\d{2}:[0-5][0-9]:[0-5][0-9]\Z')
    mo = regex.match(time)
    if mo:
       timeList = re.split(r':', time)
    else:
        return None
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])
