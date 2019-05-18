# https://www.codewars.com/kata/decode-the-morse-code/train/python

def decodeMorse(morse_code):
    morse_code = morse_code.lstrip(' ').rstrip(' ')
    morse_word_list = morse_code.split('   ')
    morse_dict = {'.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D', 
    '.' : 'E', '..-.' : 'F', '--.' : 'G', '....' : 'H', '..' : 'I', 
    '.---' : 'J', '-.-' : 'K', '.-..' : 'L', '--' : 'M', '-.' : 'N', 
    '---' : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R', '...' : 'S', 
    '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'W', '-..-' : 'X', 
    '-.--' : 'Y', '--..' : 'Z', '.----' : '1', '..---' : '2', '...--' : '3', 
    '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8', 
    '----.' : '9', '-----' : '0', 
    '...---...' : 'SOS', '-.-.--' : '!', '.-.-.-' : '.'}

    for word in morse_word_list:
        letters = word.split()
        for i in range(len(letters)):
            for key, value in morse_dict.items():
                if letters[i] in key and len(letters[i]) == len(key):
                    letters[i] = value
        morse_word_list[morse_word_list.index(word)] = ''.join(letters)
    return ' '.join(morse_word_list)
