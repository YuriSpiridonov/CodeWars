# https://www.codewars.com/kata/return-substring-instance-count-2/train/python

import re
def search_substr(full_text, search_text, allow_overlap=True):
    if len(full_text) == 0 or len(search_text) == 0:
        return 0
    elif allow_overlap == True:
        regex = re.compile('(?=%s)' % search_text)
        mo = regex.findall(full_text)
        return len(mo)
    else:    
        return full_text.count(search_text)
        
        
print(search_substr('aa_bb_cc_dd_bb_e', 'bb'), 2)
print(search_substr('aaabbbcccc', 'bbb'), 1)
print(search_substr('aaacccbbbcccc', 'cc'), 5)
print(search_substr('aaa', 'aa'), 2)
print(search_substr('aaa', 'aa',False), 1)
print(search_substr('aaabbbaaa', 'bb',False), 1)
print(search_substr('a', ''), 0)
print(search_substr('', 'a'), 0)
print(search_substr('', ''), 0)
print(search_substr('', '',False), 0)        
