# https://www.codewars.com/kata/codewars-api/train/python
# solution is right but can't submit it on codewars

import urllib.request, urllib.parse, urllib.error
import re
import json

def get_codeChallenges(n):
    total = list()
    url = 'https://www.codewars.com/users/leaderboard'
    serviceurl = 'https://www.codewars.com/api/v1/users/'
    regex = re.compile(r'<tr data-username=\"(\w+[.-_\s]?)\"><td class=\"rank is-small\">#'+str(n))
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        mo = regex.search(line.decode().strip())
        if mo:
            username = mo.group(1)
    uh = urllib.request.urlopen(serviceurl + username)
    data = uh.read().decode()
    jsonData = json.loads(data)
    total.append(jsonData["codeChallenges"]["totalAuthored"])
    total.append(jsonData["codeChallenges"]["totalCompleted"])
    return total
