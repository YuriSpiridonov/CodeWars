# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    lst=[]
    lstClean = []
    lst=list(iterable)
    for i in lst:
        if i not in lstClean:
            lstClean.append(i)
        else:
            if i != lstClean[-1]:
                lstClean.append(i)
            else:
                continue
    pass
    return lstClean
