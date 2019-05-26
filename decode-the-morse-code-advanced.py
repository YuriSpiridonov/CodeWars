# https://www.codewars.com/kata/decode-the-morse-code-advanced/train/python
# py2.7 
# problems with "Multiple bits per dot handling", cant solve it atm

def decodeBits(bits):
    return bits.replace('111', '-').replace('000', '  ').replace('1', '.').replace('0', '')

def decodeMorse(morseCode):
    morse_dict = {'.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D',
    '.' : 'E', '..-.' : 'F', '--.' : 'G', '....' : 'H', '..' : 'I',
    '.---' : 'J', '-.-' : 'K', '.-..' : 'L', '--' : 'M', '-.' : 'N',
    '---' : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R', '...' : 'S',
    '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'W', '-..-' : 'X',
    '-.--' : 'Y', '--..' : 'Z', '.----' : '1', '..---' : '2', '...--' : '3',
    '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8',
    '----.' : '9', '-----' : '0',
    '...---...' : 'SOS', '-.-.--' : '!', '.-.-.-' : '.'}

    morseCode = morseCode.lstrip(' ').rstrip(' ')
    morse_word_list = morseCode.split('   ')
    for word in morse_word_list:
        letters = word.split()
        for i in range(len(letters)):
            for key, value in morse_dict.items():
                if letters[i] in key and len(letters[i]) == len(key):
                    letters[i] = value
                    break
        morse_word_list[morse_word_list.index(word)] = ''.join(letters)
    return ' '.join(morse_word_list)

print(decodeMorse(decodeBits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110')))
