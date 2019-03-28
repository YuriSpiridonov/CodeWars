# https://www.codewars.com/kata/converting-measures/train/python

import re, math

def convert_recipe(recipe):
    tbsp = 15 #g
    tsp = 5 #g
    regex = re.compile(r'''
    ((\d{,}?/?\d+)          # amount
    (\stbsp))            # measurement
    |
    ((\d{,}?/?\d+)          # amount
    (\stsp))             # measurement
    ''', re.VERBOSE)
    mo = regex.findall(recipe)

    for i in range(len(mo)):
        if mo[i][2] == ' tbsp':
            if '/' in (mo[i][1]):
                nem, dem = mo[i][1].split('/')
                number = int(nem)/int(dem)
            else:
                number = int(mo[i][1])
            gramm = math.ceil(number*tbsp)
            grammStr = ' ('+str(round(gramm))+'g)'
            index = recipe.find(mo[i][0])
            recipe = recipe[:index+(len(mo[i][0]))] + grammStr + recipe[index+(len(mo[i][0])):]
        else:
            if '/' in (mo[i][4]):
                nem, dem = mo[i][4].split('/')
                number = int(nem)/int(dem)
            else:
                number = int(mo[i][4])
            gramm = math.ceil(number*tsp)
            grammStr = ' ('+str(round(gramm))+'g)'
            index = recipe.find(mo[i][3])
            recipe = recipe[:index+(len(mo[i][3]))] + grammStr + recipe[index+(len(mo[i][3])):]
    return recipe




print(convert_recipe("19/5 tsp of vanilla extract"))
print(convert_recipe("2 tbsp of butter"))
#, "2 tbsp (30g) of butter")
print(convert_recipe("Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tbsp of dried dill"))
#, "Add to the mixing bowl and coat well with 1 tbsp (15g) of olive oil & 1/2 tbsp (8g) of dried dill")
