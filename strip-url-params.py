# https://www.codewars.com/kata/strip-url-params/train/python

import re
def strip_url_params(url, params_to_strip = []):

    if params_to_strip:
        newUrl = url.split(params_to_strip[0])
        if len(newUrl[0]) == len(url):
            return url
        clearUrl = newUrl[0][:-1]
                
    else:    
        newUrl = url.split('?')
        urlEnd = newUrl[1].split('&')
        regex = re.compile(r'(\w=)+')
        mo = regex.findall(newUrl[1])
        removeDoubles = set(mo)
        newEndUrl = '&'.join(urlEnd[0:len(removeDoubles)])
        clearUrl = newUrl[0]+'?'+newEndUrl
    
    return clearUrl
