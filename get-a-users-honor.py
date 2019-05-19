# https://www.codewars.com/kata/get-a-users-honor/train/python

def get_honor(username):
    import urllib.request, urllib.parse, urllib.error
    import json

    serviceurl = 'https://www.codewars.com/api/v1/users/'

    while True:
        url = serviceurl + username
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
    
        try:
            js = json.loads(data)
        except:
            js = None
    
        honor = js['honor']
        return honor
