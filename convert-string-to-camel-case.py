# https://www.codewars.com/kata/convert-string-to-camel-case/train/python

import re
def to_camel_case(text):
    lineRegex = re.compile(r'([a-zA-Z]+)') #\w+ = alphabet + _ + 0-9 remember it! _ !
    wordMO = lineRegex.findall(text)
    if len(wordMO) == 0:
        return ''
    returnString = wordMO.pop(0)
    for i in range(len(wordMO)):
        returnString += wordMO[i].title()
    return returnString


print(to_camel_case(''))#, '', "An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior"))#, "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior"))#, "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C"))#, "ABC", "to_camel_case('A-B-C') did not return correct value")  
