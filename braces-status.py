# https://www.codewars.com/kata/braces-status/train/python

def braces_status(string):
    symbols = ".QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz1234567890"
    for letter in string:
        if letter in symbols:
            string = string[:string.index(letter)]+string[string.index(letter)+1:]
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()','').replace('[]','').replace('{}','')
    return bool(len(string)==0)
