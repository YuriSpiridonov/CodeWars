# https://www.codewars.com/kata/next-smaller-number-with-the-same-digits/train/python

def next_smaller(n):
    lst = list(str(n))
    templst1half = list()
    templst2half = list()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    for index in range(1,len(lst)+1):
        try:
            if lst[-index] < lst[-(index+1)]:
                templst1half = lst[:-(index+1)]
                templst2half = lst[-(index+1):]
                templst1half.append(templst2half.pop(templst2half.index(max(i for i in templst2half if i < templst2half[0]))))
                templst1half.extend(sorted(templst2half, reverse = True))
                for i in range(len(templst1half)):
                    if templst1half[0] != 0:
                        templst1half[i] = str(templst1half[i])    
                return int(''.join(templst1half))
        except:
            return -1
