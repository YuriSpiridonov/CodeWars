# https://www.codewars.com/kata/range-extraction/train/python
# best shitcode ever

def solution(args):
    lst= list()
    string = str()
    try:
        for i in range(len(args)):
            if args[i]+1 == args[i+1]:
                lst.append(args[i])
                lst.append(args[i+1])
            elif args[i]+1 != args[i+1] and len(lst) > 2:
                temp = str(lst[0])+'-'+str(lst[-1])
                string += temp+','
                lst = []
            elif args[i]+1 != args[i+1] and len(lst) == 2:
                temp = str(lst[0])+','+str(lst[-1])
                string += temp+','
                lst = []
            else:
                string+=str(args[i])+','
    except:
        if len(lst) > 2:
            temp = str(lst[0])+'-'+str(lst[-1])
            string += temp+','
            lst = []
        elif len(lst) == 2:
            temp = str(lst[0])+','+str(lst[-1])
            string += temp+','
            lst = []
        else:
            string+=str(args[i])+','
    return string.rstrip(',')
    
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
