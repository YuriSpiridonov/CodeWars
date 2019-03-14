#  https://www.codewars.com/kata/ip-validation/train/python
# in progress

import re

def is_valid_IP(strng):
    print(strng)
    ipRegex = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    mo = ipRegex.findall(strng)
    
    try:
    
        for i in range(4):
            if len(mo[0][i]) >1 and int(mo[0][i][0]) == 0:
                return False
    
        if int(min(mo[0]))>=0 and int(max(mo[0]))<=255:
            return True
        elif  int(min(mo[0]))<0 or int(max(mo[0]))>255:
            return False
        #else:
        #    return False
    except:
        return False



print(is_valid_IP('192.168.1.300'))#,   False)
print(is_valid_IP('0.34.82.53'))#,       True)
print(is_valid_IP('abc.def.ghi.jkl')) #, False))
print(is_valid_IP(''))# False
print(is_valid_IP('123.045.067.089'))#, False))
