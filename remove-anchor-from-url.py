# https://www.codewars.com/kata/remove-anchor-from-url/train/python

import re
def remove_url_anchor(url):
    cleanUrl = re.compile(r'([a-zA-Z0-9./=?:]+)')
    moUrl = cleanUrl.search(url)
    return moUrl.group()
