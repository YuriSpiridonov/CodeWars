# https://www.codewars.com/kata/string-incrementer/train/python

import re
def increment_string(strng):
    if len(strng) == 0:
        return str(1)
    regex = re.compile(r'(((.*)?\D)|(\d+$)?)')
    mo = regex.findall(strng)
    lst = list()
    
    if type(mo[0][1]) == str:
        lst.append(mo[0][1])
        if len(mo[-2][0]) > 0 and mo[-2][0].isdigit() is True:
            lst.append(mo[-2][0])
        else:    
            lst.append('0')
    else:     
        str1 = strng[:-len(mo[-2][0])]
        lst.append(str1)
        lst.append(mo[-2][0])

    if len(lst[0]) == 0 and len(lst[-1]) == 0: # empty string ""
        return str(1)
    elif len(lst[0]) == 0 and len(lst[-1]) > 0: # only numbers in string "00324324"
        lst[1] = str(int(lst[1])+1).zfill(len(lst[1]))
        strng = ''.join(lst)
        return strng
    elif len(lst[0]) == 0: # only letters in string "ertgdfg"
        lst[1] = str(1)
        strng = ''.join(lst)
        return strng
    else:
        lst[1] = str(int(lst[1])+1).zfill(len(lst[1]))
        strng = ''.join(lst)
        return strng

print(increment_string("foo"))#, "foo1")
print(increment_string("foobar001"))#, "foobar002")
print(increment_string("foobar1"))#, "foobar2")
print(increment_string("foobar00"))#, "foobar01")
print(increment_string("foobar99"))#, "foobar100")
print(increment_string("foobar099"))#, "foobar100")
print(increment_string(""))#, "1")
print(increment_string("009")) #010
print(increment_string("##4&L16838526gFwC)/u<08\G:>))789381Hl?r\1W;f2079921W{06680000000004698")) # ##4&L16838526gFwC)/u<08\\G:>))789381Hl?r\\1W;f2079921W{06680000000004699

