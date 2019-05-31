# https://www.codewars.com/kata/regex-like-a-boss-number-3-different-number-formats/train/python
# tested beta kata

REGEX = r'''^(0{1}|((0(?=\.)\.\d*[1-9])|([1-9]\d{,2}(?<=\d)([,]\d{3})*(\.\d*[1-9])?))|((0(?=,),\d*[1-9])|([1-9]\d{,2}(?<=\d)([\s]\d{3})*(\,\d*[1-9])?)))$'''
