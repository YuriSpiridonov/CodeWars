# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    printList = dict()
    sent = str()
    string = str()
    letter = str()
    lst = sentence.split(' ')
    i=0
    for i in range(len(lst)):
        letterList = list(lst[i])
        i+=1
        for number in letterList:
            if number.isdigit():
                string = ''.join(str(letter)for letter in letterList)
                printList[int(number)] = string
        sent = ' '.join('{}'.format(val) for key, val in sorted(printList.items()))   
    return sent
