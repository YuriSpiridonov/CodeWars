# https://www.codewars.com/kata/sum-of-a-sequence/train/python
#very bad

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    summ=begin_number
    stepped = begin_number
    while stepped <= end_number:
        stepped = stepped + step 
        if stepped <= end_number:
            summ = summ + stepped
            print(summ)
    return summ
