# https://www.codewars.com/kata/counting-duplicates/train/python

def duplicate_count(text):
    lettersDict = dict()
    counter = 0
    letters = list(text.lower())
    for letter in letters:
        lettersDict[letter] = lettersDict.get(letter, 0) + 1
    for value in lettersDict.values():
        if value > 1:
            counter += 1
    return counter  
