# https://www.codewars.com/kata/find-the-word-pair/train/python 
# Timeout 12sec

def compound_match(words, target):
    wordList = list()
    positionList = list()
    for word in words:
        if target.startswith(word):
            temp = word
            for word in words:
                if len(wordList) < 1:
                    if target.endswith(word) and len(temp+word) == len(target) and len(wordList) < 2:
                        positionList.insert(0,words.index(temp))
                        positionList.insert(1,words.index(word))
                        if words.index(temp) < words.index(word):
                            wordList.append(temp)
                            wordList.append(word)
                        else:
                            wordList.append(word)
                            wordList.append(temp)
                else:
                    break
    wordList.append(positionList)
    if len(wordList) > 1:
        return wordList
    else:
        return None
