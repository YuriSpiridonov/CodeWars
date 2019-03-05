# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    lst=list(s.lower())
    printstr = ''
    count=0
    for letter in lst:
        printstr+=letter.upper()
        for i in range(count):
            printstr+=letter.lower()
        printstr+='-'
        count+=1
    printstr = printstr.rstrip('-')
    
    return printstr 
