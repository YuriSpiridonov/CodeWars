# https://www.codewars.com/kata/scraping-get-the-year-a-codewarrior-joined/train/python

import urllib.request
import re
def get_member_since(username):
    url = 'https://www.codewars.com/users/' + username
    regex = re.compile(r'\w{3}\s\d{4}')
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        mo = regex.search(line.decode().strip())
        if mo:
            return mo.group()
            
print(get_member_since('jhoffner'), 'Oct 2012')    
