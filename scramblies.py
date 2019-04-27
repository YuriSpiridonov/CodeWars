# https://www.codewars.com/kata/scramblies/train/python
# not elegant solution

def scramble(s1, s2):
    s1dict = dict()
    s1list = list(s1)
    s2list = list(s2)
    word = str()
    for i in range(len(s1list)):
        if s1list[i] not in s1dict:
            s1dict[s1list[i]] = 1
        else:
            s1dict[s1list[i]] += 1
    for i in range(len(s2list)):    
        if s2list[i] in s1dict.keys() and s1dict[s2list[i]] > 0:
            word+=s2list[i]
            s1dict[s2list[i]]-=1      
            i+=1
    return bool(word == s2)
    
print(scramble('rkqodlw', 'world'),  True)
print(scramble('cedewaraaossoqqyt', 'codewars'), True)
print(scramble('katas', 'steak'), False)
print(scramble('scriptjava', 'javascript'), True)
print(scramble('scriptingjava', 'javascript'), True)     
