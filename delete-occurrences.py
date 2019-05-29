# https://www.codewars.com/kata/delete-occurrences-of-an-element-if-it-occurs-more-than-n-times/train/python

def delete_nth(order,max_e):
    deleted = list()
    for element in order:
        if deleted.count(element) < max_e:
            deleted.append(element)           
    return deleted
