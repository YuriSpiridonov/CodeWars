# https://www.codewars.com/kata/where-my-anagrams-at/train/python

def anagrams(word, words):
    lst = list()
    for element in words:
        if set(word) == set(element) and len(word) == len(element):
            lst.append(element)
    return lst 
    
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])    
