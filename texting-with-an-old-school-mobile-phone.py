# https://www.codewars.com/kata/texting-with-an-old-school-mobile-phone/train/python

def send_message(m):
    letters = {'0' : '0-', '1' : '1-', '2' : '2-',
'3' : '3-', '4' : '4-', '5' : '5-',
'6' : '6-', '7' : '7-', '8' : '8-',
'9' : '9-', ' ' : '0',
'.' : '1', ',' : '11', '?' : '111', '!' : '1111',
"'" : '*', '-' : '**', '+' : '***', '=' : '****',
'*' : '*-', '#' : '#-',
'A' : '2', 'B' : '22', 'C' : '222',
'D' : '3', 'E' : '33', 'F' : '333',
'G' : '4', 'H' : '44', 'I' : '444',
'J' : '5', 'K' : '55', 'L' : '555',
'M' : '6', 'N' : '66', 'O' : '666',
'P' : '7', 'Q' : '77', 'R' : '777', 'S' : '7777',
'T' : '8', 'U' : '88', 'V' : '888',
'W' : '9', 'X' : '99', 'Y' : '999', 'Z' : '9999',
'a' : '2', 'b' : '22', 'c' : '222',
'd' : '3', 'e' : '33', 'f' : '333',
'g' : '4', 'h' : '44', 'i' : '444',
'j' : '5', 'k' : '55', 'l' : '555',
'm' : '6', 'n' : '66', 'o' : '666',
'p' : '7', 'q' : '77', 'r' : '777', 's' : '7777',
't' : '8', 'u' : '88', 'v' : '888',
'w' : '9', 'x' : '99', 'y' : '999', 'z' : '9999'}
    caseTrigger = 0 #lower
    message = list(m)
    for i in range(len(message)):
        if  message[i].isalpha():
            if message[i].islower() and caseTrigger == 0:
                message[i] =  letters.get(message[i])
                if message[i-1][-1] == message[i][0]:
                    message[i] = ' '+message[i]
            elif message[i].islower() and caseTrigger != 0:
                caseTrigger = 0
                message[i] =  '#'+letters.get(message[i])
                if message[i-1][-1] == message[i][0]:
                    message[i] = ' '+message[i]
            elif  message[i].isupper() and caseTrigger == 1:
                message[i] =  letters.get(message[i])
                if message[i-1][-1] == message[i][0]:
                    message[i] = ' '+message[i]
            elif  message[i].isupper() and caseTrigger != 1:
                caseTrigger = 1
                message[i] =  '#'+letters.get(message[i])
                if message[i-1][-1] == message[i][0]:
                    message[i] = ' '+message[i]
        elif bool(message[i].isalpha()) == False:
            message[i] =  letters.get(message[i])
            if message[i-1][-1] == message[i][0]:
                    message[i] = ' '+message[i]

    return ''.join(message).strip(' ')

print(send_message("WW"))
print(send_message("Hello World!"))
