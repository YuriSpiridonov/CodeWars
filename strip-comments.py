# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):
    stringList = string.split('\n')
    for marker in markers:
        for element in stringList:
            index = stringList.index(element)
            if marker in element:
                element = element[:element.find(marker)].rstrip()
                stringList[index] = element
    result = '\n'.join(stringList) 
    return result
#tests
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd") 
