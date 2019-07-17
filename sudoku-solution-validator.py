# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):
    square1 = list()
    square2 = list()
    square3 = list()
    tempChecker = list()
    counter = 0
    for i in range(len(board)):
        if 0 in board[i]:
            break
        if len(set(board[i])) == 9:
            tempChecker.clear()
            for index in range(0,9):
                tempChecker.append(board[index][i])
            if len(set(tempChecker)) == 9:
                counter += 1
        square1 += board[i][0:3]
        square2 += board[i][3:6]
        square3 += board[i][6:9]
        if len(square1) == 9:
            if len(set(square1)) == 9 and len(set(square2)) == 9 and len(set(square3)) == 9:
                square1.clear()
                square2.clear()
                square3.clear()
                counter -= 3
            else:
                break                
    return bool(counter == 0)
