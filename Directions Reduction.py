# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
# WRONG SOLUTION 

def dirReduc(arr):
    lst = list()
    for i, j in zip(arr[:-1],arr[1:]):
        if i == j:
            pass
        else:
            if  "SOUTH" not in arr or "NORTH" not in arr:
                pass
            elif i == 'NORTH' and j == 'SOUTH' or i == 'SOUTH' and j == 'NORTH':
                arr.remove(i)
                arr.remove(j)
                continue
            if "WEST" not in arr or "EAST" not in arr:
                pass
            elif i == 'EAST' and j == 'WEST' or i == 'WEST' and j == 'EAST':
                arr.remove(i)
                arr.remove(j)
                continue
    return arr   

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))   
