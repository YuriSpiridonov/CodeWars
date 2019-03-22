# https://www.codewars.com/kata/mexican-wave/train/python

def wave(str):
    returnWave = list()
    lst = list(str)
    for i in range(len(lst)):
        try:
            if lst[i].isalpha():
                lst[i] = lst[i].upper()
                if len(lst) > 1:
                    lst[i-1] = lst[i-1].lower()       
            else:
                lst[i-1] = lst[i-1].lower()
                continue
            returnWave.append(''.join(lst))
        except:
            continue
    return returnWave
