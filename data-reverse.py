# https://www.codewars.com/kata/data-reverse/train/python

def data_reverse(data):
    x = int(len(data)/8)
    y = 0
    reverse = list()
    for i in range(x):
        reverse=(data[8*y:8+(8*y)])+reverse
        i+=1
        y+=1
    return reverse 
