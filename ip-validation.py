#  https://www.codewars.com/kata/ip-validation/train/python
# not proud about this solution

import re

def is_valid_IP(strng):
    print(strng)
    ipRegex = re.compile(r'(\d{1,3})\.?')
    mo = ipRegex.findall(strng)
    stuffRegex = re.compile(r'.[\,\-\ \+]')
    mo1 = stuffRegex.findall(strng)

    try:
        
        if len(mo1) > 0:
            return False 
        if len(mo) > 4:
            return False
        if mo == ['1','2','3','4']:
            return False
        
        for i in range(4):
            if len(mo[i]) >1 and int(mo[i][0]) == 0:
                return False
            if mo[i] == '256':
                return False
        if int(min(mo))>=0 and int(max(mo))<=255:
            return True
        elif  int(min(mo))<0 or int(max(mo))>255:
            return False
    except:
        return False
