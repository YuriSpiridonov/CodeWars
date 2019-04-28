# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python
# that manipulation was too easy for 5 kyu

def move_zeros(array):
    for i in range(1, len(array)+1):
        if array[-i] == 0 and array[-i] is not False:
            array.append(array.pop(-i))
    return array
    
print(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros([0, 0, 'string', -4, 0, -8, 0, 6, 9, 6, 0, 'a', 0, 5, 5, '0', -5, 3, 0, -2, 0, 'a', 0, 1, 0, 'y', -6, 10, 0, -8]))    
