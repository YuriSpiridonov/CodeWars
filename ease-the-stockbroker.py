# https://www.codewars.com/kata/ease-the-stockbroker/train/python
# IN PROGRESS lots of issues, doing everything wrong
import re

def balance_statement(lst):
    lst2 = list()
    badFormat = list()
    testlist = list()
    lst1 = lst.split(', ')
    for x in range(len(lst1)):
        lst2.append(lst1[x].split(' '))
    #testlist = re.findall('\S+',lst) return same as lines 8 to 10 but not useble format    
    print(lst2)
    # fist need to find way check str content for inner value is lst2[1] is able to be int and [2] to be float
    # my try re for it [1] only digits [2] digits with a dot . then convert it to int and float
    
    for i in range(len(lst2)):
        lst2[i].insert(2, int(lst2[i][1]))
        lst2[i].pop(1)
        lst2[i].insert(3, float(lst2[i][2]))
        lst2[i].pop(2)
        if len(lst2[i]) < 4:
            badForamt.append(lst2[i])
            print(badFormat)

        elif type(lst2[i][1]) is int:
            print(lst2[i][1])
            if type(lst2[i][2]) is int:
                mult= lst2[i][1] * lst2[i][2]
                #print(mult)



    print(lst2)


    #return "?"

print(balance_statement("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B, OGG 20 580.1,  OWW 1000 11 B")) #    #"Buy: 29499 Sell: 0"))
#3458 , 2816, 11623, 11602
#"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"
#"Buy: PARAMETR Sell: PARAMETR; Badly formed NUMBER: str; str;"
