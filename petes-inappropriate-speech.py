# https://www.codewars.com/kata/petes-inappropriate-speech/train/python
# Can't get whats wrong. Tests failings but output is correct.

import re
def replacer(word, ok):
    ok = [words.lower() for words in ok]
    if word.lower() in ok:
        return word
    else:
        return word[0]+(len(word)-2)*'*'+ word[-1]    
def pete_talk(speech, ok=[]):
    print(speech)
    print(ok)
    sentence = re.findall(r'[A-Za-z :;,]*$|[A-Za-z][^\.!?]*[\.!?]', speech)
    for i in range(len(sentence)):
        sentence[i] = re.sub(r'\w{3,}', lambda mo : replacer(mo.group(), ok), sentence[i]).capitalize().lstrip()
    speech = ' '.join(sentence)
    return speech.rstrip()  
