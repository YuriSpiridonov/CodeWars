# https://www.codewars.com/kata/not-very-secure/train/python

def alphanumeric(string):
    return bool(string.isalnum())
    
print(alphanumeric("hello_world"))#, False)
print(alphanumeric("PassW0rd"))#, True)
print(alphanumeric("     "))#, False)
print(alphanumeric("a"))#, True)        
