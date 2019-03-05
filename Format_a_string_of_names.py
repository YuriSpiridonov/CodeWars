# https://www.codewars.com/kata/53368a47e38700bd8300030d

def namelist(names):
    str = ''
    lenght = len(names)
    count = 0
    for items in names:
        for key, value in items.items():
            count+=1
            if key == 'name':
                if lenght - count == 1:
                    str+=value+' & '
                elif lenght - count == 0:
                    str+=value
                else:
                    str+=value+', '
    return str 
