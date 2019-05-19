# https://www.codewars.com/kata/arrh-grabscrab/train/python

def grabscrab(word, possible_words):
    words_list = list()
    for words in possible_words:
        if sorted(words) == sorted(word):
            words_list.append(words)
            continue
        else:
            continue
    return words_list
    
print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]), ["pool", "loop"], "Should have found 'pool' and 'loop'")
