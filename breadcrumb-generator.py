# https://www.codewars.com/kata/breadcrumb-generator/train/python
# again python 2 !!!

import re
def longElement(ele):
    ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    acronym = str()
    if len(ele) > 30:
        longName = ele.split('-')
        print(longName)
        for word in ignore:
            while word in longName:
                longName.remove(word)
        for words in longName: 
            acronym += words[0]
            ele = acronym
    else:
        ele = ele.replace('-', ' ')
    return ele    

def generate_bc(url, separator):
    parsingRegex = re.compile(r'(?<!/)/([\w\d\-\_]*)+?')
    mo = parsingRegex.findall(url)
    print(mo)   
    if 'index' in mo: mo.pop(mo.index('index'))
    if '' in mo: mo.pop(mo.index(''))
    if mo == []:
        lst = ['<span class="active">HOME</span>',]
    else:
        lst = ['<a href="/">HOME</a>',]
    for i in range(len(mo)):
        if i > 0 and i != len(mo)-1:
            mod += '/'+mo[i]
            if '-' in mo[i]:
                ele = mo[i]
                mo[i] = longElement(ele)    
            element = '<a href="/'+mod+'/">'+mo[i].upper()+'</a>'
            lst.append(element)
        elif i == len(mo)-1:
            if '-' in mo[i]:
                ele = mo[i]
                mo[i] = longElement(ele)
            element = '<span class="active">'+mo[i].upper()+'</span>'
            lst.append(element)    
        else:    
            mod = mo[i]
            if '-' in mo[i]:
                ele = mo[i]
                mo[i] = longElement(ele)    
            element = '<a href="/'+mod+'/">'+mo[i].upper()+'</a>'
            lst.append(element)  
    return separator.join(lst)
    
    
print(generate_bc('https://pippi.pi/profiles/files/for-to-at-bioengineering-a-a-uber-from-for-insider-pippi-or/files#conclusion', ' - '))    
print(generate_bc('https://www.facebook.fr/web/images/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/diplomatic-of-kamehameha-the-at-research-uber-paper-the/secret-page.htm',  ' - '), 'a href="/"&gt;HOME&lt;/a&gt; - &lt;a href="/web/"&gt;WEB&lt;/a&gt; - &lt;a href="/web/images/"&gt;IMAGES&lt;/a&gt; - &lt;a href="/web/images/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/"&gt;PYWYNSBYCUN&lt;/a&gt; - &lt;a href="/web/images/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/diplomatic-of-kamehameha-the-at-research-uber-paper-the/"&gt;DKRUP&lt;/a&gt; - &lt;span class="active"&gt;SECRET PAGE&lt;/span')    
print(generate_bc("https://www.agcpartners.co.uk/to-by-paper-surfer-bladder-for-at-pippi/games/wanted/test.html", " : "))
print(generate_bc("mysite.com/pictures/holidays.html", " : "), '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>')
print(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "), '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>')
print(generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * "), '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>')
print(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "), '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>')
print(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "), '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>')       
