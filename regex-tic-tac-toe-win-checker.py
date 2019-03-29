# https://www.codewars.com/kata/regex-tic-tac-toe-win-checker/train/python

import re
def regex_tic_tac_toe_win_checker(board):
    regex = re.compile('''
    (
    XXX......|OOO......|
    ...XXX...|...OOO...|
    ......XXX|......OOO|
    X..X..X..|O..O..O..|
    .X..X..X.|.O..O..O.|
    ..X..X..X|..O..O..O|
    X...X...X|O...O...O|
    ..X.X.X..|..O.O.O..
    )
        ''', re.VERBOSE)
    mo = regex.match(board)
    if mo != None:
        return True            
    else:
        return False
