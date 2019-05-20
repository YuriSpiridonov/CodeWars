# https://www.codewars.com/kata/codewars-leaderboard/train/python

import urllib.request, urllib.parse, urllib.error
import re

def get_leaderboard_honor():
    url = 'https://www.codewars.com/users/leaderboard'
    regex = re.compile(r'(\d{1,3})\,(\d{3})')
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        mo = regex.findall(line.decode().strip())
        if mo:
            for i in range(1,len(mo)+1):
                mo[-i] = int((mo[-i][0]+mo[-i][1]))
            return mo
