# https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python

# Tests with invalid input returns arrors when 'words' looks like that yvrse'', oapmaltw'. 
# I think it's happens because \W exclude ' at the end of 'word'.

import re, operator
def top_3_words(text):
    wordsDict = dict()
    topWords = list()
    sortedDict = dict()
    regex = re.compile(r"[a-zA-Z']*'*?[a-zA-Z']*?[^\s_\W]")
    words = regex.findall(text.lower())
    for word in words:
        if word not in wordsDict and word != "'":
            wordsDict[word] = 1
        elif word != "'":
            wordsDict[word] += 1    
    sortedDict = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse = True)
    if len(sortedDict) < 3:
        for index in range(len(sortedDict)):
            topWords.append(sortedDict[index][0])
    else:    
        for index in range(0,3):
            topWords.append(sortedDict[index][0])
    return topWords
