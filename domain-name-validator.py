# https://www.codewars.com/kata/domain-name-validator/train/python
# don't judge my 'poem' please

import re

def validate(domain):
    regex = re.compile(r'''
    (
                #sub.site.com parsing
    (?=.{3,253}$)                           # max 253 char
                # sub.
    ((?![-.])                               # exclude - and . from start point
    [a-zA-Z0-9-.]*                          # subdomain chars
    [^-.]                                   # exclude - and . from end point
    (\-[a-zA-Z0-9]*[^-])?                   # additional dashed section
    \.{1})?                                 # . dotted end of not necessary subdomain
                # end of sub. section
                # site.com
    (
    (?=.{,63}$)                             # max 63 char for domain name
    (?![-.])                                # exclude - and . from start point
    [a-zA-Z0-9\-]*                          # domain chars
    [^-.]                                   # exclude - and . from end point
                # .com section
    \.{1}                                   # separator between site and .com
    (?![-.])                                # exclude - and . from start point
    (
    ([0-9]*\-[0-9]*)[^-.]|                       # 1-2
    ([a-zA-Z]{1,})[^-.]|                         # a-b
    ([0-9]*\-[a-zA-Z]{1,})[^-.]|                 # 1-a
    ([a-zA-Z]{1,}\-[0-9]*)[^-.]|                 # a-1
    ([a-zA-Z]{1,}[0-9]*)[^-.]|                   # ab1 or a12
    ([0-9]*[a-zA-Z]{1,})[^-.]|                   # 1ab or 12a
    ([a-zA-Z]{1,}[0-9]*[a-zA-Z]{1,})[^-.]|       # a1b
    ([0-9]*[a-zA-Z]{1,}[0-9]*)                   # 1a2
    )$
    )$                                      # making sure that domain formation site.com at the end of line
                # end of .com section
                # end of site.com section
    )

    ''', re.VERBOSE)
    mo = regex.match(domain)
    return bool(mo)
