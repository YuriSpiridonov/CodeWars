# https://www.codewars.com/kata/which-filetypes-are-you-using-the-most/train/python

import re

def solve(files):
    ext_dict=dict()
    value_list = list()
    max_list = list()
    for file in files:
        extention = re.findall(".*(\..*)", file)
        if extention[0] not in ext_dict:
            ext_dict[extention[0]]= 1
        else:
            ext_dict[extention[0]]+=1
    for key,value in list(ext_dict.items()):
        value_list.append((int(value),key))
    value_list.sort(reverse=True)
    for i in range(len(value_list)):
        if value_list[i][0] == value_list[0][0]:
            max_list.append(value_list[i][1])
    max_list.sort()
    print(max_list)
    return max_list
