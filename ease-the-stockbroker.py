# https://www.codewars.com/kata/ease-the-stockbroker/train/python
# IN PROGRESS lots of issues, doing everything wrong
import re

def balance_statement(lst):
    lst1 = lst.split(', ')
    lst2 = list()
    lst3 = list()
    testlist = list()
    tempB = 0
    tempS = 0
    counter = 0
    for x in range(len(lst1)):
        lst2.append(lst1[x].split(' '))
        lst3.append(lst1[x].split(' '))
    print(lst2)    
    for i in range(len(lst2)):
        if lst2[i][1].isdigit():
            lst2[i].insert(2, int(lst2[i][1]))
            lst2[i].pop(1)
        else:
            badstr=''.join(lst3[i])
            counter+=1
        testList = re.findall('[0-9]+',lst2[i][2])
        if len(testList) == 2:   
            lst2[i].insert(3, float(lst2[i][2]))
            lst2[i].pop(2)
        else:
            badstr=''.join(lst3[i])
            counter+=1
        if len(lst2[i]) < 4:
            badstr=''.join(lst3[i])
            counter+=1
        if lst2[i][3] == 'B':
            mult= lst2[i][1] * lst2[i][2]
            tempB= tempB + mult
            
        elif lst2[i][3] == 'S':
            mult= lst2[i][1] * lst2[i][2]
            tempS= tempS + mult
        else:
            print(lst3[i])
            
            badstr =' '.join(lst3[i])
            counter+=1
    stringjoin = 'Buy: ' +str(tempB)
    stringjoin = stringjoin +' Sell: ' +str(tempS)+';'
    if counter > 0:
        stringjoin = stringjoin + ' Badly formed '+ str(counter) + ': '
        stringjoin = stringjoin + str(badstr)
   
    #print(stringjoin)
    return stringjoin
   
            
                
    

print(balance_statement("ZNGA 1300 2.66 S, CLH15.NYM 50 56.32 S, OWW 1000 11.623 B, OGG 20 580.1 B, OGG 20 580.1 T")) #  , OGG 20 580.1,  OWW 1000 11 B")) "Buy: 29499 Sell: 0"))
#3458 , 2816, 11623, 11602
#"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"
#"Buy: PARAMETR Sell: PARAMETR; Badly formed NUMBER: str; str;"
