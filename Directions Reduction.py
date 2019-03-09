# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
# WRONG SOLUTION 

def dirReduc(arr):
    print(arr)
    while True:
        if  "SOUTH" not in arr or "NORTH" not in arr:
            break
        else:    
            if arr.index("NORTH")+1 == arr.index("SOUTH") or arr.index("SOUTH")+1 == arr.index("NORTH"):
                arr.pop(arr.index("NORTH"))
                arr.pop(arr.index("SOUTH"))
            else:
                break
            
        if "WEST" not in arr or "EAST" not in arr:
            break
        else:
            if arr.index("WEST")+1 == arr.index("EAST") or arr.index("EAST")+1 == arr.index("WEST"):
                arr.pop(arr.index("WEST"))
                arr.pop(arr.index("EAST"))
            else:
                break
    return arr
