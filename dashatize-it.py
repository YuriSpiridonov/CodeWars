# https://www.codewars.com/kata/dashatize-it/train/python
# simple one

def dashatize(num):
    num = str(num)
    lst = list(num)
    numList = ['1','3','5','7','9']
    for item in lst:
        if item in numList:
            lst[lst.index(item)] = '-'+item+'-'
    dashed  = ''.join(lst).replace('--','-').strip('-')
    return dashed
