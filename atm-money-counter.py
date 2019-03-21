# https://www.codewars.com/kata/atm-money-counter/train/python

import re
def atm(value):
    count=0
    moneyCounter = list()
    formated = str()
    formatedCount = str()
    returnCount = str()
    regex = re.compile(r'([a-zA-Z]+)?\s?(\d+)\s?([a-zA-Z]+)?')
    mo = regex.findall(value)
    amount = int(mo[0][1])
    if len(mo[0][0]) >len(mo[0][2]):
        currensy = mo[0][0].upper()
    else:
        currensy = mo[0][2].upper()
    if currensy not in VALUES.keys():
            returningAns = ['Sorry, have no ', currensy +'.']
            returningAnswer = ''.join(returningAns)
            return returningAnswer
    for key, values in VALUES.items():
        if key == currensy:
            if amount%min(values) != 0:
                returningAns = ['Can\'t do ', str(amount),' ', key+'. Value must be divisible by ',str(min(values))+'!']
                returningAnswer = ''.join(returningAns)
                return returningAnswer
            for i in range(1,len(values)+1):
                while amount - values[-i] >= 0:
                    amount -= values[-i]
                    count+=1
                    continue
                moneyCounter.append((count, values[-i]))
                i+=1
                count = 0
    for index in range(len(moneyCounter)):
        if moneyCounter[index][0] >0:
            formated = [str(moneyCounter[index][0]), '*',str(moneyCounter[index][1]), str(currensy)]
            formatedCount = ' '.join(formated)
            print(formatedCount)
            index+=1
            returnCount += formatedCount + ', '
            continue
    return returnCount[:-2]
