# https://www.codewars.com/kata/count-ip-addresses/train/python

def ips_between(start, end):
    number = 0
    startlist = start.split('.')
    endlist = end.split('.')
    number = int(endlist[3])-int(startlist[3])+(int(endlist[2])-int(startlist[2]))*256+(int(endlist[1])-int(startlist[1]))*256*256+(int(endlist[0])-int(startlist[0]))*256*256*256
    return number
