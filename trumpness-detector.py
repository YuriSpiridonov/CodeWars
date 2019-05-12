# https://www.codewars.com/kata/trumpness-detector/train/python

import re
def trump_detector(trump_speech):
    regex= re.compile(r'[a]+|[e]+|[i]+|[o]+|[u]+')
    mo = regex.findall(trump_speech.lower())
    return round((len(''.join(mo))-len(mo))/len(mo), 2)
