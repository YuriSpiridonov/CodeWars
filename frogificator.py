# https://www.codewars.com/kata/frogificator/train/python

import re
def frogify(s):
    newSentence = str()
    newList = list()
    insertIndex = 0
    regex = re.compile(r'\w+|[\.\?\!]')
    mo = regex.findall(s)
    for i in range(len(mo)):
        if mo[i].isalpha() == True:
            newList.insert(insertIndex, mo[i])
            newSentence =  ' '.join(newList) # cherez +
        else:
            newList.append(mo[i])
            insertIndex = i+1
            newSentence +=(mo[i])
            continue
    newSentence = newSentence.replace(' .', '.')
    newSentence = newSentence.replace(' !', '!')
    newSentence = newSentence.replace(' ?', '?')
    return newSentence
