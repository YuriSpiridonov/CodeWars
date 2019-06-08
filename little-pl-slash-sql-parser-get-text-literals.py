# https://www.codewars.com/kata/little-pl-slash-sql-parser-get-text-literals/train/python

import re
def comment_replace(comment):
    return ' '*len(comment)
def one_line_comment_replace(comment):
    return ' '*len(comment)

def get_textliterals(pv_code):
    pv_code = re.sub(r'/\*.*\*/', lambda mo : comment_replace(mo.group()), pv_code)
    pv_code = re.sub(r'(--.*)', lambda mo : one_line_comment_replace(mo.group()), pv_code)
    pv_code = re.sub(r"\'\'", '  ', pv_code)
    results = list()
    while "'" in pv_code:
        start_index = pv_code.index("'")
        pv_code = pv_code[:pv_code.index("'")]+'X'+pv_code[pv_code.index("'")+1:]
        if "'" in pv_code:
            end_index = pv_code.index("'")+1
            pv_code = pv_code[:pv_code.index("'")]+'X'+pv_code[pv_code.index("'")+1:]
        if start_index < end_index:
            indxs = (start_index, end_index)
        else:
            indxs = (start_index, len(pv_code))
        results.append(indxs)        
    return results
