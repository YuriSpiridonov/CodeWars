# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    lst=list()
    for item in l:
        if type(item) is int:
            lst.append(item)
    return lst
