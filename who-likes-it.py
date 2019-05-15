# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
    counter = len(names)
    if counter == 0:
        string = 'no one likes this'
    elif counter == 1:
        string = names[0]+' likes this'
    elif counter == 2:
        string = names[0]+' and '+names[1]+' like this'
    elif counter == 3:
        string = names[0]+', '+names[1]+' and '+names[2]+' like this'
    else:
        string = names[0]+', '+names[1]+' and '+str(counter-2)+' others like this'
    return string
