# https://www.codewars.com/kata/generic-numeric-template-formatter/train/python

def numeric_formatter(template, numbers = '1234567890'):
    y = 0
    while len(template) > len(numbers):
        numbers+=numbers
    newstr= str()    
    for i in range(len(template)):
        if template[i].isalpha() == True:
            newstr += template[i].replace(template[i], numbers[y])
            y+=1
        else:
            newstr += template[i]
    return newstr
