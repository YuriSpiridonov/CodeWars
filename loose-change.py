# https://www.codewars.com/kata/loose-change/train/python

import math
def loose_change(cents):
    cents = math.floor(cents)
    change_dict = {'Nickels': 5, 'Pennies': 1, 'Dimes': 10, 'Quarters': 25}
    change_numbers = {25 : 0, 10 : 0, 5 : 0, 1 : 0}
    check_list = list()
    for key, value in change_numbers.items():
        while cents - key >= 0:
            cents = cents - key
            change_numbers[key] += 1
    for key, value in change_dict.items():
        for k, v in change_numbers.items():
            if k == change_dict[key] and key not in check_list:
                change_dict[key] = v
                check_list.append(key)
    return change_dict
