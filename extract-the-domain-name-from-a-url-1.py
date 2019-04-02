# https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python

import re
def domain_name(url):
    regex = re.compile(r'''
    ^(http://|https://|http://www.|https://www.|www.)  # http + wwww
    ([a-zA-Z0-9\-]+)                                   # domain
    (\.[a-z0-9/]+)$                                    # .com
    ''', re.VERBOSE)
    mo = regex.findall(url)
    return mo[0][1]

print(domain_name("http://zombie-bites.com"))# == "zombie-bites"
print(domain_name("http://github.com/carbonfive/raygun"))# == "github"
print(domain_name("http://www.zombie-bites.com"))# == "zombie-bites"
print(domain_name("https://www.cnet.com"))# == "cnet"
