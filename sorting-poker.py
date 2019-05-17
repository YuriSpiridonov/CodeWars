# https://www.codewars.com/kata/sorting-poker/train/python

import re
def sort_poker(john, uncle):
    JohnDict = dict()
    cards = str()
    JohnRegex = re.compile(r'[CDHS][0-9JQKA]{1,2}')
    JohnMo = JohnRegex.findall(john)
    UncleRegex = re.compile(r'[CDHS]')
    UncleMo = UncleRegex.findall(uncle)
    for card in JohnMo:
        jqka = {'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
        if card[-1].isdigit() and card[-1] != '0':
            JohnDict[card] = JohnDict.get(card, int(card[-1])) 
        elif card[-1] in jqka.keys():
            JohnDict[card] = JohnDict.get(card, jqka[card[-1]])
        else:
            JohnDict[card] = JohnDict.get(card, 10)
    for item in UncleMo:
        while UncleMo.count(item) > 1:
            UncleMo.pop(UncleMo.index(item))
    sorted_JohnDict = sorted(JohnDict.items(), key=lambda kv: kv[1])
    for item in UncleMo:
        for i in range(len(sorted_JohnDict)):
            if item in sorted_JohnDict[i][0]:
                cards += sorted_JohnDict[i][0]
    return cards            
    


print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","S2S3S5HJHQHKC8C9C10D4D5D6D7"), "S3SJSKSAH2H5H10C5C7CQD2D5D6")
print(sort_poker("D6H2S3D5SJCQSKC7D2C5H5H10SA","C8C9C10D4D5D6D7S2S3S5HJHQHK"), "C5C7CQD2D5D6S3SJSKSAH2H5H10")
