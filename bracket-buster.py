# https://www.codewars.com/kata/bracket-buster/train/python

import re
def bracket_buster(string):
    if type(string) is not str:
        return "Take a seat on the bench."    
    regex = re.compile(r'''
    (?:\[)   #1st bracket
    (.*?)    #text in between
    (?:\])   #2nd bracket 
    ''',re.VERBOSE)
    mo = regex.findall(string)
    return mo
    
    
print(bracket_buster("[]"))
print(bracket_buster("arc.tic.[circle]?[?]"))             # ['circle', '?']
print(bracket_buster("[][]]]][[[[[[][]"))                 # ['', '', '[[[[[', '']
print(bracket_buster("Don't [pass to Ramone]"))           # ["pass to Ramone"])
print(bracket_buster(1337))                               # "Take a seat on the bench.")
print(bracket_buster("[I'm] glad y'all [set it]] off"))   # ["I'm", 'set it'])    
