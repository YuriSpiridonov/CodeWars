"""
    Snail Sort
    Given an n x n array, return the array elements arranged from outermost 
    elements to the middle element, traveling clockwise.

    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    For better understanding, please follow the numbers of the next array 
    consecutively:

    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]
    This image will illustrate things more clearly:

    NOTE: The idea is not sort the elements from the lowest value to the highest; 
          the idea is to traverse the 2-d array in a clockwise snailshell pattern.

    NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an 
            array [[]].
"""
#Difficulty: 4 kyu
#Name: Snail
#Link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(snail_map):
    if not snail_map: return None
    rows = len(snail_map)
    columns = len(snail_map[0])
    row = 0
    col = 0
    count = 0
    result = list()
    go_reverse = False
    while count < columns * rows:
        if not go_reverse:
            while col < columns:
                if snail_map[row][col] is not None:
                    result.append(snail_map[row][col])
                    snail_map[row][col] = None
                    col += 1
                    count += 1
                else:
                    break
            col -= 1
            if snail_map[row][col] == None or col == columns:
                row += 1
            while row < rows:
                if snail_map[row][col] is not None:
                    result.append(snail_map[row][col])
                    snail_map[row][col] = None
                    row += 1
                    count += 1
                else:
                    break    
            row -= 1
            if snail_map[row][col] == None or row == rows:
                col -= 1
            go_reverse = not go_reverse
        else:
            while col > -1:
                if snail_map[row][col] is not None:
                    result.append(snail_map[row][col])
                    snail_map[row][col] = None
                    col -= 1
                    count += 1
                else:
                    break
            if snail_map[row][col] == None or col == -1:
                col += 1
                row -= 1
            while row > -1:
                if snail_map[row][col] is not None:
                    result.append(snail_map[row][col])
                    snail_map[row][col] = None
                    row -= 1
                    count += 1
                else:
                    break
            if snail_map[row][col] == None or row == -1:
                col += 1
                row += 1
            go_reverse = not go_reverse
    return result
