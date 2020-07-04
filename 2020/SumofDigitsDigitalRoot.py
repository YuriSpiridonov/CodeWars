"""
    Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one 
    digit, continue reducing in this way until a single-digit number is produced. 
    This is only applicable to the natural numbers.

    Examples
        16  -->  1 + 6 = 7
       942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
    493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
#Difficulty: 6 kyu
#Name: Sum of Digits / Digital Root
#Link: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    number = 0 # our var to save result
    while n: # while n > 0 we will reduce it
        digit = n % 10 # taking remainder
                       # reminder of div by 10
                       # always last digit
        number += digit # adding last digit to result var
        n //= 10 # decreasing our current number
    if number < 10: # base case when result found
        return number # return result from recursion
    else: # else - start recursion
       number = digital_root(number) # recursion itself, 
                                     # saving result to 
                                     # result var
    return number # return final result 
