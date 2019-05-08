# https://www.codewars.com/kata/parseint-reloaded/train/python

def firstten(number):
    first12 = {'zero' : 0,
    'one' : 1, 'two' : 2, 'three' : 3,
    'four' : 4, 'five' : 5, 'six' : 6,
    'seven' : 7, 'eight' : 8, 'nine' : 9,
    'ten' : 10, 'eleven' : 11, 'twelve' : 12}
    for key, value in first12.items():
        if number in key:
            return first12[key]
def teens(number):
    teens = {'thirteen' : 13,
    'fourteen' : 14, 'fifteen' : 15, 'sixteen' : 16,
    'seventeen' : 17, 'eighteen' : 18, 'nineteen' : 19, }
    for key, value in teens.items():
        if number in key:
            return teens[key]
def tens(number):
    tens = { 'twenty' : 20, 'thirty' : 30,
    'forty' : 40, 'fifty' : 50, 'sixty' : 60,
    'seventy' : 70, 'eighty' : 80, 'ninety' : 90 }
    for key, value in tens.items():
        if number in key:
            return tens[key]
def hundreds(number):
    hundreds = {'hundred' : 100, 'thousand' : 1000, 'million' : 1000000}
    for key in hundreds.keys():
        if number in key:
            return hundreds[key]

def parse_int(string):
    hunds = ['hundred', 'thousand', 'million']
    tempIndex = list()
    strlist = string.split(' ')
    for element in strlist:
        if 'and' == element:
            strlist.pop(strlist.index(element))
    for index, element in enumerate(strlist):
        if '-' in element:
            temp = element.split('-')
            for ele in temp:
                if 'ty' in ele:
                    temp10 = tens(ele)
                else:
                    temp1 = firstten(ele)
            strlist[index] = temp10+temp1
        elif 'ty' in element:
            strlist[index] = tens(element)
        elif 'teen' in element:
            strlist[index] = teens(element)
        elif element in hunds:
            strlist[index] = hundreds(element)
            if strlist[index] == 100:
                strlist[index] *= strlist[index-1]
                tempIndex.insert(0, index-1)
        else:
            strlist[index] = firstten(element)
    for i in tempIndex:
        strlist.pop(i)
    if 1000 in strlist:
        strlist[strlist.index(1000)-1] = sum(strlist[:strlist.index(1000)])
        strlist[-1] = strlist[strlist.index(1000)-1]*strlist[strlist.index(1000)]+sum(strlist[strlist.index(1000)+1:]) 
    elif 1000000 in strlist:
        return strlist[-1]
    else:
        return sum(strlist)
    return strlist[-1]
    
print(parse_int("one million"))
print(parse_int('two hundred three thousand'))
print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))
print(parse_int('eighteen'))
print(parse_int('two thousand'), 1)
print(parse_int('twenty'), 20)
print(parse_int('forty-six'), 46)
print(parse_int('two hundred forty-six'), 246)
