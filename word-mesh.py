# https://www.codewars.com/kata/word-mesh/train/python
# This exercise was a regex practice. So you can see my todays regex skills :)

def word_mesh(arr):
    match = str()
    counter = int()
    try:
        for i in range(len(arr)):
            for y in range(len(arr[i])):
                if arr[i+1].startswith(arr[i][y:]) is not True:
                    continue
                else:
                    match += ''.join(arr[i][y:])
                    counter+=1
                    break
    except:
        if counter == len(arr)-1:
            return match
        else:
            return "failed to mesh"
