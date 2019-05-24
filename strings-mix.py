# https://www.codewars.com/kata/strings-mix/train/python

def custom_key(elems):
    return -len(elems), elems.lower()

def mix(s1, s2):
    s1 = sorted(s1.replace(' ', '').replace(',', '').replace("'", ''))
    s2 = sorted(s2.replace(' ', '').replace(',', '').replace("'", ''))
    s1set = set(s1)
    s2set = set(s2)
    unionset = s1set.union(s2set)
    lst = list()
    for letter in unionset:
        if letter.isalpha() and bool(letter.islower()) == True:
            if s1.count(letter) > 1 or s2.count(letter) > 1:
                if s1.count(letter) > s2.count(letter):
                    lst.append('1:'+str(letter*s1.count(letter)))
                elif s1.count(letter) < s2.count(letter):
                    lst.append('2:'+str(letter*s2.count(letter)))
                elif s1.count(letter) == s2.count(letter):
                    lst.append('=:'+str(letter*s1.count(letter)))
    lst = sorted(lst, key=custom_key)
    return '/'.join(lst)

print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
print(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
print(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
print(mix("codewars", "codewars"), "")
print(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
