# https://www.codewars.com/kata/brainfuck-translator/train/python
# work only with simple tests 

import re
def Countable(element):
    genCountable = {'+' : '*p += X;\n', '-' : '*p -= X;\n',
    '>' : 'p += X;\n', '<' : 'p -= X;\n'}
    return genCountable[element[0]].replace('X', str(len(element)))
def NonCountable(element):
    genNonCountable = {'.' : 'putchar(*p);\n', ',' : '*p = getchar();\n',
    '[' : 'if (*p) do {\n', ']' : '} while (*p);\n'}
    if len(element) > 1:
        lst = list(element)
        for item in lst:
            lst[lst.index(item)] = genNonCountable[item]
        return ''.join(lst)    
    else:        
        return genNonCountable[element]
def tab(temp, y):
    temp = temp.strip(' ').rstrip('\n').split('\n')
    for ind in range(len(temp)):
        temp[ind] = '  '*y+temp[ind]+'\n'
    return ''.join(temp)
def brainfuck_to_c(source_code):
    parsed = list()
    regex = re.sub(r'[^+-<>,.\[\]]', '', source_code)
    while '[]' in regex or '><' in regex or '+-' in regex or '-+' in regex or '<>' in regex:
        regex = re.sub(r'\[\]', '', regex)
        regex = re.sub(r'><', '', regex)
        regex = re.sub(r'\+\-', '', regex)
        regex = re.sub(r'\-\=', '', regex)
        regex = re.sub(r'<>', '', regex)    
    if '[' in regex and ']' not in regex:
        return "Error!"
    elif '[' in regex:
        if regex.index(']') < regex.index('['):
            return "Error!"
    regex2 = re.compile(r'([+]*)([-]*)([\.]*)([,]*)([>]*)([<]*)([\[]*)([\]]*)')
    mo = regex2.findall(regex)    
    for item in mo[:-1]:
        print(item)
        for element in item:
            if element != '':   
                parsed.append(element)
    for item in parsed:
        if item[0] in ['+','-','<','>']:
            parsed[parsed.index(item)] = Countable(item)
        else:
            parsed[parsed.index(item)] = NonCountable(item)
    print(parsed)
    tempstr = ''.join(parsed)
    print(tempstr)
    y=0
    for i in range(len(parsed)):
        if '{' in parsed[i]:
            parsed[i] = tab(parsed[i],y)
            y+=1
        elif '}' in parsed[i]:
            y-=1
            parsed[i] = tab(parsed[i],y)
        else:
            parsed[i] = tab(parsed[i],y)
    return ''.join(parsed)     
