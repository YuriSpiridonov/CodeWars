# https://www.codewars.com/kata/master-of-files/train/python

import re
def is_audio(file_name):
    # .mp3, .flac, .alac, or .aac.
    musicExtentions = ['.mp3', '.flac', '.alac', '.aac']
    regexAudio = re.compile(r'''
    ([a-zA-Z]*[^\s0-9\-_])(\.[a-z0-9]+)
    ''', re.VERBOSE)
    mo = regexAudio.findall(file_name)
    try:
        if mo[0][1] in musicExtentions and len(mo[0][0]) == file_name.index('.'):
            return True
        else:
            return False
    except:
        return False

def is_img(file_name):
#    #jpg, .jpeg, .png, .bmp, or .gif.
    imageExtentions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    regexImage = re.compile(r'''
    ([a-zA-Z]*[^\s0-9\-_])(\.[a-z0-9]+)
    ''', re.VERBOSE)
    mo = regexImage.findall(file_name)
    try:
        if mo[0][1] in imageExtentions and len(mo[0][0]) == file_name.index('.'):
            return True
        else:
            return False
    except:
        return False
