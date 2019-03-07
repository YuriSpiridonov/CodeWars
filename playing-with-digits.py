# https://www.codewars.com/kata/playing-with-digits/train/python

def dig_pow(n, p):
    n_str =str(n)
    n_list = list(n_str)
    k=0
    number=0
    for i in n_list:
        number += int(i)**(p+k)
        k+=1
    return_number = number/n    
    if number%n == 0:
        return int(return_number)
    else:    
        return -1
