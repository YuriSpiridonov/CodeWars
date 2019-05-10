# https://www.codewars.com/kata/find-the-word-pair/train/python
# Max Buffer Size Reached (1.5 MiB)

def compound_match(words, target):
    print(words)
    wordList = list()
    positionList = list()
    for word1 in words:
        for word2 in words:    
            if target.startswith(word1) is True and target.endswith(word2) and len(word1+word2) == len(target):
                if words.index(word1) < words.index(word2):
                    wordList.append(word1)
                    wordList.append(word2)
                else:
                    wordList.append(word2)
                    wordList.append(word1)
                positionList.insert(0,words.index(word1))
                positionList.insert(1,words.index(word2))
                wordList.append(positionList)            
                return wordList
