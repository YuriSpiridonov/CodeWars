# https://www.codewars.com/kata/convert-all-the-cases/train/python

import re
def change_case(identifier, targetCase):
    regex = re.compile(r'[A-Z]?[a-z]*')   

    if '-' in identifier and identifier.islower():
        mo = identifier.split('-')
    elif '_' in identifier and identifier.islower():
        mo = identifier.split('_')
    elif '-' not in identifier and not '_' in identifier:
        mo = regex.findall(identifier)
    else:
        return None
      
    for ele in mo:
        if len(ele) == 0:
            mo.pop(mo.index(ele))
        elif ele.isalpha():
            continue
        else:
            return None
            
    if  targetCase is "snake":
        return "_".join(mo).lower()
    elif targetCase is "kebab":
        return "-".join(mo).lower()
    elif targetCase is "camel":
        for index in range(1,len(mo)):
            mo[index] = mo[index].title()
        return "".join(mo)
    else:
        return None
