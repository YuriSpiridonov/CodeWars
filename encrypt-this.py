# https://www.codewars.com/kata/encrypt-this/train/python

def encrypt_this(text):
    text = text.split(' ')
    for word in text:
        if len(word) > 2:
            text[text.index(word)] = str(ord(word[0]))+word[-1]+word[2:-1]+word[1]
        elif len(word) == 2:
            text[text.index(word)] = str(ord(word[0]))+word[-1]
        elif len(word) == 1:
            text[text.index(word)] = str(ord(word))
    return ' '.join(text)
