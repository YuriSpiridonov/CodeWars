# https://www.codewars.com/kata/matching-and-substituting/train/python

import re
def change(s, prog, version):
    dic = {"Program title" : "Program: "+prog, 'Author: ' : "Author: g964", 'Corporation: ' : '','Date: ' : 'Date: 2019-01-01', 'Level' : ''}
    # validation of phone and version in s
    if bool(re.search(r'\+1-\d{3}-\d{3}-\d{4}', s)) == False or bool(re.search(r'\s\d{1,}\.\d{1,}\s', s)) == False:        
        return 'ERROR: VERSION or PHONE'
    # phone
    s = re.sub(r'\+\d-\d{3}-\d{3}-\d{4}', '+1-503-555-0090', s)
    # version
    if re.search(r'\d{1,}\.\d{1,}', s).group() != '2.0':
        s = re.sub(r'\d{1,}\.\d{1,}', version, s)

    for k,v in dic.items():
        s = re.sub(k+r'.*', v, s)
    return s.replace('\n', ' ').strip(' ').replace('  ', ' ') 
