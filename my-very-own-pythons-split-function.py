# https://www.codewars.com/kata/my-very-own-pythons-split-function/train/python
# faced an error do not know how to solve it.
# And if delimiter is empty...
# Expected an error when empty delimiter!

import re
def my_very_own_split(string, delimiter = None):
    print(delimiter)
    result = list()
    if len(string) == 0:
        return ['']
    if delimiter is not None and delimiter not in string:
        return re.findall(r'.+', string)
    if delimiter is None:
        string = re.sub(r'\s+', '\!/', string)
    if delimiter:
        while delimiter in string:
            string = string.replace(delimiter, '\!/')
    string +='\!/'
    while '\!/' in string:
        counter = string.count('\!/')
        for i in range(counter):
            if '\!/' in string:
                temp = string[:string.index('\!/')]
                string = string[string.index('\!/')+3:]
                result.append(temp)
    return result
