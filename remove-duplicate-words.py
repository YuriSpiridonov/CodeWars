# https://www.codewars.com/kata/remove-duplicate-words/train/python

import re
def remove_duplicate_words(s):
    strWords = str()
    wordsRegex = re.compile(r'\w+')
    moWords = wordsRegex.findall(s)
    for i in range(len(moWords)):
        if moWords[i] not in strWords:
            strWords = strWords + moWords[i] + ' '
        else:
            continue 
    return strWords.rstrip()
